# Teaching Materials Best Practices Guide

This document outlines core principles for creating and maintaining teaching materials for MN5813 and other modules. It serves as a reference when developing or updating course content.

**For detailed templates, checklists, and formatting rules**, use the specialized commands:
- `/teaching_templates` - Commit message, notebook, and README templates
- `/teaching_checklist` - Development workflow and quality control checklists
- `/teaching_formatting` - Detailed markdown and code formatting rules
- `/teaching_progression` - Content progression and module structure standards
- `/teaching` - Load all detailed guides at once (comprehensive mode)

---

## Repository Structure

### Folder Organisation

```
2025-26/
├── MN5813/
│   ├── README.md                    # Module overview and weekly summary
│   ├── Setup/
│   │   ├── README.md                # Week summary
│   │   ├── Introduction.ipynb       # Key principles and further readings
│   │   ├── Demonstration.ipynb      # Hands-on demonstrations
│   │   ├── Exercises.ipynb          # 90-minute practice exercises
│   │   ├── Solutions.ipynb          # Simple + advanced solutions
│   │   └── assets/data/             # Week-specific data files
│   ├── Week01/
│   │   ├── README.md
│   │   ├── Introduction.ipynb
│   │   ├── Demonstration.ipynb
│   │   ├── Exercises.ipynb
│   │   ├── Solutions.ipynb
│   │   └── assets/data/
│   └── ...
├── tutorials/                       # VIDEO TUTORIAL SCRIPTS (NOT IN GIT)
│   ├── Setup-Demonstration.md       # Script for Setup/Demonstration video
│   ├── Week01-Demonstration.md      # Script for Week01/Demonstration video
│   └── ...
└── README.md                        # Year overview with all module links
```

### Git Exclusions

The following must be excluded from Git (add to `.gitignore`):
- `tutorials/` - Video tutorial scripts remain local
- `.claude/` - Already excluded by default

---

## Attribution and Acknowledgements

### Canonical acknowledgement text

All notebooks and README files must include acknowledgement of AI assistance. Use the appropriate version below based on authorship.

#### For notebooks originally compiled by Alex Reppel

```markdown
Note: This Jupyter Notebook was originally compiled by Alex Reppel (AR) based on conversations with [ClaudeAI](https://claude.ai/) *(version 3.5 Sonnet)*. For this year's materials, further revisions were made using [Claude Code](https://www.anthropic.com/claude-code) *(Sonnet 4.5)*, including updated documentation and git commit messages.
```

#### For notebooks with multiple authors

```markdown
Note: This Jupyter Notebook was originally written by [Author Name] ([Initials]); it was reformatted and expanded by Alex Reppel (AR) based on conversations with [ClaudeAI](https://claude.ai/) *(version 3.5 Sonnet)*. For this year's materials, further revisions were made using [Claude Code](https://www.anthropic.com/claude-code) *(Sonnet 4.5)*, including updated documentation and git commit messages.
```

### Placement

**In Jupyter notebooks**:
- Place in the **second markdown cell** (after the title/description cell)
- Use italic text for the introductory description in the first cell
- Format as a "Note:" paragraph

**In README files**:
- Place in an "Attribution" or "Acknowledgements" section near the end
- Use standard paragraph formatting

### Updating the model version

When Claude Code is updated:
1. Update this section in CLAUDE.md with the new model version
2. Update all notebook acknowledgements to match
3. Document the change in git commit messages

---

## Pedagogical Delivery Model

### Session Structure

**Actual available time**:
- Workshop: 105 minutes (120min session - 5min setup - 10min leaving early)
- Lecture: 45 minutes

**Weekly cycle (Option 2 - Flipped Classroom)**:

1. **Week N Lecture (45 minutes)** - Introduces Week N+1 content
   - 20-25 minutes: Present Introduction notebook (concepts, objectives, prerequisites)
   - 15-20 minutes: Discussion, questions, connections to previous weeks
   - Assign: "Work through Demonstration notebook for Week N+1 before workshop" (optional but strongly recommended)

2. **Pre-Workshop Self-Study (60-75 minutes)** - Students work through Demonstration at own pace
   - Self-paced walkthrough of Demonstration notebook
   - Students run code cells, experiment with examples, take notes
   - Core content clearly marked (essential techniques for exercises)
   - Supplementary content clearly marked (optional deeper exploration)
   - Not mandatory before workshop (instructor covers key techniques live as needed)

