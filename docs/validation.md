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
| Desktop Excel open and chart rendering | Not yet confirmed |

The public file includes only synthetic rows. None of the original stale pivot caches were copied. Matplotlib PNG/PDF use the same numerical results; they are not Excel screenshots. Snapshot helper membership and bounded ranges must be extended for new records.
