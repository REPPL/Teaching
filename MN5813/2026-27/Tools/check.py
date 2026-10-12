#!/usr/bin/env python3
"""Student self-check (Tier 1). GENERATED FILE, do not edit.

This is the SAME Tier-1 code your marker runs (transparency symmetry): it
was assembled from the toolchain's published checks package
(tooling/marking/checks/) by tooling/marking/marker/tools/precheck_dist.py.
Re-generate it there; never edit here.

How to use it (any Python 3.11+, stdlib only, nothing to install):

    python3 check.py              # check the current folder
    python3 check.py path/to/work

It prints a feed-forward checklist (every line: what to fix + where the
handbook helps) and writes precheck-report.json next to your work. A red
line never delays shipping: ship red is fine. Checks inform; humans mark.

Optional: `--resolve-dois` asks Crossref (api.crossref.org) whether the
DOIs in your notebook's markdown cells resolve. That is the ONLY network
use in this tool, it is off by default, `--offline-safe` forces it off,
results are cached in precheck-report.json, and it is indicative only:
non-DOI and non-Crossref scholarship is counted by your marker, not this
tool.
"""

from __future__ import annotations

# ===========================================================================
# embedded from tooling/marking/checks/catalogue.py
# ===========================================================================

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

# ===========================================================================
# embedded from tooling/marking/checks/notebook_checks.py
# ===========================================================================

"""Tier-1 notebook checks: parse, template sections, execution order, shape.

Presence-only section checks derived from the report template's headings,
plus the ~30-line nbformat-style metrics that replaced pynblint:
execution-order monotonicity, markdown:code ratio, and length.
Everything is a number, boolean, or null, never text quoted from student
work. All checks are tri-state.

Stdlib-only, and deliberately independent of nbformat: notebooks are parsed
with a plain JSON reader (plus a normalisation of the legacy nbformat-v3
``worksheets`` layout) so the result never depends on which packages happen
to be installed on the host. The distributed student tool runs on a bare
Python (locked-down labs) and the marker runs the identical code path. That
byte-for-byte agreement is the transparency-symmetry guarantee.
"""


import json
from pathlib import Path


#: check id -> lowercase phrases; the section is present when any markdown
#: heading contains any phrase. Derived from the report template's headings.
TEMPLATE_SECTIONS: dict[str, tuple[str, ...]] = {
    "intro_section_present": ("introduction",),
    "aim_section_present": ("aim",),
    "objectives_section_present": ("objective",),
    "project_summary_present": ("project summary", "executive summary"),
    "review_section_present": ("review",),
    "data_mgmt_section_present": ("data management",),
    "analysis_section_present": ("analysis",),
    "conclusions_section_present": ("concluding remarks", "conclusion"),
    "declaration_section_present": ("ai use record",
                                    "generative ai declaration",
                                    "ai declaration"),
}

#: every notebook-battery check id, in output order.
NOTEBOOK_CHECK_IDS: tuple[str, ...] = (
    "notebook_parses",
    *TEMPLATE_SECTIONS,
    "execution_order_monotonic",
    "markdown_code_ratio",
    "notebook_cell_count",
)


def find_notebook(submission_dir: Path) -> Path | None:
    """Locate the report notebook: report.ipynb (any case), else the first
    .ipynb.

    The .ipynb extension is matched case-insensitively. Sorted, checkpoint
    copies and hidden directories excluded, top level preferred over nested,
    and a report.ipynb wins over other notebooks at its level regardless of
    filename case. Returns None when the submission has no notebook.
    """
    submission_dir = Path(submission_dir)

    def _notebooks(paths) -> list[Path]:
        return sorted(
            p for p in paths
            if p.is_file() and p.suffix.lower() == ".ipynb"
            and not any(part.startswith(".") or part == ".ipynb_checkpoints"
                        for part in p.relative_to(submission_dir).parts)
        )

    for candidates in (_notebooks(submission_dir.glob("*")),
                       _notebooks(submission_dir.glob("**/*"))):
        for candidate in candidates:
            if candidate.name.lower() == "report.ipynb":
                return candidate
        if candidates:
            return candidates[0]
    return None


def _normalise_legacy_cell(cell: object) -> object:
    """Map a legacy nbformat-v3 cell onto the v4 field names the checks read.

    v3 code cells store the source under ``input`` and the run counter under
    ``prompt_number``; v4 uses ``source`` / ``execution_count``. Only the
    fields this package inspects are translated; everything else is left as-is.
    """
    if not isinstance(cell, dict):
        return cell
    cell = dict(cell)
    if "source" not in cell and "input" in cell:
        cell["source"] = cell["input"]
    if "execution_count" not in cell and "prompt_number" in cell:
        cell["execution_count"] = cell["prompt_number"]
    return cell


