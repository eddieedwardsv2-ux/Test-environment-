# Session hand-off

Overwritten by `session-handoff`; history stays in `decisions.md` and Git.

## Latest handoff — brand engagement and style-guide planning
**Written:** 12 October 2026, 11:30 UK, by ChatGPT/Codex. Charlie requested /sessions-handoff. Research paused before completed engagement analysis or style-guide drafts.

### Working on
Research large, engaged AI/education brands and plan a few style guides for future outputs. Charlie selected **AI and education**, rather than major consumer brands or a mix. This direct request does not change the existing 90-day priority.

### Summary points
- Compared relevant saved Nate and AI Impact teaching: shared routing, selective context, source-to-concept processing, evidence links, repeatable workflows, scoped rules and predict/run/compare. AI Impact slide coverage remains missing; agreement does not prove performance.
- Brand shortlist: Kurzgesagt, Veritasium, 3Blue1Brown, Fireship, Nate Herk, Matt Wolfe/Future Tools and AI Explained. This is a candidate set, not an exhaustive biggest-brand ranking.
- Direct public YouTube channel pages returned rounded subscriber labels: Kurzgesagt 25.7m; Veritasium 21.4m; 3Blue1Brown 8.69m; Fireship 4.29m; Nate 1.06m; Matt 1.02m; AI Explained 455k. Treat these as a dated snapshot, not engagement measurements.
- Public SPEAKRJ pages supplied example views, likes and comments for Kurzgesagt, Veritasium, Fireship, 3Blue1Brown and AI Explained. Format/age are not yet controlled. No highest-engagement verdict or median-rate comparison completed.
- Creator websites inspected for positioning. Fireship describes approachable developer learning; 3Blue1Brown emphasises visual understanding; Kurzgesagt describes approachable complex topics through vector illustration/animation; Veritasium describes experiments/interviews/demos; Future Tools curates AI news/tools; Nate teaches practical AI automation.
- Proposed directions, not approved final guides: practical teaching; visual explanation; evidence-led analysis. Borrow techniques and develop Charlie's voice, rather than copying another brand.
- A temporary Python scan initially found subscriber labels but no videos because YouTube now used lockupViewModel rather than videoRenderer. Parser correction started; completion/results were not retrieved before the workspace tool failed. No raw scan/script is durably saved or required to resume.
- Automatic approval review rejected workspace write_stdin/polling due to a usage-limit review failure, not a safety determination. Do not bypass/retry the rejected workspace action. No paid research/transcript services used.

### Key files / where information lives
- This section holds the complete durable research starting point; no style-guide draft file exists yet.
- Nate: research/nate-herk/README.md; lesson-smallest-context.md; steal-my-exact-ai-os-setup-5-simple-tips--Ek1NBfnnTH0-transcript.md; i-built-another-andrej-karpathy-using-claude--bvGptCLDhyo-transcript.md.
- AI Impact: research/ai-impact/index.md and videos/spT1e-1LpHc.md, z02Y-1OvWSM.md, xUnVQkPrnrA.md, _X5jSMka5e4.md, sOkUzrjeO5s.md, 8mL3D6ku8MQ.md, yP4p3reZUcU.md. Caption-derived summaries; creator claims unverified.
- Brand primary sources: https://kurzgesagt.org/ ; https://www.veritasium.com/ ; https://www.3blue1brown.com/about/ ; https://fireship.dev/ ; https://futuretools.io/ ; https://www.nateherk.com/ . Channel handles: @kurzgesagt, @veritasium, @3blue1brown, @Fireship, @mreflow, @nateherk, @aiexplained-official.
- Secondary video metrics: https://www.speakrj.com/audit/report/UCsXVk37bltHxD1rDPwtNM8Q/youtube/media-stats ; UCHnyfMqiRRG1u-2MsSQLbXA ; UCsBjURrPoezykLs9EqgamOA ; UCYO_jab_esuFRV4b17AJtAw ; UCNJ1Ymd5yFuUPtn21xtRbbw (substitute each channel ID in the same URL).
- Prior work, open decisions and branches remain in the reconciliation below; context/todo.md and current-focus.md remain authoritative for their status.

### Decisions made / open decisions
Charlie chose AI/education references. No guide direction chosen yet; no need to re-ask the sector. Assume future articles, videos and guides as initial applications, but confirm formats if the choice materially changes the drafts. No current Desk answers were read in this session; preserve prior unknown/open decisions.

### Pick up here
1. Finish a bounded comparison on one platform (YouTube first): sample ten recent non-Shorts uploads per candidate, record IDs/publication times/durations/views/likes/comments and capture time. Flag missing fields and format differences; exclude very new uploads or use a common age window. Compare median views and median (likes + comments)/views; views/subscribers is a reach proxy, not engagement or retention. Public data cannot establish saves, shares, watch time or causal reasons for success.
2. Inspect a small matched set of actual content per shortlisted brand (transcripts and visuals where accessible). Extract hook, structure, sentence rhythm, evidence use, visual hierarchy and calls to action. Separate observed patterns from hypotheses about engagement; use existing Nate/AI Impact corpus selectively.
3. Present three concrete guide briefs with example openings on the same topic: practical teaching (Nate + selective Fireship concision), visual explanation (3Blue1Brown/Kurzgesagt), evidence-led analysis (Veritasium/AI Explained). Include audience, voice, visual rules, output-specific adaptations and quality checks. Do not claim full guides, visual inspection or performance tests until completed.

