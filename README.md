# Teaching Materials Repository

This repository contains teaching materials for various modules taught at Royal Holloway, University of London.

## Repository Structure

```
Teaching/
├── 2025-26/           # Academic year 2025-26
│   └── MN5813/        # Python Programming & Data Analysis
├── .claude/           # Claude Code configuration
└── .gitignore         # Git ignore patterns
```

## Modules

### 2025-26

#### MN5813 - Python Programming & Data Analysis

An introductory module covering Python programming fundamentals, data analysis with Pandas, and data visualization. The module is structured into weekly sessions with comprehensive Jupyter notebooks.

**Module structure:**
- **Setup**: Environment setup and installation instructions
- **Week01**: Python Fundamentals (strings, lists, dictionaries, functions)
- **Week02**: Advanced Python (list comprehensions, functional programming, error handling)
- **Week03**: Assessment Overview
- **Week04**: Introduction to Pandas (DataFrames, Series, data manipulation)
- **Week05**: Data Analysis with Pandas (grouping, aggregation, merging)
- **Week06**: Group Project Application Week
- **Week07-08**: Data Visualization
- **Week09-11**: Revision and Practice

**Each week typically includes:**
- `Introduction.ipynb`: Learning objectives and overview
- `Demonstration.ipynb`: Worked examples and explanations
- `Exercises.ipynb`: Practice problems for students
- `Solutions.ipynb`: Complete solutions with detailed explanations
- `README.md`: Week overview and structure
- `assets/`: Supporting files (data, images, resources)

See [2025-26/MN5813/README.md](2025-26/MN5813/README.md) for full module details.

## Getting Started

### For Students

1. Navigate to your module directory (e.g., `2025-26/MN5813/`)
2. Follow the Setup instructions in the module's README
3. Work through materials week by week, starting with `Introduction.ipynb`
4. Complete exercises independently before checking solutions

### For Instructors

This repository uses:
- **Jupyter Notebooks** for interactive teaching materials
- **Git** for version control and collaboration
- **Claude Code** for AI-assisted content development and maintenance

## Content Development

Teaching materials in this repository are developed using:
- Original content by module instructors
- AI assistance from [Claude AI](https://claude.ai/) (Claude 3.5 Sonnet)
- Further refinements using [Claude Code](https://www.anthropic.com/claude-code) (Opus 4.1/Sonnet 4.5)

All AI-generated contributions are reviewed and edited by qualified instructors to ensure accuracy and pedagogical quality.

## File Organization Standards

**Data Files:**
- All data files should be organized in `assets/data/` subdirectories
- Input data files should be documented in a `README.md` within the data directory
- Generated/output files should be clearly marked in documentation

**Notebooks:**
- Follow consistent naming: Introduction, Demonstration, Exercises, Solutions
- Include attribution notes in notebook headers
- Use clear cell-level comments for code examples
- Mark supplementary content clearly

## Contributing

For contributions or corrections:
1. Create a new branch for your changes
2. Follow the existing module structure and naming conventions
3. Test all notebook cells before committing
4. Update relevant README files
5. Submit a pull request with a clear description of changes

## License

These teaching materials are © Royal Holloway, University of London. All rights reserved.

Materials are provided for educational purposes only.