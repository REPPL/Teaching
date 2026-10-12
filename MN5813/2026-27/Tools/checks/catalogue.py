"""Tier-1 check catalogue: ids, criteria, descriptions, and feedforward text.

This is the base module of the checks package. It defines the machine-readable
catalogue of every Tier-1 check (id, criterion, description, tier), the shared
tri-state status constants, and the single result constructor used by every
check module. Only Tier-1 results ever become marker evidence fields;
this catalogue is the published scope of the transparency-symmetry
guarantee.

Concatenated FIRST into the distributable student check.py by
tools/precheck_dist.py, so it must stay stdlib-only and import nothing from
marklib.
"""

from __future__ import annotations

import copy
import re
from typing import Any

#: Version of the Tier-1 battery; recorded as the extractor version in
#: evidence fields and in student tool output.
TIER1_VERSION = "1.0"

TIER1 = 1

STATUS_OK = "ok"
STATUS_ARTEFACT_MISSING = "artefact_missing"
STATUS_EXTRACTION_FAILED = "extraction_failed"
STATUSES = (STATUS_OK, STATUS_ARTEFACT_MISSING, STATUS_EXTRACTION_FAILED)


def _entry(check_id: str, criterion: str, description: str, hint: str,
           handbook: str, expect: dict | None = None) -> dict:
    """One catalogue entry (all Tier 1).

    *expect* declares what value passes for a count-valued check
    (``{"min": n}`` and/or ``{"max": n}``, bounds inclusive). Boolean
    checks need no expectation: the value judges itself. An entry with
    neither is informational: renderers must show its value as
    information, never as a pass (iss-126).
    """
    return {
        "id": check_id,
        "criterion": criterion,
        "description": description,
        "tier": TIER1,
        "fixHint": hint,
        "handbook": handbook,
        "expect": expect,
    }