3. **Week N+1 Workshop (105 minutes)** - Hands-on practice
   - 5 minutes: Quick recap, answer Demonstration questions
   - 90 minutes: Exercises (guided practice with instructor support)
   - 10 minutes: Wrap-up, preview next week

### Content Time Standards

**Introduction notebooks**:
- Reading time: 20-30 minutes
- Presentation time: 20-25 minutes (leaves 20min for discussion in 45min lecture)
- Content: Conceptual foundations, learning objectives, prerequisites, preview examples

**Demonstration notebooks**:
- Self-study target: 60 minutes (max 75 minutes for complex topics like Week 04/05)
- **Must clearly mark**: Core content vs Supplementary content using markdown headings
- Core content (essential): 50-60 minutes - techniques needed for exercises
- Supplementary content (optional deeper exploration): remaining content

**Exercises notebooks**:
- Time budget: 90 minutes
- Structure: 5-6 parts with progressive difficulty
- Design: Business scenarios, clear instructions, time estimates per part

**Solutions notebooks**:
- Review time: 30 minutes
- Must use ONLY techniques from Demonstration
- Simple solution first, advanced alternatives only if taught in Demo

---

## Notebook Structure Standards

### Critical requirement: All notebooks must execute successfully

**IMPORTANT**: All notebook files must run from top to bottom without throwing errors. This is essential because:
- Notebooks are compiled into the module handbook using bookdown/R
- Students expect to be able to run demonstration code successfully
- Broken code creates confusion and undermines learning

**Showing errors for pedagogical purposes**:
If you need to demonstrate an error or common mistake:
1. **Comment out the error-causing code**
2. **Explain the error in a markdown cell**
3. **Show the fixed version that runs successfully**

**Code examples in Markdown cells vs. Code cells**:

**Markdown cells** (for non-executable examples):
- **Always use `{python, eval=FALSE}`** for Python code examples that are meant to illustrate concepts
- **Never use `python`** in Markdown cell code blocks (causes compilation errors)
- Use plain ` ``` ` for folder structures, terminal output, or text examples
- **Purpose**: Show syntax/patterns without executing (e.g., showing an alternative approach, explaining a concept)

**Code cells** (for executable code):
- **NEVER add `eval=FALSE` metadata to Code cells** unless it's truly a non-executable example
- **CRITICAL**: If a Code cell creates variables or modifies state, it MUST execute during handbook build
- **Rule**: If later cells depend on this cell's output, it MUST NOT have `eval=FALSE` metadata
- **When to use eval=FALSE in Code cells**: ONLY for isolated examples that demonstrate errors or alternative patterns

**Common mistake to avoid**:
```
❌ BAD: Code cell with eval=FALSE that creates variables used later
Cell 1 (Code, eval=FALSE): df["new_column"] = ...
Cell 2 (Code): print(df["new_column"])  # KeyError! Column doesn't exist

