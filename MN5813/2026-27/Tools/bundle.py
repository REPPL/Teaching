#!/usr/bin/env python3
"""Ship-it bundler: plain stdlib, no install, executes nothing.

Builds the checkpoint/final zip you upload to Moodle: your shared payload
files plus one manifest.json (file list, sha256 checksums, week, your group
or candidate ID (never names), tool versions, and your AIAS declaration
level). Checksums verify *transfer*, never students. The moment the zip is
written you get a local receipt: your work is safe and yours.

Ship-it:

    python3 bundle.py --lc LC1 --week 4 --id G01 [--aias 3] [path]

Portfolio assembly, where a module asks for one:

    python3 bundle.py --portfolio --id P401001 --excerpts a.md b.md c.md

Notes:
- The zip name is deterministic: submission-wkNN-<id>-<UTC>.zip.
- Your record is NEVER bundled: `.specstory/`, transcript folders, `retro.md`
  and `standup.md` are all excluded. They stay with you. If your module wants
  any of them, it asks for them separately and tells you how. This tool will
  not put them in a zip on your behalf.
- Record content that was actually there (`.specstory/`, `transcripts/`,
  `retro.md`, `standup.md`) is named when the zip is written, so leaving it
  out is a decision you make rather than a surprise later. The tools
  themselves, the generated manifest, prior zips and `.pyc` files are
  excluded silently: nobody expects those in a submission.
- This tool never runs your notebook and never touches the network.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import sys
import zipfile
from datetime import datetime, timezone
from pathlib import Path

BUNDLE_PY_VERSION = "1.0"

CANDIDATE_ID_RE = re.compile(r"^P[0-9]{4,8}$")
GROUP_ID_RE = re.compile(r"^G[0-9]{2,4}$")
LC_RE = re.compile(r"^(LC[1-9][0-9]?|final)$")

#: directories never bundled (transcripts, VCS internals, tool output).
EXCLUDED_DIRS = frozenset({
    ".git", ".specstory", ".ipynb_checkpoints", "__pycache__",
    "local-receipts", "portfolio", "transcripts",
})
#: individual files never bundled (team-only ceremony files, the tools).
EXCLUDED_FILES = frozenset({
    "manifest.json", "check.py", "bundle.py", "retro.md", "standup.md",
})
#: extensions never bundled.
EXCLUDED_SUFFIXES = frozenset({".zip", ".pyc"})

#: record and ceremony names, matched case-folded: on the case-insensitive
#: filesystems most students run, Transcripts/ IS transcripts/, and the
#: promise that the record never ships must not hang on a capital letter.
#: Tool-output and tool-file names stay byte-exact: a student's own
#: Portfolio/ or Check.py is their work, and folding an unreported name
#: would swallow it silently.
RECORD_DIRS = frozenset({".specstory", "transcripts"})
RECORD_FILES = frozenset({"retro.md", "standup.md"})


def utc_stamp() -> str:
    """Current UTC time as the zip-name stamp (YYYYMMDDTHHMMSSZ)."""
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def utc_iso() -> str:
    """Current UTC time as an ISO-8601 timestamp."""
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def sha256_file(path: Path) -> str:
    """SHA-256 hex digest of *path* (streamed)."""
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def valid_submission_id(value: str) -> bool:
    """True for a candidate ID (P…) or group ID (G…). Never a name."""
    return bool(CANDIDATE_ID_RE.match(value) or GROUP_ID_RE.match(value))


def _excluded_dir(part: str) -> bool:
    """Whether one path component names a directory the walk excludes."""
    return (part in EXCLUDED_DIRS or part.lower() in RECORD_DIRS
            or part.startswith("."))


def _included(rel_parts: tuple[str, ...]) -> bool:
    """Whether a file at *rel_parts* (relative path parts) is bundled."""
    if any(_excluded_dir(part) for part in rel_parts):
        return False
    name = rel_parts[-1]
    if name in EXCLUDED_FILES or name.lower() in RECORD_FILES:
        return False
    suffix = Path(name).suffix.lower()
    return suffix not in EXCLUDED_SUFFIXES


#: Excluded content a student could reasonably expect to find in the zip. The
#: tools themselves (check.py, bundle.py), the generated manifest and prior
#: zips are excluded too, but nobody is surprised by that, so naming them would
#: be noise that buries the ones that matter. The register applies the walk's
#: own predicate per kind: a directory is reported only under a record
#: DIRECTORY name, because a directory wearing a record FILE name (retro.md/)
#: is the student's own folder: the walk bundles it, so naming it "not
#: bundled" would be false. A file is reported under either kind of name:
#: the walk excludes a file named transcripts through the directory predicate
#: on its last component, and dropping the report would leave that exclusion
#: silent.
REPORTED_EXCLUSIONS = frozenset({
    ".specstory", "transcripts", "retro.md", "standup.md",
})


def excluded_content(root: Path) -> list[str]:
    """Excluded record and ceremony content that is actually present.

    Leaving it out is right: a student's record is theirs, and nothing here
    ships it anywhere by accident. But it must not be SILENT, for the same
    reason out_of_tree_links is not: a team whose Stoa exports live in
    transcripts/ can otherwise build a checkpoint zip with none of the evidence
    in it and be told their work is safe.

    An empty excluded directory is not reported (nothing is being left out),
    and a directory is named once rather than once per file inside it.
    """
    found: list[str] = []
    reported_dirs: list[tuple[str, ...]] = []
    for path in sorted(root.rglob("*")):
        rel = path.relative_to(root)
        parts = rel.parts
        if any(parts[:len(d)] == d for d in reported_dirs):
            continue  # inside a directory already named
        if path.is_dir():
            if parts[-1].lower() in RECORD_DIRS and any(
                    p.is_file() for p in path.rglob("*")):
                found.append(rel.as_posix() + "/")
                reported_dirs.append(parts)
        elif path.is_file() and parts[-1].lower() in REPORTED_EXCLUSIONS:
            found.append(rel.as_posix())
    return found


def _link_escapes(root: Path, path: Path) -> bool:
    """True for a symlink whose target lies outside the project folder.

    A broken link is False: it carries nothing to bundle or lose.
    """
    if not path.is_symlink():
        return False
    try:
        target = path.resolve(strict=True)
    except (OSError, RuntimeError):
        # ELOOP is RuntimeError on Python <= 3.12, OSError from 3.13.
        return False
    return target != root and root not in target.parents


def out_of_tree_links(root: Path) -> list[Path]:
    """Symlinks under *root* whose target lies outside the project.

    Neither side of such a link is bundled: rglob does not descend into a
    directory symlink, and collect_payload skips a file symlink resolving
    outside the project, the same policy that refuses an explicit --files
    path escaping the project folder. Leaving OUT-OF-TREE content out is
    right, but it must not be SILENT, because this tool tells the student
    their work is safe. The files behind the link are missing from the zip
    AND from manifest.json, so the marker's checksum verification has nothing
    to compare and reports nothing either.

    A link that resolves back INSIDE the project is not reported HERE: a
    file link's bytes are bundled (or refused) on their own path, and a
    directory link's files are bundled under their real path, but the path
    THROUGH a directory link's name is lost, which is in_project_dir_links's
    case, not this one. A file link the payload walk excludes by NAME is not
    reported either: a real file at that path would be left out just the
    same, so the copy-it-in remedy cannot change the outcome, and an excluded
    name in REPORTED_EXCLUSIONS gets its one warning (with the true reason)
    from excluded_content.
    """
    links: list[Path] = []
    for path in sorted(root.rglob("*")):
        rel_parts = path.relative_to(root).parts
        if path.is_dir():
            # A directory link's loss is its contents, bundled under any
            # non-excluded directory name, so only the directory arm applies.
            if any(_excluded_dir(part) for part in rel_parts):
                continue
        elif not _included(rel_parts):
            continue
        if _link_escapes(root, path):
            links.append(path)
    return links


def _link_target_excluded(root: Path, path: Path) -> bool:
    """True for a file symlink whose in-project target the walk excludes.

    is_file() follows links, so without this a link named notes.md would ship
    the bytes behind transcripts/session1.md (content _included refuses on
    its own path), hashed into manifest.json as the student's own work, while
    excluded_content says in the same run that the record is never bundled.
    An out-of-tree target is _link_escapes's case, not this one.
    """
    if not path.is_symlink():
        return False
    try:
        target = path.resolve(strict=True)
    except (OSError, RuntimeError):
        # ELOOP is RuntimeError on Python <= 3.12, OSError from 3.13.
        return False
    if target == root or root not in target.parents:
        return False
    return not _included(target.relative_to(root).parts)


def excluded_target_links(root: Path) -> list[Path]:
    """File links the walk would bundle whose in-project target it excludes.

    collect_payload skips them, which is right, but never SILENTLY, for the
    same reason out_of_tree_links is not silent: the student is about to be
    told their work is safe, and a link that pointed at excluded content must
    not be a quiet exception to the words describing it.
    """
    return [
        path for path in sorted(root.rglob("*"))
        if path.is_file() and _included(path.relative_to(root).parts)
        and not _link_escapes(root, path)
        and _link_target_excluded(root, path)
    ]


def in_project_dir_links(root: Path) -> list[Path]:
    """Directory links resolving inside the project whose contents bundle.

    The payload walk never descends into a directory link and the link
    itself is not a file, so its files ship only under the target's real
    path: every path THROUGH the link name is absent from the zip while the
    student's notebook reads through it locally. The bytes survive, the path
    does not, and the marking tools address a submission by path, so a
    notebook reading data/sales.csv through data -> datasets fails at
    marking time over a bundling artefact. Named here, never bundled twice:
    a link resolving to the project root would recurse, and duplicate bytes
    count against the marker's caps.

    A link at an excluded path is not reported (nothing under it would ship
    from there anyway). A link whose TARGET is excluded is also left alone:
    its content ships under neither name by policy, so there is no shipped
    real path to redirect the student to. A target named in
    REPORTED_EXCLUSIONS draws excluded_content's warning (naming the
    target, never the link); other excluded targets (VCS internals,
    caches, tool output and dot-folders) draw none. An out-of-tree
    target is out_of_tree_links's case, and a broken link carries
    nothing to bundle or lose.
    """
    links: list[Path] = []
    for path in sorted(root.rglob("*")):
        if not path.is_symlink() or not path.is_dir():
            continue
        rel_parts = path.relative_to(root).parts
        if any(_excluded_dir(part) for part in rel_parts):
            continue
        try:
            target = path.resolve(strict=True)
        except (OSError, RuntimeError):
            # ELOOP is RuntimeError on Python <= 3.12, OSError from 3.13.
            continue
        if target != root and root not in target.parents:
            continue
        if target != root and any(_excluded_dir(part)
                                  for part in target.relative_to(root).parts):
            continue
        links.append(path)
    return links


#: The marker's ingest refuses a bundle above these caps and then treats it
#: exactly like an unreadable archive. Mirrored here rather than imported
#: because bundle.py ships to students and depends on nothing; the marker's
#: own test suite asserts the two stay equal.
MAX_BUNDLE_FILES = 2000
MAX_BUNDLE_TOTAL_BYTES = 256 << 20


def _payload_shares(root: Path, payload: list[Path],
                    by_bytes: bool) -> list[tuple[str, int]]:
    """Top-level names contributing most of the payload's count or size."""
    totals: dict[str, int] = {}
    for path in payload:
        parts = path.relative_to(root).parts
        name = parts[0] + ("/" if len(parts) > 1 else "")
        share = path.stat().st_size if by_bytes else 1
        totals[name] = totals.get(name, 0) + share
    return sorted(totals.items(), key=lambda item: -item[1])[:3]