#: The machine-readable Tier-1 check catalogue, in battery run order.
CATALOGUE: list[dict] = [
    # ---- notebook checks -------------------------------------------------
    _entry(
        "notebook_parses", "professionalism",
        "The submitted notebook opens as a valid .ipynb file.",
        "Your notebook could not be opened as a valid .ipynb file. Re-save "
        "it from Jupyter and re-run this check.",
        "Assessment brief → report template",
    ),
    _entry(
        "intro_section_present", "intro",
        "An 'Introduction' heading is present.",
        "Add an 'Introduction' heading from the template.",
        "Assessment brief → report template",
    ),
    _entry(
        "aim_section_present", "intro",
        "An 'Aim' heading is present.",
        "Add an 'Aim' heading under Introduction.",
        "Assessment brief → report template",
    ),
    _entry(
        "objectives_section_present", "intro",
        "An 'Objectives' heading is present.",
        "Add an 'Objectives' heading under Introduction.",
        "Assessment brief → report template",
    ),
    _entry(
        "project_summary_present", "intro",
        "An 'Executive summary' (or 'Project summary') heading is present.",
        "Add the template's 'Executive summary' section.",
        "Assessment brief → report template",
    ),
    _entry(
        "review_section_present", "review",
        "A 'Review' heading is present.",
        "Add a 'Review' heading covering prior work on your topic.",
        "Assessment brief → report template",
    ),
    _entry(
        "data_mgmt_section_present", "data_mgmt",
        "A 'Data management' heading is present.",
        "Add a 'Data management' heading describing how you cleaned the data.",
        "Assessment brief → data management",
    ),
    _entry(
        "analysis_section_present", "analysis",
        "An 'Analysis' heading is present.",
        "Add the template's 'Analysis & presentation of results' heading.",
        "Assessment brief → report template",
    ),
    _entry(
        "conclusions_section_present", "conclusions",
        "A 'Concluding remarks' heading is present.",
        "Add a 'Concluding remarks' heading (limitations are welcome there).",
        "Assessment brief → report template",
    ),
    _entry(
        "declaration_section_present", "professionalism",
        "An 'AI Use Record' heading is present.",
        "Complete the 'AI Use Record' section (tools, uses, rejected "
        "outputs, verification). No level of AI use is penalised.",
        "Assessment brief → AI Use Record",
    ),
    _entry(
        "execution_order_monotonic", "professionalism",
        "Code cells were executed once, top to bottom (Restart & Run All).",
        "Run 'Kernel → Restart & Run All' before shipping so cells execute "
        "in order. This is a fixable convention, not a judgment.",
        "Handbook → Professionalism",
    ),
    _entry(
        "markdown_code_ratio", "professionalism",
        "Markdown-to-code cell ratio (indicative only).",
        "Balance narrative and code: explain each step in markdown near the "
        "code that does it. Indicative only, never marked by count.",
        "Handbook → Professionalism",
    ),
    _entry(
        "notebook_cell_count", "professionalism",
        "Total notebook cell count (indicative only).",
        "Indicative size only: quality beats length.",
        "Handbook → Professionalism",
    ),
    # ---- reference checks ------------------------------------------------
    _entry(
        "reference_section_present", "review",
        "A 'References' heading is present.",
        "Add a 'References' heading listing your sources.",
        "Handbook → References",
    ),
    _entry(
        "n_references", "review",
        "Reference-list items detected (~detected, verify).",
        "~detected, verify: an indicative count only; your marker counts "
        "your references, not this tool. Aim for at least 5 scholarly "
        "sources.",
        "Handbook → References",
    ),
    # ---- cleaned-CSV schema checks ----------------------------------------
    _entry(
        "cleaned_csv_present", "data_mgmt",
        "A cleaned CSV file is included in the submission.",
        "Include your cleaned dataset under data/ (see the handbook for the "
        "taught filename convention).",
        "Assessment brief → data management",
    ),
    _entry(
        "cleaned_csv_parses", "data_mgmt",
        "The cleaned CSV reads as valid CSV with a header row.",
        "The cleaned CSV could not be read; re-export it from your notebook.",
        "Assessment brief → data management",
    ),
    _entry(
        "cleaned_csv_key_columns_present", "data_mgmt",
        "The published schema's key columns are present.",
        "Include the key columns from the published cleaned-output schema. "
        "A deviation with a stated rationale is acceptable and never "
        "hard-fails.",
        "Assessment brief → data management",
    ),
    _entry(
        "cleaned_csv_dtypes_ok", "data_mgmt",
        "Column values parse as the published schema's types.",
        "Some values do not parse as the published column types. A deviation "
        "with a stated rationale is acceptable and never hard-fails.",
        "Assessment brief → data management",
    ),
    _entry(
        "cleaned_csv_no_duplicate_keys", "data_mgmt",
        "No duplicate rows on the schema's key columns.",
        "Key columns repeat across rows; drop duplicates or state your "
        "rationale. Never hard-fails.",
        "Assessment brief → data management",
    ),
    _entry(
        "referenced_data_files_exist", "data_mgmt",
        "Every data file the notebook reads exists in the submission.",
        "A file your notebook reads is missing from the submission folder; "
        "use relative data/ paths and include the file.",
        "Assessment brief → data management",
    ),
    # ---- figure checks -----------------------------------------------------
    _entry(
        "n_figures", "analysis",
        "Saved PNG figures found in the submission.",
        "Save each figure as a PNG (e.g. figures/fig1.png) so it ships with "
        "your work.",
        "Handbook → Figures",
        expect={"min": 1},
    ),
    _entry(
        "n_figures_readable", "analysis",
        "PNG figures whose header parses with positive dimensions.",
        "No PNG figure could be read; re-save them from your notebook.",
        "Handbook → Figures",
        expect={"min": 1},
    ),
    _entry(
        "n_figures_unreadable", "analysis",
        "PNG figures found whose header does not parse (corrupt or not PNG).",
        "One or more PNG files are corrupt; re-save them from your notebook.",
        "Handbook → Figures",
        expect={"max": 0},
    ),
    _entry(
        "min_figure_width_px", "analysis",
        "Smallest figure width in pixels (indicative only).",
        "Indicative smallest figure width; very small figures can be "
        "unreadable, so export at a sensible size.",
        "Handbook → Figures",
    ),
    # ---- bundle manifest checks -------------------------------------------
    _entry(
        "manifest_parses", "professionalism",
        "manifest.json parses as JSON.",
        "manifest.json lives inside the zip bundle.py writes, never in your "
        "project folder, so missing here is normal and nothing to fix. This "
        "check only means anything when you unpack a bundle and run "
        "'python3 check.py' on the unpacked folder.",
        "Handbook → Ship-it ritual",
    ),
    _entry(
        "manifest_meets_validity_floor", "professionalism",
        "manifest.json parses and lists at least one payload file.",
        "The bundle must list at least one payload file; re-run bundle.py "
        "from your project folder.",
        "Handbook → Ship-it ritual",
    ),
]

_BY_ID = {entry["id"]: entry for entry in CATALOGUE}

ALL_CHECK_IDS = tuple(entry["id"] for entry in CATALOGUE)

