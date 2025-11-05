# Week 09: Data Visualisation Practice (Individual Project Workshop)

## Overview

Week 09 is an application week where you apply the visualisation skills from Weeks 07 and 08 to your individual project. This week bridges the gap between learning visualisation techniques and implementing them in your assessment.

## The 3-week learning block

This week completes the data visualisation learning block:

- **Week 07**: Basic visualisation principles (plot types, Pandas/Matplotlib/Seaborn)
- **Week 08**: Advanced visualisation techniques (small multiples, interactive plots, dashboards)
- **Week 09**: Application to your individual project ← **You are here**

## Week structure

Unlike previous teaching weeks, Week 09 focuses on **application and practice**:

- **No new concepts** – consolidate what you've learnt
- **No exercises notebook** – you'll work on your actual project
- **Demonstration as reference** – worked example you can adapt
- **Individual project time** – apply techniques to your dataset

## Materials

### Notebooks

1. **[Introduction.ipynb](Introduction.ipynb)** – Application week overview, workflow, and common challenges
2. **[Demonstration.ipynb](Demonstration.ipynb)** – Complete visualisation workflow example

### Data files

Located in `assets/data/`:

- **retail_sales.csv** – Demonstration dataset used in Demonstration notebook
- Sample data files demonstrating different data structures

## Your individual project

### Dataset requirements

- Your chosen dataset (different from group project)
- Minimum 1000 rows
- Multiple numerical and categorical variables
- Suitable for answering analytical questions

### Visualisation requirements

Your individual report should include:

1. **Exploratory visualisations**
   - Distributions of key variables
   - Relationships between variables
   - Patterns and trends over time (if applicable)

2. **Analytical visualisations**
   - Supporting your research questions
   - Comparisons across groups or categories
   - Evidence for your conclusions

3. **Quality standards**
   - Clear, readable labels and titles
   - Appropriate chart types for data and message
   - Consistent styling throughout report
   - Accessible colour schemes (colourblind-friendly)
   - Professional presentation

See your individual project brief for complete requirements and marking criteria.

## Prerequisites

Effective visualisation requires well-prepared data:
- **Week 04-05**: Data cleaning, reshaping, and aggregation with Pandas
- **Week 06**: Application workflow from group project
- **Week 07-08**: Visualisation techniques learned in previous weeks

## How to use Week 09 materials

### The demonstration workflow

The Demonstration notebook shows a **complete visualisation workflow** from data loading through to final publication-ready figures:

1. Data loading and preparation
2. Exploratory visualisations
3. Analytical visualisations
4. Multi-panel figures
5. Polish and finalize
6. Interactive visualisations (optional)

### Workflow

1. **For your project**: Work in your individual project notebook
2. **For guidance**: Reference Week09/Demonstration.ipynb workflow
3. **For techniques**: Review Week07 and Week08 materials as needed

## Recommended session workflow

### Before the session (30-45 minutes)

**Review your data and analysis** (15 min)
- What are your key findings?
- What patterns have you identified?
- What comparisons are important?

**Plan your visualisations** (15 min)
- List questions each visualisation will answer
- Choose appropriate chart types
- Sketch rough layouts

**Review Week 07-08 techniques** (10 min)
- Identify which techniques you'll need
- Note any customisations required
- Prepare code snippets to adapt

### During the session (105 minutes)

**Phase 1: Create exploratory visualisations** (30 min)
- Quick plots to understand your data
- Test different chart types
- Identify what works and what doesn't
- Reference: Week 07 Demonstration, Week 09 Demonstration Part 2

**Phase 2: Build presentation visualisations** (45 min)
- Refine your best exploratory plots
- Add professional styling
- Ensure clear labels and titles
- Test different colour schemes
- Reference: Week 09 Demonstration Part 3

**Phase 3: Create integrated figures** (20 min)
- Combine related visualisations
- Design multi-panel figures
- Ensure consistent styling
- Reference: Week 08 Demonstration, Week 09 Demonstration Part 4

**Phase 4: Review and refine** (10 min)
- Check for clarity and accuracy
- Verify all labels and legends
- Test colour accessibility
- Export at appropriate resolution

### After the session (60-90 minutes)

**Get feedback**
- Share with peers or instructor
- Ask specific questions about clarity
- Consider alternative perspectives

**Make final refinements**
- Address feedback points
- Fine-tune colours and fonts
- Ensure consistency across all figures

**Prepare for report**
- Export in appropriate formats (PNG 300 DPI, PDF)
- Document data sources
- Write captions for each figure
- Organise files systematically

## Common challenges

### Challenge 1: Choosing the right chart type

**Problem**: Unsure which visualisation best shows your data.

**Solutions**:
- **For trends over time**: Line plots
- **For comparing categories**: Bar charts
- **For distributions**: Histograms or box plots
- **For relationships**: Scatter plots
- **For parts of whole**: Stacked bars (avoid pie charts)
- **For many variables**: Small multiples or heatmaps

Reference: Week 09 Introduction, Section 5 (Common challenges)

### Challenge 2: Colour schemes and accessibility

**Problem**: Choosing colours that look good and are accessible.

**Solutions**:
- Use colourblind-friendly palettes (Seaborn default, ColourBrewer)
- Avoid red-green combinations alone
- Use patterns or shapes in addition to colours
- Test with colourblind simulators
- Maintain sufficient contrast

