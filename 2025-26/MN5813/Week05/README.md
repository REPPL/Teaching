# Week 05: Advanced Pandas

## Overview

This week explores advanced Pandas techniques for complex data manipulation and analysis, building on the fundamentals you learnt in Week 04. You'll master data reshaping, pivot tables, hierarchical indexing, and advanced aggregation techniques essential for sophisticated data analysis.

## Learning objectives

By the end of this week, you will be able to:

- Understand and apply tidy data principles to structure datasets effectively
- Reshape data between wide and long formats using `melt()`, `pivot()`, and `pivot_table()`
- Work with hierarchical data using MultiIndex for multi-dimensional analysis
- Apply window functions and rolling calculations for trend analysis
- Perform complex aggregations with multiple functions simultaneously
- Create efficient data processing pipelines using method chaining
- Understand when and why to use different data structures for analysis

## Materials

### Notebooks

1. **[Introduction.ipynb](Introduction.ipynb)** – Key concepts, tidy data principles, and further resources
2. **[Demonstration.ipynb](Demonstration.ipynb)** – Hands-on demonstrations of data reshaping and advanced operations
3. **[Exercises.ipynb](Exercises.ipynb)** – 90-minute practice exercises with business scenarios
4. **[Solutions.ipynb](Solutions.ipynb)** – Detailed solutions with explanations and alternative approaches

### Data Files

Located in `assets/data/`:

- Sample datasets are generated within the notebooks for demonstration purposes
- No external data files required for Week 05

## Topics Covered

### 1. Tidy Data Principles

- Understanding "tidy" vs "messy" data
- The three principles of tidy data
- When and why to reshape data
- Common data quality problems and solutions

### 2. Data Reshaping Fundamentals

- **Wide vs long format**: Understanding the differences and use cases
- **`melt()`**: Converting wide data to long format
- **`pivot()`**: Converting long data to wide format
- **`pivot_table()`**: Advanced pivoting with aggregation functions

### 3. MultiIndex Operations

- Creating and manipulating hierarchical indices
- Cross-sectional selection with `.xs()`
- `stack()` and `unstack()` for reshaping multi-level data
- Sorting and slicing MultiIndex DataFrames

### 4. Advanced DataFrame Operations

- Window functions and rolling calculations
- Group-wise transformations with `.transform()`
- Advanced data cleaning techniques
- Binning continuous data with `pd.cut()` and `pd.qcut()`

### 5. Aggregation and Analysis

- Applying multiple aggregation functions simultaneously
- Creating summary statistics by multiple groups
- Method chaining for efficient data pipelines
- Time series resampling and analysis

## Prerequisites

Before starting this week's materials, you should be comfortable with:

- **Week 04 Pandas fundamentals**:
  - Creating and manipulating DataFrames
  - Filtering and selecting data with boolean indexing
  - Using `groupby()` for basic aggregations
  - Merging and concatenating DataFrames
  - Handling missing values

- **Python fundamentals (Weeks 01-02)**:
  - Lists, dictionaries, and functions
  - Control flow (if/else, loops)
  - List comprehensions

If you need to review these topics, please revisit the appropriate week's materials before proceeding.

## Key Concepts

### Tidy Data

A dataset is tidy when:
1. Each variable forms a column
2. Each observation forms a row
3. Each type of observational unit forms a table

Tidy data makes analysis easier, more intuitive, and compatible with most data analysis tools.

### When to Reshape

- **Melt to long format** when:
  - Creating visualisations
  - Performing statistical analysis
  - Working with time series data
  - Preparing data for machine learning

- **Pivot to wide format** when:
  - Creating summary tables
  - Comparing values across categories
  - Calculating differences between time periods
  - Preparing data for reporting

### MultiIndex Use Cases

- Organizing hierarchical data (Country → Region → City)
- Multi-dimensional analysis
- Complex grouping operations
- Time series with multiple frequencies

## Practical Applications

This week's content is essential for:

- Preparing data for statistical analysis and machine learning
- Creating publication-ready summary tables
- Integrating data from multiple sources with different structures
- Building efficient data processing pipelines
- Analyzing multi-dimensional business data (sales by region, product, time)
- Identifying trends and patterns in complex datasets

## Time commitment

**Note**: This module uses 60-minute lecture slots and 2-hour workshop slots. The timings below show how content fits within these sessions, allowing time for discussion and questions.

- **Introduction**: 20-30 minutes (presented in 45-minute lecture, which fits comfortably in the 60-minute slot)
- **Demonstration**: 60-75 minutes (self-study notebook, work through before workshop)
  - Core content: Essential techniques for exercises
  - Supplementary content: Optional deeper exploration
  - Run code cells, experiment with examples, take notes
- **Workshop exercises**: 90 minutes (hands-on practice with instructor support, fits comfortably in the 2-hour workshop slot)
- **Solutions review**: 30 minutes (after completing exercises)

**Session structure**:
- Lecture: 45 minutes (introduces next week's content)
- Workshop: 105 minutes (includes setup time and early departure)

**Total self-study**: Approximately 3-3.5 hours per week

## Recommended workflow

1. **Attend lecture** (45 min) - Conceptual introduction to next week's topics
2. **Work through Demonstration** (60-75 min) - Before workshop (optional but strongly recommended)
   - Run all code cells in sequence
   - Experiment with modifying examples
   - Take notes on techniques you'll use in exercises
3. **Attend workshop** (105 min) - Practice exercises with instructor support
4. **Review solutions** (30 min) - Compare your approach after workshop

## Study Tips

1. **Follow along actively**: Run the Demonstration code yourself, experiment with variations
2. **Understand the "why"**: Don't just memorize syntax—understand when to use each technique
3. **Practice with your own data**: Apply these techniques to datasets you're interested in
4. **Focus on patterns**: The core patterns (melt/pivot, group/aggregate) appear repeatedly
5. **Reference the documentation**: Week 05 is complex—use the Pandas documentation liberally
6. **Connect to Week 04**: These advanced techniques build directly on basic operations

## Further resources

See the [Introduction notebook](Introduction.ipynb) for comprehensive reading lists, including:

- Academic readings on tidy data principles
- Pandas documentation on reshaping and aggregation
- Video tutorials on advanced Pandas operations
- Interactive learning resources

## Connection to assessment

The techniques in Week 05 are crucial for:

- **Week 06**: Application to your Olympics group project
- **Stretch goals**: Advanced analyses beyond basic requirements
- **Individual project**: More sophisticated data manipulation and analysis

Mastering Week 05 content will enable you to:
- Create more insightful analyses
- Handle complex data structures efficiently
- Present findings in multiple formats
- Demonstrate advanced technical skills

## Getting help

- **Moodle Q&A Forum**: Ask questions about concepts or exercises
- **Office Hours**: For detailed explanations and guidance
- **Week 04 Materials**: Review if you're struggling with basic Pandas operations
- **Pandas Documentation**: Comprehensive reference with examples

## Next steps

After completing Week 05:

1. **Week 06**: Apply these techniques to your Olympics group project
2. **Practice**: Try reshaping and analyzing your own datasets
3. **Explore**: Investigate additional Pandas features for your interests
4. **Prepare**: Week 07-09 cover data visualisation—you'll visualise reshaped data

---

**Week structure**: Teaching week (Week 04 = basic, Week 05 = advanced, Week 06 = application)
