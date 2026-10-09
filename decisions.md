# Decision log

Newest first. One line per decision: date — decision — why.
This is history: what's true now is in `AGENTS.md` and
`context/current-focus.md`. A later entry can supersede an earlier one.

- 2026-10-09 — **Hands Brain map, OS Guide, ENATE name, backtest** (Charlie): Hands Brain site gets a Map view like Charlie's Brain (categories as hubs, tools, links to ENATE concepts, gold rings for tools Nate uses: `research/hands/enate-links.json`, `nate-mentions.json`). Charlie now calls Nate's brain **ENATE**; "Nate" is the real person. New plain-English OS Guide (`system/guide/`). Backtest of the 8 October work (`audits/evidence/2026-10-09-backtest/`): all passed except one ambiguous trigger (fixed in `hands-ingest`) and one loose "replaced by" (advisor now caveats it).
- 2026-10-08 — **Decision Desk answers acted on; Hands Brain started** (Charlie): base kit = Nate's kit plus our three additions, with his note (audit each set-up until returns stop, a wiki brain from past chats and an interview, voice from 3 emails, articles or stories) in plan v0.4; level-up (176→60 lines) and find-skills (144→19) trimmed, onboard parked in `references/parked-skills/`; all 13 newer Nate transcripts ingested (concepts 40-43, Rules 42-43); `/doctor` researched: `claude doctor` only checks the cloud install, so `tools/context_check.py` is our context doctor (about 8,000 characters load every message, no hidden files); GitHub connector not needed (`gh api` reads Actions runs). New: Hands Brain (`research/hands/`, `hands-ingest` skill, `hands-brain` agent, site), fed by The Next New Thing week by week from descriptions (free tool lists) plus transcripts.
- 2026-10-08 — **Questions move to the Decision Desk; router trimmed; one audit skill** (Charlie: "any time you give me decisions to make you need to create some kind of browser… so I am not being asked so many questions"): new `decide` skill and Decision Desk page (`system/pages.md`); small, easy-to-undo work is done without asking. Applied Nate's smallest-context proposals 1-4 and 6: `AGENTS.md` 93→76 lines (~8,100→4,800 chars), dashboards to `system/pages.md`, `os-audit` folded into `audit` (`content-check.md`, also after model switches), 6 long descriptions cut. Fresh-session test before/after matches (`audits/evidence/2026-10-08-smallest-context/`). Trimming the kit's thick skills and the other choices are Desk cards.
- 2026-10-08 — **Newest Nate video ingested; set-up kit paused for a cleaner brain** (Charlie: "pause that agenda", "I need a cleaner brain"): 14 newest transcripts saved; oz2CwrPV2Rg ingested as concept 39 / Rule 41 (smallest context that works, prune after every new model), checked against Anthropic's article. Clean-up proposals in `research/nate-herk/lesson-smallest-context.md`, none applied yet.
- 2026-10-08 — **Nate-first map built** (Charlie asked to see our OS as if we'd started from Nate's kit): `system/merge-map/`, rules in `tools/build_merge_map.py` (his router and EXPANSIONS.md). Result: 75 of 99 dots stay put, 20 move (system/, tools/, learning/, exports/, decisions.md), os-audit folds into /audit, our blank template isn't needed. No files moved in this repo: it would break checked routes for looks only. Map builders now share `tools/graph_lib.py` (Kit Compare output checked identical).
- 2026-10-08 — **Set-up plan v0.3** (Charlie): session 1 is built on three questions (what annoys you about AI, what do you wish it could do, one thing to automate today with a start-to-finish process) and ends with one automation in training-wheels mode plus Nate's bike method (`references/3ms-framework.md`). The 14-day follow-up is designed later. Kit Compare rebuilt as two connected maps (ours above Nate's on a phone, side by side on a computer).
- 2026-10-08 — **Set-up plan v0.2** (Charlie): test set-ups are free but each person pays for their own Claude plan, in return for honest opinions on old AI vs the new way (before/after questions in the session, day-14 opinion); one 90-minute session. Base kit still open; Kit Compare page built to decide it (recommended: Nate's kit plus one rulebook, the fresh-session test and the research guide from ours).
- 2026-10-08 — **Set-up kit plan drafted** (Charlie: "do both"): `projects/ai-os-setup-kit/plan.md` v0.1, built on Nate's AIS-OS kit and Claude Code on the web (phone-friendly): prep, 7-step session with a done-when each, weeks 1-2, day-14 checks, lessons loop. 3 open questions for Charlie in the file. Also refreshed `exports/chatgpt-instructions.md` (Four Cs, no forced quizzes; closes AIOS-b9f5-02).
- 2026-10-08 — **Brain review: all cards accepted for now** (Charlie: "all the view cards, accepted for now"). Only Concept 2 (expertise vs situational context) was marked confusing; explained in chat, brain wording left as is. Re-review later from the dashboard if anything changes.
- 2026-10-08 — **Brain dashboard replaces the Brain Map** (Charlie: "plan sounds good", after showing Nate's Herk Brain): one page maps every .md in the repo plus Nate's 38 concepts and 40 rules as a connected graph (links, backtick routes, video citations), with a one-card review tab. Same link and `flags` database. Obsidian waits for the Mac (`context/mac-day.md`, triggered by "I'm on Mac") because it ignores our backtick routes and needs paid Sync for the iPhone.
- 2026-10-08 — **Audits keep receipts** (Charlie: "Go"): each `audit` run saves `audits/evidence/<run-id>/` (commands with real output, phone and desktop screenshots of pages checked), and every score names its receipt; no receipt = unverified. Why: the first audit's evidence existed only in chat. Connector checks record "read OK" only (public repo).
- 2026-10-08 — **Adopted Nate's AIS-OS kit** (Charlie: "Approve ai os";
  github.com/nateherkai/AIS-OS, MIT, commit ce9cb93): skills `onboard`,
  `audit` (Four Cs rubric v2, now the weekly audit), `link`, `level-up`, newer
  `grill-me`; `connections.md`, `aios-intake.md`, `references/3ms-framework.md`,
  `EXPANSIONS.md`. Why: our OS over-built Context and skipped Connections,
  Cadence and a scored audit. `os-audit` kept for failure modes and backtrack.
  Kept on purpose: committed audits and brainstorms (cloud sessions wipe
  uncommitted files), `decisions.md` (one decisions file), `research/`.
  Not copied: `3d-brain` (Parking Lot), the kit's scripts.
- 2026-10-08 — **Router ends with "keep this router current"** (Charlie: "Add
  it"): update the router in the same turn when a file moves, a folder is
  added or a project starts. Added to the blank template too. Came from a
  "Memory · Level 2: build router files" prompt Charlie shared; the rest of
  that prompt we already had.
- 2026-10-08 — **Router confirmed as final** by Charlie ("Router confirmed"),
  after the full-channel Nate audit and the 8/8 router-to-brain retrieval
  test. Standard AI-OS v1 is complete. The 8 audit decisions stay open in
  `audits/2026-10-08-nate-channel.md` for Charlie to pick up when he likes.
- 2026-10-08 — **Nate full-channel audit done** (`audits/2026-10-08-nate-channel.md`):
  359 videos sorted by title; 35 more read in full; 47 new rows in the
  standard (29 met, 1 fixed, 16 open, 1 declined: plan mode), 8 new "not adopted"
  entries. 8 decisions for Charlie listed in the report.
- 2026-10-08 — **New 90-day priority from `grill-me`**
  (`brainstorms/2026-10-08-who-i-am.md`): become confident setting up a
  Standard AI-OS for someone new to AI, via a repeatable set-up kit
  (`projects/ai-os-setup-kit/`). First set-ups free for friends and family,
  recorded for the channel. Standard AI-OS v1 moved to done. Privacy rule
  added to the router: other people's details, OSs and recordings in private
  repos only; their consent before YouTube.
- 2026-10-08 — **Router confirmed; no forced tests** — Charlie understands
  how the router works. Standing rule in `context/how-i-learn.md`: never force
  an explain-back or quiz; offer once at most.
- 2026-10-08 — **Router walkthrough skipped** — Charlie already knows what
  each file does; next step is personalising with `grill-me`.
- 2026-10-08 — **Charlie's choices on the Nate comparison applied**
  (`system/comparison-vs-nate.md`): R14 option B; secret scan in the audit;
  helper agents on `model: sonnet`; READMEs in every folder Charlie uses;
  quarterly priority refresh with an audit warning; run gate renamed
  "structure gate"; Karpathy rules labelled second-hand; foundation tests
  merged into the standard. Plan mode not adopted. Charlie confirmed the
  router works "for now".
- 2026-10-08 — **Nate's brain covers all 20 saved videos** (ingested the 14
  newer ones: concepts 17 → 28, rules 18 → 30). `tools/audit.py` now checks
  every brain quote that has a timestamp link against its transcript
  (110 in Nate's brain, all pass). The knowledge base the router pulls from is
  now complete for the saved videos.
- 2026-10-07 — **First weekly audit saved** (`audits/2026-10-07.md`): fixed
  stale Nate counts (brain index, nate-brain agent), parked-flashcard steps in
  4 capabilities, about-me "Now" → "Long-term goal". Router test 10/10.
- 2026-10-07 — **Applied R11, R14, X4** (all Nate requirements; reversible
  in Git; Charlie can undo any): router rules cut to one line each, details
  moved to `context/working-rules.md` (94 → 67 lines); 95%-confidence merged
  into "Aim for the outcome"; `.claude/settings.json` deny list blocks
  force-push, hard reset, git clean and `rm -rf` (tested: blocked).
- 2026-10-07 — **v1 extended to 20 Nate videos** (6 more, incl. the 6h
  Non-Coders course): 92 requirements, every quote checked. New checks in
  `tools/audit.py`: router under 200 lines (Nate's limit), skill/agent front
  matter valid. `os-audit` adds overlap and trigger tests. `.agents/skills`
  links to `.claude/skills` so Codex sees the same skills. Fresh-session
  tests: repo 12/12, template 9/9. Open for Charlie: R11 (slim router),
  R14 (95%-confidence rule), X4 (deny list in settings).
- 2026-10-07 — **Park flashcards** with the rest of Nick's teaching: focus
  stays on Nate and the OS. The app and cards stay; nothing deleted.
- 2026-10-07 — **Standard AI-OS v1 written and applied**: 66 requirements
  from all 14 saved Nate videos, each quote checked against its timestamp, in
  `system/standard-ai-os-v1.md`; blank copy in `templates/standard-ai-os-v1/`.
  Gaps fixed: `os-audit` now saves dated reports to `audits/` and runs weekly
  (Nate: Ek1 10:14, bCl 2:28:30); new `grill-me` skill saves to
  `brainstorms/` (c0k); `.env` ignored by Git (bCl 41:50); `brain-ingest`
  applies the one-year test (DTC 27:23); router asks for a session hand-off
  in `current-focus.md` (0WD 22:24). Not adopted: levels 3-5, bypass
  permissions, ingesting email/Slack, Auto Dream. The fourth core video is
  assumed to be bvGptCLDhyo (Charlie gave three links).
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
