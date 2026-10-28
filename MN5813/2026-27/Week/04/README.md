<!-- gen:values.yml#weeks.04.heading -->
# Week 04: Introduction to pandas
<!-- /gen -->

*`DataFrames` are the tables an <!-- plain-language: everyday Analyst -->analyst works with every day. Your group project also starts this week.*


## Overview

Block 2 begins. This week you're introduced to [pandas](https://pandas.pydata.org/), the Python library for working with tables of data. In [Quest 04](../../Guides/glossary.md#term-quest), *The Messy Merger*, you use it on two retailers' sales ledgers that disagree.

Your [group project](../../Assessment/group-project.md) starts with today's workshop. Your team also holds its first [stand-up](../../Guides/glossary.md#term-stand-up). Your team meets on Microsoft Teams, or in an optional [Stoa](../../Guides/glossary.md#term-stoa) room (probably more convenient, see [Stoa workflow guide](../../Guides/stoa-workflow.md)).

You work in your [GitHub Codespace](../../Guides/codespaces-start.md).


## This week's learning objectives

By the end of Week 4 you can:

1. Create and inspect pandas `Series` and `DataFrames`, and check each column's data type (its `dtype`) before trusting any number
2. Read and write CSV, Excel, and JSON files. Explain what can go wrong when you read a file, even when Python reports no error
3. Select, filter, and sort `DataFrame` rows using boolean conditions, `loc`, and `iloc`
4. Combine data with `pd.concat` and `pd.merge`, choose the right `how=`, and check the row counts afterwards
5. Summarise data with `groupby` aggregation. Defend a data-cleaning <!-- plain-language: everyday decision -->decision with evidence in rows and pounds
6. Run a recorded analysis session from start to finish. Point to its [Prompt Diary](../../Guides/glossary.md#term-prompt-diary) entry as your record


## Before class

- [ ] Read the [Introduction](./Introduction.ipynb)
- [ ] Read the [Stoa workflow guide](../../Guides/stoa-workflow.md) (about 10 min)
- [ ] Read the [London Fire Brigade data note](../../Assessment/lfb-data.md)
- [ ] Work through the [Demonstration](./Demonstration.ipynb) (about 75 to 90 min)


## In class

<!-- gen:values.yml#session.line -->
- Session: 45-minute lecture + 105-minute workshop
<!-- /gen -->

### Lecture

**<!-- gen:values.yml#session.lecture-label -->Lecture (45 min within the 60-minute slot)<!-- /gen -->:** I introduce pandas: `DataFrames`, the week's key operations, and how *Quest 04* uses them.

### Workshop

**<!-- gen:values.yml#session.workshop-label -->Workshop (105 min within the 120-minute slot)<!-- /gen -->**

- **Your team's first stand-up** (15 min): Log your team's first [`DECISION:` entry](../../Guides/glossary.md#term-decision-entry). The [Stoa workflow guide](../../Guides/stoa-workflow.md) gives the agenda, and how to set up your room
- **Download the [London Fire Brigade data](../../Assessment/lfb-data.md)** (10 min): Every team member fetches it. Then your team agrees on one copy
- Work on *Quest 04* with your [Associate](../../Guides/glossary.md#term-associate) (80 min), and add its exchanges to your Prompt Diary


## At home (about 1 to 1.5 hours, before Week 5)

- [ ] With your team, finish the team setup on the same day. The [Stoa workflow guide](../../Guides/stoa-workflow.md) lists every step. Hold or schedule your team's next stand-up
- [ ] Finish [Quest 04](./Quest.ipynb) at least to [Bronze](../../Guides/glossary.md#term-bronze) (about 30 min). [Silver](../../Guides/glossary.md#term-silver) is the expected standard by the end of term
- [ ] Update your `QuestLog.md`. **Add today's exchanges to your Prompt Diary**

If you cannot tick a box for whatever reason, bring it to the Week 5 workshop for us to discuss.


## Contents

| File | What it is |
|------|------------|
| [Introduction.ipynb](./Introduction.ipynb) | A preview of the week's concepts, and the start of group work |
| [Demonstration.ipynb](./Demonstration.ipynb) | The pandas walk-through, with [AI Lens](../../Guides/glossary.md#term-ai-lens) callouts |
| [Quest.ipynb](./Quest.ipynb) | **Quest 04: The Messy Merger** (about 90 min). Reconcile two sales ledgers that disagree, for Hartley & Voss |
| [Debrief.ipynb](./Debrief.ipynb) | Worked answers, the cleaning strategies compared with the numbers, and the [AI failure gallery](../../Guides/glossary.md#term-ai-failure-gallery) (released with Week 5) |

**Start here:** Read the [Introduction](./Introduction.ipynb). Then work through the [Demonstration](./Demonstration.ipynb) in your Codespace.


## Essential guides

- [Stoa workflow](../../Guides/stoa-workflow.md): Your team's room, stand-ups, `DECISION:` entries, and your team's record
- [Group project brief](../../Assessment/group-project.md): The task, and what your team submits
- [London Fire Brigade data](../../Assessment/lfb-data.md): The group-project data, and how you fetch it
