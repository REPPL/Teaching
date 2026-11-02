# The Runnymede Standard: Data visualisation design guide

*The reference for creating charts & figures in the "DataViz" block (weeks 6, 8, and 9) and in both assessments.*

Remember: [Runnymede Analytics](./glossary.md#term-runnymede-analytics) is old school in the way that every figure you send to a client must carry **your name**. Your [Associate](./glossary.md#term-associate) can draft a figure in seconds. You decide whether it is the *right* figure: Accurate, clear, accessible, and, above all, answers the client's *question*. 

This guide explains how to make that choice and how to show your reasoning.

---

## 1. Design judgement

Your Associate (typically) produces a polished chart from a one-line prompt (until it doesn't). Joking aside, your Associate can struggle with knowing whether that chart answers the question, misleads the reader, or even suits the audience.

These judgements stay with you:

- **Choosing.** Which chart serves this question for this reader? The Associate makes a plausible chart of the data. You make the chart the reader can act on
- **Not misleading.** A truncated axis, a flattering baseline, or a dual axis that suggests a correlation is a design <!-- plain-language: everyday decision -->decision. You are responsible for it. The Associate does not notice when a chart misleads (although they'll happily investigate if you ask them to!)
- **Audience.** The Associate has never met your client and does not know what they already believe

One rule for the whole term: **A beautiful wrong chart is worse than an ugly right one.** The ugly right one fails to impress. The beautiful wrong one will be worked with and acted on. In other words, it has *implications*.

This guide is about figures made for a reader. While you explore a dataset, you also make quick, rough figures for yourself, to find out what the data shows. They matter: Summary statistics can hide what a plot shows at once. Anscombe (1973) built four small datasets with almost the same means, variances, and correlations (see [my summary on Moodle](https://moodle.royalholloway.ac.uk/pluginfile.php/2134003/mod_resource/content/4/Talk.html)). Plotted, they look nothing alike. An exploratory figure needs no takeaway title and no rationale. Once a figure goes to a reader, everything in this guide applies.

The guide follows the letters of **[TRACE](./glossary.md#term-trace)**:

- Task
- Reduce
- Accessible
- Context
- Explain

Section 7 turns these letters into the checklist for every key figure. Section 8 sets out the [Four-D crit](./glossary.md#term-four-d-crit), and section 9 covers working with your Associate on figures.

---

## 2. T: Task

Start from the **question**, not from the data ("what can I plot?") or from the charting tool ("what does seaborn make pretty?"). What does the reader need to see, compare, or decide? Write that question down in one sentence before you prompt for anything. Quite frankly ... if you cannot write it, you are not ready to make a figure!

Almost every business question is one of the following analytical tasks. Each task has its usual chart forms and its common mistakes:

- **Comparison.** The reader needs to rank or compare values across categories
  - Usual forms: A horizontal bar chart sorted by value, or a dot plot (one dot per category on a common scale) for many categories
  - Common mistakes: Alphabetical order (sort by value unless the categories have a natural order), 3D bars, and bars that do not start at zero
- **Distribution.** The reader needs to see the shape, spread, and outliers of one variable
  - Usual forms: A histogram, a box plot for several groups side by side, or a strip or violin plot when the shape matters
  - Common mistake: Reporting only the mean. A bar chart of averages hides everything a distribution question asks about
- **Relationship.** The reader needs to judge whether two variables move together
  - Usual forms: A scatter plot. Add a trend line only if you can defend it. Use bubble size only for a third variable the reader needs roughly, not exactly
  - Common mistakes: A title that implies causation, lines connecting the scatter points, and overplotting (points so dense they hide one another). For overplotting, use transparency or 2D bins (a grid that shows how many points fall in each cell)
- **Change over time.** The reader needs to follow a trend and spot turning points
  - Usual forms: A line chart. Use an area chart only for cumulative or stacked totals. For many series, use small multiples (a grid of mini charts, one per series, sharing the same axes)
  - Common mistakes: More than about four lines in one panel, smoothing that hides the turning points, and uneven time intervals plotted as even
- **Part-to-whole.** The reader needs to see how a total divides into components
  - Usual forms: A stacked bar (few components), or a 100% stacked bar for comparing compositions. A plain sorted bar chart is often clearer than both
  - Common mistakes: Pie and doughnut charts, and stacked areas whose middle layers cannot be read. Although some disagree, I strongly recommend never using a pie chart

In the following, I've summarised my teaching materials on data visualisation for this module. An important concept is that of **visual encodings**, that is, how data is represented in a chart. Looking at which encodings work best for people has a long history in data visualisation design. For example, Cleveland and McGill (1984) showed that *position* (i.e., where a value is positioned in a chart) is most important, followed by length, direction, and angle. Heer and Bostock (2010) repeated the experiments with far more people and found pretty much the same. The [Week 6 Introduction](../Week/06/Introduction.ipynb) tests the ranking on you.

Some authors, such as Tamara Munzner (2014), count *motion* as a visual encoding, too. She describes interaction (hovering, filtering, and zooming) as a way to show more detail, which is now possible on a screen (vs. on static paper). So, a printed report or a PDF is static and its figures cannot use motion. But a screen can. The Week 8 Demonstration shows an interactive chart made with hvPlot (while we won't spend much time on it, it's useful to know).

Keep these habits:

- **One figure, one task.** A chart that tries to show too much shows ... nothing. Split it
- **Tables for exact values.** If the reader needs exact values, or will look up a specific number at a time, use a table
- **More chart forms.** For an unusual task, use the [FT Visual Vocabulary](https://github.com/Financial-Times/chart-doctor/tree/main/visual-vocabulary), the *Financial Times* poster that maps each analytical task to its chart forms

---

## 3. R: Reduce

Every mark on a figure should show data or help the reader read data. Everything else gets in the reader's way: Decorative borders, dense gridlines, tinted backgrounds, and redundant legends. Edward Tufte calls the share of a figure's ink that shows data its *data-ink ratio*. His rule is to make that ratio as high as you can, *within reason*.

Defaults add marks the reader does not need. matplotlib frames every plot with four spines. seaborn's default theme (`sns.set_theme()`) adds a grey background and a white grid. AI drafts often add a legend to everything. Reduction is nearly always your first edit.

Work through the **declutter sequence**, in this order, on every draft:

1. **Borders and spines.** "Spines" is matplotlib's word for the four lines framing the plot. Remove the box around the plot. Keep at most the bottom and left spines
2. **Gridlines.** Delete them. Add back only what the reader needs to judge values, usually a few light horizontal lines, or none if values are labelled directly
3. **Backgrounds.** Use white or transparent
4. **Replace legends with direct labels.** Wherever possible, delete the legend and label each line or bar directly, at its end. Write the label in the series colour only if that colour passes the text contrast test in section 4. On white, only the Okabe-Ito black and blue pass. Otherwise, use a darker shade of the series colour, or black text beside a marker in the series colour
5. **Rounding and axis density.** "£2.4m" beats "£2,412,384.17". Use fewer, rounder numbers along the axis. Avoid vertical axis text turned 90° where you can
6. **Emphasis last.** Once the clutter is gone, give the one series or bar that carries the story a single strong colour. Turn the rest grey

Give each step to your Associate as a short instruction ("remove the top and right spines"), then check the result. The Week 8 Demonstration applies the sequence to one chart, one step at a time.

---

## 4. A: Accessible

Roughly 8% of men and about 0.5% of women have some form of colour-vision deficiency, most often with red and green.

The Runnymede rules:

- **Use a colour-blind-safe palette by default.** Use one of these:
  - The **Okabe-Ito palette**: Eight colours that stay distinct under the common forms of colour-blindness. They are black `#000000`, orange `#E69F00`, sky blue `#56B4E9`, bluish green `#009E73`, yellow `#F0E442`, blue `#0072B2`, vermillion `#D55E00`, and reddish purple `#CC79A7`. Reference: [Okabe & Ito's Color Universal Design page](https://jfly.uni-koeln.de/color/) <!-- docs-lint: allow: ColorBrewer is a product name, "colorblind safe" its filter label, and the Okabe-Ito URL is a URL -->
  - **[ColorBrewer](https://colorbrewer2.org)**: Sequential, diverging, and qualitative palettes with a "colorblind safe" filter. Match the palette type to the data: Sequential for ordered values, diverging for values around a meaningful midpoint, and qualitative for unordered categories <!-- docs-lint: allow: ColorBrewer is a product name, "colorblind safe" its filter label, and the Okabe-Ito URL is a URL -->
- **Never encode by colour alone.** Add a second way to tell them apart: Direct labels, differing line styles or markers, position, or annotation. A figure printed in greyscale needs this too
- **Check contrast.** Text needs a contrast ratio of at least 4.5 to 1 against its background, the WCAG AA level for normal text. Lines, bars, and markers that carry data need at least 3 to 1. On white, the Okabe-Ito blue and black pass both tests, while its yellow, orange, and sky blue fail both. Grey text lighter than `#767676` fails on white. Test any pairing you are unsure of with the [WebAIM contrast checker](https://webaim.org/resources/contrastchecker/)
- **Text at final size.** Judge text at the size the figure will be seen, pasted into a report page or projected on a slide, not zoomed in a notebook. Once the figure is placed, make axis and label text no smaller than the report's footnote text
- **Alt text in one sentence.** Alt text is the sentence a screen reader reads in place of the image. Every figure in your submissions carries it, or an equivalent caption line. Write the chart type, then the variables, then the takeaway (the finding). For example: "Line chart of median first-engine attendance time per month across London since January 2025, showing the summer peak inside the six-minute target"
- **A longer description for key figures.** One sentence cannot list every value. Give each key figure a longer description as well. Write it as a short paragraph or a small table, with the values the takeaway rests on. Put it below the figure or in an appendix. The W3C's [complex images tutorial](https://www.w3.org/WAI/tutorials/images/complex/) calls the alt text and the longer description together a two-part text alternative

---

## 5. C: Context

### Takeaway titles

The title states the finding, not the variables. "Attendance time by borough and month" names the variables. "First engines reach the outer boroughs a minute later than the inner ones" states a finding. Test it: If a colleague reads only your titles, do they get your argument? Keep the descriptive version ("Median first-engine attendance time by borough, 2025") as a subtitle if the figure needs it.

### Annotation

Annotation puts your words on the figure, next to the data they explain. Most business figures need one to three annotations. These are the usual kinds:

- **Mark the event**: A thin line and a short label where something changed ("Relaunch, Oct 2025")
- **Name the difference**: The number that matters, next to the gap, peak, or drop it describes ("−£38k year on year")
- **Say the "so what"**: One short phrase of interpretation, on the chart ("growth now covers the in-store decline")

Annotate the finding, not every small movement in the data. If a figure needs more than three annotations, it makes too many points.

In the title and the annotations, claim only what the figure shows. Kong, Liu, and Karahalios (2018) showed people the same chart under differently slanted titles. The title changed what readers took from the chart. Readers also remembered the title's message more than the data's. A doubtful reader holding only your figure should be able to check every claim on it. The Week 8 Introduction puts annotations like these on one chart.

### Axis labels and units

Label every axis with what it measures **and its units**: "Revenue (£m)", "Athletes per team", "Change since 2000 (%)". If the values are transformed (log-transformed, indexed, per head, seasonally adjusted), the label states it, prominently.

### Baselines

- **Bar charts: Start at zero.** Bars show value as length. Cut the axis at 90 and a 5% difference looks like a large one. On a log scale, where zero cannot appear, bars of ratios start at 1, the point of no change. Where zero means nothing for the measure, use dots instead of bars
- **Line charts: The axis may start above zero.** Lines show value as position and slope, so a cropped axis can be the right choice. A chart of body temperature would be unreadable from zero. The range must show variation that matters, not exaggerate a small change. If you crop the axis, say so on the figure ("axis begins at 80"), and defend the choice in your rationale. Never shade the area under a cropped line, because the shaded area then reads as the value

### Misleading designs

Your Associate will likely produce all of the following:

- **Truncated bar axes**: A bar chart whose axis does not start at zero
- **Dual y-axes**: Two different scales in one panel let you make any two series look correlated by adjusting the scales. Two stacked panels sharing an x-axis are almost always better. So is indexing both series to 100 at a common start point: Divide every value by the series' starting value and multiply by 100. If you must use dual axes, justify them in the rationale
- **Selective time windows**: A trend that starts at the most flattering year. Show the fuller window, or state why the window is what it is
- **Uneven intervals plotted evenly**: The [releases](./glossary.md#term-release) in the [abcd record](./glossary.md#term-abcd-record) come several on one day, then more than a week apart. Convert the dates with `pd.to_datetime()` before you plot: matplotlib spaces real dates by time, and spaces dates stored as text evenly
- **Area and 3D distortion**: Readers misjudge value shown as area or volume. 3D adds distortion and nothing else
- **Deleted uncertainty**: Dropping error bars, confidence bands, or small-sample warnings because they look untidy. If the uncertainty changes the conclusion, hiding it is the most serious mistake on this list

### Like-for-like comparisons

A comparison of raw numbers often misleads:

- **Rates, not counts, when groups differ in size.** A borough with twice the homes can have twice the fires and the same risk. Divide by the size of each group (incidents per 1,000 homes, revenue per store). Name the rate in the axis label
- **Real money across years.** Prices rise, so £100 in 2015 bought more than £100 does today. When you plot money over several years, adjust it for inflation. Name the base year in the axis label ("Revenue (£m, 2025 prices)")
- **Maps of rates, not counts.** A map shaded by raw counts mostly shows where people live. Shade by a rate, or show the counts as a sorted bar chart

### Source and date

Every key figure carries a source line: Dataset name, coverage period, and any filters applied. For example: *"Source: London Fire Brigade incident records, London Datastore; incidents from 1 January 2025; false alarms excluded."* The [fire brigade data note](../Assessment/lfb-data.md) gives the licence line your group project carries. Date the figure if the data could go out of date.

---

## 6. E: Explain

Every key figure in the group project and the individual report comes with a written **[design rationale](./glossary.md#term-design-rationale)**. The [group project](../Assessment/group-project.md) and [individual report](../Assessment/individual-report.md) <!-- plain-language: everyday brief -->briefs set how many key figures to expect and how long each rationale runs.

A rationale has these parts, in order:

1. **The question.** What the reader needs to see or decide, in one or two sentences
2. **Why this form.** Which analytical task this is (section 2), and why this chart type serves it
3. **Alternatives rejected.** At least one credible alternative you considered, and the specific reason it lost
4. **AI draft vs your changes.** What your Associate first produced, what you changed, and why. Cite your [Prompt Diary](./glossary.md#term-prompt-diary) entry

### A good rationale

> **Figure 4: Small multiples of median first-engine attendance time by month, six busiest boroughs.**
> The question is whether response times in the busiest boroughs are drifting apart or moving together over the eighteen months. It is a change-over-time comparison across six boroughs. A single line chart of six series was unreadable, with four lines overlapping between 300 and 360 seconds. I chose small multiples: One mini line chart per borough, sharing identical x- and y-axes. The reader can then compare shapes and levels at a glance. The panels are ordered left to right by incident count, so position shows workload. I rejected a stacked area chart because it answers a part-to-whole question, not this one, and middle layers are unreadable. I rejected an animated chart because the report is a static document. My Associate's first draft used a rainbow palette, independent y-axes per panel, and the title "Attendance Time by Borough". I fixed the axes to a common scale, because independent scales flattered the quieter boroughs and broke comparability. I replaced colour-coding with one Okabe-Ito blue per panel plus a grey all-London reference line for context. I retitled it to the finding: "Since spring, the outer boroughs have drifted away from the target." Source, period, and the excluded no-attendance incidents are on the figure. (Session: Prompt Diary, 16 November.)

Why it works: Every choice is tied to the question or the reader. The rejected alternatives are real, and the reasons specific. The part on the AI draft names concrete changes and why each mattered, not "I tidied it up".

### A weak rationale

> I used a line chart because it is good for showing data over time and looks clean and professional. I considered other charts but this one was the best fit for the data. The AI helped me make the chart and I checked it was correct. I made some improvements to the styling and colours so it looks better.

**What is wrong:** Every sentence could sit under any figure in any report. The alternatives are unnamed, and the "improvements" are unspecified.

Write the rationale while you design, not after. If part 3 is hard, you have not considered an alternative yet. Ask your Associate to draft one (section 9).

---

## 7. The TRACE checklist

TRACE is one way of drawing together work from Tufte (2001), Cleveland and McGill (1984), Munzner (2014), Knaflic (2015), Wilke (2019), and Cairo (2019). It also draws on [WCAG 2.2](https://www.w3.org/TR/WCAG22/).

Apply TRACE to **every key figure**, in both assessments before submission. In Week 9's [Gallery](./glossary.md#term-gallery), it is also used as a scorecard.

**Ask yourself:**

- **T: Task.** Does this figure answer a stated question for a known reader?
  - The question is written down in one sentence
  - The chart form matches the analytical task (section 2)
  - One figure, one task
- **R: Reduce.** Does every mark show data or help the reader read it?
  - Declutter sequence applied (section 3)
  - Legend replaced by direct labels where possible
  - Numbers rounded to what the <!-- plain-language: everyday decision -->decision needs
- **A: Accessible.** Can *everyone* in the room read it?
  - Colour-blind-safe palette, and nothing encoded by colour alone
  - Contrast checked, and text readable at final size
  - Alt text written: Chart type, variables, and takeaway
  - Longer description written: A short paragraph or a small table of the values
- **C: Context.** Does it stand on its own without misleading the reader?
  - Takeaway title states the finding
  - Axes labelled with units
  - Title and annotations claim only what the figure shows
  - Bars start at zero, or at 1 for ratios on a log scale
  - Uncertainty shown where it could change the conclusion: Error bars, intervals, or sample sizes
  - Counts turned into rates where groups differ in size
  - Money adjusted for inflation across years
  - No unjustified dual axes or selective time windows
  - Source, period, and filters on the figure
- **E: Explain.** Could you defend it to a sceptic?
  - Rationale written (section 6)
  - At least one rejected alternative, with a specific reason
  - AI draft vs your changes documented and traceable to a Prompt Diary entry

---

## 8. The Four-D crit protocol

The Four-D crit is one way of (very broadly) drawing together work from Feldman (1994) on the stages of art criticism. This is used in Week 9's Gallery, which is a structured peer critique of group-project figures. The crit protocol is also useful when you need a second opinion on a figure, including in a team meeting.

The rounds run in this order:

1. **Describe.** Critics say only what they literally see: "A line chart. Six lines. The y-axis has no units. The red line ends above the others." **No judgements yet**
2. **Decode.** Each critic states the figure's message in one sentence, without help. If three critics decode three different messages, the figure is ambiguous, whatever the author intended
3. **Diagnose.** Critics score the figure against TRACE, one line per letter (pass, fix, or fail), and articulate the **single biggest problem**
4. **Redesign.** Each critic proposes **exactly one change**: The one they believe has the highest impact

Ground rules:

- **Authors are silent until the author response.** No explaining, no defending, no "what I meant was". Authors respond only after step 4 (Redesign)
- **Critique the chart, never the person.** "The axis is unlabelled", not "you forgot the axis"
- **Every crit is written down.** Your team's scribe/note taker records each one as a [`CRIT` entry](./glossary.md#term-crit-entry). The [Stoa workflow guide](./stoa-workflow.md) explains where the entry goes

---

## 9. Your Associate

Your Associate draws charts fast and (over-)confidently. It cannot judge whether a design works, and it does not know your reader. Give it the task, ask it for options, and refine the best one. This is the [GENERATE-JUDGE](./glossary.md#term-generate-judge) move from the [AI guide](./ai-guide.md), applied to figures.

### The prompt pattern

State the **task, the audience, and the constraints** before you ask for anything:

> "I need a figure for the board pack (non-technical readers, printed A4, possibly greyscale). The task: Compare median first-engine attendance times across six boroughs over time, and show whether the gap to the six-minute target is closing. Constraints: Colour-blind-safe palette, no legend (direct labels), axis ranges that do not mislead (state any non-zero baseline), and a takeaway title. Draft **two contrasting approaches**, such as small multiples and a line chart indexed to 100 (section 5). Explain the trade-off between them."

Then **judge, pick, and refine the better one** with specific instructions. For example: "Common y-scale across panels; grey reference line for the all-London median; move the labels to the line ends."

Precise prompts need precise words. Wilkinson (2005) describes every chart within a *grammar of graphics*. In it, data is mapped to aesthetics (position, colour, size, and shape) and drawn as geometries (points, lines, and bars) in a coordinate system. Wickham (2010) built R's ggplot2 (arguably the best visualisation tool there is) on a layered version of it. "Map borough to colour and month to the x-axis" tells your Associate more than "make a chart of the boroughs".

To have your Associate critique a figure against TRACE, use the [AI Lens](./glossary.md#term-ai-lens) prompts in the [Week 6 Demonstration](../Week/06/Demonstration.ipynb). Check its verdict yourself, because it also passes charts that fail.

### Typical AI chart failures

In my experience, these appear often in Associate drafts. Catching them is [Red Flags](./glossary.md#term-red-flags) practice. Several appear in the Week 6 and Week 8 [AI failure galleries](./glossary.md#term-ai-failure-gallery):

- **Rainbow palettes by default**: Many colours, not colour-blind-safe, and implying an order that does not exist. Ask for `Okabe-Ito` or a `ColorBrewer` palette by name <!-- docs-lint: allow: ColorBrewer is a product name, "colorblind safe" its filter label, and the Okabe-Ito URL is a URL -->
- **3D anything**: Offered as "more visually engaging". It distorts the values. Refuse it
- **Over-legended figures**: A legend box for two series, on top of the data. Ask for direct labels instead
- **Dual y-axes by default**: Mention two variables over time, and your Associate often reaches for twin axes. Ask for stacked panels or indexing instead (section 5)
- **Deleted uncertainty**: Asked to "clean up" a figure, your Associate often removes error bars, confidence bands, and sample sizes as clutter. Put it back
- **Titles that name variables, not findings**: "Chart of X by Y". Always retitle it yourself

The rationale (section 6) and your [AI Use Record](./glossary.md#term-ai-use-record) say who did what, and your Prompt Diary backs both up.

---

## 10. Further reading

- **[FT Visual Vocabulary](https://github.com/Financial-Times/chart-doctor/tree/main/visual-vocabulary)**: The poster named in section 2
- **[Storytelling with Data blog](https://www.storytellingwithdata.com/blog)**: Cole Nussbaumer Knaflic's posts on decluttering and takeaway-driven business charts
- **[ColorBrewer](https://colorbrewer2.org)**: Pick a sequential, diverging, or qualitative palette with the colour-blind-safe filter on, and copy the hex codes into your code <!-- docs-lint: allow: ColorBrewer is a product name, "colorblind safe" its filter label, and the Okabe-Ito URL is a URL -->
- **[WebAIM contrast checker](https://webaim.org/resources/contrastchecker/)**: Paste two hex colours and get a pass or fail against the WCAG levels
- **[Datawrapper blog](https://www.datawrapper.de/blog)**: Practical posts on chart choice and colour
- **[Okabe & Ito's colour universal design page](https://jfly.uni-koeln.de/color/)**: The original reference for the Okabe-Ito palette <!-- docs-lint: allow: ColorBrewer is a product name, "colorblind safe" its filter label, and the Okabe-Ito URL is a URL -->
- **Knaflic (2015), *Storytelling with Data***: A practical book on business charts
- **Cairo (2016), *The Truthful Art***: A book-length treatment of how charts mislead and how to stop yours doing it
- **Cairo (2019), *How Charts Lie***: A short, readable book on reading charts critically
- **Few (2012), *Show Me the Numbers*, 2nd edition**: A thorough desk reference for tables and graphs in business
- **Tufte (2001), *The Visual Display of Quantitative Information*, 2nd edition**: The book that introduced data-ink and chartjunk
- **Anscombe (1973), "Graphs in statistical analysis", *The American Statistician* 27(1)**: The four datasets in section 1
- **Cleveland and McGill (1984), "Graphical perception", *Journal of the American Statistical Association* 79(387)**: The ranking of encodings in section 2
- **Heer and Bostock (2010), "Crowdsourcing graphical perception", *CHI 2010***: The online repeat of Cleveland and McGill's experiments
- **Kong, Liu, and Karahalios (2018), "Frames and slants in titles of visualizations on controversial topics", *CHI 2018***: The study of slanted titles in section 5
- **[Healy (2018), *Data Visualization: A Practical Introduction*](https://socviz.co/)**: A free online textbook on making good charts in code
- **[Wilke (2019), *Fundamentals of Data Visualization*](https://clauswilke.com/dataviz/)**: A free online textbook on chart choice, colour, and common mistakes
- **Wong (2010), *The Wall Street Journal Guide to Information Graphics***: Short, practical rules for business charts
- **Munzner (2014), *Visualization Analysis and Design***: A university textbook on tasks, encodings, and channels
- **Feldman (1994), *Practical Art Criticism***: The stages of criticism the Four-D crit draws on
- **Wilkinson (2005), *The Grammar of Graphics*, 2nd edition**: The grammar in section 9
- **Wickham (2010), "A layered grammar of graphics", *Journal of Computational and Graphical Statistics* 19(1)**: The layered version behind ggplot2
- **[WCAG 2.2](https://www.w3.org/TR/WCAG22/)**: The W3C's accessibility standard, the source of the contrast levels in section 4

---

Related module documents:

- The [AI guide](./ai-guide.md) for the moves of working with your Associate
- The glossary entries for [Red Flags](./glossary.md#term-red-flags) and [Debrief](./glossary.md#term-debrief), the [quest](./glossary.md#term-quest) stages that connect to figure work
- The [Stoa workflow guide](./stoa-workflow.md) for your team's record, on Microsoft Teams or in a [Stoa](./glossary.md#term-stoa) room
- The [assessment interpretation](../Assessment/interpretation.md) for the AI Use Record and the process indicators