def _manifest_bytes_bound(root: Path, payload: list[Path]) -> int:
    """An upper bound on manifest.json's size, computed without hashing.

    The manifest is a zip entry like any other, so the marker counts it
    against both caps. Bounding it costs nothing, where building it first
    would SHA-256 an entire over-cap tree only to refuse it.
    """
    per_entry = 160  # JSON scaffolding, the 64-char digest, and a byte count
    paths = sum(len(path.relative_to(root).as_posix()) for path in payload)
    return 400 + paths + per_entry * len(payload)


def check_payload_caps(root: Path, payload: list[Path]) -> None:
    """Refuse a payload the marker's ingest would discard.

    An over-cap zip is not a partial submission the student can weigh up: the
    marker's ingest cannot read it at all, so a final submission would be
    recorded with no work extracted and no evidence. Here, with the folder
    still in front of them, is the only point at which it can be fixed, so
    this refuses and names what to take out.

    Counts are the zip's, not the folder's: manifest.json goes into the
    archive too, so a payload sitting exactly on a cap puts the zip over it.
    """
    total = sum(path.stat().st_size for path in payload)
    zip_files = len(payload) + 1
    zip_bytes = total + _manifest_bytes_bound(root, payload)
    over_count = zip_files > MAX_BUNDLE_FILES
    over_bytes = zip_bytes > MAX_BUNDLE_TOTAL_BYTES
    if not (over_count or over_bytes):
        return
    if over_count:
        measured = (f"{len(payload)} files, which is over the "
                    f"{MAX_BUNDLE_FILES}-file limit once the bundle's own "
                    f"manifest is added")
        worst = [f"{name}: {share} files"
                 for name, share in _payload_shares(root, payload, False)]
    else:
        limit_mb = MAX_BUNDLE_TOTAL_BYTES / (1 << 20)
        measured = (f"{zip_bytes / (1 << 20):.1f} MB, which is over the "
                    f"{limit_mb:.0f} MB limit")
        worst = [f"{name}: {share / (1 << 20):.1f} MB"
                 for name, share in _payload_shares(root, payload, True)]
    raise SystemExit(
        f"bundle.py: your project folder holds {measured}, so the marking "
        f"tools could not open the zip and your work would arrive empty. "
        f"Nothing has been written.\n"
        f"  Biggest: {'; '.join(worst)}\n"
        f"Move what is not your submitted work out of the project folder (a "
        f"virtual environment, a downloaded dataset, or a node_modules/ are "
        f"the usual causes), then run bundle.py again. To bundle just the "
        f"files you name, use --files."
    )


