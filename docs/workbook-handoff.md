# Workbook usage

The public workbook is included at `workbook/Script_Store_Operations_Synthetic.xlsx`. It contains only verified fictional records and fresh synthetic pivot caches. The original upload remains unchanged.

## Navigation

Start Here → Dashboard → Assumptions → Script_List / Raw Data → Pivot_Analysis → Checks.

Raw Data contains one operated session per row. Script_List contains one fictional script per row. Wage inputs are total session amounts. The source data have no separate individual DM identities.

## Changes and refresh

1. Work on a disposable copy first.
2. Change a session's modeled price and confirm revenue, contribution, script totals, and Dashboard totals recalculate.
3. Use Data > Refresh All to update five native PivotTables.
4. Inspect Checks. Baseline controls intentionally change if inputs change; update expected controls only after independently validating an intentional new dataset. Script/session reconciliation differences must remain zero.
5. If adding sessions, extend check-detail ranges. If a previously unopened script opens, update scatter and median-helper membership. New scripts also require extending lookup ranges. Top-20 is a saved snapshot, not a dynamic ranking.
6. Recalculate and save in Excel before running `scripts/build_preview.py`; the script reads saved cached values.

Native desktop Excel open/refresh/visual behavior has not been tested in this environment. Object presence and source contents were inspected; perform the manual steps above before claiming native refresh is verified.

The PNG/PDF use the same synthetic results but are rendered with Matplotlib, not Excel screenshots. Do not add confidential records to the public repository.
