---
description: Generate module handbook with comprehensive testing and intelligent error tracing
---

# Generate Module Handbook

This command generates a module handbook with comprehensive pre-build testing, intelligent error tracing, and version management.

---

## What This Command Does

1. **Environment Detection**: Extracts year and module code from current working directory
2. **Version Management**: Prompts for version number, tracks build history
3. **Comprehensive Notebook Testing**: Tests ALL notebooks for the module (100% pass required)
4. **Handbook Build**: Executes build script if tests pass
5. **Intelligent Error Tracing**: If build fails, traces errors to specific notebook cells
6. **Version Tracking**: Updates `.claude/handbook_version.json` with build results

---

## Expected Outcomes

- **All notebooks execute successfully** (100% pass rate required)
- **Handbook builds successfully** (only if notebooks pass)
- **Version tracking updated** with build results
- **Specific error guidance** if build fails (traced to notebook/cell)

---

## Usage

Run this command from the module directory (e.g., `2025-26/MN5813/`):

```bash
/teaching_generate_handbook
```

You will be prompted to enter the handbook version (e.g., "2.2", "3.0").

---

## How It Works

### Phase 1: Environment Detection

**Extract year and module from current working directory**:

```python
import os
import re

# Get current working directory
cwd = os.getcwd()

# Extract year (pattern: YYYY-YY, e.g., "2025-26")
year_match = re.search(r"(\d{4}-\d{2})", cwd)
if not year_match:
    print("ERROR: Could not extract year from working directory")
    print(f"Current directory: {cwd}")
    print("Expected pattern: .../2025-26/MN5813")
    exit(1)
year = year_match.group(1)

# Extract module code (pattern: [A-Z]{2}[0-9]{4}, e.g., "MN5813")
module_match = re.search(r"([A-Z]{2}\d{4})", cwd)
if not module_match:
    print("ERROR: Could not extract module code from working directory")
    print(f"Current directory: {cwd}")
    print("Expected pattern: .../2025-26/MN5813")
    exit(1)
module = module_match.group(1)

print(f"Detected environment: {year}/{module}")
```

**Construct handbook directory path**:

```python
# Convert GitHub path to OneDrive Teaching path
# From: ~/OneDrive/Shared/GitHub/Teaching/2025-26/MN5813
# To:   ~/OneDrive/Teaching/2025-26/Modules/MN5813/Handbook
home = os.path.expanduser("~")
handbook_dir = f"{home}/OneDrive/Teaching/{year}/Modules/{module}/Handbook"

if not os.path.exists(handbook_dir):
    print(f"ERROR: Handbook directory does not exist")
    print(f"Expected: {handbook_dir}")
    exit(1)

print(f"Handbook directory: {handbook_dir}")
```

### Phase 2: Version Management

**Load version tracking file**:

```python
import json
from datetime import datetime

version_file = f"{home}/OneDrive/Shared/GitHub/Teaching/.claude/handbook_version.json"

# Load existing version data
if os.path.exists(version_file):
    with open(version_file, "r") as f:
        version_data = json.load(f)
else:
    version_data = {}

# Get current version for this module
current_version = version_data.get(module, {}).get("current_version", "1.0")
print(f"Current handbook version: {current_version}")
```

**Prompt user for new version**:

Use the AskUserQuestion tool to prompt:
- Question: f"What version number should this handbook be? (Current: {current_version})"
- Header: "Version"
- Options:
  - Increment minor (e.g., "2.2" → "2.3")
  - Increment major (e.g., "2.2" → "3.0")
  - Custom (user specifies)

Parse user input and validate version format (X.Y).

### Phase 3: Comprehensive Notebook Testing

**Find all notebooks for the module**:

```python
import glob

# Find all .ipynb files in the module directory
notebook_pattern = f"{cwd}/*/*.ipynb"
notebooks = sorted(glob.glob(notebook_pattern))

# Exclude .ipynb_checkpoints
notebooks = [nb for nb in notebooks if ".ipynb_checkpoints" not in nb]

print(f"Found {len(notebooks)} notebooks to test")
```

