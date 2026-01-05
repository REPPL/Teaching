# MN5813

## Business Analytics Languages and Platforms

*Content (incl. `README.md` files and Jupyter Notebooks) was originally compiled by Alex Reppel (AR) based on conversations with [ClaudeAI](https://claude.ai/) *(version 3.5 Sonnet)*. For this year's materials, further revisions were made using [Claude Code](https://www.anthropic.com/claude-code) *(Opus 4.1)*, including updated documentation and git commit messages.*


## Session outline

| Week | Format | Topic | Content | README |
|------|--------|-------|---------|--------|
| Setup | Self study | Installation & Python basics | Anaconda installation, environment setup, and Python foundations for non-programmers | [📖](./Setup/README.md) |
| Week 01 | In person | Introduction to Python | Python fundamentals: variables, strings, control flow, functions, lists, dictionaries, file I/O | [📖](./Week01/README.md) |
| Week 02 | In person | Advanced Python | List comprehensions, lambda functions, functional programming, error handling, OOP concepts | [📖](./Week02/README.md) |
| Week 03 | In person | Assessment | Overview of two-part assessment: group project (artefact) and individual analytics report | [📖](./Week03/README.md) |
| Week 04 | In person | Introduction to Pandas | DataFrames, Series, file I/O, basic operations, merging, and aggregation | [📖](./Week04/README.md) |
| Week 05 | In person | Advanced Pandas | Data reshaping (melt, pivot, stack/unstack), window functions, and complex aggregations | [📖](./Week05/README.md) |
| Week 06 | In person | Pandas application (group project workshop) | Apply Pandas skills to the group assignment | [📖](./Week06/README.md) |
| Week 07 | In person | Introduction to data visualisation | Basic plotting with Pandas, Seaborn, Matplotlib | [📖](./Week07/README.md) |
| Week 08 | In person | Advanced Data visualisation | Time series visualisation, interactive plots with hvPlot, small multiples | [📖](./Week08/README.md) |
| Week 09 | In person | Data visualisation practice | Practical session to work towards your group assignment | [📖](./Week09/README.md) |
| Week 10 | In person | First revision session | Module revision to support your group assignment | |
| Week 11 | Hybrid | Second revision session | Q&A & revision to support your individual report | |


## Progress flow

```
┌─────────────────────┐
│ Setup: Environment  │ ← Start here: Install Anaconda & generate datasets
└──────────┬──────────┘
           │
┌──────────▼──────────┐
│        Block 1      │ ← Foundation: Variables, strings, functions, data structures
│        =======      │
│                     │ 
│  Weeks: 1-3         │ ← Build skills: Functional programming, error handling
│                     │
│  PYTHON             │ ← KEY MILESTONE: Understand requirements
│                     │   • Group Project (20%): Olympics data
│                     │   • Individual Report (80%): Your choice
└──────────┬──────────┘
           │
┌──────────▼──────────┐
│        Block 2      │ ← Core tool: DataFrames for data analysis
│        =======      │
│                     │ 
│  Weeks: 4-6         │ ← Power skills: Reshape, pivot, aggregate
│                     │
│  PANDAS             │ ← APPLY: Clean & prepare group project data
│                     │ → Progress on Group Project
│                     │ 
└──────────┬──────────┘
           │
┌──────────▼──────────┐
│        Block 3      │ ← Visualise: Charts, plots, best practices
│        =======      │
│                     │ 
│  Weeks: 7-9         │ ← Enhance: Interactive & complex visuals
│                     │
│  DATA               │ ← CREATE: Compelling visualisations
│  VISUALISATION      │ → Progress on Individual Report
│                     │ 
└──────────┬──────────┘
           │
      ┌────┴────┐
      │         │
┌─────▼────┐  ┌─▼──────────┐
│  Week 10 │  │  Week 11:  │ ← SUPPORT: Revision & Q&A sessions
│   First  │  │ Assessment │ → Final preparation for submissions
| revision │  |    Q&A     │
└──────────┘  └────────────┘
```


## Learning materials

Each week's folder contains different types of learning materials.

Recommendation:

1. Start with the `Introduction` notebook *(if available)*
2. Work through the `Demonstration` notebook
3. Attempt the `Exercises` independently
4. Check your work against the `Solutions`
5. Explore `Resources` for additional learning *(if available)*


### Core materials

- **Introduction.ipynb**: Overview of the week's objectives, key concepts, and learning outcomes. Start here to understand what you'll be learning.

- **Demonstration.ipynb**: Live coding examples with detailed explanations. These notebooks show how to apply concepts in practice with comprehensive code examples and outputs.

- **Exercises.ipynb**: Practice problems designed to reinforce learning. These contain challenges for you to solve independently, typically requiring 60-90 minutes to complete.

- **Solutions.ipynb**: Complete solutions to the exercises with explanations. Review these after attempting the exercises to check your understanding and learn alternative approaches.


### Supporting materials

- **Resources.ipynb**: Additional learning resources, references, and links to external materials for deeper exploration of topics.

- **Template.ipynb**: Starter templates for assignments or projects, providing structure and guidance for your work.

- **assets/**: Folder containing data files, images, and other resources used in the notebooks
  - CSV, JSON, Excel files for data analysis exercises
  - SVG diagrams for visual learning
  - Example outputs and reference materials
