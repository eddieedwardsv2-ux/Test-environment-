# Battle test of this session's work (2026-10-09)

Charlie: "double check all this new session's work… run tests until
diminishing returns." Plan → test → fix → re-test, stopping when a round
finds nothing new. All tests are scripts (no extra Claude runs, so none of
Charlie's usage), except where named.

## Rounds
| Round | What | Result | Fixed |
|---|---|---|---|
| 1 | `tools/fault_drill.py`: 18 planted faults (routes, imports, hidden or missing skills, Codex link, front matter, 200-line cap, secrets, brain pages, ENATE and Hands quotes, categories, sponsors, stale list, bad ENATE links, coverage counts, model rule) | **15/18 caught** | 3 gaps: secret scan saw nothing outside a Git checkout; the router could name a deleted skill; a helper could slip back to a cheaper model |
| 2 | Same 18 | **18/18** | — |
| 3 | 5 new kinds (broken note link, a page's source deleted, corrupt week file, bad queue line, focus review overdue) | **22/23** | 1 gap: a page's source file could vanish unseen |
| 4 | All 23 | **23/23** | — diminishing returns reached for the repo checks |
| Logic | Hands ranking: no tool ranks above our own verdict; "use now" holds no "later", "drop" or "need: no" tool | **Pass** (0 violations; picks led by need = yes) | — |
| Pages | Every published page is in `system/pages.md` | **Pass** (14 of 15; Thread Notes left out on purpose, private) | — |
| Routines | Last runs | **Friday audit FAILED** (usage limit at 08:59); Saturday Hands update not run yet; flashcard check runs daily though flashcards are parked | Desk card for the audit; others on the to-do list |
| Earlier today | Claude vs Codex parity (`2026-10-09-parity-test.md`), FreeLLMAPI ranking fault, the hidden `link` skill, the Hands save-button bug, the 90-line rule | all fixed and re-tested | — |

## What this proves, and what it doesn't
- **Proved:** the structure checks catch 23 kinds of mistake, each by planting it.
  The drill now runs with the audit, so a fixed gap can't quietly come back.
- **Not proved:** anything Codex does (not installed here); whether the Desk,
  Hands Brain buttons and routines work while Charlie is away (needs real use);
  the quality of answers, which only real questions and model comparisons test
  (`system/model-usage.md`).

**READY** for the repo checks. **NOT READY**: Codex, the failed Friday audit,
model comparisons. All of these are in `context/todo.md`.
