# Nate full-channel audit 2026-10-08

**Question:** does our AI OS follow everything Nate Herk teaches about how to
set up and run one, not just the 20 videos the standard was built from?
**Answer:** mostly yes. 35 more videos were read in full. They added 47 new
requirements: 30 already met (29 met, 1 fixed today), 16 still open and 1 we
deliberately don't follow. Nothing he says breaks the router. The open items are habits and
safety checks, not filing.

## Scope: which of the 359 videos
| Group | Videos | Treatment |
|---|---|---|
| Already in the standard | 20 | Audited 2026-10-07 |
| Saved but not yet used | 15 | Read in full today |
| Fetched today (titles about Claude Code/Codex working methods, context, tokens, skills, agents, permissions, planning, routines) | 20 | Read in full today |
| n8n and no-code tutorials (mostly 2024-25, before he moved to Claude Code) | about 144 | Left out: tool-specific, and his newer videos supersede them |
| Model tests, news, money and sales, design/video tools | about 160 | Left out by title: no OS teaching |

The rows above are counted from `research/nate-herk/videos.md`. The title sort is a judgement call:
a few left-out videos may hold a working tip. Re-run this audit when he
posts a new OS or course video.

## Method
- 7 read-only helper agents (on Sonnet), each with 1-7 transcripts and the
  standard. They reported only new or conflicting teachings, with exact quotes.
- The main session merged about 120 raw findings into 47 rows, kept the
  newest video's quote for each, and added them to
  `system/standard-ai-os-v1.md`.
- Every quote is checked automatically: `tools/check_quotes.py` passes
  148 of 148, and two planted fakes were caught.

## Decisions waiting for Charlie (recommended answer first)
1. **Plan mode (S20).** Nate says it in at least 13 of the 35 videos. You declined it
   today. *Recommend:* keep R14 option B, but use plan mode for anything
   bigger than one session.
2. **Allow-list safe commands (X6).** Fewer permission prompts, deny list
   stays. *Recommend:* yes, read-only commands only (the
   `fewer-permission-prompts` skill drafts the list).
3. **Auto mode** (in "Deliberately not adopted"). *Recommend:* not yet.
4. **Hand-off wording (H10).** Change H7's "250-300k tokens" to "about half
   the context window". *Recommend:* yes.
5. **Private-info scan (X8).** Extend the push-time secret scan to flag
   emails, phone numbers and similar. *Recommend:* yes, as warnings.
6. **Challenge step (S22).** One line in `context/working-rules.md`:
   ask the AI to attack a plan before big builds. *Recommend:* yes.
7. **`os-audit` additions (M14-M16):** a score per audit, a "model, tool
   or our setup?" first question, and a `/context` check. *Recommend:* yes.
8. **Network setting (X10):** check the cloud environment is on trusted
   domains, not full access. *Recommend:* check next session.

Open items for later (no decision needed now): K15, M13, M17, M20, S26,
H11, H15, H20.

## Not adopted (with reasons in the standard)
Auto memory and auto-capture plugins, copying CLAUDE.md to AGENTS.md,
connectors before keys, credentials in the project folder, never-expiring
all-permission tokens, auto mode, batching instructions, global skills.

## Still to do
- Done 2026-10-08: the 35 videos are in Nate's brain (concepts 29-38, Rules 31-40). Their
  teachings are already in the standard, which `nate-brain` reads.
- One transcript is cut short: 6LNlCpQPYFc stops at 33:38.
