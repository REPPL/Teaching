#!/usr/bin/env python3
"""Fetch the London Fire Brigade records once and write the group-project tables.

    python3 Tools/fetch_lfb.py            # download, trim, write work/data/lfb/
    python3 Tools/fetch_lfb.py --check    # verify the tables match the manifest
    python3 Tools/fetch_lfb.py --selftest # prove the trim on a tiny extract

The group project analyses the London Fire Brigade's open incident and
mobilisation records, published by the Greater London Authority on the
London Datastore under the Open Government Licence v2. Nothing is hosted in
this repository: this script downloads the two current extracts, keeps the
rows and columns the brief names, and writes two tables and a manifest into
the student's work/data/lfb/ folder, which work/.gitignore keeps out of git. Run it once per workstation with network access;
later runs reuse the cached downloads and reproduce the same tables, and
`--check` proves it.

What is kept: every incident and every mobilisation dated 1 January 2025 or
later (the mobilisation extract starts there, and the two tables should
cover the same months), and the columns listed in COLUMNS below. Postcodes,
property references and coordinates are already redacted by the publisher
for incidents at dwellings; this script drops the remaining full postcodes
and coordinates, keeping the postcode district, borough, ward and station
ground, so the tables carry no location finer than a district.

What a referenced dataset can and cannot promise: the publisher refreshes
these extracts (incidents quarterly, mobilisations monthly) at the same
URLs. A workstation that has fetched once keeps its cached download (under
`~/.cache/mn5813-fetch/`, outside the delivery), so its
tables never change. A workstation that first fetches after a refresh gets
more recent rows. The manifest records each download's size and SHA-256 and
each table's row count, so two teammates can tell in one glance whether
they hold the same cut; the data note (Assessment/lfb-data.md) asks every
team to compare manifests in the first block of the Week 7 Sprint Zero and,
if they differ, to copy one member's work/data/lfb/ folder to the others.

Tables written (gzipped CSV; the data note describes every column):

    incidents.csv.gz      one row per 999 incident
    mobilisations.csv.gz  one row per fire engine sent to an incident

Needs the delivery's Python environment (pandas, openpyxl, requests).
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import io
import json
import os
import pathlib
import shutil
import sys
import tempfile
from datetime import datetime, timezone

def find_work(tools: pathlib.Path) -> pathlib.Path:
    """The work/ folder the fetched data goes in.

    Published, work/ sits at the root of the student's repository, two
    folders above Tools/ (<repo>/<module>/<year>/Tools); in the source tree it
    sits beside Tools/. So walk up from Tools/ to the first folder that holds
    a work/ folder, stopping at the repository root (the folder that holds
    .git), whose work/ is used even before it exists.
    """
    for folder in tools.parents:
        if (folder / "work").is_dir() or (folder / ".git").exists():
            return folder / "work"
    return tools.parent / "work"


HERE = pathlib.Path(__file__).resolve().parent
# The data lives in the student's work/ folder, never in Tools/: find_work()
# says where that is. OLD_DIR is where earlier versions wrote; the next run
# moves a copy found there across.
WORK = find_work(HERE)
OUT_DIR = WORK / "data" / "lfb"
OLD_DIR = HERE / "data" / "lfb"
# The raw downloads are scratch (about 150 MB): they live in the user's cache
# directory, outside the delivery, and are reused on every later run.
# Override with FETCH_LFB_CACHE to put them elsewhere.
CACHE_DIR = pathlib.Path(os.environ.get("FETCH_LFB_CACHE")
                         or pathlib.Path.home() / ".cache" / "mn5813-fetch" / "lfb")

SOURCES = {
    "incidents": {
        "url": "https://data.london.gov.uk/download/em8xy/58m/LFB%20Incident%20data%20from%202024%20onwards.xlsx",
        "page": "https://data.london.gov.uk/dataset/london-fire-brigade-incident-records-em8xy",
        "cache": "incidents.xlsx",
        "kind": "xlsx",
    },
    "mobilisations": {
        "url": "https://data.london.gov.uk/download/24r65/7d5b4e2f-3ddb-48b9-8a4d-bf86bdf6a4ef/LFB%20Mobilisation%20data%20from%202025.csv",
        "page": "https://data.london.gov.uk/dataset/london-fire-brigade-mobilisation-records-24r65/",
        "cache": "mobilisations.csv",
        "kind": "csv",
    },
}
LICENCE = "Open Government Licence v2 (contains public sector information licensed under the OGL v2.0; source: London Fire Brigade via the London Datastore)"
CUT_FROM = "2025-01-01"

COLUMNS = {
    "incidents": [
        "IncidentNumber", "DateOfCall", "CalYear", "TimeOfCall", "HourOfCall",
        "IncidentGroup", "StopCodeDescription", "SpecialServiceType",
        "PropertyCategory", "PropertyType", "AddressQualifier", "Postcode_district",
        "IncGeo_BoroughCode", "IncGeo_BoroughName", "IncGeo_WardCode", "IncGeo_WardName",
        "IncidentStationGround",
        "FirstPumpArriving_AttendanceTime", "FirstPumpArriving_DeployedFromStation",
        "SecondPumpArriving_AttendanceTime", "SecondPumpArriving_DeployedFromStation",
        "NumStationsWithPumpsAttending", "NumPumpsAttending", "PumpCount",
        "PumpMinutesRounded", "Notional Cost (£)", "NumCalls",
    ],
    "mobilisations": [
        "IncidentNumber", "CalYear", "BoroughName", "WardName", "HourOfCall",
        "ResourceMobilisationId", "Resource_Code", "PerformanceReporting",
        "DateAndTimeMobilised", "DateAndTimeMobile", "DateAndTimeArrived",
        "TurnoutTimeSeconds", "TravelTimeSeconds", "AttendanceTimeSeconds",
        "DateAndTimeLeft", "DateAndTimeReturned",
        "DeployedFromStation_Code", "DeployedFromStation_Name", "DeployedFromLocation",
        "PumpOrder", "PlusCode_Code", "PlusCode_Description",
        "DelayCodeId", "DelayCode_Description",
    ],
}
DATE_COLUMN = {"incidents": "DateOfCall", "mobilisations": "DateAndTimeMobilised"}
DATE_FORMAT = {"incidents": None, "mobilisations": "%d/%m/%Y %H:%M"}


# --- helpers ----------------------------------------------------------------

def sha256_of(path: pathlib.Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def say(msg: str) -> None:
    print(msg, flush=True)


def show(path: pathlib.Path) -> str:
    """*path* as the pages name it: from the folder that holds work/ or Tools/."""
    for base in (WORK.parent, HERE.parent):
        if path.is_relative_to(base):
            return path.relative_to(base).as_posix()
    return str(path)


def move_old_data(old: pathlib.Path, new: pathlib.Path) -> None:
    """Move tables an earlier version wrote under Tools/data/ to work/data/,
    so nobody downloads them again. When both exist, the new copy wins."""
    if old.is_dir() and not new.exists():
        new.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(old), str(new))
        say(f"moved {show(old)}/ to {show(new)}/ (the data now lives in work/)")
        try:
            old.parent.rmdir()  # Tools/data/, once nothing else is in it
        except OSError:
            pass
    elif old.is_dir():
        say(f"note: {show(new)}/ is in use; the older copy in {show(old)}/ can be deleted")


def require_deps() -> None:
    try:
        import pandas  # noqa: F401
        import openpyxl  # noqa: F401
        import requests  # noqa: F401
    except ImportError as exc:
        print(f"fetch_lfb: missing {exc.name}. Run this script with the delivery's Python "
              f"environment (the Codespace has it; locally, install requirements.lock).", file=sys.stderr)
        sys.exit(2)


# --- fetch --------------------------------------------------------------------

def download(name: str, cache_dir: pathlib.Path) -> pathlib.Path:
    import requests
    src = SOURCES[name]
    dest = cache_dir / src["cache"]
    if dest.is_file() and dest.stat().st_size > 0:
        say(f"reusing cached download {dest.name} ({dest.stat().st_size // (1 << 20)} MB)")
        return dest
    say(f"downloading {name} from the London Datastore ...")
    try:
        with requests.get(src["url"], stream=True, timeout=600) as r:
            r.raise_for_status()
            tmp = dest.with_suffix(dest.suffix + ".part")
            with tmp.open("wb") as fh:
                for chunk in r.iter_content(1 << 20):
                    fh.write(chunk)
            tmp.replace(dest)
    except requests.RequestException as exc:
        print(f"fetch_lfb: could not download {src['url']}\n  {type(exc).__name__}: {exc}\n"
              f"  This needs network access. If the URL has changed, find the current file on\n"
              f"  {src['page']} and tell the module team.", file=sys.stderr)
        sys.exit(2)
    say(f"  saved {dest.name} ({dest.stat().st_size // (1 << 20)} MB)")
    return dest


# --- trim -----------------------------------------------------------------------

def trim(name: str, raw: pathlib.Path):
    """The extract as a DataFrame with the brief's columns and the cut applied."""
    import pandas as pd
    if SOURCES[name]["kind"] == "xlsx":
        # The incidents file is a 77 MB spreadsheet; reading it peaks at
        # about 1.2 GB and takes under a minute on a workstation, a few
        # minutes in a default Codespace. A streamed read was measured and
        # saved neither memory nor bytes, so the plain read stays.
        df = pd.read_excel(raw)
    else:
        df = pd.read_csv(raw, low_memory=False)
    missing = [c for c in COLUMNS[name] if c not in df.columns]
    if missing:
        print(f"fetch_lfb: the {name} extract no longer carries these columns: {missing}\n"
              f"  The publisher has changed the file; tell the module team.", file=sys.stderr)
        sys.exit(1)
    df = df[COLUMNS[name]].copy()
    date_col = DATE_COLUMN[name]
    parsed = pd.to_datetime(df[date_col], format=DATE_FORMAT[name], errors="coerce")
    df = df[parsed >= pd.Timestamp(CUT_FROM)].copy()
    # A stable row order, so the same input always gives the same bytes.
    keys = ["IncidentNumber"] + (["ResourceMobilisationId"] if name == "mobilisations" else [])
    df = df.sort_values(keys, kind="mergesort").reset_index(drop=True)
    return df


