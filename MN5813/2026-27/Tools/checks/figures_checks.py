"""Tier-1 figure checks: PNG count and header-derived dimensions.

Counts saved PNG files and parses each PNG's IHDR header (pure stdlib, no
image library) for its pixel dimensions. Counts inform, never select, a
band; the smallest-width metric is explicitly indicative.
"""

from __future__ import annotations

import struct
from pathlib import Path

from .catalogue import STATUS_ARTEFACT_MISSING, STATUS_OK, make_result

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
