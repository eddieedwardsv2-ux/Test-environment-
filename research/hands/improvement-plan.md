# Hands Brain: improvements and skill plan (2026-10-09)

Written from a read of `tools.json` (95 tools, weeks W39-W41 plus one
skills.sh snapshot), the `hands-ingest` skill and the `hands-brain` agent.
Nothing here is built yet; Charlie picks on the Decision Desk
(cards "hands-improve" and "hands-skills").

## What the data shows (real counts)
| Finding | Number | Why it matters |
|---|---|---|
| Head-to-head (`vs`) filled in | **0 of 95** | Charlie's 2026-10-09 rule (each new tool vs its category's #1) isn't in the data yet; it only applies to new weeks. |
| Tools seen only on skills.sh, never shown in a video | 31 of 95 | No demo, no timestamp: ranked on install count alone. |
| Category #1 is something Charlie already has | 2 (find-skills, grill-me) | The top of "Claude Code skills & plugins" tells him nothing new. Also, the match is by name only: skills.sh's `find-skills` (Vercel) isn't the same file as ours. |
| Built into Claude already | pptx, pdf (#1 and #2 in "Other") | They're already in every session as Anthropic skills; no install needed. |
| Price unknown | 16 | Includes the #1s in agent orchestration (ChatGPT Dots) and models (Jev). |
| Tools Charlie has actually tried | **0** | Every rank comes from a YouTube show or install counts, never from his own use. |
| Weeks covered | W39-W41 (+ W37, W38 listed; 18 of 24 transcripts saved) | Backfill is waiting, as planned. |
| Something starts it every week | No | Like the audit before Friday's routine, it only runs when someone remembers. |

## Suggested improvements (small first)
1. **Split "you already have it" from "new for you".** Tools we already have
   (ours, or built into Claude) get a ✓ badge and drop out of the ranking, so
   each category's #1 is always something new. Change: `tools/build_hands.py`
   plus a short `builtin` list. About 20 lines. Fixes the find-skills/pptx problem.
2. **Back-fill the head-to-head.** A script fills `vs.tool` with the current #1
   for every tool; a helper writes `verdict` and `gap` for the 11 tools
   scored `for_charlie: 3` only (not all 95). The site shows "beats / loses to".
3. **Mark "seen on skills.sh only".** A grey tag on the 31 with no demo, so a
   video-shown tool and an install-count tool don't look equally proven.
4. **Find the 16 unknown prices**, starting with category #1s (one web check
   each, written to the week file with a source link).
5. **A weekly Hands routine** (cadence): every Saturday morning, after the
   show's weekly video, a fresh session runs `hands-ingest` for the newest
   week, rebuilds the site, and puts any installs on the Desk.

## Suggested skills
### A. `try-tool` (new skill, recommended)
**Job:** turn a top-ranked tool into one safe, real trial, and write the
result back so the Hands Brain learns from Charlie's own use, not just the show.
**Why:** 0 of 95 tools have been tried. Nate's litmus test (the OS beats
Charlie at a real job) needs his own results. ENATE Rule 23 (new skills
report only until tested) and Rule 34 (built from a real run).
**Steps it would follow:**
1. Ask `hands-brain` for the #1 new tool for the job (improvement 1 first).
2. Read the tool's page and `check` flag; say price, what it installs, risks.
3. Decision Desk card for the install (always: the rule says ask for installs).
4. Install into this project only (never globally), run one real task from
   Charlie's work (a YouTube clip, a page, a script), keep the receipt.
5. Write `research/hands/tried.json`: tool, date, task, verdict
   (keep / drop / later), one-line why. `build_hands.py` then ranks it:
   "keep" = +5, "drop" = moves to the bottom with his reason shown.
6. Uninstall if "drop". Commit.
**Size:** SKILL.md about 30 lines, plus about 15 lines in `build_hands.py`.
**Done when:** one tool tried end to end and its verdict shows on the site.

