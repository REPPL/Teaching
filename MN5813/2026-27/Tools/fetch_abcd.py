#!/usr/bin/env python3
"""Fetch the abcd project record once and write the individual-report tables.

    python3 Tools/fetch_abcd.py            # fetch, derive, write work/data/abcd/
    python3 Tools/fetch_abcd.py --check    # verify the tables match the manifest
    python3 Tools/fetch_abcd.py --selftest # prove the derivation on a tiny record

The individual report analyses the documented record of abcd, an open-source
tool (MIT licence, github.com/intentdriven/abcd). Nothing is hosted in this
repository: this script clones the repository once at one pinned release tag
and derives ten tables from it (the record files' own fields, the links
between records, the commit history, and the releases) into the student's
work/data/abcd/ folder, where the individual report commits them. Run it once per workstation with network access; every
later run reuses the cached clone and reproduces the same tables byte for
byte, and `--check` proves it.

The source is PINNED. A moving target would give every student a different
dataset, so the tables come from the repository at the tag, never from the
live site (abcdev.app shows the same record, and its graph view is a good
way to explore it, but it moves with every release). The manifest records
the tag, the commit and the SHA-256 of every output. Change the pin only by
editing PINNED below and telling the cohort.

Tables written (gzipped CSV; the primer in Assessment/abcd-record.md
describes every column):

    issues.csv.gz        one row per issue record
    intents.csv.gz       one row per intent record
    specs.csv.gz         one row per spec record
    decisions.csv.gz     one row per architecture decision record
    releases.csv.gz      one row per release
    commits.csv.gz       one row per commit
    commit_files.csv.gz  one row per file touched by a commit
    nodes.csv.gz         one row per record, as a node of the link graph
    edges.csv.gz         one row per typed link between records
    mentions.csv.gz      one row per untyped mention of one record by another

Needs git and the delivery's Python environment (pandas). Standard library
otherwise. Never run at marking time on a different pin than the students'.
"""
from __future__ import annotations

import argparse
import csv
import gzip
import hashlib
import io
import json
import os
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from typing import NoReturn

def find_work(tools: pathlib.Path) -> pathlib.Path:
    """The work/ folder the fetched data goes in.

    Published, work/ sits at the root of the student's repository, two
    folders above Tools/ (<repo>/<module>/<year>/Tools); in the source tree it
    sits beside Tools/. So walk up from Tools/ to the first folder that holds
    a work/ folder, stopping at the repository root (the folder that holds
    .git), whose work/ is used even before it exists.
    """
    for folder in tools.parents:
        if (folder / "work").is_dir() or (folder / ".git").exists():
            return folder / "work"
    return tools.parent / "work"


HERE = pathlib.Path(__file__).resolve().parent
# The data lives in the student's work/ folder, never in Tools/: find_work()
# says where that is. OLD_DIR is where earlier versions wrote; the next run
# moves a copy found there across.
WORK = find_work(HERE)
OUT_DIR = WORK / "data" / "abcd"
OLD_DIR = HERE / "data" / "abcd"
# The clone is scratch, not data: it lives in the user's cache directory,
# outside the delivery, so no documentation lint or publisher walk under
# materials/ ever meets a second repository's files. Override with
# FETCH_ABCD_CACHE to put it elsewhere.
CACHE_DIR = pathlib.Path(os.environ.get("FETCH_ABCD_CACHE")
                         or pathlib.Path.home() / ".cache" / "mn5813-fetch" / "abcd")

PINNED = {
    "repository": "https://github.com/intentdriven/abcd",
    "tag": "v0.8.0",
    # A site export committed at the tag would be read if present; the tag
    # carries none, so the graph is built from the record files themselves,
    # which is what makes the derivation reproducible from the tag alone.
    "export_path": "site/record.json",
}

RECORD_DIRS = {
    "issue": [".abcd/work/issues/open", ".abcd/work/issues/resolved", ".abcd/work/issues/wontfix"],
    "intent": [".abcd/development/intents/drafts", ".abcd/development/intents/planned",
               ".abcd/development/intents/shipped", ".abcd/development/intents/superseded",
               ".abcd/development/intents/disciplines"],
    "spec": [".abcd/development/specs/open", ".abcd/development/specs/closed"],
    "adr": [".abcd/development/decisions/adrs"],
}
ID_RE = re.compile(r"\b(?:iss|itd|spc|adr)-\d+\b")
STAMP_RE = re.compile(r"^(?:iss|itd|spc)-(\d{16})$")
CONVENTIONAL_RE = re.compile(r"^(feat|fix|docs|chore|refactor|test|build|ci|perf|style|revert)(\(|:|!)")