#: The house pedagogical categories a catalogue entry's ``criterion`` may name
#: (DATA_MODEL section 3.2). Authored independently of CATALOGUE (not derived
#: from it) so a typo'd or unsanctioned criterion slug in a catalogue entry is
#: caught by the parity test rather than silently accepted. These are house
#: categories, not any delivery's rubric ids, so this stays module-agnostic.
CATALOGUE_CRITERIA = frozenset({
    "intro", "review", "data_mgmt", "analysis", "conclusions", "professionalism",
})


def catalogue() -> list[dict]:
    """Return a deep copy of the machine-readable Tier-1 check catalogue."""
    return copy.deepcopy(CATALOGUE)


def feedforward_for(check_id: str, status: str = STATUS_OK) -> str:
    """The feedforward line for *check_id*: fix hint + handbook pointer.

    A check that could not run (``extraction_failed``) has nothing to fix
    of its own: its fix hint describes a fault in a value that was never
    computed (a "remove duplicate rows" hint over a CSV whose key columns
    are missing), so the line says the check did not run and points at the
    checks above it. An absent artefact keeps the entry's hint, which is
    written for absence.
    """
    entry = _BY_ID[check_id]
    if status == STATUS_EXTRACTION_FAILED:
        return (f"This check could not run because a check it depends on "
                f"did not pass; see the checks above ({entry['handbook']})")
    return f"{entry['fixHint']} ({entry['handbook']})"


#: The checks whose value is a count or measure, and so the ones a
#: delivery's ``evidenceThresholds`` may bound (``min_<id>`` / ``max_<id>``
#: in config.json). Authored by hand rather than derived, so a threshold on
#: a boolean check is refused by the config validator instead of sitting
#: inert.
COUNT_CHECK_IDS = frozenset({
    "n_references", "n_figures", "n_figures_readable", "n_figures_unreadable",
    "min_figure_width_px", "notebook_cell_count", "markdown_code_ratio",
})

#: A threshold key: min_ or max_ followed by a count check's id.
THRESHOLD_KEY_RE = re.compile(r"^(min|max)_([a-z][a-z0-9_]*)$")


def expect_for(check_id: str, thresholds: dict | None = None) -> dict | None:
    """The bounds that judge *check_id*: the catalogue's, overridden per
    side by the delivery's *thresholds* (``min_<id>``, ``max_<id>``).

    A threshold on a count the catalogue leaves indicative (n_references)
    makes it judged for that delivery: that is what a threshold is for. A
    threshold on a check outside COUNT_CHECK_IDS is ignored here and
    refused by the config validator, so it cannot sit inert.
    """
    expect = dict(_BY_ID[check_id]["expect"] or {})
    if thresholds and check_id in COUNT_CHECK_IDS:
        for side in ("min", "max"):
            value = thresholds.get(f"{side}_{check_id}")
            if isinstance(value, (int, float)) and not isinstance(value, bool):
                expect[side] = value
    return expect or None


def judge_result(result: dict, thresholds: dict | None = None) -> bool | None:
    """True/False for a judged result, None for one that cannot be judged.

    A result is judged only when it ran (status ok) and either its value
    is boolean (the value judges itself) or ``expect_for`` yields a bound
    (inclusive): the catalogue's, or the delivery's ``evidenceThresholds``.
    Everything else (non-ok statuses, counts with no declared expectation)
    returns None: information for a human, never a pass and never a fail
    (iss-126).
    """
    if result["status"] != STATUS_OK:
        return None
    value = result["value"]
    if isinstance(value, bool):
        return value
    expect = expect_for(result["id"], thresholds)
    if expect is None:
        return None
    if value is None:
        return False
    if "min" in expect and value < expect["min"]:
        return False
    if "max" in expect and value > expect["max"]:
        return False
    return True


def make_result(check_id: str, value: Any, status: str) -> dict:
    """Build the uniform Tier-1 result: {id, value, status, feedforward}.

    *check_id* must exist in the catalogue and *status* must be tri-state.
    When status is not 'ok' the value is forced to None (the evidence
    contract: no automated evidence renders as absent, never as 0).
    """
    if check_id not in _BY_ID:
        raise ValueError(f"unknown check id: {check_id!r}")
    if status not in STATUSES:
        raise ValueError(f"bad status for {check_id}: {status!r}")
    if status != STATUS_OK:
        value = None
    return {
        "id": check_id,
        "value": value,
        "status": status,
        "feedforward": feedforward_for(check_id, status),
    }