### Verification / carried forward
GitHub documents were reread against latest main commit 81d3e0b before saving. Existing handoff preserved verbatim below; nothing dropped or closed without proof. Branch/Desk inventory was not freshly rerun here; use the prior reconciliation as recorded evidence, not a new verification. Workspace audit/page-build could not run after the usage-limit review failure; Claude artifact publishing unavailable. Handoff saving is a separate claim from research quality/independent review. Research/style guides remain NOT VERIFIED.

---

## Current reconciliation — 12 October 2026, ChatGPT
This section supersedes stale status statements in the historical 9 Oct handoff
below. Checked main `c0f2437`, remote branch tips and PR #3; no implementation
branches merged, no hosting or social publishing performed.

### Pick up here
1. Independent Claude Guardian: cover main's outstanding commits from `e210980`
   onwards (baseline audit 11 missing-review errors / 0 warnings), then review
   browser/media branch work against their recorded gates. Do not claim approval
   from the worker's test receipts.
2. Browser branch `codex/shared-iphone-browser`, tip
   `ff94d389b8dc5cd09eb58aa9cd69ae86c51d86bb`: prototype exists. Read its
   [browser README](https://github.com/eddieedwardsv2-ux/Test-environment-/blob/ff94d389b8dc5cd09eb58aa9cd69ae86c51d86bb/projects/shared-browser/README.md), `progress.md`, `verification.md`.
   Recorded 16/16 tests and live workspace checks; not rerun here. External
   hosting, actual iPhone/third-party login, fresh-task restoration and Guardian
   remain unverified. No public phone URL. Existing-host access is the deployment
   blocker; preserve user control and request no passwords in chat.
3. Media branch `chatgpt/nate-video-editing-ingest-2026-10-10`, tip
   `9fdc528a5ed5faa204f9ca2fd864aec2b8781daa`, open
   [PR #3](https://github.com/eddieedwardsv2-ux/Test-environment-/pull/3): real r5
   1080×1920, 57.736-second MP4 recorded. Read branch
   [branch result](https://github.com/eddieedwardsv2-ux/Test-environment-/blob/9fdc528a5ed5faa204f9ca2fd864aec2b8781daa/projects/youtube-channel/videos/ai-os-journey-short/result.md) and
   `delivery.json`; production commit `1bb636f9806eb9d8cd2247ca98ce109974d6bf49`.
   G16/full audit and independent Guardian remain open, as does page republishing.
   No social publishing. Review and integrate deliberately: both branches diverge
   from main, so copying their old context files would discard later research.

### Other live continuations
- AI Impact: 49 caption sources / 342 derived records; zero verified slides.
  Continue visual capture from `research/ai-impact/HANDOFF.md`.
- Official sources: 1,959 URLs / 117 model references / 20 teaching records;
  no complete durable original-text mirror. Missing lessons/reference content
  and semantic review in `research/official-docs/HANDOFF.md`.
- Selective reading: three trials passed; fresh Claude/Codex runtime behaviour
  and billing savings unverified. `audits/2026-10-12-selective-reading.md`.
- Desk wake and tool-action live round-trip remain open; current Claude artifact
  answers were inaccessible here. Never infer present decisions from 9 Oct's
  "none open" snapshot. Setup kit v0.4 remains the 90-day priority.
- WIP `x-themes.md` remains on `claude/nate-brain-wip`. No branch deleted.
- Latest Actions commit `c0f2437` changed AI Impact's research-table count to 0
  while the creator's derived 49-caption corpus remains saved. Use its creator README/HANDOFF for actual coverage.

### Verification of this reconciliation
- `git diff --check` passed; all three documentation files reviewed against
  the branch results. Implementation tests and media playback were not rerun.
- `tools/pages_status.py --build` rebuilt five stale pages locally. No Claude
  artifact publishing tools are available here; no publication mark changed.
  Only the three session records are saved in this documentation commit.
- Main's baseline audit has 11 existing missing-Guardian errors. Generated
  page staleness is recorded above; independent review remains outstanding.

### Carried forward / dropped
No open item dropped. The historical handoff and later research additions are
retained below; `context/todo.md` keeps Mac tasks, plugins, parked projects,
Elder fault trials, model routing and the remaining tool/session loops.

## Historical handoff — 9 October 2026
**Written:** 2026-10-09, about 22:55 UK, by Claude; Charlie ran `/session-handoff` to end the day.

## Working on
Nothing half-done. Tomorrow (10 Oct): close the broken loops and prove the system works,
Guardian paused until then (`context/current-focus.md`, top).

## Summary points
- Desk tells Claude with no connector: Send saves `poke.json` inside the Desk, waking sessions that watch it (63567f5). Saving proven from Charlie's phone; the wake itself unproven.
- Elder pilot trial 1: frontend-design via council + Guardian (53d899d); Charlie's verdict **Later** (`research/hands/tried.json`).
- Quartermaster: Nate's 30 tools are now a source (25 added, 187 tools, gold rings) (55e5725); it and the Architect read each other's files (e210980; live from this next session).
- Router steps measured: 85 of 99 notes within 2 steps, none unreachable (`tools/route_depth.py`); names checked against the rules: three skill descriptions use the new names (30ff0c2).
- Pages: `system/published.json` + `tools/pages_status.py`; republish once per run (19f716c, e210980).
- Codex's hand-off merged and checked (eaa3db3, 60c23f2). TinyFish removed by Charlie.

## Key files
- `context/current-focus.md` (10 Oct plan), `context/todo.md`, `decisions.md` (top entries)
- `audits/2026-10-09-advisors-and-router.md`, `audits/2026-10-09-pages-and-links-check.md`
- `.claude/agents/quartermaster.md`, `.claude/agents/architect.md`, `.claude/skills/decide/SKILL.md`
- `tools/build_hands.py` (source 4), `tools/route_depth.py`, `tools/pages_status.py`, `tools/check_links.py`

## Where the information lives
- Priority: `context/current-focus.md`; everything unfinished: `context/todo.md`; Mac-only steps: `context/mac-day.md`.
- Desk, pages and rebuild steps: `system/pages.md` (Desk watched at session start: `decide` skill).
- Guardian reports: `audits/guardian/`; last scored audit `audits/audit-2026-10-09-112239-a7c3.md` (64/100).
- Codex's browser research (TinyFish profiles, LinuxServer Chromium/Selkies, Browserbase) and Higgsfield CLI notes: `git show 2c52266:context/handoff.md` and `references/higgsfield-api.md`; the CLI lived at `/workspace/higgsfield-tools/` in Codex's instance.

## Decisions made
- Guardian paused until the end of 10 Oct (warns, not fails; back 11 Oct by itself).
- Both browser routes: Claude's own browser on Mac day, and Codex writes its shared phone-browser plan (approval before any build or spend).
- frontend-design: Later. Bitcoin newsletter: side project. Pages republished once per run.
- Check the Quartermaster before tasks that make something or need a tool.

## Open decisions
- Desk: none open (checked about 22:50).
- Higgsfield sign-in (Mac day; Charlie couldn't find a way from his phone); Katana access and exact credit cost unverified; never ask for tokens in chat.
- Codex's browser plan: written plan only, for Charlie's approval.
- Branch `claude/nate-brain-wip` keeps one unverified file ([unverified X themes](https://github.com/eddieedwardsv2-ux/Test-environment-/blob/314fb9c973e2104da2baba422303c8fa58a1ebff/research/nate-herk/brain/x-themes.md)).

## Pick up here
1. Claude: watch the Desk, then test the loop: Charlie presses Send on a test card and the session wakes; then test the real `quartermaster` and `architect` once each (todo).
2. Close the other loops in current-focus (audit hole on merges first: a Guardian line should only clear its own ancestors). On 11 Oct the first Guardian run covers commits from `e210980` on.
3. Codex: write the shared phone-browser plan (nothing built or paid before approval); Higgsfield resumes once signed in (Mac day), quote before any spend.

## Carried forward / dropped
- From Codex's hand-off: browser plan (step 3), prototype and test before hosting (todo), Higgsfield/Katana (step 3, Open decisions), research links (Where the information lives), branch WIP (Open decisions). Desk `qm-frontend-design` and `shared-browser-design` closed with outcomes. Nothing dropped.

## Additional handoff — AI Impact (2026-10-12)
Direct channel-ingestion request: `research/ai-impact/README.md`. 49 public videos, 49 English caption sources processed, 342 derived records, searchable SQLite + JSON, topic backlinks. Captions worked through native `youtube-transcript-api`; historical keyless endpoint now asks for a key. No paid tools used.

Visual downloads/storyboards returned HTML error pages and browser playback stayed black. No slides captured. 45 caption visual cues are a starting list, not full slide coverage. `research/ai-impact/HANDOFF.md` preserves evidence, retrieval rules and the next visual pass. Full request NOT VERIFIED. Prior handoff items above remain open.

## Additional handoff — official references (2026-10-12)
`research/official-docs/README.md`: 1,959 source URLs (1,745 body captures, 212 landing-only, 2 empty), 117 model-reference extracts, 20 teaching records from selected sections of seven pages. Saved source catalogue/derived facts and compressed SQLite; original full text stays in temporary working cache, not a durable mirror. Independent review corrected pricing-table context, hidden mapping gaps and false empty-capture success. Full user request remains NOT VERIFIED. See `research/official-docs/HANDOFF.md` for exact limits and next work. Prior pending tasks above remain open.

## Additional handoff — task-specific reading (2026-10-12)
`audits/2026-10-12-selective-reading.md`: Architect previously required whole rules.md/concepts.md (~26K rough tokens). It now selects complete relevant sections through `research/nate-herk/brain/retrieval.md`. Official docs uses `topics.md` or a bounded query; large index is human browsing. Three independent source-grounded question trials passed; universal compliance and billed usage savings are unverified.