def load_notebook(path: Path) -> tuple[dict | None, str | None]:
    """Read a notebook: (notebook_dict, None) or (None, error_code).

    A plain JSON parse (stdlib only) with a minimal structural check, plus a
    normalisation of the legacy nbformat-v3 ``worksheets`` layout into a v4
    ``cells`` list. Deliberately does NOT use nbformat even when it is
    installed: the parse result must not depend on which packages happen to be
    present on the host, or the marker and the student self-test could disagree
    on the same file (the transparency-symmetry guarantee). A leading UTF-8 BOM
    is tolerated (``utf-8-sig``), matching csv_checks. Never raises for bad
    student input (record-don't-reject).
    """
    path = Path(path)
    if not path.is_file():
        return None, "file_missing"
    try:
        with open(path, "r", encoding="utf-8-sig") as handle:
            nb = json.load(handle)
    except Exception:
        # json.load's failures are an open-ended class, not just
        # JSONDecodeError: RecursionError for a deeply nested document,
        # bare ValueError for an integer over CPython's digit limit. Bad
        # student input must never raise out of here.
        return None, "parse_error"
    if not isinstance(nb, dict):
        return None, "parse_error"
    if not isinstance(nb.get("cells"), list):
        # Legacy nbformat v2/v3 stored cells under worksheets[].cells; flatten
        # them into a v4-style cells list so old exports parse identically
        # whatever the host has installed.
        worksheets = nb.get("worksheets")
        if not isinstance(worksheets, list):
            return None, "parse_error"
        cells: list = []
        for worksheet in worksheets:
            if isinstance(worksheet, dict) and isinstance(worksheet.get("cells"), list):
                cells.extend(worksheet["cells"])
        nb = dict(nb)
        nb["cells"] = [_normalise_legacy_cell(c) for c in cells]
    return nb, None


def cell_source(cell: dict) -> str:
    """A cell's source as one string (nbformat stores str or list of str)."""
    source = cell.get("source", "")
    if isinstance(source, list):
        return "".join(s for s in source if isinstance(s, str))
    return source if isinstance(source, str) else ""


def _cells(nb: dict, cell_type: str | None = None) -> list[dict]:
    """The notebook's cells, optionally filtered by cell_type."""
    cells = [c for c in nb.get("cells", []) if isinstance(c, dict)]
    if cell_type is not None:
        cells = [c for c in cells if c.get("cell_type") == cell_type]
    return cells


def markdown_headings(nb: dict) -> list[str]:
    """Every markdown heading's text, lowercased, in document order."""
    headings: list[str] = []
    for cell in _cells(nb, "markdown"):
        for line in cell_source(cell).splitlines():
            stripped = line.strip()
            if stripped.startswith("#"):
                headings.append(stripped.lstrip("#").strip().lower())
    return headings


def _section_present(headings: list[str], phrases: tuple[str, ...]) -> bool:
    return any(phrase in heading for heading in headings for phrase in phrases)


def _execution_order_monotonic(nb: dict) -> bool | None:
    """True iff every code cell ran, in strictly increasing order.

    None when the notebook has no code cells (no evidence either way).
    """
    counts = [c.get("execution_count") for c in _cells(nb, "code")]
    if not counts:
        return None
    if not all(isinstance(c, int) for c in counts):
        return False
    return all(a < b for a, b in zip(counts, counts[1:]))


def run_notebook_checks(submission_dir: Path,
                        notebook: Path | None = None) -> list[dict]:
    """Run the notebook battery over *submission_dir*; list of results.

    *notebook* overrides auto-detection. Missing notebook: every check is
    artefact_missing. Unparseable notebook: notebook_parses is False and the
    remaining checks are extraction_failed.
    """
    submission_dir = Path(submission_dir)
    nb_path = Path(notebook) if notebook else find_notebook(submission_dir)
    if nb_path is None:
        return [make_result(cid, None, STATUS_ARTEFACT_MISSING)
                for cid in NOTEBOOK_CHECK_IDS]

    nb, error = load_notebook(nb_path)
    if error == "file_missing":
        return [make_result(cid, None, STATUS_ARTEFACT_MISSING)
                for cid in NOTEBOOK_CHECK_IDS]
    if nb is None:
        results = [make_result("notebook_parses", False, STATUS_OK)]
        results.extend(
            make_result(cid, None, STATUS_EXTRACTION_FAILED)
            for cid in NOTEBOOK_CHECK_IDS if cid != "notebook_parses"
        )
        return results

    results = [make_result("notebook_parses", True, STATUS_OK)]
    headings = markdown_headings(nb)
    for cid, phrases in TEMPLATE_SECTIONS.items():
        results.append(
            make_result(cid, _section_present(headings, phrases), STATUS_OK)
        )

    monotonic = _execution_order_monotonic(nb)
    if monotonic is None:
        results.append(make_result("execution_order_monotonic", None,
                                   STATUS_ARTEFACT_MISSING))
    else:
        results.append(make_result("execution_order_monotonic", monotonic,
                                   STATUS_OK))

    n_markdown = len(_cells(nb, "markdown"))
    n_code = len(_cells(nb, "code"))
    if n_code == 0:
        results.append(make_result("markdown_code_ratio", None,
                                   STATUS_ARTEFACT_MISSING))
    else:
        results.append(make_result("markdown_code_ratio",
                                   round(n_markdown / n_code, 2), STATUS_OK))
    results.append(make_result("notebook_cell_count", len(_cells(nb)),
                               STATUS_OK))
    return results

