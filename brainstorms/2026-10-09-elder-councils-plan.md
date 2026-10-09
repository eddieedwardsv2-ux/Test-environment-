# Elder councils: each Elder gets experts and a guardian (plan, 2026-10-09)

Charlie's idea: each Elder works like a senior expert who **runs one part of
the operation**. It has its own **council of expert professionals** who make
and improve the work, and a **guardian** who checks that work on its own
before it reaches **the Chief** (Charlie). Inspiration: Nate Herk, "I asked
Claude Code to make me as much money as possible" (iTY8Q449YNQ, transcript in
`research/nate-herk/`).

**This is a plan only. Nothing is built.** Real choices are in "Open
questions" at the bottom (for the Chief's Desk). Builds on
`brainstorms/2026-10-09-middle-plans.md` (the Elders by job) and
`research/council-plan.md` (the council of elders, asked side by side).

---

## 1. The pattern in plain words

```
Chief (Charlie) ── decides, judges taste last
   ▲
   │  report: VERIFIED / NOT VERIFIED, plus any real choice on the Desk
Guardian ── a separate checker; never one of the makers
   ▲  fail → back to the council (at most 2 rounds), then up to the Chief
   │
Elder ── runs one department; owns its "definition of done"
   │
Expert council ── 3 to 6 named experts, each checking one angle
   │
Hands ── skills, scripts, connectors that do the actual work
```

Think of a building firm. The **Elder** is the site manager for one trade.
The **council** is the specialists he brings in: a surveyor, a joiner, a
sparky, a decorator. The **guardian** is the building inspector: he wasn't
on the job, he has his own checklist, and his sign-off is what matters. The
**Chief** is the client who signs it off and says whether he likes it.

