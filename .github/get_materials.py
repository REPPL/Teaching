"""Bring the module's latest materials into a student's repository without
touching anything the student changed.

Run by the "Get new materials" workflow (.github/workflows/get-materials.yml)
inside the student's own repository, after it has fetched the module's
public repository into a local ref. The workflow runs this file from that
fetched ref, never from the student's copy, so a fix here reaches every
student on their next run.

The rule, for every file the module's repository holds now:

- A file the student does not have is added.
- A file the student has never changed is replaced by the latest version.
  "Never changed" means its content equals some version the module ever
  published at that path, so no record of earlier runs is needed.
- A file the student changed is never written. (A file changed back to
  exactly an earlier published version counts as unchanged.) When the module has a newer
  version than the one the student started from, it is saved next to theirs
  as ``<name>.updated<suffix>`` (``Quest.ipynb`` gets ``Quest.updated.ipynb``).
  That copy is replaced again only while the student leaves it unchanged.
- Files under ``.github/workflows/`` are never written: the workflow's token
  cannot change workflows.
- A file the student deleted stays deleted, and a file the module deletes
  stays in the student's repository.

Each notebook's "Open in GitHub Codespaces" button is pointed at the
student's own repository (``codespaces.new/<repo>?quickstart=1``), which
resumes their Codespace. Content is compared with that change undone.

Standard library only; it runs on the workflow runner's own Python.
"""

import argparse
import hashlib
import os
import re
import subprocess
import sys
from pathlib import Path, PurePosixPath

BOT_NAME = "github-actions[bot]"
BOT_EMAIL = "41898282+github-actions[bot]@users.noreply.github.com"

WORKFLOWS_DIR = PurePosixPath(".github", "workflows")
UPDATED_TAG = ".updated"

BADGE_IMAGE = "(https://github.com/codespaces/badge.svg)]"
GENERIC_TARGET = BADGE_IMAGE + "(https://github.com/codespaces)"


def personal_target(repo: str) -> str:
    return BADGE_IMAGE + f"(https://codespaces.new/{repo}?quickstart=1)"


def personalise(path: str, data: bytes, repo: str) -> bytes:
    """*data* with each notebook's Codespaces button pointed at *repo*."""
    if not path.endswith(".ipynb"):
        return data
    return data.replace(GENERIC_TARGET.encode(), personal_target(repo).encode())


# A personalised button for any repository, so a notebook personalised
# before the student renamed or moved the repository still compares equal.
_PERSONAL_RE = re.compile(
    re.escape(BADGE_IMAGE.encode())
    + rb"\(https://codespaces\.new/[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+\?quickstart=1\)")


def normalise(path: str, data: bytes, repo: str) -> bytes:
    """personalise() undone, for this or any earlier name of the repository,
    so a file can be compared with the module's."""
    if not path.endswith(".ipynb"):
        return data
    return _PERSONAL_RE.sub(GENERIC_TARGET.encode(), data)


def blob_id(data: bytes) -> str:
    """The id git gives *data* as a blob (git hash-object)."""
    return hashlib.sha1(b"blob %d\0" % len(data) + data).hexdigest()


def updated_name(path: str) -> str:
    """Where the module's newer version of a changed file is saved."""
    p = PurePosixPath(path)
    if p.suffix and p.stem:
        return str(p.with_name(p.stem + UPDATED_TAG + p.suffix))
    return path + UPDATED_TAG


def git_bytes(*args: str) -> bytes:
    return subprocess.run(["git", *args], check=True,
                          stdout=subprocess.PIPE).stdout


def git(*args: str) -> str:
    return git_bytes(*args).decode("utf-8", "surrogateescape")


def tree(ref: str) -> dict:
    """{path: (mode, blob id)} for every regular file in *ref*."""
    files = {}
    raw = git("ls-tree", "-r", "-z", "--full-tree", ref)
    for entry in raw.split("\0"):
        if not entry:
            continue
        meta, path = entry.split("\t", 1)
        mode, kind, oid = meta.split()
        if kind == "blob" and mode in ("100644", "100755"):
            files[path] = (mode, oid)
    return files


def history(ref: str) -> dict:
    """{path: set of blob ids} over every commit reachable from *ref*: Each
    version the module ever published at each path."""
    seen = {}
    for commit in git("rev-list", ref).split():
        for path, (_, oid) in tree(commit).items():
            seen.setdefault(path, set()).add(oid)
    return seen


def student_base(path: str, published: set, repo: str):
    """The newest unchanged module version of *path* in the student's own
    history (HEAD), or None: The version the student started from."""
    for commit in git("log", "--format=%H", "HEAD", "--", path).split():
        try:
            data = git_bytes("show", f"{commit}:{path}")
        except subprocess.CalledProcessError:
            continue  # deleted in this commit
        oid = blob_id(normalise(path, data, repo))
        if oid in published:
            return oid
    return None