def collect_payload(root: Path, explicit: list[str] | None) -> list[Path]:
    """The payload files to bundle, sorted by relative path.

    With --files, exactly those files (relative to *root*). Otherwise every
    file under *root* except the exclusions above (transcripts, VCS, team
    ceremony files, prior zips).
    """
    if explicit:
        chosen = []
        for raw in explicit:
            # The typed spelling (lexically normalised, links untouched) is
            # the name the zip carries; resolve() serves the containment and
            # exclusion tests only. Appending the resolved path instead would
            # ship a link's target under a path the student never typed:
            # for notes.md -> transcripts/session1.md, the record itself,
            # with every walk guard suppressed under --files.
            typed = Path(os.path.normpath(root / raw))
            try:
                path = typed.resolve()
            except (OSError, RuntimeError):
                # ELOOP is RuntimeError on Python <= 3.12; refuse with the
                # path in bundle.py's own register, never a traceback.
                raise SystemExit(
                    f"bundle.py: --files path {raw} cannot be resolved: a "
                    f"link there points at itself (or loops). Fix or remove "
                    f"the link and re-run.")
            if path != root and root not in path.parents:
                raise SystemExit(f"bundle.py: --files path escapes the "
                                 f"project folder: {raw}")
            if path.is_dir():
                # The over-cap refusal prints folder names and says "use
                # --files"; "not found" for a folder the student can see
                # would be false. Name the restriction and the remedy.
                raise SystemExit(
                    f"bundle.py: --files path {raw} is a folder, and --files "
                    f"takes files. Name the files inside it (for example "
                    f"{raw.rstrip('/')}/results.csv), or run without "
                    f"--files to bundle the project.")
            if not path.is_file():
                raise SystemExit(f"bundle.py: --files path not found: {raw}")
            try:
                rel = typed.relative_to(root)
            except ValueError:
                # A spelling outside the project that resolves back inside
                # (a ../ path or aliased absolute path): the typed name
                # cannot be kept, and the exclusion refusal below still
                # applies: an outside link into excluded content must not
                # ship what an inside link may not.
                rel = None
            if ((rel is None or typed != path)
                    and not _included(path.relative_to(root).parts)):
                target = path.relative_to(root).as_posix()
                raise SystemExit(
                    f"bundle.py: --files path {raw} is a link to {target}, "
                    f"which is never put in a zip. If it is submitted work, "
                    f"copy it in as a real file (not a link) and re-run; if "
                    f"it is your record or a team file, it stays with you.")
            chosen.append(typed if rel is not None else path)
        return sorted(set(chosen))
    return sorted(
        p for p in root.rglob("*")
        if p.is_file() and _included(p.relative_to(root).parts)
        # is_file() follows symlinks, so without these a file link would ship
        # bytes the walk excludes under an in-project name: an out-of-tree
        # target's (content the --files branch above refuses), or an excluded
        # in-project target's (the record excluded_content promises stays with
        # the student).
        and not _link_escapes(root, p)
        and not _link_target_excluded(root, p)
    )


