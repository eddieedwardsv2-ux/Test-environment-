# Model comparison 1: repo look-up questions (pre-declared 2026-10-09, before any run)

**Task class:** answer a question about Charlie's AI OS by reading this repo (what the
`architect`, `quartermaster` and lookup helpers do all day). Read-only.
**Baseline:** the main model (`inherit`). **Candidate:** Sonnet (`model: sonnet`).
Same prompt, same tools (general-purpose helper, read-only by instruction), one run each.
**Pass rule (system/model-usage.md):** every critical check passes: right answer, a file path
as evidence, and "not in the repo" for the missing-data question (no invented number).
One wrong or invented answer = candidate rejected for this task class.

| # | Question | Right answer | Evidence file | Kind |
|---|---|---|---|---|
| 1 | Which file is the only place Charlie's current priority lives? | `context/current-focus.md` | AGENTS.md | easy |
| 2 | In the Quartermaster ranking, how many points does a tool get for being in Anthropic's *official* plugin catalog, and how many for the community one? | official +2, community (or knowledge-work) +1 | tools/build_hands.py | recent change |
| 3 | Which tool ranks #1 in the "Business & finance" category of the Quartermaster? | Claude for Small Business | research/hands/tools.json | data |
| 4 | On what date do the old names (ENATE, Hands Brain, Decision Desk) stop being aliases? | 2026-11-09 | AGENTS.md or context/todo.md | easy |
| 5 | How many subscribers does Charlie's YouTube channel have? | Not in the repo (channel not launched / no figure) | n/a | missing data |
| 6 | Which of Nate's rules says to finish with VERIFIED / NOT VERIFIED, and which concept supports it? | Rule 44, concept 44 | research/nate-herk/brain/rules.md | hard (newest) |
| 7 | When does the weekly audit run by itself, and where does it run? | Fridays 8:59 UK time, in its own runner session with the repo attached ("Weekly AI OS audit (runner)") | context/current-focus.md | multi-part |
