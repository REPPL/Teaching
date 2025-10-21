# Week 06 Data Files

This directory contains datasets for Week 06 (Pandas Application Week).

## employee_sales.csv

### Purpose

This dataset provides a worked example that parallels the Olympics group assessment dataset structure. It allows students to see complete solutions to similar data wrangling problems without directly solving their assessment.

### Dataset Structure

**Size**: 245 rows × 15 columns

**Time period**: 2023-Q1 through 2024-Q1

### Column Definitions

| Column | Type | Description | Expected Range | Olympics Equivalent |
|--------|------|-------------|----------------|---------------------|
| `employee_id` | Integer | Unique employee identifier | 1-50 | ID |
| `name` | String | Employee full name | Text | Name |
| `gender` | String | Employee gender (F/M/D)* | F, M, D | Sex (M/F only) |
| `age` | Float | Employee age in years | 22-59, with ~8% missing | Age |
| `height_cm` | Float | Height in centimetres | 155-194, with ~10% missing | Height |
| `weight_kg` | Float | Weight in kilograms | 50-99, with ~10% missing | Weight |
| `team` | String | Sales team affiliation | UK/US/EU Sales Team | Team |
| `region` | String | Three-letter region code | LON, NYC, PAR | NOC |
| `quarter` | String | Sales quarter | YYYY-QN format | Games |
| `year` | Integer | Year of sale | 2023, 2024 | Year |
| `half` | String | Half of year | H1, H2 | Season |
| `office` | String | Office location | London, New York, Paris | City |
| `product_category` | String | Broad product category | 5 categories | Sport |
| `product` | String | Specific product sold | Various | Event |
| `award` | String | Sales award received | Gold/Silver/Bronze/NaN | Medal |

**Note on gender**: Our demonstration dataset uses `gender` (F/M/D) to recognize gender diversity. The Olympics dataset uses `Sex` (M/F only), reflecting historical binary categorization. This difference is a good teaching point about evolving data practices.

### Mapping to Olympics Dataset

This dataset has a 1:1 column mapping with the Olympics athlete_events.csv:

```
employee_sales.csv          Olympics athlete_events.csv
-------------------         ---------------------------
employee_id                 ID
name                        Name
gender                      Sex
age                         Age
height_cm                   Height
weight_kg                   Weight
team                        Team
region                      NOC
quarter                     Games
year                        Year
half                        Season
office                      City
product_category            Sport
product                     Event
award                       Medal
```

### Data Characteristics

#### Missing Values

The dataset includes realistic missing values:

- `age`: ~8% missing (mimics real-world demographic data)
- `height_cm`: ~10% missing
- `weight_kg`: ~10% missing
- `award`: ~76% missing (most sales don't receive awards, just like most athletes don't win medals)

#### Award Distribution

Awards follow a realistic distribution similar to Olympic medals:

- **No award**: ~76% (most common)
- **Bronze**: ~8%
- **Silver**: ~9%
- **Gold**: ~7%

This parallels the Olympics where most athletes compete without winning medals.

#### Gender Distribution

- **F (Female)**: ~50%
- **M (Male)**: ~43%
- **D (Diverse)**: ~7%

#### Duplicates

The dataset contains approximately 2% duplicate rows (5 rows) for deduplication exercises, mirroring potential data quality issues students might encounter.

### Product Categories and Items

**Electronics**: Laptop Pro, Wireless Mouse, Keyboard Deluxe, Monitor 27"

**Clothing**: T-Shirt, Jeans, Jacket, Sneakers

**Home & Garden**: Coffee Maker, Garden Tools Set, Vacuum Cleaner, Bedding Set

**Books**: Business Strategy, Python Programming, Marketing 101, Finance Basics

**Sports Equipment**: Yoga Mat, Dumbbells, Tennis Racket, Football

### Expected Analysis Patterns

Students can adapt these techniques to their Olympics analysis:

1. **Data loading**:
   - Read CSV with `pd.read_csv()`
   - Explore with `.head()`, `.info()`, `.describe()`

2. **Data cleaning**:
   - Identify missing values with `.isnull().sum()`
   - Handle NaN appropriately per column
   - Remove duplicates with `.drop_duplicates()`
   - Convert `year` to datetime

3. **Data wrangling**:
   - Create age groups using `pd.cut()` or conditionals
   - Combine name fields (if needed)
   - Extract temporal features (decade, century)

4. **Data analysis**:
   - Group by `product_category` to find average age
   - Count awards by `region` to find top performers
   - Identify most decorated employees by category
   - Compare metrics across `gender`, `region`, `half`

5. **Advanced techniques** (Week 05):
   - Use `pivot_table()` for multi-dimensional analysis
   - Create MultiIndex for hierarchical analysis
   - Apply rolling calculations for trends
   - Use method chaining for efficient pipelines

### Data Generation

This dataset was synthetically generated using Python with:
- Controlled randomness (seed=42 for reproducibility)
- Realistic distributions for all variables
- Intentional data quality issues for teaching purposes
- Gender-inclusive categories

### Usage in Week 06

This dataset is used in the Week 06 Demonstration notebook to show:

1. **Complete worked examples**: Students see how to solve problems similar to their assessment
2. **Technique transfer**: Each technique maps directly to Olympics analysis
3. **Code adaptation**: Students can adapt the code patterns to their dataset
4. **Best practices**: Demonstrates proper documentation, error handling, and analysis workflow

The dataset should NOT be used for the actual group project—students must use the Olympics athlete_events.csv dataset as specified in the assessment brief.

---

**Dataset created**: 2025-10-21
**Purpose**: Week 06 Demonstration teaching example
**Assessment**: Olympics group project (Week 03)
