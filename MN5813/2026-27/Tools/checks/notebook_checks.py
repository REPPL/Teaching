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

from __future__ import annotations

import json
from pathlib import Path

from .catalogue import (
    STATUS_ARTEFACT_MISSING,
    STATUS_EXTRACTION_FAILED,
    STATUS_OK,
    make_result,
)

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
