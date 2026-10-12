# Current focus

**Refresh by:** 2027-01-08. Every 3 months, re-read this file with Charlie,
update it, then move this date on 3 months (`tools/audit.py` warns once it passes).

**Priority (90 days, set 2026-10-08 with `grill-me`):** become confident
helping someone brand new to AI set up their own Standard AI-OS. Finish line:
a repeatable set-up kit (prompts, skills, plugins and a step-by-step plan,
built on Nate's AIS-OS kit plus our three additions, Charlie's choice 2026-10-08) that someone can follow to get the
same result every time. First 2-3 set-ups are free, for friends and family,
recorded (with their consent) for the YouTube channel. Project:
`projects/ai-os-setup-kit/`. Interview notes: `brainstorms/2026-10-08-who-i-am.md`.

**Done:** Standard AI-OS v1 (2026-10-08): router confirmed, standard
`system/standard-ai-os-v1.md`, blank copy `templates/standard-ai-os-v1/`.

**Current policy (Charlie, 12 Oct):** mandatory tool trials, smallest-version /
simpler-wins policies and the Guardian agent/review gate are removed. Verify
results directly; unavailable Claude-only review controls do not block Codex.
Historical statuses below are superseded where they mention those gates.
Plugin activation and practical-use receipts: `audits/2026-10-12-tool-policy-and-plugins.md`.

**Hand-off for a new session:** `context/handoff.md` (read it first).

**Next step (tool request, 2026-10-12):** requested policy removals and five-plugin project installation are complete on this host. Use them directly on relevant work. On a new Claude host, run `tools/install_approved_plugins.sh`, then restart/reload plugins; do not repeat the approval. Actual Mac/account runtime remains untested. Receipts: `audits/2026-10-12-tool-policy-and-plugins.md`.

**Continuation (style-guide trials, 2026-10-12):** all nine articles and nine scripts are saved in `brainstorms/2026-10-12-style-guide-test-drafts.md` with fact packets and checks alongside. Collect real beginner answers and compare understanding separately from preference. Draft checks are author review, not audience or independent approval. Current continuation: `context/handoff.md`. Existing browser/video work and the 90-day priority remain unchanged.

