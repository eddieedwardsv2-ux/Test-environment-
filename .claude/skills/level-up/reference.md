# level-up: background and checks

Moved out of SKILL.md so it loads only when needed. Adapted from The Three Ms of AI™ © 2026 Nate Herk (MIT kit, see `THIRD-PARTY-NOTICES.md`).

## What it does
Walks the user through the 3Ms each week to surface and ship one new automation. One interview = one artifact. After 4-6 runs the user starts spotting opportunities mid-week because the questions become internal defaults. The kit relies on `/level-up` running every Friday, not on cron jobs.

## What it is NOT
- Not `/audit`. `/audit` is structural ("is the AIOS built right?"); `/level-up` is functional ("what leverage am I missing?"). Run `/audit` first if structure is messy.
- Not a multi-candidate planner. One run = one shipped artifact.
- Not a coach. The user does the thinking; the skill conducts the interview.

## When it runs
- First run: Day 14, after at least one MCP/script is connected and `/audit` has run once. Earlier gives trivial output.
- Cadence: weekly, Friday afternoon. Review the week, surface one automation, ship Monday.
- On demand any time, e.g. mid-week when a manual task itches.

## Critical rules (restated)
1. One interview = one artifact.
2. Mindset phase always runs first, even with a pre-formed idea.
3. EAD enforces "eliminate first". Eliminate is a win, not a failure.
4. Default to the lowest autonomy level that works. Push back on L4.
5. Boring-is-Beautiful default in Machine handoff: highest non-AI option.
6. Tie-to-KPI is mandatory: no bucket and metric, the skill stops.
7. Bike Method ships into every artifact (`bike-method-phase: 1`).
8. Limit edits to the decisions log and the selected artifact. A selected audit repair may update its existing workflow or routing files; preserve unrelated content.
9. Every report and scaffolded artifact references the framework.

## Verification (for the implementer)
- Dry run with no prompt: expect 2-3 candidates drawn from recent activity, priorities and top pain. Generic output ("you should build a brief") = fail.
- Eliminate-first test: feed an obviously eliminable candidate. Expect Eliminate, exit, win logged.
- L4 push-back test: user asks for an autonomous email-replier on first build. Expect L1/L2 first, no L4 without explicit override.
- Boring-is-Beautiful test: a candidate solvable with deterministic Python should default to option 2, deterministic skill.
- Bike Method anti-skip: user asks to jump to Phase 4 straight after scaffolding. Expect them to read each phase and confirm lower phases are validated.

> *The Three Ms of AI™ is a trademark of Nate Herk. © 2026 Nate Herk. All rights reserved.*
