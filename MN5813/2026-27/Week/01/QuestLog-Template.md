# QuestLog: [your name]

*My personal learning journal for this module, started [date].*

## Why this file exists

This log is three things:

1. **Your record.** You write one dated entry per [quest](https://github.com/REPPL/Teaching/blob/main/MN5813/2026-27/Guides/glossary.md#term-quest), in your own words
2. **Your evidence.** You claim [badges](https://github.com/REPPL/Teaching/blob/main/MN5813/2026-27/Guides/glossary.md#term-badge) here, and they are spot-verified in workshops. Your entries feed the [AI Use Record](https://github.com/REPPL/Teaching/blob/main/MN5813/2026-27/Guides/glossary.md#term-ai-use-record) in both assessments (see `Guides/ai-guide.md`, section 6, "Your record is your evidence")
3. **Your revision aid.** By Week 10 this log holds a term of notes on what you learned, where the [Associate](https://github.com/REPPL/Teaching/blob/main/MN5813/2026-27/Guides/glossary.md#term-associate) misled you, and what you would do differently

## How to use it

- Copy this file and rename it `QuestLog.md`
- Keep it at the top level of your repository, which you create in Week 2
- Add each entry within a day of finishing the quest. A short, honest entry beats a polished one written late
- Delete the "Why this file exists" and "How to use it" sections once the file is yours. Keep the example entry at the bottom until you have written two entries of your own

## Badge table

Quests are numbered by teaching week. Weeks 3, 7, 9, and 10 have no quest, so those numbers are missing from the table. Quest 02b belongs to the optional Week 2b.

| Quest | Badge claimed (🥉/🥈/🥇) | Date |
|-------|------------------------|------|
| [Workstation Ready](https://github.com/REPPL/Teaching/blob/main/MN5813/2026-27/Guides/glossary.md#term-workstation-ready) ⭐ | | |
| Quest 01: [Tutorial Island](https://github.com/REPPL/Teaching/blob/main/MN5813/2026-27/Guides/glossary.md#term-tutorial-island) | | |
| Quest 02 | | |
| Quest 02b (optional) | | |
| Quest 04 | | |
| Quest 05 | | |
| Quest 06 | | |
| Quest 08 | | |

Workstation Ready is the Week 2 badge. Claim the ⭐ when you have ticked all ten checklist items in the Codespaces Start guide (`Guides/codespaces-start.md`). You do items 1 and 2 in Week 1. You tick items 3 to 10 with the class in the Week 2 workshop.

---

## Entry template

Copy this block for each quest:

```markdown
## Quest NN: [title]

- **Date:**
- **Badge claimed:** 🥉 / 🥈 / 🥇
- **1. Client explanation** (this week's key technique, three sentences, no jargon):
- **2. Associate audit** (where the AI was wrong, misleading, or unhelpful, with the exchange):
- **3. Quiz me** (the three questions it set me, and how I did without AI):
- **One thing I'll do differently next quest:**
```

---

## EXAMPLE (Quest 01: Tutorial Island)

*This example comes from the module team and shows the expected length and honesty. It contains **Quest 01 answers**. Do the quest and write your own entry before you read it.*

- **Date:** 1 October
- **Badge claimed:** 🥈
- **1. Client explanation:** One of the twelve prices on the receipt was typed as text rather than a number. That is why the computer refused to add it up. We converted it back to a number and got the right total, £36.80, which matches the £3.20 change from the £40 note. The lesson is that data that *looks* fine can still be the wrong kind of thing, so we check types before we trust totals
- **2. Associate audit:** Gemini's "quick" version crashed on the text price, which the quest warned about. But I had to catch the worse mistake myself. When I asked it what the average was, it *told me* "£3.35" in chat instead of running anything. The real answer from my code was £3.07. It stated a wrong number with complete confidence. I noted the exchange in my AI Use Record. The rule I learned: Only trust numbers from code that I ran
- **3. Quiz me:** It set me: (1) What does `len()` do, (2) why does `"2.80" + 0.30` fail, (3) write a loop that finds the most expensive item. Got 1 and 2 right, made a mess of 3 (forgot to update the variable inside the `if`) but fixed it without asking. Fair result: Loops need more reps
- **One thing I'll do differently next quest:** Write my prediction cells properly instead of vague ones like "some numbers". The one prediction I wrote precisely ("twelve lines saying float") was the one that caught the string price. That turned out to be the whole quest
