"""Tier-1 reference checks: reference-section presence and indicative count.

The count is honest about being a heuristic: it is labelled "~detected,
verify", and the patterns are style-robust; its feedforward states
that non-standard reference formats are counted by the marker, not the tool.
Patterns accept numbered lists, bracketed numbers, bullets, and
author-(year) lines so APA/Harvard/ACM styles all count.
"""

from __future__ import annotations

import re
from pathlib import Path

from .catalogue import (
    STATUS_ARTEFACT_MISSING,
    STATUS_EXTRACTION_FAILED,
    STATUS_OK,
    make_result,
)
from .notebook_checks import cell_source, find_notebook, load_notebook

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
