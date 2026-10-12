# Research experiment 2 — simplest reliable AI-OS architecture
Date: 2026-10-12

## Decision
**Keep the existing AI-OS architecture. No redesign and no new dependency justified.** Describe its working functions as route → retrieve → execute → verify → record; these are descriptive, not renamed components or new policy gates.

## Selective GitHub evidence
- `AGENTS.md`: shared router, selective task-specific reading, verification, and tools.
- `CLAUDE.md`: `@AGENTS.md` import avoids instruction divergence.
- `system/architecture.md`: existing router, research brain, skills, deterministic tools, project scope, cadence.
- `context/current-focus.md`: current TRADEFLOW demo remains priority.
- AI Impact `research/ai-impact/videos/zmrPY6S1FwY.md` timestamps https://www.youtube.com/watch?v=zmrPY6S1FwY&t=291s indexing before browsing; linked markdown entities; separate numerical data.
- AI Impact `research/ai-impact/videos/z02Y-1OvWSM.md` https://www.youtube.com/watch?v=z02Y-1OvWSM&t=434s typed links; https://www.youtube.com/watch?v=z02Y-1OvWSM&t=307s reports 600 vs 9,000 tokens, NOT reproducibly verified.
- AI Impact `research/ai-impact/videos/8mL3D6ku8MQ.md` https://www.youtube.com/watch?v=8mL3D6ku8MQ&t=244s human sign-off; https://www.youtube.com/watch?v=8mL3D6ku8MQ&t=831s numerical datasets outside the knowledge prose.
- Nate `research/nate-herk/lesson-smallest-context.md`: task-specific skills and minimal sufficient context; source primary https://www.youtube.com/watch?v=Ek1NBfnnTH0 .
- The Next New Thing `research/the-next-new-thing/free-on-github-manage-agents-11labs-alternative-incredible--CQhWqUOouYM-transcript.md` https://www.youtube.com/watch?v=CQhWqUOouYM&t=92s Paperclip is for managing tasks/permissions across agents, not an automatically necessary foundational layer. Usage cost of models is separate.
- Official format https://agents.md/ supports predictable repository instructions and scoped overrides.
- Anthropic official guidance https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/prompt-templates-and-variables supports clear success criteria, sourced research, proportional use of specialised agents.

## Disagreements
Nate emphasises smaller always-loaded context. AI Impact adds structured typed knowledge graphs, durable session records and organisation-wide promotion. The Next New Thing profiles broader orchestration (Paperclip) after teams accumulate many agents. These differ chiefly in operational scale. A knowledge graph database and separate orchestration platform are not shown necessary by the studied sources.
AI Impact 600 vs 9,000 token benefit is a creator claim; no independent backtest here. AI Impact corpus is caption-derived, slides not captured.

## Actual verification run: 9/9 structural GitHub retrievals
Connected GitHub API fetched the first 12 lines successfully for:
1. AGENTS.md
2. context/current-focus.md
3. context/handoff.md
4. research/ai-impact/index.md
5. system/capability-map.md
6. tools/audit.py
7. projects/README.md
8. CLAUDE.md
9. system/architecture.md

**9/9 structural route targets retrievable.** This is not a simulation of the agent's reasoning; routes could exist yet be ignored, stale or misinterpreted.

## Test plan (next live checks)
1. 5 fresh-session route questions in both Claude and Codex, 10 trials: current priority, where client data belongs, where research lives, how to use a skill, how to record outcome. Require 10/10 correct with brief file-read traces.
2. Five cross-creator retrieval queries; compare top selected 3–5 source records with expert gold answers. Require recall >= 90%, 100% provenance, no unsupported claims and documented context size.
3. Three real tasks: one deterministic calculation with error input, one research synthesis resolving contradictory sources, one safe reversible project change. Require 3/3 outputs inspected with saved receipts.
4. Deliberately add stale/contradictory evidence in *isolated test fixtures only*; verify 5/5 tests detect contradiction and use current priority without modifying real project files.
5. Interrupted session recovery: three fresh-session restarts; require 3/3 correct active goal, constraints and next step from handoff.
6. Verify user decision recording and use through existing Desk, permissions and logs, including no action before required authorisation.
7. Measure context bytes/tokens for each run and compare to naive full-folder retrieval; optimisation wins only if accuracy remains at least equal.
8. Record cost, runtime and errors; distinguish static availability checks from live executions and beginner comprehension.

## Status
Research comparison and **9/9 structural retrieval checks VERIFIED**.
Fresh-session autonomous routing, useful retrieval, task execution, contradiction detection, real recovery, correct approval flow and context-efficiency improvement: **NOT VERIFIED** in this experiment.
No files changed except this research report. No architecture or plugin changes.