def last_copy(copy: str, repo: str):
    """The blob id, normalised, that *copy* last held in the student's
    history (HEAD), or None if it never existed there or held nothing
    readable. A copy the student deleted is written again only when the
    module has a newer version than this."""
    for commit in git("log", "--format=%H", "HEAD", "--", copy).split():
        try:
            data = git_bytes("show", f"{commit}:{copy}")
        except subprocess.CalledProcessError:
            continue  # deleted in this commit
        return blob_id(normalise(copy, data, repo))
    return None


def inside(root: Path, target: Path) -> bool:
    """*target* resolves inside *root*, so no symlinked folder in the
    student's repository can send a write elsewhere."""
    try:
        target.resolve().relative_to(root.resolve())
        return True
    except ValueError:
        return False


def write(root: Path, path: str, data: bytes, mode: str) -> None:
    target = root / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(data)
    target.chmod(0o755 if mode == "100755" else 0o644)


def plan(root: Path, upstream: str, repo: str) -> dict:
    """Decide and write every file; returns the report by outcome."""
    now = tree(upstream)
    published = history(upstream)
    report = {"added": [], "updated": [], "kept": [], "kept-no-copy": [],
              "skipped": []}

    for path, (mode, oid) in sorted(now.items()):
        if PurePosixPath(path).parts[:2] == WORKFLOWS_DIR.parts:
            continue
        target = root / path
        folders = [root / f for f in PurePosixPath(path).parents
                   if f != PurePosixPath(".")]
        if not inside(root, target) or any(
                f.is_symlink() or f.is_file() for f in folders):
            report["skipped"].append(path)  # a link, or a file where a folder goes
            continue
        new = personalise(path, git_bytes("cat-file", "blob", oid), repo)

        if not target.exists() and not target.is_symlink():
            if git("rev-list", "-1", "HEAD", "--", path).strip():
                continue  # the student had it and deleted it
            write(root, path, new, mode)
            report["added"].append(path)
            continue
        if target.is_symlink() or not target.is_file():
            report["skipped"].append(path)
            continue

        local = target.read_bytes()
        local_oid = blob_id(normalise(path, local, repo))
        if local_oid in published.get(path, ()):
            if local != new:
                write(root, path, new, mode)
                report["updated"].append(path)
            continue

        # The student changed this file: Theirs is never written.
        if student_base(path, published.get(path, set()), repo) == oid:
            continue  # nothing new since the version they started from
        copy = updated_name(path)
        copy_target = root / copy
        if copy_target.is_symlink() or (copy_target.exists() and not copy_target.is_file()):
            report["kept-no-copy"].append(path)
            continue
        if copy_target.exists():
            theirs = blob_id(normalise(path, copy_target.read_bytes(), repo))
            if theirs not in published.get(path, ()):
                report["kept-no-copy"].append(path)  # they changed the copy too
                continue
            if copy_target.read_bytes() == new:
                continue
        elif last_copy(copy, repo) == oid:
            continue  # they deleted this very version of the copy
        write(root, copy, new, mode)
        report["kept"].append(path)
    return report


def summary(report: dict, upstream_commit: str) -> str:
    lines = [f"## Get new materials (module release {upstream_commit[:7]})", ""]
    if not any(report[k] for k in ("added", "updated", "kept", "kept-no-copy")):
        lines.append("You already have everything. Nothing was changed.")
    sections = (
        ("added", "New files"),
        ("updated", "Files you had not changed, now updated"),
        ("kept", "Files you changed, kept as they are. "
                 "The new version is saved next to each one, "
                 f"with `{UPDATED_TAG}` in its name"),
        ("kept-no-copy", "Files you changed, kept as they are. "
                         f"You also changed the `{UPDATED_TAG}` copy, "
                         "so no new version was saved"),
        ("skipped", "Not written, because something else is in the way"),
    )
    for key, title in sections:
        if report[key]:
            lines += ["", f"### {title}", ""]
            lines += [f"- `{p}`" for p in report[key]]
    return "\n".join(lines) + "\n"


def commit(paths: list, upstream_commit: str) -> bool:
    if not paths:
        return False
    git("add", "--force", "--", *paths)
    if not git("diff", "--cached", "--name-only").strip():
        return False
    git("-c", f"user.name={BOT_NAME}", "-c", f"user.email={BOT_EMAIL}",
        "commit", "--quiet", "-m",
        f"Get new materials (module release {upstream_commit[:7]})")
    return True


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(
        description="Bring the module's latest materials into this repository.")
    parser.add_argument("--upstream", required=True,
                        help="the fetched ref of the module's repository")
    parser.add_argument("--repo", required=True,
                        help="this repository, as OWNER/NAME")
    args = parser.parse_args(argv)

    root = Path(git("rev-parse", "--show-toplevel").strip())
    os.chdir(root)
    upstream_commit = git("rev-parse", args.upstream).strip()
    report = plan(root, args.upstream, args.repo)
    written = report["added"] + report["updated"] + [
        updated_name(p) for p in report["kept"]]
    commit(written, upstream_commit)

    text = summary(report, upstream_commit)
    print(text)
    step_summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if step_summary:
        with open(step_summary, "a", encoding="utf-8") as fh:
            fh.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
