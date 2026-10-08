# How the AI OS is built

`AGENTS.md` is the only router. This file explains the design; it doesn't
route. Source: Nate Herk's videos; the full requirement list with quotes
and status is `system/standard-ai-os-v1.md`.

## Layers (top loads first)
| Layer | Where | What goes there |
|---|---|---|
| Router | `AGENTS.md` (Claude reads it via `CLAUDE.md`) | Who Charlie is, rules for every session, where things live. Points; doesn't store. |
| Knowledge | `context/`, `research/` | Small lasting facts (`context/`); raw evidence (transcripts, X posts) and derived brains (`research/<creator>/brain/`) |
| Capabilities | `.claude/skills/`, `.claude/agents/` | Repeatable procedures (skills) and specialist advisors (agents). List: `system/capability-map.md` |
| Deterministic tools | `tools/`, `research/*.py` | Counting, fetching, checking: code, not AI reasoning |
| Cadence | `.github/workflows/` | Work that repeats on a schedule (hourly transcripts, audit on push) |
| Projects | `projects/<name>/` | Deliverables and their own situational context |

## Two kinds of context
- **Expertise:** useful in almost every session (the router, working rules,
  environment limits). Lives in the router or one hop from it.
- **Situational:** needed for one job (one transcript, one creator, one
  video project). Fetched by route when the job needs it, never preloaded.

Default: load the smallest context that can answer the task correctly.

## Four ways context fails (and what catches each)
| Failure | Meaning | Caught by |
|---|---|---|
| Poisoning | a false fact is in context | quote/timestamp checks; the `audit` content check |
| Bloat | too much loaded or searched | small router, segmented folders, smallest-context rule; the `audit` content check |
| Confusion | missing or misrouted info, so the AI guesses | `tools/audit.py` (routes and links exist), reverse routing, backtracking |
| Clash | two current sources disagree, often one stale | count checks in `tools/audit.py`; precedence rule in `AGENTS.md`; the `audit` content check |

## How knowledge flows
raw evidence (transcript) → coverage index (README ticks) → derived brain
(concepts, rules, with timestamps) → advisor agent or skill → real task →
check → audit → backtrack any miss → fix the route, knowledge or tool.

## Keep it at the lowest level that works
Level 1-2 (router + markdown wiki). No vector database, embeddings, graphs or
memory layers until a measured retrieval problem needs them.