**Test each notebook**:

```python
import subprocess
import time

test_results = []
total_time = 0

for i, notebook in enumerate(notebooks, 1):
    # Extract week name for display
    week = os.path.basename(os.path.dirname(notebook))
    nb_name = os.path.basename(notebook)

    print(f"[{i}/{len(notebooks)}] Testing {week}/{nb_name}...", end=" ")

    # Run jupyter nbconvert --execute
    start_time = time.time()
    try:
        result = subprocess.run(
            [
                "jupyter", "nbconvert",
                "--to", "notebook",
                "--execute", notebook,
                "--output", f"{nb_name.replace('.ipynb', '_test.ipynb')}",
                "--ExecutePreprocessor.timeout=180"
            ],
            capture_output=True,
            text=True,
            cwd=os.path.dirname(notebook),
            timeout=200
        )
        elapsed = time.time() - start_time
        total_time += elapsed

        if result.returncode == 0:
            print(f"✓ PASS ({elapsed:.1f}s)")
            test_results.append({
                "notebook": f"{week}/{nb_name}",
                "status": "pass",
                "time": elapsed
            })
            # Clean up test output
            test_output = os.path.join(os.path.dirname(notebook), f"{nb_name.replace('.ipynb', '_test.ipynb')}")
            if os.path.exists(test_output):
                os.remove(test_output)
        else:
            print(f"✗ FAIL ({elapsed:.1f}s)")
            test_results.append({
                "notebook": f"{week}/{nb_name}",
                "status": "fail",
                "time": elapsed,
                "error": result.stderr
            })
    except Exception as e:
        elapsed = time.time() - start_time
        total_time += elapsed
        print(f"✗ ERROR ({elapsed:.1f}s)")
        test_results.append({
            "notebook": f"{week}/{nb_name}",
            "status": "error",
            "time": elapsed,
            "error": str(e)
        })

# Count results
passed = sum(1 for r in test_results if r["status"] == "pass")
failed = sum(1 for r in test_results if r["status"] == "fail")
errors = sum(1 for r in test_results if r["status"] == "error")

print("\n" + "="*60)
print(f"Test Results: {passed} passed, {failed} failed, {errors} errors")
print(f"Total time: {total_time:.1f}s")
print("="*60)
```

**Abort if any tests fail**:

```python
if failed > 0 or errors > 0:
    print("\nERROR: Not all notebooks executed successfully")
    print("\nFailed notebooks:")
    for result in test_results:
        if result["status"] != "pass":
            print(f"  - {result['notebook']}")
            if "error" in result:
                # Show first 5 lines of error
                error_lines = result["error"].split("\n")[:5]
                for line in error_lines:
                    print(f"    {line}")

    print("\nHandbook build ABORTED. Fix failing notebooks first.")
    exit(1)

print("\n✓ All notebooks passed. Proceeding with handbook build...")
```

### Phase 4: Handbook Build

**Execute build script**:

```python
print(f"\nBuilding handbook in {handbook_dir}...")
print("Running: ./Handbook\n")

try:
    build_result = subprocess.run(
        ["./Handbook"],
        capture_output=True,
        text=True,
        cwd=handbook_dir,
        timeout=600  # 10 minutes max
    )

    if build_result.returncode == 0:
        print("✓ Handbook built successfully")
        build_status = "success"
        build_error = None
    else:
        print("✗ Handbook build FAILED")
        build_status = "failed"
        build_error = build_result.stderr

except Exception as e:
    print(f"✗ Handbook build ERROR: {e}")
    build_status = "error"
    build_error = str(e)
```

### Phase 5: Intelligent Error Tracing (If Build Fails)

**Parse error from build output**:

