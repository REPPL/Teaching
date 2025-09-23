# Synthetic datasets

This folder contains documentation for the synthetic datasets used in MN5813. The datasets simulate real-world business data with typical characteristics you might encounter in practice.

## Dataset descriptions

### Business_metrics.csv
Daily business performance metrics over 200 days, including website traffic, marketing spend, conversion rates, and customer satisfaction.

### Retail_sales.csv
Individual retail transactions over 6 months, containing customer segments, product categories, pricing, and satisfaction scores.

## Column definitions

### Business_metrics.csv
| Column | Description | Expected Range |
|--------|-------------|----------------|
| date | Date of observation | 2023-06-01 to 2023-12-17 |
| visitors | Daily website visitors | Typically 600-1,500 |
| marketing_spend | Daily marketing expenditure (£) | Typically 300-800 |
| conversion_rate | Proportion of visitors who purchase | 0.01-0.05 |
| avg_order_value | Average purchase amount (£) | Typically 40-65 |
| revenue | Total daily revenue (£) | Calculated field |
| satisfaction | Customer satisfaction score | 1.0-5.0 |

### Retail_sales.csv
| Column | Description | Expected Range |
|--------|-------------|----------------|
| transaction_id | Unique transaction identifier | 1-5000+ |
| date | Transaction timestamp | 2023-06-01 to 2023-12-31 |
| customer_id | Customer identifier | 1-1000 |
| customer_segment | Customer category | New, Regular, Premium |
| product_category | Type of product | Electronics, Clothing, Books, Home & Garden, Sports & Outdoors |
| quantity | Number of items purchased | Typically 1-3 |
| unit_price | Price per item (£) | Varies by category |
| discount | Discount percentage | 0.0-0.3 |
| discounted_price | Price after discount (£) | Calculated field |
| total_amount | Transaction total (£) | Calculated field |
| payment_method | Payment type | Credit Card, Debit Card, Digital Wallet, Cash |
| satisfaction_score | Customer satisfaction | 1.0-5.0 |

## Notes for analysis

- These datasets reflect common patterns in business data
- Consider exploring data quality as part of your analysis
- Real-world data often requires cleaning and validation

---

## Data quality report

⚠️ **Try to identify these issues yourself before reading this section!**

<details>
<summary><strong>Click to reveal data quality issues (after your own exploration)</strong></summary>

### Business_metrics_special.csv - Data quality issues

#### Missing values (NaN)
1. **Satisfaction scores**: 15 random missing values
   - Represents customers who didn't complete satisfaction surveys
   - Not missing at random - consider imputation strategies

2. **Marketing spend**: 8 random missing values
   - Simulates data collection/recording failures
   - May need interpolation or forward-fill

3. **Average order value**: Missing for days with very low visitors (<5th percentile)
   - Represents system issues on low-traffic days
   - Conditional missingness pattern

#### Data entry errors
1. **Negative satisfaction scores**: 2 instances with value -1
   - Obviously impossible values (scale is 1-5)
   - Need validation rules

2. **Extreme marketing spend**: 3 instances with 3x maximum normal spend
   - Potential decimal point errors or special campaigns
   - Require investigation before handling

#### Special events
- **Day 180**: Black Friday effect (2.5x visitors, 1.5x conversion, 1.3x AOV)
- **Day 145**: Technical issue (0.5x visitors, 0.3x conversion, 0.7x satisfaction)

### Retail_sales_special.csv - Data quality issues

#### Missing values (NaN)
1. **Customer segment**: 200 missing values
   - New customers not yet classified
   - Consider "Unknown" category or predictive classification

2. **Satisfaction score**: 500 missing values
   - Customers who didn't provide feedback
   - Analyse missingness pattern - may correlate with satisfaction level

3. **Payment method**: 20 missing values (only from cash transactions)
   - Recording issues at point of sale
   - Can likely be imputed as "Cash"

#### Data entry errors
1. **Negative quantities**: 5 transactions with quantity = -1
   - Impossible values requiring correction
   - May represent returns (need business context)

2. **Extreme unit prices**: 3 items with 100x normal price
   - Decimal point errors (£5,000 instead of £50.00)
   - Use category-based validation

3. **Zero prices**: 10 items with unit_price = 0
   - Promotional items or data entry errors
   - Need business rules for handling

#### Duplicate records
- **20 duplicate transactions**: Same details but different transaction_id (+10000)
- Require deduplication strategy
- Consider keeping first occurrence

### Learning objectives

These issues help students practice:
1. **Data exploration**: Identifying anomalies through summary statistics and visualisation
2. **Missing data analysis**: Understanding patterns and choosing imputation strategies
3. **Outlier detection**: Statistical methods vs domain knowledge
4. **Data validation**: Creating business rules and constraints
5. **Documentation**: Recording cleaning decisions for reproducibility

### Recommended analysis approach

1. Start with exploratory data analysis (EDA)
2. Create data quality reports
3. Document all issues found
4. Develop cleaning strategies
5. Validate results
6. Document decisions made

</details>
