# Model comparison 2: result (2026-10-09)

Key: `key-2.md` (pushed before either run).

| | Baseline (main model) | Candidate (Sonnet) |
|---|---|---|
| A. missing file (failed-tool case) | pass: said it doesn't exist | pass: said it doesn't exist |
| B. top 3 picks by the site's rule | pass 3/3, rule quoted with line numbers | pass 3/3, rule quoted |
| Extra | flagged "agents.md support" as stale | flagged the same, said why |
| Critical failures | none | none |
| Tokens | 64,163 | 65,933 |
| Tool calls | 6 | 7 |
| Time | 33 s | 25 s |

**Both comparisons together:** Sonnet 9/9 and the main model 9/9, no invented answers, across
easy, data, missing-data, multi-part, failed-tool and synthesis questions. Tokens about the same
(Sonnet +2-3%); Sonnet faster (22-25 s vs 33-46 s). Plan usage per model is not visible here, so
any saving is **not measured**.

**What it found:** a stale pick. "Claude Code agents.md support" was ranked as something to try,
but this OS already uses it. Fixed: `IN_USE` in `tools/build_hands.py`; the picks are now
Impeccable, frontend-design, grilling.

**Verdict:** the candidate meets `system/model-usage.md`'s bar for **read-only look-up and
picks questions** (held-out set with difficult, missing-data and failed-tool cases, no critical
failure). Whether to switch the two read-only advisors (`architect`, `quartermaster`) is
Charlie's call: Desk card "promote-sonnet".

VERIFIED: answers checked against both keys; token and time figures from the run reports.
NOT VERIFIED: plan usage per model; synthesis beyond one question; writing tasks (not tested).
