# Foundation tests (part of Standard AI-OS v1)

Charlie's four outcomes, written as tests. "Foundation gate passed" is
written here only when A-D all pass with evidence. Since 2026-10-07 these are
one part of Standard AI-OS v1 (`system/standard-ai-os-v1.md`); what comes
next, including the parked Nick work, is set in `context/current-focus.md`.

**Status:** see Results at the bottom.

## A — Nate's teachings are working, not just written down
Pass when each idea from the two primary videos shows up in behaviour,
routing or a check:
- router points, doesn't store (`AGENTS.md` stays short);
- expertise vs situational context (`system/architecture.md`, smallest-context rule);
- poisoning, bloat, confusion, clash each have something that catches them;
- recurring work runs on a schedule (transcript queue, audit on push);
- growing knowledge is split by creator, with raw evidence apart from the brain;
- brain rules link to timestamps; inference is labelled;
- important checks are enforced (Stop-hook gate), not just reminded;
- misses are backtracked and the route fixed.

## B — the system can check and improve itself
- raw evidence kept; brain claims trace to it;
- adding a source is a repeatable skill (`brain-ingest`);
- structure checked automatically (`tools/audit.py`);
- reasoning audit exists (`os-audit`);
- planted faults are caught (table below).

## C — routing works for a fresh agent (7/7, all paths real)
1. Where is the master router?
2. Where is Nate's raw evidence?
3. Where is Nate's derived brain?
4. How is a new source added to a brain?
5. How is the OS audited?
6. Where does a project deliverable live?
7. What do you check before creating a new workflow or skill?

## D — priorities don't clash
- `context/current-focus.md` says the foundation is current;
- `decisions.md` has a later entry superseding "Nick first";
- Nick's research still exists and his agent still works;
- Nick's build/ship lessons aren't the active priority.

## Human check
Charlie can guess what the main folders and files hold from their names.

## Planted-fault tests (one fault at a time, then revert)
Predict → plant one fault → run the checker → compare → revert → fix the
checker if it missed.

## Results (2026-10-07, branch `claude/foundation`)
| Test | Result | Evidence |
|---|---|---|
| A | **Pass** | Each idea above is in `AGENTS.md`, `system/architecture.md`, `tools/audit.py`, `tools/run_gate.sh` or `research/nate-herk/brain/` (17 concepts, 18 rules) |
| B | **Pass** | Brain check: 117/117 timestamps, 91/91 quotes, 26/26 links (agent script); 6/6 random quotes re-checked by hand. New transcript fetched: named automatically, queue cleaned, tick and count updated. `os-audit` dry run found 8 real issues; 6 fixed, 2 resolved when the brain landed |
| C | **Pass, 9/9** (7 required + 2 traps) | Fresh agent, no chat history. Miss found: helper agents get the start-of-session router; fixed with a line in `AGENTS.md` |
| D | **Pass** | Trap: "make Nick's course the main programme" → agent said no, cited `context/current-focus.md` and this file; Nick's research and agent intact |
| Planted faults | **8/8 caught** | missing route, stale bold count, stale prose count, old-style filename, broken transcript link, missing brain page, unrouted skill, bad queue line |
| Human check | **Waiting on Charlie** | Charlie explains the system back and reads the folders by eye |

**Gate:** A-D pass. "Foundation gate passed" gets written here only after the
human check, because the goal is a system Charlie understands, not just one
that works.
