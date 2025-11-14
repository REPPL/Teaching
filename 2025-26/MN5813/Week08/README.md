# Week 08: Advanced Data Visualisation

## Overview

This week explores advanced data visualisation techniques for complex analysis and interactive presentations, building on the fundamentals you learnt in Week 07. You'll master multi-panel figures, small multiples, time series visualisations, and interactive plotting essential for sophisticated data communication.

## Learning objectives

By the end of this week, you will be able to:

- Create complex time series visualisations with multiple series and dual axes
- Design small multiples (trellis plots) using FacetGrid for comparative analysis
- Build interactive visualisations with hvPlot for dynamic data exploration
- Apply advanced Seaborn techniques including PairGrid and complex statistical plots
- Design effective dashboards combining multiple visualisations
- Optimise visualisations for large datasets and performance

## Materials

### Notebooks

1. **[Introduction.ipynb](./Introduction.ipynb)** – Advanced concepts, building on Week 07 foundations
2. **[Demonstration.ipynb](./Demonstration.ipynb)** – Hands-on demonstrations of advanced techniques
3. **[Exercises.ipynb](./Exercises.ipynb)** – 90-minute practice exercises with complex scenarios
4. **[Solutions.ipynb](./Solutions.ipynb)** – Detailed solutions with design explanations

### Data files

Located in `assets/data/week08/`:

- Sample datasets are generated within the notebooks for demonstration purposes
- No external data files required for Week 08

## Topics

### 1. Complex Time Series

- Multiple time series on same axes
- Dual-axis plots for different scales
- Combining line and area plots
- Annotating key events and trends
- Trend lines and confidence intervals

### 2. Small Multiples

- **FacetGrid fundamentals**: Creating trellis plots
- **Consistent scales**: Fair comparisons across panels
- **Layout strategies**: Organising for readability
- **Applications**: Comparing trends across categories, regions, or time periods

### 3. Interactive Visualisation *(hvPlot)*

- Converting static plots to interactive
- Hover tooltips for detailed information
- Zooming and panning for exploration
- Linked brushing across multiple plots
- Dashboard components and widgets

### 4. Advanced Seaborn

- **PairGrid**: Comprehensive relationship matrices
- **Complex statistical plots**: Joint plots, violin plots with splits
- **Custom colour palettes**: Brand-consistent and accessible colours
- **Combining plot types**: Histograms, KDE, scatter in one figure

### 5. Dashboards

- Logical layout and information hierarchy
- Consistent styling across components
- Balanced use of space
- Clear narrative flow
- Effective use of colour and typography

### 6. Better Performance *(optional!)*

- Handling large datasets efficiently
- Aggregation before plotting
- Downsampling strategies
- Rendering performance tips

## Prerequisites

Before starting this week's materials, you should be comfortable with:

**Week 07 Visualisation fundamentals**:

- Creating basic `plot`s with Pandas, Matplotlib, Seaborn
- Customising titles, labels, colours, and legends
- Arranging `subplot`s
- Understanding chart types

**Weeks 04-05 Pandas skills**:

- `DataFrame` manipulation and aggregation
- `GroupBy` operations
- Data reshaping and pivot tables

If you need to review these topics, please revisit the appropriate week's materials before proceeding.

## Key concepts

### Small multiples (Trellis plots)

Small multiples show the same visualisation repeated across categories:
- Maintain consistent scales for fair comparison
- Reveal patterns that differ by group
- Reduce cognitive load vs overlapping plots
- Ideal for categorical comparisons

### Interactive visualisations

Interactive plots enable:
- **Exploration**: Users can zoom, pan, and investigate details
- **Engagement**: Dynamic features increase audience attention
- **Flexibility**: One visualisation serves multiple purposes
- **Presentations**: Professional, modern data storytelling

**Note**: Your final report requires static figures (PNG/PDF), but interactive plots enhance presentations and exploration.

### Dashboard design principles

Effective dashboards:

1. **Focus on key insights**: Don't overwhelm with information
2. **Logical flow**: Guide the viewer through the story
3. **Consistent styling**: Unified colour scheme and typography
4. **Clear hierarchy**: Important information stands out
5. **Appropriate detail**: Balance overview with specifics

## Practical applications

This week's content is essential for:

- Creating comprehensive exploratory visualisation suites
- Building integrated figures for project reports
- Presenting multiple findings cohesively
- Adding interactivity for stakeholder presentations
- Designing professional data dashboards
- Communicating complex insights effectively

## Time commitment

**Note**: This module uses 60-minute lecture slots and 2-hour workshop slots. The timings below show how content fits within these sessions, allowing time for discussion and questions.

- **Introduction**: 20-30 minutes (presented in 45-minute lecture, which fits comfortably in the 60-minute slot)
- **Demonstration**: 60-75 minutes (self-study notebook, work through before workshop)
  - Core content: Essential advanced techniques for exercises
  - Supplementary content: Interactive visualisation and advanced customisation
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
   - Note techniques you'll use in exercises and your project
3. **Attend workshop** (105 min) - Practice exercises with instructor support
4. **Review solutions** (30 min) - Compare your approach after workshop

## Tips

1. **Follow along actively**: Run the Demonstration code yourself, try variations
2. **Understand design choices**: Why use small multiples vs overlapping lines?
3. **Practice with your data**: Apply techniques to your individual project dataset
4. **Focus on patterns**: Learn when to use each advanced technique
5. **Reference Week 07**: These advanced techniques build on basic plotting
6. **Experiment with interactivity**: Try hvPlot on your own visualisations

## Further resources

See the [Introduction notebook](Introduction.ipynb) for comprehensive resources, including:

- Official hvPlot and HoloViz documentation
- Visualisation design books and articles
- Interactive plotting tutorials
- Dashboard design principles

## Connection to assessment

The techniques in Week 08 are particularly valuable for:

- **Week 09**: Application to your individual project visualisations
- **Individual project**: Creating sophisticated, publication-ready figures
- **Presentations**: Interactive plots for engaging stakeholders
- **Higher marks**: Demonstrating advanced technical skills

Mastering Week 08 content will enable you to:
- Create comprehensive multi-panel figures for reports
- Build interactive dashboards for presentations
- Communicate complex findings clearly
- Demonstrate professional visualisation skills

## Getting help

- **Moodle Q&A Forum**: Ask questions about concepts or exercises *(please ...)*
- **Office Hours**: For detailed explanations and design guidance
- **Week 07 Materials**: Review if you're struggling with basic plotting
- **Documentation**: hvPlot, Seaborn, and Matplotlib official docs

## Next steps

After completing Week 08:

1. **Week 09**: Apply these techniques to your individual project
2. **Practice**: Create advanced visualisations for your analysis
3. **Explore**: Experiment with interactive features for your presentation
4. **Prepare**: Week 09 provides dedicated time for creating project visualisations

---

**Week structure**: Teaching week (Week 07 = basic, Week 08 = advanced, Week 09 = application)
