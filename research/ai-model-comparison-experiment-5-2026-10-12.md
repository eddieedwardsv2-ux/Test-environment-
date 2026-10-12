# Research Experiment 5 — AI Model Comparison
Date: 2026-10-12. Research and audit only. No model rerouting, agent configuration edits or AI-OS redesign.

## Question / success criteria
Determine where a cheaper model gives equally dependable task results. A candidate requires matching source input and permissions, **all critical checks passed**, independent answer-key verification, held-out negative and synthesis cases, no unsupported claims, and recorded actual model/version/effort, cost, latency, tokens and corrections where available. Do not claim financial savings without plan/billed usage.

## Existing model policy
`system/model-usage.md` already says quality first; complex work stays on the strongest model, unproven delegations inherit. On 2026-10-09 the owner approved Sonnet for two read-only advisors, Architect and Quartermaster, after recorded side-by-side tests. Other helpers inherit. There is no general automatic lower-cost routing or fallback.

## Sources read
- `system/model-usage.md`
- `audits/evidence/2026-10-09-model-compare/result-2.md`
- `audits/evidence/2026-10-09-model-compare/spot-check.md`
- `research/hands/reviews/freellmapi-2026-10-09.md`
- AI Impact `research/ai-impact/videos/rqI8w6KZA8M.md` — subjective Claude-v-Codex demonstrations; no systematic comparative model benchmark (https://www.youtube.com/watch?v=rqI8w6KZA8M&t=30s).

## Previously executed historical comparison (not a fresh model invocation)
Reported read-only lookup and selection suite: strong main model 9/9; Sonnet 9/9, zero documented critical failures. Second subset: 2/2, including absent-file refusal and multi-part selection. Tokens for second subset: baseline 64,163 vs Sonnet 65,933 (Sonnet **2.8% more**); elapsed 33 s vs 25 s (**24.2% faster** in this subset). No billed or plan cost observation; do not call this cheaper. Other historical subset reported Sonnet faster too. Model alias/version and actual active routing NOT freshly resolved by this session.

## New practical check in this session (documentary consistency, not inference)
Connected GitHub API read three source documents and checked nine assertions:
1. Both models documented 9/9: PASS.
2. Missing-file negative case captured: PASS.
3. Zero critical failures documented: PASS.
4. Both token counts available: PASS.
5. Both time measurements available: PASS.
6. Plan usage not measured: PASS (case-insensitive recheck after initially case-sensitive matcher missed this).
7. Scope restricted to read-only tasks: PASS.
8. Promoted advisors remain exactly Architect and Quartermaster: PASS according to policy record, not runtime configuration inspection.
9. Untested fallback prohibited: PASS.
**9/9 documentary checks passed after fixing check #6's case sensitivity.** This is document consistency, not 9 additional model output evaluations.

## Disagreements and limitations
AI Impact's landing-page and breakout-game comparisons are personal preferences without controlled scoring; the YouTube headline cannot establish benchmark superiority. FreeLLMAPI marketing claims about no-fee inference and model-equivalence conflict with variable quotas and provider coverage in its own documentation; no valid cost or equivalence proof for it. Nate's guidance prioritises relevant small context and actual output quality, which can influence apparent model performance; control context length and data when comparing.

## Held-out comparison protocol for future *real* execution
Use the existing evaluation policy and add a fixed 12-case test pack: 4 source-grounded retrievals with distractors; 2 missing/unavailable-source cases; 2 deterministic extract/transform cases with exact expected JSON; 2 multi-source contradictory evidence syntheses; 1 tool failure; 1 real read-only advisor task from the active project. Key and critical checks fixed *before* invocation, compare current strongest baseline and candidate on same permission and retrieval bundle. Record exact resolved model IDs, host and effort, prompt/context sizes, raw output, tool receipts, tokens, elapsed time, billed cost if visible, and manual corrections. Candidate passes only 12/12 critical checks and non-inferior quality. Cost-saving requires measured total workflow cost (including checking and retries) less than baseline; speed comparisons require repeated samples not one run.
Do not change promotions without such evidence and user intent.

## Overall outcome
**VERIFIED:** historical report contains 9/9 versus 9/9, 2.8% extra Sonnet tokens and 24.2% less time in subset; 9/9 documentary assertions pass after case-insensitive recovery; policy applies narrow read-only promotion.
**NOT VERIFIED:** fresh two-model execution in this session; controlled blind held-out generalisation; exact current resolved model versions; actual billed savings; creative/business/coding parity; automatic fallback.
This session does not expose a controllable two-model inference benchmark runner, and no approved credentials/model APIs were used. No runtime quality comparisons were fabricated.
