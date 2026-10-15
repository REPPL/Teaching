# The individual-report data: The abcd project record

*This page explains what [the record](../Guides/glossary.md#term-abcd-record) is (the data you'll be analysing) and who the client is (hint: It's me). It shows how you get the data, what each table contains, challenges you may encounter, and the measures each [brief](../Guides/glossary.md#term-brief) uses. Read this before you choose a brief and again during the independent practice week.*


## The client

The project you'll be assessing belongs to me, which makes me your client. What is required is a *critical reading* of this project. Findings critical of what I have built are **expected**. Otherwise, I wouldn't know what to work on!


## Part 1: The record

`abcd` is a small open-source software tool I'm building as part of my research. What's fairly novel is, I think, that it's built in the open. That means it keeps a written record of its own work as files inside the project. Each entry is one file, with a short header of named fields and a body of text. Over the past few months, I spent countless hours on it: I made several thousand changes, filed over thirteen hundred problems, two hundred promises, eighty designs, and sixty [decisions](../Guides/glossary.md#term-decision).

That record, exactly as it stood at one [release](../Guides/glossary.md#term-release), is your dataset.

You do not need to know how the tool works, or any programming specific to it. But as an [analyst](../Guides/glossary.md#term-analyst), you need to familiarise yourself with the language your client uses. Here are the essential terms, because every table is built from them.

- **[Issue](../Guides/glossary.md#term-issue)**: A record of a problem somebody noticed. It has a severity (nitpick, minor, major, critical) and a category (bug, security, documentation, and so on). It also notes how it was found, and sometimes the file it points at. It is open, resolved with a note of what fixed it, or closed with a reason for not fixing it
- **[Intent](../Guides/glossary.md#term-intent)**: A record of a promise, written as the press release the project would publish once the promise is kept. It starts as a draft, becomes planned when I sign it off, and ends shipped (the work is done) or superseded (overtaken by another). Some intents are disciplines, which are standing rules rather than features
- **[Spec](../Guides/glossary.md#term-spec)**: A record of a design, the plan for delivering one intent. It is open while the work is under way and closed when the work is done
- **[Decision](../Guides/glossary.md#term-decision)**: A dated, written ruling on how something is done and why, known as an architecture decision record. A later decision can supersede it
- **Principle**: A standing position the project <!-- plain-language: everyday commit -->commits to, such as "a stage that no-ops must say so"
- **[Commit](../Guides/glossary.md#term-commit)**: One saved change to the project's files, with a timestamp, an author, a one-line message, and the files it touched. The message starts with a conventional word that names the kind of change (`feat`, `fix`, `docs`, `chore`, `test`, `refactor`)
- **Release**: A version tag on one commit, the moment a set of changes is published under a number

Records can refer to each other, for example:

- An intent builds on earlier intents
- A spec implements an intent
- A decision supersedes an older decision
- An issue is blocked by another

The body text of a record also mentions other records by id, thousands of times in total. Together these references form a network, called a graph. Some of the briefs are about it.


## Part 2: Getting the data

We use a Python script to fetch (i.e., get) the record from the public project. For now, we will use all data up to one fixed release. The script also builds the tables you need for your analysis:

```bash
python3 Tools/fetch_abcd.py
```

Run it once, in your Codespace, from the folder that contains `Tools/`. The `Tools/` in `python3 Tools/fetch_abcd.py` above shows that the script is in the `Tools` folder. It downloads a copy of the project (about 50 MB, under a minute). It reads every record file and the change history, and writes the tables into `work/data/abcd/`, in your own `work` folder.

It also writes `manifest.json`, which records the version number of `abcd` (called a `tag`), the commit it points at, and a checksum for every table. The tables are identical on any machine. The [Tools page](../Tools/README.md) explains how to check your tables against the manifest.

Read a table with `pandas`. The example below is for a notebook kept at the top of your `work` folder, next to `data/`. The timestamps are plain text in a specific format, so `pd.to_datetime` is needed to convert a date as text into a date `object` (we'll cover this in class):

```python
import pandas as pd

issues = pd.read_csv("data/abcd/issues.csv.gz")
issues["created_at"] = pd.to_datetime(issues["created_at"])
```

Commit (i.e., add) both the tables and the manifest to **your own repository**. The [individual report brief](./individual-report.md) explains why.

**Licence**: The project is published under the MIT licence, which makes any use, including this one, straightforward. Cite it as *abcd project record, release v0.8.0, github.com/intentdriven/abcd, MIT licence*. The live record is browsable at abcdev.app, with a graph view. It changes with every release. *(Keep in mind that your data comes from the tag, not from the website.)*

The Licence information is added here for completeness so that you make it second nature to acknowledge data sources; it's not really necessary here, but it will be essential for future projects.


## Tables

| Table | One row per | Columns to know first |
|-------|-------------|-----------------------|
| `issues` | problem record (1,327) | `id`, `bucket` (open, resolved, wontfix), `severity`, `category`, `source` (how it was found), `found_during`, `found_at` (a file path), `resolution`, `created_at`, `created_source`, `first_commit`, `last_commit`, `body_words`, `mentions` |
| `intents` | promise record (195) | `id`, `bucket` (drafts, planned, shipped, superseded, disciplines), `impact`, `builds_on`, `spec_id`, `created_at`, `first_commit`, `last_commit` |
| `specs` | design record (81) | `id`, `bucket` (open, closed), `intent`, `created_at` |
| `decisions` | decision record (59) | `id`, `status` (accepted, superseded, proposed), `date` (the record's own date), `supersedes`, `first_commit` |
| `releases` | release (21) | `tag`, `version`, `date` |
| `commits` | saved change (2,993) | `sha`, `timestamp`, `author`, `prefix`, `subject`, `is_merge`, `record_ids` (ids named in the message), `files_changed`, `insertions`, `deletions` |
| `commit_files` | file touched by a commit (11,888) | `sha`, `path`, `insertions`, `deletions` |
| `nodes` | record in the graph (1,662) | `id`, `type`, `lifecycle`, `title` |
| `edges` | typed link between two records (261) | `from`, `to`, `rel` (builds_on, implements, blocked_by, supersedes) |
| `mentions` | one record naming another in its prose (3,006) | `from`, `to` |

The four record tables (`issues`, `intents`, `specs`, and `decisions`) also carry `path`, `title`, and `body_words`. Every timestamp is in one format, in UTC (Coordinated Universal Time), but without a time-zone marker. The commit table keeps my git names as they are (`REPPL` and `Alex Reppel`). One other human contributor's name is replaced with a made-up one. The bots (automated accounts) keep their names.


## The challenges (well, some of them!)

Each one **forces a decision**, and part of your responsibility is to record it.

**1. When issues were resolved.** Of the 919 resolved issues, 764 were created directly in the resolved folder. This is because my automated review process typically files a problem and its fix in one step. For those, `first_commit` equals `last_commit`, so their time-to-resolve is zero. A median time-to-resolve over all resolved issues is therefore near zero and tells you nothing about how long a problem waits after somebody notices it. Decide what population of issues your question is about, and say what you excluded.

**2. Creation dates.** Records show the day a file was imported, although the true date an intent or issue was created is earlier. For example, the project's files were imported into the public repository on 6 July 2026. Although sixty intents and twenty-three decisions carry that day as their `first_commit`, they were written earlier. The decisions' own `date` field runs back to May. *(This is because the project was based on a previous attempt.)*

For issues, `created_at` comes from one of two places. Where the id contains a timestamp, it comes from the id (941 rows, `created_source` = `id`). Otherwise it comes from git (386 rows, `created_source` = `git`). Only the git-dated rows can show the import day instead of the earlier true date. Use `date` for decisions. Prefer `created_source` = `id` where the question is about timing. Never read the import day as a burst of activity.

Watch for these smaller things too:

- Some values in `source` mean almost the same thing, such as `agent-finding` and `agent-observation`. If you group them, say how in your report
- `found_during` is free text, so almost every value is different. Do not group on it as it stands


## The measures the briefs use

- **Time-to-resolve**: For a resolved issue, `last_commit` minus `created_at`, in days. See challenge 1
- **Throughput**: Records created, or resolved, per week (`created_at` or `last_commit`, grouped by ISO week, Monday to Sunday)
- **Backlog**: Open issues at the end of a week. Compute it as created so far minus resolved so far, or as the count of rows whose bucket is open at the tag
- **Churn**: Lines inserted plus deleted, per file or per week, from `commit_files` or `commits`
- **Degree**: The number of links a record has, in either direction, counted from `edges` (typed links) or `edges` plus `mentions` (all references)
- **Lead time**: For an intent, from its first commit to the closing of its spec. For a release, from the previous release's date to its own date

The record covers July to early September 2026 for issues and commits, with many releases (i.e., versions). Most of the issue activity falls in three weeks at the end of August. Each brief explains what that means for its question. Every number on this page is from release v0.8.0 (commit `514ea960`).

The briefs, each with a stakeholder and a starting question, are on the [briefs page](./individual-briefs.md).
