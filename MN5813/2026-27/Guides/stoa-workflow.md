# Stoa Workflow: Group Work at Runnymede

*How your team runs the group project: Rooms, [stand-ups](./glossary.md#term-stand-up), [decision logging](./glossary.md#term-decision-entry), and what is recorded. You need this from Week 4, when the [Stoa](./glossary.md#term-stoa) rooms open.*

> ⚠️ **Draft:** This page is a draft. It will be confirmed in Week 3.

At [Runnymede Analytics](./glossary.md#term-runnymede-analytics), when the client asks "why did you drop that data?", someone answers with a date and a reason. Your group project works the same way.

## Contents

1. [What Stoa is, and what is recorded](#1-what-stoa-is-and-what-is-recorded)
2. [Team setup in Week 4](#2-team-setup-in-week-4)
3. [The weekly ritual: the recorded stand-up](#3-the-weekly-ritual-the-recorded-stand-up)
4. [The DECISION: convention](#4-the-decision-convention)
5. [Using the room's Associate well](#5-using-the-rooms-associate-well)
6. [How process evidence feeds the rubric](#6-how-process-evidence-feeds-the-rubric)
7. [Weekly export and backup](#7-weekly-export-and-backup)
8. [Etiquette and conflict](#8-etiquette-and-conflict)
9. [Fallback plan if Stoa is unavailable](#9-fallback-plan-if-stoa-is-unavailable)

## 1. What Stoa is, and what is recorded

[Stoa](https://withstoa.com/) is a live team room for group work. It is made by <!-- plain-language: everyday SpecStory -->SpecStory, the company behind the extension that records your AI sessions in your Codespace (see the [Codespaces Start guide](./codespaces-start.md)). Your team meets in the room. Stoa transcribes the session, captures <!-- plain-language: everyday decision -->decisions and action items with named owners, and provides the room's built-in **[Associate](./glossary.md#term-associate)**, a Claude agent the whole team shares.

Stoa normally costs $5 per hour, pay-as-you-go. **For this module it is free**, by agreement with <!-- plain-language: everyday SpecStory -->SpecStory. Your workshop tutor confirms in Week 4 how the free access reaches you, and the module arrangement covers your room. [Section 2](#2-team-setup-in-week-4) covers how you sign up. If Stoa ever asks you for payment details, stop and tell your tutor. Do not pay.

### What is recorded: full transparency, up front

The room keeps:

- **The room transcript**: Who said or typed what, by name, with timestamps
- **<!-- plain-language: everyday decision -->Decisions and action items**: Anything captured as a <!-- plain-language: everyday decision -->decision or action, and who owns it
- **The Associate's activity**: What your team asked the Associate, and what it produced

Module staff can read your group's transcripts. The transcript is your team's evidence of process, and process evidence is part of how the group project is assessed. Nothing in the room is private from the marking team. Everything in the room is private from other groups.

The assessment interpretation document, section "2. What we collect and why", lists what the module collects across Stoa, [SpecStory](./glossary.md#term-specstory), and your submissions.

## 2. Team setup in Week 4

Teams are announced on Moodle before Week 4. Each team creates its Stoa room in the Week 4 workshop.

1. **Create your account.** Everyone signs up at [withstoa.com](https://withstoa.com/) with the **module Google account** they made in Week 1. Use your name as it appears on the register, so your name in the transcript matches the register
2. **Create the room.** One team member creates the room. Look for the option to create a new room or session on the Stoa home screen after signing in
3. **Name the room** **<!-- gen:values.yml#module.code -->MN5813<!-- /gen -->-Group-NN** (so Group 7 is **<!-- gen:values.yml#module.code -->MN5813<!-- /gen -->-Group-07**). Staff use this name to find your room and to match your transcripts to your submission
4. **Everyone joins.** The room creator invites the rest of the team with the room's invite or share option. Every member joins with their own account, under their own name. Check in the workshop that all names appear correctly. A member who takes part through someone else's screen is invisible in the evidence
5. **Add module staff.** Your workshop tutor tells you how staff access works. Do this in the workshop
6. **Hold your first [stand-up](./glossary.md#term-stand-up) in the workshop.** A stand-up is a short status meeting. This first one is **15 minutes**: Each member says what they have done, what they will do next, and what is blocking them. Then log your first `DECISION:`, normally your meeting day and time for the coming weeks. The full weekly stand-up is in [Section 3](#3-the-weekly-ritual-the-recorded-stand-up)
7. **Complete the rest of the setup as a team:**
   - Agree where your shared evidence lives: A shared git repository (recommended) or a shared folder. Log it as a `DECISION:`
   - Agree who exports the transcript each week (rotate it) and log the rota as a `DECISION:`
   - Agree your working agreements (the [Atlassian working agreements play](https://www.atlassian.com/team-playbook/plays/working-agreements) is a 10-minute template) and log them as a `DECISION:`

Finish setup **before you leave the Week 4 workshop, or as a team by the end of the same day**. Setup is complete when you can tick every item below:

- [ ] Room created and named **<!-- gen:values.yml#module.code -->MN5813<!-- /gen -->-Group-NN**
- [ ] Every member visible in the room under their own name
- [ ] Module staff added
- [ ] Meeting day and time agreed
- [ ] Shared evidence location agreed and logged as a `DECISION:`
- [ ] Export rota agreed and logged as a `DECISION:`
- [ ] Working agreements logged as a `DECISION:`

## 3. The weekly ritual: the recorded stand-up

From Week 4 until group submission, your team holds **at least one recorded stand-up per week, roughly 30 minutes, in your Stoa room**. The Week 4 first stand-up is a shorter, 15-minute version ([Section 2](#2-team-setup-in-week-4)). More meetings are fine. Longer working sessions in the room are encouraged. Week 7 holds a full working session, your self-paced [Sprint Zero](./glossary.md#term-sprint-zero). The weekly stand-up is required.

The agenda is the same every week, with four items:

### Progress: what moved since last time

Each member reports briefly, in turn. Be concrete.

> "I cleaned the attendance-time columns: About 5% of incidents had no first-engine time, handled per last week's <!-- plain-language: everyday decision -->decision. The cleaned file is in the repo as `data/cleaned_incidents.csv`, and the SpecStory transcript of the session is in `.specstory/history/`."

### Blockers: what is stuck, and what would unstick it

Say what is blocking you, so the team can help.

> "I can't get the engine counts per incident to match `NumPumpsAttending`; I think it's the 1,400 mobilisations whose incident isn't in the extract. I need a second pair of eyes for twenty minutes, or a <!-- plain-language: everyday decision -->decision that we footnote it and move on."

### Decisions: what the team is agreeing today

When the team settles something, say or type it with the `DECISION:` prefix ([Section 4](#4-the-decision-convention)).

> "`DECISION:` We treat fires, false alarms, and special services as separate series in all time-based charts. We do this because pooling them hides the summer fire peak under the false-alarm volume. Owner: Marta updates the two existing figures by Friday."

### Next steps: who does what by when

Every action has one owner and a date. "We should all look at the visualisations" is a wish. "Dayo drafts the response-time figure by Tuesday, Priya reviews it against [TRACE](./glossary.md#term-trace) by Thursday" is a plan. TRACE is the figure checklist in the DataViz Design Guide, taught from Week 6. Before then, "a teammate reviews it" does the same job.

> "Next stand-up Monday 4pm. Dayo: Response-time figure by Tuesday. Priya: TRACE review Thursday. Marta: Chart fixes Friday. Ben: Draft the data-cleaning section of the report, first pass Sunday."

Keep discussion of *how* to do things out of the stand-up. Note the topic, then schedule a separate working session for it, ideally also in the room.

## 4. The DECISION: convention

Type every significant agreement into the room with the prefix `DECISION:`, followed by **what** you decided, **why**, and **who owns** any resulting action:

```
DECISION: exclude incidents with no first-engine attendance time from
the response-time analysis because no engine attended them (about 5%
of rows, mostly calls stood down before arrival). We keep them in the
false-alarm counts and note the cut in the report. Owner: Priya
updates the loading script.
```

How markers read your <!-- plain-language: everyday decision -->decision trail is in the group project brief, section "6. How each criterion is evidenced".

### A good/bad pair

**Bad:**

> `DECISION:` Use pandas for the cleaning.

No reasoning, no owner, and it is barely a <!-- plain-language: everyday decision -->decision.

**Good:**

> `DECISION:` Keep the 1,400 mobilisations whose incident is not in the incidents table. Use a left join with an indicator column, rather than an inner join. We keep them because dropping them silently understates station workload in the last weeks of the extract. We flag them in a new column. Owner: Ben implements; Marta spot-checks 20 rows.

This entry gives what, why, the alternative considered, and two named owners.

Log reversals too. For example:

> `DECISION:` Reverse our 19 October <!-- plain-language: everyday decision -->decision on the unmatched mobilisations. The flagged column revealed they distort the per-borough figures. So we now drop them from the borough analysis and say so.

### A second prefix from Week 9: `CRIT`

From Week 9's [Gallery](./glossary.md#term-gallery), one member of your group is the scribe. The scribe types every [Four-D crit](./glossary.md#term-four-d-crit) your group receives into your room as one scorecard entry prefixed `CRIT`. One entry per figure, per crit round. The template is in Week 9's Introduction notebook, section "The scorecard". Crit outcomes then become ordinary `DECISION:` entries: Which change you accepted, why, owner, and deadline.

## 5. Using the room's Associate well

The room's **Associate** can see what your team says and types there. Use it in four ways:

- **"Summarise our disagreement."** When two of you keep arguing over a choice, ask the Associate to summarise both positions. A neutral summary often settles it, or turns it into a `DECISION:` you can log
- **"Draft a <!-- plain-language: everyday spec -->spec from this discussion."** Suppose you have discussed a figure or an analysis for twenty minutes without a conclusion. Ask the Associate to turn the discussion into a short written specification (a plan of what to build). Then edit it as a team. This is the [GENERATE-JUDGE](./glossary.md#term-generate-judge) move from the [AI Guide](./ai-guide.md), done as a team
- **"List the open questions."** At the end of a messy session, ask the Associate what was raised but not resolved
- **"Challenge our approach."** Before you <!-- plain-language: everyday commit -->commit to a plan, ask the Associate to argue against it

⚠️ **The Associate is a participant, not a member.** It drafts, summarises, and challenges. Your team decides, and every <!-- plain-language: everyday decision -->decision in your log must be yours, for reasons you can defend. "The Associate said so" is not a reason.

## 6. How process evidence feeds the rubric

The rubric is in the group project brief. Its section "6. How each criterion is evidenced" says what markers read from your recorded process.

- **Process indicators are checks, not marks.** An indicator is a count from your record, such as meetings per week or `DECISION:` entries per member. No grade is computed from any indicator
- **A member with no recorded contribution is asked about their role, not accused.** If your name appears in no transcripts, <!-- plain-language: everyday decision -->decision log, <!-- plain-language: everyday commit -->commits, or exports, staff invite you to a conversation, and you can present other evidence
- **There is an alternative evidence route.** If a disability, caring responsibility, or access <!-- plain-language: everyday issue -->issue makes recorded live meetings difficult, talk to the module leader early. Written stand-ups, shared documents, and SpecStory sessions can carry the same weight (see the interpretation document, section "2. What we collect and why")

## 7. Weekly export and backup

Every week, after your stand-up, **one member exports the room's outputs**. They save them to **the shared space your team agreed in Week 4** ([Section 2](#2-team-setup-in-week-4)). Follow the export rota you logged in Week 4.

- Use the export, download, or sync option in your Stoa room. Save at minimum the meeting notes, the <!-- plain-language: everyday decision -->decisions log, and the transcript in whatever format Stoa offers
- Save them in one folder per session, named by date, such as `transcripts/2026-10-19-standup/`
- If your shared space is a git repository, <!-- plain-language: everyday commit -->commit them. A transcript folder next to your `.specstory/history/` makes a tidy evidence pack

At the **Week 8 evidence checkpoint**, one member uploads your team's current export bundle to the Moodle checkpoint. Nothing from it is marked. See the Week 8 README and the group project brief.

## 8. Etiquette and conflict

- **Cameras and microphones are optional.** Typed contributions are transcribed and attributed exactly like spoken ones. Contributing visibly is not optional
- **Disagreement is healthy. Log it.** When you disagree and then decide, the [`DECISION:` entry](./glossary.md#term-decision-entry) says "we considered X and Y; we chose Y because…"
- **Attack the analysis, not the <!-- plain-language: everyday Analyst -->analyst.** "That merge double-counts engine minutes" is useful. "You always get the merges wrong" is not. The Four-D crit's first round (describe before you diagnose) works on teammates' code and prose too
- **If someone stops showing up:** Ask them directly and kindly, and note the absence in the room (for example, "Sam absent, third week. Priya has messaged to check in."). After two weeks with no contact or contribution, **email the module leader**, with your transcripts as context
- **If the team is stuck in a conflict it cannot resolve:** Email the module leader early, with specifics and the transcript of the disagreement

## 9. Fallback plan if Stoa is unavailable

Markers assess your **recorded process** (regular meetings, logged <!-- plain-language: everyday decision -->decisions, and visible contributions), not any single tool. If Stoa is unavailable (an outage, an account problem, or a change in the arrangement mid-term):

1. **Meet on Microsoft Teams** (your university account) at your usual time. Turn on transcription or recording if available. Otherwise appoint a minute-taker
2. **Keep a `decisions.md`** in the group repository, with date, `DECISION:` line, reasoning, and owner. It is the same convention, typed by hand
3. **Keep using SpecStory individually.** Your personal AI sessions are still recorded in `.specstory/history/`. Individual SpecStory transcripts plus a shared `decisions.md` and meeting notes are an assessable evidence trail
4. **Tell the module leader**

---

*Related guides: [Codespaces Start](./codespaces-start.md) · [AI Guide: Working with Your Associate](./ai-guide.md) · Assessment interpretation · Group project brief*
