# Data dictionary

This describes the verified public synthetic workbook. Session table is `Raw Data` (Table `RawData`); script table is `Script_List`. Some explanatory names below map to existing headers, such as `Open Session Count` and `Avg Contribution(Opened Only)`. A text `Report Month` helper supports native monthly PivotTables.

## Record grain and keys

- Session table: one operated game session per row. Session ID must be unique and nonblank.
- Script table: one script per row. Script ID must be unique and nonblank.
- Each session references one script. Several DMs must not create several revenue rows for the same session.
- Editions or acquisition-cost assumptions must not multiply session records when joined.

| Field | Table | Type / unit | Meaning and rule |
| --- | --- | --- | --- |
| Session ID | Session | Text ID | Stable session key; preserve leading zeros |
| Script ID | Both | Text ID | Session foreign key; script primary key |
| Date | Session | Excel date | Operated session date; reporting cutoff explicit |
| Month Start | Session | Excel date | First day of the session month |
| Script Name | Script | Text | Fictional public display name |
| Script Type | Script | Category | One documented category or explicit multi-category policy |
| Script Edition | Script | Category | City-limited, exclusive, or boxed |
| DM Count | Session | Integer | Staff count, distinct from a DM identity |
| Players | Session | Integer | Actual players in that synthetic session |
| Price Per Player | Session | USD/player | Modeled session price; historical price if available |
| Estimated Gross Revenue | Session | USD | Players times price per player |
| Standard DM Wage | Session | USD | Total modeled wage for the session |
| Estimated Contribution | Session | USD | Modeled revenue minus standard DM wage |
| Cost Low/Base/High USD | Script | USD/script | One acquisition-cost estimate per script per scenario |
| Opened Session Count | Script | Integer | Sessions observed in the analysis window |
| Cumulative Estimated Contribution | Script | USD | Sum of linked session contribution |
| Average Contribution per Session | Script | USD/session | Cumulative contribution divided by observed sessions |
| Surplus Low/Base/High | Script | USD | Cumulative contribution minus acquisition cost |
| Cost Recovery Status | Script | Category | Scenario-specific acquisition-cost comparison |

Missing is not zero. A never-opened script has zero observed sessions and undefined average contribution. Missing acquisition costs mean recovery is unknown. Multiple releases sharing an acquisition must use a documented allocation rather than charging the full cost twice.
