<!-- gen:values.yml#weeks.06.heading -->
# Week 06: DataViz I: Visual encoding and chart choice
<!-- /gen -->

*Block 3 opens. Your [Associate](../../Guides/glossary.md#term-associate) draws the charts ... usually quite quickly. But it's **you** who has to decide which chart to use, and whether it is ready for a client.*


## Overview

This week we start on data visualisation *design*. A chart shows numbers as, e.g., a position, a length, an angle, an area, a colour, etc. (these are sometimes called 'visual encodings' or 'visual variables'). However, the challenge is that people read some of these variables more accurately than others. That ranking should guide your choice of chart. For that, you must understand your reader's task (e.g., a comparison or a trend), and then pick an appropriate chart family. **[TRACE](../../Guides/glossary.md#term-trace)** is the checklist every figure at [Runnymede Analytics](../../Guides/glossary.md#term-runnymede-analytics) must pass.

In **[Quest 06](../../Guides/glossary.md#term-quest): The Chart Doctor**, you diagnose the faults in a colleague's investor deck. Then you direct your Associate to rebuild the charts.

You also choose your individual-report [brief](../../Guides/glossary.md#term-brief) this week.


## This week's learning objectives

By the end of Week 6 you can:

1. Rank the visual encodings from the most accurately read to the least, and explain how that ranking guides your chart choice
2. Match a business question to its analytical task, and choose a chart family you can defend
3. Build and revise the core chart types (bar, line, scatter, histogram, and box plot) in `matplotlib` and `seaborn` by directing your Associate
4. Run the TRACE checklist over any figure, and give a one-line verdict that names the failing letter and the fix
5. Diagnose the classic misleading charts, such as truncated bars, dual axes, crowded pies *(yes, we do not like them!)*, rainbow palettes, 3D effects *(we REALLY do not like them!)*, and line charts with too many lines


## Before class

- [ ] Read the [Week 5 Debrief](../05/Debrief.ipynb) first, including the [AI failure gallery](../../Guides/glossary.md#term-ai-failure-gallery)
- [ ] Read the [Introduction](./Introduction.ipynb)
- [ ] Read the [DataViz design guide](../../Guides/dataviz-design-guide.md), sections 1–2, 5, and 7. Also read the watch list of typical AI chart failures in section 9 (about 45 to 60 min for the guide) <!-- values-guard: allow: a self-study estimate, not the lecture length -->


## In class

<!-- gen:values.yml#session.line -->
- Session: 45-minute lecture + 105-minute workshop
<!-- /gen -->

### Lecture

I demonstrate how people read charts and how we encode them (20 min). Then I cover how to choose a chart from the reader's task, and the TRACE checklist (25 min).

### Workshop

- Work through the [Demonstration](./Demonstration.ipynb) in teams (30 min): Run each pair of charts. Try its revision prompt with your Associate
- Work on **Quest 06: The Chart Doctor** with your Associate (60 min). Aim to leave with [Bronze](../../Guides/glossary.md#term-bronze) verified and [Silver](../../Guides/glossary.md#term-silver) attempted
- Choose and declare your brief (10 min), under the rules on the [briefs page](../../Assessment/individual-briefs.md)
- Wrap-up (5 min): I go through the verdict format, the [badges](../../Guides/glossary.md#term-badge), and your [QuestLog](../../Guides/glossary.md#term-questlog) entry


## At home (about 1–2 hours, before Week 7)

- [ ] Finish [Quest 06](./Quest.ipynb) to at least Bronze (about 30 min). Silver is the expected standard by the end of term
- [ ] Hold this week's team [stand-up](../../Guides/glossary.md#term-stand-up) on Microsoft Teams or in your [Stoa](../../Guides/glossary.md#term-stoa) (optional) room ([Stoa workflow guide](../../Guides/stoa-workflow.md))
- [ ] Write your QuestLog entry in `QuestLog.md`. Add the quest session's exchanges to your [Prompt Diary](../../Guides/glossary.md#term-prompt-diary)
- [ ] Week 7 has no classes. Your team runs its [Sprint Zero](../../Guides/glossary.md#term-sprint-zero) at its own pace. The Week 7 README lists what to do before it


## Contents

| File | What it is |
|------|------------|
| [Introduction.ipynb](./Introduction.ipynb) | The week's key concepts: The encoding ladder with a live demonstration, the analytical tasks, and TRACE |
| [Demonstration.ipynb](./Demonstration.ipynb) | Pairs of charts in matplotlib and seaborn: The Associate's first draft, then your revision with the prompt that fixed it. [AI Lens](../../Guides/glossary.md#term-ai-lens) callouts give prompts to try |
| [Quest.ipynb](./Quest.ipynb) | **Quest 06: The Chart Doctor** (about 90 min). Diagnose the faulty charts in a colleague's investor deck, then rebuild them by directing your Associate |
| Debrief.ipynb | Worked diagnoses, every rebuild, a model memo, and the [AI failure gallery](../../Guides/glossary.md#term-ai-failure-gallery) of your Associate's chart defaults (released with Week 7) |

**Start here:** Read the [Introduction](./Introduction.ipynb) before the lecture.


## Essential guides

- [DataViz design guide](../../Guides/dataviz-design-guide.md): The reference for every figure in both assessments
- [Briefs page](../../Assessment/individual-briefs.md): The individual-report briefs, and the rules for choosing and declaring one
- [Stoa workflow](../../Guides/stoa-workflow.md): Your team's room, stand-ups, and [`DECISION:` entries](../../Guides/glossary.md#term-decision-entry)