def write_table(df, path: pathlib.Path) -> tuple[int, str]:
    buf = io.StringIO()
    df.to_csv(buf, index=False, lineterminator="\n")
    data = buf.getvalue().encode("utf-8")
    with gzip.GzipFile(filename="", mode="wb", fileobj=path.open("wb"), mtime=0) as gz:
        gz.write(data)
    return len(df), sha256_of(path)


def run_fetch(out_dir: pathlib.Path = OUT_DIR, cache_dir: pathlib.Path = CACHE_DIR) -> int:
    require_deps()
    cache_dir.mkdir(parents=True, exist_ok=True)
    out_dir.mkdir(parents=True, exist_ok=True)
    manifest = {
        "dataset": "London Fire Brigade incident and mobilisation records",
        "licence": LICENCE, "cut_from": CUT_FROM,
        "fetched_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "sources": {}, "tables": {},
    }
    for name in SOURCES:
        raw = download(name, cache_dir)
        manifest["sources"][name] = {"url": SOURCES[name]["url"], "page": SOURCES[name]["page"],
                                     "bytes": raw.stat().st_size, "sha256": sha256_of(raw)}
        say(f"trimming {name} ...")
        df = trim(name, raw)
        path = out_dir / f"{name}.csv.gz"
        n, digest = write_table(df, path)
        manifest["tables"][name] = {"file": path.name, "rows": n, "columns": list(df.columns), "sha256": digest}
        say(f"  wrote {show(path)}  ({n} rows, {len(df.columns)} columns)")
    (out_dir / "manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    say(f"wrote {show(out_dir / 'manifest.json')}")
    say(f"done: records from {CUT_FROM}, two tables under {show(out_dir)}")
    return 0


def run_check(out_dir: pathlib.Path = OUT_DIR) -> int:
    mpath = out_dir / "manifest.json"
    if not mpath.is_file():
        print(f"fetch_lfb: no manifest at {mpath}; run the script without --check first", file=sys.stderr)
        return 1
    manifest = json.loads(mpath.read_text(encoding="utf-8"))
    bad = 0
    for meta in manifest["tables"].values():
        path = out_dir / meta["file"]
        if not path.is_file():
            say(f"MISSING {meta['file']}")
            bad += 1
        elif sha256_of(path) != meta["sha256"]:
            say(f"CHANGED {meta['file']} (does not match the manifest)")
            bad += 1
        else:
            say(f"ok      {meta['file']}  ({meta['rows']} rows)")
    say("all tables match the manifest" if not bad else f"{bad} problem(s)")
    return 1 if bad else 0


# --- selftest ------------------------------------------------------------------------

def selftest() -> int:
    require_deps()
    import pandas as pd
    fails = 0

    def expect(name: str, ok: bool, detail: str = "") -> None:
        nonlocal fails
        print(("  ✓ " if ok else "  ✗ ") + name)
        if not ok:
            fails += 1
            if detail:
                print("      " + detail[:300])

    with tempfile.TemporaryDirectory(prefix="fetch-lfb-selftest-") as tmp:
        root = pathlib.Path(tmp)
        inc = pd.DataFrame({c: ["x"] * 3 for c in COLUMNS["incidents"]})
        inc["IncidentNumber"] = ["000002-01012024", "000001-02012025", "000003-03032025"]
        inc["DateOfCall"] = pd.to_datetime(["2024-01-01", "2025-01-02", "2025-03-03"])
        inc["Postcode_full"] = ["N2 8AY", "SW1A 1AA", None]
        inc["Latitude"] = [51.5, 51.6, None]
        inc.to_excel(root / "incidents.xlsx", index=False)
        mob = pd.DataFrame({c: ["y"] * 3 for c in COLUMNS["mobilisations"]})
        mob["IncidentNumber"] = ["000001-02012025", "000001-02012025", "000003-03032025"]
        mob["ResourceMobilisationId"] = [2, 1, 3]
        mob["DateAndTimeMobilised"] = ["02/01/2025 00:02", "02/01/2025 00:02", "03/03/2025 10:00"]
        mob.to_csv(root / "mobilisations.csv", index=False)
        a = trim("incidents", root / "incidents.xlsx")
        expect("the incident cut drops rows before 2025", list(a["IncidentNumber"]) == ["000001-02012025", "000003-03032025"])
        expect("full postcodes and coordinates are dropped", "Postcode_full" not in a.columns and "Latitude" not in a.columns)
        expect("the brief's columns are kept, in order", list(a.columns) == COLUMNS["incidents"])
        b = trim("mobilisations", root / "mobilisations.csv")
        expect("mobilisations parse DD/MM/YYYY and keep all three rows", len(b) == 3)
        expect("rows sort by incident then mobilisation id", list(b["ResourceMobilisationId"]) == [1, 2, 3])
        out = root / "out"; out.mkdir()
        h1 = write_table(a, out / "incidents.csv.gz")[1]
        h2 = write_table(a, out / "incidents.csv.gz")[1]
        expect("writing twice gives identical bytes", h1 == h2)
        n, hb = write_table(b, out / "mobilisations.csv.gz")
        (out / "manifest.json").write_text(json.dumps({"tables": {
            "incidents": {"file": "incidents.csv.gz", "rows": 2, "sha256": h1},
            "mobilisations": {"file": "mobilisations.csv.gz", "rows": n, "sha256": hb}}}))
        expect("--check passes on matching tables", run_check(out) == 0)
        (out / "mobilisations.csv.gz").write_bytes(b"changed")
        expect("--check fails on a changed table", run_check(out) == 1)
        bad = inc.drop(columns=["NumCalls"])
        bad.to_excel(root / "bad.xlsx", index=False)
        try:
            trim("incidents", root / "bad.xlsx")
            expect("a missing column is refused", False)
        except SystemExit as exc:
            expect("a missing column is refused", exc.code == 1)
    with tempfile.TemporaryDirectory(prefix="fetch-lfb-selftest-work-") as tmp:
        repo = pathlib.Path(tmp)
        (repo / ".git").mkdir()
        tools = repo / "MOD" / "2000-01" / "Tools"
        tools.mkdir(parents=True)
        expect("work/ is found at the repository root, before it exists", find_work(tools) == repo / "work")
        (repo / "work").mkdir()
        expect("work/ is found two folders above Tools/", find_work(tools) == repo / "work")
        old, new = tools / "data" / "lfb", repo / "work" / "data" / "lfb"
        old.mkdir(parents=True)
        (old / "manifest.json").write_text("{}")
        move_old_data(old, new)
        expect("an old Tools/data copy moves to work/data", (new / "manifest.json").is_file() and not (tools / "data").exists())
    print("\nselftest: " + ("all checks passed" if not fails else f"{fails} failed"))
    return 1 if fails else 0


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--check", action="store_true", help="verify the written tables match the manifest")
    p.add_argument("--selftest", action="store_true", help="prove the trim on a tiny extract")
    a = p.parse_args()
    if a.selftest:
        return selftest()
    move_old_data(OLD_DIR, OUT_DIR)
    if a.check:
        return run_check()
    return run_fetch()


if __name__ == "__main__":
    sys.exit(main())
