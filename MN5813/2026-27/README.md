# Business Analytics Languages and Platforms

Welcome to [Runnymede Analytics](./Guides/glossary.md#term-runnymede-analytics). For ten weeks, this module is your first analytics job. You join as a **[Junior Analyst](./Guides/glossary.md#term-analyst)** and work with an AI **[Associate](./Guides/glossary.md#term-associate)**: Fast, tireless, and sometimes ... confidently wrong! The Associate writes most (if not all) of the code. You carry the judgement, and you sign off their work.

*All materials for this module were built with AI assistance. The declaration covering every page and notebook is in [ACKNOWLEDGEMENTS.md](./ACKNOWLEDGEMENTS.md).*


## Getting started

All you need is a modern browser. Each week's lessons are a collection of notebooks that you can read in multiple ways.

1. **On the module website.** Every notebook appears there with its outputs, and the site works on a phone and with a screen reader. The link is on <!-- gen:values.yml#links.moodle_course|link:the Moodle page -->[the Moodle page](https://moodle.royalholloway.ac.uk/course/view.php?id=32615)<!-- /gen -->
2. **On GitHub.** <!-- gen:values.yml#links.student_repository|link:The teaching repository -->[The teaching repository](https://github.com/REPPL/Teaching)<!-- /gen --> shows each notebook as a page, without its outputs
3. **By running it.** In Week 1 you open each notebook in [Google Colab](https://colab.research.google.com/) from the <!-- plain-language: everyday badge -->badge in the week's README. From the Week 2 workshop you run them in your own [GitHub Codespace](https://github.com/features/codespaces). The [Your workstation guide](./Guides/codespaces-start.md) takes you through it

You also have the option to work locally, that is, on your own machine or on one of the PCs in the Lab. The [Working locally](./Guides/working-locally.md) guide arrives together with Week 3 and you can read it in your own time. Your Codespace already has the module's Python libraries installed. For local work only, install from [requirements.lock](./requirements.lock). It is the fully pinned environment built from the library list in [requirements.txt](./requirements.txt).


## How this module works

This module is completely [AI-open](./Guides/ai-guide.md), which means that:

- **AI is expected.** You may use AI tools for all parts of this module, including assessments. There is no penalty for using it, but there's an obvious penalty for using it *wrong*: You won't learn much. What you need to do is to show *how* you used it. Start by reading the [AI guide](./Guides/ai-guide.md) first
- **Zero-install start.** Week 1 runs entirely in [Google Colab](https://colab.research.google.com/) where notebooks open in a browser with Python already running. From the second week onwards, you will work in [GitHub Codespaces](https://github.com/features/codespaces). See the [Your workstation guide](./Guides/codespaces-start.md)
- **Quests, not exercises.** Most teaching weeks end with an **Analyst Quest**: A client scenario with [Bronze](./Guides/glossary.md#term-bronze), [Silver](./Guides/glossary.md#term-silver), and [Gold](./Guides/glossary.md#term-gold) tiers, completed with your *Associate*. Every [quest](./Guides/glossary.md#term-quest) leaves a record: Your notebook, your AI transcripts, and your [QuestLog](./Guides/glossary.md#term-questlog). The [glossary](./Guides/glossary.md#term-quest) explains the stages and tiers
- **Data visualisation design is the human craft.** This is where you will experience the limits of your AI Associate: You decide *which* chart to make, and whether they do it right and in a way that's clear and accessible. Block 3 is built around design *judgement*, using the TRACE checklist and structured critique
- **Group work runs through [Stoa](https://withstoa.com/).** You have the option to meet with your team in a live [Stoa](./Guides/glossary.md#term-stoa) room with a built-in AI agent. The room transcript is your evidence of process: Regular meetings, logged decisions, and contributions from everyone. See the [Stoa workflow](./Guides/stoa-workflow.md)
- **Assessments run on real data that no tutorial covers.** The group project analyses the *London Fire Brigade*'s incident and mobilisation records for a fictional operations director. The individual report analyses the [abcd project record](./Guides/glossary.md#term-abcd-record), the documented history of a small open-source tool. See the group project brief and the individual report brief


## Session outline

| Week | Format | Topic | Content | README | Status |
|------|--------|-------|---------|--------|--------|
| Week 01 | In person | Onboarding at Runnymede Analytics | Module orientation and the AI-open charter, then accounts and a Colab taster | [Week 01](./Week/01/README.md) | <!-- gen:publish.yml#status.week01 -->Released<!-- /gen --> |
| Week 02 | In person | Python fundamentals | Variables, strings, control flow, functions, lists, dictionaries: How to ask and judge an AI Associate. The Codespace build in the workshop | [Week 02](./Week/02/README.md) | <!-- gen:publish.yml#status.week02 -->Released<!-- /gen --> |
| Week 02b | Optional, self-paced | Advanced Python | An overview of advanced Python concepts, such as comprehensions, lambdas, error handling, light object-oriented programming. This will help you judge AI-generated code | [Week 02b](./Week/02b/README.md) (optional, for your own time) | <!-- gen:publish.yml#status.week02b -->Released<!-- /gen --> |
| Week 03 | In person | Assessment briefing | Both assessments explained, the assessment interpretation document, plus support clinic for any remaining workstation problems | Week 03 | <!-- gen:publish.yml#status.week03 -->Not yet<!-- /gen --> |
| Week 04 | In person | Introduction to pandas | DataFrames, Series, file I/O, filtering, merging, aggregation; introduction to the (optional) Stoa team rooms | Week 04 | <!-- gen:publish.yml#status.week04 -->Not yet<!-- /gen --> |
| Week 05 | In person | Advanced pandas | Reshaping (melt, pivot, stack/unstack), window functions, complex aggregations | Week 05 | <!-- gen:publish.yml#status.week05 -->Not yet<!-- /gen --> |
| Week 06 | In person | Data Visualisations I | Visual encoding and chart choice: Perception, chart choice, and the [TRACE](./Guides/glossary.md#term-trace) checklist (using matplotlib and seaborn) | Week 06 | <!-- gen:publish.yml#status.week06 -->Not yet<!-- /gen --> |
| Week 07 | No classes | Independent practice week | Fire-brigade [Sprint Zero](./Guides/glossary.md#term-sprint-zero), self-paced, in your team's Stoa room as an easy way of recording AI transcripts | Week 07 | <!-- gen:publish.yml#status.week07 -->Not yet<!-- /gen --> |
| Week 08 | In person | Data Visualisations II | Storytelling, decluttering, and accessibility, incl. annotation, colour, axes, etc. | Week 08 | <!-- gen:publish.yml#status.week08 -->Not yet<!-- /gen --> |
| Week 09 | In person | Data Visualisations III | Design and critical reflection: The [Gallery](./Guides/glossary.md#term-gallery) and structured peer critique of group-project figures using the Four-D protocol | Week 09 | <!-- gen:publish.yml#status.week09 -->Not yet<!-- /gen --> |
| Week 10 | In person | Group presentations | A 10-minute presentation per group, then 5 minutes of questions (formative). **Attendance is compulsory** | Week 10 | <!-- gen:publish.yml#status.week10 -->Not yet<!-- /gen --> |
| January | Hybrid: <!-- gen:values.yml#weeks.revision.when -->Tuesday 19 January 2027, 14:00 to 17:00 (UK time)<!-- /gen --> | Revision session and individual report Q&A | Design-rationale surgery, [brief](./Guides/glossary.md#term-brief) clinic, [AI Use Record](./Guides/glossary.md#term-ai-use-record) walkthrough | Revision session | <!-- gen:publish.yml#status.revision -->Not yet<!-- /gen --> |


## Teaching blocks

<!-- gen:values.yml#blocks -->
The term has three teaching blocks:

1. **Block 1** (Weeks 1–3) is Python foundations with an AI pair. **Week 1** is taught in Google Colab, with nothing to install. It covers your accounts, the AI-open charter, a Python warm-up, and Quest 01. In **Week 2** you work Quest 02 in GitHub Codespaces. Week 2 confirms the ⭐ **[Workstation Ready](./Guides/glossary.md#term-workstation-ready)** milestone: Codespaces, GitHub Copilot, and your automatic record, built with the class in that week's workshop. The optional **Week 2b** is self-paced, for your own time, and ends with Quest 02b. Week 3 briefs you on both assessments. The group project is formative and uses the fire-brigade data. The individual report is your module mark and uses the abcd project record, on a brief you choose in Week 6

2. **Block 2** (Weeks 4 and 5) is pandas, the core tool for analysing data in DataFrames. You work Quests 04–05, recorded with [SpecStory](./Guides/glossary.md#term-specstory). Stoa team rooms open in Week 4 for weekly stand-ups, logged decisions, and a recorded process

3. **Block 3** (Weeks 6, 8, and 9) is dedicated to data visualisation design or the human craft of design judgement. You apply TRACE to every figure and write the rationale. **Week 7** falls inside Block 3. It is the independent practice week, with no classes. Your team runs its fire-brigade [Sprint Zero](./Guides/glossary.md#term-sprint-zero) in its Stoa room, self-paced, which moves the group project forward. **Week 10** is the group presentation: Each team presents for 10 minutes, then takes 5 minutes of questions (formative)

An additional (optional) **January revision session** (hybrid) supports your individual report: Design-rationale surgery, the brief clinic, and comments on your AI Use Record.
<!-- /gen -->


## Learning materials

Each teaching week's folder contains:

- **Introduction.ipynb**: The week's key concepts and how the week fits the bigger picture. Start here
- **Demonstration.ipynb**: Worked examples with detailed explanations. Each example shows your Associate's first draft next to the human-directed revision
- **Exercises.ipynb**: Practice for the workshop (not all weeks have an exercise book). Week 2's Exercises are your first practice in your Codespace
- **Quest.ipynb**: The week's *Analyst Quest*, about 90 minutes of work. It is a client scenario with five stages (Briefing, [First look](./Guides/glossary.md#term-first-look), Build, [Red Flags](./Guides/glossary.md#term-red-flags), and [Debrief](./Guides/glossary.md#term-debrief)). Complete it with your Associate and keep <!-- plain-language: everyday abcd record -->the record
- **Debrief.ipynb**: Worked answers, alternative approaches, and the *[AI failure gallery](./Guides/glossary.md#term-ai-failure-gallery)*: The mistakes AI tools plausibly make on this week's material, and how to catch them
- **assets/**: A folder with supporting files, which some notebooks create when you run them


### Recommended way forward

1. Read the week's `README.md`, then work through `Introduction.ipynb`
2. Work through `Demonstration.ipynb`: Run everything, and ask your Associate to explain anything unclear three different ways
3. In a week that has `Exercises.ipynb`, work through it in the workshop
4. Complete `Quest.ipynb`. Aim for at least Bronze. Silver is the expected standard by the end of term
5. Update your `QuestLog.md` and make sure your session transcript is saved
6. Only then read `Debrief.ipynb`, including the AI failure gallery. From Week 4, each week's Debrief arrives with the following week


## Guides

| Guide | For | What it covers |
|-------|-----|----------------|
| [AI guide: Working with your Associate](./Guides/ai-guide.md) | Students | The AI-open charter, the four canonical moves, prompting for analytics, evidence and attribution |
| [Your workstation](./Guides/codespaces-start.md) | Students | Your Week 2 workstation and the module's default environment: GitHub Codespaces, GitHub Copilot, and your automatic record |
| [Working locally (optional)](./Guides/working-locally.md) | Students | The same toolchain on your own machine, if you prefer it to your Codespace |
| [Stoa workflow](./Guides/stoa-workflow.md) | Students | Group work: Rooms, stand-ups, [decision logging](./Guides/glossary.md#term-decision-entry), what is recorded |
| The Runnymede Standard: Data visualisation design guide | Students | Chart choice, decluttering, colour, honesty, accessibility, TRACE, design rationales |
| [Glossary](./Guides/glossary.md) | Students | What every module term means, and which notebook and section teaches each technique |
| [Prompt library](./Guides/prompts.md) | Students | Every prompt the materials ask you to try, on one page, with what a good answer contains |
| [Briefing for the Associate](./AGENTS.md) | Students' AI tools | What your AI tool reads at the start of every session: The module's words, layout, and the rules it follows when helping you |


## Assessment

There are two assessments. The group project is formative: Your team gets feedback and nothing from it counts towards your mark. The individual analytics report is your module mark.

- **Group project (formative)**: A team analysis of the *London Fire Brigade* incident and mobilisation records for a fictional operations director. See the group project brief and the data note for details
- **Individual report (the module mark)**: Your own analysis of the `abcd` [project record](https://abcdev.app/record/) on a brief you choose in Week 6. The client is the module leader and findings critical of it are expected. See the individual report brief, the primer, and the seven stakeholder briefs for details
- **Assessment interpretation**: The AI-open statement and what markers read as evidence for each rubric criterion. It also covers the process indicators computed from transcripts, and what we collect and why. It arrives with Week 3. Read it before the Week 3 briefing
