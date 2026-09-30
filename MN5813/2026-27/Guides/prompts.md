# Prompt library

*Every prompt the module's materials ask you to try, on one page.*

> ⚠️ **Draft:** This page is a draft. It will be confirmed in Week 3.

This page collects the prompts that appear across <!-- gen:values.yml#module.code -->MN5813<!-- /gen -->. It holds one template prompt for each of the four moves and the six prompting patterns. It also holds the three [Debrief](./glossary.md#term-debrief) prompts and every **[AI Lens](./glossary.md#term-ai-lens)** prompt, week by week. Fill in anything in angle brackets (your code, your figure, and your questions). Then paste the whole prompt into your [Associate](./glossary.md#term-associate). Do not reword it. Where a note in italics follows the prompt, judge the reply against it. The note says what a good answer contains. The moves and the habits of checking are in the [AI Guide](./ai-guide.md). The glossary explains the [Debrief](./glossary.md#term-debrief) stage.

## The four moves

[Section 3 of the AI Guide](./ai-guide.md) describes the four moves. This page gives one template prompt for each.

### GENERATE-JUDGE

The Associate drafts. You accept or reject, with reasons.

```text
Write a pandas snippet that flags customers with no purchase in the last 90 days. The DataFrame is `orders` with columns `customer_id`, `order_date` (datetime), `amount`. Give me two approaches and say which you'd recommend and why.
```

### PREDICT-RUN

Write one line saying what the code will produce, then run it. The Associate checks your prediction without giving away the output.

```text
Here is a piece of code and my one-line prediction of what it produces. Do not tell me the output. Say whether my prediction is right, and if it is wrong, what I have misunderstood.

Code:
<paste the code here>

My prediction:
<your one-line prediction, for example: a table of about four rows, one per region, average sales to one decimal place>
```

### BUG-HUNT

The Associate is the suspect. You are the auditor. Send it the code with one specific suspicion. If you ask it vaguely whether the code is right, it usually says yes.

```text
Review this code for bugs. Pay particular attention to the merge: could it duplicate rows?
```

### TEACH-BACK

The Associate sets the questions or plays the student. You explain.

```text
Set me three questions on pandas `groupby`, from easy to hard. I'll answer without help; then mark my answers strictly.
```

## Six prompting patterns

Your Associate has never seen your data, so each prompt describes your data. The six patterns are in [section 4 of the AI Guide](./ai-guide.md). Adapt the words and keep the structure.

### The schema anchor

Start any data task with the schema (the column names and their types) and a sample row.

```text
I have a DataFrame `sales` with columns: `date` (string, 'DD/MM/YYYY'), `store` (string), `units` (int), `revenue` (float, GBP). Sample row: `'03/11/2026', 'Egham', 42, 315.50`. First task: convert `date` to datetime.
```

### The business question first

Lead with the business question, not only the task.

```text
Business question: the client thinks weekend trading isn't worth the staffing cost. Using `sales`, compare weekday vs weekend revenue per trading day. What would you compute, and what would you caution the client about?
```

### The alternatives ask

Ask for more than one option on anything that matters.

```text
Give me three ways to handle the missing values in `revenue`, with the trade-offs of each for a monthly revenue report. Recommend one and justify it.
```

### The assumptions flush

Make the Associate list its assumptions before it writes any code.

```text
Before writing any code: list every assumption you're making about my data and my goal. I'll confirm or correct each one.
```

### The constraint retrofit

Give the Associate a constraint it was not told, and make it adapt the output. This is the Silver-tier move.

```text
Good, but this report will be re-run monthly by a colleague who doesn't know Python. Restructure it as one function taking a file path, with clear error messages if the columns aren't what we expect.
```

### The explain-back check

Before you accept anything that matters, make the Associate explain it. If the explanation does not match what you asked for, neither does the code.

```text
Walk me through this line by line. For each step, tell me what could go wrong with messy real-world data.
```

## The Debrief prompts

