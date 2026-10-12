# Script Store Operations Analysis

An Excel dashboard analyzing synthetic script-store operations, contribution, and estimated cost recovery.

[View the Dashboard PDF](./Script_Store_Operations_Dashboard_Synthetic.pdf)

## Project Overview

This project demonstrates an Excel-based operating analysis system for a fictional script-murder game store. All displayed records are synthetic and were created for portfolio purposes. No confidential business data is included.

## Business Questions

- How many game sessions were operated each month?
- Which scripts generated the highest estimated contribution?
- Which script editions performed best per session?
- Which scripts recovered their estimated acquisition costs?
- Which scripts should receive more scheduling or promotional support?

## Tools and Techniques

- Microsoft Excel
- Excel Tables
- XLOOKUP
- IF and IFERROR
- COUNTIF and SUMIFS
- PivotTables and PivotCharts
- Scenario analysis
- Dashboard design
- Data validation and reconciliation checks

## Dataset

The synthetic dataset contains:

- 160 fictional scripts
- 416 fictional game sessions
- Session dates from September 2025 through October 8, 2026
- Script type, edition, player count, and price
- Estimated revenue and standard DM wages
- Low, base, and high acquisition-cost scenarios
- Contribution and cost-recovery metrics

## Analysis Workflow

1. Structured script-level and session-level records as Excel Tables.
2. Connected session records with script attributes using lookup functions.
3. Estimated gross revenue from player count and price per player.
4. Calculated contribution after standard DM wages.
5. Modeled acquisition costs under low, base, and high scenarios.
6. Created PivotTables for monthly activity and script performance.
7. Segmented scripts by session frequency and contribution per session.
8. Built an executive-style Excel dashboard.

## Metric Definitions

**Estimated Gross Revenue**

Players × Price per Player

**Estimated Contribution**

Estimated Gross Revenue − Standard DM Wage

Estimated contribution is not net profit because rent, utilities, taxes, and other operating expenses are unavailable.

## Data Limitations

- All records are synthetic and intended only for portfolio demonstration.
- Revenue does not include actual membership discounts or transaction adjustments.
- Acquisition costs are modeled estimates rather than verified purchase prices.
- Contribution excludes rent, utilities, taxes, and other operating expenses.
- October 2026 is a partial month.
- This project demonstrates analytical methodology and does not claim actual business growth caused by the analyst.