def build_manifest(root: Path, payload: list[Path], lc: str, sub_id: str,
                   week: int, aias: int | None) -> dict:
    """The bundle manifest (DATA_MODEL.md §3.9). IDs only, never names."""
    manifest = {
        "schema": "mn5813.bundle/1",
        "lc": lc,
        "id": sub_id,
        "week": week,
        "files": [
            {
                "path": path.relative_to(root).as_posix(),
                "sha256": sha256_file(path),
                "bytes": path.stat().st_size,
            }
            for path in payload
        ],
        "toolVersions": {
            "python": ".".join(str(v) for v in sys.version_info[:3]),
            "bundle_py": BUNDLE_PY_VERSION,
        },
    }
    if aias is not None:
        manifest["aiasLevel"] = aias
    return manifest


def write_bundle(root: Path, out_dir: Path, lc: str, sub_id: str, week: int,
                 aias: int | None,
                 files: list[str] | None) -> tuple[Path, int]:
    """Build the ship-it zip; returns (zip path, payload file count).

    Executes nothing: files are hashed and copied into the zip, never run.
    """
    payload = collect_payload(root, files)
    if not payload:
        raise SystemExit(
            "bundle.py: nothing to bundle. Run this from your project "
            "folder (the one holding your notebook)."
        )
    check_payload_caps(root, payload)
    manifest = build_manifest(root, payload, lc, sub_id, week, aias)

    zip_name = f"submission-wk{week:02d}-{sub_id}-{utc_stamp()}.zip"
    out_dir.mkdir(parents=True, exist_ok=True)
    zip_path = out_dir / zip_name
    # Build under a temporary name and rename only on success. If a file cannot
    # be added (a copy carrying a pre-1980 timestamp raises ValueError, which
    # is easy to acquire by extracting from an archive), the `with` block still
    # closes the archive, so writing straight to zip_path would leave a
    # truncated but perfectly openable zip: some files, no manifest.json, and no
    # sign to the student that it is incomplete. A submission must be whole or
    # absent, never quietly partial.
    partial = out_dir / (zip_name + ".part")
    try:
        with zipfile.ZipFile(partial, "w",
                             compression=zipfile.ZIP_DEFLATED) as archive:
            for path in payload:
                archive.write(path, path.relative_to(root).as_posix())
            archive.writestr(
                "manifest.json",
                json.dumps(manifest, indent=2, sort_keys=True) + "\n",
            )
    except BaseException:
        try:
            partial.unlink()
        except OSError:
            pass
        raise
    partial.replace(zip_path)
    return zip_path, len(payload)