# --- helpers ----------------------------------------------------------------

def sha256_of(path: pathlib.Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def say(msg: str) -> None:
    print(msg, flush=True)


def show(path: pathlib.Path) -> str:
    """*path* as the pages name it: from the folder that holds work/ or Tools/."""
    for base in (WORK.parent, HERE.parent):
        if path.is_relative_to(base):
            return path.relative_to(base).as_posix()
    return str(path)


def move_old_data(old: pathlib.Path, new: pathlib.Path) -> None:
    """Move tables an earlier version wrote under Tools/data/ to work/data/,
    so nobody downloads them again. When both exist, the new copy wins."""
    if old.is_dir() and not new.exists():
        new.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(old), str(new))
        say(f"moved {show(old)}/ to {show(new)}/ (the data now lives in work/)")
        try:
            old.parent.rmdir()  # Tools/data/, once nothing else is in it
        except OSError:
            pass
    elif old.is_dir():
        say(f"note: {show(new)}/ is in use; the older copy in {show(old)}/ can be deleted")


def fail(msg: str, code: int = 1) -> NoReturn:
    print(f"fetch_abcd: {msg}", file=sys.stderr)
    sys.exit(code)


def parse_frontmatter(text: str) -> tuple[dict, str]:
    """A tolerant reader for the `---` block: scalars, quoted scalars, and
    simple lists (inline `[a, b]` or `- item` lines). Enough for the record."""
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end < 0:
        return {}, text
    block, body = text[3:end], text[end + 4:]
    fields: dict = {}
    key = None
    for line in block.split("\n"):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if line.startswith((" ", "\t")) and key is not None:
            item = line.strip()
            if item.startswith("- "):
                fields.setdefault(key, [])
                if not isinstance(fields[key], list):
                    fields[key] = []
                fields[key].append(_scalar(item[2:]))
            continue
        if ":" not in line:
            continue
        key, _, raw = line.partition(":")
        key = key.strip()
        raw = raw.strip()
        if raw == "":
            fields[key] = []
        elif raw.startswith("[") and raw.endswith("]"):
            fields[key] = [_scalar(x) for x in raw[1:-1].split(",") if x.strip()]
        else:
            fields[key] = _scalar(raw)
    return fields, body


def _scalar(raw: str):
    raw = raw.strip()
    if len(raw) >= 2 and raw[0] == raw[-1] and raw[0] in "\"'":
        return raw[1:-1]
    if raw in ("null", "~", "None"):
        return ""
    return raw


def to_naive_utc(iso: str) -> str:
    """A git date like 2026-08-22T13:42:50+01:00 as naive UTC, the same
    shape the id stamps decode to, so one column holds one kind of time."""
    if not iso:
        return ""
    try:
        dt = datetime.fromisoformat(iso)
    except ValueError:
        return iso
    if dt.tzinfo is not None:
        dt = dt.astimezone(timezone.utc).replace(tzinfo=None)
    return dt.isoformat(timespec="seconds")


def stamp_to_iso(record_id: str) -> str:
    m = STAMP_RE.match(record_id)
    if not m:
        return ""
    s = m.group(1)
    try:
        return datetime(2000 + int(s[0:2]), int(s[2:4]), int(s[4:6]), int(s[6:8]),
                        int(s[8:10]), int(s[10:12])).isoformat()
    except ValueError:
        return ""


# --- fetch --------------------------------------------------------------------

def clone_at_tag(repo: str, tag: str, dest: pathlib.Path) -> str:
    """Clone the repository at the tag with full history (the commit table
    needs it). Returns the commit the tag points at."""
    if dest.exists():
        head = subprocess.run(["git", "-C", str(dest), "rev-parse", "HEAD"],
                              capture_output=True, text=True)
        if head.returncode == 0:
            say(f"reusing cached clone at {dest}")
            return head.stdout.strip()
        shutil.rmtree(dest)
    say(f"cloning {repo} at {tag} ...")
    done = subprocess.run(["git", "clone", "--quiet", "--branch", tag, repo, str(dest)],
                          capture_output=True, text=True)
    if done.returncode != 0:
        tail = (done.stderr.strip().splitlines() or ["(no output)"])[-1]
        fail(f"could not clone {repo} at {tag}: {tail}\n"
             f"  This needs network access. Run the script again when you are online.", 2)
    head = subprocess.run(["git", "-C", str(dest), "rev-parse", "HEAD"], capture_output=True, text=True)
    return head.stdout.strip()


