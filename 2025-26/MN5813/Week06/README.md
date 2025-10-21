# Week 06: Pandas application (group project workshop)

## Overview

Week 06 is an application week where you apply the Pandas skills from Weeks 04 and 05 to your Olympics group project. This week bridges the gap between learning data wrangling techniques and implementing them in your assessment.

## The 3-week learning block

This week completes the Pandas learning block:

- **Week 04**: Basic Pandas principles (DataFrames, filtering, grouping, merging)
- **Week 05**: Advanced Pandas techniques (reshaping, pivot tables, MultiIndex)
- **Week 06**: Application to your Olympics group project ← **You are here**

## Week structure

Unlike previous teaching weeks, Week 06 focuses on **application and practice**:

- **No new concepts** – consolidate what you've learnt
- **No exercises notebook** – you'll work on your actual project
- **Demonstration as reference** – worked example you can adapt
- **Group project time** – apply techniques to Olympics dataset

## Materials

### Notebooks

1. **[Introduction.ipynb](Introduction.ipynb)** – Application week overview, workflow, and common challenges
2. **[Demonstration.ipynb](Demonstration.ipynb)** – Complete worked example using Olympics-parallel dataset

### Data files

Located in `assets/data/`:

- **[employee_sales.csv](assets/data/employee_sales.csv)** – Demonstration dataset (245 rows × 15 columns)
- **[README.md](assets/data/README.md)** – Detailed dataset documentation and column mapping

### Project files (from Week 03)

- **[Week03/Template.ipynb](../Week03/Template.ipynb)** – Use this for your actual group project
- **[Week03/Introduction.ipynb](../Week03/Introduction.ipynb)** – Complete assessment requirements

## Your group project

### Dataset

