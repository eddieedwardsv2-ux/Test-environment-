# Claude vs Codex: same rulebook, same routes? (2026-10-09)

Charlie: "check you, Claude, actually have the same access and routing as
AGENTS.md does, like Nate's starter kit does." Run as plan → test → build,
the way we said we'd work (`context/working-rules.md`, "done when" first).

## Plan and "done when"
| # | Check | Done when |
|---|---|---|
| 1 | Claude loads the rulebook | A fresh Claude with **no file access** answers rulebook questions correctly |
| 2 | Claude sees every skill and helper | Its list matches `.claude/skills/` and `.claude/agents/` |
| 3 | Claude follows routes to the brains | A fresh Claude reaches the right brain file and gives a checked quote |
| 4 | Codex gets the same things | Each part has a Codex route, or a written fallback |
| 5 | Faults can't come back unseen | A planted fault makes `tools/audit.py` fail |

## How Nate's kit does it, and how we do it
Nate's kit keeps **two identical copies** (`CLAUDE.md` and `AGENTS.md`, "update
both together") and a script (`scripts/sync-codex-skills.sh`) to copy skills
into `.agents/skills/`. We keep **one** rulebook: `CLAUDE.md` imports
`@AGENTS.md`, and `.agents/skills` is a link to `.claude/skills`, so the two
can't drift.

## Results
| # | Result | Receipt |
|---|---|---|
| 1 | **Pass.** 5/5 right with no file access: reply ending, the `decide` skill and Desk, ENATE, `system/pages.md`, the Claude-only note | `claude -p … --allowedTools ""` (this session) |
| 2 | **Fail → fixed.** `link` and `i-have-adhd` were hidden from Claude (`disable-model-invocation: true`). `i-have-adhd` is meant to be Charlie-only; `link` is a skill the rulebook expects agents to use, so it was a real routing gap (it came that way from Nate's kit). Removed the flag; a fresh Claude then answered "YES, `link` is in my available skills" | before/after `claude -p` runs |
| 3 | **Pass.** Router → `context/working-rules.md` → `brain/index.md` → concepts and rules → transcript; quote checked word for word | `audits/evidence/2026-10-09-end-to-end/` (other session; not re-run, as the re-run hit Charlie's usage limit) |
| 4 | **Partly: on paper.** Codex isn't installed here. See table below | — |
| 5 | **Pass.** Put the `link` flag back on purpose: `ERROR … is hidden from Claude`; restored: 0 errors | `tools/audit.py` section 8 |

## Claude vs Codex, part by part
| Part | Claude | Codex | Status |
|---|---|---|---|
| Rulebook | `CLAUDE.md` → `@AGENTS.md` (proved, test 1) | reads `AGENTS.md` itself | Same file |
| Skills | `.claude/skills/` | `.agents/skills` → same folder (audit now checks the link) | Same |
| Helper agents (ENATE, Hands, tutor) | `.claude/agents/` | none | **Fallback written:** open the agent file and follow it |
| End-of-turn audit gate | Stop hook | none | **Fallback written:** run `tools/audit.py` yourself; GitHub runs it on every push for both |
| Blocked commands | deny list in `.claude/settings.json` | Codex's own sandbox and approvals | Check on Mac day |
| Decision Desk | ArtifactData | can't reach it | **Fallback written:** "Waiting on Charlie" in `current-focus.md`; next Claude session moves it to the Desk |

## Build (only what the tests asked for)
- `link` skill visible to Claude again.
- `tools/audit.py` section 8: errors if a skill is hidden from Claude (except the
  Charlie-only list) or if `.agents/skills` stops pointing at `.claude/skills`.
- `AGENTS.md`: one rule, "Same routes in Codex", with the three fallbacks.

## READY / NOT READY
**READY for Claude.** **NOT READY for Codex:** the fallbacks are written but not
run, because Codex isn't installed here. That test is on the Mac-day list
(`context/mac-day.md`, the Codex check).
