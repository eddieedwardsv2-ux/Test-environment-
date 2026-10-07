# Decision log

Newest first. One line per decision: date — decision — why.
This is history: what's true now is in `AGENTS.md` and
`context/current-focus.md`. A later entry can supersede an earlier one.

- 2026-10-07 — **Park Nick; build Standard AI-OS v1 from Nate** (supersedes
  "Foundation first" below as the current priority): a not-yet-personalised
  router + filing cabinet made only from Nate Herk's teaching, audited
  against his videos before any knowledge base is added. Nick's research and
  agent stay but are parked — Charlie wants a correct standard router first.
- 2026-10-07 — **Foundation first** (supersedes "starting with Nick" and
  "Karpathy and Nate brains after Nick's" below): the AI-OS routing +
  knowledge foundation from Nate's two primary videos ("Steal My Exact AI OS
  Setup", "I Built Another Andrej Karpathy Using Claude") must pass the tests
  in `system/foundation-tests.md` before Nick's build/ship lessons become the
  active priority. Nick's research and agent stay as they are. Karpathy brain
  and the council wait in the Parking Lot — Charlie's A-D outcomes, worked
  out with ChatGPT's audit of this repo.
- 2026-10-07 — Transcript files named `<title>--<video-id>-transcript.md`
  (named automatically from the transcript's title; tools find files by ID)
  — Charlie should be able to read folders by eye; the ID stays for tools.

- 2026-10-07 — Build Karpathy and Nate brains lean, in the background, after
  Nick's; ChatGPT gets the same rules via exports/chatgpt-instructions.md —
  Charlie wants all three teachers' ways of working in every AI he uses.
- 2026-10-07 — Adopt Karpathy's 7 rules (via Nate) as how every agent works
  and teaches; enforce rule 5 with a Stop-hook run gate (tools/run_gate.sh
  runs the audit before an agent may finish) and a `teach` skill that checks
  its own answer against all 7 — Charlie flagged the rules were overlooked.
- 2026-10-07 — Build creator "brains" (knowledge base + advisor agent),
  starting with Nick Saraev — Charlie wants Nick's thinking available
  alongside the OS, grounded in sources (Nate's Karpathy-brain idea).
- 2026-10-07 — Automatic audit (tools/audit.py) on every push; manual checks
  in proportion to risk — checks were too heavy on small edits, too light
  on things only remembered.
- 2026-10-07 — Spending rule: free first, but under ~£5-10 is fine when the
  knowledge is worth it (Nate pulled all of Karpathy's X posts for ~$1) —
  saves repeating the same workarounds. Charlie approves each spend.
- 2026-10-07 — X: free tool default raised to 25 pages (~6 months); full
  history via TwitterAPI.io (~$0.15/1,000 posts) only if needed.
- 2026-10-07 — Transcript queue run hourly by GitHub Actions — YouTube blocks
  all data centres (GitHub too), but the free transcript service limits per
  IP, so GitHub's runner adds its own allowance. No phone, sign-up or Mac.
- 2026-10-07 — Flashcards: no scoring, no rescheduling; app shows right/wrong
  only, with New and Practise-all modes — Charlie doesn't want wrong answers
  to hold him back or a judging system to maintain.
- 2026-10-07 — Suggest plugins proactively from all 9 families (rule in
  AGENTS.md, shortlist in research/plugin-map.md) — Charlie can't ask for
  tools he doesn't know exist.
- 2026-10-07 — Flashcards: multiple choice in plain English; prompts only at
  milestones (lesson or build finished, or 5+ due), not every reply; the app's
  database is the single source of truth (flashcards.md is a backup) — Charlie
  found questions unclear and per-reply quizzes too frequent; two card lists
  would "clash" (Nate's failure mode).
- 2026-10-07 — Daily 18:59 UK flashcard check (Routine "Flashcard check",
  trig_01MjF4jCRr9MHQbbmeuryFYS) messages Charlie in this session when cards
  are due — flashcards should come to him, not wait to be remembered.
- 2026-10-07 — Flashcards reviewed in a Claude artifact app (spaced repetition,
  results in its database) — Charlie wanted interactive screens; Claude can
  read results back to target weak spots. flashcards.md stays the question list.
- 2026-10-07 — Connect the Anthropic community plugin marketplace in project
  settings but install nothing yet — all 2,284 plugins one command away
  without slowing every session down.
- 2026-10-07 — X posts via FxTwitter's free API (research/get_x_posts.py).
- 2026-10-07 — Keep this repo public until the Mac arrives — Charlie is happy with that; nothing private goes in (see AGENTS.md rule).
- 2026-10-07 — Work in one long cloud session until the Mac arrives — the
  chat continues, but the workspace can still be wiped when idle, so every
  change is pushed to GitHub straight away.
- 2026-10-07 — Organise this repo as a level-1 "filing cabinet" (CLAUDE.md as
  router + context/, projects/, decisions) with research/ as a level-2 wiki —
  Nate Herk: use the lowest level that fixes a real pain; the pains were
  re-explaining between sessions and growing research notes.
- 2026-10-07 — Router lives in AGENTS.md; CLAUDE.md imports it with @AGENTS.md (official docs pattern) — one source of truth so
  Claude Code and Codex never get different instructions.
- 2026-10-07 — Transcripts via youtube-transcript.ai (free, no sign-up) —
  YouTube blocks cloud servers; tested 9+ alternatives first.
- 2026-10-07 — Install only Anthropic-reviewed or well-known skills/plugins,
  and only when a real problem needs them.
- 2026-10-07 — Focus: learn Claude Code and Codex and build a YouTube channel
  as a learner; decorating business parked. Income is not the immediate worry.
