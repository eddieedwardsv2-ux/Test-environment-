# Session hand-off

One status file, rewritten at the end of each long session (Nate). History:
`decisions.md` and this file's Git history. Every agent (Claude, Codex,
ChatGPT) reads this and updates it before stopping.

**Written:** 2026-10-09, about 5am UK, end of the long 9 October session.

## Where things stand
- **Proven working (receipts in `audits/evidence/2026-10-09-new-session-backtest.md`):**
  the router (fresh-session test 10/10), `tools/audit.py` on every push and
  before finishing, the Decision Desk, the GitHub transcript queue, the tools
  brain pipeline, the maps, quote checking.
- **Not yet proven:** the two weekly routines ("Weekly AI OS audit" Fri 8:59 UK,
  first run today; "Weekly Hands Brain update" Sat 8:47 UK), Codex in this repo,
  the ChatGPT side, the Voice Gym (no rewrites yet), `try-tool` (one run), the
  set-up kit on a real person.
- **Theory only:** the "middle", the council of elders, model routing.

## Built on 9 October
- **ENATE page** (Nate's brain on its own map) beside Charlie's Brain and the
  Hands Brain. Rule: rebuild and republish all three after every run.
- **Hands Brain:** 21 videos (14 Sep to 8 Oct), 117 tools; head-to-heads;
  owned tools ticked; grey "skills.sh only" tag; presenters' opinions on 115
  tools (they'd use 64, we disagree on 29) in `research/hands/voices/`.
- **HyperFrames tried** (10-second title card, 14 s render), kept out of the repo;
  new `try-tool` skill built from that run.
- **Voice Gym** page (7 practice messages to rewrite), feeds `aios-intake.md` Q2.
- **Cheaper ingest:** `brain-ingest` triages first; 4 Nate gap videos transcribed,
  waiting in `research/nate-herk/triage.md` until Charlie says "ingest the queue".
- **Fixes:** capability map now lists connectors and built-in skills (why tools
  were missed); ENATE Rule 19 replaced by Rule 41; pipeline no longer drops videos.
- All links: `system/pages.md`.

## Charlie's thinking (in his words: `brainstorms/2026-10-09-charlies-thoughts.md`)
1. **Learn in the most streamlined way**, save usage for when there's spare.
2. **Find his voice:** the Voice Gym.
3. **Newest first, older for context**; the tools brain will have more sources
   (next: Anthropic's community plugin marketplace).
4. **Council of elders:** each brain gets a voice (Nate's too, so "Nate" and
   ENATE become one), named by its job, giving input on what's best, optimal,
   safest and properly audited.
5. **The "middle":** is the routing clear, and where is the brains' middle?
   Also what are our head, hands and desk (desk = Mac-day context, later).
   **Discuss before changing anything.**
6. **One YouTube ingester skill** for every brain.
7. **Nate's kit from his newest thesis backwards**, plus Boris Cherny (named in
   10 of Nate's transcripts, the source of the "10x Claude" thesis) and Karpathy.
8. **Claude and ChatGPT/Codex in step:** both must hear about each other's work
   at every hand-off. Gap found: a non-Claude session changed `AGENTS.md` at
   04:04 on 9 Oct with no log entry.
9. **Is it working or theory?** See "Where things stand".
10. **A kit for blank accounts:** core thesis, routes, workflows, skills and
    plugins, no ingested data (`projects/ai-os-setup-kit/`, the 90-day priority).
11. **Lessons to YouTube:** a pipeline from lessons to shorts, filming prompt
    cards and edit plans; first short next.
- Also saved, not started: ChatGPT's model-routing prompt
  (`brainstorms/2026-10-09-model-routing-handoff.md`), the same theme as 5.

## Waiting on Charlie (Decision Desk, 7 open cards)
next-big-step (what first; recommended: end-to-end test in Claude and Codex) ·
elder-names · youtube-ingest · hands-window (stop at 4 weeks, or 3 months) ·
hyperframes-verdict · hands-prices (24 unknown) · and his own steps: switch off
9 claude.ai skills; add Higgsfield (`https://mcp.higgsfield.ai/mcp`) and finish
Canva's sign-in (check `ListConnectors` before promising either).

## Pick up here
1. Read the Desk answers (`decide` skill).
2. Check the Friday audit left a new report in `audits/` (after 8:59 today).
3. Talk through the "middle" with Charlie before acting on items 4 to 8.
4. Then do what "next-big-step" says.

Keep sessions short: hand off at about half the context window.
