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
Done since the hand-off (2026-10-08): first scored audit, 49/100 Foundation
(`audits/audit-2026-10-08-184245-b9f5.md`); audits now keep receipts;
Brain dashboard (whole repo + Nate's brain as one map, review cards); "I'm on
Mac" checklist (`context/mac-day.md`). Brain review: everything accepted for
now; only Concept 2 marked confusing (explained in chat, wording unchanged).
Set-up kit plan now v0.3 (`projects/ai-os-setup-kit/plan.md`: three
questions, one automation, the bike method; 14 days designed later); ChatGPT
export refreshed. Kit Compare v2 (two connected maps, link in the project
README). Nate-first map (https://claude.ai/artifact/BM1CEX52wfMKT5G4B8X6ky, `system/merge-map/`): our OS today vs the same
work placed by Nate's kit rules (75 of 99 dots stay put, 20 move, our blank
template not needed). The two map builders share `tools/graph_lib.py`.
Later the same day: Nate's newest video ingested (concept 39, Rule 41);
router trimmed to 76 lines, `os-audit` folded into `audit`, and every
question for Charlie now lives on the Decision Desk (`decide` skill, links in
`system/pages.md`).
**First thing next session:** run the `decide` skill's "read answers" step
and act on what Charlie sent. Open cards: base kit, trimming the kit's thick
skills, which new Nate videos to ingest, `/doctor`, GitHub connector.
Then: rebuild the Brain dashboard in the radial style.
Keep sessions short: hand off at about half the context window.
