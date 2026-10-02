# AI guide: Working with your Associate

Your AI tools (GitHub Copilot, [Stoa](./glossary.md#term-stoa)'s agent, Colab's Gemini in Week 1, or any other assistant you choose) are your **[Associate](./glossary.md#term-associate)**. You are the **[Analyst](./glossary.md#term-analyst)**. The whole module is built on that distinction.


## 1. The charter

This module is **AI-open**. That means:

- **You may use AI for everything.** Every [quest](./glossary.md#term-quest), every notebook, and assessments
- **What is assessed is your judgement and your record.** That means the questions you ask, the outputs you accept or reject and why, the designs you can defend, and the evidence you keep
- **Undocumented work is the risk.** A transcript that shows you directing, questioning, and correcting your Associate is strong evidence of your ability. A submission with no record gives markers nothing to assess

The module has one rule:

> **The Associate writes the code; the Analyst carries the judgement and signs the work.**

When you submit, your name is on the analysis. If a merge silently dropped half the rows, or a chart's axis flatters the data, "the AI wrote that bit" is not a defence. You are responsible for everything you submit, however it was produced.

What AI-open does **not** mean:

- It does not mean the module asks less of you. Learning to direct an Associate well is a skill
- It does not mean anything goes elsewhere; this module has quite a few rules to be aware of
- It does not mean Royal Holloway's academic integrity policy is set aside or can be ignored: You name your AI use in the [AI Use Record](./glossary.md#term-ai-use-record)
- It does not mean you can skip understanding: See [section 8, Learning so it sticks](#8-learning-so-it-sticks)

> ⚠️ **Do this now.** Apply for the [GitHub Student Developer Pack](https://education.github.com/pack) in the Week 1 workshop. It gives verified students the free Copilot Student plan. Verification can take several days. The steps are in [Your workstation, Step 1](./codespaces-start.md#step-1-github-account-and-student-developer-pack). You are done when GitHub emails you that your student status is approved and Copilot shows as active in your account settings.


### If you cannot get Copilot, or run out of chat

Copilot Free needs no verification and covers everything this module asks of you. Its code completions (the suggestions it offers as you type) are sufficient under normal circumstances, but Chat can be the scarce part (roughly fifty messages a month). Keep those for the questions that matter, and use a second tool for long exploratory conversation. Any AI tool you can chat with about code works (e.g., [duck.ai](https://duck.ai/)).

Your university account gives you one for free: **Microsoft Copilot** which is separate from GitHub Copilot (despite the name!). Go to [copilot.microsoft.com](https://copilot.microsoft.com/) and sign in with your university email and password. Choose **Work**, then check for the green shield at the top right (that shield indicates the university's data protection covers what you type). Royal Holloway recommends this tool to students (see [AI tools for students](https://intranet.royalholloway.ac.uk/students/study/generative-ai/ai-tools.aspx)). However, [SpecStory](./glossary.md#term-specstory) and other tools cannot record transcripts in Microsoft Copilot, which makes that part a little tricky. Keep a [Prompt Diary](./glossary.md#term-prompt-diary) for it (see below).

Although you do not need a desktop tool (everything in this module runs in the Codespace, in your browser), you may wish to use a tool you are already familiar with. Again, if SpecStory or similar tools cannot record transcripts from your preferred tool, keep a Prompt Diary instead: Paste the exchanges that mattered into a dated markdown file in your repository. It is less complete than an automatic transcript, but markers will still read it against the same criteria.

Whatever you use, keep <!-- plain-language: everyday abcd record -->the record and declare the tool in your AI Use Record. The quests ask for prompting and judging, never for a named product.


## 2. Meet your Associate

You will find your Associate to be very capable in some directions, reliably wrong in others, and **equally confident in both**.


### What your Associate is good at

- **Drafting.** A first version of almost any code in seconds
- **Explaining.** Any line of code, error message, or concept, at any level, as many times as you like
- **Refactoring.** "Make this shorter", "add error handling", "rename these variables so my teammate can follow it". Reshaping working code is a strength
- **Exploring.** "What are three ways to approach this?" It generates alternatives faster than any human brainstorm

Top tip: If you (think you) have a great idea, tell your associate that a colleague had this idea and that you hate it. Ask it to help you prepare for an argument with your colleague. This gives your associate permission to criticise your work ... and they will!


### Where it is reliably bad, and confidently so

- Remember that your associate predicts text, and doesn't calculate it. For example, it can write `df["revenue"].sum()` correctly and tell you the answer is 47,200 when it is 45,880. Use it to write code to give you an answer (which you can verify), do not trust the answer itself
- **Current facts.** Its knowledge stops at a fixed date, which varies by model (its training cut-off)
- **Your data.** For example, it may happily write code for a column called `customer_id` when in your DataFrame, that column is called `CustID`; or it assumes your dates are stored as dates when they are stored as text (it tends to assume a lot!)
- **Admitting uncertainty.** A correct answer and an invented one sound the same

Here are two examples of the kind you meet in every [Debrief](./glossary.md#term-debrief)'s [AI failure gallery](./glossary.md#term-ai-failure-gallery):

1. *The plausible average.* Asked for average revenue per region, the Associate computes the mean of each store's mean instead of total revenue over total transactions. The code runs, the chart looks sensible, but the number is wrong
2. *The hallucinated argument.* Asked to make a legend transparent, it invents `plt.legend(transparency=0.5)`. No such argument exists (the real one is `framealpha`). Sometimes this errors, but sometimes it runs and does nothing (which is worse)

Although your Associate is fast and tireless, it does need a manager. Seriously, it does. And that manager is you.

The module repository carries a [briefing for the Associate](../AGENTS.md). This briefing gives the tool you use the module's context, file layout, the fact that the client memos are fiction, etc.

It also gives four rules for the tool:

- It does not state a cell's output before you write your prediction
- It explains before it fixes
- It hands [Bronze](./glossary.md#term-bronze) drafts back for you to verify
- It never writes your Debrief answers

However, Stoa's agent, Colab's Gemini, and Microsoft Copilot do not read repository files. With any of them, paste the file's contents into the chat. To check that a tool has loaded it, ask what the module's rule for a prediction cell is.


## 3. What you can do with your Associate

Everything you do in this module with AI is one of four things, each belonging to a quest stage (see [quest](./glossary.md#term-quest) in the glossary).


### GENERATE-JUDGE: The Associate drafts; you accept or reject, with reasons

Most Build work takes this shape and the skill is in the judging of it.

> **You:** "Write a pandas snippet that flags customers with no purchase in the last 90 days. The DataFrame is `orders` with columns `customer_id`, `order_date` (datetime), `amount`. Give me two approaches and say which you'd recommend and why."
>
> **Then you judge:** Does approach one handle customers with *no orders at all*, or only lapsed ones? Is "the last 90 days" measured from today or from the latest order in the data? You accept, reject, or send it back, and you say why.

Good [GENERATE-JUDGE](./glossary.md#term-generate-judge) work means you can say *why* you kept what you kept. "It ran" is not enough.


### PREDICT-RUN: You predict; the machine reveals

This is the fastest way to find out whether you understand a piece of code.

> Before running `df.groupby("region")["sales"].mean().round(1)`, write one line: *"A table of about four rows, one per region, average sales to one decimal place."* Then run it. A Series instead of a DataFrame? Six regions because two are capitalised inconsistently? Every surprise is a gap between what you expected and what the code does.

Although predicting first can feel slower, it is clearly the highest-value habit in this guide.


### BUG-HUNT: The Associate is the suspect; you are the auditor

This is a [Red Flag](./glossary.md#term-red-flags) where AI-generated code fails in typical ways, such as, e.g., wrong merge keys, silent type changes, off-by-one date filters, averages of averages, truncated axes, etc. The code runs, but the answer is wrong.

> Your Associate merged `orders` with `customers` and the client's revenue total looks high. You check: `len(orders)` is 8,412 before the merge and 9,067 after it. Rows were *created*: A merge on a duplicated key counts each customer with two addresses on file twice. The code ran without complaint. The row count caught it.

You can also point the Associate at itself: *"Review this code for bugs. Pay particular attention to the merge: Could it duplicate rows?"* Given a specific suspicion, this typically helps. When you ask vaguely "is this right?", it usually says yes (it's the easiest answer!)


### TEACH-BACK: The Associate examines or plays student; you explain

This is a good test of learning. Two variants:

> **AI as examiner:** "Set me three questions on pandas `groupby`, from easy to hard. I'll answer without help; then mark my answers strictly."
>
> **AI as student:** "I'm going to explain what `pivot_table` does and when I'd use it over `groupby`. Play a sceptical junior colleague: Interrupt when I'm vague."

If you cannot explain it away, you're not done (yet).


## 4. Prompting for analytics

Your Associate has never seen your data, so every good analytics prompt carries your data into the conversation. Three principles:

1. **Context.** Give the `schema` (i.e., the column names and their types) and a sample row. This removes the largest class of AI errors: Wrong column names, wrong types, and wrong assumptions about formats
2. **Constraints.** State the business question and the boundaries: Which library, what the output should be, what must not change, etc.
3. **Iteration.** Treat the first response as a **draft**. Send it back with "shorter", "handle missing values", or "now do it without a loop". Two or three rounds are typically (much) better than one long prompt

Here are some useful patterns (adapt the words, but keep the structure):

1. **The schema anchor**: Start any data task with the schema and a sample row.
   > "I have a DataFrame `sales` with columns: `date` (string, 'DD/MM/YYYY'), `store` (string), `units` (int), `revenue` (float, GBP). Sample row: `'03/11/2026', 'Egham', 42, 315.50`. First task: Convert `date` to datetime."

   Told the format is DD/MM/YYYY, the Associate writes `format="%d/%m/%Y"` instead of guessing and reading 03/11 as March

2. **The business question first**: Lead with why, not just what.
   > "Business question: The client thinks weekend trading isn't worth the staffing cost. Using `sales`, compare weekday vs weekend revenue per trading day. What would you compute, and what would you caution the client about?"

   Given the purpose, it can flag things you did not ask about, such as comparing per day rather than in total

3. **The alternatives ask**: Never settle for one option on anything that matters.
   > "Give me three ways to handle the missing values in `revenue`, with the trade-offs of each for a monthly revenue report. Recommend one and justify it."

   You cannot judge when there is only one option

4. **The assumptions flush**: Make the invisible visible.
   > "Before writing any code: List every assumption you're making about my data and my goal. I'll confirm or correct each one."

   Typical answers: "I assume `customer_id` uniquely identifies a customer", "I assume revenue is net of refunds". Half will be wrong. Find out now

5. **The constraint retrofit**: Adapt the output to a constraint the Associate was not told. This is the Silver-tier move
   > "Good, but this report will be re-run monthly by a colleague who doesn't know Python. Restructure it as one function taking a file path, with clear error messages if the columns aren't what we expect."

6. **The explain-back check**: Use it before accepting anything that matters.
   > "Walk me through this line by line. For each step, tell me what could go wrong with messy real-world data."

   If the explanation does not match what you asked for, neither does the code

Every prompt on this page, and every other prompt in the materials, is in the [prompt library](./prompts.md). Each entry has a line on what a good answer contains. Module terms are defined in the [glossary](./glossary.md). For deeper technique, read Anthropic's [prompt engineering guide](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview), which applies to most tools. Ethan Mollick's [One Useful Thing](https://www.oneusefulthing.org) is a running commentary on working with AI (registration is optional!).


## 5. Verification

Five recommended habits:

1. **Never accept unrun code.** Code you have not run is a claim, not a result
2. **Check shapes and count your rows.** After any filter, merge, groupby, or dropna, check `df.shape`, or compare `len(before)` with `len(after)`. Rows lost or gained that you did not expect are the most common silent failure in data analysis
3. **Recompute one number by hand.** Pick one value in any summary table and check it independently. Filter the raw rows for one region in one month, add them up, and compare. This is how you honestly tick a quest's [Definition of Done](./glossary.md#term-definition-of-done) (the self-check list in every quest Briefing)
4. **The three explanations trick.** Take any output you are about to rely on. Ask your Associate to explain it three ways: To a programmer, to a manager, and to a ten-year-old (or, alternatively, to a [golden retriever](https://youtu.be/LTDS6SHwA6w)). Invented answers rarely survive that, and should the versions disagree about what the code does, investigate
5. **Eyeball the extremes.** Look at `df.describe()`, the min and max, and the top five and bottom five rows of anything sorted. A negative age, a £2 million coffee order, or a date in 1970 is where a broken pipeline shows itself

Every Debrief notebook ends with an **AI failure gallery**: Realistic ways AI gets that week's material wrong, and what would have told you. Treat the <!-- plain-language: everyday Gallery -->galleries as your verification training set.


## 6. Your record is your evidence

Suppose a transcript shows you giving the Associate the schema, rejecting its first draft for double-counting, and directing the fix. That transcript is dated evidence of your judgement. What you keep throughout is the **AI Use Record**: An honest account of what you asked, what you accepted or rejected, and why. It does not depend on which tool you use. Three records feed it:

- **Prompt Diary** (Week 1 only, in Colab): A Prompt Diary cell at the end of Quest 01. Paste your *best* exchange (the prompt that worked, and why) and your *worst* (where the Associate misled you, and how you caught it)
- **SpecStory transcripts** (Week 2 onwards, in your Codespace): Files in `.specstory/history/` inside your project, written automatically by the pre-installed SpecStory extension. Confirm files are appearing there ([Your workstation, Step 5](./codespaces-start.md#step-5-check-your-record-specstory)) and <!-- plain-language: everyday commit -->commit them with your work
- **[QuestLog.md](./glossary.md#term-questlog)** (all weeks): Your personal learning journal, from the template issued in Week 1. Add a dated entry per quest with the [badge](./glossary.md#term-badge) you claimed and your Debrief answers

SpecStory is a convenience not a requirement. Any consistent, honest way of keeping the AI Use Record meets the same standard: SpecStory, a hand-kept log, or whatever suits your setup. (For group work from Week 4, your Stoa room transcript is the team's equivalent. See the [Stoa workflow guide](./stoa-workflow.md).)

While markers will look at your transcripts (see the assessment interpretation), those indicators are supporting evidence only, and no mark is computed from them. (The interpretation arrives with Week 3.)

Remember: A transcript full of rejected AI output and corrections is a *good* transcript. <!-- plain-language: everyday abcd record -->The record to worry about is the empty one.


## 7. The AI Use Record

Both submissions (the group project and the individual report) include an **AI Use Record**. It is a short declaration plus a summary of how AI was involved. It is half a page to a page long in total. It has four parts:

1. **Tools used.** Name each and where you used it
2. **What each was used for.** Be honest and specific
3. **Notable rejections and corrections.** Give two or three moments where you overruled the Associate, with your reason. This part shows the judgement being assessed most directly
4. **One paragraph of reflection.** Say where the Associate helped, where it slowed or misled you, and what you would do differently

Week 7 rehearses part 4: The [REFLECT prompt](./prompts.md#reflect-on-your-prompts) reads your own prompts back to you.

Avoid two failure modes: The empty gesture ("I used ChatGPT for some things") and the exhaustive log (all 214 prompts, pasted). Be specific, honest, and <!-- plain-language: everyday brief -->brief. The transcripts hold the detail. The full specification is in the assessment interpretation, section "The AI Use Record: The canonical specification".


## 8. Learning so it sticks

Working this way carries one risk. If the Associate does all the thinking, you learn nothing while feeling productive. Watching fluent code appear feels like understanding until ... you face a blank cell alone. The quest stages were designed to guard against this (see [quest](./glossary.md#term-quest) in the glossary). Remember: The individual report asks you to direct an Associate on your own analysis of [the record](./glossary.md#term-abcd-record), and that cannot be delegated to the Associate.

Three practices beyond the quests:

- **Turn the Associate off on purpose, briefly and often.** Before asking for anything, spend sixty seconds sketching your own approach, even a bare "filter, then group, then sort" in a comment. Then compare the Associate's answer with your sketch. You can pause Copilot's inline suggestions from the Copilot menu in VS Code's status bar (see the [GitHub Copilot documentation](https://docs.github.com/en/copilot))
- **Close the book test.** Once a week, take one technique you "learned" and use it in a fresh empty notebook, from memory, with no AI. Whatever you cannot reproduce, you have not learned (yet)
- **Ask "explain" before "fix".** When something breaks, ask "explain what this error means and why my code triggered it; don't fix it yet" before you ask for a fix