```python
if build_status != "success":
    print("\n" + "="*60)
    print("ERROR ANALYSIS")
    print("="*60)

    # Extract error message
    error_lines = build_error.split("\n")

    # Find the key error line (typically contains "Error in" or "Quitting from lines")
    error_line = None
    error_context = []

    for i, line in enumerate(error_lines):
        if "Quitting from lines" in line or "Error in" in line:
            error_line = line
            # Get surrounding context (5 lines before and after)
            start = max(0, i - 5)
            end = min(len(error_lines), i + 6)
            error_context = error_lines[start:end]
            break

    if error_line:
        print(f"\nKey error: {error_line}")

        # Extract line numbers if present (e.g., "lines 6678-6682")
        line_match = re.search(r"lines? (\d+)(?:-(\d+))?", error_line)
        if line_match:
            error_start_line = int(line_match.group(1))
            error_end_line = int(line_match.group(2) or line_match.group(1))

            print(f"Error occurred at lines {error_start_line}-{error_end_line} in temporary .Rmd file")
```

**Read temporary .Rmd file to trace error**:

```python
            # Read temporary .Rmd file
            temp_rmd = f"{handbook_dir}/__TEMP/{module}-Handbook.Rmd"

            if os.path.exists(temp_rmd):
                print(f"\nReading {temp_rmd} to trace error...")

                with open(temp_rmd, "r") as f:
                    rmd_lines = f.readlines()

                # Get error context from .Rmd
                error_rmd_context = rmd_lines[max(0, error_start_line-1):error_end_line]

                print("\nError context from .Rmd:")
                for i, line in enumerate(error_rmd_context, start=error_start_line):
                    print(f"  {i:4d}: {line.rstrip()}")

                # Trace backwards to find source notebook
                # Look for markdown headers like "# Week 05: ..." or "## Demonstration"
                source_week = None
                source_notebook = None

                for i in range(error_start_line - 1, -1, -1):
                    line = rmd_lines[i]

                    # Check for week marker (e.g., "# Week 05:")
                    week_match = re.search(r"^# (Week \d+|Setup):", line)
                    if week_match:
                        source_week = week_match.group(1)
                        break

                    # Check for notebook type marker
                    nb_match = re.search(r"## (Introduction|Demonstration|Exercises|Solutions)", line)
                    if nb_match:
                        source_notebook = nb_match.group(1)

                if source_week and source_notebook:
                    print(f"\n→ Error likely in: {source_week}/{source_notebook}.ipynb")

                    # Try to map to cell number
                    # Count code chunks from start of notebook section
                    chunk_count = 0
                    for i in range(error_start_line - 1, -1, -1):
                        line = rmd_lines[i]
                        if re.search(r"^```\{python", line):
                            chunk_count += 1
                        if re.search(r"## (Introduction|Demonstration|Exercises|Solutions)", line):
                            break

                    print(f"→ Approximately code chunk #{chunk_count} in that notebook")

                else:
                    print("\n→ Could not determine source notebook automatically")
                    print("   Inspect the .Rmd file manually for context")

            else:
                print(f"\nWARNING: Temporary .Rmd file not found at {temp_rmd}")
                print("Cannot trace error to source notebook")
```

**Suggest fix based on error type**:

```python
        # Parse the actual error message (e.g., KeyError, NameError)
        actual_error = None
        for line in error_context:
            if "Error" in line and ":" in line:
                actual_error = line.strip()
                break

        if actual_error:
            print(f"\nActual error: {actual_error}")

            # Provide specific guidance based on error type
            if "KeyError" in actual_error:
                # Extract column name
                col_match = re.search(r"['\"]([^'\"]+)['\"].*not in index", actual_error)
                if col_match:
                    missing_col = col_match.group(1)
                    print(f"\n→ SUGGESTION: Column '{missing_col}' does not exist in the dataframe")
                    print(f"   Common causes:")
                    print(f"   1. Column was added to df_new but code references df")
                    print(f"   2. Column name misspelled")
                    print(f"   3. Column created in later cell but referenced earlier")
                    print(f"   4. Dataframe operation created new df without copying column")

            elif "NameError" in actual_error:
                var_match = re.search(r"name '([^']+)' is not defined", actual_error)
                if var_match:
                    missing_var = var_match.group(1)
                    print(f"\n→ SUGGESTION: Variable '{missing_var}' is not defined")
                    print(f"   Common causes:")
                    print(f"   1. Variable defined in later cell")
                    print(f"   2. Variable name misspelled")
                    print(f"   3. Cell execution order issue")

            elif "SyntaxError" in actual_error:
                print(f"\n→ SUGGESTION: Python syntax error")
                print(f"   Common causes:")
                print(f"   1. Unclosed parentheses/brackets/quotes")
                print(f"   2. Invalid indentation")
                print(f"   3. Markdown code block using 'python' instead of '{python, eval=FALSE}'")

            else:
                print(f"\n→ SUGGESTION: Review the error context above")
                print(f"   Trace the error in the source notebook and fix")

    else:
        print("\nCould not parse error details from build output")
        print("\nFull error output:")
        print(build_error)

    print("\n" + "="*60)
    exit(1)
```

### Phase 6: Version Tracking Update

**Update handbook_version.json**:

```python
# Prepare build record
build_record = {
    "version": version,
    "date": datetime.now().isoformat(),
    "status": build_status,
    "notebooks_tested": len(notebooks),
    "notebooks_passed": passed,
    "test_time": round(total_time, 1)
}

# Update version data
if module not in version_data:
    version_data[module] = {
        "current_version": version,
        "last_build": build_record["date"],
        "build_history": []
    }

if build_status == "success":
    version_data[module]["current_version"] = version
    version_data[module]["last_successful_version"] = version

version_data[module]["last_build"] = build_record["date"]
version_data[module]["build_history"].insert(0, build_record)

# Keep only last 10 builds
version_data[module]["build_history"] = version_data[module]["build_history"][:10]

# Save version file
with open(version_file, "w") as f:
    json.dump(version_data, f, indent=2)

print(f"\nVersion tracking updated: {version_file}")
```

### Phase 7: Post-Build Actions (If Successful)

**Rename handbook output with version**:

```python
if build_status == "success":
    # Check for handbook output (PDF)
    handbook_pdf = f"{handbook_dir}/{module}-Handbook.pdf"

    if os.path.exists(handbook_pdf):
        # Rename with version
        versioned_pdf = f"{handbook_dir}/{module}-Handbook-v{version}.pdf"
        os.rename(handbook_pdf, versioned_pdf)
        print(f"\nHandbook saved as: {versioned_pdf}")

        # Also copy to main filename (for Moodle upload)
        import shutil
        shutil.copy(versioned_pdf, handbook_pdf)
        print(f"Copy saved as: {handbook_pdf}")
    else:
        print(f"\nWARNING: Expected PDF not found at {handbook_pdf}")
```

**Embed version in handbook metadata** (if using LaTeX/Pandoc):

This would require modifying the build script to pass version metadata. Example:

```yaml
# In handbook YAML front matter
---
title: "MN5813 Module Handbook"
version: "2.2"
date: "2025-10-25"
---
```

---

## Error Tracing Algorithm

The command uses a sophisticated error tracing algorithm:

1. **Parse error from build output**: Extract line numbers where error occurred
2. **Read temporary .Rmd file**: Contains combined content from all notebooks
3. **Search backwards from error line**: Find markdown headers indicating week/notebook
4. **Count code chunks**: Estimate which cell in source notebook
5. **Provide specific guidance**: Based on error type (KeyError, NameError, etc.)

**Example output**:

```
ERROR ANALYSIS
==============================================================

Key error: Quitting from lines 6678-6682 [unnamed-chunk-309] (MN5813-Handbook.Rmd)
Error occurred at lines 6678-6682 in temporary .Rmd file

Reading __TEMP/MN5813-Handbook.Rmd to trace error...

Error context from .Rmd:
  6678: df_sorted = df.sort_values("salary_2022")
  6679: df["salary_rolling_mean"] = df.groupby("department")["salary_2022"].transform(
  6680:     lambda x: x.rolling(window=2, min_periods=1).mean()
  6681: )
  6682: print(df.head())

→ Error likely in: Week 05/Demonstration.ipynb
→ Approximately code chunk #74 in that notebook

Actual error: KeyError: "['salary_rolling_mean'] not in index"

→ SUGGESTION: Column 'salary_rolling_mean' does not exist in the dataframe
   Common causes:
   1. Column was added to df_new but code references df
   2. Column name misspelled
   3. Column created in later cell but referenced earlier
   4. Dataframe operation created new df without copying column
```

---

## Version Tracking File Format

`.claude/handbook_version.json`:

```json
{
  "MN5813": {
    "current_version": "2.2",
    "last_successful_version": "2.2",
    "last_build": "2025-10-25T14:30:00.123456",
    "build_history": [
      {
        "version": "2.2",
        "date": "2025-10-25T14:30:00.123456",
        "status": "success",
        "notebooks_tested": 22,
        "notebooks_passed": 22,
        "test_time": 145.6
      },
      {
        "version": "2.1",
        "date": "2025-10-24T10:15:00.123456",
        "status": "failed",
        "notebooks_tested": 22,
        "notebooks_passed": 21,
        "test_time": 132.4
      }
    ]
  }
}
```

---

## Implementation Notes

This command should be implemented as a Python script that:

1. **Uses AskUserQuestion tool** to prompt for version number
2. **Uses Bash tool** to execute jupyter nbconvert and ./Handbook
3. **Uses Read tool** to parse temporary .Rmd file
4. **Uses Edit/Write tools** to update version tracking file
5. **Provides detailed progress output** throughout execution

The command should be robust to:
- Missing directories
- Failed notebook tests
- Build script errors
- Malformed .Rmd files

All error messages should be clear and actionable.

---

## Usage Example

```bash
# Navigate to module directory
cd ~/OneDrive/Shared/GitHub/Teaching/2025-26/MN5813

# Run command
/teaching_generate_handbook

# Output:
Detected environment: 2025-26/MN5813
Handbook directory: ~/OneDrive/Teaching/2025-26/Modules/MN5813/Handbook
Current handbook version: 2.1

[Prompt for version number]

Found 22 notebooks to test

[1/22] Testing Setup/Introduction.ipynb... ✓ PASS (2.3s)
[2/22] Testing Setup/Installation.ipynb... ✓ PASS (1.8s)
...
[22/22] Testing Week06/Demonstration.ipynb... ✓ PASS (8.1s)

==============================================================
Test Results: 22 passed, 0 failed, 0 errors
Total time: 145.6s
==============================================================

✓ All notebooks passed. Proceeding with handbook build...

Building handbook in ~/OneDrive/Teaching/2025-26/Modules/MN5813/Handbook...
Running: ./Handbook

✓ Handbook built successfully

Version tracking updated: ~/.claude/handbook_version.json

Handbook saved as: ~/OneDrive/Teaching/2025-26/Modules/MN5813/Handbook/MN5813-Handbook-v2.2.pdf
Copy saved as: ~/OneDrive/Teaching/2025-26/Modules/MN5813/Handbook/MN5813-Handbook.pdf
```

---

## Now Proceeding

Now that you understand the requirements, implement this command when the user runs `/teaching_generate_handbook`.

**IMPORTANT IMPLEMENTATION STEPS**:

1. Extract year and module from current working directory
2. Prompt user for version number using AskUserQuestion
3. Find all notebooks in module directory
4. Test each notebook with jupyter nbconvert --execute
5. Report test results with detailed timing
6. Only proceed with build if 100% pass
7. Execute ./Handbook script in handbook directory
8. If build fails, parse error and trace to source notebook/cell
9. Update .claude/handbook_version.json with build results
10. Rename output PDF with version number

**KEY REQUIREMENTS**:

- **NO speculation** on errors - always trace via .Rmd file
- **ALL notebooks must pass** before attempting build
- **Detailed error guidance** based on actual error type
- **Persistent version tracking** across builds