def write_local_receipt(root: Path, zip_path: Path, manifest_files: int,
                        lc: str, sub_id: str, week: int) -> Path:
    """The instant, client-side receipt: proof of what you bundled, when."""
    receipts_dir = root / "local-receipts"
    receipts_dir.mkdir(parents=True, exist_ok=True)
    receipt = {
        "schema": "mn5813.localreceipt/1",
        "bundle": zip_path.name,
        "bundleSha256": sha256_file(zip_path),
        "lc": lc,
        "id": sub_id,
        "week": week,
        "filesBundled": manifest_files,
        "createdAt": utc_iso(),
        "note": ("Local receipt written by bundle.py the moment your zip "
                 "was created. Keep it: it is your index of what you "
                 "shipped."),
    }
    receipt_path = receipts_dir / f"{zip_path.stem}.receipt.json"
    with open(receipt_path, "w", encoding="utf-8") as handle:
        json.dump(receipt, handle, indent=2, sort_keys=True)
        handle.write("\n")
    return receipt_path


def assemble_portfolio(root: Path, sub_id: str,
                       excerpts: list[str] | None) -> Path:
    """--portfolio: index local receipts + your chosen excerpt files.

    Curation is yours: the tool only copies what you name into portfolio/
    and writes an index. It reads nothing else and executes nothing. Each
    run rebuilds receipts/, excerpts/ and the precheck copy to exactly this
    run's selection: anything an earlier run copied that this run does not
    name again is removed, and every removal is printed, so the folder never
    shows more than you chose. Every excerpt is validated before anything is
    copied: a refused run leaves the previous portfolio untouched.
    """
    portfolio = root / "portfolio"

    sources: list[Path] = []
    #: destination name (case-folded, for the case-insensitive filesystems
    #: most students run) -> (the argument that claimed it, its path).
    claimed: dict[str, tuple[str, Path]] = {}
    for raw in excerpts or []:
        path = Path(raw)
        if not path.is_absolute():
            path = root / raw
        if path.is_dir():
            raise SystemExit(f"bundle.py: excerpt path {raw} is a folder, "
                             f"and --excerpts takes files; name each file itself.")
        if not path.is_file():
            raise SystemExit(f"bundle.py: excerpt not found: {raw}")
        earlier = claimed.get(path.name.lower())
        if earlier is not None:
            earlier_raw, earlier_path = earlier
            try:
                one_file = os.path.samefile(earlier_path, path)
            except OSError:
                one_file = False
            if one_file:
                raise SystemExit(
                    f"bundle.py: the same file is named twice: "
                    f"{earlier_raw} and {raw} are one file. There is "
                    f"nothing to rename; name it once.")
            raise SystemExit(
                f"bundle.py: two excerpts would land at the same name "
                f"portfolio/excerpts/{path.name}: {earlier_raw} and {raw}. "
                f"portfolio/excerpts/ is flat, so the second would replace "
                f"the first while the index claimed both. Rename one file "
                f"and name the renamed copy instead.")
        claimed[path.name.lower()] = (raw, path)
        sources.append(path)

    # Build this run's portfolio in a stage inside portfolio/ (the walk never
    # enters portfolio/, so an interrupted stage can never reach a zip), then
    # swap it in, so disk and index can only describe the same set.
    stage = portfolio / ".stage"
    if stage.exists():
        shutil.rmtree(stage)
    try:
        (stage / "receipts").mkdir(parents=True)
        (stage / "excerpts").mkdir(parents=True)

        receipt_names = []
        receipts_dir = root / "local-receipts"
        if receipts_dir.is_dir():
            for receipt in sorted(receipts_dir.glob("*.receipt.json")):
                shutil.copy2(receipt, stage / "receipts" / receipt.name)
                receipt_names.append(receipt.name)

        excerpt_names = []
        for path in sources:
            shutil.copy2(path, stage / "excerpts" / path.name)
            excerpt_names.append(path.name)

        precheck = root / "precheck-report.json"
        if precheck.is_file():
            shutil.copy2(precheck, stage / "precheck-report.json")

        index = {
            "schema": "mn5813.portfolio/1",
            "id": sub_id,
            "receipts": receipt_names,
            "excerpts": excerpt_names,
            "assembledAt": utc_iso(),
        }
        with open(stage / "index.json", "w", encoding="utf-8") as handle:
            json.dump(index, handle, indent=2, sort_keys=True)
            handle.write("\n")
    except BaseException:
        shutil.rmtree(stage, ignore_errors=True)
        raise

    # Name every file an earlier run copied that this run drops, before it
    # goes: an omission is a decision you made, never a silent surprise.
    for sub_name, fresh, remedy in (
            ("receipts", receipt_names,
             "it is no longer in local-receipts/"),
            ("excerpts", excerpt_names,
             "you did not name it this time; pass it to --excerpts "
             "again to keep it")):
        prior = portfolio / sub_name
        if prior.is_dir():
            for leftover in sorted(p.name for p in prior.iterdir()):
                if leftover not in fresh:
                    print(f"bundle.py: WARNING: removing portfolio/"
                          f"{sub_name}/{leftover}: {remedy}",
                          file=sys.stderr)
    old_precheck = portfolio / "precheck-report.json"
    if old_precheck.is_file() and not (stage / "precheck-report.json").is_file():
        print("bundle.py: WARNING: removing portfolio/precheck-report.json: "
              "your project has no precheck-report.json this run",
              file=sys.stderr)

    for sub_name in ("receipts", "excerpts"):
        old = portfolio / sub_name
        if old.exists():
            shutil.rmtree(old)
        os.replace(stage / sub_name, old)
    if (stage / "precheck-report.json").is_file():
        os.replace(stage / "precheck-report.json", old_precheck)
    elif old_precheck.is_file():
        old_precheck.unlink()
    os.replace(stage / "index.json", portfolio / "index.json")
    shutil.rmtree(stage, ignore_errors=True)
    return portfolio


