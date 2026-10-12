# The individual-report briefs

*Here are several [briefs](../Guides/glossary.md#term-brief) on the [abcd project record](../Guides/glossary.md#term-abcd-record). You choose one in Week 6. See ["The rules"](#the-rules) at the end of this page.*

Every [brief](../Guides/glossary.md#term-brief) sets a **primary table**, a **slice** (how the table is split), and a **primary measure**. You must use all three. The rest of the analysis is yours. The starting question is where you begin, not what you must conclude. The [individual report brief](./individual-report.md) explains how you sharpen it. Also read the [primer](./abcd-record.md) again.


## Brief 1: Where should review effort go?

- **Stakeholder**: The maintainer, deciding which parts of the code get the next review pass
- **Starting question**: Which parts of the project attract the most problems? Is that because they are large, because they change most, or because they are hard?
- **Primary table**: `issues`, sliced by `found_at` and joined to `commit_files` for churn (lines changed) per folder. `found_at` is the file an [issue](../Guides/glossary.md#term-issue) points at, grouped by the first one or two folders in its path
- **Primary measure**: Issues per folder against lines changed per folder
- **Chart family**: A treemap or a bar of issues per folder, then a scatter of issues against churn with the outliers named
- **Risk**: `found_at` is free text, and 10% of issues have none. The top folder contains half the code, so raw counts overstate its problems. Normalise before you conclude

## Brief 2: Is the backlog under control, and did releases help?

- **Stakeholder**: A <!-- plain-language: everyday release -->release manager, deciding whether the next [release](../Guides/glossary.md#term-release) can go out or the backlog has to come down first
- **Starting question**: How did the number of open problems move week by week? Does the backlog change direction at a release?
- **Primary table**: `issues`, sliced by week of `created_at` and week of `last_commit`, with `releases` as event markers
- **Primary measure**: The backlog per week (created so far minus resolved so far)
- **Chart family**: A stacked area or a pair of lines (created, resolved) with the backlog and release dates marked
- **Risk**: There are only ten weekly points. Most of the activity is one burst at the end of August. The born-resolved challenge ([primer](./abcd-record.md)) inflates both created and resolved in the same week. Decide whether born-resolved issues belong in a backlog at all

## Brief 3: How fast are problems fixed, and does severity matter?

- **Stakeholder**: The maintainer, checking that critical problems are fixed faster than nitpicks
- **Starting question**: What is the time-to-resolve, how spread out is it, and does it differ by severity and by category?
- **Primary table**: `issues`, resolved bucket only, sliced by `severity` and `category`
- **Primary measure**: Time-to-resolve in days. State your <!-- plain-language: everyday decision -->decision on the born-resolved rows
- **Chart family**: Box plots or an empirical distribution per severity, then a small table of medians and 90th percentiles. An empirical distribution shows the share of issues resolved within each number of days
- **Risk**: Most resolved issues are born resolved, so the medians are near zero ([primer](./abcd-record.md)). What matters is the rest. Chart only the issues your sentence is about

## Brief 4: Is the automated bug hunt worth paying for?

- **Stakeholder**: A product owner, deciding whether to keep funding an automated review that files problems on its own
- **Starting question**: What share of problems does each channel find, how severe are they, and how often are they later closed as not worth fixing?
- **Primary table**: `issues`, sliced by `source` (its values grouped by what they mean) and by the run names in `found_during`
- **Primary measure**: Share of issues by source and the wontfix rate per source
- **Chart family**: 100% stacked bars of severity per source, then a bar of wontfix rates
- **Risk**: Define and defend the grouping of `source`. `found_during` needs a pattern to extract the run names. A channel that files many nitpicks is not necessarily worse than one that files a few major problems

## Brief 5: Are promises ('intents') kept?

- **Stakeholder**: A product owner, reading how many promises reach delivery and how long each stage takes
- **Starting question**: Of every promise made, what share is shipped? How long do [intents](../Guides/glossary.md#term-intent) wait in each stage?
- **Primary table**: `intents` joined to `specs` on `spec_id`, sliced by `bucket`
- **Primary measure**: Counts per stage and dwell time (waiting time) from `first_commit` to the [spec](../Guides/glossary.md#term-spec)'s `last_commit`
- **Chart family**: A funnel or a bar per stage, then a dot plot of dwell times
- **Risk**: The `intents` table is small. Many of its rows carry the import day as their first [commit](../Guides/glossary.md#term-commit) ([primer](./abcd-record.md)). The buckets are a snapshot at the tag (the release the data comes from), not a history. Say what a stage count can and cannot mean

## Brief 6: Does connectedness predict resolution?

- **Stakeholder**: A triage lead (the person who sorts new problems by urgency), deciding whether well-linked problems get fixed faster or get overlooked
- **Starting question**: Do issues with more references to and from other records resolve more often, or sooner, than isolated ones?
- **Primary table**: `edges` and `mentions`, reduced to a degree per record, joined to `issues`
- **Primary measure**: Degree (all references, both directions) against bucket and time-to-resolve
- **Chart family**: Grouped bars of resolution share by degree band, then a scatter of degree against time-to-resolve for the noticed issues (those not born resolved)
- **Risk**: 495 issues have no reference at all. Degree partly measures how much prose a record has. The expected story (linked issues resolve faster) may be wrong. A report that shows it is wrong is a good report. Use tabular measures only, not a drawn network

## Brief 7: Which decisions does the most work rest on?

- **Stakeholder**: The maintainer, wanting to know which [decisions](../Guides/glossary.md#term-decision) the project rests on and which have been superseded (replaced by a later decision)
- **Starting question**: Which decisions are referred to most, by which kinds of record, and which are superseded?
- **Primary table**: `decisions`, joined to `mentions` and `edges` for references to each decision id, with `status` and `date`
- **Primary measure**: References per decision, by the type of the referring record
- **Chart family**: A ranked bar of the most-referenced decisions, coloured by referrer type, then a timeline of decisions by `date` with the superseded ones marked
- **Risk**: A `supersedes` link sits on the newer decision only, so the older one does not record that it was replaced. A few decisions are referenced by nothing. Use <!-- plain-language: everyday abcd record -->the record's own `date`, never the git date, which can be the import day ([primer](./abcd-record.md))


## The rules

- **Choosing**: Choose your brief in the Week 6 workshop. Briefs go first come, first served. Each brief takes two students until every brief has two. Two students on one brief take different slices (a different period, category, or folder) and agree their split (in writing). Once every brief has two students, the next student takes a third slice on a taken brief, and so on
- **Declaring**: Write one line in your [QuestLog](../Guides/glossary.md#term-questlog) under Week 6 naming the brief and your slice. That line is your Week 6 declaration. Copy the same line under "Brief and slice" in the [report template](./Template.ipynb). If you are also on a group team, add a [`DECISION:` entry](../Guides/glossary.md#term-decision-entry) to your team's record saying so