**[120 years of Olympic history: athletes and results](https://www.kaggle.com/heesoo37/120-years-of-olympic-history-athletes-and-results)**

- 271,116 rows (athlete-event combinations)
- 15 columns: ID, Name, Sex, Age, Height, Weight, Team, NOC, Games, Year, Season, City, Sport, Event, Medal
- Data from Athens 1896 to Rio 2016

### Core requirements

1. **Data loading**: Load athlete_events.csv into Pandas
2. **Data cleaning**: Handle missing values, convert types, remove duplicates
3. **Data wrangling**: Create Age_Group, Full_Name, Century columns
4. **Data analysis**: Calculate averages, top countries, medal leaders
5. **Data visualisation**: Create meaningful visualisations
6. **Export results**: Save cleaned data and visualisations

See [Week 03 Introduction](../Week03/Introduction.ipynb) for complete details, marking criteria, and stretch goals.

## How to use Week 06 materials

### The demonstration dataset

The Demonstration uses `employee_sales.csv` – a dataset with **identical structure** to the Olympics data:

| Employee sales dataset | Olympics dataset |
|------------------------|------------------|
| employee_id | ID |
| name | Name |
| gender (F/M/D) | Sex (M/F) |
| age | Age |
| height_cm | Height |
| weight_kg | Weight |
| team | Team |
| region | NOC |
| quarter | Games |
| year | Year |
| half | Season |
| office | City |
| product_category | Sport |
| product | Event |
| award | Medal |

This 1:1 mapping allows you to:
- See complete solutions to similar problems
- Understand the analytical approach
- Adapt code patterns to your Olympics data
- Develop problem-solving skills (not just copy code)

### Workflow

1. **For your project**: Use [Week03/Template.ipynb](../Week03/Template.ipynb)
2. **For guidance**: Reference Week06/Demonstration.ipynb
3. **For techniques**: Review Week04 and Week05 materials as needed

## Recommended session workflow

### Before the session (15 minutes)

- Review Week 04 Demonstration (basic Pandas)
- Review Week 05 Demonstration (data reshaping)
- Download Olympics athlete_events.csv
- Read Week 03 assessment requirements

### During the session (2 hours)

**Phase 1: Setup (15 min)**
- Organize your group, assign roles
- Copy Week03/Template.ipynb for your group
- Place athlete_events.csv in same directory

**Phase 2: Data loading (20 min)**
- Load dataset with `pd.read_csv()`
- Explore with `.head()`, `.info()`, `.describe()`
- Discuss initial observations
- Reference: Demonstration Part 2, Section 1

**Phase 3: Data cleaning (30 min)**
- Identify missing values (`.isnull().sum()`)
- Fix data types (Year to datetime)
- Remove duplicates
- Document your decisions
- Reference: Demonstration Part 2, Section 2

**Phase 4: Data wrangling (30 min)**
- Create Age_Group column
- Handle Full_Name (may already be complete)
- Extract Century from Year
- Reference: Demonstration Part 2, Section 3

**Phase 5: Initial analysis (30 min)**
- Average age by event
- Top 10 countries by gold medals
- Most decorated athletes by sport
- Reference: Demonstration Part 2, Section 4

**Phase 6: Plan next steps (15 min)**
- Review completed work
- Identify remaining requirements
- Assign tasks for outside session
- Schedule next meeting

### After the session

- Complete remaining analysis
- Create visualisations (Week 07-09 techniques)
- Write introduction, literature review, conclusion
- Format references
- Review and polish together

## Common challenges

### Challenge 1: Missing medal values

**Issue**: Most athletes don't win medals (Medal column is mostly NaN)

**Solution**: This is expected! Filter appropriately:
```python
# Count only medals (not NaN)
df[df["Medal"].notna()].groupby("NOC")["Medal"].count()
```

### Challenge 2: Year to datetime

**Issue**: Year is integer, not full date

**Solution**:
```python
df["Year_dt"] = pd.to_datetime(df["Year"], format="%Y")
```

### Challenge 3: Duplicate entries

**Issue**: Athletes appear multiple times (different events/years)

**Solution**: This is correct! Each row = one athlete-event. Only remove true duplicates:
```python
df.drop_duplicates()  # Removes identical rows only
```

### Challenge 4: Team vs individual sports

**Issue**: Multiple athletes get same team medal

**Solution**: Document your approach (count per athlete or per event)

### Challenge 5: Historical country changes

**Issue**: NOC codes for countries that no longer exist (USSR, etc.)

**Solution**: Keep as-is (basic) or combine historical/modern codes (stretch goal)

See [Introduction notebook](Introduction.ipynb) for more detailed solutions.

## Stretch goals (advanced techniques)

Once essentials are complete, consider Week 05 techniques:

- **Reshaping**: Use `pivot_table()` for medal counts by country/year
- **MultiIndex**: Hierarchical analysis (Country → Sport → Event)
- **Trends**: Rolling averages of participation over time
- **Advanced aggregations**: Multiple functions simultaneously

Reference: Demonstration Part 2 "Advanced placeholder" sections

## Time commitment

**Note**: This module uses 60-minute lecture slots and 2-hour workshop slots. The timings below show how content fits within these sessions, allowing time for discussion and questions.

- **Introduction**: 20-30 minutes (presented in 45-minute lecture, which fits comfortably in the 60-minute slot)
- **Demonstration**: 60-90 minutes (self-study notebook, work through before workshop)
  - Complete worked example using Olympics-parallel dataset
  - Reference material for adapting to your project
  - Run code cells, see how techniques apply to similar data
- **Workshop**: 90 minutes (group project work with instructor support, fits comfortably in the 2-hour workshop slot)
- **Follow-up work**: Variable (depends on group progress and requirements)

**Session structure**:
- Lecture: 45 minutes (introduces Week 07 content)
- Workshop: 105 minutes (includes setup time and early departure)

**Total in-session**: 2.5-3 hours
**Total with follow-up**: Variable based on project needs

## Recommended workflow

1. **Attend lecture** (45 min) - Introduction to Week 07 topics (data visualisation)
2. **Work through Demonstration** (60-90 min) - Before workshop (see complete worked example)
   - Run all code cells with employee_sales data
   - Identify which techniques apply to your Olympics project
   - Note the 1:1 column mapping for adaptation
3. **Attend workshop** (105 min) - Apply techniques to your Olympics group project
4. **Complete group work** (variable) - Finish remaining project requirements outside session

## Connection to assessment

### Group report (20%)

Week 06 provides:
- Structured approach to data loading, cleaning, wrangling
- Example analyses you can adapt
- Best practices for documentation
- Workflow for collaborative coding

### Individual analytics report (80%)

Week 06 skills transfer to:
- Your chosen dataset
- More sophisticated analyses
- Advanced techniques for higher marks
- Professional data workflows

## Getting help

- **In-session support**: Use session time to ask questions
- **Moodle Q&A Forum**: Post challenges and solutions
- **Office hours**: Detailed guidance on approaches
- **Demonstration notebook**: Worked example for reference
- **Week 04/05 materials**: Technical reference

## Further resources

- **Week 03 Introduction**: Assessment brief, marking criteria
- **Week 03 Template**: Notebook structure for submission
- **Week 04 Materials**: Basic Pandas reference
- **Week 05 Materials**: Advanced techniques reference
- **Pandas Documentation**: [Missing data](https://pandas.pydata.org/docs/user_guide/missing_data.html), [Group by](https://pandas.pydata.org/docs/user_guide/groupby.html)
- **Olympics Dataset**: [Kaggle page](https://www.kaggle.com/heesoo37/120-years-of-olympic-history-athletes-and-results)

## Next steps

After Week 06:

1. **Complete group project**: Continue working with your group
2. **Week 07-09**: Learn data visualisation for your project
3. **Apply visualisation**: Add sophisticated plots to your analysis
4. **Finalize submission**: Polish, format, review before deadline

---

**Week structure**: Application week (Week 04 = basic, Week 05 = advanced, Week 06 = application)

**Important**: Use Week03/Template.ipynb for your actual project, use Week06/Demonstration.ipynb as a reference guide