# --- derive ---------------------------------------------------------------------

def read_records(root: pathlib.Path) -> dict[str, list[dict]]:
    out: dict[str, list[dict]] = {k: [] for k in RECORD_DIRS}
    for kind, dirs in RECORD_DIRS.items():
        for d in dirs:
            folder = root / d
            if not folder.is_dir():
                continue
            for path in sorted(folder.glob("*.md")):
                if path.name.upper() == "README.MD":
                    continue  # a folder's own readme, not a record
                text = path.read_text(encoding="utf-8", errors="replace")
                fields, body = parse_frontmatter(text)
                rec: dict = {"id": str(fields.get("id") or (path.stem.split("-")[0] + "-" + path.stem.split("-")[1]
                                                            if path.stem.count("-") else path.stem))}
                rec["bucket"] = folder.name if kind != "adr" else ""
                rec["path"] = str(path.relative_to(root))
                title = next((l[2:].strip() for l in body.split("\n") if l.startswith("# ")), "")
                rec["title"] = title
                rec["body_words"] = len(body.split())
                rec["created_from_id"] = stamp_to_iso(rec["id"])
                for k, v in fields.items():
                    if k in ("id",):
                        continue
                    rec[k] = "; ".join(str(x) for x in v) if isinstance(v, list) else str(v)
                rec["mentions"] = "; ".join(sorted({m for m in ID_RE.findall(body) if m != rec["id"]}))
                out[kind].append(rec)
    return out


def git_dates(root: pathlib.Path, paths: list[str]) -> dict[str, tuple[str, str]]:
    """(first commit date, last commit date) per path, one git call."""
    first: dict[str, str] = {}
    last: dict[str, str] = {}
    log = subprocess.run(["git", "-C", str(root), "log", "--format=%x00%aI", "--name-only",
                          "--find-renames", "--", *paths], capture_output=True, text=True)
    stamp = ""
    for line in log.stdout.split("\n"):
        if line.startswith("\x00"):
            stamp = line[1:]
        elif line.strip():
            last.setdefault(line.strip(), stamp)
            first[line.strip()] = stamp
    return {p: (first.get(p, ""), last.get(p, "")) for p in paths}


def read_commits(root: pathlib.Path) -> tuple[list[dict], list[dict]]:
    log = subprocess.run(["git", "-C", str(root), "log", "--format=%x00%H|%aI|%an|%s|%P", "--numstat"],
                         capture_output=True, text=True)
    commits: list[dict] = []
    files: list[dict] = []
    cur = None
    for line in log.stdout.split("\n"):
        if line.startswith("\x00"):
            sha, ts, author, subject, parents = line[1:].split("|", 4)
            m = CONVENTIONAL_RE.match(subject)
            cur = {"sha": sha, "timestamp": to_naive_utc(ts), "author": author, "prefix": m.group(1) if m else "",
                   "subject": subject, "is_merge": len(parents.split()) > 1,
                   "record_ids": "; ".join(sorted(set(ID_RE.findall(subject)))),
                   "files_changed": 0, "insertions": 0, "deletions": 0}
            commits.append(cur)
        elif line.strip() and cur is not None:
            parts = line.split("\t")
            if len(parts) == 3:
                ins = int(parts[0]) if parts[0].isdigit() else 0
                dele = int(parts[1]) if parts[1].isdigit() else 0
                cur["files_changed"] += 1
                cur["insertions"] += ins
                cur["deletions"] += dele
                files.append({"sha": cur["sha"], "path": parts[2], "insertions": ins, "deletions": dele})
    return commits, files


MAINTAINER_ALIASES = {"REPPL", "Alex Reppel"}   # the maintainer's two git names, kept as they are
BOT_MARKERS = ("[bot]", "dependabot", "Claude", "github-actions")


def pseudonymise(commits: list[dict]) -> None:
    """Human authors other than the maintainer become contributor-1,
    contributor-2, ... in order of first appearance. The maintainer keeps both
    spellings of one name (a deliberate cleaning step for the student), and
    bots keep their names because a bot is not a person."""
    seen: dict[str, str] = {}
    for c in commits:
        a = c["author"]
        if a in MAINTAINER_ALIASES or any(m in a for m in BOT_MARKERS):
            continue
        if a not in seen:
            seen[a] = f"contributor-{len(seen) + 1}"
        c["author"] = seen[a]


