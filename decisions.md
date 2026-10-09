# Decision log

## 2026-10-09 — Quality-first usage and actionable Hands review
Charlie asked to continue implementation after the connected GitHub write
route succeeded. Added Search / Check / Implement and notes to the Hands
review panel, preserving decision history with unique request IDs, visible
status and a labelled device-only export fallback. Shared owner permissions,
visual QA and publication remain a Claude-side check, not claimed complete.

Replaced the blanket cheaper-helper rule with system/model-usage.md: define
quality first, trial candidates, escalate rejected outputs, count total work,
and one lead integrates bounded independent helpers. Active Claude agents
inherit the main model by default; no cheaper production route is promoted.
One isolated extraction fixture matched its nine expected fields on both
small and strong comparator models; costs and broader reliability unmeasured.
Updated FreeLLMAPI review for the reported limit stop and current source
limitations. No external provider installed, paid calls made or credentials
collected. Source corrections: Context Mode licence; startup-offer capacity.
Report and receipts: audits/2026-10-09-usage-hands-check.md.

## 2026-10-09 — Include Creative Claw in YouTube production
Charlie requested finding and adding Creative Claw for future YouTube flows.
Matched the existing Hands Brain entry to CreativeClawCo; added connection
preflight and first-trial steps to the channel README and capability map.
Plugin not connected in this session. No spending or publishing authorised
by this route alone.

## 2026-10-09 — Notion replaces Google Drive
Charlie explicitly requested dropping Google Drive and using Notion whenever
Drive would previously have been used. GitHub remains the project entry
point. Updated the router, connections, capability map and ChatGPT export.
ChatGPT removal returned "not installed"; Claude connection status remains
unverified. No content migration or deletion performed.

Newest first. One line per decision: date — decision — why.
This is history: what's true now is in `AGENTS.md` and
`context/current-focus.md`. A later entry can supersede an earlier one.

