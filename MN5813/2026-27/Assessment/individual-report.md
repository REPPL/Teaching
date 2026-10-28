# Individual analytics report

*<!-- gen:values.yml#module.code -->MN5813<!-- /gen --> <!-- gen:values.yml#module.name -->Business Analytics Languages and Platforms<!-- /gen --> · <!-- gen:values.yml#module.year -->2026-27<!-- /gen -->*


The individual report counts 100% towards **your module mark**. You analyse the **[abcd project record](../Guides/glossary.md#term-abcd-record)** on a **[brief](../Guides/glossary.md#term-brief) you choose in Week 6**. You submit a Jupyter notebook and upload a PDF to Moodle.

Remember that this module is AI-open: You may, and are expected to, use AI throughout. Markers assess your judgement and <!-- plain-language: everyday abcd record -->the record you keep. Read the [assessment interpretation](./interpretation.md) before Week 4.

---

## 1. The brief

You are lead [Analyst](../Guides/glossary.md#term-analyst) to support a client's open source efforts. This year, the dataset is the record of **abcd** at one [release](../Guides/glossary.md#term-release). The [primer](./abcd-record.md) explains the record. You take one brief from the [list of briefs](./individual-briefs.md). The rules on that page explain how you select it.

Your brief gives you a stakeholder and a starting question. Your job is to sharpen that starting question into a **business question the stakeholder needs answered**. For example, not *"how fast are problems fixed?"* but *"for the problems somebody noticed, does a critical one wait less than a nitpick?"* A report that charts the primary measure once and never states what the stakeholder should do differently scores poorly.

Write the report as work you would hand to a client. It needs a clear problem, a method you can justify, findings the evidence supports, well-designed figures, and conclusions a manager could act on. Your [Associate](../Guides/glossary.md#term-associate) can help at every stage. **The question, the choices, and the sign-off remain yours.**


## 2. Dataset

The [primer](./abcd-record.md) shows how you download the record's tables. Every report dataset must meet the following rules:

- **At least 1,000 rows.** The rule applies to the table your brief joins to: `issues` or `commits`, which both meet it. It does not apply to the smaller tables (`decisions`, `releases`, `specs`) on their own
- **Several numerical *and* categorical variables.** Severities, categories, buckets, sources, and authors are categorical. Word counts, line counts, the durations you derive, and the degrees you compute are numerical
- **Publicly shareable or properly licensed.** The record is public and MIT-licensed. Cite it as the primer explains

Markers run your notebook exactly as submitted, without fetching anything. <!-- plain-language: everyday commit -->Keep your report notebook at the top of your `work` folder. Commit the fetched tables (`work/data/abcd/`, under 1 MB together) and their `manifest.json` with it. Load them by **relative paths**, which start inside your project folder.

These are examples of **poor** choices:

- **Too literal.** You chart the starting question once with the primary measure and sharpen nothing. There is little to write under Methods and Analysis
- **The wrong population.** Your number is computed over rows your sentence is not about. The median time-to-resolve over every resolved [issue](../Guides/glossary.md#term-issue) is near zero (the primer's first challenge). It tells you nothing about how long a noticed problem waits
- **No question in it.** If you cannot state, in one sentence, a <!-- plain-language: everyday decision -->decision someone might take differently after reading your report, sharpen again
- **The fire-brigade data.** You have already worked on it in the group project. The individual report is on the record

If you are unsure, bring your angle to any workshop in Weeks 6, 8, and 9. You can also bring it to **Polishing your brief** at the January revision session, although this may be a little late.


## 3. The client

The `abcd` tool is my project, and I am its only substantial author. Treat me as a client who has handed you my own operational record and asked for a critical reading of it. The stakeholder in your brief is a role I ask you to address.

**Findings critical of the project are expected.** Your report is marked on the quality of your reasoning and your evidence, never on whether the news is good for the project.


## 4. Required structure

Your submission is **one Jupyter notebook** plus **one PDF** in two parts. The first is an **extended executive summary** of at most one page, which expands the summary in your notebook. The second is your **[personal AI declaration](./interpretation.md)**, the one text you write without any AI help. The notebook must run top to bottom without errors. The [report template](./Template.ipynb) gives you a starting point. Structure the notebook to mirror the rubric, in these sections:

1. **Introduction**: The problem statement, your aim and objectives, and the concepts you draw on. By the end of the first screen, a reader knows what question you are answering and why it matters
2. **Review**: A short literature and context review with **at least five academic references**. It may, and often should, include the visualisation-design literature you build on (Tufte, Few, Cairo, Knaflic) alongside sources on your business domain
3. **Data management**: Where the data comes from, what it contains, and every pre-processing step: Cleaning <!-- plain-language: everyday decision -->decisions, exclusions, transformations, and why you made each one. For the abcd record, that means the tag and [commit](../Guides/glossary.md#term-commit) from the manifest, and the tables your brief uses. For each of the primer's challenges, it means the <!-- plain-language: everyday decision -->decision you took and the row counts it affected
4. **Methods**: Description and justification of the techniques you use. This includes **justifying the visual form** of your figures. For example, say why a slope chart and not grouped bars
5. **Analysis & presentation of results**: Your findings, with figures that pass the [TRACE checklist](../Guides/glossary.md#term-trace). **Each key figure carries a short [design rationale](../Guides/glossary.md#term-design-rationale) (typically 150-300 words)**. It gives the task the figure serves, the alternatives you considered, and the design <!-- plain-language: everyday decision -->decisions you made. Expect roughly 4-8 key figures
6. **Concluding remarks**: Limitations, managerial implications, and future improvements, all grounded in your results
7. **[AI Use Record](../Guides/glossary.md#term-ai-use-record)**: This section is required. The [assessment interpretation](./interpretation.md) explains what it contains and gives a worked example. The [AI guide](../Guides/ai-guide.md) explains the working habits behind it

**Executive summary:** The question, the headline findings, and the recommendation, written for a **manager** who reads nothing else.


## 5. Your record

Two records matter in this report. The `abcd` record is your data. This section is about the record of your own work.

Your **[Prompt Diary](../Guides/glossary.md#term-prompt-diary)** is that record. Keep it across the whole project. To submit, commit and push your `PromptDiary.md` alongside your notebook. Then upload the report PDF on the Moodle submission page. See the [assessment interpretation](./interpretation.md) and the instructions on the submission page.

The record is evidence **in your favour**. The [assessment interpretation](./interpretation.md) explains what markers read in it and the process indicators they count. If a module tool does not suit you, the same page explains the other ways to show your record. Our rule: No student is disadvantaged by the tools they use.


## 6. The rubric

Your report is marked against the following criteria. Each weight is that criterion's share of your module mark.

<!-- BEGIN GENERATED rubric:individual; edit rubric.yml, then run scripts/project-rubric.py --fix -->

**Introduction and background (10%).** Clarity of problem statement and rationale; project aim and objectives; concepts drawn on; a question the data can answer and a stakeholder would act on.

| Mark | Descriptor |
|:-----|:-----------|
| Missing (0%) | No introduction, or an empty heading. |
| Very Poor (25%) | A topic is named; no aim, no objectives, and no reason the analysis matters. |
| Weak (40%) | The aim or the objectives are stated but not both; background is generic; the reader is not prepared for what follows. |
| Good (55%) | A clear aim, identifiable objectives, and adequate background; the motivation is stated. |
| Very Good (65%) | As Good, plus the objectives are specific and achievable, and the summary maps accurately onto the report's structure. |
| Excellent (75%) | As Very Good, plus the question is sharpened from the starting <!-- plain-language: everyday brief -->brief into one the data can answer and the stakeholder would act on. The background also anticipates the analytical approach. |
| Outstanding (85%) | As Excellent, plus the introduction is one coherent argument: Question, rationale, objectives, and roadmap work together, and every concept introduced is used later. |
| Perfect (100%) | Nothing of substance to improve. |

**Review (10%).** Subject placed in the context of literature; a minimum of five academic references, each checked against its source and used in the argument.

| Mark | Descriptor |
|:-----|:-----------|
| Missing (0%) | No review and no reference list. |
| Very Poor (25%) | One or two sources mentioned in passing; no recognisable referencing style; or a cited source that does not exist. |
| Weak (40%) | Fewer than five credible academic sources; or sources summarised one by one with no connection to the project; or references that cannot be traced. |
| Good (55%) | Five or more academic sources, referenced consistently, each connected to the project's question; the treatment is largely summary. |
| Very Good (65%) | As Good, plus sources are compared and contrasted, and the review states what is already known against the project's objectives. |
| Excellent (75%) | As Very Good, plus the literature is synthesised around themes, and gaps or tensions are named and used to justify the analysis. Every claim attributed to a source is one the source makes. |
| Outstanding (85%) | As Excellent, plus the review positions the project precisely and directly shapes the methods and the interpretation of results. |
| Perfect (100%) | Nothing of substance to improve. |

**Data management (20%).** Data source and licence; description of the data; every pre-processing (cleaning) step documented with its reason and reproducible from the raw data.

| Mark | Descriptor |
|:-----|:-----------|
| Missing (0%) | No dataset, no acquisition or cleaning code, or the section is absent. |
| Very Poor (25%) | Data is present but its origin is undocumented; cleaning is incidental; the notebook cannot locate its own data. |
| Weak (40%) | Provenance or licence is unclear, or cleaning steps are undocumented or not reproducible; data is loaded from paths outside the repository. |
| Good (55%) | Documented provenance; cleaning is adequate for the analysis and runs from repository-local data; the key <!-- plain-language: everyday decision -->decisions are named, though some go unexplained. |
| Very Good (65%) | As Good, plus each <!-- plain-language: everyday decision -->decision on missing values, duplicates, types, and structure is explained, and the analysis-ready dataset is clearly defined. |
| Excellent (75%) | As Very Good, plus data quality is assessed rather than assumed, with explicit checks. The known challenges in the data are handled as recorded <!-- plain-language: everyday decision -->decisions, with the row counts they affected. |
| Outstanding (85%) | As Excellent, plus the pipeline, its documentation, and its limitations could be handed to another <!-- plain-language: everyday Analyst -->analyst and used with confidence, reproducible from the repository alone. |
| Perfect (100%) | Nothing of substance to improve. |

**Methods and/or methodology (10%).** Description and justification of techniques used, including the visual form chosen for each key figure and the alternatives set aside.

| Mark | Descriptor |
|:-----|:-----------|
| Missing (0%) | No methods section and no identifiable analytical approach. |
| Very Poor (25%) | Techniques are applied without being named; the reader cannot tell what was done or why. |
| Weak (40%) | Techniques are named but poorly matched to the question, or described too thinly to be re-applied; the form of the figures is never mentioned. |
| Good (55%) | Appropriate techniques, correctly named and applied, with a <!-- plain-language: everyday brief -->brief justification linking them to the objectives; the chart form of each key figure is stated. |
| Very Good (65%) | As Good, plus parameters and assumptions are stated, and each key figure's form is justified against the task it serves and its audience. |
| Excellent (75%) | As Very Good, plus alternatives, analytical and visual, are acknowledged and set aside for stated reasons. The limitations of the chosen techniques are handled explicitly. |
| Outstanding (85%) | As Excellent, plus technique choice, assumptions, and limitations are integrated into the analysis rather than listed beside it. The account shows the author's judgement overriding a default or a proposed option where the task required it. |
| Perfect (100%) | Nothing of substance to improve. |

**Analysis & presentation of results (20%).** This criterion covers the accuracy and utility of procedures and the documentation of analysis and trade-offs. It covers figures chosen and designed by the author's own judgement, with the reasoning stated and defaults or AI-proposed figures examined rather than accepted. It also covers the discussion of findings.

| Mark | Descriptor |
|:-----|:-----------|
| Missing (0%) | No analysis or results. |
| Very Poor (25%) | Fragments of output with no interpretation; figures unreadable or unconnected to any question. |
| Weak (40%) | Basic descriptive output; library-default figures with no stated reason to exist; claims outrun the analysis. |
| Good (55%) | A sound analysis that answers the stated objectives; figures readable, labelled, and with axes that do not mislead. A reason is given for each key figure; interpretation is accurate though descriptive. |
| Very Good (65%) | As Good, plus figures are chosen to answer specific questions, interpretation distinguishes pattern from noise, and the accuracy and utility of the procedures are assessed. |
| Excellent (75%) | As Very Good, plus each key figure carries a [design rationale](../Guides/glossary.md#term-design-rationale) naming the task, the choices made, and the alternatives rejected. Defaults and proposed figures were changed where judgement required it; uncertainty and caveats are acknowledged. |
| Outstanding (85%) | As Excellent, plus the visual and numerical evidence builds one persuasive argument, alternative explanations are weighed, and the figures are accessible as standard practice. |
| Perfect (100%) | Nothing of substance to improve. |

**Concluding remarks (10%).** Limitations and managerial implications; possible future improvements; remarks must be based on results.

| Mark | Descriptor |
|:-----|:-----------|
| Missing (0%) | No conclusion. |
| Very Poor (25%) | A sentence or two that restates the title; no findings and no limitations. |
| Weak (40%) | Findings restated rather than concluded; limitations missing or token; boilerplate that would fit any project; claims exceed the evidence. |
| Good (55%) | The main findings are summarised accurately against the objectives; limitations, managerial implications, and future improvements are each mentioned and related to the results. |
| Very Good (65%) | As Good, plus the limitations are specific to this analysis and the implications are ones the stakeholder could act on. |
| Excellent (75%) | As Very Good, plus limitations trace to named data and method <!-- plain-language: everyday decision -->decisions, and their consequences for the claims are assessed. The improvements are concrete next steps. |
| Outstanding (85%) | As Excellent, plus the conclusion adds interpretive value. Findings are weighed against the literature and the data's limits. Implications are drawn with precision and appropriate caution, whether or not the news is welcome. |
| Perfect (100%) | Nothing of substance to improve. |

**Professionalism (20%).** Professional conduct and presentation. This covers attribution of AI and other assistance, verifiable references, and a runnable, reproducible submission. It also covers a kept record of how the work was made, and the clarity, organisation, and quality of writing, tables, and figures.

| Mark | Descriptor |
|:-----|:-----------|
| Missing (0%) | No submission standard met; required declarations, identifiers, or the repository absent. |
| Very Poor (25%) | Not runnable; or no record of how the work was made; or no AI attribution; or references that cannot be traced; presentation disordered. |
| Weak (40%) | Runs only with intervention or shows out-of-order execution; attribution or record present but thin; organisation and writing need substantial work. |
| Good (55%) | Runs top to bottom from a fresh start; appropriate [AI Use Record](../Guides/glossary.md#term-ai-use-record); traceable references; an organised, readable notebook and repository. |
| Very Good (65%) | As Good, plus a continuous record that tells how the work was made, consistent style throughout, and figures and tables clear at first reading. |
| Excellent (75%) | As Very Good, plus <!-- plain-language: everyday abcd record -->the record shows AI output being checked and corrected. Accessibility is handled as standard (alt text, colour-safe palettes, legible type). The [AI Use Record](../Guides/glossary.md#term-ai-use-record) names what was overridden and why. |
| Outstanding (85%) | As Excellent, plus the whole submission could be audited from the artefacts alone and handed to a client as it stands. |
| Perfect (100%) | Nothing of substance to improve. |

<!-- END GENERATED rubric -->


### How each criterion is evidenced

This is what markers read as evidence in <!-- gen:values.yml#module.year -->2026-27<!-- /gen -->. The full detail is in the [assessment interpretation](./interpretation.md).

- **Introduction (10%)**: A business question, clearly motivated and sharpened from your brief's starting question. AI can draft prose. The choice of question is yours
- **Review (10%)**: Five or more academic references *that exist and that you have read*. The review may include visualisation-design literature (Tufte, Few, Cairo, Knaflic) where it informs your design <!-- plain-language: everyday decision -->decisions. Verify every reference your Associate suggests
- **Data management (20%)**: The recorded process, not only the clean result. Your notebook documents each cleaning <!-- plain-language: everyday decision -->decision and its justification. Your Prompt Diary shows how you checked AI-proposed steps before you accepted them
- **Methods (10%)**: Justification of techniques includes justification of **visualisation form**: Why this chart type serves this task, and what you rejected
- **Analysis & presentation (20%)**: Accurate and useful procedures, a discussion of findings and trade-offs, *and* visual design quality. Figures pass [TRACE](../Guides/glossary.md#term-trace), and each key figure carries the design rationale described in section 4
- **Concluding remarks (10%)**: Limitations, managerial implications, and improvements grounded in your results, including, where relevant, the limits of what your AI-assisted process could establish
- **Professionalism (20%)**: Polish and organisation, **accessibility** of figures (colour-safe palettes, alt text, legible labels), and **clear AI attribution** in your AI Use Record. A well-organised, continuous Prompt Diary is evidence of organisation


## 7. Timeline and support

- **Week 3**: Assessment briefing. I walk you through this document and the [assessment interpretation](./interpretation.md) in the session. Afterwards, read the [primer](./abcd-record.md) and skim the [briefs](./individual-briefs.md)
- **Week 6**: **Choose and declare your brief** in the workshop, following the rules on the [briefs page](./individual-briefs.md)
- **Weeks 6, 8, and 9**: DataViz (Data Visualisations) design weeks. Practise designing figures. Bring draft figures to workshops
- **Weeks 6, 8, and 9**: **Individual-report support in any workshop**. I take questions during the workshop segments. There is no separate slot
- **Week 7**: Independent practice week. Reread the brief you declared in Week 6 with the [primer](./abcd-record.md) beside it
- **Week 8**: Check that your Prompt Diary is up to date and your AI Use Record is in draft
- **January revision session**: **Polishing your brief** (does your angle answer the stakeholder's question from the table your brief sets?). There is also **feedback on your design rationale** and an individual report Q&A. Bring a key figure and its rationale for structured feedback. I also walk through the AI Use Record
- **After term**: **Submission: <!-- gen:values.yml#assessments.individual.deadline -->Thursday 21 January 2027, 12:00 (UK time)<!-- /gen -->, through <!-- gen:values.yml#links.moodle_course|link:Moodle -->[Moodle](https://moodle.royalholloway.ac.uk/course/view.php?id=32615)<!-- /gen -->** (repository pushed and report PDF uploaded via Moodle)

Start early. The report is due after term, but the support runs during term.


## 8. FAQs

### Can AI write my literature review?
It may draft, summarise, and suggest sources. Check each reference against the paper itself (library search, DOI, publisher page) before it goes in your bibliography. Read what you cite.

### Do I lose marks for using AI a lot?
No. You do not lose marks for using it a little, either. You lose marks for **absent judgement**: Cleaning steps accepted without checking, unexamined default charts, references you never opened, and conclusions your data does not support.

### My columns parse cleanly and have no missing values. Is there anything to clean?
Yes. The record's messiness is in what the rows mean, not in their formatting. The [primer](./abcd-record.md) explains this: State each as a <!-- plain-language: everyday decision -->decision with row counts. If a column is clean, show the checks that established it.

### Is there a self-check I can run before I submit?
Yes. Run `python3 Tools/check.py` in your project folder. It runs the same first-pass automated checks that your marker's tooling runs. [Tools/README.md](../Tools/README.md) explains it.

### Does the design rationale count towards the word count of the report?
The rationales are part of the notebook and part of the assessed work. There is no separate overall word limit for the notebook.

### What if my Prompt Diary misses some sessions?
Say in the AI Use Record what is missing and why. A short written summary of the missing session (what you asked, what you did with the answer) is an acceptable supplement.

### Can my Associate critique my figures before I submit?
Yes. Ask it to run your figure through [TRACE](../Guides/glossary.md#term-trace), argue for an alternative chart form, or play the sceptical client. Then record the exchange.

---

*More questions? Bring them to any workshop in Weeks 6, 8, and 9 or the January revision session. Or see the [primer](./abcd-record.md), the [briefs](./individual-briefs.md), the [module overview](../README.md), the [AI guide](../Guides/ai-guide.md), and the [assessment interpretation](./interpretation.md).*
