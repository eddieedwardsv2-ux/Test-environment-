# Session hand-off

One status file, rewritten at the end of each long session (Nate). History:
`decisions.md` and this file's Git history. Every agent (Claude, Codex,
ChatGPT) reads this first and updates it before stopping.

**Written:** 2026-10-09, about 6am UK, end of the long 9 October session.
**Updated:** 2026-10-09, about 05:29 UK, by the session that ran the 5 Desk answers (sections 3-5).
Charlie's own words for everything below: `brainstorms/2026-10-09-charlies-thoughts.md`.

## Latest steering (2026-10-09, ChatGPT)
- Hands map/ranked review now has Search / Check / Implement controls in
  source, with 14 adapter tests passing; backed by the artifact tool_actions collection with device-only
  fallback/export. Republish Hands and test a real save/read/close round trip
  before calling it live; session pickup route: `research/hands/README.md`.
- Creative Claw requested for the next YouTube production session; route and
  first trial in `projects/youtube-channel/README.md`. Installation/sign-in
  remains incomplete; no credits spent or output tested.
- GitHub first; ignore the old Google Drive START HERE instructions. Use
  Notion for work previously routed to Drive. ChatGPT removal reported Drive
  not installed; this does not revoke a separate Claude connection.
- Scoped system check and source review are in `audits/2026-10-09-usage-hands-check.md`.
  `system/model-usage.md` now defines evidence gates, bounded escalation and
  fan-out/fan-in; active Claude helpers default to inherit. One fixed-input
  comparison passed 9/9 fields on both gpt-6-luna and gpt-6-astra. This is a
  synthetic smoke test, not production promotion or proven cost savings.
- Next: in a signed-in Claude session republish Hands and validate one real
  owner save/read/close round-trip, then run held-out real model comparisons.
  Check the Friday audit routine: no new report appeared on main by the
  11:13 UK continuation; execution itself is unverified, not proven failed.
- GitHub writes work through the connected integration; see environment.md.
  Command-line push lacks credentials. The private Claude session needs sign-in.

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
  the Decision Desk, the transcript queue, the Hands pipeline, the maps, quote
  checks, and now the **end-to-end path in Claude** (fresh headless session:
  router → Nate's brain → checked quote; `audits/evidence/2026-10-09-end-to-end/`).
- **Not yet proven:** both weekly routines (first runs Fri 9 Oct 8:59, Sat 10 Oct
  8:47), **Codex** (not installed in the cloud; repeat the test on the Mac:
  command in the report), the ChatGPT side, the Voice Gym, `try-tool`, the set-up kit on a real person.
- **Still unproven:** the middle and council. Model routing now has a written
  quality/step-up policy and one narrow smoke test (latest steering above);
  production equivalence and savings remain unmeasured.
- **Known gap:** a non-Claude session changed `AGENTS.md` at 04:04 on 9 Oct with
  no log entry (item 8). Also: another Claude session was pushing to main at the
  same time as this one (journey video drafts); pull before every push.

## 4. Desk answers (all 5 closed 2026-10-09 with outcomes)
- **next-big-step → end-to-end test:** done (Claude works; Codex on paper).
- **hands-window → stop at 4 weeks:** in `hands-ingest` and `current-focus.md`.
- **price-plan → steps 1 and 2:** done; `research/hands/improvement-plan.md` (bottom).
  Step 3 (web lookups for the 35 unknowns) not chosen.
- **elder-names, youtube-ingest:** plans only, in `brainstorms/2026-10-09-middle-plans.md`.
  **Open card "middle-go"** asks: go ahead (ingester first, then names), one only, or talk first.
- **Also open on the Desk:** "journey-video-style" (from the other session).
- **His steps still open:** switch off 9 claude.ai skills (Settings, Skills: built-in-browser,
  chrome-browser, computer-use, import-memory, morning, docx, xlsx, pptx, pdf); add Higgsfield
  (`https://mcp.higgsfield.ai/mcp`) and finish Canva's sign-in (check `ListConnectors` first);
  rewrite a few Voice Gym messages.

## 5. Plan for the next session (in order)
1. Follow the `i-have-adhd` style in replies; read the Desk (`decide` skill) first.
2. Check the Friday audit report in `audits/` (routine ran 8:59 UK, 9 Oct) and act on it.
   (Not done this session: it ran at about 05:20, before the routine.)
3. **If "middle-go" is answered:** build the plan he picked from
   `brainstorms/2026-10-09-middle-plans.md` (ingester first: move steps, no
   script changes, re-run last week's ingest, `git diff` must match); re-run the
   end-to-end test after any rename. If he picked "talk", start with its 4 questions.
4. Rebuild and republish the main pages, update this file, commit and push.
5. Later, one at a time: keep Claude and Codex/ChatGPT in step (re-run the
   end-to-end test in Codex on the Mac); model routing talk (ChatGPT's prompt; the
   step-up gap); the council (Nate's voice first, research Boris Cherny); the
   Anthropic plugin marketplace as the tools brain's next source; the kit for blank
   accounts (keep Charlie's base-kit note: audit each set-up until the returns stop,
   a wiki brain from past chats plus an interview, voice from 3 emails, articles or
   stories); the first YouTube short.

## 6. Also open (checked 2026-10-09; don't lose these)
- **From another session:** at 04:04 on 9 Oct a non-Claude session added
  `research/corey-haines/` (Corey Haines' marketing skills compared with NewsJack)
  and a router line for it, with no `decisions.md` entry. Review it with Charlie,
  log it, and decide if it feeds the tools brain. (It is also the proof for item 8.)
- **ChatGPT's copy of the rules** (`exports/chatgpt-instructions.md`) was last synced
  2026-10-08; re-sync as part of 5b.
- **Grok Bot video** (Nate, MgvwZaDPCs4) behind ChatGPT's routing prompt: not in our
  video list or transcribed yet; triage it before that prompt is run.
- **Voice Gym follow-up:** once Charlie has rewritten 5 or more, Claude writes his
  voice notes into `aios-intake.md` Q2 (the base-kit note: voice from 3 emails,
  articles or stories).
- **Higgsfield:** once Charlie adds the connector, make one small test image (say the
  credit cost first).
- **The "desk" name:** if the Mac workspace becomes "the desk", the Decision Desk may
  need another name. Part of the middle talk.
- **Claude's theory of where this is heading** (collect, try on real work, keep what
  wins, teach, set others up): offered as the "why" for `context/current-focus.md`;
  Charlie hasn't confirmed it.
- **ENATE tidy:** Rules 2 and 3 and concepts 19 and 28 aren't linked to each other
  (as written, not from today's changes).
- **Older open items** (Charlie's call, no need to chase): 8 decisions in
  `audits/2026-10-08-nate-channel.md` (plan mode, allow-list, auto mode, hand-off
  wording, private-info scan, challenge step, audit additions, network check);
  `aios-intake.md` Q2, Q5 and half of Q7; offered, not agreed: rename `tools/` to
  `scripts/`, a one-command save script, one home page for all pages, refresh the
  Watch Path and the two oldest lessons, mark Kit Compare as decided, the round Brain
  map; the "Thread Notes No1" page isn't listed in `system/pages.md` (check with Charlie).
- **Routines running:** "Weekly AI OS audit" (Fri 8:59), "Weekly Hands Brain update"
  (Sat 8:47), "Flashcard check" (daily 18:59, though flashcards are parked).

Keep sessions short: hand off at about half the context window.
