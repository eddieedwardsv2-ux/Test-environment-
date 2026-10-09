# Audit review: is the audit itself checking the right things? (2026-10-09)

Charlie asked for a health check on the audit system: did we learn `/doctor`,
does it fit, and are the agents in each part of the brain being checked
properly. Receipts: the commands and outputs below, plus
`audits/evidence/2026-10-09-backtest/report.md`.

## /doctor: what we learned
There are two different "doctors":

| Doctor | Checks | Where it runs | Fits our audit as |
|---|---|---|---|
| Claude Code's `/doctor` (`claude doctor` on the command line) | The Claude Code install, settings, updates. Interactive `/doctor` also flags context and MCP problems. | Ran here 2026-10-08: only the cloud container's install (3 container warnings, nothing about the repo). Useful on the Mac. | **Layer 0**: on Mac day and after Claude Code updates (`context/mac-day.md`) |
| Our context doctor `tools/context_check.py` | Everything loaded into every message: rulebook, skill and agent descriptions, hidden instruction files, hooks | Anywhere | **Now automatic**: `tools/audit.py` section 7 turns its warnings into audit warnings (since 2026-10-09) |

## The layers, after today's fixes
| Layer | What | When | Automatic? |
|---|---|---|---|
| 0 | `/doctor` (install) | Mac day, after updates | No (Charlie types it) |
| 1 | `tools/audit.py`: routes, links, counts, partial transcripts, brain contract, skill routing, front matter, secrets, quotes, **Hands Brain**, **context size** | Every push (GitHub) and before any agent finishes (Stop hook) | Yes |
| 2 | `audit` skill: weekly Four Cs score with receipts, plus its content check (clash, bloat, stale facts, backtrack) | Fridays, big changes, model switches | **No: nothing starts it** (Desk card asked) |
| 3 | Backtest: re-run real questions against what was built | After a big build | By hand |

## Each part of the brain: who builds it, who checks it
| Part | Built by | Checked by | Gap found | Status |
|---|---|---|---|---|
| Rulebook and routes | main session | audit.py §1, §4b; fresh-session test | none | OK |
| ENATE (Nate's brain) | `brain-ingest` helpers | integration step + every quote checked automatically (§5) | none | OK |
| Nick's brain (parked) | same | same | none | OK |
| **Hands Brain** | one helper per week | before today: only the helpers' own self-checks and the backtest | **quotes, categories, ENATE links and freshness were not checked automatically**; two helpers handled a sponsor differently | **Fixed**: audit.py §6 checks every quote (week files and Nate's mentions), every category, every ENATE link, sponsor names, and warns when the list needs rebuilding |
| Decision Desk | `decide` skill | nothing (its data lives on the page, not in the repo) | answered cards could sit unactioned | **Fixed**: the weekly audit now lists the cards and flags answered-not-closed and open over 7 days |
| Dashboards | builders + republish | backtest only | a page could fall behind its data | **Fixed**: weekly audit opens every `system/pages.md` link; audit.py warns when the Hands list is stale |
| Skills and agents | main session | §2d routing, front matter; trigger tests in the backtest | trigger tests are manual | Open (fine for now: re-run when a skill is added) |
| Model switches | n/a | content check "after a switch" | nothing notices a switch | **Fixed**: each weekly report records the model; a change triggers the content check |

## Proof the new checks work (predict, run, compare)
Prediction: breaking one Hands quote and one category gives 2 errors and a "rebuild" warning.
```
ERROR research/hands/weeks/2026-W40.json: Paperclip quote not in transcript CQhWqUOouYM: "this sentence was never said in the video"
ERROR research/hands/weeks/2026-W40.json: Hindsight has unknown category 'Made up group'
WARN  research/hands/tools.json is out of date with the week files ...
audit: 2 errors, 1 warnings
```
Matched. File restored; `python3 tools/audit.py` → `audit: 0 errors, 0 warnings`.

## Still open
1. Nothing starts the weekly scored audit: Decision Desk card "weekly-audit-routine".
2. The last scored audit is 2026-10-08 (49/100, Foundation). The next one should score after these fixes.
