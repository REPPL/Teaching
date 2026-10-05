<!-- gen:values.yml#weeks.02b.heading -->
# Week 02b: Advanced Python
<!-- /gen -->

*Optional and self-paced, with no taught session: Comprehensions, lambdas, error handling, and a first class, learnt as reading skills. Released with Week 2, it ends with [Quest](../../Guides/glossary.md#term-quest) 02b: The Subscription Churn Memo.*


## Overview

This material is for your own time, at your own pace. It teaches three named strategies for reading code you didn't write, alongside the Python patterns AI-generated code uses most. It ends with **Quest 02b: The Subscription Churn Memo**. Your client is StreamShore, a streaming startup whose board wants churn numbers it can trust.

Nothing later in the module depends on it. Later weeks explain each construct where they use it.


## This week's learning objectives

By the end of Week 2b you can:

1. Read an unfamiliar piece of Python using three named strategies: Trace the data flow, name the <!-- plain-language: everyday intent -->intent of each block, and run fragments
2. Read and write list and dictionary comprehensions, and judge when a comprehension is too clever to ship
3. Rank structured data with `sorted(key=...)`, using a `lambda` or a named function, and explain your choice
4. Handle predictable failures with `try`/`except` on *specific* exceptions, and explain why `except: pass` silently corrupts an analysis
5. Read a simple class: Find its data in `__init__`, treat its methods as verbs, and explain `self`
6. Judge an AI-generated analysis whose definition (not its arithmetic) is the problem, and defend a choice between two fixes in business terms


## In class

Week 2b has no class, because it is optional and self-paced.


## At home (about 4 hours, in your own time)

- [ ] Start with the [Introduction](./Introduction.ipynb): The three code-reading strategies and a preview of the week's vocabulary (about 20 min)
- [ ] Work through the [Demonstration](./Demonstration.ipynb) (60 to 75 min)
- [ ] Do [Quest 02b](./Quest.ipynb) (about 90 min)
- [ ] Finish the [quest](../../Guides/glossary.md#term-quest) tiers, then read the Debrief (60 to 75 min for both)
- [ ] Add a dated Quest 02b entry to your `QuestLog.md`. Then tick its line in your `Optional-Checklist.md`


## Contents

| File | What it is |
|------|------------|
| [Introduction.ipynb](./Introduction.ipynb) | Start here: The three code-reading strategies and a preview of the week's vocabulary |
| [Demonstration.ipynb](./Demonstration.ipynb) | Comprehensions, `lambda` with `sorted`, error handling, and a first class, each as an [Associate](../../Guides/glossary.md#term-associate) draft you read and direct. An optional 🧗 Stretch section closes the notebook |
| [Quest.ipynb](./Quest.ipynb) | **[Quest 02b](../../Guides/glossary.md#term-quest): The Subscription Churn Memo** (about 90 min). It covers churn by plan, a customer-lifetime number with two honest definitions, and a board-pack draft with a silent bug |
| Debrief.ipynb | Worked answers and the case for each of the two lifetime fixes. It also holds the [AI failure gallery](../../Guides/glossary.md#term-ai-failure-gallery): Bare `except`, a mutable default argument, and the comprehension that drops records. Read it after you attempt the quest |

