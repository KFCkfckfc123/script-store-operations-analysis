# Compatibility validation record

October 14, 2026. Public file: workbook/Script_Store_Operations_Synthetic_Compatible.xlsx.

The previous export showed #REF! values, a session count of 1, missing charts and broken title layout in the user's desktop screenshot. The precise import/repair sequence is unavailable. The replacement avoids the earlier custom pivot XML and structured references and uses standard XlsxWriter file serialization.

| Check | Result |
| --- | --- |
| Synthetic session/script unique keys | 416 sessions, 160 scripts; no duplicate keys |
| Session-script mapping | Zero unmatched IDs |
| Row revenue and contribution calculations | Matched independent computation |
| Totals | Revenue $280,352; wages $84,912; contribution $195,440 |
| Opened scripts | 136 |
| Script/session reconciliation | Counts and contribution matched |
| Scenario costs | Low ≤ base ≤ high; conversion 7.2 RMB/USD |
| Formula-engine recalculation | Nine checks matched independent controls |
| Formula error scan | No listed formula errors after recalculation |
| Input-change check | Price +$1 for six players increased revenue and contribution by $6 |
| Standard-file reload | Passed with openpyxl; three charts and two Excel Tables present |
| Structured references / custom pivot objects | Omitted in compatibility edition |
| Desktop Excel open and chart rendering | Owner confirmed correct display of the latest English workbook on October 23, 2026 |

The public file includes only synthetic rows. None of the original stale pivot caches were copied. Matplotlib PNG/PDF use the same numerical results; they are not Excel screenshots. Snapshot helper membership and bounded ranges must be extended for new records.


## English release verification — October 23, 2026

- Translated 1,162 category cells and retained every original numeric cell within a 1e-8 comparison tolerance after formula recalculation.
- Refreshed edition chart bindings and caches. No Chinese characters remain in workbook XML or published text/code.
- Added formula-linked English month labels for the monthly chart.
- Formula-engine test: Raw Data H2 increased by $1 for six players; revenue and contribution each increased by $6. Restored input and original baseline before export.
- Nine reconciliation differences are zero. The saved workbook contains no error-typed cells, external workbook links or pivot caches.
- Seven worksheets, two Excel Tables and three native charts remain. Changed dashboard, category summaries and source-table ranges were rendered and inspected.
- Independent Python checks verify 416 unique sessions, 160 unique scripts, 136 opened scripts, row calculations and script/session totals.
- Refreshed PNG/PDF use workbook-derived KPI totals. They are plotting-library previews, not Excel screenshots.
- Mac Excel automation returned AppleEvent timeout (-1712). Subsequently, the owner confirmed that the latest English workbook displayed correctly in Excel. Opening and display acceptance is user-operated; independent native Excel recalculation and input-change tests were not completed.

Run `python scripts/validate_project.py` to repeat the saved-file checks. These checks preserve the supplied synthetic fixture and do not establish actual commercial performance or independently verify its original generation process.

## Owner acceptance and local cleanup — October 23, 2026

The owner confirmed that the latest English workbook displayed correctly in Excel after reopening the current version. This supplements formula-engine recalculation, input-change tests and saved-file checks; it is not an independently automated native Excel test. Superseded synthetic workbooks in Downloads and the prior local synthetic-project backup were moved to the Mac Trash. The current public workbook and original private business files were retained.
