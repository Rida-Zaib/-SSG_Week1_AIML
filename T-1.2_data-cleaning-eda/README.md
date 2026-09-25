# Task 1.2 — Data Cleaning & EDA

## Overview
This task cleans a sample sales dataset and explores it using NumPy, Pandas, and
Matplotlib to uncover patterns and anomalies.

## Dataset
`raw_sales_data.csv` — 310 rows of sample sales data with columns: item, category,
price, quantity, rating. The raw file intentionally contains missing values,
duplicate rows, and a few extreme price outliers to practice cleaning on.

## What the notebook does
1. Loads and inspects the raw data (`.info()`, `.describe()`)
2. Checks for missing values and duplicate rows
3. Cleans the data — fills missing `price` and `rating` with the column median,
   drops duplicates
4. Caps price outliers using the IQR method
5. Saves the cleaned dataset as `cleaned_sales_data.csv`
6. Runs exploratory data analysis with three visualizations:
   - Price distribution histogram
   - Average price per category (bar chart)
   - Price vs. rating (scatter plot)

## Files
- `data_cleaning_eda.ipynb` — the full notebook, code + outputs
- `raw_sales_data.csv` — input data
- `cleaned_sales_data.csv` — output, generated after running the notebook

## How to run
```bash
pip install pandas numpy matplotlib
jupyter notebook data_cleaning_eda.ipynb
```
Then Run All Cells.

## Key findings
- Missing values in `price` and `rating` were filled with medians rather than dropped,
  to keep the dataset size intact.
- A handful of prices were extreme outliers, likely data entry errors, and were capped.
- Electronics and Sports categories tend to have higher average prices.
- Price and rating show no strong relationship in this sample.

## Deliverable
Jupyter notebook with cleaned dataset + visualizations, as required by the Skill Set
Go EduTech AI/ML track, Week 1, Task 1.2.