Every [quest](./glossary.md#term-quest)'s Stage 5, the Debrief, asks the same three [TEACH-BACK](./glossary.md#term-teach-back) questions. Answer them in the quest, then copy your answers into your `QuestLog.md` as a dated entry with the [badge](./glossary.md#term-badge) you are claiming.

**1. Client explanation**

```text
Explain this week's key technique to the client in three sentences, no jargon.
```

**2. Associate audit**

```text
Where was your Associate wrong, misleading, or unhelpful this week? Paste the exchange.
```

**3. Quiz me**

```text
Ask your Associate to set you three questions on this week's material. Paste the quiz and answer it without AI help.
```

Each quest's Quiz me also suggests a prompt naming that week's topics. Its shape is always the same. It asks for three short questions (easy, medium, hard) on the week's topics, and tells the Associate not to show answers until you have tried.

## Reflect on your prompts

In Week 7, run this once on your own record. Nothing from it is marked.

**REFLECT: read your own prompting**: Open one transcript from `.specstory/history/`, or your [Prompt Diary](./glossary.md#term-prompt-diary), then paste this with the file open.

```text
Read only the file I have open. It is my own record of prompts to an AI assistant: A transcript or my Prompt Diary.
If the file is empty, or is not a record of my prompts, say so and stop.
Answer in exactly three parts, quoting my exact words.
1. Three patterns: Name three patterns in how I prompt. Quote one of my prompts for each.
2. One prompt that worked: Quote it, then say why it worked.
3. Two things to try: Give two changes for next time, each written as a prompt I could paste.
Give no general advice that would fit anyone.
```

*A good answer quotes your own prompts back to you and could not have been written without reading your file. An answer that could fit anyone is not one.*

## AI Lens prompts by week

This section lists every **AI Lens** callout in the notebooks, in module order. Each entry is named after the notebook section it sits in. The callout in the notebook says what to do with the reply.

### [Week 1: Demonstration](../Week/01/Demonstration.ipynb)

**f-strings: readable output**: Ask for a business analogy, then check it against the code you ran.

```text
Explain what an f-string is in Python using a business analogy, as if I write reports for a living.
```

*A good answer describes an f-string as a report template whose named slots are filled with live values when it runs. Nothing in the answer contradicts what the notebook's cell printed.*

**Reading an error message, top to bottom**: Paste an error you caused on purpose and get two fixes to choose between.

```text
<paste the whole error message here>

Explain this error in plain English, and give me two different ways to fix it.
```

*A good answer says in plain words that Python was asked to add a number to a piece of text. It offers two fixes that are genuinely different, one of which is `float()`.*

### Week 2: Exercises

**Cells run in the order you run them**: Ask for a plain-English explanation of an error.

```text
<paste the NameError here>

Explain this error in plain English. What was Python trying to tell me?
```

*A good answer says Python met the name `mystery_number` before any cell had given it a value. The answer points at the order the cells were run in rather than at a broken notebook.*

**Meet your Associate: GitHub Copilot**: Ask what a kernel restart does, then compare the reply with what the notebook says.

```text
What does restarting the kernel do in a Jupyter notebook, and what do I lose when I do it?
```

*A good answer says a restart forgets every variable, import, and function while the notebook's text and old outputs stay on screen. The answer adds that nothing exists again until you re-run the cells.*

### Week 2: Demonstration

**Data types, and why you check them**: Ask for three explanations of one cell, then decide which you trust.

```text
<paste the cell's code here>

Explain this code three different ways: to a programmer, to a manager, and to a 10-year-old.
```

*A good answer says the same thing all three times. Each explanation says that a variable is a label that can be moved to a new value, even one of a different type. The version you trust most is the one you can check against the printed output.*

**Functions: code you can reuse** ([GENERATE-JUDGE](./glossary.md#term-generate-judge)): Ask for two versions of a loyalty-tier function, then check both at the tier cut-offs (£60, £30, £10).

```text
Write a Python function that maps a monthly spend to a loyalty tier: Gold from £60, Silver from £30, Bronze from £10, otherwise 'New customer'. Give me two different implementations and say which you'd recommend for a beginner-level codebase and why.
```

*A good answer gives two implementations that agree at every boundary (£60 is <!-- plain-language: everyday Gold -->Gold, £9.99 is 'New customer'). The answer recommends the one a beginner can read. Two versions that disagree at a boundary are the bug you were meant to catch.*

**More loop patterns** ([PREDICT-RUN](./glossary.md#term-predict-run)): Have the Associate check your prediction of a `range()` loop without telling you the output.

```text
Here is a Python cell and what I predicted it would print before I ran it. Do not just tell me the output: say whether my prediction is right, and if it is wrong, explain the rule about where range() stops that I have misunderstood.

Code:
<paste the cell's code here>

My prediction:
<your prediction, first and last number included>
```

*A good answer is your own prediction matching the printed output, first and last number included. Where it does not, the Associate's explanation should say that `range(1, 6)` stops before 6.*

**String methods**: Test whether the Associate invents string methods.

```text
Does Python have a string method called `.reverse()`? What about `.capitalise()`?
```

*A good answer says neither exists (`.reverse()` belongs to lists, not strings, and the string method is spelled `.capitalize()`). Your spare cell agrees with it.*

**Dictionaries: labelled data** (GENERATE-JUDGE): Try the vague prompt, then the prompt that carries the schema and a sample row.

```text
How do I total sales in Python?
```

```text
I have a Python list called `transactions` where each item is a dict like `{"item": "latte", "cups": 2, "price": 3.60}`. Its `price` is per cup. Write a beginner-level loop that totals revenue.
```

*A good answer to the second prompt is a loop that multiplies `cups` by `price` for every transaction. The loop adds each result to a running total and uses your real key names. The first prompt's reply shows you what guessing looks like.*

**File handling: write it, read it back**: Ask what `with open()` gives you. Predict the answer to the second question before you read the reply.

```text
In Python, what does `with open(...)` do that a bare `open(...)` doesn't, and what can go wrong without it?
```

```text
What happens to the file's old contents when I open it in `'w'` mode?
```

*A good answer says `with` closes the file for you even when an error interrupts the block. It also says that opening in `'w'` mode empties the file the moment it opens, which is what you should have predicted.*

### Week 2b: Introduction (optional, for your own time)

**Strategy 3: run fragments**: Ask for a walk-through of the data flow, then check it with fragments you run yourself.

```text
<paste the draft here>

Walk me through the data flow: what is the type and shape of each variable?
```

*A good answer names every variable in the draft with its type and shape. The draft has a list of dicts, a dict of names to totals, and a list of pairs. Each claim survives a fragment you run yourself.*

### Week 2b: Demonstration (optional, for your own time)

**When a comprehension is too clever**: Ask for a loop rewrite of an unreadable one-liner, then three explanations of it.

```text
<paste the one-liner here>

Rewrite this as a plain loop with intermediate variables and one comment per step.
```

```text
<paste the one-liner here>

Explain this code three different ways: to a programmer, to a manager, and to a 10-year-old.
```

*A good answer to the first prompt is a loop that prints the same `by_day` dictionary as the one-liner, with one idea per line. The version to ship is the one whose explanation you would trust in front of a client.*

**`lambda` and `sorted(key=...)`**: Ask for the week's quietest day by revenue. Predict it before you run the draft.

```text
I have a Python list called `sales` where each item is a dict with keys `day`, `cups`, and `price_per_cup`, and a list `DAYS` of the six day names. Write one expression using min() with a key= argument that returns the day with the lowest total revenue, where a sale's revenue is cups times price_per_cup.
```

*A good answer uses `min(DAYS, key=...)` with a key that totals `cups * price_per_cup` over each day's sales. It names the same day as the bottom of the one-liner's output.*

**The anti-pattern your Associate loves**: Ask why a bare `except` is dangerous, then make the Associate audit its own draft for one.

```text
Why is a bare `except` dangerous? Show me a case where it hides a bug that a specific `except KeyError` would have exposed.
```

```text
Audit your last draft for the pattern you just described: any bare `except`, or any `except` that silently swallows an error. For each one, name the specific exception it should catch instead and rewrite it.
```

*A good answer shows a bare `except` turning a misspelled key into a quiet wrong result. `except KeyError` would have crashed and pointed at the typo instead. The audit either finds the pattern in its draft or shows there was none to find.*

**How to read a class**: Ask for `self` explained three ways.

```text
Explain what `self` means in a Python class three ways: to a Java programmer, to an Excel user, and to a 10-year-old.
```

*A good answer says the same thing in all three voices: `self` is this particular object, Priya's card and not the idea of a card. Your own prediction for `priya.add_stamps(25)` should match what the fragment prints.*

**Stretch 4: classes that cooperate**: Ask for a class edit, then check it for invented attributes.

```text
<paste the LoyaltyCard class here>

Add a `spend_per_stamp` idea of your own to this class. Show the whole class after your change, and say what you added and why.
```

*A good answer changes `__init__` only if the new idea needs new data, and uses only attributes the class actually sets. It explains the addition in a sentence you can check against the code.*

### Week 4: Demonstration

**Creating and manipulating Series**: Ask how a Series differs from a list and a dictionary, once for a programmer and once for a manager.

```text
Explain how a pandas Series differs from a Python list and from a dictionary, once for a programmer, once for a manager who has only ever used Excel.
```

*A good answer tells the programmer a Series is a single-typed column with an index and vectorised maths. It tells the manager it is one labelled column of a spreadsheet. The manager's version is the one to test aloud.*

**Selecting data**: Ask for a DataFrame where `.loc` and `.iloc` disagree.

```text
Construct a small DataFrame where `df.loc[1]` and `df.iloc[1]` return DIFFERENT rows, and explain why.
```

*A good answer constructs a DataFrame whose index labels are not the default 0, 1, and 2. It shows the two calls returning different rows and says why: `.loc` looks up the label, `.iloc` counts the position.*

**Filtering rows**: Ask for three ways to write one filter, and their trade-offs.

```text
<paste the code that builds df here>

Show me three different ways to filter this DataFrame for people aged 30+ in the UK (boolean indexing, `.query()`, and `.loc` with a mask) and the trade-offs of each.
```

*A good answer gives three filters that return the same rows as the notebook's own filter. Its trade-offs mention readability, `.query()` sparing you the repeated `df[...]`, and `.loc` letting you pick columns in the same call.*

**Applying functions to columns**: Ask which `.apply()` calls could be replaced, and when `.apply()` is the right tool.

```text
<paste the cell's code here>

Which of these `.apply()` calls could be replaced by a vectorised operation? Rewrite them, and tell me when `.apply()` is genuinely the right tool.
```

*A good answer rewrites `df["Age"].apply(lambda x: x - 5)` as `df["Age"] - 5` and `df["Name"].apply(len)` as `df["Name"].str.len()`, and keeps `.apply()` for logic column maths cannot express. A reply that says `.apply()` is fine as it stands has missed the point.*

**Handling missing data**: Ask for both sides of drop-or-repair, and what decides it.

```text
For a sales ledger where 4% of revenue values are missing, argue for dropping the rows, then argue for repairing them, then tell me what you would need to know to choose.
```

*A good answer makes both cases honestly. It then names what decides it: Whether the gaps are random or concentrated in one store or month, and what the report is for.*

**Grouping and aggregating**: Explain split-apply-combine in your own words and have the Associate grade it. Then ask the Associate for its own three-sentence client version.

```text
I am going to explain split-apply-combine in my own words. Grade my explanation out of 10, and point out anything wrong or missing.

<your explanation of split-apply-combine>
```

```text
Explain split-apply-combine to a client in three sentences, no jargon.
```

*A good answer from you names all three steps. The steps are: Split the rows into groups, apply a calculation to each group, combine the results into one table. The Associate's client version only beats yours if it says the same in plainer words.*

**Merging and joining DataFrames**: Ask which `how=` to use when some keys are missing.

```text
I have a sales table and a product-details table, and some products in the sales table are missing from the details table. Which `how=` should I use to add product details to sales, what happens to sales rows for the missing products, and how do I count how many I affected?
```

*A good answer says `how="left"` and warns that the default `how="inner"` silently drops the sales rows for the missing products. It counts the affected rows by checking for `NaN` in the detail columns after the merge, or by comparing row counts before and after.*

### Week 5: Demonstration

**`melt()`: wide to long**: Describe the shape you want, wide to long and then long to wide, without naming a pandas function.

```text
I have a DataFrame with columns centre, line, and one column per month. I want one row per centre per line per month, with columns centre, line, month, sales.
```

```text
I have a DataFrame with columns centre, line, month, sales: one row per centre per line per month. I want one row per centre per line, with one column per month holding that month's sales.
```

*A good answer reaches for `melt()` for the first shape and a pivot for the second without being told either verb. The code it writes runs on the notebook's `report` and `tidy_report`.*

**The silent default**: Try the vague pivot prompt, then the full shape sentence.

```text
pivot the daily data so I can see sales by date and centre
```

```text
Pivot the daily data so I can see sales by date and centre: rows = dates, columns = centres, cells = the sum of the three lines' sales.
```

*A good answer to the vague prompt asks you what the cells should contain. A draft that silently takes the mean is the silent default in action. The full shape sentence should produce `aggfunc="sum"` without any further hint.*

**What `unstack()` does with holes**: Make the Associate describe the index and the `NaN`.

```text
<paste the reshape code and its output here>

What is the index of this object right now, and what does a NaN in it mean in business terms?
```

*A good answer names the index and the columns by level. It says what the `NaN` stands for in business terms (a centre-and-line combination that was never observed, not a zero take). It does not call it 'missing data'.*

**Window functions: trend from noise**: Ask what goes wrong with a plain `shift(7)` compared with a grouped one. Then ask for a counter-example that shows it.

```text
<paste the cell's code here>

Explain the difference between `df['sales'].shift(7)` and `df.groupby('centre')['sales'].shift(7)` on this data. What exactly goes wrong with the first?
```

```text
Construct a tiny DataFrame with two centres and at least eight days each, sorted by centre then date, and show `shift(7)` with and without `groupby('centre')` side by side. Point at the rows where the plain shift hands one centre's values to the other.
```

*A good answer says the plain shift hands the last rows of one centre to the first rows of the next. The grouped shift stays inside each centre. The counter-example shows the leaked rows rather than asserting them.*

### Week 6: Introduction

**Five analytical tasks, five chart families**: Ask for the task and chart family for your own business questions.

```text
Here are three business questions from my group project. For each one: Which of the five analytical tasks is this (comparison, distribution, relationship, change over time, part-to-whole), and which chart family follows?

1. <your first business question>
2. <your second business question>
3. <your third business question>
```

*A good answer names one task per question and the chart family the table gives for it, with a reason. Where it picks a family the table does not, one of you is wrong.*

### Week 6: Demonstration

**Pair 1, comparison: bar chart**: Ask for a critique of the draft bar chart against Task, Reduce, Accessible, Context.

```text
<paste the draft cell's code here>

Critique this chart against the checklist Task, Reduce, Accessible, Context. What would you change?
```

*A good answer names the meaningless colours, the redundant legend, the alphabetical order, the missing units and source, and a title that tells nobody anything. That is the list the notebook's revision fixes.*

**Pair 3, relationship: scatter plot**: Ask for three rival explanations for a correlation.

```text
Give me three reasons this correlation between marketing spend and weekly revenue might exist even if the marketing does nothing.
```

*A good answer gives three distinct mechanisms: Seasonality, a common cause such as a product launch, or spend being set from expected revenue. You could turn each one into one caveat sentence in a memo.*

**Where this goes next**: Run [TRACE](./glossary.md#term-trace) on any revision before the quest.

```text
<paste the revision's code here>

Run this through TRACE: Task, Reduce, Accessible, Context, Explain. Where does it still fall short?
```

*A good answer names the letter the figure is weakest on and says specifically what would fix it. A reply that passes every letter has not looked hard enough.*

### Week 7: Demonstration

**Part 1: the audit**: Ask for hypotheses to test in your data audit. Do not record the reply as findings in your log.

```text
What data-quality problems would you expect in a fire brigade's incident and mobilisation records, where one table has a row per 999 call, the other a row per engine sent, and the two join on an incident number?
```

*A good answer lists plausible suspects. Some are engines whose incident is missing from the other table, and arrival times empty where no engine arrived. Others are timestamps stored as text in more than one format, place names cased differently across the two tables, and repeated engine rows. Your audit is what decides which of them are real.*

**Part 2: <!-- plain-language: everyday decision -->decisions, then cleaning**: Ask the room's Associate for a neutral summary of a team disagreement.

```text
Summarise our disagreement about the empty attendance times. State each position and its strongest argument fairly, then list what evidence from our own audit would settle it.
```

*A good answer states both positions fairly enough that each side would sign its own summary. It names evidence from your own audit instead of picking a winner. The evidence covers how many times are blank, what `NumPumpsAttending` says on those rows, and which of your questions the column feeds.*

### Week 8: Demonstration

**The exploratory draft**: Run TRACE on the Associate's first draft.

```text
<paste the cell's code here>

Run this figure through TRACE (Task, Reduce, Accessible, Context, Explain). Where does it fail?
```

*A good answer fails the figure on most letters and matches the notebook's own critique. It names six competing colours, a legend on the data, and the tinted panel and full grid. It also names an axis labelled `value` and a title that names variables instead of the finding.*

**Step 6: emphasis last**: Give the Associate the six declutter steps, one at a time and then all at once.

```text
<paste the original draft chart code here>

I am going to give you six changes to this chart, one at a time. Apply only the change I name, show the full revised code, and change nothing else. Step 1: Remove the box around the plot; keep only the bottom and left spines.
```

```text
<paste the original draft chart code here>

Apply all six of these changes to this chart and show the full revised code:
1. Remove the box around the plot; keep only the bottom and left spines.
2. Delete the grid, then add back only a few faint horizontal lines.
3. White background: lose the tinted panel.
4. Delete the legend box and name each line at its right-hand end instead.
5. Plot in £k, not raw pounds; label the axis with what it measures and its units; round ticks.
6. Push the five context branches into grey; pull Egham into one strong colour.
```

*A good answer by either route looks like the notebook's `pair(6)` right-hand panel. The step-by-step transcript is the better one to cite if it shows you catching a change you did not ask for.*

**The accessibility pass**: Ask for alt text, the sentence a screen reader reads in place of the figure. Mark it against the formula of type, variables, and takeaway.

```text
<paste the figure's code here>

Draft one-sentence alt text for this figure.
```

*A good answer names the chart type, the variables and their units, and the takeaway, as the notebook's alt text does. The takeaway is Egham roughly doubling while the other five branches stay flat. A draft that stops at the furniture is the one you fix.*

**Interlude: interactive charts with hvPlot**: Ask what a printed board pack loses, first what stops working and then what you stop controlling.

```text
<paste the hvPlot cell's code here>

The CFO gets this figure in a printed board pack. What breaks if I ship the hvPlot version?
```

```text
Beyond hover, zoom, and widgets dying on paper: if I ship the hvPlot version of this figure in a printed board pack, what do I lose control of?
```

*A good answer to the first lists hover, zoom, and widgets dying on paper. A good answer to the second says you surrender the reader's first impression, the framing, and the emphasis. That is the real reason boardroom figures are static.*

### Week 9: Demonstration

**Exhibit A: the candidate figure**: Run TRACE before you read the crit.

```text
<paste Exhibit A's code here>

Run this figure through TRACE (Task, Reduce, Accessible, Context, Explain). Where does it fail?
```

*A good answer fails Exhibit A on the letters the critics' scorecard fails it on. The scorecard's failures are the tangle of lines, the legend, the axis labelled `value`, and a title with no finding. Anything it passes that the scorecard fails, check against the chart yourself.*

**Consistent styling across a report**: Ask for every inconsistency between two candidate figures.

```text
<paste the code of both candidate figures here>

Do these two figures look like they come from the same report? List every inconsistency: fonts, palette, source-line format, title style, margins.
```

*A good answer is a specific list (font, palette, source-line wording, title position, and margins). You can confirm or reject each item against the exported figures. An inconsistency you cannot find is one it invented.*

### Week 10: Introduction

**How to prepare for the presentation's questions**: Ask for the sceptical marker's hardest questions on your [`DECISION:` entries](./glossary.md#term-decision-entry).

```text
Here are three DECISION: entries from our project's room log. Play the sceptical marker at our group presentation: ask us the three hardest 'walk me through this' questions these entries invite.

<paste your three DECISION: entries here>
```

*A good answer asks about evidence, not syntax (the row counts before and after, the alternative you rejected, and who proposed the change). The rehearsal counts only if every team member can answer one of the three.*

### January revision session: Introduction

**The design-rationale surgery**: Ask for an attack on your figure's chart form, then accept or rebut it on <!-- plain-language: everyday abcd record -->the record.

```text
<paste your figure's code here>

Run this figure against TRACE and argue for a different chart form as if you were a sceptical client.
```

*A good answer makes a real case for a different chart form. The case is tied to the task the figure serves and to a TRACE letter it fails. The reply you write back, accepting or rebutting it, is the evidence.*
