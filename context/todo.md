# Everything unfinished (one list, so nothing gets forgotten)

Written 2026-10-09 from `current-focus.md`, the hand-off, the Desk, Mac day,
ChatGPT's hand-off and the battle test. The priority still lives only in
`current-focus.md`; this is the full list behind it. Tick items off by
deleting them (history stays in `decisions.md`).

## Needs Charlie (Decision Desk or a setting only he can change)
- [ ] Plugins ticked 9 Oct (Marketing, context7, Superpowers, watch-video, claude-patterns) not yet showing as enabled on his account (`ListPlugins` empty): check they installed; a new session loads them; then one `try-tool` test each
- [ ] claude.ai settings: switch off 9 unused built-in skills (built-in-browser, chrome-browser, computer-use, import-memory, morning, docx, xlsx, pptx, pdf)
- [ ] Add the Higgsfield connector (`https://mcp.higgsfield.ai/mcp`) and finish Canva's sign-in; then Claude makes one test image (cost said first)
- [ ] Voice Gym: rewrite 5 or more messages; then Claude writes his voice notes into `aios-intake.md` Q2
- [ ] Check ChatGPT accepts the longer instructions box (`exports/chatgpt-instructions.md`, box 2 is about 2,000 characters)
- [ ] Confirm or change Claude's "where this is heading" theory for `current-focus.md`

- [ ] Elder councils: 3 open Desk cards (elder-pilot-go, elder-pushback, elder-two-desks); plan now on main at `brainstorms/2026-10-09-elder-councils-plan.md` (was only on branch `elder-councils-plan`, which also holds `research/nate-herk/prompt-upgrade2-landing-page.md`)
- [ ] Bitcoin newsletter (`projects/bitcoin-newsletter/`, added 9 Oct 16:47 outside a Claude session): active or parked? Not in current-focus or `decisions.md`; Desk card "btc-newsletter"
- [ ] `aios-intake.md` Q2, Q5 and half of Q7 still unanswered

## Next to build (in order, after the Desk answers)
2. [ ] Model comparisons on real work (comparisons 1-2 done 9 Oct: both 9/9; Desk card "promote-sonnet" for the two advisors) before any helper goes back to a cheaper model (`system/model-usage.md`); add the missing "step up to the stronger model" rule
2b. [x] Guardian report required (9 Oct): `tools/audit.py` errors on a 4+ file commit with no newly added, matching Guardian report; fault drill 24/24. Limits: it runs locally and in the Stop hook only (GitHub's shallow clone skips it); the hook sends a turn back once, and only after the commit exists; it proves a fresh report with a matching verdict was filed, not that the Guardian wrote it. Ended NOT READY after the last fix round (`audits/guardian/2026-10-09-guardian-enforced.md`): the shallow-clone fix was made after the Guardian's final check, so the next Claude session should run the Guardian on it. Open: (a) a commit message quoting the rule as an example is read as a citation; (b) file names with spaces are over-counted; (c) Codex route also belongs in this list: Codex commits, leaves the error, notes it under "Waiting on Charlie"; (d) try the Guardian on a different model (Nate says a different model judges)
3. [ ] Journey video: Mix improved 9 Oct evening (scene 3 cut, growing-brain background; `brainstorms/2026-10-09-journey-video-thesis.md`). Next: Charlie's notes on it, then a proper video file with voice-over; later film the real brain growing in Obsidian (Mac)
4. [ ] The council (Nate's voice first; research Boris Cherny as "the Maker")
6. [ ] Set-up kit (paused): first friend or family set-up from plan v0.4
7. [ ] First YouTube short

## Found 2026-10-09 (session review: dropped from the 9 Oct hand-off rewrite)
- [ ] ChatGPT's model-routing prompt saved, not started (`brainstorms/2026-10-09-model-routing-handoff.md`); triage the Grok Bot video first
- [ ] Quartermaster's Search / Check / Implement buttons: republished, but one real save, read and close round trip not yet tested
- [ ] Creative Claw (for YouTube production): sign-in unfinished, no output tested
- [ ] "Thread Notes No1" page (PQn4jTAa9PzUizgtYynEFW) isn't in `system/pages.md`: keep or drop?
- [ ] Watch Path page's source was only on branch `nate-watch-path`; now on main at `research/nate-herk/watch-path.html` (add it to `system/pages.md` when refreshed)
- [ ] Older sessions in the `my-claude-skills` repo (6 Oct) ended waiting on Charlie: a "yes" to write the agency-validation research into that Second Brain; retired-repo deletions and a reply owed by a contact; lesson 1 quiz answer (four parts of an agent). Check if still wanted.
- [ ] Offered, not agreed: a one-command save script

## Waiting for the Mac (`context/mac-day.md`, starts when Charlie says "I'm on Mac")
- [ ] Clone the repo; Obsidian; Nate's 3D brain; context7 and superpowers plugins
- [ ] **Codex test**: same 5 rulebook questions, every skill listed, the three Codex fallbacks, what Codex blocks
- [ ] Small Business plugin (after Charlie's Pro upgrade): install in the desktop app, `smb-onboard`, one `try-tool` trial
- [ ] `/doctor` on the Mac; optional FreeLLMAPI trial only if limits keep stopping sessions

## Small tidy-ups (Claude can do these; offered, not yet agreed)
- [ ] One home page linking every page
- [ ] Refresh the Watch Path and the two oldest lessons (they still name `MISSION.md`, `NOTES.md`)
- [ ] Mark Kit Compare as decided; the round Brain map
- [ ] Review the Corey Haines research another session added (`research/corey-haines/`) and log it
- [ ] Triage Nate's Grok Bot video (MgvwZaDPCs4) before ChatGPT's routing prompt is run
- [ ] ENATE: link Rules 2 and 3 with concepts 19 and 28
- [ ] Hands Brain: the 35 tools with unknown prices (step 3 of `research/hands/improvement-plan.md`, not chosen)

## Watch-outs (things running on their own)
- [x] Re-run Friday audit landed: 64/100 (`audits/audit-2026-10-09-112239-a7c3.md`); fixes on the Desk card "Audit fixes"
- [ ] Old names (ENATE, Hands Brain, Decision Desk) stop being aliases on 2026-11-09: remove them from the router then
- [ ] "Weekly Hands Brain update" runs Saturdays at 8:47am: the same early time that hit the usage limit on Friday
- [ ] "Flashcard check" still runs every evening although flashcards are parked: pause it?
- [ ] Two sessions editing at once caused clashes today: close sessions when they finish
- [ ] NVIDIA Switchyard (model router): watch only; look again if a routine moves to pay-per-use API keys (`research/hands/reviews/switchyard-2026-10-09.md`)

## Parked by choice (don't start without Charlie)
Nick Saraev work; flashcards; Karpathy brain; Dan Martell; the decorators'
Facebook post and an unlisted test video; vidIQ (after 5 videos) and Canva
thumbnails (after 3); the decorating business; Nate-channel audit's 8 older
decisions (`audits/2026-10-08-nate-channel.md`); `tools/` → `scripts/` rename.