✓ GOOD: Code cell executes and creates variables
Cell 1 (Code): df["new_column"] = ...
Cell 2 (Code): print(df["new_column"])  # Works correctly
```

**See `/teaching_formatting` for detailed guidance**

### Notebook Purposes

**1. Introduction.ipynb**:
- Explain key concepts and principles with basic code examples
- Include Further Resources section (academic readings, videos, documentation)
- Focus on "why" rather than "how"
- Time: 20-30 minutes reading

**2. Demonstration.ipynb**:
- Hands-on demonstrations with detailed explanations
- Reference previous sessions early
- Progressive complexity (simple → intermediate)
- Business-focused examples
- **Must have corresponding tutorial script** in `tutorials/` folder
- Time: 60-75 minutes self-study

**3. Exercises.ipynb**:
- 90-minute self-study practice exercises
- 5-6 parts with time estimates
- Business scenarios (not foo/bar examples)
- Clear instructions, hints, starter code

**4. Solutions.ipynb**:
- Clear solutions with explanations
- **CRITICAL**: Use ONLY techniques from Demonstration
- Always provide simplest solution first
- Advanced alternatives only if taught in Intro/Demo

**For detailed notebook templates**, use `/teaching_templates`.

### Alternative notebook types

- **Resources.ipynb**: Optional advanced content beyond core objectives
- **Installation.ipynb**: Setup instructions for software/libraries
- **Template.ipynb**: Starting point for student project work

**Guidelines**:
- Must have clear purpose stated in first cell
- Should be referenced in week's README.md
- Use same attribution and formatting standards

---

## Language and Style

### British English
All materials must use British English throughout:
- Spelling: "organise" (not "organize"), "colour" (not "color"), "analyse" (not "analyze")
- Terminology: "whilst" acceptable, "programme" for course, "program" for code
- Date format: DD/MM/YYYY or "1 January 2025"

### Voice and Tone
- **Encouraging**: "You'll be able to...", "Let's explore..."
- **Clear and direct**: Avoid jargon unless explained
- **Professional but approachable**: Neither too formal nor too casual
- **Active voice**: "We'll create..." rather than "A dictionary will be created..."

### Common Phrases
- "In this notebook, we'll..." (opening)
- "Building on what we learnt in..." (references)
- "Let's explore..." (introducing new concept)
- "Note that..." (highlighting important points)
- "You'll practise this in the exercises" (transitions)

### Core Formatting Standards

**Headings**:
- Use sentence case, not Title Case
- H1 for notebook title only, H2 for major sections, H3 for subsections
- Exception: Proper nouns and acronyms remain capitalised

**Quote style**:
- Always use double quotes (`"`) for outer strings
- Use single quotes within strings to avoid escaping
- **CRITICAL**: Do not use double quotes within double quotes (causes syntax errors)

**Lists**:
- Use `-` (hyphen) for consistency
- Indent with 2 spaces for nested lists