# ===========================================================================
# embedded from tooling/marking/checks/refs_checks.py
# ===========================================================================

"""Tier-1 reference checks: reference-section presence and indicative count.

The count is honest about being a heuristic: it is labelled "~detected,
verify", and the patterns are style-robust; its feedforward states
that non-standard reference formats are counted by the marker, not the tool.
Patterns accept numbered lists, bracketed numbers, bullets, and
author-(year) lines so APA/Harvard/ACM styles all count.
"""


import re
from pathlib import Path


REFS_CHECK_IDS: tuple[str, ...] = ("reference_section_present", "n_references")

#: heading phrases that open the reference section.
_REF_HEADING_PHRASES = ("reference", "bibliography", "works cited")

#: a line that looks like one reference-list item.
_LIST_ITEM_RE = re.compile(r"^\s*(?:\d+[.)]|\[\d+\]|[-*+•])\s+\S")
#: an author-(year) style line, e.g. "Sample, E. (2020). ..." .
_YEAR_RE = re.compile(r"\((?:19|20)\d{2}[a-z]?\)")


def _is_ref_heading(text: str) -> bool:
    lowered = text.lower()
    return any(phrase in lowered for phrase in _REF_HEADING_PHRASES)


def count_references(nb: dict) -> tuple[bool, int]:
    """(reference_section_present, indicative item count) for a notebook.

    Counts lines between a References-style heading and the next heading
    that either start with a list marker or carry an author-(year) pattern.
    Each line counts once.
    """
    section_present = False
    count = 0
    in_refs = False
    for cell in (c for c in nb.get("cells", []) if isinstance(c, dict)):
        if cell.get("cell_type") != "markdown":
            continue
        for line in cell_source(cell).splitlines():
            stripped = line.strip()
            if stripped.startswith("#"):
                heading = stripped.lstrip("#").strip()
                in_refs = _is_ref_heading(heading)
                section_present = section_present or in_refs
                continue
            if in_refs and stripped:
                if _LIST_ITEM_RE.match(stripped) or _YEAR_RE.search(stripped):
                    count += 1
    return section_present, count


def run_refs_checks(submission_dir: Path,
                    notebook: Path | None = None) -> list[dict]:
    """Run the reference battery over *submission_dir*; list of results."""
    submission_dir = Path(submission_dir)
    nb_path = Path(notebook) if notebook else find_notebook(submission_dir)
    if nb_path is None:
        return [make_result(cid, None, STATUS_ARTEFACT_MISSING)
                for cid in REFS_CHECK_IDS]
    nb, error = load_notebook(nb_path)
    if error == "file_missing":
        return [make_result(cid, None, STATUS_ARTEFACT_MISSING)
                for cid in REFS_CHECK_IDS]
    if nb is None:
        return [make_result(cid, None, STATUS_EXTRACTION_FAILED)
                for cid in REFS_CHECK_IDS]

    section_present, count = count_references(nb)
    results = [make_result("reference_section_present", section_present,
                           STATUS_OK)]
    if section_present:
        results.append(make_result("n_references", count, STATUS_OK))
    else:
        # No reference section: render "no automated evidence", never 0.
        results.append(make_result("n_references", None,
                                   STATUS_ARTEFACT_MISSING))
    return results

# ===========================================================================
# embedded from tooling/marking/checks/csv_checks.py
# ===========================================================================

"""Tier-1 cleaned-CSV schema checks and referenced-data-files-exist.

The cleaned-output contract is deliberately minimal: key
columns, column types, no duplicate key. A deviation with a stated
rationale is acceptable, so nothing here ever hard-fails a submission.

This module is MODULE-AGNOSTIC: it hardcodes no delivery's dataset. The
default schema below names no specific file or columns; a delivery supplies
its own dataset contract as DATA: the marker passes it in from the delivery
config (``cleanedCsvSchema`` in ``<year>/<module>/marking/config.json``), and
callers may pass any ``schema=`` dict of the same shape.

Stdlib csv module only, so the distributed student tool runs on a bare
Python; pandas is deliberately not required for Tier 1.
"""


import ast
import csv
import io
import re
import tokenize
import warnings
from pathlib import Path


#: Module-agnostic DEFAULT cleaned-output contract: it names no delivery's
#: dataset. With no key columns or dtypes declared, the schema checks only
#: locate a cleaned CSV (any ``data/*.csv``) and confirm it parses; a delivery
#: passes its own key columns / dtypes via ``schema=`` (see module docstring).
#: Types: "string" (anything), "integer" (int()), "number" (float()).
CLEANED_CSV_SCHEMA: dict = {
    "file": "data/cleaned.csv",
    "keyColumns": [],
    "dtypes": {},
}

CSV_CHECK_IDS: tuple[str, ...] = (
    "cleaned_csv_present",
    "cleaned_csv_parses",
    "cleaned_csv_key_columns_present",
    "cleaned_csv_dtypes_ok",
    "cleaned_csv_no_duplicate_keys",
    "referenced_data_files_exist",
)

