# Validation record

Reviewed on October 14, 2026. Scope: current README and one-page synthetic Dashboard PDF. No Excel source workbook was available. A check below is a report of evidence, not a claim of workbook certification.

| Check | Result | Evidence / next action |
| --- | --- | --- |
| Public data provenance statement | Documented, not independently established | README and PDF label data synthetic |
| Published workbook availability | Missing | Repository contains README and PDF, no XLSX |
| Displayed KPI readability | Readable | 416; $280,352; $195,440; 136 |
| Edition values readability | Readable | $506; $528; $431 |
| Monthly peak consistency | Conflict | Narrative says 66; plot is near 32 and axis maximum 35 |
| Performance matrix rendering | Defect | Points appear near/below plot boundaries; two cutoffs shown without a usable point distribution |
| Partial-month disclosure | Present | Reporting ends October 8, 2026 |
| Net profit terminology | Clarified | Contribution excludes operating expenses |
| Session IDs, script IDs, joins | Not tested | Inspect unique keys and orphan records in workbook |
| Source-to-summary reconciliation | Not tested | Count sessions and sum revenue/wages/contribution independently |
| Formula error handling | Not tested | Inspect errors, missing vs zero, and lookup failures |
| Pivot refresh / new rows | Not tested | Add a disposable session, refresh, verify totals and charts |
| Cost scenarios / shared releases | Not tested | Confirm monotonic costs and single acquisition allocation |

## Acceptance before calling the Excel version complete

1. All source session IDs unique and all script references valid.
2. Independently recomputed totals match dashboard values, or correct the dashboard and document the reason.
3. Monthly counts sum to the same session total and the narrative matches the verified peak.
4. Edition averages use the documented weighting and show denominators.
5. Missing values do not become silent healthy zeroes.
6. Scatter series includes valid script points; cutoffs are defined and labels are visible.
7. A new record changes summaries after the documented refresh steps.
8. Synthetic provenance is documented and no restricted source records are included.

Temporary input-change checks should be performed on a disposable copy. Do not report unperformed checks as passed.
