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

from __future__ import annotations

import ast
import csv
import io
import re
import tokenize
import warnings
from pathlib import Path

from .catalogue import (
    STATUS_ARTEFACT_MISSING,
    STATUS_EXTRACTION_FAILED,
    STATUS_OK,
    make_result,
)
from .notebook_checks import cell_source, find_notebook, load_notebook

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