#: The dtype vocabulary a schema's ``dtypes`` values may use (see
#: ``_value_matches``): "string" accepts anything, "integer" requires int(),
#: "number" requires float(). This is the SINGLE source of the vocabulary --
#: the schema validator (marklib.common.validate_cleaned_csv_schema) imports it
#: so validator and checker cannot drift.
CSV_DTYPES: tuple[str, ...] = ("string", "integer", "number")

#: rows/files ceilings so one hostile CSV cannot stall the batch.
_MAX_ROWS = 500_000

#: read calls whose first string literal argument names a data file.
_READ_CALL_RE = re.compile(
    r"(?:read_csv|read_table|read_excel|read_json)\(\s*['\"]([^'\"]+)['\"]"
)
#: open() is separate because only its READ modes name an input. The mode is
#: captured so a file the notebook writes is not demanded as an input, and the
#: call is anchored against a preceding word or dot so an attribute form
#: (p.open("w")) cannot match and hand back the mode string as a path. The
#: four stdlib module-level opens are re-admitted by name: the bare anchor
#: dropped gzip.open("data/x.csv.gz") entirely, so a missing compressed input
#: passed referenced_data_files_exist, an affirmative green on a check that
#: promises every file the notebook reads exists. Their mode sits in the same
#: second-positional/mode= shapes the mode pattern already reads.
_OPEN_CALL_RE = re.compile(
    r"(?<![\w.])(?:(?:gzip|io|bz2|lzma)\.)?open\(\s*['\"]([^'\"]+)['\"]([^)]*)"
)
#: the mode within an open() argument list: the second positional literal, or
#: a mode= keyword anywhere among the others (open(p, encoding=..., mode="w")).
_MODE_ARG_RE = re.compile(
    r"^\s*,\s*['\"]([^'\"]*)['\"]|[,(]\s*mode\s*=\s*['\"]([^'\"]*)['\"]"
)
#: any of these in a mode string means the call creates or appends to the file.
#: '+' is deliberately absent: 'r+' reads an existing file (and so is a real
#: input), while every creating variant ('w+', 'a+', 'x+') carries its own
#: letter here anyway.
_WRITE_MODE_CHARS = frozenset("wax")
_URL_RE = re.compile(r"^[a-zA-Z][a-zA-Z0-9+.-]*://")
_ABS_RE = re.compile(r"^(/|~|[A-Za-z]:[\\/])")
#: IPython's line-transform escapes. A cell carrying one can execute under
#: an IPython kernel even though compile() refuses it, so the fallback gate
#: in _strip_comments screens these out before trusting compile(): the six
#: escape prefixes (! % ? , ; /), the assignment-from-shell/magic form
#: ('files = !ls', 'out = %timeit -o f()') and the trailing-help form
#: ('df.groupby?'). A screen over IPython's documented line transforms, not
#: a parser: a matching line in a string literal still holds the cell out,
#: which only keeps comments (the safer failure).
_IPYTHON_LINE_RE = re.compile(
    r"^\s*[!%?,;/]"
    r"|^\s*[\w.]+(?:\s*,\s*[\w.]+)*\s*=\s*[!%]"
    r"|\?{1,2}\s*$",
    re.MULTILINE,
)


def _shipped_input(referenced: str, nb_dir: Path, submission_dir: Path) -> bool:
    """True if *referenced* names a file shipped inside the submission.

    Resolved against the NOTEBOOK's own directory, because that is what the
    read resolves against when the student runs the cell, so a nested
    ``notebooks/report.ipynb`` reading ``../data/cleaned.csv`` is a
    legitimate in-tree read, while a top-level notebook reading the same
    thing is not.

    A target that resolves outside *submission_dir* is not shipped, whatever
    is at the other end: a read of ``../../config.json`` or
    ``../P401002/data/cleaned.csv`` would otherwise be answered by the
    marker's own config or a classmate's tree. It counts as missing rather
    than being dropped from the count: dropping it makes a submission whose
    ONLY read escapes pass on an empty list, the vacuous green this check
    exists to refuse. Backslashes are folded so a Windows-authored
    ``..\\data\\x.csv`` is judged as the escape it is.
    """
    target = nb_dir / referenced.replace("\\", "/")
    try:
        resolved = target.resolve()
    except OSError:
        return False
    return resolved.is_relative_to(submission_dir) and resolved.is_file()


def find_cleaned_csv(submission_dir: Path, schema: dict) -> Path | None:
    """Locate the cleaned CSV: the schema's declared path, else data/*.csv.

    The data/ fallback matches the .csv extension case-insensitively; the
    schema-declared path is taken as written.
    """
    submission_dir = Path(submission_dir)
    declared = submission_dir / schema.get("file", "data/cleaned.csv")
    if declared.is_file():
        return declared
    data_dir = submission_dir / "data"
    fallbacks = sorted(
        p for p in data_dir.glob("*")
        if p.is_file() and p.suffix.lower() == ".csv"
    ) if data_dir.is_dir() else []
    return fallbacks[0] if fallbacks else None