- 2026-10-09 — **ChatGPT's hand-off checked by Claude**: its two commits (Notion instead of Drive, Creative Claw route, quality-first model use, Hands review controls) are in and the audit passes. Claude fixed a bug its mocked tests missed (the Hands save buttons only connected after a filter chip was tapped; export used a download link artifact pages block), republished the Hands Brain with saving on, and proved a save/read/close round trip with a test entry (deleted). The Friday audit did not run: the routine fired at 08:59 UK and failed on the usage limit. Two leftover Sonnet notes updated to the new model rule.
- 2026-10-09 — **Claude vs Codex parity tested** (Charlie, after comparing our kit with Nate's): one rulebook for both is proved for Claude (a fresh Claude with no file access answered 5/5). Found and fixed: `link` was hidden from Claude by a flag from Nate's kit. `tools/audit.py` now fails on hidden skills and on a broken `.agents/skills` link (proved by planting the fault). Codex fallbacks written into `AGENTS.md`; the real Codex run waits for the Mac. Report: `audits/evidence/2026-10-09-parity-test.md`.
- 2026-10-09 — **Hands Brain ranking uses our own verdict** (Charlie asked why FreeLLMAPI was a top pick): relevance is now capped by the newest sighting's `our_view.need` (yes 3, maybe 2, no 1), and "Use these now" skips tools Charlie marked later or drop and lists need = yes first. FreeLLMAPI fell from 2nd to 6th; review `research/hands/reviews/freellmapi-2026-10-09.md` (not a use-now tool: needs a computer running it, many sign-ups, sends work to free providers; optional Mac-day trial). Journey video: Notebook replaced by a Mix style from Charlie's notes; his style notes saved as channel voice notes.
- 2026-10-09 — **ECC researched: ideas adopted, nothing installed** (Charlie asked to research and install it): ECC is a 293-skill coding kit with hooks on 7 events, so installing it would break Rule 41 (smallest context) and clash with our Stop-hook gate. Three of its ideas were written in instead: a "done when" check before building and READY / NOT READY at the end of big tasks (`context/working-rules.md`), and scoring a lesson before it becomes a rule (`content-check.md`). Review: `research/hands/reviews/ecc-2026-10-09.md`; Charlie's verdict on the Desk ("ecc-verdict").
- 2026-10-09 — **Five Desk answers acted on** (Charlie, about 6am): (1) **end-to-end test** run in a fresh headless Claude session: router → Nate's brain → checked quote, works; Codex not installed here, so on paper only; gap found: no rule for stepping up to a stronger model (`audits/evidence/2026-10-09-end-to-end/`). (2) **Hands Brain stops at 4 weeks** (W38-W41), new videos only (supersedes the "back day by day to W38" order). (3) **Prices, steps 1-2, our own data**: `price` split into `open_source` / `repo` / `cost` in every week file; 13 real prices from our transcripts; skills.sh tools now "public code", not open source; no category #1 changed. (4, 5) **Elder names by job, one YouTube ingester**: plans written (`brainstorms/2026-10-09-middle-plans.md`), nothing renamed or merged yet; Desk card "middle-go" asks to go ahead.
- 2026-10-09 — **Decision Desk map view** (Charlie: choose which question first, see them all without one big list, most important stands out, Claude's 1st and 2nd subtly marked): "Waiting" opens on small tiles grouped by area, bigger when a card decides others ("Decides 3 others"), amber edge and "Claude's 1st/2nd suggestion" on two picks with a reason; tap a tile to answer that one. New card fields `short`, `weight`, `unblocks`, `pick`, `pickWhy` (documented in the `decide` skill). Tested with sample cards on phone and desktop, no errors.
- 2026-10-09 — **i-have-adhd installed** (Charlie): skill only, into this project (not its plugin, which adds a start-up hook); checked first (MIT, 55,849 stars, 24,300 installs, file read in full, nothing outside the repo changed). Runs only when he types `/i-have-adhd`.
- 2026-10-09 — **HyperFrames and prices** (Charlie, Desk notes): HyperFrames left as "later" (he couldn't view the video in the app; revisit with the first short). Prices: split "open source" (a licence) from cost model (free, pay per use, monthly, yearly, one-off), learn from our own data first; plan in `research/hands/improvement-plan.md`, start on card "price-plan".
- 2026-10-09 — **Desk answers acted on (4 cards)** (Charlie): Hands Brain hides what he already has (ours or built into Claude), every "use now" tool has a head-to-head, grey "skills.sh only" tag that drops off once a video shows the tool, Saturday routine "Weekly Hands Brain update" (8:47 UK). HyperFrames tried for real (10-second title card, rendered in 14 s) and the new `try-tool` skill built from that run; trial kept out of the repo (21 skills, about 6,000 characters a message). Presenters' opinions now on every video W38 to W41 (115 tools: they'd use 64, we disagree on 29), kept per tool, per week and in one voice summary; voice-file quotes now checked by `tools/audit.py`. Charlie switches off 9 unused claude.ai skills; the weekly audit checks whether any were missed. New ENATE page; main maps rebuilt after every run.
- 2026-10-09 — **Hands Brain order clarified; presenter opinions added** (Charlie): newest video first, then back day by day to W38 (older ones add context and catch old tools not yet replaced); I had misread this as "no backfill" and reverted it. New per-tool field: what the presenters think and whether they'd use it, against our own view; first step towards a "council" of brains with voices.
- 2026-10-09 — **Cheaper ingest: triage first; Voice Gym; W38 in the Hands Brain** (Charlie: save usage for when he has more to spare): `brain-ingest` now triages in tiers (titles, then descriptions and chapters checked against the brain, then a free GitHub transcript fetch, then reading only the matching chapters when he has spare time); `research/nate-herk/triage.md` lists 4 gap videos queued (CLI vs MCP, metadata, STORM research, deploy methods). Voice Gym page: 7 AI-style drafts for Charlie to rewrite, feeding `aios-intake.md` Q2. Hands Brain: 3 of 6 W38 videos (29 tools, all with head-to-heads), 115 tools. `pipeline.py` now merges instead of overwriting.
- 2026-10-09 — **ENATE clashes fixed, no merge; new-session backtest** (Charlie, Decision Desk "enate-merge": only fix the clashes): Rule 19 and concept 18 ("under 200 lines") marked as replaced by Rule 41 / concept 39 (smallest context that works); 200 lines is only the hard ceiling. Backtest `audits/evidence/2026-10-09-new-session-backtest.md`: fresh-session test 10/10, skills and agents load, scripts clean; Higgsfield not added and Canva sign-in unfinished (still Charlie's); Friday routine exists but hadn't run yet.
- 2026-10-09 — **Weekly audit scheduled** (Charlie, Decision Desk): routine "Weekly AI OS audit" every Friday 8:59 UK time, a fresh session runs the full `audit` skill, commits the report, puts any questions on the Desk, and pushes a phone notification. It has no connectors, so it attaches the repo itself (step 0 of its prompt).
- 2026-10-09 — **Audit reviewed; skills.sh added to the Hands Brain** (Charlie): `audits/2026-10-09-audit-review.md`. Claude Code's `/doctor` checks the install (Layer 0, Mac); our context doctor is now inside `tools/audit.py`. New automatic checks: every Hands Brain quote, category, ENATE link, sponsor name and stale list (proved by breaking a quote and a category on purpose: both caught). The weekly audit now also checks the Decision Desk, every page link and the model. Open: nothing starts the weekly audit (Desk card). skills.sh leaderboard is a second Hands source (`research/hands/skills_sh.py`; installs add up to 3 points).
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
