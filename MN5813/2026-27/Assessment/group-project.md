# Group project

*A team analysis of every 999 incident London's fire brigade has attended since January 2025. You keep a record of how you work, on Microsoft Teams or in a [Stoa](../Guides/glossary.md#term-stoa) room. You submit a Jupyter notebook.*

> **Memo: [Runnymede Analytics](../Guides/glossary.md#term-runnymede-analytics), Client Engagements Desk**
>
> *To: Junior [Analyst](../Guides/glossary.md#term-analyst) teams*
>
> *Re: Engagement FRS-2026*
>
> The operations director of a fire and rescue service has engaged Runnymede Analytics. She has the public record of every 999 incident her crews attended and every engine they sent. She wants a small number of well-chosen questions, answered from the evidence, with figures she can put in front of her board. Where are response times getting worse? What do the false alarms cost? Which stations attend the most incidents? What delays crews? Your team has the engagement. Your [Associate](../Guides/glossary.md#term-associate) is on the project with you. You sign the work.

*(Shocking revelation: Both the director and the firm are invented. Your **Associate** is your AI tool of choice, with the default being the one provided by the University to all students (see the [AI guide](../Guides/ai-guide.md)). While the people are not real, the data is: It is the London Fire Brigade's published record of incidents and mobilisations, described in this [note](./lfb-data.md).)*


## 1. The task

In a team of three or four, you analyse the **London Fire Brigade incident and mobilisation records**. They contain every incident attended from January 2025, and every engine sent to it. You submit a **Jupyter notebook report** with your questions, your data work, your analysis, your visualisations, and your conclusions.

- **Formative:** Your team gets a feedback letter (a suggested classification), not a mark
- **Dataset:** The two fire-brigade tables, the same for every team. The [data note](./lfb-data.md) explains how you get them, and how your team works from one copy
- **Timeline:** The project runs from **Week 4** (team meetings begin) to **Week 10** (group presentation). Submission is your team repository's last push before **<!-- gen:values.yml#assessments.group.deadline -->Thursday 3 December 2026, 12:00 (UK time)<!-- /gen -->**. Your feedback arrives before the January revision session
- **AI use:** Expected throughout, for code, data exploration, figure critique, and prose. What is assessed is your judgement and <!-- plain-language: everyday abcd record -->the record you keep. See the [AI guide](../Guides/ai-guide.md) and the [interpretation document](./interpretation.md)


## 2. Requirements

Your notebook report must include:

1. **Introduction.** A clear problem statement and rationale. State your **two to four questions** (four the absolute maximum), why they matter, what a reader should expect, and your aim and objectives
2. **Review.** Place your questions in the context of the literature, with a **minimum of five academic references**. Literature on emergency-service operations and response times is optional (to highlight the relevance). Literature on analytics practice and data visualisation design matters more
3. **Data loading and cleaning.** Load the two tables, describe them, join them, and deal with their problems. The [data note](./lfb-data.md) describes the problems to look out for. Log every non-obvious cleaning choice as a [`DECISION:` entry](../Guides/glossary.md#term-decision-entry) (section 3). Your notebook must also write the **cleaned incidents table** described in section 4
4. **Data wrangling with derived features.** Create the features relevant to your questions. Examples include a response-time continuum (against the Brigade's target), a false-alarm flag by property type, and engine minutes per incident. Other examples are the weekday and time of day, and a per-station or per-borough aggregate where feasible
5. **Analysis.** Answer your questions with pandas (filtering, grouping, reshaping, and aggregation). Discuss the accuracy, utility, and trade-offs of the procedures you chose
6. **Visualisations.** Every key figure passes the [TRACE checklist](../Guides/glossary.md#term-trace). Each carries a short **[design rationale](../Guides/glossary.md#term-design-rationale)**: Why this chart form, for this task, for this audience, and so on. Expect **4 to 8 key figures**, each with a rationale of about 150 to 300 words
7. **Concluding remarks.** Limitations, managerial implications, and possible future improvements, all grounded in your results
8. **[AI Use Record](../Guides/glossary.md#term-ai-use-record).** Required. See section 7

**The notebook must run top-to-bottom** from a fresh start (*Restart & Run All*) without errors. This is essential!


## 3. Process

Your team meets on Microsoft Teams. A [Stoa](https://withstoa.com/) room is the optional alternative, and it makes your team's record a little more convenient to keep. The [Stoa workflow guide](../Guides/stoa-workflow.md) explains how to run both. Whichever room you use, the requirements are:

- Hold **at least one recorded 30-minute [stand-up](../Guides/glossary.md#term-stand-up) per week from Week 4**, using the agenda *Progress / Blockers / <!-- plain-language: everyday decision -->Decisions / Next*
- Start every logged <!-- plain-language: everyday decision -->decision with **`DECISION:`**, especially data-cleaning and design <!-- plain-language: everyday decision -->decisions. The [Stoa workflow guide](../Guides/stoa-workflow.md) shows what a good entry looks like. Markers read these entries when assessing Data management
- **Export your meeting transcripts or notes weekly** and <!-- plain-language: everyday commit -->commit it to the team repository (section 4)

**Your [SpecStory](../Guides/glossary.md#term-specstory) history.** Transcripts that show you checking your Associate's cleaning steps count as evidence. Checks include counting rows, inspecting what a merge did, and rejecting a plausible-but-wrong suggestion.

If you cannot use a tool for accessibility or access reasons, contact me early to agree an alternative.


## 4. Deliverables and logistics

What you submit, and when:

- **Submission.** Your team repository is the submission. It carries the notebook, the two tables and their manifest (see the [data note](./lfb-data.md)), and the cleaned incidents table. **There is no Moodle upload for the group project!**
- **Cleaned table.** `data/cleaned_incidents.csv`, written by your notebook. One row per incident, with `IncidentNumber` as the key and at least these columns: `DateOfCall`, `IncidentGroup`, `IncGeo_BoroughName`, `IncidentStationGround`, `FirstPumpArriving_AttendanceTime`, `NumPumpsAttending`, `PumpMinutesRounded`, and `Notional Cost (£)`
- **AI Use Record.** In the notebook (section 7)
- **Process record.** <!-- plain-language: everyday commit -->Commit and push the weekly exports of your meeting transcripts or notes and each member's SpecStory history to the team repository with the notebook
- **Team size.** Three or four, self-selected
- **Submission date.** Your team repository's last push before **<!-- gen:values.yml#assessments.group.deadline -->Thursday 3 December 2026, 12:00 (UK time)<!-- /gen -->** is read

Key dates in the teaching schedule:

- **Week 3.** Assessment briefing: This <!-- plain-language: everyday brief -->brief and the [interpretation document](./interpretation.md), walked through in class
- **Week 4.** Weekly stand-ups begin
- **Week 7.** **Independent practice week**: No classes. Your team runs its **[Sprint Zero](../Guides/glossary.md#term-sprint-zero)** at its own pace, finding out what the two tables contain
- **Week 9.** **The [Gallery](../Guides/glossary.md#term-gallery)**: Structured peer critique of your draft figures, using the [Four-Ds](../Guides/glossary.md#term-four-d-crit)
- **Week 10.** **Group presentation**: Each team presents for 10 minutes, then takes 5 minutes of questions on its <!-- plain-language: everyday decision -->decisions
- **<!-- gen:values.yml#assessments.group.deadline -->Thursday 3 December 2026, 12:00 (UK time)<!-- /gen -->.** **Submission**: Your team repository's last push before this time is the work the letter reads
- **January revision session.** Your team's feedback letter arrives well before this session: An indicative classification and comments for each criterion. Nothing is marked


## 5. The rubric

Your feedback letter uses the rubric for the [individual report](./individual-report.md), with an indicative classification for each criterion. It leaves out Methods. Data management and Professionalism carry a weight of 30 each, and every other criterion 10. The weights order the letter, heaviest first; they are not marks.


## 6. Evidence

This section explains what evidence the feedback reads for each criterion. The [interpretation document](./interpretation.md) explains what both assessments share.

- **Introduction.** Markers read the notebook for a problem statement your team can defend
- **Review.** Markers read the notebook for five or more academic references that your report uses, not only lists. Visualisation-design literature that supports your figure choices is particularly welcome!
- **Data management.** Markers read the **recorded process** as much as the result. They read `DECISION:` entries in your team's record for cleaning choices, and SpecStory transcripts that show you checking Associate-proposed steps. They also run a notebook that reproduces the final dataset top-to-bottom. The <!-- plain-language: everyday decision -->decision trail is the primary evidence they read
- **Analysis & presentation of results.** Markers check that each key figure passes [TRACE](../Guides/glossary.md#term-trace) and carries a design rationale: Justified for task, form, and audience, with the trade-offs you weighed
- **Concluding remarks.** Markers read the notebook for limitations and implications traceable to *your* results, including what the data cannot support
- **Professionalism.** Markers assess everything you submit, <!-- plain-language: everyday abcd record -->the record included, against the rubric. Exports that are current and well organised, <!-- plain-language: everyday decision -->decisions that can be found, and an appropriate AI Use Record all count

**Process indicators.** The [interpretation document](./interpretation.md) lists the counts markers take from your record.


## 7. The AI Use Record

Every submission includes an **AI Use Record**. The [interpretation document](./interpretation.md) explains what it contains, with a worked example.


## 8. FAQs

### Do we have to fetch the data ourselves?

Yes, once each, with one command. The [data note](./lfb-data.md) walks through it.

### Can our Associate write our report?

It may draft anything: Code, figures, and prose. You must check it, take responsibility for it, and record it in your AI Use Record.

### Is there a self-check we can run before we submit?

Yes. Run `python3 Tools/check.py` in your project folder. It runs the marker's automated first pass (the Tier-1 checks): Sections present, references, the cleaned table's shape, and figures readable. It prints a checklist of what to fix before you submit. A red (failed) line never blocks submitting. The [Tools README](../Tools/README.md) explains it.

### Do we all need to be in every stand-up?

Aim for full attendance. What matters is the pattern: The weekly stand-ups in section 3, with everyone contributing regularly across the term. One missed meeting with a note in the transcript is fine.

### We fixed the data but forgot to log decisions.

The <!-- plain-language: everyday decision -->decision trail is the primary evidence for Data management, one of the two most important marking criteria. Start logging straight away. `DECISION:` entries added at the time are better than a reconstruction, but a retrospective is far better than trying to pretend it didn't happen.

### Our questions turned out to be boring. Can we change direction mid-project?

Yes. Log it ("`DECISION:` pivoting from X to Y because…"), update your introduction, and carry on. A recorded change of direction with reasons is good evidence of judgement.

### Whose SpecStory history counts, since we work on different machines?

Everyone's history counts. Each member's `.specstory/history/` shows their own hands-on contribution. Your meeting transcripts or notes show the team's shared work. <!-- plain-language: everyday commit -->Commit and push both to the team repository (section 4). Check in Week 4 or 5, not Week 10, that your history is being saved. [Your workstation guide](../Guides/codespaces-start.md) shows how to check.

### How polished do figures need to be for the Week 9 Gallery?

Draft quality is fine. Bring real figures from your analysis, run them through the Four-Ds, and keep the critique notes. Acting on critical feedback is, well, critical.

### How many figures, and how long should the rationales be?

Section 2, item 6, sets the figure count and rationale length. There is no overall length limit for the notebook.

### Does everyone in the team get the same feedback?

Yes.

---

*Questions? Ask in class, in your Stoa room if your team uses one (the agent has read this <!-- plain-language: everyday brief -->brief), or at the Week 10 group presentation. See also the [individual report brief](./individual-report.md) and the [module overview](../README.md).*