def _value_matches(value: str, dtype: str) -> bool:
    """True if *value* parses as *dtype*; empty cells count as missing, ok."""
    if value == "":
        return True
    if dtype == "integer":
        try:
            int(value)
            return True
        except ValueError:
            return False
    if dtype == "number":
        try:
            float(value)
            return True
        except ValueError:
            return False
    return True  # "string" and unknown types accept anything


def _read_rows(path: Path) -> tuple[list[str], list[dict]] | None:
    """(header, rows-as-dicts) or None when the file is not readable CSV."""
    try:
        with open(path, "r", encoding="utf-8-sig", newline="") as handle:
            reader = csv.DictReader(handle)
            header = reader.fieldnames
            if not header:
                return None
            rows = []
            for i, row in enumerate(reader):
                if i >= _MAX_ROWS:
                    break
                rows.append(row)
            return list(header), rows
    except (OSError, UnicodeDecodeError, csv.Error):
        return None


def _schema_results(csv_path: Path | None, schema: dict) -> list[dict]:
    """Results for the five cleaned-CSV checks."""
    if csv_path is None:
        results = [make_result("cleaned_csv_present", False, STATUS_OK)]
        results.extend(
            make_result(cid, None, STATUS_ARTEFACT_MISSING)
            for cid in CSV_CHECK_IDS[1:5]
        )
        return results

    results = [make_result("cleaned_csv_present", True, STATUS_OK)]
    parsed = _read_rows(csv_path)
    if parsed is None:
        results.append(make_result("cleaned_csv_parses", False, STATUS_OK))
        results.extend(
            make_result(cid, None, STATUS_EXTRACTION_FAILED)
            for cid in CSV_CHECK_IDS[2:5]
        )
        return results
    header, rows = parsed
    results.append(make_result("cleaned_csv_parses", True, STATUS_OK))

    key_columns = list(schema.get("keyColumns", []))
    keys_present = all(col in header for col in key_columns)
    results.append(make_result("cleaned_csv_key_columns_present",
                               keys_present, STATUS_OK))

    dtypes = dict(schema.get("dtypes", {}))
    dtypes_ok = all(
        _value_matches(row.get(col) or "", dtype)
        for row in rows
        for col, dtype in dtypes.items()
        if col in header
    )
    results.append(make_result("cleaned_csv_dtypes_ok", dtypes_ok, STATUS_OK))

    if keys_present and key_columns:
        seen: set[tuple] = set()
        no_dupes = True
        for row in rows:
            key = tuple(row.get(col) or "" for col in key_columns)
            if key in seen:
                no_dupes = False
                break
            seen.add(key)
        results.append(make_result("cleaned_csv_no_duplicate_keys",
                                   no_dupes, STATUS_OK))
    else:
        results.append(make_result("cleaned_csv_no_duplicate_keys", None,
                                   STATUS_EXTRACTION_FAILED))
    return results


def _strip_line_comment(line: str) -> str:
    """Drop the first unquoted ``#`` and everything after it from *line*."""
    quote = ""
    i = 0
    while i < len(line):
        ch = line[i]
        if quote:
            if ch == "\\":
                i += 2
                continue
            if ch == quote:
                quote = ""
        elif ch in "\"'":
            quote = ch
        elif ch == "#":
            return line[:i]
        i += 1
    return line


def _strip_comments(source: str) -> str:
    """Blank comment spans so commented-out code is never read as live.

    Tokenize-based so a ``#`` inside a string literal survives; a stray
    ERRORTOKEN (an IPython ``?`` suffix) does not raise. On a cell
    tokenize refuses outright (a bracket left open at the end of the
    cell), fall back to a quote-aware per-line scan, but only when the
    cell carries no IPython escape syntax and compiling the raw cell
    fails too. compile() failing does not by itself mean the cell
    never runs: an IPython kernel executes cells CPython refuses (a
    ``!`` shell escape, a ``%`` magic, trailing ``?`` help, an
    assignment from a shell command), so any line matching
    _IPYTHON_LINE_RE holds the whole cell out of the scan first, and
    it also compiles cells carrying top-level ``await`` (autoawait),
    which can sit mid-expression where no line screen sees it, so the
    gate compiles with IPython's own ``PyCF_ALLOW_TOP_LEVEL_AWAIT``
    flag rather than plain compile()'s stricter view. A screened
    cell, like one that compiles, keeps its comments: the
    per-line scan carries no multi-line string state, so it can blank a
    genuinely executed read (a triple-quoted string whose closing line
    starts with ``#``), and counting a commented read is the safer
    failure. Both arms scan the source with ``\\r\\n`` and ``\\r``
    normalised to ``\\n`` first (compile()'s universal-newline view),
    except one known 3.11 edge: a trailing backslash before a final
    ``\\r\\n`` compiles raw but not normalised, which is why the gate
    above compiles the raw source rather than the normalised one. The
    gate's ``compile()`` is parse-only (nothing executes) and runs
    with warnings suppressed, so an invalid escape in a refused cell
    never prints a SyntaxWarning over the student checklist. The live
    hazard the normalisation closes is the lone ``\\r``: the
    pure-Python tokenizer on Python <= 3.11 swallows it and the live
    code after it into the COMMENT token while the notebook executes
    that code at runtime; ``\\r\\n`` already ends a comment there and
    is normalised for parity with that view alone. Lines are then
    split on newlines only: tokenize numbers rows by newline, and a
    splitlines()-style split would desync on any of its other
    terminators inside a string literal (``\\v``, form feed,
    ``\\x1c``-``\\x1e``, ``\\x85``, U+2028, U+2029) and blank the
    wrong line.
    """
    raw = source
    source = source.replace("\r\n", "\n").replace("\r", "\n")
    try:
        readline = io.StringIO(source).readline
        spans = [(tok.start, tok.end)
                 for tok in tokenize.generate_tokens(readline)
                 if tok.type == tokenize.COMMENT]
    except (tokenize.TokenError, IndentationError, SyntaxError, ValueError):
        if _IPYTHON_LINE_RE.search(source):
            return source
        try:
            with warnings.catch_warnings():
                warnings.simplefilter("ignore")
                compile(raw, "<cell>", "exec",
                        flags=ast.PyCF_ALLOW_TOP_LEVEL_AWAIT)
        except (SyntaxError, ValueError):
            return "\n".join(_strip_line_comment(line)
                             for line in source.split("\n"))
        return source
    lines = source.split("\n")
    for (srow, scol), (erow, ecol) in spans:
        line = lines[srow - 1]
        lines[srow - 1] = line[:scol] + " " * (ecol - scol) + line[ecol:]
    return "\n".join(lines)