### B. HyperFrames skill (install from the Hands list, recommended first trial)
**What:** #1 in "Video, clips & images" (score 17.9, open-source), from HeyGen.
The HyperFrames connector is already connected, but its `compose` and
`render_video` tools refuse coding agents and point to the local skills:
`npx skills add heygen-com/hyperframes` (adds `/hyperframes`,
`/hyperframes-cli`, `/hyperframes-media`).
**Why:** it's for the YouTube channel (animated titles, explainer clips) and
it's the natural first `try-tool` run.
**Check first:** needs Node (it's in the cloud container); render may need
Chromium (installed here). Read the skill files before installing.
**Done when:** a 10-second title card for the channel renders to MP4 here.

### C. Not suggested now
- **Vercel's `find-skills`**: we already have our own trimmed `find-skills`.
- **`frontend-design` / Impeccable**: Claude's built-in `artifact-design` skill
  covers our pages; revisit if a page looks poor.
- **OpenShorts** (#2 video): a hosted website, nothing to install; try it by
  hand with a channel video when there is one.

## Order if all are chosen
1 → B (via A's steps by hand) → A written from that real run → 2 → 3 → 4 → 5.
Building `try-tool` *from* the HyperFrames trial follows ENATE Rule 34
(skills built from a real run, not from imagination).

## Prices and licences (Charlie's note on the Desk, 2026-10-09)
"Learn from our data about prices: pay per use, or monthly and yearly
subscription, but only when one applies, as some skills and MCPs are just free.
Also know which ones are open source, in case a skill deserves debating whether
to build our own or pay for the existing one."

**What our data shows now:** the single `price` field mixes two different
things. "Open source" is a licence (can we read and copy the code?), not a
price, and 77 of 117 tools are filed as "open-source" (30 of them only because
they're on skills.sh). Some open-source tools also sell a hosted plan. 24 tools
are "unknown"; 10 tools already have a price mentioned in their notes.

**Plan (smallest first):**
1. Split the field in the week files and the build: `open_source` (yes / no /
   unknown, with the repo link) and `cost`, filled only when one applies:
   `free`, `pay-per-use`, `monthly`, `yearly`, `one-off` or `free tier + paid`,
   with the amount, where it was found and the date. No web needed: derive from
   what we hold (GitHub links, the show's own words, the `check` notes).
2. Read our own transcripts for price talk on the 24 unknowns (one helper,
   Sonnet), so we learn from our data before searching.
3. Web lookup only for what's left, number ones first, each with a source link.
4. Site: show "Open source" and the cost model as separate tags. A filter for
   "open source, could we build our own?" feeds the build-or-buy debate.
5. Ranking: free and open source keep their small bonus; a monthly fee gets
   none. Re-check prices in the Saturday routine for new tools only.

**Done 2026-10-09 (Desk card `price-plan`: steps 1 and 2, our own data only):**
- Step 1: every week file now has `open_source` (`yes` 47, `public code` 35,
  `unknown` 35 tools), `repo` and `cost` instead of `price`. "Public code" =
  readable on GitHub but licence not checked (most skills.sh entries), so the
  30 skills.sh tools no longer count as open source. `cost` is filled only
  when one applies (19 tools); empty otherwise.
- Step 2: read our 23 saved transcripts for price talk near each tool (no web).
  13 tools got a real cost model with its video and time, e.g. GrokBot (about
  $20 entry, then pay-per-use: a $140/month plan ran $265 over in 2 days),
  VMPal (one-off, about $34-35), CreativeClaw and Hyperagent (pay-per-use),
  Skillry (monthly or one-off; skills from $4.99), Instinct (free for now).
  Boring Funnels' "$2.99 a year" looks like a caption slip: flagged.
- Build: the small score bonus now goes to free or truly open-source tools
  (1) and free tiers (0.5); 8 lower ranks moved, no category #1 changed.
  Site: separate "open source" / "public code" and cost tags.
- Left for step 3 (web, not chosen): the 35 "unknown" tools and paid tools
  with no stated model (Twilio, Spira AI).
