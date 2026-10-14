# Metrics and assumptions

These definitions describe the public workbook. Formula results were checked against independent aggregation; native Excel refresh remains a manual check.

## Session economics

Estimated gross revenue = players × modeled price per player.

Estimated contribution = estimated gross revenue − total standard DM wage for the session.

This is a limited contribution estimate, not accounting gross profit or net profit. Do not subtract acquisition costs per session and then subtract the same full acquisition again in recovery analysis.

Previously specified wage policy: emotional/performance scripts use a fixed configured wage; inference, mechanism, and comedy scripts use modeled script fees × 0.875 × 0.30. The 0.875 factor is a modeling assumption, not verified evidence of actual discounts. The public workbook retains supplied standard wage inputs rather than inferring an uncovered category rule. Each wage is a total session amount, not a per-DM amount. Raw sessions look up that configured script wage. Tips belong to DMs and are outside modeled store revenue and wages.

## Aggregation

Monthly sessions = count of unique session IDs within the month and reporting window.

Script sessions = count of unique sessions linked to that script.

Average contribution per session = sum of session contribution / session count. For an edition, aggregate all relevant session contribution and divide by all relevant sessions. Averaging script averages would give rarely opened scripts equal weight and answers a different question.

Script cumulative contribution = sum of linked session contribution over the observed window. It is not lifetime contribution unless the history is complete.

Scenario surplus = cumulative estimated contribution − scenario acquisition cost, once per script. Nonnegative surplus means modeled acquisition cost is recovered within the observed window; it does not mean the store is profitable. Missing costs yield unknown status. Low ≤ base ≤ high holds. RMB costs convert at 7.2 RMB/USD, rounded to whole USD. This matches the supplied synthetic costs and corrects the previous assumption of 7.

## Comparisons and decisions

October 2026 ends on October 8. Exclude it from full-month comparisons or compare equal observation windows. Calendar-day normalization alone does not account for opening schedules or seasonality.

Rankings by total contribution and contribution per session answer different questions. Edition differences may reflect price, player count, wage policy, script selection, and frequency. Session duration and capacity are unavailable, so contribution per staff-hour or room-hour cannot be calculated.

A performance matrix must plot one point per opened script using observed session count on X and average contribution on Y. Define numerical cutoffs and their basis before assigning segments. The rebuilt matrix excludes unopened scripts. Cutoffs use opened-script medians (2 sessions, $490); ties are high. These segments indicate investigation priorities, not verified economic recommendations.
