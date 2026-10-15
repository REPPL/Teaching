# The group-project data: London Fire Brigade records

*What the data is, where it comes from, how you get it, and the challenges associated with it. Read this before the Week 4 workshop, where your team fetches (i.e., downloads) the data and agrees on a way forward.*


## The data

The London Fire Brigade publishes two tables on the Greater London Authority's London Datastore. One describes every 999 incident the Brigade attended. The other describes every fire engine it sent.

- **Incidents**: One row per 999 call attended, from 1 January 2025 onwards. Each row shows when and where, down to the postcode district, borough, ward, and station ground (the area one fire station covers). It gives the kind of incident (fire, false alarm, or special service) and the kind of property. It also records how long the first and second engines took to arrive, and how many engines and stations attended. It adds the minutes of engine time the incident used, and the Brigade's notional cost of attending (an estimate, not money spent)
- **Mobilisations**: One row per fire engine sent to an incident. Each row gives the station the engine came from, and when it was mobilised, when it was moving, when it arrived, and when it left. It also records the turnout, travel, and attendance times in seconds. Where the crew was held up, a delay code gives the reason (traffic, roadworks, or a wrong address)

The two tables join (match row to row) on `IncidentNumber`. Both are real, current operational data. The publisher refreshes both extracts regularly, and each dataset page shows when it last changed.

Each source page links to the current data file (verify yourself!):

