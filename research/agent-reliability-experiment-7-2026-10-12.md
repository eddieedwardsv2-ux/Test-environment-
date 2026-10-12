# Research Experiment 7 — Agent Reliability
Date: 2026-10-12
Scope: deterministic isolated failure fixtures plus targeted real GitHub research. No AI-OS architecture changes or customer actions.

## Predeclared acceptance
Five categories: dated stale-evidence precedence, absent-file truthful handling, bounded tool failure recovery, saved checkpoint restoration, and completed arithmetic task with missing-data guard. Each test must match the explicit fixture expected output; report the difference between simulations, real connector calls and genuine autonomous agent testing. A full agent reliability verdict requires *fresh agent sessions with injected failures*, not this harness alone.

## Source and existing mechanism
`AGENTS.md`, `context/current-focus.md`, `context/handoff.md`, `system/architecture.md` and `research/ai-os-architecture-experiment-2-2026-10-12.md` read through the live GitHub connector. Current active priority remains TRADEFLOW quote demo; do not alter it. Existing precedence, check and handoff instructions are in place; routing compliance by fresh agents not tested.

## Test execution
Run with Python 3 in a separate temporary sandbox using synthetic non-customer data.
The harness generated an evidence JSON file and saved/restored a temporary checkpoint. Five executed checks:
| Scenario | Fixture | Observed | Result |
|---|---|---|---|
| Stale evidence | 2026-10-09 price 80 vs 2026-10-12 price 95 | selected date-newest price 95 | PASS |
| Missing file | checked absent `fixtures/does-not-exist.json` | reported missing and did not invent file contents | PASS |
| Tool failure | fake timeout then fake success, maximum two attempts | recovered on second simulated response | PASS |
| Interrupted session | saved JSON with goal, done, next, constraints | re-read same state | PASS |
| Completed practical arithmetic | fictional 3 × £125 + 2 × £40, and a missing-price item | £455; item with no unit price flagged | PASS |

**5/5 deterministic fixture checks passed.** The tool failure was NOT a real GitHub outage, the restored checkpoint was NOT a new AI conversation, and the quote arithmetic was NOT an end-to-end TRADEFLOW business workflow. Exact test harness and results were executed locally and are available as session artifacts; this report is a durable summary.

## Next actual agent acceptance test
Run a new Claude Code session and separate Codex session with only repository entry instructions, present each with the five *isolated fixture* challenges; log actual model, tool calls, attempted sources, output, tokens when measurable, and permission checks. For each category require both models to detect the fault and recover or accurately stop (10/10), then repeat checkpoint recovery after a real context reset (2/2). Do not modify real price lists, real customer data or production branches to trigger failures. A genuine complete-task proof additionally requires a reviewable project deliverable that passes its own acceptance checks, not merely calculation.

## Status
VERIFIED: 5/5 scripted isolated fixtures, active sources readable by GitHub connector.
NOT VERIFIED: independent Claude/Codex agent behaviour, real failed service recovery, fresh-session recovery, real TRADEFLOW quote demo completion, reliability rate across runs, latency or billed cost.
No architecture redesign.
