# Assessment interpretation

*How markers read the <!-- gen:values.yml#module.code -->MN5813<!-- /gen --> rubric in an AI-open module in <!-- gen:values.yml#module.year -->2026-27<!-- /gen -->.*

---

## 1. The AI-open statement

> In <!-- gen:values.yml#module.code -->MN5813<!-- /gen --> you may use AI tools for every part of your work, and we expect you to. There is no penalty for using AI and none for declining it. What is assessed is your judgement: The questions you ask, the outputs you accept or reject, the designs you defend, and <!-- plain-language: everyday abcd record -->the record you keep. Every submission includes an [AI Use Record](../Guides/glossary.md#term-ai-use-record).

### The AI Use Record

An AI Use Record is half a page to a page long. It opens with a declaration line, as in the worked example below.

**I encourage you to experiment:** Work towards your individual 'AI declaration', the one document you think through, write, and review without AI. It goes in the PDF you submit with your [individual report](./individual-report.md).

Change the declaration line so it fits your submission. These parts follow the declaration:

1. **Tools used**: Each tool and where you used it (for example "Copilot in VS Code; the [Stoa](../Guides/glossary.md#term-stoa) agent for team sessions")
2. **What each was used for**: Specific, not general
3. **Notable rejections and corrections**: Two or three moments where you overruled the AI, with your reasons
4. **Reflection**: One short paragraph on where the AI helped, where it misled or slowed you, and what you would do differently

For the individual report, write "I" rather than "we". A worked example:

> **AI Use Record: Team 7, Engagement FRS-2026**
>
> *"This submission was produced with AI assistance. <!-- plain-language: everyday abcd record -->The record below summarises the tools we used, what we used them for, and notable outputs we rejected or corrected. See our [Prompt Diaries](../Guides/glossary.md#term-prompt-diary) for further details."*
>
> **Tools used.** GitHub Copilot in VS Code (individual coding, Weeks 4-9); the Stoa agent (team sessions and figure critique).
>
> **What each was used for.** Copilot drafted most of the cleaning pipeline and the first version of every figure; we specified the transformations and wrote the interpretation and conclusions ourselves. The Stoa agent generated alternative chart forms for Figures 2 and 4 and critiqued our drafts against [TRACE](../Guides/glossary.md#term-trace).
>
> **Notable rejections and corrections.** (1) Copilot's first join of the mobilisations to the incidents was an inner join. It silently dropped about 1,400 engines whose incident is not in the extract. We caught it with a row count before and after, and switched to a left join with an indicator column. We logged the choice as a `DECISION:` on 12 November. (2) The agent proposed a stacked bar for response time by borough. It hid the comparison the question needed, and we chose a dot plot against the six-minute target instead. (3) One suggested reference did not exist; we removed it and verified every remaining source against its DOI.
>
> **Reflection.** The [Associate](../Guides/glossary.md#term-associate) was fastest on wrangling and weakest on our data's quirks. Every join needed a row-count check. Its first mean attendance time silently excluded the incidents no engine attended. Next time we would give it the data note earlier: Half our corrections traced back to it guessing what a column meant.

---

## 2. Things that matter

| What | Where it lives | Who can see it |
|------|----------------|----------------|
| **Your [Prompt Diary](../Guides/glossary.md#term-prompt-diary)** | `PromptDiary.md` in your repository, kept by you after each AI session and submitted with your work | Markers, at marking |
| **Team meeting transcripts or notes** | Your team's meetings on Microsoft Teams or in a Stoa room, exported weekly and submitted with the project | Markers, at marking |
| **Your submitted notebook and files** | Your submission | Markers, moderators, and external examiners |

- **What markers cannot see**: Your screen, your unrecorded conversations, and anything you leave out of your submission
- **How you submit**: The group project is your team repository's last push before <!-- gen:values.yml#assessments.group.deadline -->Thursday 3 December 2026, 12:00 (UK time)<!-- /gen -->. The [individual report brief](./individual-report.md) explains how to submit the report
- **Retention**: Submitted records are kept under the University's retention schedule for assessed work
- **Third-party tools**: [Stoa](https://withstoa.com/) stores your room on its servers, under its privacy policy. It has been reviewed against the University's data-protection requirements
- **Concerns**: Speak to me (contact details are on Moodle), or use the School's anonymous feedback channels
- **One firm rule**: Never paste other people's personal data into any AI tool. If your dataset identifies a living person, anonymise it before analysis
- **Alternative evidence route**: Stoa is optional. If a module tool or the Prompt Diary does not suit you, contact me early. We then agree another way to show your process

---

## 3. The rubric

Both assessments use one rubric. The [individual report brief](./individual-report.md) contains it, followed by what markers read for each criterion. The [group project brief](./group-project.md) explains how the feedback letter uses it.

Every reference must exist and support the claim you cite it for. AI tools invent plausible citations, and markers check. A fabricated reference is an academic-integrity matter, whichever tool produced it.

---

## 4. Process indicators

Markers count the following in your submitted record. **Important:** No mark is computed from any of them, but they can point markers to useful explanations.

- **Team sessions per week** (from Week 4): At least one, the weekly [stand-up](../Guides/glossary.md#term-stand-up)
- **[`DECISION:` entries](../Guides/glossary.md#term-decision-entry) per member**: No quota, but a visible contribution from everyone
- **Contribution-turn spread** (turns across members in the team transcripts): No threshold. One member should not dominate while the others stay silent
- **Session continuity** (the dates of the sessions in your submitted record): Sessions should spread across the working period, not cluster in the final days

What the marker reads in the work outweighs any count. Five `DECISION:` entries that record a choice, a reason, and a rejected alternative count for more than a hundred that say "decided to proceed".

---

*Questions? Ask in the Week 3 briefing, in any workshop, or by email. See also the [module overview](../README.md), the [AI guide](../Guides/ai-guide.md), the [Stoa workflow](../Guides/stoa-workflow.md), and the Data Visualisations design guide.*