**OS backlog status (2026-10-09, after the re-run audit):** both middle plans are built
(one `youtube-ingest` skill; elders named by job: Architect, Quartermaster,
Chief's Desk), and every Desk card is answered or closed. The re-run audit scored
64/100 (`audits/audit-2026-10-09-112239-a7c3.md`); Charlie chose fix 1 only (this
note); fixes 2-5 stay open in that report. Next to build, in order: real model
comparisons under `system/model-usage.md` (no cheaper route is promoted yet); the
journey video was parked at that time (newer production status below). Full list: `context/todo.md`. Nate's six-phrases DM
is ingested (concept 44, Rule 44: finish with VERIFIED / NOT VERIFIED).
Later the same day: model comparisons 1-2 done (9/9 each), so `architect` and
`quartermaster` run on Sonnet with a weekly spot-check in the Friday audit; new `connect`
skill (Canva connected and proven); Small Business's 44 skills mapped in the Quartermaster
(not installed). **Approved plugins:** Marketing, Context7, Superpowers, watch-video and
claude-patterns. Project configuration and current-host checks are recorded in
`audits/2026-10-12-tool-policy-and-plugins.md`; approvals do not need repeating.
GitHub first; Notion replaces Drive. The setup-kit priority remains unchanged.

**Next step (set-up kit, paused):** `projects/ai-os-setup-kit/plan.md` is at v0.4;
the base is decided (Nate's kit plus our three additions). Next: test it on the
first friend or family set-up.
Weekly `audit` runs by itself every Friday 8:59 UK time and the Quartermaster update
every Saturday 8:47, each inside its own runner session that has the repo attached
("Weekly AI OS audit (runner)", "Weekly Hands Brain update (runner)"; fixed 2026-10-09:
the first routines had no repo and failed).

**Quartermaster weekly run (10 Oct):** 1 new video (Wsru44p-J14, 9 Oct) in W41, 16 tools; best new: Agent Reach (Desk card `qm-agent-reach`). Next run Saturday 17 Oct.

**Hands Brain window (2026-10-09, Desk):** 4 weeks of history (W38 to W41)
and stop; new videos only, through the Saturday routine.

**Parked:** Nick Saraev — his research, brain and `nick-brain` agent stay as
they are, but no Nick work while the set-up kit is the priority (v1 done; kept parked 2026-10-08).

## Open quiz
- Name the failure type: (1) old and new price lists both saved, AI quotes the
  old one; (2) finish date not written anywhere, AI makes one up; (3) notes say
  satin but customer said eggshell. Bonus: should one customer's job notes
  live in CLAUDE.md?

**Everything unfinished, in one list:** `context/todo.md`.

## Waiting on Charlie
- Brand style-guide draft commits `133ce9e` and `7557c42` are saved proposals. Files saved and read back; full audit, visual-brand inspection and runtime output tests not run. They are proposals, not an activated voice or validated engagement ranking.
- Shared browser: branch `codex/shared-iphone-browser` at `ff94d389b8dc5cd09eb58aa9cd69ae86c51d86bb`
  contains the prototype. Its recorded 16/16 tests and workspace live checks
  are not fresh checks in this session.
  existing-host access, real external HTTPS/iPhone login and fresh-environment
  restoration remain open. No public phone URL exists.
- Journey Short: branch `chatgpt/nate-video-editing-ingest-2026-10-10` at
  `9fdc528a5ed5faa204f9ca2fd864aec2b8781daa`, open PR #3, contains production
  source/evidence. Check production commit `1bb636f9806eb9d8cd2247ca98ce109974d6bf49`
  against its remaining actual media gates and republish stale pages. The
  separate-reviewer prerequisite is withdrawn. Result is NOT VERIFIED overall; a 57.736-second r5 MP4 is recorded in
  its [branch delivery record](https://github.com/eddieedwardsv2-ux/Test-environment-/blob/9fdc528a5ed5faa204f9ca2fd864aec2b8781daa/projects/youtube-channel/videos/ai-os-journey-short/delivery.json).
- Official reference/reading-efficiency commit `9f84dc96d7c6d11b43e5d6c5dcb4c78981c2e29b` has no outstanding mandatory separate-reviewer requirement. Three selective retrieval trials passed; full corpus ingestion and all-runtime reading compliance remain NOT VERIFIED. No new payment or account decision is needed.
- AI Impact ingestion commit `06acbb112e4a5b182aa31c1fdb4e87edbe1b7156` has no outstanding mandatory separate-reviewer requirement. Caption-derived corpus is saved; slides remain blocked and result is NOT VERIFIED. No payment or account decision is needed.
- Answered 9 Oct late evening: both browser routes (Claude's own browser on Mac day; Codex
  writes its shared phone-browser plan next), TinyFish removed, Higgsfield sign-in moved to
  Mac day (Charlie couldn't find a way from the phone). Open: `qm-frontend-design` (preview page to compare).
  Katana access and credits are still unverified.
- Codex's hand-off commits `975420c` and `2c52266` were checked by the Guardian (READY,
  `audits/guardian/2026-10-09-codex-handoff-merge.md`) and the pages republished.

## Parking Lot
- Journey video: the 9 Oct parking decision is history. Charlie's subsequent
  production request yielded an r5 MP4 on the media branch (11 Oct), still
  NOT VERIFIED overall. Review/integration remains open; Obsidian filming stays
  a later Mac task. See the current handoff for exact branch and result paths.
- Nick Saraev: build/ship lessons, brain-ingest of his 4 courses, his advice
  as a teaching programme (parked 2026-10-07; still parked for the set-up kit)
- Flashcards (app, new cards, review): came from Nick's teaching; parked
  2026-10-07; still parked for the set-up kit. The app and its cards stay as they are.
- Karpathy brain, then a "council" that asks Nick, Nate and Karpathy side by
  side (after the foundation gate; Karpathy's X posts and 4 transcripts saved)
- Dan Martell second-brain content (one creator at a time)
- Post the AI question in the decorators' Facebook group (see projects/youtube-channel)
- Unlisted test video for the channel
- **Mac items** (Obsidian, `3d-brain`, plugins, Codex check): all in `context/mac-day.md`, started when Charlie says "I'm on Mac"
- vidIQ (after 5 videos), Canva thumbnails (after 3 videos)
- Decorating business (parked, not deleted)

## Latest direct request — AI Impact channel ingestion (2026-10-12)
49 public caption sources processed into 342 timestamp-linked derived records, searchable SQLite and JSON: `research/ai-impact/README.md`. No slides captured; full request NOT VERIFIED.

**Next step for this request:** finish visual capture in an environment with functioning video access, beginning with 45 caption cues and then reviewing all videos for unannounced slides. This creator corpus does not change the 90-day priority or promote unverified tool claims into the OS.

## Latest direct request — official model documentation (2026-10-12)
Official Anthropic/OpenAI reference layer: `research/official-docs/README.md`. 1,959 source URLs catalogued, 117 model references, 20 first-pass teaching records; catalogue/facts saved, complete source text not durably retained. Full educational/semantic ingestion NOT VERIFIED.

**Next step for this request:** resolve empty training captures, expand actual public course/video content, and derive topic-specific knowledge with retrieval tests. Recheck changing product facts live. Previous AI Impact slide work and the 90-day priority remain unchanged.

## Latest direct request — reading efficiency (2026-10-12)
A full-file reading instruction in Architect was repaired. Small task maps now select Nate rule/concept sections and official source records. Three independent retrieval trials passed; all-runtime compliance and optimal billing remain NOT VERIFIED. Evidence: `audits/2026-10-12-selective-reading.md`.

**Next step:** repeat varied retrieval tasks in fresh Claude Code/Codex sessions, retaining a small read trace and acceptance checks. Do not load whole creator folders/catalogues for ordinary advice. Official source retention/semantic review and AI Impact slides remain open.