- Incidents: [London Fire Brigade Incident Records](https://data.london.gov.uk/dataset/london-fire-brigade-incident-records-em8xy)
- Mobilisations: [London Fire Brigade Mobilisation Records](https://data.london.gov.uk/dataset/london-fire-brigade-mobilisation-records-24r65/)

The data is published under the [Open Government Licence v2](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/2/). Put the line below in your report, and on every figure you show outside the report.

*Contains public sector information licensed under the Open Government Licence v2.0. Source: London Fire Brigade, via the London Datastore.*


## How to get it

This module's repository hosts no data. One script fetches it:

```bash
python3 Tools/fetch_lfb.py
```

Everyone runs it once, in the Week 4 workshop. Run it in your Codespace, from the folder that contains `Tools/`. It downloads the two current extracts (about 150 MB together). It keeps the rows and columns listed under [What is kept, what is dropped, and why](#what-is-kept-what-is-dropped-and-why). It writes the files below into `work/data/lfb/`, a folder git ignores:

| File | What it contains |
|------|---------------|
| `incidents.csv.gz` | One row per incident dated 1 January 2025 or later |
| `mobilisations.csv.gz` | One row per engine sent |
| `manifest.json` | The URL, size, and checksum of each download, and the row count, columns, and checksum of each table |

The first run takes about three minutes in a default two-core Codespace (you need network access!). It keeps the downloads under `~/.cache/mn5813-fetch/`. Every later run reuses those downloads, needs no network, finishes in under a minute, and writes the same files byte for byte. Run `python3 Tools/fetch_lfb.py --check` to confirm the files are unchanged.

Read the tables with pandas. The example below is for a notebook kept at the top of your `work` folder, next to `data/`. Keep the incident number as text so it has the same type in both tables:

```python
import pandas as pd

incidents = pd.read_csv("data/lfb/incidents.csv.gz", dtype={"IncidentNumber": str})
mobilisations = pd.read_csv("data/lfb/mobilisations.csv.gz", dtype={"IncidentNumber": str}, low_memory=False)
```


## One copy per team

The Brigade updates its files regularly, so teammates who fetch on different days can end up with different data. Your team works from **one copy**.

1. Everyone fetches in the Week 4 workshop. Compare the `sha256` values under `sources` in your `manifest.json` files
2. If they differ, pick one member's copy and give everyone that member's `work/data/lfb/` folder. Log it as `DECISION: working from <name>'s fetch of <date>`
3. One member <!-- plain-language: everyday commit -->commits the two tables and the manifest to the **team repository** (about 20 MB)

Your notebook reads the tables from there, so *Restart & Run All* works for the marker without fetching anything.


## Modifications

**Both tables start on 1 January 2025**, the date the mobilisations extract starts. This means you can join every incident in your table to the engines sent to it. The incidents extract also carries 2024, and the script drops that year.

**Location detail stops at the postcode district.** The publisher removes full postcodes, property references, and coordinates for incidents at people's homes. The script drops the remaining full postcodes and coordinates for every incident. It keeps the postcode district, borough, ward, and station ground. Nothing in your data locates an incident to a building.

**Columns we keep for the incidents table**:

- `IncidentNumber`, `DateOfCall`, `CalYear`, `TimeOfCall`, `HourOfCall`
- `IncidentGroup`, `StopCodeDescription`, `SpecialServiceType`, `PropertyCategory`, `PropertyType`, `AddressQualifier`
- `Postcode_district`, `IncGeo_BoroughCode`, `IncGeo_BoroughName`, `IncGeo_WardCode`, `IncGeo_WardName`, `IncidentStationGround`
- `FirstPumpArriving_AttendanceTime`, `FirstPumpArriving_DeployedFromStation`, `SecondPumpArriving_AttendanceTime`, `SecondPumpArriving_DeployedFromStation`, `NumStationsWithPumpsAttending`, `NumPumpsAttending`, `PumpCount`, `PumpMinutesRounded`, `Notional Cost (£)`, `NumCalls`

**Columns we keep for the mobilisations table**:

- `IncidentNumber`, `CalYear`, `BoroughName`, `WardName`, `HourOfCall`
- `ResourceMobilisationId`, `Resource_Code`, `PerformanceReporting`
- `DateAndTimeMobilised`, `DateAndTimeMobile`, `DateAndTimeArrived`, `TurnoutTimeSeconds`, `TravelTimeSeconds`, `AttendanceTimeSeconds`, `DateAndTimeLeft`, `DateAndTimeReturned`
- `DeployedFromStation_Code`, `DeployedFromStation_Name`, `DeployedFromLocation`, `PumpOrder`, `PlusCode_Code`, `PlusCode_Description`, `DelayCodeId`, `DelayCode_Description`

The publisher's column descriptions are in the metadata spreadsheets linked from each source page. Two of the columns matter early. `PerformanceReporting` is 1 for the first engine to arrive at an incident, the engine the Brigade uses to measure its response-time target. `Notional Cost (£)` is engine minutes multiplied by a fixed hourly rate, so it measures effort, not money spent.


## The challenges

When you meet one, log the <!-- plain-language: everyday decision -->decision you make.

### 1. Engines whose incident is not in the table

About 1,400 mobilisation rows (under half a per cent) carry an incident number that is not in the incidents extract. An inner join drops those engines and does not tell you. A left join keeps them with empty incident columns. Either join is acceptable, as long as you notice what happened to those rows. Count rows before and after the join, and decide.

### 2. Attendance time is empty when no engine attended

`FirstPumpArriving_AttendanceTime` is missing for about one incident in twenty, mostly calls that were stood down before any engine arrived, or calls handled without an engine. A mean of the column leaves them out without telling you. A chart of response times that does not state the exclusion shows the wrong set of incidents. Decide what your question needs and say what you excluded.

### Smaller things to know

- `DateAndTimeReturned` is missing for many rows and mixes date formats. Check its formats before you convert it to dates, or leave it alone
- `IncGeo_BoroughName` and `BoroughName` (in the mobilisations table) are both in capitals. Elsewhere in the Brigade's files, names appear in `ProperCase` (a capital first letter, the rest lower case). Check that both columns use the same case before you join on a name

## Questions to get you started

Your team chooses its own questions. The [group project brief](./group-project.md) sets how many. The Week 7 sprint starts from the questions below, any of which you can pick. *(Remember to also assess their value, such as in terms of how they are written, framed, etc.)*

1. **Response times.** How long does the first engine take to arrive, by borough and by hour of the day, and where does it exceed the Brigade's target?
2. **False alarms.** What share of incidents are false alarms, what do they cost in engine minutes, and where (which property types, which boroughs) do they cluster?
3. **Station workload.** Which stations attend the most incidents, and how often does an incident need engines from more than one station?
4. **Delays.** What slows engines down, and does it vary by borough or by time of day?
5. **Seasonality.** How do incident volumes and types move through the year, and what does the summer peak consist of?

The fictional client's memo is in the [group project brief](./group-project.md).
