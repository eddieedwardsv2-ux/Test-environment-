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
**Written 2026-10-09** at the end of the long session that built: the trimmed
rulebook (76 lines), the Decision Desk (`decide` skill), one `audit` skill with
the content check, ENATE (Nate's brain: 69 videos, 43 concepts, 43 rules), the
Hands Brain (`research/hands/`: The Next New Thing + skills.sh, 95 tools, map
view, ENATE links), the OS Guide, the lesson slides, the audit review, and the
Friday audit routine ("Weekly AI OS audit", 8:59 UK time). All links:
`system/pages.md`. History: `decisions.md`.

**First thing:** run the `decide` skill's "read answers" step. Open card:
"enate-merge" (merge ENATE's overlapping rules; see
`research/nate-herk/brain/overlap-review.md`).

**Waiting on Charlie:** add Higgsfield as a custom connector
(`https://mcp.higgsfield.ai/mcp`, guide `references/higgsfield-api.md`);
finish the Canva sign-in. Connectors load only when a session starts.

**Suggestions offered, not yet chosen:** one home page for all pages; refresh
the Watch Path and the two oldest lessons; mark Kit Compare as decided; a
weekly Hands Brain routine; the round Brain map.

Keep sessions short: hand off at about half the context window.
