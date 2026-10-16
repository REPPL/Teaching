# Stoa workflow: Group work at Runnymede

*How your team runs the group project, on Microsoft Teams or in a [Stoa](./glossary.md#term-stoa) room: Rooms, [stand-ups](./glossary.md#term-stand-up), [decision logging](./glossary.md#term-decision-entry), and your team's record. You need this from Week 4, when your team's meetings begin.*

At [Runnymede Analytics](./glossary.md#term-runnymede-analytics), when the client asks "*why did you remove that data from your analysis?*", someone answers with a date and a reason.

Your group project works the same way: You record what you're doing, including the [decisions](./glossary.md#term-decision) that were taken, why they were taken, and what you expect from it.


## Contents

1. [Rooms](#1-rooms)
2. [Team setup in Week 4](#2-team-setup-in-week-4)
3. [The weekly stand-up](#3-the-weekly-stand-up)
4. [The DECISION: convention](#4-the-decision-convention)
5. [The Stoa room's Associate](#5-the-stoa-rooms-associate)
6. [Process evidence](#6-process-evidence)
7. [Weekly export and backup](#7-weekly-export-and-backup)
8. [Etiquette and conflict](#8-etiquette-and-conflict)


## 1. Rooms

Your team meets on **Microsoft Teams**, with your university account. A [Stoa](https://withstoa.com/) room is the alternative, and using one is optional, although it remains the more convenient option for the team. Markers are interested in your **recorded process** (regular meetings, logged <!-- plain-language: everyday decision -->decisions, and visible contributions), not any single tool.

In either room, your team keeps the same record:

- Your weekly stand-ups ([section 3](#3-the-weekly-stand-up))
- Your `DECISION:` entries ([section 4](#4-the-decision-convention))
- Your meeting transcripts or notes, exported every week ([section 7](#7-weekly-export-and-backup))
- Each member's [SpecStory](./glossary.md#term-specstory) history, in `.specstory/history/`

> ⚠️ **Remember:** This module is designed as a safe space for you to experiment. That means, adapting the above to make it practical and useful.
>
> Don't spend your energy on worrying about this and/or trying to figure out what I want. When you can justify a decision, it's probably the right one!

The [assessment interpretation document](../Assessment/interpretation.md) explains what we see across your meetings, SpecStory, and your submissions.

### Microsoft Teams

Record every meeting, as [section 2](#2-team-setup-in-week-4) describes. Keep a `decisions.md` in your team repository, with the date, the `DECISION:` line, the reasoning, and the owner of each entry.

### Stoa

Stoa is a live team room that makes your team's record easier to keep. It is made by <!-- plain-language: everyday SpecStory -->SpecStory, the company whose extension records your AI sessions in your Codespace ([Your workstation guide](./codespaces-start.md)). Stoa transcribes your meetings, captures <!-- plain-language: everyday decision -->decisions and action items with named owners, and gives the team a shared **[Associate](./glossary.md#term-associate)**, the room's built-in Claude agent.

Stoa normally charges by the hour. **For this module it is free**. I'll confirm in Week 4 how you get the free access. [Section 2](#2-team-setup-in-week-4) covers how you sign up. If Stoa ever asks you for payment details (it shouldn't!), stop and tell your tutor. **Do not pay.**

A Stoa room keeps:

- **The room transcript**: Who said or typed what, by name, with timestamps
- **<!-- plain-language: everyday decision -->Decisions and action items**: Anything captured as a <!-- plain-language: everyday decision -->decision or action, and who owns it
- **The Associate's activity**: What your team asked the Associate, and what it produced

Stoa rooms are **public**, so anyone, me included, can see your room. Your team exports its transcripts and submits them. Markers assess them as evidence of your process.

Your team may lose Stoa through an outage, an account problem, or a change in the arrangement mid-term. If it does, move to Microsoft Teams and keep the same record. Tell me when your team changes room.


## 2. Team setup in Week 4

You form your own team before Week 4. The [group project brief](../Assessment/group-project.md) sets its size. Your team sets up its room in the Week 4 workshop.

**On Microsoft Teams:**

1. **Start the meeting.** One team member starts a Microsoft Teams meeting and invites the rest of the team. Every member joins with their own university account, so that your names in the transcript match the register
2. **Turn on transcription or recording** for every meeting. Where neither is available, appoint a minute-taker

**In a Stoa room:**

1. **Create your account.** Sign up at [withstoa.com](https://withstoa.com/) with the **"throwaway" Google account** you made in Week 1. Do not use your real name, but an alias instead (e.g. "Alex Anders"). The name you use in Stoa must not match your real name (because all of it can be seen by anyone else in the class); having said that, you are, of course, free to share your alias with friends and classmates if you wish to do so
2. **Create the room.** One team member creates the room, from the Stoa home screen after signing in (TBC: I may do that for you)
3. **Name the room** after your team's letter, such as **<!-- gen:values.yml#module.code -->MN5813<!-- /gen -->-Team-A**. Markers use this name to match your transcripts to your submission
4. **Everyone joins.** The room creator invites the rest of the team with the room's invite or share option. Every member joins with their own account, under their own name. Check in the workshop that every name appears correctly. A member who takes part through someone else's screen does not appear in the transcript

**Then, in either room:**

1. **Hold your first [stand-up](./glossary.md#term-stand-up) in the workshop.** This first one is **15 minutes**: Each member says what they have done, what they will do next, and what is blocking them. Then log your first `DECISION:`, normally your meeting day and time for the coming weeks. [Section 3](#3-the-weekly-stand-up) covers the full weekly stand-up
2. **Complete the rest of the setup as a team:**
   - Agree on your team repository, where your shared evidence lives. Log it as a `DECISION:`
   - Agree who exports the transcript or notes each week (rotate it). Log the rota as a `DECISION:`
   - Write your team's working agreements, and log them as a `DECISION:`. Atlassian's [working agreements template](https://www.atlassian.com/team-playbook/plays/working-agreements) takes about 10 minutes

Finish setup **before you leave the Week 4 workshop, or as a team by the end of the same day**. Setup is complete when you can tick every item below:

- [ ] Room set up: A recorded Microsoft Teams meeting, or a Stoa room named after your team's letter
- [ ] Every member visible in the room under their own name
- [ ] Meeting day and time agreed
- [ ] Team repository agreed and logged as a `DECISION:`
- [ ] Export rota agreed and logged as a `DECISION:`
- [ ] Working agreements logged as a `DECISION:`


## 3. The weekly stand-up

The [group project brief](../Assessment/group-project.md) sets how often your team holds a stand-up, and for how long, from Week 4 until submission. Hold it in your team's room ([section 1](#1-rooms)). The first stand-up, in the Week 4 workshop, is shorter ([section 2](#2-team-setup-in-week-4)). You can meet more often, and hold longer working sessions in the room. Week 7 is one such session: Your team's self-paced [Sprint Zero](./glossary.md#term-sprint-zero).

The agenda is the same every week:

### Progress

Each member reports, in turn, what they have done since the last stand-up. Be concrete.

> "I cleaned the attendance-time columns: About 5% of incidents had no first-engine time, handled per last week's <!-- plain-language: everyday decision -->decision. The cleaned file is in the repo as `data/cleaned_incidents.csv`, and the SpecStory transcript of the session is in `.specstory/history/`."

### Blockers

Say what is **blocking your work**, and what would help, so the team can act on it.

> "I can't get the engine counts per incident to match `NumPumpsAttending`; I think it's the 1,400 mobilisations whose incident isn't in the extract. I need a second pair of eyes for twenty minutes, or a <!-- plain-language: everyday decision -->decision that we footnote it and move on."

### Decisions

When the team settles something, say or type it with the `DECISION:` prefix ([section 4](#4-the-decision-convention)).

> "`DECISION:` We treat fires, false alarms, and special services as separate series in all time-based charts. We do this because pooling them hides the summer fire peak under the false-alarm volume. Owner: Marta updates the two existing figures by Friday."

### Next steps

Every action has one owner and a date. "We should all look at the visualisations" is a wish. "Dayo drafts the response-time figure by Tuesday, Priya reviews it against [TRACE](./glossary.md#term-trace) by Thursday" is a plan. You meet TRACE in Week 6, in the DataViz design guide. Until then, "a teammate reviews it" does the same job.

> "Next stand-up Monday 4pm. Dayo: Response-time figure by Tuesday. Priya: TRACE review Thursday. Marta: Chart fixes Friday. Ben: Draft the data-cleaning section of the report, first pass Sunday."

Keep discussion of *how* to do things out of the stand-up. Note the topic, then schedule a separate working session for it, ideally also in the room.


## 4. The DECISION

Log every significant agreement with the prefix `DECISION:`, followed by **what** you decided, **why**, and **who owns** any resulting action. On Microsoft Teams, add it to your team's `decisions.md` ([section 1](#1-rooms)). In a Stoa room, type it into the room. For example:

```
DECISION: Exclude incidents with no first-engine attendance time from
the response-time analysis because no engine attended them (about 5%
of rows, mostly calls stood down before arrival). We keep them in the
false-alarm counts and note the cut in the report. Owner: Priya
updates the loading script.
```

The [group project brief](../Assessment/group-project.md) explains how markers read your <!-- plain-language: everyday decision -->decision trail.

### Good and bad entries

**Bad:**

> `DECISION:` Use pandas for the cleaning.

No reasoning, no owner, and it is barely a <!-- plain-language: everyday decision -->decision.

**Good:**

> `DECISION:` Keep the 1,400 mobilisations whose incident is not in the incidents table. Use a left join with an indicator column, rather than an inner join. We keep them because dropping them silently understates station workload in the last weeks of the extract. We flag them in a new column. Owner: Ben implements; Marta spot-checks 20 rows.

This entry gives *what*, *why*, the *alternative* considered, and *named owners*.

Log reversals too. For example:

> `DECISION:` Reverse our 19 October <!-- plain-language: everyday decision -->decision on the unmatched mobilisations. The flagged column revealed they distort the per-borough figures. So we now drop them from the borough analysis and say so.

### A second prefix from Week 9: `CRIT`

From Week 9's [Gallery](./glossary.md#term-gallery), one member of your team is the scribe. The scribe types every [Four-D crit](./glossary.md#term-four-d-crit) your team receives into your team's record (your meeting notes or your Stoa room), as a [`CRIT` entry](./glossary.md#term-crit-entry). Each figure gets one entry per crit round. The template is in Week 9's Introduction notebook, section "The scorecard". Crit outcomes then become ordinary `DECISION:` entries: Which change you accepted, why, owner, and deadline.


## 5. The Stoa room's Associate

In a Stoa room, the **Associate** can see what your team says and types there. Use it in these ways:

- **"Summarise our disagreement."** When two of you keep arguing over a choice, ask the Associate to summarise both positions. A neutral summary often settles it, or turns it into a `DECISION:` you can log
- **"Draft a <!-- plain-language: everyday spec -->spec from this discussion."** Suppose you have discussed a figure or an analysis for twenty minutes without a conclusion. Ask the Associate to turn the discussion into a short written specification (a plan of what to build). Then edit it as a team. This is the [GENERATE-JUDGE](./glossary.md#term-generate-judge) move from the [AI guide](./ai-guide.md), done as a team
- **"List the open questions."** At the end of a messy session, ask the Associate what was raised but not resolved
- **"Challenge our approach."** Before you <!-- plain-language: everyday commit -->commit to a plan, ask the Associate to argue against it

⚠️ **The Associate is a participant, not a member.** It drafts, summarises, and challenges. Your team *decides*. Every <!-- plain-language: everyday decision -->decision in your log must be yours, for reasons you can defend. "The Associate said so" is not a reason.


## 6. Process evidence

The [group project brief](../Assessment/group-project.md) explains what we look at from your recorded process. The [assessment interpretation document](../Assessment/interpretation.md) lists the process indicators.

**There is an alternative evidence route:** If you cannot make and/or keep a recording, talk to me early. The [interpretation document](../Assessment/interpretation.md) explains the alternatives.


## 7. Weekly export and backup

Every week, after your stand-up, **the member on your export rota exports your team's record** ([section 2](#2-team-setup-in-week-4)).

- On Microsoft Teams, download the meeting transcript, or save the minute-taker's notes
- In a Stoa room, use the room's export, download, or sync option. Save at least the meeting notes, the <!-- plain-language: everyday decision -->decisions log, and the transcript, in whatever format Stoa offers
- Save them in one folder per session, named by date, such as `transcripts/2026-10-19-standup/`
- Put the folder in your team repository, next to your `.specstory/history/`. Then <!-- plain-language: everyday commit -->commit and push it


## 8. Etiquette and conflict

- **Cameras and microphones are strongly recommended,** but typed contributions count like spoken ones (just make sure your record keeps them!)
- **Log disagreements.** When you disagree and then decide, the [`DECISION:` entry](./glossary.md#term-decision-entry) records it: "We considered X and Y; we chose Y because…"
- **Criticise the analysis, not the <!-- plain-language: everyday Analyst -->analyst.** "That merge double-counts engine minutes" is useful. "You always get the merges wrong" is not. The Four-D crit's first round (describe before you diagnose) works on teammates' code and prose too
- **If someone stops showing up:** Ask them directly and kindly, and note the absence in your record (for example, "Alice absent, third week. Bob has messaged to check in."). After two weeks with no contact or contribution, **email me**
- **If the team is stuck in a conflict it cannot resolve:** Email me early, with the details and the transcript of the disagreement

---

*Related guides: [Your workstation](./codespaces-start.md) · [AI guide](./ai-guide.md) · [Assessment interpretation](../Assessment/interpretation.md) · [Group project brief](../Assessment/group-project.md)*
