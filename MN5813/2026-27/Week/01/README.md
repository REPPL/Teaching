<!-- gen:values.yml#weeks.01.heading -->
# Week 01: Onboarding at Runnymede Analytics
<!-- /gen -->

*Your first taught week: Accounts in the workshop, your first notebook in Colab, and the rest at home before Week 2.*


## Overview

Welcome to [Runnymede Analytics](../../Guides/glossary.md#term-runnymede-analytics). Week 1 is a taught week, with a lecture and a workshop. In the workshop you set up your accounts with staff, then open your first notebook in **Google Colab**. Colab runs a notebook in your browser from a link, with Python already working. There is nothing to install. At home (before Week 2) you finish the notebooks and run your first [quest](../../Guides/glossary.md#term-quest) with an AI [Associate](../../Guides/glossary.md#term-associate).

Your workstation for the rest of the module is a GitHub Codespace, with GitHub Copilot and an automatic record of your AI sessions. You build it with the class in the **Week 2 workshop**.


## This week's learning objectives

By the end of Week 1 you can:

1. Explain the module's AI-open charter and what the module assesses: Your judgement and your record
2. Open a notebook in Google Colab, run its cells in order, and edit and re-run one
3. Write and run basic Python: Variables, f-strings, comparisons, `if`/`else`, lists, `for` loops, and a first function
4. Read a Python error message from top to bottom and ask your Associate a well-formed question about it
5. Complete an [Analyst Quest](../../Guides/glossary.md#term-quest) from start to finish (predictions, tiers, [Red Flags](../../Guides/glossary.md#term-red-flags), [Debrief](../../Guides/glossary.md#term-debrief)) and record it in your [QuestLog](../../Guides/glossary.md#term-questlog) and [AI Use Record](../../Guides/glossary.md#term-ai-use-record)


## Before class

- [ ] Read the [Introduction](./Introduction.ipynb): What this week covers, and how to run a notebook's cells


## In class

<!-- gen:values.yml#session.line -->
- Session: 45-minute lecture + 105-minute workshop
<!-- /gen -->

<!-- gen:values.yml#session.what-to-bring -->
**What to bring:** A laptop, your phone, your student ID card, and your university email login. You create a new Google account for this module in the workshop. Google may send a code to your phone to check it. GitHub may also ask you to confirm a sign-in on your phone. The Student Developer Pack application may ask for a photo of your student ID card. You need the laptop in the workshop, not the lecture.
<!-- /gen -->

### Lecture

**<!-- gen:values.yml#session.lecture-label -->Lecture (45 min within the 60-minute slot)<!-- /gen -->:** All of it comes from Part 1 of the [Demonstration](./Demonstration.ipynb). You install nothing and run nothing in this slot.

- How the module works (15 min): The three blocks, the weekly rhythm, and quests and [badges](../../Guides/glossary.md#term-badge)
- The AI-open charter and your Associate (15 min): What AI-open means, and who does the checking
- The assessments in overview (15 min): The group project and the individual report. The full <!-- plain-language: everyday brief -->brief comes in Week 3

### Workshop

**<!-- gen:values.yml#session.workshop-label -->Workshop (105 min within the 120-minute slot)<!-- /gen -->**

- Accounts (45 min): Staff help you with each step <!-- values-guard: allow: a workshop segment, not the lecture length -->
  - Create or check your GitHub account with your university email (15 min)
  - Create your module Google account and sign in to Colab with it (10 min)
  - Submit the Student Developer Pack application (20 min)
- The Colab taster (45 min): Open the Demonstration from its badge, run the first cells, and ask Colab's Gemini one question <!-- values-guard: allow: a workshop segment, not the lecture length -->
- Wrap (15 min): The "At home" list, and how the [Prompt Diary](../../Guides/glossary.md#term-prompt-diary) works

Your module Google account is new, and you use it only for this module. Part 1 of the [Demonstration](./Demonstration.ipynb) gives the address to choose. You sign in to Colab with it now, and to [Stoa](../../Guides/glossary.md#term-stoa) from Week 4.

GitHub's student verification takes days. When GitHub approves you, turn on the free Copilot Student plan. Until then, Copilot Free needs no verification, so nothing in the module waits on the Pack.


## At home (about 2.5 hours, before Week 2)

- [ ] If not done, finish Part 1 of the [Demonstration](./Demonstration.ipynb) **at home**, your first day at the firm (about 15 minutes)
- [ ] **Also at home**, work through Part 2 of the Demonstration, the Python warm-up (about 45 minutes). Run every cell and do every ✏️ Try it <!-- values-guard: allow: a self-study estimate, not the lecture length -->
- [ ] Read the [AI Guide](../../Guides/ai-guide.md). Then complete [Quest 01](./Quest.ipynb) with your [Associate](../../Guides/glossary.md#term-associate) (about 75 minutes for both). Fill in its Prompt Diary cell: Your best and worst exchange, pasted
- [ ] Copy [QuestLog-Template.md](./QuestLog-Template.md) to `QuestLog.md`. This is your [QuestLog](../../Guides/glossary.md#term-questlog). Write your first entry in it, for Quest 01 (about 15 minutes)
- [ ] Check that your GitHub account signs in
- [ ] Check that your module Google account signs in to Colab
- [ ] Submit your GitHub Student Developer Pack application. [Codespaces Start](../../Guides/codespaces-start.md), Step 1, has the detailed steps


## Contents

| File | What it is |
|------|------------|
| [Introduction.ipynb](./Introduction.ipynb) | Start here: What this week covers, the lecture, the workshop, and what to finish at home |
| [Demonstration.ipynb](./Demonstration.ipynb) | Part 1, the onboarding memo: How the module works, the AI-open charter, your Associate, and your accounts. Part 2, the Python warm-up: Numbers, text, variables, <!-- plain-language: everyday decision -->decisions, loops, and your first error message |
| [Quest.ipynb](./Quest.ipynb) | **Quest 01: [Tutorial Island](../../Guides/glossary.md#term-tutorial-island)** (about 45 to 60 minutes): Your first job for the Partner, in the full quest format |
| Debrief.ipynb | Worked answers for Quest 01, the [Red Flags](../../Guides/glossary.md#term-red-flags) fix, and the [AI failure gallery](../../Guides/glossary.md#term-ai-failure-gallery), released with Week 2 |
| [QuestLog-Template.md](./QuestLog-Template.md) | Your personal learning journal, kept all term |

**Start here:** Read the [Introduction](./Introduction.ipynb), then open `Demonstration.ipynb` in Colab from this <!-- plain-language: everyday badge -->badge.

<!-- gen:values.yml#colab-badge|Demonstration.ipynb -->
[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/REPPL/Teaching/blob/main/MN5813/2026-27/Week/01/Demonstration.ipynb)
<!-- /gen -->

<!-- generated from videos.json: week01-colab-setup; edit videos.json, not this region -->
<!-- end generated from videos.json -->


## Essential guides

- [AI Guide: Working with Your Associate](../../Guides/ai-guide.md): Read it at home, before Quest 01
- [Codespaces Start](../../Guides/codespaces-start.md): Step 1 happens in this week's workshop. You build the rest in the Week 2 workshop
