<!-- gen:values.yml#weeks.05.heading -->
# Week 05: Advanced pandas
<!-- /gen -->

*This session is all about reshaping data, that is, turning the table you have into the table the question needs. Advanced pandas will also cover window functions and (more) complex aggregation.*

Key concepts include tidy vs. messy data (see, e.g., [Tidy vs. Messy Part I](https://github.com/tri-cods/tidy-data/blob/master/sections/tidy-vs-messy.md) and [Tidy vs. Messy Part II](https://github.com/tri-cods/tidy-data/blob/master/sections/tidy-vs-messy-ii.md)) and long vs. wide formats (see, e.g., [Long vs. Wide Data](https://www.statology.org/long-vs-wide-data/)).


## Overview

The [quest](../../Guides/glossary.md#term-quest) client is **Marlow & Finch**, a retail chain. Its director wants one table for Friday's board meeting, to answer one question: Are weekend promotions working? To answer it, you change the **shape** of the data. You give your [Associate](../../Guides/glossary.md#term-associate) a one-sentence *shape description*, such as "rows = regions, columns = promo vs no-promo, cells = average daily sales".


## This week's learning objectives

By the end of Week 5 you can:

1. State the rules of tidy data and diagnose which one a messy table breaks
2. Reshape long data into a board-ready grid with `pivot_table()`, stating the aggregation explicitly. Recognise the jobs that call for `melt()` or `stack()`/`unstack()` instead
3. Read and slice a `MultiIndex` produced by grouping on several keys
4. Read trends built with window functions (`rolling()`, `shift()`, `pct_change()`) and explain why they need sorted, per-group data
5. Summarise several statistics at once with named aggregation, and recognise when `agg()` dictionaries or `transform()` fit better
6. Specify a reshape to your Associate as a shape description, state the aggregation explicitly, and verify one cell of the result by hand

You use `pivot_table()` and named aggregation in the quest. You practise `melt()`, `stack()`/`unstack()`, window functions, and `transform()` in the Demonstration. You use them again on the [London Fire Brigade data](../../Assessment/lfb-data.md) in Week 7.


## Before class

- [ ] Read the [Week 4 Debrief](../04/Debrief.ipynb) first, especially the [AI failure gallery](../../Guides/glossary.md#term-ai-failure-gallery). This week builds on its merging and grouping
- [ ] Read the [Introduction](./Introduction.ipynb): The week's key concepts, from tidy data to complex `groupby()`
- [ ] Then work through the [Demonstration](./Demonstration.ipynb) (about 75 min for this and the Introduction)
- [ ] Open your Codespace. Check that [SpecStory](../../Guides/glossary.md#term-specstory) saves your Copilot chats in `.specstory/history/`


## In class

<!-- gen:values.yml#session.line -->
- Session: 45-minute lecture + 105-minute workshop
<!-- /gen -->

### Lecture

**<!-- gen:values.yml#session.lecture-label -->Lecture (45 min within the 60-minute slot)<!-- /gen -->:** I cover tidy data, `melt()`, and `pivot_table()` with its default `aggfunc` (25 min). Then I cover `MultiIndex`, window functions, and complex `groupby()` (20 min).

### Workshop

**<!-- gen:values.yml#session.workshop-label -->Workshop (105 min within the 120-minute slot)<!-- /gen -->**

- Work on **Quest 05: The Pivot Pitch** with your Associate (95 min). Aim to leave with [Bronze](../../Guides/glossary.md#term-bronze) verified and [Silver](../../Guides/glossary.md#term-silver) attempted
- Wrap-up (10 min): I go through the till-feed bug in [Red Flags](../../Guides/glossary.md#term-red-flags), the [badges](../../Guides/glossary.md#term-badge), and how Week 7 uses this material


## At home (about 2 hours, before Week 6)

- [ ] Finish [Quest 05](./Quest.ipynb) to at least Bronze (about 30 min). Silver is the expected standard by the end of term
- [ ] Hold this week's team [stand-up](../../Guides/glossary.md#term-stand-up) on Microsoft Teams or in your [Stoa](../../Guides/glossary.md#term-stoa) room ([Stoa workflow guide](../../Guides/stoa-workflow.md))
- [ ] Write your [QuestLog](../../Guides/glossary.md#term-questlog) entry in `QuestLog.md`. Check that the SpecStory transcript of your quest session is in `.specstory/history/`. It is your record of the quest, and your [AI Use Record](../../Guides/glossary.md#term-ai-use-record) draws on it later
- [ ] If VS Code, GitHub Copilot, or SpecStory does not work in your Codespace, use the [Your workstation guide](../../Guides/codespaces-start.md) to fix it
- [ ] Week 6 opens data visualisation design. Before its workshop, read the DataViz design guide, sections 1–2, 5, and 7. Also read the watch list of typical AI chart failures in section 9
- [ ] Read the [record primer](../../Assessment/abcd-record.md) and the [briefs page](../../Assessment/individual-briefs.md). You choose and declare your [brief](../../Guides/glossary.md#term-brief) in Week 6, under the rules in the [individual report brief](../../Assessment/individual-report.md)


## Contents

| File | What it is |
|------|------------|
| [Introduction.ipynb](./Introduction.ipynb) | The week's key concepts: Tidy data, the reshaping verbs, `MultiIndex`, window functions, and complex `groupby()` |
| [Demonstration.ipynb](./Demonstration.ipynb) | Worked examples on Hartwell Garden Centres' data, including `pivot_table`'s silent default, with [AI Lens](../../Guides/glossary.md#term-ai-lens) prompts |
| [Quest.ipynb](./Quest.ipynb) | **Quest 05: The Pivot Pitch** (about 90 min). Build the one table that answers the Marlow & Finch director's question for the board |
| Debrief.ipynb | Worked answers, and the [AI failure gallery](../../Guides/glossary.md#term-ai-failure-gallery) of NaN-as-zero, chained assignment, and vanishing groups (released with Week 6) |

**Start here:** Work through the [Introduction](./Introduction.ipynb), then the [Demonstration](./Demonstration.ipynb), before the lecture.


## Essential guides

- DataViz design guide: The reading for the Week 6 workshop
- [Your workstation](../../Guides/codespaces-start.md): Your Codespace and how to troubleshoot VS Code, Copilot, and SpecStory
