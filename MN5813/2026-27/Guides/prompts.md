# Prompt library

*Every prompt the module's materials ask you to try (and adapt!).*

> ⚠️ **Draft:** This page is a draft. It will be confirmed at a later date.

This page collects the prompts that appear across <!-- gen:values.yml#module.code -->MN5813<!-- /gen -->. It holds one template prompt for each of the four "moves" and the six prompting patterns. 

It also holds the [Debrief](./glossary.md#term-debrief) prompts and the REFLECT prompt. Fill in anything in brackets (e.g., *your code*, *your figure*, and *your questions*). Then paste the whole prompt into your [Associate](./glossary.md#term-associate). Do not reword it, so that you learn its outcomes (which may differ). Adapt later. 

Where a note in *italics* follows the prompt, judge the reply against it. The note says what a good answer contains. The *moves* and the *habits* of checking are in the [AI guide](./ai-guide.md). The glossary explains the [Debrief](./glossary.md#term-debrief) stage.


## The four moves

[Section 3 of the AI guide](./ai-guide.md) describes them. This page gives one template prompt for each.

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

The six patterns are in [section 4 of the AI guide](./ai-guide.md). Adapt the words and keep the structure.

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

**REFLECT: Read your own prompting**: Open one transcript from `.specstory/history/`, or your [Prompt Diary](./glossary.md#term-prompt-diary), then paste this with the file open.

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
