# Model usage — quality first, then lower usage

Charlie's policy, 2026-10-09. This extends the existing router; it is not a
new routing service or a claim that automatic model switching is installed.

## Choose before delegating
1. Keep the user's main model. Use a deterministic script for exact counts,
   filtering, file checks or transformations when one already does the job.
2. Define the output and its acceptance checks before choosing a worker.
   Retrieve only the sources needed; do not load whole brains or full chats.
3. Default unproven delegations to the main model (`inherit` in active Claude
   agent definitions). A cheaper candidate is a trial until it has evidence
   for that task class, source conditions and model version. Verify the actual
   model selected by the host; aliases and configuration can change it.
4. Complex synthesis, architecture, ambiguous tasks and decisions with serious
   consequences stay with the strongest configured available model. Do not
   quietly change the user's main model, bypass a model allowlist or invent
   access to a provider. If the strong model is unavailable, save the state
   and mark the task blocked; do not silently lower the quality bar.

## Acceptance, escalation and promotion
- Compare candidate and strongest available baseline using the same inputs,
  context, permissions and acceptance criteria. The baseline also has to pass
  source/tests-based checks; agreement alone does not prove correctness.
- All critical checks must pass: source accuracy, required completeness,
  usable output format, uncertainty handling and instruction boundaries.
  For prose, match required quality rather than identical wording.
- A candidate's missed critical check, unsupported assertion, lost requirement
  or worse usable result rejects that result. Escalate the failed task to the
  strong model with the original evidence and a compact failure description.
  Validate that output too. A permissions or missing-source failure is not
  repaired by paying for a stronger model: resolve or report that blocker.
- At most one candidate attempt and one strong recovery by default; no retry
  loops or multi-model panels. A transient tool failure may get one bounded
  retry if useful, recorded separately from reasoning failure.
- Before making a cheaper route normal, pass a predeclared representative
  held-out set including difficult, missing-data and failed-tool cases.
  Record inputs, model/version/effort, outputs, checks and failures. Critical
  failures mean no promotion; narrow the scope or retain the strong model.
- Compare total workflow usage: worker + checker + retries + integration;
  record tokens/cost, latency and human corrections where exposed. Unknown
  metrics stay unmeasured. Do not claim savings without observations.
- Recheck after model, skill, prompt or source changes; suspend a route after
  a quality regression. Restore the previous proven route without losing work.

## Fan-out and fan-in
Use one lead by default. Start with at most two helpers for independent,
substantial, checkable tasks; this is a conservative starting limit, not a
measured optimum. Increase only with a concrete benefit, budget and separate
ownership, within the host's limits. Simple lookups and dependent steps stay
sequential. Each helper gets task, minimal sources, constraints, output shape
and finish check; no helpers spawning more helpers by default.

One lead integrates all outputs, checks citations and contradictions, flags
missing or failed pieces, and writes shared files once. Do not treat a set of
plausible worker answers as a checked final answer. Stop work that is no longer
needed and preserve a short handoff when limits approach.

## Current evidence and next trial
`audits/evidence/2026-10-09-usage-pilot/`: one fixed-input extraction case;
gpt-6-luna and gpt-6-astra, medium reasoning, each matched all nine expected
fields. No tools used. This is a smoke test, not nine independent tasks or a
production approval. Costs, tokens and controlled latency are unmeasured.
No cheaper production route has been promoted by this test.

Next use `try-tool` on held-out real extraction/retrieval jobs against the
strong baseline. FreeLLMAPI needs a separate explicit-provider trial, current
terms and working credentials. Do not enable untested automatic fallback.
The current review is `research/hands/reviews/freellmapi-2026-10-09.md`.

Claude configuration source, checked 2026-10-09:
https://code.claude.com/docs/en/sub-agents#choose-a-model . `inherit` uses the
main model; per-invocation choices/configuration can affect selection. This
session has not verified actual Claude model resolution after these edits.