def main(argv: list[str] | None = None) -> int:
    """CLI entry point for the ship-it bundler / portfolio assembler."""
    parser = argparse.ArgumentParser(
        description="Bundle your work for upload (or assemble your "
                    "portfolio). Executes nothing; never phones home."
    )
    parser.add_argument("path", nargs="?", default=".",
                        help="your project folder (default: current folder)")
    parser.add_argument("--id", required=True, dest="sub_id",
                        help="your group ID (G01) or candidate ID (P401001), "
                             "never your name")
    parser.add_argument("--lc", default=None,
                        help="checkpoint (LC1..LC5) or 'final'")
    parser.add_argument("--week", type=int, default=None,
                        help="teaching week number (e.g. 4)")
    parser.add_argument("--aias", type=int, default=None,
                        help="your AIAS declaration level (1-5); no level "
                             "is penalised")
    parser.add_argument("--files", nargs="+", default=None,
                        help="bundle exactly these files instead of the "
                             "default selection")
    parser.add_argument("--out", default=None,
                        help="folder for the zip (default: project folder)")
    parser.add_argument("--portfolio", action="store_true",
                        help="assemble portfolio/ from local receipts and "
                             "--excerpts instead of bundling")
    parser.add_argument("--excerpts", nargs="+", default=None,
                        help="(portfolio mode) your chosen excerpt files")
    args = parser.parse_args(argv)

    root = Path(args.path).resolve()
    if not root.is_dir():
        print(f"bundle.py: not a folder: {root}", file=sys.stderr)
        return 2
    if not valid_submission_id(args.sub_id):
        print("bundle.py: --id must be a group ID like G01 or a candidate "
              "ID like P401001 (IDs only, never names)", file=sys.stderr)
        return 2

    if args.portfolio:
        portfolio = assemble_portfolio(root, args.sub_id, args.excerpts)
        print(f"Portfolio assembled at {portfolio}")
        print("You selected; the tool assembled. The marker sees what you "
              "chose to show.")
        return 0

    if args.lc is None or args.week is None:
        print("bundle.py: --lc and --week are required when bundling "
              "(e.g. --lc LC1 --week 4)", file=sys.stderr)
        return 2
    if not LC_RE.match(args.lc):
        print("bundle.py: --lc must be LC1..LC99 or 'final'", file=sys.stderr)
        return 2
    if not 1 <= args.week <= 12:
        print("bundle.py: --week must be 1..12", file=sys.stderr)
        return 2
    if args.aias is not None and not 1 <= args.aias <= 5:
        print("bundle.py: --aias must be 1..5", file=sys.stderr)
        return 2

    # Anything behind or through a link to outside the project folder is NOT
    # bundled. Say so before the zip is written, and name every one, so the
    # omission is a decision the student makes rather than a surprise at
    # marking time. (--files with such a path refuses outright, so the copy
    # remedy is the only one that works.)
    skipped_links = [] if args.files else out_of_tree_links(root)
    for link in skipped_links:
        rel = link.relative_to(root).as_posix() + ("/" if link.is_dir() else "")
        print(f"bundle.py: WARNING: not bundling {rel}: it is a link "
              f"pointing outside the project folder, and only files inside "
              f"the project folder are bundled. Copy what you need INTO the "
              f"project folder (a real copy, not a link) and re-run.",
              file=sys.stderr)

    # A link the walk would bundle whose in-project target is excluded ships
    # neither name. Deliberate (the target is excluded on its own path), but
    # named, because the warning below is about to say the record stays with
    # the student.
    skipped_target_links = [] if args.files else excluded_target_links(root)
    for link in skipped_target_links:
        rel = link.relative_to(root).as_posix()
        target = link.resolve().relative_to(root).as_posix()
        print(f"bundle.py: WARNING: not bundling {rel}: it is a link to "
              f"{target}, which is never put in a zip. If it is submitted "
              f"work, copy it in as a real file (not a link) and re-run; if "
              f"it is your record or a team file, it stays with you.",
              file=sys.stderr)

    # An in-project directory link's files ship only under their real path,
    # so anything read THROUGH the link name is absent from the zip while it
    # works in the student's own folder. Never bundled twice (a link to the
    # project root would recurse, and duplicates count against the caps),
    # but named, so the loss of the path is a decision, not a surprise.
    skipped_dir_links = [] if args.files else in_project_dir_links(root)
    for link in skipped_dir_links:
        rel = link.relative_to(root).as_posix() + "/"
        target = link.resolve()
        tgt = ("the project folder itself" if target == root
               else target.relative_to(root).as_posix() + "/")
        print(f"bundle.py: WARNING: {rel} is a link to {tgt}. The zip "
              f"carries the real path only, so anything your notebook reads "
              f"through {rel} will not be found at marking time. Use the "
              f"real path in your work, or copy the folder in as a real "
              f"copy (not a link) and re-run.", file=sys.stderr)

    # Your record and your team's ceremony files are never bundled. That is
    # deliberate, but say which ones were there, so a checkpoint that needs
    # them is not uploaded without them.
    skipped_content = [] if args.files else excluded_content(root)
    for name in skipped_content:
        print(f"bundle.py: WARNING: not bundling {name}: your record and "
              f"team files stay with you and are never put in a zip. If this "
              f"upload is meant to carry them, send them the way your module "
              f"asks.", file=sys.stderr)

    out_dir = Path(args.out).resolve() if args.out else root
    zip_path, payload_count = write_bundle(root, out_dir, args.lc,
                                           args.sub_id, args.week,
                                           args.aias, args.files)
    receipt_path = write_local_receipt(root, zip_path, payload_count,
                                       args.lc, args.sub_id, args.week)

    print(f"Bundle written: {zip_path}")
    print(f"Local receipt:  {receipt_path}")
    if (skipped_links or skipped_target_links or skipped_dir_links
            or skipped_content):
        # Never the unqualified reassurance while work was left out of the zip.
        names = ", ".join(
            [l.relative_to(root).as_posix() + ("/" if l.is_dir() else "")
             for l in skipped_links]
            + [l.relative_to(root).as_posix() for l in skipped_target_links]
            + [l.relative_to(root).as_posix() + "/"
               for l in skipped_dir_links]
            + skipped_content)
        print(f"NOT included: {names} (see the warnings above). Check that is "
              f"what you meant before you upload to the Moodle assignment for "
              f"{args.lc}.")
    else:
        print("Your work is safe and yours. Upload the zip to the "
              f"Moodle assignment for {args.lc} whenever you are ready, "
              "any time within the window, no reason needed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