### How it maps to Nate's video
| Nate's upgrade (paraphrased) | Timestamp | What it gives our Elders |
|---|---|---|
| **1. /roast:** a council of personas (contrarian, expansionist, first-principles thinker, deep researcher, the buyer), then a judge gives one verdict (green light, reshape or kill) plus the cheapest 48-hour test | [3:07](https://www.youtube.com/watch?v=iTY8Q449YNQ&t=187s)–[3:38](https://www.youtube.com/watch?v=iTY8Q449YNQ&t=218s) | Every council has a **contrarian**, and every run ends with **one verdict**, not a list of opinions |
| Plain Claude gave a much more generic answer than the council | [6:42](https://www.youtube.com/watch?v=iTY8Q449YNQ&t=402s)–[7:12](https://www.youtube.com/watch?v=iTY8Q449YNQ&t=432s) | The pilot compares "with council" against "without" before we keep it (Rule 34: retire what doesn't earn its place) |
| **2. Verification loop:** don't trust that it looks right; check it yourself (Playwright screenshots of every section at both screen sizes), fix, re-check, stop only at a written **definition of done**; then stress test (forms filled many ways, edge cases) | [10:46](https://www.youtube.com/watch?v=iTY8Q449YNQ&t=646s)–[11:47](https://www.youtube.com/watch?v=iTY8Q449YNQ&t=707s), [14:18](https://www.youtube.com/watch?v=iTY8Q449YNQ&t=858s)–[15:18](https://www.youtube.com/watch?v=iTY8Q449YNQ&t=918s) | Every Elder writes its **definition of done first**, and its guardian runs a **fix → re-check** loop |
| The landing-page prompt Charlie photographed holds about five experts in one prompt (brand/product strategist, conversion copywriter, designer, engineer, QA) | prompt shown on screen around [10:46](https://www.youtube.com/watch?v=iTY8Q449YNQ&t=646s); not read aloud, so the five roles come from Charlie's photo, not the transcript | **Default: experts run inside one prompt**, one after another, not as five separate helpers (cheaper, and allowed by our model rules) |
| Verification depends on what you built: a landing page, an edited video and a data pipeline are checked differently | [9:43](https://www.youtube.com/watch?v=iTY8Q449YNQ&t=583s)–[10:14](https://www.youtube.com/watch?v=iTY8Q449YNQ&t=614s) | Each guardian has a **build-specific check**, written per Elder below |
| The page passed every check but still looked generic ("AI sloppy") | [13:17](https://www.youtube.com/watch?v=iTY8Q449YNQ&t=797s) | Passing proves it **works**, not that it's **good**. Every council needs a **taste expert**; the Chief judges taste last |
| **3. /session-handoff** before clearing: what we're doing, key files, decisions locked, running state, verification, open questions, where to pick up | [18:21](https://www.youtube.com/watch?v=iTY8Q449YNQ&t=1101s), [20:22](https://www.youtube.com/watch?v=iTY8Q449YNQ&t=1222s) | Every run ends with a **handoff note** in the same shape, so the next session (or Codex) can pick up |
| **4. Sub-agents in parallel** for independent pieces; **/goal** keeps working until a written finish line, and a **separate evaluator model** decides if it's done, so the worker never marks its own homework | [21:54](https://www.youtube.com/watch?v=iTY8Q449YNQ&t=1314s), [22:25](https://www.youtube.com/watch?v=iTY8Q449YNQ&t=1345s)–[22:55](https://www.youtube.com/watch?v=iTY8Q449YNQ&t=1375s), [24:26](https://www.youtube.com/watch?v=iTY8Q449YNQ&t=1466s) | The **guardian is a separate agent** with a fresh context; parallel experts only for independent work that writes to separate files |

This is already in the Architect's brain as **Rule 32** (let the AI attack the
plan), **Rule 33** (a separate checker decides "done", then try to break it)
and **Rule 44** (say what the check won't catch; VERIFIED / NOT VERIFIED).
The council pattern turns those rules into a fixed shape every Elder uses.

**Not proven here:** `/goal` and its evaluator are what Nate shows; Claude
Code's sub-agent docs (checked 2026-10-09) don't describe `/goal`, so treat
its details as "check before relying on it". The plan works without it.

---

## 2. The Elders, one by one

The Elders are the ones named in `middle-plans.md` (Plan 1, built
2026-10-09). Two are live (Architect, Quartermaster); the rest are
**proposed or parked**, and stay that way unless Charlie un-parks them.

| Elder | State today | Its department |
|---|---|---|
| Architect | live (`architect` agent, Sonnet, read-only advisor) | how the OS is built and run; the set-up kit |
| Quartermaster | live (`quartermaster` agent, Sonnet, read-only advisor) | the kit: which tools, skills, plugins to use; trials |
| Guardian | proposed (a role, not a person) | checking: "is it true and does it work?" and "is it safe?" |
| Maker | proposed (needs Boris Cherny research first) | how Claude Code is meant to be used: skills, agents, hooks, settings |
| Teacher | parked (Karpathy); `teach` skill and `video-tutor` agent are live | teaching Charlie; lessons |
| Builder | parked (Nick, `nick-brain`) | building and shipping |

**Big change in the Elders' job.** Today the two live Elders are
**advisors**: they answer a question from their brain. Running a department
means **producing work** (a trial, a plan, a fix). So each Elder gets two
modes:
- **Advise** (as today): quick answer, no council, no guardian. "Ask the
  Architect" keeps working exactly as it does, so the routing tests still pass.
- **Run**: a real job with a deliverable. Council, guardian, definition of
  done, handoff note.

### 2.1 The Quartermaster (runs the kit)
**Job:** decides which tools Charlie uses, runs real trials, keeps the ranked
list (`research/hands/`) honest. **Next real job:** the 5 plugins Charlie
ticked (`context/current-focus.md`), one `try-tool` trial each.

| Expert | What they check or add |
|---|---|
| **Scout** | Is there something newer or already owned? Reads `tools.json` (`have`, `replaced_by`, newest week) and the capability map's "Already available" table |
| **Contrarian** (from /roast) | "Do we need this at all?" Eliminate first (3Ms: EAD). Names the fatal flaw |
| **Cost and footprint accountant** | Price and cost model; what it installs; how many characters it adds to every message (`try-tool` step 3); usage spent |
| **Safety vetter** | Licence, stars, who made it, hooks and permissions it adds, data it sends out (Rule 37: vet any plugin first) |
| **Charlie's shoes** (the "buyer" from /roast; the **taste** expert) | Would Charlie really use this on his phone, for the channel or the OS? Is the trial output something he'd be proud to show? |

**Guardian's build-specific check (a tool trial):**
1. The trial really ran: an output file exists and the guardian **looks at
   it** (a frame, a screenshot via `tools/screenshot.py`, or the real output).
2. It was installed in scratch only; nothing new in `.claude/` or
   `~/.claude/skills/` that wasn't declared.
3. `research/hands/tried.json` has a valid entry with every field
   (`name, date, task, result, time, cost, adds, verdict, why`).
4. `python3 tools/build_hands.py` runs and the tool's rank moved as the
   verdict says; `python3 tools/audit.py` 0 errors (it checks quotes and
   timestamps).
5. Every claim in the review (price, "free", stars) has a source link or is
   marked "claim to check".

**Definition of done:** one review in `research/hands/reviews/<tool>-<date>.md`
with the council's verdict (keep / drop / later) and the cheapest next test;
guardian report VERIFIED / NOT VERIFIED; a Desk card for Charlie's verdict;
pages rebuilt and republished.
**Reuses:** `quartermaster` agent, `try-tool`, `hands-ingest`, `find-skills`,
`connect`, `tools/build_hands.py`, `tools/screenshot.py`, `decide`.
**Gaps:** no review template yet (the five existing reviews differ in shape);
the safety vetter has no checklist of its own (borrow the Guardian Elder's).

### 2.2 The Architect (runs the OS and the set-up kit)
**Job:** how this OS is organised, and the 90-day priority: a set-up kit a
beginner can follow (`projects/ai-os-setup-kit/plan.md`, v0.4, paused until
the first friend or family set-up).

| Expert | What they check or add |
|---|---|
| **Router keeper** | Every route lands; smallest context that works (Rule 41); router under 200 lines; no stale pointer |
| **First-timer** (the beginner's eye) | Could someone who has never opened a terminal follow each step on a phone? Plain UK English, one step at a time (`context/how-i-learn.md`) |
| **Contrarian** | The fatal flaw, and "the three decisions Charlie is most likely to disagree with" (Rule 44) |
| **Source checker** | Does it match Nate's kit and rules? Quotes verbatim, newer video wins (`research/nate-herk/brain/`) |
| **Privacy and consent officer** | Public repo: no one else's details, recordings only with consent, nothing private (router rule) |
| **The channel's eye** (taste) | Is it clear and good enough to film? Would it make a decent episode? |

**Guardian's build-specific check (routing, docs or a set-up):**
1. The fresh-session test: a new headless session answers the 5 router
   questions (as in `audits/evidence/2026-10-09-end-to-end/`), every answer
   lands directly, not by searching.
2. `python3 tools/audit.py` 0 errors; `python3 tools/context_check.py` sizes
   not worse; `python3 tools/fault_drill.py` still 23/23 if the audit changed.
3. For the set-up kit: a dry run on a blank copy of
   `templates/standard-ai-os-v1/`, following the steps literally, noting every
   step that needed knowledge the plan didn't give.

**Definition of done:** the change or plan is saved; every route it touches
followed; fresh-session test passed; guardian report and handoff in
`audits/evidence/<date>-<slug>/`; router and focus updated.
**Reuses:** `architect` agent, `audit` skill (and `content-check.md`), `link`,
`level-up`, `grill-me`, `tools/audit.py`, `tools/context_check.py`,
`tools/fault_drill.py`, `system/standard-ai-os-v1.md`, the blank template.
**Gaps:** the fresh-session test is run by hand, not a script; no dry-run
checklist for the set-up kit yet.

### 2.3 The Guardian (runs checking) — proposed
**Job:** owns the two checklists from the walk notes (section C) and supplies
**every other Elder's guardian**. One Elder, many guardians: each Elder's
guardian = the Guardian's shared checklists + that Elder's build-specific check.

| Expert | What they check |
|---|---|
| **Truth checker** | Receipts: every "done, saved, pushed" has output; quotes appear in their transcript; links resolve |
| **Works checker** | Run it, don't read it ("I reviewed the code" is not a check, Rule 44) |
| **Safety officer** | Secrets, private data, other people's details, permissions and hooks, untrusted web content (Rules 36, 37) |
| **Red-teamer** | Try to break it: odd inputs, missing files, the edge cases (Nate [15:18](https://www.youtube.com/watch?v=iTY8Q449YNQ&t=918s)) |

**Who guards the guardian:** `tools/fault_drill.py`. It already plants 23
faults and proves `tools/audit.py` catches each. Each Elder's guardian gets
one planted fault of its own (e.g. a trial review with a made-up timestamp)
and must catch it before it goes live.
**Definition of done (for the Guardian itself):** every Elder's check is
written, and the drill catches every planted fault.
**Reuses:** `audit` skill, `tools/audit.py`, `tools/check_quotes.py`,
`tools/fault_drill.py`, `tools/run_gate.sh`, the deny list in
`.claude/settings.json`, Claude Code's built-in `security-review`.
**Gaps:** no "is it safe?" checklist written down in one place yet (it's
spread over the router, Rules 36-37 and the secret scan).

### 2.4 The Maker (runs Claude Code itself) — proposed, needs research
**Job:** how skills, agents, hooks and settings should be written, from Boris
Cherny (who created Claude Code; to research first, `context/todo.md` #4).

| Expert (provisional until the research) | What they check |
|---|---|
| **Skill writer** | One job per skill, description that triggers, under 300 lines, built from a real run (Rules 34, 44) |
| **Permissions expert** | Deny plus allow, helpers inherit limits (Rule 36) |
| **Context accountant** | What the change adds to every message (`tools/context_check.py`) |
| **Boris check** | Does it match how Claude Code is meant to be used (after the research) |
| **Contrarian** | Is a skill needed, or does a prompt or existing skill do it? |

**Guardian's check (a skill or agent):** a trigger test in a fresh session
(3 phrases that should fire it, 2 that shouldn't); `tools/audit.py` (every
skill and agent routed, none hidden); context size before and after.
**Definition of done:** the skill fires on the right phrases only, is routed,
and one real run produced the output it promises.
**Reuses:** `find-skills`, `level-up` (machine handoff), claude.ai
`skill-creator`, `research-creator` (for the Boris research).
**Gaps:** no sources yet. Don't build until the research run is done.

### 2.5 The Teacher (runs lessons) — parked
**Job:** turns knowledge into lessons Charlie can use. The `teach` skill's
7-rule self-check is already a council of one; `video-tutor` writes lessons.

| Expert | What they check |
|---|---|
| **Karpathy's 7 rules** | Smallest first, predict before showing, wrong version shown, Charlie builds something |
| **Plain-English editor** | UK English, every term explained, trade analogies |
| **Source checker** | Every key idea has a working timestamp link |
| **Charlie's shoes** (taste) | Is it short and useful on a phone, not a lecture? |

**Guardian's check (a lesson):** every quote is in its transcript at that
timestamp; the practice task is done once, by the guardian, in under 20
minutes; flashcards skipped while parked.
**Definition of done:** lesson file saved; guardian report; task tested.
**Reuses:** `teach`, `video-tutor`, `working-rules.md`. **Gaps:** Karpathy
brain parked; leave this Elder as a sheet only until un-parked.

### 2.6 The Builder (Nick) — parked
Listed for completeness only. If un-parked: a shipper (smallest thing that
ships this week), an offer expert, a contrarian, Nick's rules
(`research/nick-saraev/brain/rules.md`), and a guardian whose check is "it
ran live once, end to end". **Don't build while the set-up kit is the
priority** (`context/current-focus.md`).

### Gaps across all Elders
- **No Elder owns the YouTube channel** (lessons to Shorts, filming cards,
  edits: walk notes section K). Nate's landing-page prompt (strategist,
  copywriter, designer, engineer, QA) fits a channel department almost
  exactly, and a video needs its own check (watch the render, captions,
  length). See open question 7.
- The Bitcoin newsletter project already has its own editorial checks
  (`projects/bitcoin-newsletter/README.md`); it doesn't need an Elder now.

---

## 3. Shared rules for every council

| Rule | In practice |
|---|---|
| **Definition of done first** | Written before any work starts (working rules: "Done when" first). The guardian checks against it, not against its own idea of good |
| **Guardian is independent** | A **separate agent** with a fresh context. It gets only the deliverable, the definition of done and its check, **not the makers' reasoning**, so it can't just agree (Nate [22:25](https://www.youtube.com/watch?v=iTY8Q449YNQ&t=1345s)). It never edits the work; the council fixes |
| **Fix and re-check, capped** | Make → check → fix → re-check. **At most 2 fix rounds**, then stop and report NOT READY to the Chief with the guardian's list. Matches `system/model-usage.md` (no endless retry loops) |
| **One verdict** | The Elder ends with one line (keep / reshape / drop, or ready / not ready) and the cheapest next test, like /roast's judge |
| **Fixed report shape** | VERIFIED (what ran, what it returned) / NOT VERIFIED (what couldn't be checked, why), plus what the check **would not** catch (Rule 44) |
| **Taste is separate from checks** | Each council has a taste expert who signs with reasons; the guardian checks that sign-off exists; the Chief has the last word on taste |
| **Handoff note every run** | Nate's session-handoff shape: started from, decisions locked, what shipped, key files, running state, verification, open questions, pick up here. Saved with the run's receipts |
| **Experts in one prompt by default** | Like the landing-page prompt: one maker plays each expert in turn. Cheaper, and keeps us within "at most two helpers" (`context/working-rules.md`) |
| **Parallel only when independent** | Separate helpers only when experts need their own big reading (research) **and** write to separate files (Nate's /goal run: one helper per deliverable, [24:26](https://www.youtube.com/watch?v=iTY8Q449YNQ&t=1466s)). Rate-limited sources one at a time. The guardian always runs **after** the makers |
| **One lead integrates** | The main session runs the loop: Elder's council → guardian → fix → Chief. Elder agents don't spawn helpers: working rules say no helpers spawning helpers by default. Claude Code would allow it (sub-agent docs, checked 2026-10-09: up to three layers), but both live Elder agents have `tools: Read, Glob, Grep` (no `Agent`), so they can't today. Keep it that way |
| **Quality before savings** | Run mode and the guardian use the main model (`inherit`). The Sonnet promotion covers read-only **Advise** look-ups only (`system/model-usage.md`); a cheaper guardian is a trial with its own comparison first |
| **Questions go on the Desk** | Real choices become Desk cards (`decide`); everything small is done and stated |

---

## 4. How to store it in the repo

### Options
| Option | What it looks like | For | Against |
|---|---|---|---|
| A. All inline in each agent file | `.claude/agents/quartermaster.md` grows a council, a check and a done | One file per Elder; easy to find | The Advise agent reads the Run instructions too (muddles it); file grows long |
| B. Every expert its own agent | `.claude/agents/qm-scout.md`, `qm-contrarian.md`… | Each expert gets a clean context | 20-30 agents; every description loads in every message (bloat); expensive to run |
| **C. One skill, one sheet per Elder, one guardian (recommended)** | see below | Only one skill description and one agent description load each message; sheets load only when used; Advise mode stays untouched | One more hop to find the sheet (the skill points to it) |

### Recommended layout (option C)
```
.claude/skills/elder-run/SKILL.md      the loop and the shared rules (section 3), ~40 lines
.claude/skills/elder-run/elders/quartermaster.md   one sheet per Elder (the worked example below)
.claude/skills/elder-run/elders/architect.md       (added when that Elder is upgraded)
.claude/agents/guardian.md             the one independent checker; reads the sheet's "Guardian's check"
.claude/agents/quartermaster.md        unchanged (Advise mode)
.claude/agents/architect.md            unchanged (Advise mode)
```
Receipts go where each Elder already keeps them (no new folders):
Quartermaster → `research/hands/reviews/`; Architect → `audits/evidence/`.

**`guardian.md` in short:** `model: inherit`; tools `Read, Glob, Grep, Bash`
(Bash only to run checks: told never to edit, and the deny list applies);
input = the deliverable's paths + the sheet's definition of done + its
check; output = PASS / FAIL per check, VERIFIED / NOT VERIFIED, and what it
would not catch. It holds the Guardian Elder's shared checklists (truth,
works, safe).

### Worked example: the Quartermaster's sheet
This is what `.claude/skills/elder-run/elders/quartermaster.md` would hold.
It is the Elder for Charlie's current **Next** step (the 5 plugin trials).

```markdown
# Quartermaster: run sheet

**Runs:** the kit. Which tools Charlie uses, real trials, the ranked list.
**Run mode starts when:** "try <tool>", "trial the plugins", a new #1 in a
category, or a Saturday Hands update that names a tool for Charlie (need = yes).
**Advise mode** (a quick "what's best for X?") stays with the `quartermaster`
agent: no council, no guardian.

## Definition of done (write the job's own version before starting)
- [ ] One real task from Charlie's work, run with the tool, output saved
- [ ] Review `research/hands/reviews/<tool>-<date>.md` in the shape below
- [ ] `research/hands/tried.json` entry, `tools/build_hands.py` re-run
- [ ] Guardian report: every check PASS, or NOT READY with reasons
- [ ] Desk card for Charlie's keep / drop / later; pages republished

## The council (play each in turn, in one pass; 2-4 lines each)
1. **Scout:** do we already have it (`have: true`, capability map's
   "Already available")? Has something newer replaced it?
2. **Contrarian:** what's the fatal flaw? What breaks if we just don't?
3. **Cost and footprint:** price and cost model (with source), what it
   installs, characters added per message, usage this trial spent.
4. **Safety vetter:** licence, maker, stars, hooks and permissions it adds,
   where our data goes. Anything outward-facing needs Charlie's OK.
5. **Charlie's shoes (taste):** would he use it on his phone, this month,
   for the channel or the OS? Is the output good, not just working?
**Verdict (the Elder):** keep / drop / later, in one line, plus the cheapest
next test. Where experts disagree, say so before deciding.

## Guardian's check (passed to the `guardian` agent; it gets no council notes)
1. Output exists and was looked at (screenshot, frame or the file itself).
2. Installed in scratch only; `.claude/` and `~/.claude/skills/` unchanged
   apart from what the review declares.
3. `tried.json` entry valid with all 9 fields; `build_hands.py` runs; the rank
   moved as the verdict says.
4. Every price, "free" or star count has a source or says "claim to check".
5. `python3 tools/audit.py` 0 errors.
Report: PASS / FAIL per line; VERIFIED / NOT VERIFIED; what these checks
would not catch (e.g. whether the tool is good for long jobs).

## Loop
Fail → council fixes only what failed → guardian re-checks. Max 2 rounds,
then NOT READY to the Chief with the open fails.

## Handoff note (end of the review file)
Started from · decisions locked · what shipped · key files · running state ·
verification · open questions · pick up here.

## Reuses
`try-tool` (the steps), `quartermaster` (Advise), `hands-ingest`,
`tools/build_hands.py`, `tools/screenshot.py`, `decide`.
```

---

## 5. Rollout, smallest first (Karpathy rule)

**First Elder: the Quartermaster.** Why:
- Its next job is the top of current-focus right now (5 plugin trials), so
  the pilot is real work, not a demo (Rule 34: build from a real run).
- `try-tool` already has steps and a trial record, so the change is small:
  add a council pass, a definition of done and a guardian.
- Its check is concrete and machine-checkable (files, JSON, a build, a
  screenshot), so we'll know quickly if the guardian works.
- The Architect's big job (the set-up kit) is paused until a friend is
  booked, so it goes second.

| Step | What | Done when |
|---|---|---|
| 1. Predict, then pilot by hand | Write the Quartermaster sheet (above) as a draft. Before running, write down what we expect the guardian to flag. Run **one** plugin trial with the council in one prompt, then a separate `guardian` agent (draft file) | Review saved with council verdict, guardian report and handoff; prediction compared with what it actually flagged; audit 0 errors |
| 2. Test the guardian | Plant one fault in a copy of that review (a made-up timestamp or missing `tried.json` field) and run the guardian on it | The guardian catches it; if not, fix its check and re-run |
| 3. Is it worth it? | Same trial question to plain `try-tool` without the council (as Nate did at [6:42](https://www.youtube.com/watch?v=iTY8Q449YNQ&t=402s)); compare the two side by side, with usage counted | A short comparison in the review; Charlie's keep / drop on the pattern via the Desk |
| 4. Second trial, then the skill | Run the next plugin trial the same way; only then write `elder-run/SKILL.md` and `guardian.md` from the two runs (Rule 44: a skill on the second solve) | Skill and agent routed in `AGENTS.md` and `system/capability-map.md`; audit passes; trigger test (3 should, 2 shouldn't) passes |
| 5. Guardian Elder in the drill | Add the Quartermaster's planted fault to `tools/fault_drill.py`; write the shared "is it safe?" checklist into `guardian.md` | Drill catches 24/24; weekly audit runs it |
| 6. Architect on the set-up kit | Architect sheet; run it on plan v0.4 before the first friend set-up (dry run on the blank template) | Fresh-session test 5/5 on the template copy; dry-run gaps listed; guardian report in `audits/evidence/` |
| 7. Maker | After the Boris Cherny research (`research-creator`), write the Maker sheet and run it on the next new skill | Research saved; one real skill built through the loop; trigger test passes |
| 8. Teacher, Builder | Stay parked. Sheets only when Charlie un-parks them | Charlie's Desk answer |
| 9. Council of elders | The side-by-side council (`research/council-plan.md` step 5) uses Elders' Advise answers; Run reports feed it later | Its own plan step; not before steps 1-6 |

After each step: update the router and capability map in the same turn,
re-run the fresh-session routing test (both "ask the Quartermaster" and
"run the Quartermaster" must land), and add a `decisions.md` line.

---

## 6. Open questions for Charlie (for the Chief's Desk; my recommendation first)

1. **Which Elder first?** Recommended: the **Quartermaster** (real job this
   week, smallest change, easy check). Alternative: the Architect, if you'd
   rather harden the set-up kit before the first friend set-up.
2. **The word "council" now means two things:** each Elder's own experts, and
   the Elders asked side by side. Recommended: keep **"expert council"** for
   each Elder's experts (your word), and call the side-by-side meeting **"the
   Elders' Table"**, so no session confuses the two. Alternative: keep both
   as "council".
3. **How many fix rounds before it comes to you?** Recommended: **2**, then
   NOT READY with the open fails. Alternatives: 1 (saves usage), or "until
   done" (Nate's style, but can burn usage).
4. **Where it's stored:** recommended **option C** (one `elder-run` skill
   with a sheet per Elder, one shared `guardian` agent). Alternative: option
   A, everything inside each Elder's agent file.
5. **Guardian's model:** recommended **the main model** until a cheaper one
   passes a comparison (quality first). Alternative: trial Sonnet as the
   guardian straight away.
6. **Quick questions ("ask the Architect") stay council-free?** Recommended:
   **yes**, council and guardian only in Run mode. Alternative: every answer
   gets a short contrarian line.
7. **A seventh Elder for the YouTube channel?** Nate's landing-page five
   experts fit it closely. Recommended: **later**, after the first Short
   (`context/todo.md` #7), so it's built from a real run. Alternative: add it
   now as a proposed Elder with a sheet only.
8. **Guardian reports on the Desk?** Recommended: **only when NOT READY or a
   real choice is needed**; otherwise the report sits with the receipts.
   Alternative: a Desk card after every run.