def read_releases(root: pathlib.Path) -> list[dict]:
    tags = subprocess.run(["git", "-C", str(root), "for-each-ref", "--sort=creatordate",
                           "--format=%(refname:short)|%(creatordate:iso-strict)", "refs/tags"],
                          capture_output=True, text=True)
    rows = [line.split("|", 1) for line in tags.stdout.split("\n") if "|" in line]
    # A fresh clone also fetches the tags made after the pin: Keep only the
    # releases dated up to the pinned tag, so every clone gives the same table.
    pinned = dict(rows).get(PINNED["tag"])
    if pinned:
        when = datetime.fromisoformat
        rows = [(tag, date) for tag, date in rows if when(date) <= when(pinned)]
    return [{"version": tag.lstrip("v"), "tag": tag, "date": date[:10]} for tag, date in rows]


def read_export(root: pathlib.Path) -> "dict | None":
    p = root / PINNED["export_path"]
    if not p.is_file():
        return None
    return json.loads(p.read_text(encoding="utf-8"))


def graph_tables(export: "dict | None", records: dict[str, list[dict]]) -> tuple[list[dict], list[dict], list[dict]]:
    if export:
        nodes = [{"id": n.get("id", ""), "type": n.get("type", ""), "lifecycle": n.get("lifecycle", ""),
                  "title": n.get("title", ""), "status": n.get("status", ""), "date": n.get("date", ""),
                  "created": (n.get("dates") or {}).get("created", ""),
                  "entered": (n.get("dates") or {}).get("entered", ""),
                  "degree": n.get("degree", "")} for n in export.get("nodes", [])]
        edges = [{"from": e.get("from", ""), "to": e.get("to", ""), "rel": e.get("rel", "")} for e in export.get("edges", [])]
        mentions = [{"from": m.get("from", ""), "to": m.get("to", "")} for m in export.get("mentions", [])]
        return nodes, edges, mentions
    # No export at the tag: build the graph from the record files.
    nodes, edges, mentions = [], [], []
    for kind, recs in records.items():
        for r in recs:
            nodes.append({"id": r["id"], "type": kind, "lifecycle": r.get("bucket", ""), "title": r.get("title", ""),
                          "status": r.get("status", ""), "date": r.get("date", ""), "created": "", "entered": "", "degree": ""})
            for rel in ("builds_on", "blocked_by", "supersedes", "related"):
                for target in [x for x in r.get(rel, "").split("; ") if x]:
                    edges.append({"from": r["id"], "to": target, "rel": rel})
            if r.get("spec_id"):
                edges.append({"from": r["spec_id"], "to": r["id"], "rel": "implements"})
            for target in [x for x in r.get("mentions", "").split("; ") if x]:
                mentions.append({"from": r["id"], "to": target})
    return nodes, edges, mentions


def derive(root: pathlib.Path) -> dict[str, list[dict]]:
    records = read_records(root)
    paths = [r["path"] for recs in records.values() for r in recs]
    dates = git_dates(root, paths)
    for recs in records.values():
        for r in recs:
            first, last = (to_naive_utc(x) for x in dates.get(r["path"], ("", "")))
            r["first_commit"] = first
            r["last_commit"] = last
            r["created_at"] = r["created_from_id"] or first
            r["created_source"] = "id" if r["created_from_id"] else "git"
    commits, files = read_commits(root)
    pseudonymise(commits)
    nodes, edges, mentions = graph_tables(read_export(root), records)
    return {
        "issues": records["issue"], "intents": records["intent"], "specs": records["spec"],
        "decisions": records["adr"], "releases": read_releases(root),
        "commits": commits, "commit_files": files, "nodes": nodes, "edges": edges, "mentions": mentions,
    }


# --- write ------------------------------------------------------------------------

def write_table(rows: list[dict], path: pathlib.Path) -> tuple[int, str]:
    columns: list[str] = []
    for r in rows:
        for k in r:
            if k not in columns:
                columns.append(k)
    buf = io.StringIO()
    w = csv.DictWriter(buf, fieldnames=columns, extrasaction="ignore", lineterminator="\n")
    w.writeheader()
    for r in sorted(rows, key=lambda r: json.dumps(r, sort_keys=True)):
        w.writerow({k: r.get(k, "") for k in columns})
    data = buf.getvalue().encode("utf-8")
    # mtime pinned to zero so the gzip bytes are reproducible.
    with gzip.GzipFile(filename="", mode="wb", fileobj=path.open("wb"), mtime=0) as gz:
        gz.write(data)
    return len(rows), sha256_of(path)