**Code**:
- Always specify language in code blocks for Code Cells (` ```python `)
- In Markdown cells, use `{python, eval=FALSE}` for examples (not `python`)
- Use plain ` ``` ` for folder structures and non-code monospace text
- Use inline code for function/variable names

**For detailed formatting rules**, use `/teaching_formatting`.

---

## Pedagogical Principles

### 1. Scaffolded Learning
- Each week builds explicitly on previous weeks
- Always reference prerequisites at the start of Introduction and Demonstration
- Show the progression: Setup → Week 1 → Week 2 → ...
- Exercises should mix review (30%) with new content (70%)

### 2. Business Context
All examples should use business scenarios:
- **Retail**: Product catalogues, inventory, sales transactions
- **Marketing**: Campaign spend, conversion rates, customer segments
- **Finance**: Revenue, costs, pricing, discounts
- **Operations**: Customer satisfaction, performance metrics
- **HR/CRM**: Employee data, customer databases

Avoid generic "foo/bar" or abstract mathematical examples.

### 3. Active Learning
- Demonstration notebooks should invite students to run and modify code
- Include prompts like "Try changing the value to..." or "What happens if...?"
- Exercises should encourage experimentation
- Solutions should explain the thinking process, not just show answers

### 4. Progressive Complexity

**Within each notebook**:
- Start with simplest case
- Add one complication at a time
- Build to realistic complexity
- End with integration of multiple concepts

**Across weeks**:
- Early weeks: Single concepts, explicit code
- Middle weeks: Combining concepts, introducing efficiency
- Later weeks: Complex problems requiring synthesis

### 5. Real-World Data Skills

**Data quality teaching**:
- Introduce "messy" data with intentional issues (missing values, outliers, duplicates)
- Document data issues in data README files
- Teach students to identify and handle these issues

**Best practices**:
- Use realistic datasets
- Show validation and error checking
- Teach defensive programming
- Encourage documentation of data cleaning decisions

---

## Data & Exercise Design

### Synthetic Dataset Creation

**Dataset characteristics**:
1. **Realistic volume**: 10-50 rows (early), 100-500 rows (mid), 1000+ rows (later)
2. **Business relevance**: Reflect actual business metrics
3. **Data quality issues** (intentional): 5-10% missing, 2-3% outliers, 1-2% duplicates
4. **Documentation**: Create README.md in data folders with column definitions

### Exercise Design

**90-Minute Time Budget**:
- Part 1 (15 mins): Warm-up with familiar concepts
- Parts 2-4 (20 mins each): Core new skill practice
- Part 5 (10 mins): File handling or output
- Bonus (5 mins): Optional challenge

**Difficulty progression**:
- Exercises 1-3: Guided (detailed instructions, hints, starter code)
- Exercises 4-7: Semi-guided (clear instructions, minimal hints)
- Exercises 8-12: Independent (brief description, students design approach)
- Bonus: Challenge (requires synthesis or extension)

**File path conventions**:
- Reading: `assets/data/sales_data.txt` (provided)
- Writing: `assets/data/output.txt` (created)

**For detailed exercise scaffolding patterns**, use `/teaching_formatting`.

---

## Version Control & Workflow

### Before Committing

**Checklist for any notebook update**:
1. **Run all cells** to ensure no errors
2. **Clear all outputs** (for cleaner git diffs, optional but recommended for Exercises)
3. **Check cross-references**: Are references to previous weeks accurate?
4. **Verify file paths**: Do all data file references work?
5. **British English**: Run a spell check
6. **For Demonstration notebooks**: Review and update corresponding tutorial script

### Git Commit Messages

**Use the enhanced three-section format**:
1. **What was changed** (3-5 high-level bullet points)
2. **Claude Code contributions** (what AI did)
3. **Manual edits** (verification and human changes)

**Structure**:
```
type(scope): brief description

What was changed:
- High-level summary point 1
- High-level summary point 2

Claude Code contributions:
- What Claude Code specifically did
- Files created, modified, or restructured

Manual edits:
- Human modifications after AI assistance
- Verification steps performed

🤖 Generated with Claude Code (https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
```

**Conventional commit types**: feat, fix, docs, refactor, style, chore

**For detailed commit message templates**, use `/teaching_templates`.

---

## Common Patterns & Anti-Patterns

### ✅ DO

- **Reference previous sessions**: "Building on string manipulation from Setup..."
- **Provide context**: "In business analytics, we often need to..."
- **Show progression**: Simple example → Complex example
- **Explain outputs**: Don't just show code, explain what it does
- **Use realistic data**: Business scenarios with actual metrics
- **Time your exercises**: Ensure 90-minute target is realistic
- **Update tutorial scripts**: Keep them in sync with Demonstration notebooks
- **Test all code**: Run every cell before committing
- **Document data**: Create README files for all datasets

### ❌ DON'T

- **Don't use abstract examples**: Avoid "foo", "bar", mathematical abstractions
- **Don't skip prerequisites**: Always state what students need to know first
- **Don't show advanced techniques without teaching**: Solutions should only use taught concepts
- **Don't neglect time estimates**: Students need to know how long exercises take
- **Don't forget British English**: Consistency matters
- **Don't commit without reviewing**: Check tutorial scripts for Demonstrations
- **Don't create orphaned content**: Ensure all weeks link properly in README files
- **Don't ignore data quality**: Use realistic messy data for teaching

### Common Mistakes in Teaching Materials

1. **Assuming knowledge**: Always state prerequisites explicitly
2. **Too much in one go**: Break complex topics into smaller steps
3. **Inconsistent terminology**: Use the same terms across all notebooks
4. **Missing explanations**: Every code example needs context
5. **Unrealistic time estimates**: Test exercises yourself for timing
6. **Forgetting the learning path**: Each week should build on previous weeks clearly

**For detailed quality control checklist**, use `/teaching_checklist`.

---

## Updating This Guide

This guide should evolve based on:
- Teaching experience and student feedback
- New pedagogical approaches
- Changes in Python best practices
- Module requirements updates

When updating:
1. Document the reason for the change
2. Update examples to reflect new guidance
3. Review existing materials for consistency
4. Consider impact on tutorial scripts
5. Update version in changelog

---

## Quick Reference

### Starting a New Week

1. Create week folder with README.md
2. Create 4 notebooks: Introduction → Demonstration → Exercises → Solutions
3. Create `assets/data/` folder if data files needed
4. Create tutorial script in `tutorials/[Week]-Demonstration.md`
5. Update year-level README with week link
6. Update module README with week summary

**For detailed 10-phase checklist**, use `/teaching_checklist`.

### Before Committing Notebooks

1. **CRITICAL: Use "Restart Kernel and Run All Cells"** - Must execute without errors
2. Verify error demonstrations are properly commented out
3. Run Quality Control Checklist (use `/teaching_checklist`)
4. Verify acknowledgement text matches canonical version
5. Check all cross-references and links work
6. For Demonstrations: Update corresponding tutorial script
7. Remove any empty cells
8. Verify file paths consistent between Exercises and Solutions
9. Draft commit message (use `/teaching_templates`)

### Writing Commit Messages

Quick checklist:
- [ ] Conventional commit type and scope
- [ ] "What was changed" section (3-5 points)
- [ ] "Claude Code contributions" section
- [ ] "Manual edits" section
- [ ] AI acknowledgement footer (🤖 + Co-Authored-By)

**For full templates**, use `/teaching_templates`.

### Core Formatting

- **Headings**: Sentence case (not Title Case)
- **Quotes**: Double quotes for strings, single quotes within strings
- **Lists**: Use `-` consistently
- **Code**: Always specify language (` ```python `)

**For detailed formatting standards**, use `/teaching_formatting`.

---

## Detailed Guides

For comprehensive reference material, use these commands:

- **`/teaching_templates`** - Commit message, notebook, and README templates
  - 5 detailed commit message templates
  - Notebook section templates (Introduction, Demonstration, Exercises, Solutions)
  - README templates (week-level, module-level, year-level)
  - Video tutorial script template

- **`/teaching_checklist`** - Development workflow and quality control checklists
  - Week Development Checklist (10-phase workflow)
  - Quality Control Checklist (content, formatting, pedagogical, cross-referencing)
  - Before Committing Notebooks checklist
  - Content Progression Validation Checklist

- **`/teaching_formatting`** - Detailed markdown and code formatting rules
  - Comprehensive Markdown Formatting Standards
  - Exercise Scaffolding Patterns
  - Code Style Standards (Python teaching conventions)
  - Cross-referencing and Linking patterns

- **`/teaching_progression`** - Content progression and module structure standards
  - Module Learning Progression (4-phase structure)
  - Week Type Patterns (Standard, Setup, Assessment, Application)
  - Cross-Referencing Requirements (templates and examples)
  - Content Progression Standards (Setup→Week01→Week02)
  - Session Timing Standards
  - Library Hyperlinking Standards

- **`/teaching`** - Load all detailed guides at once (comprehensive mode)

---

## Support & Questions

For questions about these guidelines or teaching materials:
- Refer to existing notebooks for examples
- Check this guide for standards
- Use `/teaching_*` commands for detailed reference
- Review recent commits for patterns
- Consult module documentation

---

**Last updated**: 25 October 2025
**Version**: 1.6.0

**Changelog**:

- **v1.6.0** (25 Oct 2025):
  - **Modular Architecture**: Refactored 2,582-line CLAUDE.md into streamlined core (~1,000 lines) + 4 detailed slash command skills
  - Created `/teaching_templates` - Commit message, notebook, README templates
  - Created `/teaching_checklist` - Development workflow and quality control checklists
  - Created `/teaching_formatting` - Detailed markdown and code formatting rules
  - Created `/teaching_progression` - Content progression and module structure standards
  - Updated `/teaching` command to load all detailed guides comprehensively
  - Removed `/teaching_view` and `/teaching_edit` (redundant with new structure)
  - Improved maintainability and reduced cognitive load
  - Core principles auto-loaded; detailed reference available on-demand

- **v1.5.1** (24 Oct 2025):
  - Quote Style Clarification: Enhanced quote style rules prohibiting double quotes within double quotes

- **v1.5** (21 Oct 2025):
  - Session Timing Standards
  - Library Hyperlinking Standards
  - Module Learning Progression (4-phase)
  - Week Type Patterns documentation
  - Cross-Referencing Requirements
  - Content Progression Standards (Setup→Week01→Week02)

- **v1.4** (21 Oct 2025):
  - Option 2 Pedagogical Model (Demonstrations as self-study)
  - Week Development Checklist (10-phase workflow)
  - Core/Supplementary Content Marking

- **v1.3** (21 Oct 2025):
  - Enhanced Git Commit Messages with structured templates

- **v1.2** (21 Oct 2025):
  - Requirement: All notebooks must execute successfully
  - Exercise Scaffolding Patterns
  - Quality Control Checklist

- **v1.1** (21 Oct 2025):
  - Comprehensive Markdown Formatting Standards

- **v1.0** (21 Oct 2025):
  - Initial version
