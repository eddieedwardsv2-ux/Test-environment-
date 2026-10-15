# Everything unfinished (one list, so nothing gets forgotten)

Written 2026-10-09 from `current-focus.md`, the hand-off, the Desk, Mac day,
ChatGPT's hand-off and the battle test. The priority still lives only in
`current-focus.md`; this is the full list behind it. Tick items off by
deleting them (history stays in `decisions.md`).

## Needs Charlie (Decision Desk or a setting only he can change)
- [x] PR #4 explicitly approved by Charlie and merged on 12 October 2026 (`4f5aa1c`). Removed policies and five-plugin configuration are on main; fresh main audit/doctor passed. Mac loading and external page publication remain separate checks.
- [ ] Shared iPhone browser: prototype exists on `codex/shared-iphone-browser`
  (`ff94d38`), not main. Read branch [browser verification](https://github.com/eddieedwardsv2-ux/Test-environment-/blob/ff94d389b8dc5cd09eb58aa9cd69ae86c51d86bb/projects/shared-browser/verification.md)
  and `progress.md`; integrate source after relevant functionality checks without overwriting newer main context. Finish existing-host deployment,
  externally reachable HTTPS, actual iPhone/login and fresh-task restoration
  checks. No public phone URL; no signup/payment authorised by this status update.
  Claude's separate Mac browser route remains a Mac-day task.
- [x] Approved five-plugin activation completed on this host: all five installed/enabled at project scope; live Context7 and watch-video use, plus skill applications, recorded in `audits/2026-10-12-tool-policy-and-plugins.md`. Mac/account-specific Claude runtime still needs its own load check.
- [ ] claude.ai settings: switch off 6 unused built-in skills (import-memory, morning, docx, xlsx, pptx, pdf). Keep built-in-browser, chrome-browser and computer-use: they are the browser that keeps him signed in (9 Oct)
- [ ] Higgsfield Katana draft for the AI OS map promo (cinematic glowing network for Instagram and X; started in Codex, half done; Codex installed the Higgsfield CLI, no account connected): sign in on the Mac (`context/mac-day.md`; Charlie couldn't find a way from the phone), then check Katana access and get an exact credit quote before any spend. Keep the parked journey video separate.
- [ ] Voice Gym: rewrite 5 or more messages; then Claude writes his voice notes into `aios-intake.md` Q2
- [ ] Check ChatGPT accepts the longer instructions box (`exports/chatgpt-instructions.md`, box 2 is 2,303 characters on 9 Oct; trim it if ChatGPT refuses)
- [ ] Confirm or change Claude's "where this is heading" theory for `current-focus.md`

- [ ] `aios-intake.md` Q2, Q5 and half of Q7 still unanswered

## Reminders for Claude
- After any session: run relevant output checks and the structural audit. Refresh pages whose sources changed.
- When Charlie asks how leftover decisions and parked tasks could fit into the set-up kit: go through all of them (this list, the Parking Lot, parked projects), including the Bitcoin newsletter (side project since 9 Oct; his note on the Desk)

## Next to build (in order, after the Desk answers)
0. [ ] Desk wake not proven. **Try 4 failed too (found 15 Oct):** Charlie pressed Send at 09:09 on 10 Oct (wake-test and qm-agent-reach), no session woke, and both answers sat unread for 5 days. History: (10 Oct, two tests; third try set up 10 Oct: watch slots were all 10 full, 3 freed; the Desk watch was stopped and its restart refused because the turn wasn't typed by Charlie, so Charlie's next message re-arms it, then card `wake-test`; his 04:11 Send saved the poke fine but the watch was off, so try 2 is set; try 2 (04:13) came before the re-watch; try 3 (07:05) saved the poke but the Desk watch registered at 04:14 was **gone** after the session restarted (older page watches survived), so no wake; re-watched 07:06, try 4 set. Documented fallback if try 4 fails: a Desk comment sent to Claude wakes a watching session): Send saves poke.json (22:11 and 22:13, after the retry fix) but no watching session woke, even with a freshly registered watch. Next: find out whether a page saving itself counts as a republish that wakes watchers, or find another connector-free route; never ask Charlie to press anything extra
0. [ ] Try `/goal` once on a real job with a printed, countable finish line (concept 45; docs: code.claude.com/docs/en/goal; its judge only reads the chat, so the proof must be printed)
2. [ ] Model comparisons on real work (comparisons 1-2 done 9 Oct: both 9/9; Desk card "promote-sonnet" for the two advisors) before any helper goes back to a cheaper model (`system/model-usage.md`); add the missing "step up to the stronger model" rule
4. [ ] The council (Nate's voice first; research Boris Cherny as "the Maker")
6. [ ] Set-up kit (paused): first friend or family set-up from plan v0.4
7. [ ] First YouTube Short: r5 journey MP4 produced on the media branch, open
   PR #3. Actual remaining media checks and page republishing remain open; the
   separate-reviewer gate is withdrawn;
   source/evidence and review delivery are in the branch project folder.

## Found 2026-10-09 (session review: dropped from the 9 Oct hand-off rewrite)
- [ ] ChatGPT's model-routing prompt saved, not started (`brainstorms/2026-10-09-model-routing-handoff.md`); triage the Grok Bot video first
- [ ] Quartermaster's Search / Check / Implement buttons: republished, but one real save, read and close round trip not yet tested
- [ ] Creative Claw (for YouTube production): sign-in unfinished, no output tested
- [ ] Lesson slides (NC9J9KZkE5Wb1vDKgntoGq) still use old names (Decision Desk, ENATE, Hands Brain): edit on the page
- [ ] Watch Path page's source was only on branch `nate-watch-path`; now on main at `research/nate-herk/watch-path.html`; it still names old files (`MISSION.md`), so refresh it with the two oldest lessons, then add its source to `system/pages.md`
- [ ] Repo `eddie-ed` (last pushed 8 Oct) exists on GitHub but nothing in this OS mentions it: look at it with Charlie's OK
- [ ] Older sessions in the `my-claude-skills` repo (6 Oct) ended waiting on Charlie: a "yes" to write the agency-validation research into that Second Brain; retired-repo deletions and a reply owed by a contact; lesson 1 quiz answer (four parts of an agent). Check if still wanted.
- [ ] Offered, not agreed: a one-command save script

## Waiting for the Mac (`context/mac-day.md`, starts when Charlie says "I'm on Mac")
- [ ] Clone the repo; Obsidian; Nate's 3D brain; context7 and superpowers plugins
- [ ] **Codex test**: same 5 rulebook questions, every skill listed, the three Codex fallbacks, what Codex blocks
- [ ] Small Business plugin (after Charlie's Pro upgrade): install in the desktop app, `smb-onboard`, a relevant real task
- [ ] `/doctor` on the Mac; optional FreeLLMAPI trial only if limits keep stopping sessions

## Small tidy-ups (Claude can do these; offered, not yet agreed)
- [x] (done 10 Oct: both answered with sourced, checked citations, and each read the other's files) Next session: test the real `quartermaster` and `architect` once each (their edited files load then): a tool question should get an "Architect:" line, and a design question a "Quartermaster:" line
- [ ] Use what we already have (Quartermaster, 9 Oct): improve one of our skills with `skill-creator` (its test step); run `security-review` once over the repo before a push; read `writing-great-skills` once (no install)
- [ ] One home page linking every page
- [ ] Refresh the Watch Path and the two oldest lessons (they still name `MISSION.md`, `NOTES.md`)
- [ ] Mark Kit Compare as decided; the round Brain map
- [ ] Review the Corey Haines research another session added (`research/corey-haines/`) and log it
- [ ] Triage Nate's Grok Bot video (MgvwZaDPCs4) before ChatGPT's routing prompt is run
- [ ] Architect: concepts 19 (four Cs in order) and 28 (one set of files for every tool) have no rule yet; write Rules 45-46 only if Charlie wants (Rules 2-3 now link concept 1, done 9 Oct)
- [ ] Hands Brain: the 35 tools with unknown prices (step 3 of `research/hands/improvement-plan.md`, not chosen)

## Watch-outs (things running on their own)
- [x] Re-run Friday audit landed: 64/100 (`audits/audit-2026-10-09-112239-a7c3.md`); fixes on the Desk card "Audit fixes"
- [ ] Old names (ENATE, Hands Brain, Decision Desk) stop being aliases on 2026-11-09: remove them from the router then
- [ ] "Weekly Hands Brain update" runs Saturdays at 8:47am: the same early time that hit the usage limit on Friday
- [ ] "Flashcard check" still runs every evening although flashcards are parked: pause it?
- [ ] Two sessions editing at once caused clashes today: close sessions when they finish
- [ ] NVIDIA Switchyard (model router): watch only; look again if a routine moves to pay-per-use API keys (`research/hands/reviews/switchyard-2026-10-09.md`)

## Parked by choice (don't start without Charlie)
- Journey video's 9 Oct parking entry is superseded by the later production
  request and branch result (11 Oct); remaining review/integration is listed
  above. Later Obsidian filming remains a Mac task.
Nick Saraev work; flashcards; Karpathy brain; Dan Martell; the decorators'
Facebook post and an unlisted test video; vidIQ (after 5 videos) and Canva
thumbnails (after 3); the decorating business; Nate-channel audit's 8 older
decisions (`audits/2026-10-08-nate-channel.md`); `tools/` → `scripts/` rename.

## AI Impact channel ingestion (direct request, 2026-10-12)
- [x] Inventory 49 public videos and retrieve all 49 caption sources; derive 342 evidence-linked knowledge records (`research/ai-impact/README.md`).
- [ ] Capture and visually verify slides from every video; video/media access is blocked on this host. Start with the 45 visual cues, then inspect the complete videos. Full request NOT VERIFIED; source and continuation in `research/ai-impact/HANDOFF.md`.

## Official model/education references (direct request, 2026-10-12)
- [x] Build official source catalogue, 117 model-reference extracts and 20 selected teaching records (`research/official-docs/README.md`).
- [ ] Finish exact-source/full-content retention decision, empty reference/training pages, actual public course/video content and comprehensive semantic review. Catalogue counts do not prove full ingestion; see `research/official-docs/HANDOFF.md`.

## Task-specific reading verification (2026-10-12)
- [x] Repair Architect full-file default; add compact topic routes; independently test three questions.
- [ ] Verify fresh Claude Code/Codex runtime behaviour on broader topics and conflicting evidence; actual account usage totals not available here. See `audits/2026-10-12-selective-reading.md`.

## Session reconciliation (2026-10-12)
- [x] Main handoff/focus/todo now identify the unmerged browser prototype and
  rendered Short. Existing priority and other open tasks preserved.
- [x] Mandatory separate-reviewer backlog retired by Charlie, 12 Oct. This closes a policy requirement, not untested output checks.

- [ ] Remaining branch residue: `claude/nate-brain-wip` retains an unverified
  [unverified X themes](https://github.com/eddieedwardsv2-ux/Test-environment-/blob/314fb9c973e2104da2baba422303c8fa58a1ebff/research/nate-herk/brain/x-themes.md); preserve it until reviewed. Older
  council/watch-path branch commits need targeted comparison before declaring
  them missing: their current files already exist on main. Ancestor branches
  with historical/renamed paths are not automatically unfinished work.

## Brand engagement and style-guide planning (direct request, 2026-10-12)
- [x] Confirm AI/education focus and gather seven candidates.
- [x] Save a 70-upload exploratory sample and three concrete guide briefs with matched examples: `brainstorms/2026-10-12-brand-style-guides.md`. Remote contents read back exactly.
- [ ] Resolve video IDs, missing Nate/Matt public-interaction data and age-matched measurement before calling the engagement ranking verified. Current sample controls count/format, not all confounders.
- [ ] Inspect actual visual content and complete missing creator caption review. Draft visual rules are proposals.
- [x] Write all three topics in all three styles: nine articles and nine short scripts (`brainstorms/2026-10-12-style-guide-test-drafts.md`); ranges and fixed inputs checked, author semantic review recorded.
- [ ] Collect real beginner answers with the fixed answer keys and blind style comparison. No responses yet; understanding, duration and independent review remain NOT VERIFIED. Choose/activate a guide only after useful results.
- [ ] Complete the outstanding factual/visual/reader checks and page updates; no mandatory separate-reviewer verdict.

## Project/artifact refresh (12 October 2026)
- [x] Reviewed current project records; corrected stale journey parking, setup-plan version and retired tool route; rebuilt sources and published the existing private Artifact Desk with 29 entries.
- [ ] Republish the nine original Claude pages identified by `tools/pages_status.py`; current browser requires Claude sign-in. Updated sources are saved; no publication fingerprint is marked. See `audits/2026-10-12-project-artifact-refresh.md`.
- [ ] **Agent Reach trial** (Desk `qm-agent-reach`: Charlie said yes, 10 Oct). One `try-tool` run on one blocked YouTube video; X and LinkedIn left out. Waits until the TRADEFLOW demo is finished (current focus parks other work).