Reference: Week 07 Best practices, Week 09 Introduction

### Challenge 3: Interactive vs static visualisations

**Problem**: Deciding when to use interactive plots.

**Solutions**:
- **Use static for**: Reports, presentations, publications (required for your report)
- **Use interactive for**: Exploration, stakeholder meetings, online dashboards
- **Tip**: Create both versions - static for report, interactive for demo

Reference: Week 08 Interactive visualisation, Week 09 Demonstration Part 6

### Challenge 4: Figure sizing and resolution

**Problem**: Figures too small, pixelated, or poorly sized.

**Solutions**:
- Set figure size before creating plot: `plt.figure(figsize=(10, 6))`
- Save at high DPI: `plt.savefig('figure.png', dpi=300, bbox_inches='tight')`
- Use vector formats when possible: `.pdf` or `.svg`
- Consider final placement (full page, half page, inline)

Reference: Week 09 Demonstration Part 5

### Challenge 5: Combining multiple visualisations

**Problem**: Creating coherent multi-panel figures.

**Solutions**:
- Use consistent colour schemes across panels
- Maintain similar font sizes and styles
- Align axes where comparable
- Use subplots effectively
- Add overall title and panel labels (A, B, C, D)

Reference: Week 08 Multi-panel figures, Week 09 Demonstration Part 4

## Stretch goals (advanced techniques)

Once core visualisations are complete:

- **Interactive dashboards**: Combine multiple hvPlot visualisations with filters
- **Animated visualisations**: Show changes over time with animations
- **Custom styling**: Create custom Matplotlib stylesheets and colour palettes
- **Publication-quality**: Export in vector formats, match journal requirements

Reference: Week 09 Introduction (Stretch goals section)

## Time commitment

**Note**: This module uses 60-minute lecture slots and 2-hour workshop slots. The timings below show how content fits within these sessions, allowing time for discussion and questions.

- **Introduction**: 20-30 minutes (presented in 45-minute lecture, which fits comfortably in the 60-minute slot)
- **Demonstration**: 60-90 minutes (self-study notebook, work through before workshop)
  - Complete visualisation workflow example
  - Reference material for adapting to your project
  - Run code cells, see how techniques apply to similar analysis
- **Workshop**: 90 minutes (individual project work with instructor support, fits comfortably in the 2-hour workshop slot)
- **Follow-up work**: Variable (depends on project progress and requirements)

**Session structure**:
- Lecture: 45 minutes (introduces subsequent content or revision)
- Workshop: 105 minutes (includes setup time and early departure)

**Total in-session**: 2.5-3 hours
**Total with follow-up**: Variable based on project needs

## Recommended workflow

1. **Attend lecture** (45 min) - Introduction to subsequent topics or revision session
2. **Work through Demonstration** (60-90 min) - Before workshop (see complete workflow example)
   - Run all code cells with retail sales data
   - Identify which techniques apply to your project
   - Note customisation approaches
3. **Attend workshop** (105 min) - Apply techniques to your individual project
4. **Complete individual work** (variable) - Finish remaining visualisations outside session

## Connection to assessment

### Individual analytics report (80%)

Week 09 provides:
- Structured approach to creating project visualisations
- Example workflow you can adapt
- Best practices for publication-quality figures
- Professional visualisation techniques

Your visualisations should:
- Support your analytical narrative
- Answer specific research questions
- Demonstrate technical skills
- Follow design best practices
- Be properly integrated in your report

## Getting help

- **In-session support**: Use session time to ask questions
- **Moodle Q&A Forum**: Post challenges and solutions
- **Office hours**: Detailed guidance on approaches
- **Demonstration notebook**: Complete workflow example for reference
- **Week 07/08 materials**: Technical reference for techniques

## Further resources

### Design principles
- [Storytelling with Data](http://www.storytellingwithdata.com/) by Cole Nussbaumer Knaflic
- [The Visual Display of Quantitative Information](https://www.edwardtufte.com/tufte/books_vdqi) by Edward Tufte
- [Data Visualisation Guide](https://www.tableau.com/learn/articles/data-visualization) by Tableau

### Colour tools
- [ColourBrewer](https://colourbrewer2.org/) - Cartography colour schemes
- [Adobe Colour](https://colour.adobe.com/) - Colour palette generator
- [Coolors](https://coolors.co/) - Colour scheme generator
- [Coblis](https://www.colour-blindness.com/coblis-colour-blindness-simulator/) - Colourblind simulator

### Technical references
- [Matplotlib Gallery](https://matplotlib.org/stable/gallery/index.html) - Example plots
- [Seaborn Gallery](https://seaborn.pydata.org/examples/index.html) - Statistical plots
- [Python Graph Gallery](https://www.python-graph-gallery.com/) - Comprehensive examples

## Next steps

After Week 09:

1. **Complete individual project visualisations**: Polish and finalize figures
2. **Integrate into report**: Add visualisations with proper captions
3. **Write supporting text**: Explain what each visualisation shows
4. **Review and polish**: Check consistency, clarity, accessibility
5. **Finalize submission**: Ensure all requirements met before deadline

---

**Week structure**: Application week (Week 07 = basic, Week 08 = advanced, Week 09 = application)

**Important**: Use Week 09 session time to work on your actual project visualisations, use Demonstration as a reference guide