def run_fetch(out_dir: pathlib.Path = OUT_DIR, cache_dir: pathlib.Path = CACHE_DIR) -> int:
    if shutil.which("git") is None:
        fail("git is not installed; the commit history comes from git", 2)
    cache_dir.mkdir(parents=True, exist_ok=True)
    clone = cache_dir / f"abcd-{PINNED['tag']}"
    commit = clone_at_tag(PINNED["repository"], PINNED["tag"], clone)
    say("deriving tables ...")
    tables = derive(clone)
    out_dir.mkdir(parents=True, exist_ok=True)
    manifest = {
        "dataset": "abcd project record", "licence": "MIT (Copyright 2026 Alex Reppel)",
        "source": PINNED["repository"], "tag": PINNED["tag"], "commit": commit,
        "export": PINNED["export_path"] if (clone / PINNED["export_path"]).is_file() else "built from record files",
        "fetched_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "tables": {},
    }
    for name, rows in tables.items():
        path = out_dir / f"{name}.csv.gz"
        n, digest = write_table(rows, path)
        manifest["tables"][name] = {"file": path.name, "rows": n, "sha256": digest}
        say(f"  wrote {show(path)}  ({n} rows)")
    (out_dir / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    say(f"wrote {show(out_dir / 'manifest.json')}")
    say(f"done: {PINNED['tag']} ({commit[:8]}), {len(tables)} tables under {show(out_dir)}")
    return 0


def run_check(out_dir: pathlib.Path = OUT_DIR) -> int:
    mpath = out_dir / "manifest.json"
    if not mpath.is_file():
        fail(f"no manifest at {mpath}; run the script without --check first", 1)
    manifest = json.loads(mpath.read_text(encoding="utf-8"))
    bad = 0
    for meta in manifest["tables"].values():
        path = out_dir / meta["file"]
        if not path.is_file():
            say(f"MISSING {meta['file']}")
            bad += 1
        elif sha256_of(path) != meta["sha256"]:
            say(f"CHANGED {meta['file']} (does not match the manifest)")
            bad += 1
        else:
            say(f"ok      {meta['file']}  ({meta['rows']} rows)")
    if manifest.get("tag") != PINNED["tag"]:
        say(f"PIN     manifest is for {manifest.get('tag')}, this script pins {PINNED['tag']}: re-run without --check")
        bad += 1
    say("all tables match the manifest" if not bad else f"{bad} problem(s)")
    return 1 if bad else 0


# --- selftest ------------------------------------------------------------------------

def selftest() -> int:
    """Derive from a tiny synthetic repository and prove the tables, the
    reproducibility, and the check."""
    fails = 0

    def expect(name: str, ok: bool, detail: str = "") -> None:
        nonlocal fails
        print(("  ✓ " if ok else "  ✗ ") + name)
        if not ok:
            fails += 1
            if detail:
                print("      " + detail[:400])

    with tempfile.TemporaryDirectory(prefix="fetch-abcd-selftest-") as tmp:
        repo = pathlib.Path(tmp) / "repo"
        for d in [x for xs in RECORD_DIRS.values() for x in xs]:
            (repo / d).mkdir(parents=True, exist_ok=True)
        (repo / ".abcd/work/issues/open/iss-1-first.md").write_text(
            '---\nid: "iss-1"\nseverity: "major"\ncategory: "bug"\nsource: "user-observation"\n'
            'found_at: "cmd/main.go"\n---\n\n# first issue\n\nRelates to itd-1.\n', encoding="utf-8")
        (repo / ".abcd/work/issues/resolved/iss-2609010101010101-second.md").write_text(
            '---\nid: "iss-2609010101010101"\nseverity: "minor"\ncategory: "docs"\nresolution: "fixed"\n---\n\n# second\n', encoding="utf-8")
        (repo / ".abcd/development/intents/planned/itd-1-thing.md").write_text(
            "---\nid: itd-1\nspec_id: spc-1\nbuilds_on:\n  - itd-0\nimpact: additive\n---\n\n# A thing\n", encoding="utf-8")
        (repo / ".abcd/development/specs/open/spc-1-thing.md").write_text(
            "---\nid: spc-1\nintent: itd-1\n---\n\n# spec\n", encoding="utf-8")
        (repo / ".abcd/development/decisions/adrs/0001-x.md").write_text(
            "---\nid: adr-1\nstatus: accepted\ndate: 2026-05-04\n---\n\n# ADR-1: x\n", encoding="utf-8")
        env = {**os.environ, "GIT_AUTHOR_NAME": "probe", "GIT_AUTHOR_EMAIL": "p@example.com",
               "GIT_COMMITTER_NAME": "probe", "GIT_COMMITTER_EMAIL": "p@example.com"}
        def git(*a):
            return subprocess.run(["git", "-C", str(repo), *a], capture_output=True, text=True, env=env)
        git("init", "-q"); git("add", "."); git("commit", "-q", "-m", "feat: first (itd-1)")
        (repo / "README.md").write_text("hi\n"); git("add", "."); git("commit", "-q", "-m", "docs: readme")
        git("tag", "v0.0.1")
        tables = derive(repo)
        expect("issues table has both issues", len(tables["issues"]) == 2)
        iss = {r["id"]: r for r in tables["issues"]}
        expect("timestamp id decodes to created_at", iss["iss-2609010101010101"]["created_at"] == "2026-09-01T01:01:01")
        expect("sequential id falls back to git date", iss["iss-1"]["created_source"] == "git" and iss["iss-1"]["created_at"])
        expect("bucket comes from the folder", iss["iss-1"]["bucket"] == "open" and iss["iss-2609010101010101"]["bucket"] == "resolved")
        expect("mentions are extracted from the body", iss["iss-1"]["mentions"] == "itd-1")
        expect("frontmatter list joins with '; '", tables["intents"][0]["builds_on"] == "itd-0")
        expect("commits carry prefix and record ids", tables["commits"][0]["prefix"] == "docs" and tables["commits"][1]["record_ids"] == "itd-1")
        expect("timestamps are naive UTC (no zone suffix)", all(c["timestamp"][-6] not in "+-" and "T" in c["timestamp"] for c in tables["commits"]), str(tables["commits"][0]["timestamp"]))
        expect("a non-maintainer author is pseudonymised", tables["commits"][0]["author"] == "contributor-1", tables["commits"][0]["author"])
        expect("commit_files has rows", len(tables["commit_files"]) >= 6)
        expect("releases from tags", tables["releases"] == [{"version": "0.0.1", "tag": "v0.0.1", "date": tables["releases"][0]["date"]}] and len(tables["releases"][0]["date"]) == 10)
        expect("graph built from record files when no export", any(e["rel"] == "implements" for e in tables["edges"]) and any(e["rel"] == "builds_on" for e in tables["edges"]))
        out = pathlib.Path(tmp) / "out"; out.mkdir()
        a = {n: write_table(rows, out / f"{n}.csv.gz")[1] for n, rows in tables.items()}
        b = {n: write_table(rows, out / f"{n}.csv.gz")[1] for n, rows in tables.items()}
        expect("writing twice gives identical bytes", a == b)
        manifest = {"tag": PINNED["tag"], "tables": {n: {"file": f"{n}.csv.gz", "rows": len(tables[n]), "sha256": a[n]} for n in tables}}
        (out / "manifest.json").write_text(json.dumps(manifest))
        expect("--check passes on matching tables", run_check(out) == 0)
        (out / "issues.csv.gz").write_bytes(b"changed")
        expect("--check fails on a changed table", run_check(out) == 1)
    with tempfile.TemporaryDirectory(prefix="fetch-abcd-selftest-work-") as tmp:
        repo = pathlib.Path(tmp)
        (repo / ".git").mkdir()
        tools = repo / "MOD" / "2000-01" / "Tools"
        tools.mkdir(parents=True)
        expect("work/ is found at the repository root, before it exists", find_work(tools) == repo / "work")
        (repo / "work").mkdir()
        expect("work/ is found two folders above Tools/", find_work(tools) == repo / "work")
        old, new = tools / "data" / "abcd", repo / "work" / "data" / "abcd"
        old.mkdir(parents=True)
        (old / "manifest.json").write_text("{}")
        move_old_data(old, new)
        expect("an old Tools/data copy moves to work/data", (new / "manifest.json").is_file() and not (tools / "data").exists())
    print("\nselftest: " + ("all checks passed" if not fails else f"{fails} failed"))
    return 1 if fails else 0


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--check", action="store_true", help="verify the written tables match the manifest")
    p.add_argument("--selftest", action="store_true", help="prove the derivation on a tiny synthetic record")
    a = p.parse_args()
    if a.selftest:
        return selftest()
    move_old_data(OLD_DIR, OUT_DIR)
    if a.check:
        return run_check()
    return run_fetch()


if __name__ == "__main__":
    sys.exit(main())
