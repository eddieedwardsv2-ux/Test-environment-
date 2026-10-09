# The "middle": two plans to talk through (2026-10-09)

Charlie answered two Desk cards that change the routing: **elder-names: by
job** and **youtube-ingest: yes, one skill**. He wanted to talk through "the
middle" before anything changes, so nothing below is built yet. One Desk card
("middle-go") asks whether to go ahead. Background: `2026-10-09-charlies-thoughts.md`
sections B, C, D; `research/council-plan.md`.

## What the end-to-end test adds (`audits/evidence/2026-10-09-end-to-end/`)
The router → brain → answer path works today in a fresh Claude session (2 hops,
quote checked). So renaming is safe **only if every route still lands**: the
same test is the check after each plan. It also found a gap for the
model-routing talk: no written rule for stepping up to a stronger model.

## Plan 1: name the elders by their job
**The picture:** head = the router (`AGENTS.md`); **middle = the council**,
where the brains meet and give a recommendation; hands = skills, scripts,
routines; Charlie = the Chief, who decides.

| Elder | Is today | Holds | Agent |
|---|---|---|---|
| **Architect** | ENATE (`nate-brain`, `research/nate-herk/brain/`) | how to build and run the OS; Nate's voice | `architect` |
| **Quartermaster** | Hands Brain (`hands-brain`, `research/hands/`) | what kit to use now, from any source | `quartermaster` |
| **Maker** | (new) Boris Cherny | how Claude Code is meant to be used | later, after research |
| **Teacher** | Karpathy (parked) | first principles, learning | later |
| **Guardian** | (new) a role, not a person | two checklists: "is it true and does it work?" (audit) and "is it safe?" (security, privacy, public repo) | later |
| **Builder** | Nick (parked) | building and shipping | parked |

**Smallest first (one session, about 45 minutes):**
1. Rename the two that exist, **names only**: agents `nate-brain` → `architect`,
   `hands-brain` → `quartermaster`; page titles ENATE → "Architect (Nate)",
   Hands Brain → "Quartermaster (tools)". Folders stay where they are
   (`research/nate-herk/`, `research/hands/`): moving them would break about
   55 links for no gain.
2. Keep the old names as aliases in the router for a month ("ENATE" and
   "Hands Brain" still route), so Charlie and other sessions never hit a dead end.
3. Page links stay the same (republish to the same address).
4. Re-run the end-to-end test with "ask the Architect…" and "ask the
   Quartermaster…"; both must land. `tools/audit.py` checks every agent is routed.
5. Maker, Teacher and Guardian are added only when they have sources (Maker
   needs a Boris Cherny research run first; Guardian can start from Rules 35
   and 37 and the security checks we already run).

**Touches:** about 24 files mention ENATE and 30 the Hands Brain; only the
router, the two agent files, `system/pages.md`, the capability map, the two
page titles and the hand-off need changing. History (`decisions.md`, logs)
keeps the old names.

## Plan 2: one `youtube-ingest` skill
**Today:** YouTube steps live in 3 skills (`research-creator` steps 1-3,
`brain-ingest` triage and "get the raw source", `hands-ingest` steps 1-2) and
3 scripts (`research/get_transcript.py`, `research/process_queue.py` +
`.github/workflows/transcripts.yml`, `research/hands/pipeline.py`).

**After:** one skill owns getting YouTube in; each brain keeps only "what does
this mean for us".
1. **List** a channel (newest first) or take a link: `yt-dlp` / `pipeline.py`.
2. **Triage** (tiers 0-3, moved from `brain-ingest`): titles, then
   descriptions and chapters, then queue, then spend.
3. **Fetch** transcripts one at a time; on rate limit, queue for GitHub.
4. **Hand over** each transcript to whichever brain asked: `brain-ingest`
   (Architect, Nick), `hands-ingest` (Quartermaster), `research-creator` (new person).

**Smallest first (one session, about an hour):**
1. Write `.claude/skills/youtube-ingest/SKILL.md` (about 40 lines) by moving
   the steps above word for word; **no script changes**.
2. Shorten the three skills to "get the videos with `youtube-ingest`, then…".
3. Test: re-run last week's ingest (W41 of the show, and the 4 Nate gap videos
   in `research/nate-herk/triage.md`) through the new skill; the week file and
   triage file must come out the same (`git diff` empty apart from dates).
4. Router: one line ("Get YouTube videos into any brain → `youtube-ingest`");
   capability map row; audit.

## Questions for the talk (my recommended answer first)
1. **Go ahead with both as written?** Recommended: yes, Plan 2 first (no
   renames, easy test), then Plan 1.
2. **Keep the folders where they are?** Recommended: yes; names change, paths don't.
3. **Rename the Decision Desk?** If "the desk" means the Mac workspace, the
   Desk could become "the Chief's Desk" (you are the Chief). Recommended: yes,
   title only, same link.
4. **Model routing** (ChatGPT's prompt) stays a separate talk after these two.
