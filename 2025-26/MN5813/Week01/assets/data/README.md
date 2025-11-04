# Week 01 Data Files

This directory contains simple text datasets for Week 01 (Introduction to Python).

## sales_data.txt

### Purpose

A minimal sales dataset used to demonstrate basic file reading in Python. This file introduces students to file I/O operations and string processing.

### Dataset Structure

**Format**: Plain text file with simple key-value pairs
**Size**: 3 records
**Encoding**: UTF-8

### Content

```
Alice: £1500
Bob: £2300
Charlie: £1800
```

Each line contains:
- **Name**: Person's first name
- **Sales**: Amount in GBP (£) format

### Usage in Week 01

Used to demonstrate:
1. Opening and reading files with `open()` and `read()`
2. Line-by-line processing with `readlines()` or iteration
3. String methods (`.strip()`, `.split()`)
4. Basic data parsing and type conversion
5. File context managers (`with` statement)

## new_sales_data.txt

### Purpose

Additional sales data used to demonstrate file appending and combining multiple data sources.

### Dataset Structure

**Format**: Plain text file with simple key-value pairs
**Size**: 3 records
**Encoding**: UTF-8

### Content

```
David: £2100
Emma: £1750
Frank: £1950
```

Each line contains:
- **Name**: Person's first name
- **Sales**: Amount in GBP (£) format

### Usage in Week 01

Used to demonstrate:
1. Reading from multiple files
2. Combining data from different sources
3. Appending data to existing files
4. List operations and data aggregation

## Expected Learning Outcomes

Students working with these files should be able to:
- Read text files using Python's built-in file operations
- Parse simple structured text data
- Extract and process string information
- Convert string data to appropriate types (removing £ symbol, converting to float/int)
- Combine data from multiple files
- Calculate basic statistics (total sales, average, etc.)

## Data Format Notes

- Currency symbol (£) must be stripped before numeric operations
- Each record is on a separate line
- Names contain no spaces (single first names only)
- Sales values range from £1500 to £2300

---

**Dataset created**: 2025
**Purpose**: Week 01 Introduction to Python teaching examples
**Topic**: File I/O and basic string processing
