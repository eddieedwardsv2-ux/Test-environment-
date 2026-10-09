# Model comparison 1: result (2026-10-09)

Key: `key.md` (written and pushed before either run). Same prompt, same read-only
general-purpose helper, one run each, run side by side.

| # | Baseline (main model) | Candidate (Sonnet) |
|---|---|---|
| 1 current priority file | pass | pass |
| 2 Anthropic bonus (+2 / +1) | pass (also cited the code line) | pass (cited README; said it read "an Anthropic catalog" as community) |
| 3 #1 in Business & finance | pass | pass |
| 4 alias end date | pass | pass |
| 5 subscribers (missing data) | pass: "Not in the repo" | pass: "Not in the repo" |
| 6 VERIFIED rule + concept | pass | pass |
| 7 audit time and place | pass | pass |
| **Score** | **7/7** | **7/7** |
| Tokens (helper total) | 64,643 | 66,726 |
| Tool calls | 7 | 6 |
| Time | 46 s | 22 s |

**Quality:** both all correct, no invented figures. The baseline went one step deeper on
evidence (the code line for #2, the history for #7); the candidate flagged its one
interpretation instead of hiding it. No critical check failed.

**Cost:** about the same number of tokens, so any saving comes from Sonnet's lower price
per token, not from doing less. Plan usage per token isn't exposed here, so the saving is
**not measured**. Sonnet was about twice as fast.

**Verdict: candidate passed, not promoted.** `system/model-usage.md` needs a held-out set
that also includes a failed-tool case and a harder synthesis task before any helper moves
off `inherit`. This set had easy, data, missing-data and multi-part questions only.
**Next (comparison 2):** the same two helpers on (a) a question whose file is missing or
renamed (failed-tool / stale-route case) and (b) one short synthesis: "which 3 tools should
Charlie try first and why", scored against the Quartermaster's own picks and rules.

VERIFIED: both answer sets checked line by line against the pre-declared key; token and
time figures are from the harness's run reports.
NOT VERIFIED: plan usage per token for each model; whether the result holds on harder work.
