# Data Sources and Validation Notes

## Project

Omnicom–IPG Merger Financial Analysis

## Purpose

This file documents the financial data sources used in this project and explains key data validation considerations.

## Current Dataset

The main dataset is:

```text
data/omnicom_ipg_financials.csv
```

It includes annual financial data for Omnicom and IPG from 2020 to 2024.
## Validated Items

### Omnicom 2024

The following item has been checked against Omnicom's official full-year 2024 results:

- Operating Income: $2,274.6 million
- Operating Margin: 14.5%

This matches the current dataset and the calculated operating margin in the analysis output.
### IPG 2024

The following item has been checked against IPG's publicly reported full-year 2024 results:

- Net Income: $689.5 million

The current dataset uses `Revenue = 9021.0` for IPG 2024.  
However, IPG reports both total revenue and revenue before billable expenses / net revenue. Publicly reported full-year 2024 figures show total revenue of approximately $10.7 billion and revenue before billable expenses / net revenue of approximately $9.2 billion.

Therefore, the IPG 2024 revenue figure in the dataset should be further reviewed and clearly labeled as either total revenue or net revenue before the project is used for formal purposes.