def referenced_data_paths(nb: dict) -> list[str]:
    """Relative data-file paths the notebook's code cells read.

    URLs and absolute paths are skipped (an absolute-path flag is a separate
    professionalism concern, not this check). A path the notebook only WRITES
    is not a path it reads: demanding it be shipped fails a complete
    submission over a file the student never opened for input. Comments are
    stripped first: delivery templates scaffold the data load as commented
    lines to uncomment, and a commented read is not a read. Whether a
    relative path stays inside the submission is decided by
    ``_shipped_input``, against the notebook's own directory, not here,
    where neither directory is known.
    """
    paths: list[str] = []
    for cell in (c for c in nb.get("cells", []) if isinstance(c, dict)):
        if cell.get("cell_type") != "code":
            continue
        source = _strip_comments(cell_source(cell))
        candidates = [m.group(1) for m in _READ_CALL_RE.finditer(source)]
        for match in _OPEN_CALL_RE.finditer(source):
            rest = match.group(2) or ""
            mode_match = _MODE_ARG_RE.search(rest)
            mode = ""
            if mode_match:
                mode = mode_match.group(1) or mode_match.group(2) or ""
            if set(mode) & _WRITE_MODE_CHARS:
                continue
            candidates.append(match.group(1))
        for candidate in candidates:
            if _URL_RE.match(candidate) or _ABS_RE.match(candidate):
                continue
            if candidate not in paths:
                paths.append(candidate)
    return paths


def _referenced_files_result(submission_dir: Path,
                             notebook: Path | None) -> dict:
    nb_path = Path(notebook) if notebook else find_notebook(submission_dir)
    if nb_path is None:
        return make_result("referenced_data_files_exist", None,
                           STATUS_ARTEFACT_MISSING)
    nb, error = load_notebook(nb_path)
    if error == "file_missing":
        return make_result("referenced_data_files_exist", None,
                           STATUS_ARTEFACT_MISSING)
    if nb is None:
        return make_result("referenced_data_files_exist", None,
                           STATUS_EXTRACTION_FAILED)
    referenced = referenced_data_paths(nb)
    base = Path(submission_dir).resolve()
    nb_dir = nb_path.parent.resolve()
    all_exist = all(_shipped_input(path, nb_dir, base) for path in referenced)
    return make_result("referenced_data_files_exist", all_exist, STATUS_OK)


def run_csv_checks(submission_dir: Path, schema: dict | None = None,
                   notebook: Path | None = None) -> list[dict]:
    """Run the data-management battery over *submission_dir*.

    *schema* defaults to the published CLEANED_CSV_SCHEMA; individual-mode
    callers may pass a dataset-specific dict of the same shape.
    """
    submission_dir = Path(submission_dir)
    schema = schema or CLEANED_CSV_SCHEMA
    results = _schema_results(find_cleaned_csv(submission_dir, schema), schema)
    results.append(_referenced_files_result(submission_dir, notebook))
    return results

# ===========================================================================
# embedded from tooling/marking/checks/figures_checks.py
# ===========================================================================

"""Tier-1 figure checks: PNG count and header-derived dimensions.

Counts saved PNG files and parses each PNG's IHDR header (pure stdlib, no
image library) for its pixel dimensions. Counts inform, never select, a
band; the smallest-width metric is explicitly indicative.
"""


import struct
from pathlib import Path


FIGURES_CHECK_IDS: tuple[str, ...] = (
    "n_figures",
    "n_figures_readable",
    "n_figures_unreadable",
    "min_figure_width_px",
)

_PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


