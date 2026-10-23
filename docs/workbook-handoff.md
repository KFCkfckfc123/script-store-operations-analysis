# Compatibility workbook usage

Download `workbook/Script_Store_Operations_Synthetic_Compatible.xlsx`. This replaces the earlier export that showed broken references in the user's screenshot. The original business workbook is unchanged.

Start Here → Dashboard → Assumptions → Script List / Raw Data → Analysis → Checks.

This edition uses bounded cell ranges and standard XLSX output. It retains Excel Tables, formulas, and three charts. Native PivotTables were omitted; Analysis uses ordinary formula summaries. Recreate PivotTables inside Excel from SessionRecords if needed.

Enable automatic calculation. On a disposable copy, changing Raw Data H2 from 75 to 76 should increase estimated revenue and contribution by $6. Baseline controls show a difference after intentional changes; validate a new dataset independently before updating expected controls. Script/session reconciliation should still be zero.

New records require extending bounded formula and check ranges. Scatter membership, median helpers, and top-20 membership are snapshot selections. Top-20 is a static ranking. Recalculate and save in Excel before rebuilding PNG/PDF from cached values.

Formula-engine tests passed, including error scans and input changes. Desktop Excel opening and native chart layout remain to be confirmed by the user. No confidential business records are included.


## English release

Use only the seven English category values listed in the data dictionary. Edit matching classifications in both source tables when changing a script category. Existing summaries and edition charts use those labels as criteria.

Before presenting the workbook, open it in desktop Excel, confirm that no repair prompt appears, recalculate, and check Dashboard, Analysis and Checks. Baseline: 416 sessions, $280,352 revenue, $195,440 estimated contribution, 136 opened scripts; Checks D2:D10 should be zero. Native Excel acceptance was not completed by automation.
