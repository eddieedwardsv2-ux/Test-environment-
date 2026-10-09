# frontend-design (Anthropic): Elder pilot trial 1, 9 Oct 2026

First run of the Elder councils pilot, step 1 (`brainstorms/2026-10-09-elder-councils-plan.md`
section 5). Charlie's pick on the Desk (`pilot-first-tool`): a tool that needs no install,
because his 5 ticked plugins aren't switched on yet. Quartermaster's pick: **frontend-design**,
#1 by score (18.0) among tools he doesn't have or hasn't tried; an Anthropic skill (official
catalog), one 9.4 KB SKILL.md, Apache 2.0 (`LICENSE.txt` in `anthropics/skills`, commit dbd4588).
Read in a scratch folder only: nothing installed on his account, nothing added to `.claude/`.

## Definition of done (this job)
- [x] One real task: restyle one of Charlie's own pages with the skill, on a scratch copy only
- [x] Before and after screenshots looked at
- [x] This review in the run sheet's shape; council verdict with the contrarian answered
- [x] `tried.json` entry (verdict `pending` until Charlie decides), `build_hands.py` re-run
- [x] Guardian report; Desk card `qm-frontend-design` for Charlie's keep / drop / later

## Prediction (written before running)
- The test page: the **OS Guide**. It shows most of the skill's own list of "AI tells": an
  ALL-CAPS mono eyebrow on every section, "A · B · C" meta strings, near-black `#05070d`,
  identical rounded cards. Expect the skill to make it look less generic and easier to read.
- Expect the council to lean **keep, as a reference read before building a page** (not
  loaded every message), and the contrarian to say "we already have `artifact-design`, which
  covers the same ground": the real question is whether it adds anything on top.
- Expect the Guardian to flag at least one thing: a "better" claim with no screenshot
  behind it, or a missing source for "free".

## The trial (scratch copy of `system/guide/guide.html`; the live page untouched)
**Design plan (the skill's first pass).** Subject: a plain-English manual for one beginner's
AI OS, read on a phone in short gaps between jobs; Charlie comes from decorating.
- Colour: primer grey `#E8EBE7` ground, wall-white `#FBFBF8` panels, ink `#1D2A30`,
  muted `#55646B`, masking-tape yellow `#E4B83A` (the one accent), link blue `#215F94`.
- Type: Fraunces (display, soft serif with character) + Atkinson Hyperlegible (body, built
  for easy reading). Two families, clearly different.
- Layout: one left-aligned column under 70 characters; no cards; each part is a plain
  section with its number on a strip of masking tape (the one bold thing).
- Principles: sentence case everywhere; labels only where they carry meaning ("What it is",
  inline and bold, not ALL-CAPS mono); no middle-dot strings; no shadows or gradients.
**Checked against the brief before building (the skill's second pass):** the first plan used
a dark navy page "to match the other pages": that is default 2 on the skill's list (near-black
with one bright accent), so it was changed to the light primer grey. Card grid dropped (default 4).

**Built and looked at.** Restyled scratch copy: `audits/evidence/2026-10-09-frontend-design/guide-after.html`;
before and after, phone width, side by side: `.../before-after.png`. Self-critique caught one fault
on the first render (labels ran into their text, "What it is:A short…"), fixed and re-shot.
What changed on screen: ALL-CAPS mono labels became bold sentence-case lead-ins; every "A · B · C"
dot string became plain commas (24 in the original; the first pass only fixed the eyebrow, and
the Guardian caught the other 23, so they were finished and the page re-shot); dark cards became one light column; each part's number sits on a yellow
"tape" strip; body text bigger (17px) with shorter lines. Script errors: none (`tools/screenshot.py`).
Time: about 15 minutes. Nothing installed; the skill was read from a scratch clone.

## The council (one pass)
1. **Scout:** not had, not replaced. Closest thing we have is the built-in `artifact-design`
   skill, which already loads before any page is built. Our pages were all built under it.
2. **Contrarian:** "We already have `artifact-design`; a second design guide is two sources for
   one job (Rule 3) and could clash." Evidence for it: both cover typography, colour and layout.
   Evidence against: pages built under `artifact-design` still carry two tells this skill names,
   ALL-CAPS labels and "·" strings. Command: `grep -c -E 'uppercase|·' <page>` (lines with either):
   OS Guide 12, System map 13, Quartermaster template 13, Desk 4, Voice Gym 2; the restyled Guide 0.
   So it adds a check the current guide misses.
3. **Cost and footprint:** free, Apache 2.0 (`LICENSE.txt`, anthropics/skills commit dbd4588);
   one 9.4 KB file; as an installed skill about 200 characters of description every message (measured: 205 with `grep -m1 "^description:"`).
   As a reference file read only when building a page: 0 characters per message.
4. **Safety:** Anthropic's official catalog; plain instructions, no scripts, hooks or
   permissions; no data leaves the repo. Nothing outward-facing.
5. **Charlie's shoes:** on a phone the after version is easier to read (bigger type, no
   shouting labels, part numbers easy to spot). But it's a different look from the dark pages
   he's used to, and he wouldn't run it himself: Claude reads it when building a page.
**Verdict (the Quartermaster): keep, as a reference read before building or restyling a page,
not an installed skill.** Contrarian: answered by the grep counts (it catches what
`artifact-design` let through); the clash risk is handled by making it a checklist that runs
after `artifact-design`, not a second rulebook. Cheapest next test: restyle one more page
(the Desk) and see if Charlie prefers it. Prediction check: council leaned keep (as predicted);
the contrarian raised `artifact-design` (as predicted); the Guardian did **not** flag what I
predicted (an unsupported "better" or an unsourced "free"): it found something I didn't expect,
a result line that claimed all dot strings were removed when 23 of 24 were left (round 1, NOT READY).

## Mini-desk
Settled here: the test page (OS Guide), scratch-only, reference instead of install.
For Charlie (Desk card `qm-frontend-design`): keep / later / drop, and whether the live OS Guide
gets the new look. Disagreements with the Chief: none yet.

## Handoff note
Started from: Desk `pilot-first-tool` (no install). Decisions locked: test page, scratch-only,
reference not install (mini-desk). Shipped: this review, `tried.json` entry (pending),
Quartermaster rebuilt and republished, evidence in `audits/evidence/2026-10-09-frontend-design/`.
Verification: Guardian report in `audits/guardian/`. Disagreements with the Chief: none.
Card for the Chief: `qm-frontend-design`. Pick up here: Charlie's verdict, then pilot step 2.