def png_dimensions(path: Path) -> tuple[int, int] | None:
    """(width, height) from a PNG's IHDR header, or None if not a valid PNG."""
    try:
        with open(path, "rb") as handle:
            head = handle.read(24)
    except OSError:
        return None
    if len(head) < 24 or not head.startswith(_PNG_SIGNATURE):
        return None
    if head[12:16] != b"IHDR":
        return None
    width, height = struct.unpack(">II", head[16:24])
    if width <= 0 or height <= 0:
        return None
    return width, height


def find_figures(submission_dir: Path) -> list[Path]:
    """Every .png (any case) in the submission, hidden directories excluded,
    sorted."""
    submission_dir = Path(submission_dir)
    return sorted(
        p for p in submission_dir.rglob("*")
        if p.is_file() and p.suffix.lower() == ".png"
        and not any(part.startswith(".")
                    for part in p.relative_to(submission_dir).parts)
    )


def run_figures_checks(submission_dir: Path) -> list[dict]:
    """Run the figure battery over *submission_dir*; list of results.

    Zero PNGs is reported as a true count of 0 (the taught convention is
    saved figures); the dimension checks then carry no automated evidence.
    """
    figures = find_figures(Path(submission_dir))
    results = [make_result("n_figures", len(figures), STATUS_OK)]
    if not figures:
        results.append(make_result("n_figures_readable", None,
                                   STATUS_ARTEFACT_MISSING))
        results.append(make_result("n_figures_unreadable", None,
                                   STATUS_ARTEFACT_MISSING))
        results.append(make_result("min_figure_width_px", None,
                                   STATUS_ARTEFACT_MISSING))
        return results

    widths = []
    readable = 0
    for figure in figures:
        dimensions = png_dimensions(figure)
        if dimensions is not None:
            readable += 1
            widths.append(dimensions[0])
    results.append(make_result("n_figures_readable", readable, STATUS_OK))
    # The readable count with expect min 1 cannot say "every figure found
    # must parse" (one good PNG beside a corrupt one is green); the
    # unreadable count with expect max 0 can.
    results.append(make_result("n_figures_unreadable", len(figures) - readable,
                               STATUS_OK))
    if widths:
        results.append(make_result("min_figure_width_px", min(widths),
                                   STATUS_OK))
    else:
        results.append(make_result("min_figure_width_px", None,
                                   STATUS_ARTEFACT_MISSING))
    return results

# ===========================================================================
# embedded from tooling/marking/checks/manifest_checks.py
# ===========================================================================

"""Tier-1 bundle-manifest checks: manifest.json parses and validity floor.

The validity floor (DATA_MODEL.md §3.9) is: the manifest
parses AND lists at least one payload file. Sub-floor bundles are flagged,
never rejected: students resubmit within the window. Before bundle.py has
run, no manifest exists and both checks report artefact_missing, which the
feedforward explains is normal.
"""


import json
from pathlib import Path


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

# ===========================================================================
# embedded from tooling/marking/checks/__init__.py
# ===========================================================================

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


from pathlib import Path



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


# ===========================================================================
# Student CLI harness (added by precheck_dist.py; not part of marklib)
# ===========================================================================

import argparse
import sys

CHECK_PY_VERSION = TIER1_VERSION

_DOI_RE = re.compile(r"\b10\.\d{4,9}/[^\s\"'<>)\]]+")

_OFFLINE_NOTE = (
    "Crossref DOI check skipped (offline). Indicative only: non-DOI and "
    "non-Crossref scholarship is counted by your marker, not this tool."
)


def _extract_dois(submission_dir, notebook=None):
    """DOIs found in the notebook's markdown cells (deduplicated, in order)."""
    nb_path = Path(notebook) if notebook else find_notebook(submission_dir)
    if nb_path is None:
        return []
    nb, error = load_notebook(nb_path)
    if nb is None:
        return []
    dois = []
    for cell in (c for c in nb.get("cells", []) if isinstance(c, dict)):
        if cell.get("cell_type") != "markdown":
            continue
        for match in _DOI_RE.finditer(cell_source(cell)):
            doi = match.group(0).rstrip(".,;:)")
            if doi not in dois:
                dois.append(doi)
    return dois


def _resolve_dois_crossref(dois, cache):
    """Best-effort Crossref lookups; returns {doi: bool}. Never raises.

    Cached results are reused, not re-fetched. Network failures leave a DOI
    out of the result rather than mis-reporting it.
    """
    import urllib.error
    import urllib.parse
    import urllib.request

    resolved = dict(cache)
    for doi in dois:
        if doi in resolved:
            continue
        url = "https://api.crossref.org/works/" + urllib.parse.quote(doi)
        request = urllib.request.Request(
            url, headers={"User-Agent": "student-check.py (Tier-1 self-check)"}
        )
        try:
            with urllib.request.urlopen(request, timeout=10) as response:
                resolved[doi] = 200 <= response.status < 300
        except urllib.error.HTTPError as exc:
            if exc.code == 404:
                resolved[doi] = False
        except Exception:  # noqa: BLE001; best-effort, offline-safe
            pass
    return resolved


