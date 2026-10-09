# Session hand-off

One status file, rewritten at the end of each long session (Nate). History:
`decisions.md` and this file's Git history. Every agent (Claude, Codex,
ChatGPT) reads this first and updates it before stopping.

**Written:** 2026-10-09, about 5:30am UK, end of the long 9 October session.
Charlie's own words for everything below: `brainstorms/2026-10-09-charlies-thoughts.md`.

## 1. Charlie's thinking (the big picture)
1. **Learn the most streamlined way.** Claude works faster than watching videos;
   save usage for when there's more to spare.
2. **Find his own voice.** He has no stories yet, so he practises on AI-style
   messages (the Voice Gym).
3. **Newest first, older for context.** Newest videos matter most; older ones
   add relations and catch old tools nothing newer has replaced.
4. **A council of wise elders.** Each brain gets a voice (Nate's too, so "Nate"
   and ENATE become one), named by its job, advising on what's best, optimal,
   safest and properly audited (security and safety).
5. **The "middle".** Is the routing clear? What are our head, middle, hands and
   desk (desk = Mac-day context, not learnt yet)? **Discuss before changing anything.**
6. **One YouTube ingester skill** that feeds every brain.
7. **Nate's kit rebuilt from his newest thesis backwards**, with Boris Cherny
   (Claude Code's creator, named in 10 of Nate's transcripts, the source of the
   "10x Claude" idea and the router-at-the-entry idea) and Karpathy.
8. **Claude and ChatGPT/Codex in step**, so neither is left behind at a hand-off.
9. **Prove it works, not theory.**
10. **A kit for blank accounts:** core thesis, routes, workflows, skills and
    plugins; no ingested data (the 90-day priority, `projects/ai-os-setup-kit/`).
11. **Lessons to YouTube:** lessons into shorts, filming prompt cards, edit plans.
- Saved, not started: ChatGPT's model-routing prompt
  (`brainstorms/2026-10-09-model-routing-handoff.md`), the same theme as 5.

## 2. What we did on 9 October
- **Backtest of the new session:** router test 10/10; connectors load (Higgsfield
  never added, Canva sign-in unfinished).
- **ENATE:** clashes fixed (Rule 19 replaced by Rule 41); its own map page; cheaper
  ingest (triage first; 4 gap videos transcribed, waiting in
  `research/nate-herk/triage.md` for "ingest the queue").
- **Hands Brain:** 21 videos (14 Sep to 8 Oct), 117 tools; head-to-heads; tools he
  has are ticked and leave the ranking; grey "skills.sh only" tag; presenters'
  opinions on 115 tools (they'd use 64, we disagree on 29) with a voice summary
  in `research/hands/voices/`; Saturday routine "Weekly Hands Brain update".
- **Tried for real:** HyperFrames (10-second title card; marked "later", revisit
  with the first short); new `try-tool` skill from that run.
- **Installed:** `i-have-adhd` (skill only; type `/i-have-adhd`, "stop adhd mode").
- **Voice Gym** page (7 practice messages; none rewritten yet).
- **Fixes from two double-checks:** wrong counts corrected; capability map and
  `connections.md` now list connectors and built-in skills (why tools were
  missed); Rule 19 had dropped off the maps (fixed, and the audit now checks
  it); Voice Gym no longer hangs outside claude.ai.
- **Pages kept current after every run:** Decision Desk, Charlie's Brain, ENATE,
  Hands Brain (`system/pages.md`).

## 3. Where things stand
- **Proven:** the router, `tools/audit.py` on every push and before finishing,
  the Decision Desk, the transcript queue, the Hands pipeline, the maps, quote checks.
- **Not yet proven:** both weekly routines (first runs Fri 9 Oct 8:59, Sat 10 Oct
  8:47), Codex in this repo, the ChatGPT side, the Voice Gym, `try-tool`, the
  set-up kit on a real person.
- **Theory only:** the middle, the council, model routing.
- **Known gap:** a non-Claude session changed `AGENTS.md` at 04:04 on 9 Oct with
  no log entry (item 8).

## 4. Waiting on Charlie
- **Decision Desk, 5 open cards:** next-big-step (what first), elder-names,
  youtube-ingest, hands-window (stop at 4 weeks or go to 3 months), price-plan
  (split "open source" from cost, our own data first).
- **His steps:** switch off 9 claude.ai skills (Settings, Skills: built-in-browser,
  chrome-browser, computer-use, import-memory, morning, docx, xlsx, pptx, pdf);
  add Higgsfield (`https://mcp.higgsfield.ai/mcp`) and finish Canva's sign-in
  (check `ListConnectors` before promising either); rewrite a few Voice Gym messages.

## 5. Plan for the next session (in order)
1. Charlie types `/i-have-adhd`, then "read the hand-off".
2. Read the Desk answers (`decide` skill) and act on them.
3. Check the Friday audit left a report in `audits/` and the Saturday Hands run
   worked; fix anything they found.
4. **Talk through the middle** (item 5) with Charlie. Nothing in items 4 to 8
   changes before that talk.
5. Then the first big job from "next-big-step". Recommended order:
   - a. **End-to-end test** in Claude and Codex (router to brain to answer): proves
     what works and answers the routing prompt's first question.
   - b. **Keep Claude and Codex/ChatGPT in step** (one session-end rule for every
     agent, an audit warning when the router changes with no log entry).
   - c. **Names and the council:** rename by job, write each elder's voice file
     (Nate first), research Boris Cherny.
   - d. **One `youtube-ingest` skill**, then add the Anthropic plugin marketplace as
     the tools brain's next source.
   - e. **Prices and licences** (if "price-plan" says go).
   - f. **Kit for blank accounts**, rebuilt from Nate's newest thesis backwards.
   - g. **First YouTube short:** script, filming prompt cards, edit plan, HyperFrames titles.

Keep sessions short: hand off at about half the context window.
