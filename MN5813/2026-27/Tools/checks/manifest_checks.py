"""Tier-1 bundle-manifest checks: manifest.json parses and validity floor.

The validity floor (DATA_MODEL.md §3.9) is: the manifest
parses AND lists at least one payload file. Sub-floor bundles are flagged,
never rejected: students resubmit within the window. Before bundle.py has
run, no manifest exists and both checks report artefact_missing, which the
feedforward explains is normal.
"""

from __future__ import annotations

import json
from pathlib import Path

from .catalogue import STATUS_ARTEFACT_MISSING, STATUS_OK, make_result

MANIFEST_CHECK_IDS: tuple[str, ...] = (
    "manifest_parses",
    "manifest_meets_validity_floor",
)


def manifest_meets_validity_floor(manifest: object) -> bool:
    """The contract's floor: a parsed object listing >= 1 payload file."""
    if not isinstance(manifest, dict):
        return False
    files = manifest.get("files")
    return (
        isinstance(files, list)
        and len(files) >= 1
        and all(isinstance(f, dict) and isinstance(f.get("path"), str)
                for f in files)
    )


def run_manifest_checks(submission_dir: Path) -> list[dict]:
    """Run the manifest battery over *submission_dir*; list of results."""
    manifest_path = Path(submission_dir) / "manifest.json"
    if not manifest_path.is_file():
        return [make_result(cid, None, STATUS_ARTEFACT_MISSING)
                for cid in MANIFEST_CHECK_IDS]
    try:
        with open(manifest_path, "r", encoding="utf-8") as handle:
            manifest = json.load(handle)
    except Exception:
        # json.load's failures are an open-ended class, not just
        # JSONDecodeError: RecursionError for a deeply nested document,
        # bare ValueError for an integer over CPython's digit limit. Bad
        # student input must never raise out of here (record-don't-reject);
        # KeyboardInterrupt/SystemExit still propagate.
        return [
            make_result("manifest_parses", False, STATUS_OK),
            make_result("manifest_meets_validity_floor", False, STATUS_OK),
        ]
    return [
        make_result("manifest_parses", True, STATUS_OK),
        make_result("manifest_meets_validity_floor",
                    manifest_meets_validity_floor(manifest), STATUS_OK),
    ]
