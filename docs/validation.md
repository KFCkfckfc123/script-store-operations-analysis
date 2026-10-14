# Validation record

Reviewed October 14, 2026. Source: supplied synthetic workbook. Public file: `workbook/Script_Store_Operations_Synthetic.xlsx`. The source was retained unchanged; only the public copy was rebuilt.

| Check | Result | Evidence |
| --- | --- | --- |
| Unique session IDs | Passed | 416 unique IDs across 416 rows |
| Unique script IDs | Passed | 160 unique IDs |
| Session-to-script mapping | Passed | Zero orphan IDs |
| Synthetic visible identifiers | Passed | SES-, SYN-, and Synthetic Script naming conventions |
| Old cached labels | Removed from public copy | All original pivot caches replaced; old pivot labels absent from exported XML |
| Session revenue | Passed | Every row equals players times price |
| Contribution | Passed | Every row equals revenue minus standard DM wage |
| Total revenue / wages / contribution | Passed | $280,352 / $84,912 / $195,440 |
| Script/session reconciliation | Passed | Script counts sum to 416; contributions sum to $195,440 |
| Scenario cost ordering and conversion | Passed | Low ≤ base ≤ high; whole-dollar conversion at 7.2 RMB/USD |
| Monthly counts | Corrected | 29–32 for complete months; October 8; sum 416 |
| Edition weighting | Passed | Session-weighted $505.50 / $527.86 / $430.96 with n=144 / 56 / 216 |
| Performance matrix membership | Corrected | One point per opened script, 136 points; no undefined-average zero points |
| Median population | Defined | Opened scripts only; count median 2, contribution median $490 |
| Spreadsheet-engine formula checks | Passed within tested scope | Nine live reconciliation checks equal zero; error scan found no listed formula errors |
| Input-change tests | Passed | On a disposable formula copy: price +$1 for six players increases revenue and contribution by $6; FX 8 makes first base acquisition cost $94 |
| Desktop Excel refresh / rendering | Not tested | Five native PivotTables and three charts are present in the saved file; desktop Excel still needs a manual opening and refresh check |
| Newly opened scripts / added script IDs | Explicit limitation | Extend scatter and median helper membership; top-20 is a snapshot |

The formula engine was tested on a disposable copy without PivotTables because the engine could not import the rebuilt native pivot objects. The delivered workbook retains its native PivotTables. Independent computations and OOXML inspection verify their synthetic sources and saved summaries; this is not proof of desktop refresh behavior.

Static PNG and PDF were regenerated from the public workbook data using Matplotlib. They are not screenshots of Excel's native chart renderer.

Synthetic provenance is the user's supplied description plus consistent fictional identifiers. It is not proof that synthetic values cannot resemble an underlying business. No old caches or restricted source labels were carried into the public copy.
