# Session hand-off

Overwritten at the end of each long session (Nate: one status file, rewritten
each time, not a growing log). History lives in `decisions.md`.

**Written:** 2026-10-08, end of the long Standard AI-OS v1 session (about
2,000 replies; it was handed off because each message was re-reading about
340k tokens).

## Where we started
Build a "not yet personalised" Standard AI-OS v1 from Nate Herk's teaching,
with a router (`AGENTS.md`, read via `CLAUDE.md`) that works before the
knowledge base is added.

## Decisions locked (details in `decisions.md`, newest first)
- Router confirmed as final by Charlie; ends with "Keep this router current".
- Nate's full channel audited (`audits/2026-10-08-nate-channel.md`); his brain
  covers all 55 saved transcripts (concepts 1-38, rules 1-40).
- Nate's AIS-OS kit adopted (github.com/nateherkai/AIS-OS, MIT): skills
  `onboard`, `audit` (weekly, scored on the Four Cs), `link`, `level-up`,
  newer `grill-me`; `connections.md`, `aios-intake.md`,
  `references/3ms-framework.md`, `EXPANSIONS.md`.
- 90-day priority: the AI OS set-up kit for beginners, built on Nate's kit
  (`projects/ai-os-setup-kit/`). Nick and flashcards parked.
- Charlie's working style: no forced quizzes or explain-backs; don't repeat a
  question he hasn't answered; plain UK English; end with **Now:** /
  **Done when:**.

## Running state
- Branch `claude/standard-ai-os-v1` and `main` are identical; working tree
  clean; `python3 tools/audit.py` shows 0 errors.
- Saving pattern used: audit → commit (with attribution lines) → push branch
  → if `main` has no new commits, push branch to `main`.

## Open items (Charlie's call, no need to chase)
1. 8 decisions in `audits/2026-10-08-nate-channel.md` (plan mode, allow-list,
   auto mode, hand-off wording, private-info scan, challenge step, audit
   additions, network check).
2. `aios-intake.md`: Q2 writing samples (paste raw), Q5, first half of Q7.
3. Offered, not yet agreed: rename `tools/` → `scripts/`; a one-command
   `save` script.

## Pick up here
Recommended next step: run the `audit` skill once to get the first Four Cs
score (baseline in `audits/`). Then the set-up kit's step-by-step plan.
Keep sessions short: hand off at about half the context window.