def _load_cached_crossref(report_path):
    """Previously-resolved DOIs from an earlier precheck-report.json."""
    try:
        with open(report_path, "r", encoding="utf-8") as handle:
            previous = json.load(handle)
        cached = previous.get("crossref", {}).get("resolved", {})
        return {k: v for k, v in cached.items() if isinstance(v, bool)}
    except Exception:  # noqa: BLE001
        # json.load's failure class is open-ended, not just JSONDecodeError:
        # a bare ValueError for an integer over CPython's digit limit, a
        # RecursionError for a deeply nested document. The report being read
        # is a file on the student's own disk that anything may have
        # corrupted, and this whole tool promises never to raise for bad
        # input. A stale cache is worth nothing, so drop it and re-resolve.
        return {}


def _result_ok(result):
    """A check 'needs a look' when it failed judgement or did not run.

    Informational results (ran, no declared expectation) are never red:
    the renderer has nothing to judge them against (iss-126).
    """
    return result["status"] == STATUS_OK and judge_result(result) is not False


def _print_checklist(results):
    """The projected feed-forward checklist. Red never blocks shipping."""
    print("Tier-1 self-check v" + CHECK_PY_VERSION)
    print("(identical code to your marker's checks; feed-forward, not a mark)")
    print("( [+] pass  [x] fix  [.] indicative info  [-] no evidence )")
    print()
    for result in results:
        judged = judge_result(result)
        if result["status"] != STATUS_OK:
            symbol, note = "-", "no automated evidence"
        elif judged is False:
            symbol, note = "x", str(result["value"])
        elif judged is True:
            symbol, note = "+", str(result["value"])
        else:
            symbol, note = ".", "{} (indicative only)".format(result["value"])
        print(" [{}] {}: {}".format(symbol, result["id"], note))
        if symbol in ("x", "-"):
            print("      fix: {}".format(result["feedforward"]))
    print()


def _write_report(report_path, results, crossref):
    """Write precheck-report.json (schema mn5813.precheck/1)."""
    report = {
        "schema": "mn5813.precheck/1",
        "toolVersion": CHECK_PY_VERSION,
        "tier1": {
            "checks": [
                {
                    "id": r["id"],
                    "ok": _result_ok(r),
                    "value": r["value"],
                    "status": r["status"],
                    "hint": r["feedforward"],
                }
                for r in results
            ]
        },
    }
    if crossref is not None:
        report["crossref"] = crossref
    with open(report_path, "w", encoding="utf-8") as handle:
        json.dump(report, handle, indent=2, sort_keys=True)
        handle.write("\n")


def main(argv=None):
    """Run the Tier-1 battery, print the checklist, write the report."""
    parser = argparse.ArgumentParser(
        description="Student self-check (Tier 1, feed-forward only)."
    )
    parser.add_argument("path", nargs="?", default=".",
                        help="your work folder (default: current folder)")
    parser.add_argument("--notebook", default=None,
                        help="notebook file (default: auto-detect)")
    parser.add_argument(
        "--resolve-dois", action="store_true",
        help="optionally ask Crossref whether the DOIs in your notebook "
             "resolve (the only network use; indicative only)",
    )
    parser.add_argument(
        "--offline-safe", action="store_true",
        help="never touch the network, even with --resolve-dois",
    )
    parser.add_argument("--report", default="precheck-report.json",
                        help="report filename (default: precheck-report.json)")
    args = parser.parse_args(argv)

    submission = Path(args.path).resolve()
    if not submission.is_dir():
        print("check.py: not a folder: {}".format(submission), file=sys.stderr)
        return 2

    if not (submission / ".git").exists():
        print("Tip: this folder is not a git repository. `git commit` is the"
              " habit you keep; the zip is how this university receives it.")
        print()

    notebook = submission / args.notebook if args.notebook else None
    results = run_tier1(submission, notebook=notebook)
    _print_checklist(results)

    report_path = submission / args.report
    crossref = None
    if args.resolve_dois:
        dois = _extract_dois(submission, notebook=notebook)
        cache = _load_cached_crossref(report_path)
        if args.offline_safe:
            print(_OFFLINE_NOTE)
            crossref = {"note": _OFFLINE_NOTE, "resolved": cache}
        elif not dois:
            print("Crossref DOI check: no DOIs found in your notebook's "
                  "markdown cells.")
            crossref = {"note": "no DOIs found", "resolved": cache}
        else:
            resolved = _resolve_dois_crossref(dois, cache)
            note = ("Indicative only: non-DOI and non-Crossref scholarship "
                    "is counted by your marker, not this tool.")
            print("Crossref DOI check ({}):".format(note))
            for doi in dois:
                if doi in resolved:
                    state = "resolves" if resolved[doi] else "does NOT resolve"
                else:
                    state = "could not be checked (offline?)"
                print("  {}: {}".format(doi, state))
            crossref = {"note": note, "resolved": resolved}
        print()

    _write_report(report_path, results, crossref)
    n_red = sum(1 for r in results if not _result_ok(r))
    print("Report written to {}".format(report_path))
    print("{} of {} checks need a look. Ship red is fine: a failing "
          "self-check never delays shipping.".format(n_red, len(results)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
