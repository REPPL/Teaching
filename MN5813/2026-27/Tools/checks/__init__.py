"""Tier-1 check battery, shared verbatim between marker and students.

This package (``tooling/marking/checks/``) is the single, module-agnostic
Tier-1 code path: the marker's extract subcommand imports it directly, and
marker/tools/precheck_dist.py concatenates the same modules into the
self-contained student self-test (``<year>/<module>/materials/Tools/
check.py``). That identity is the transparency-symmetry guarantee: every
Tier-1 marker evidence field is computable by students with identical code,
unlimited runs.

Every check returns the uniform tri-state result
``{"id", "value", "status", "feedforward"}`` where value is only ever a
number, boolean, or null (never text quoted from student work), status is
``ok | artefact_missing | extraction_failed``, and feedforward is a fix hint
plus a handbook pointer. Marker-side callers turn results into evidence
fields by adding ``extractor`` and ``version`` (use TIER1_VERSION).

Stdlib-only, and independent of nbformat/pandas: notebooks are parsed with a
plain JSON reader so the marker and the student self-test agree on the same
file whatever the host has installed. Pandas is not needed for Tier 1.
"""

from __future__ import annotations

from pathlib import Path

from .catalogue import (
    ALL_CHECK_IDS,
    CATALOGUE,
    STATUS_ARTEFACT_MISSING,
    STATUS_EXTRACTION_FAILED,
    STATUS_OK,
    STATUSES,
    TIER1_VERSION,
    catalogue,
    feedforward_for,
    make_result,
)
from .csv_checks import CLEANED_CSV_SCHEMA, run_csv_checks
from .figures_checks import run_figures_checks
from .manifest_checks import run_manifest_checks
from .notebook_checks import find_notebook, load_notebook, run_notebook_checks
from .refs_checks import run_refs_checks


def run_tier1(submission_dir: str | Path, notebook: str | Path | None = None,
              csv_schema: dict | None = None) -> list[dict]:
    """Run the full Tier-1 battery over one submission directory.

    Returns one result per catalogue entry, in catalogue order. Never raises
    for student input (record-don't-reject): missing artefacts surface as
    artefact_missing, broken ones as extraction_failed.

    *notebook* overrides report-notebook auto-detection; *csv_schema*
    overrides the published cleaned-output contract (same dict shape as
    CLEANED_CSV_SCHEMA).
    """
    submission_dir = Path(submission_dir)
    results: list[dict] = []
    results.extend(run_notebook_checks(submission_dir, notebook=notebook))
    results.extend(run_refs_checks(submission_dir, notebook=notebook))
    results.extend(run_csv_checks(submission_dir, schema=csv_schema,
                                  notebook=notebook))
    results.extend(run_figures_checks(submission_dir))
    results.extend(run_manifest_checks(submission_dir))
    return results
