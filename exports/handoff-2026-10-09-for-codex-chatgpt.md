# Hand-off: 9 Oct 2026, from Claude to Codex or ChatGPT

**Written:** Friday 9 Oct 2026, 14:00 UK, after Claude hit 95% of its weekly usage.
**Repo:** `eddieedwardsv2-ux/Test-environment-`, branch `main`, 189 commits (84 of them on 9 Oct).
**Source of truth:** `AGENTS.md` (the router). If this file and the repo disagree, the repo wins.

---

## 1. Paste-in prompts

### For Codex (has the repo, can run scripts and commit)
```
Repo: eddieedwardsv2-ux/Test-environment-, branch main. git pull first.
Read AGENTS.md (the router) and follow it, then context/current-focus.md,
context/handoff.md and exports/handoff-2026-10-09-for-codex-chatgpt.md.
Claude is out of usage until its weekly reset. Do only the jobs in section 4
"Codex can do" of that hand-off, in the order given, one at a time.
Codex rules from AGENTS.md: no helpers, hooks or Desk. Open the agent
file in .claude/agents/ and follow it yourself. Run python3 tools/audit.py and
python3 tools/fault_drill.py before you finish (0 errors, 23/23). Put any
question for Charlie under "Waiting on Charlie" in context/current-focus.md.
Never delete or move work, install anything, or publish outside the repo.
Commit each job separately with a plain message and push.
End with Now: / Done when: and VERIFIED / NOT VERIFIED for each claim.
```

### For ChatGPT (work account: research and writing, no repo writes)
```
I'm Charlie. Read this hand-off (pasted below, or from the GitHub connector:
eddieedwardsv2-ux/Test-environment-, file exports/handoff-2026-10-09-for-codex-chatgpt.md).
Do only the jobs in section 4 "ChatGPT can do". Give each result as a
Markdown block I can paste into the named file, so Codex or Claude can
commit it. Plain UK English, one next step at a time, and end with
Now: / Done when:. Mark anything you couldn't check NOT VERIFIED.
```

---

## 2. Where things stand (checked 14:00 on 9 Oct)

| Check | Result |
|---|---|
| `python3 tools/audit.py` | 0 errors, 3 warnings (only long descriptions on built-in skills) |
| `python3 tools/fault_drill.py` | 23 of 23 planted faults caught |
| `node tools/test_hands_actions.cjs` | 14 passed |
| `python3 tools/context_check.py` | about 3,400 tokens always loaded |
| Last scored audit | 64/100, up from 49 (`audits/audit-2026-10-09-112239-a7c3.md`) |
| Plugins on Charlie's account | **Only Small Business is enabled.** The 5 he ticked (Marketing, context7, Superpowers, watch-video, claude-patterns) are not installed |
| Scheduled tasks | Sat 10 Oct 8:47 Quartermaster update and Fri 16 Oct 8:59 audit are set up, with the repo attached. The old broken copies are off. The daily flashcard check still runs even though flashcards are parked |
| Branches not merged | `nate-watch-path` (2 commits: Nate Herk watch path page, 18 videos plus 2 Karpathy, **not on main**) and `claude/nate-brain-wip` (1 unverified WIP commit; main already has its own `rules.md`). The other 7 `claude/*` branches are fully merged |

**Priority (90 days, `context/current-focus.md`):** a repeatable set-up kit so
Charlie can set up a Standard AI-OS for someone brand new to AI (plan v0.4 in
`projects/ai-os-setup-kit/plan.md`; first friend or family set-up next).

---

## 3. What Claude did on 9 Oct (84 commits, grouped)

**Quartermaster (was the Hands Brain): the tool ranking**
- Classified The Next New Thing weeks W38 to W41 (newest first, with a head-to-head against each category's #1). Then Charlie chose to stop at 4 weeks and add new videos only, through the Saturday task.
- Added the presenters' opinions on every video (115 opinions, 21 videos), the skills.sh top skills (31), and Anthropic's plugin catalogues as a trust badge (2,722 plugins).
- Our own verdicts now cap a tool's rank (`research/hands/tried.json`). There is a new `try-tool` skill.
- Reviewed and decided: ECC (dropped, but its done-when check and READY/NOT READY report were adopted), FreeLLMAPI (optional Mac-day trial), NVIDIA Switchyard (watch only), and Small Business (44 skills mapped, 12 linked to ours).

**Architect (was ENATE): Nate Herk's brain**
- 13 Nate videos ingested and given their own map page. The overlap review found 9 rule groups and 5 concept pairs that repeat.
- Nate's six-phrases DM ingested: concept 44 and Rule 44, "finish with VERIFIED / NOT VERIFIED".

**How the OS runs**
- Elders are now named by job: the Architect (Nate's method), the Quartermaster (tools) and the Chief's Desk (Charlie's decisions). Old names work until 9 Nov.
- One `youtube-ingest` skill now owns listing, triage, fetching and hand-over.
- New `connect` skill (adapted from Anthropic's build-connector). Canva is connected and proven (`references/canva.md`).
- `i-have-adhd` skill installed (MIT, pinned in `skills-lock.json`).
- Desk cards can carry a link button and tap-by-tap steps.
- Source preference: GitHub first, Notion instead of Google Drive.

**Checks and quality**
- Fault drill built: 23 planted faults, all caught. `audit.py` runs on every push (GitHub Actions) and checks Desk, pages, maps, hidden skills and broken links.
- Claude vs Codex parity test written (`audits/evidence/2026-10-09-parity-test.md`). Proved for Claude; the Codex half waits (section 4).
- Model comparisons 1 and 2: Sonnet scored 9/9, the same as the main model. The `architect` and `quartermaster` agents now run on Sonnet, with a weekly spot-check in the Friday audit.
- Weekly audit re-run: 64/100. Fix 1 is done; fixes 2 to 5 were left open by Charlie's choice.
- Scheduled tasks rebuilt to run inside sessions that have the repo attached.

**Pages (claude.ai artifacts, links in `system/pages.md`)**
- New pages: System map, Reading Room, Voice Gym, the Desk's question map, the Architect page, journey video drafts (Mix style chosen), and lesson slides.
- Charlie's Brain, the Quartermaster and the Architect page were rebuilt after each run.

**Charlie's thinking captured:** `brainstorms/2026-10-09-charlies-thoughts.md`,
`brainstorms/2026-10-09-middle-plans.md`, and ChatGPT's model-routing prompt
saved but not started (`brainstorms/2026-10-09-model-routing-handoff.md`).

---

## 4. Who can continue what

### Codex can do (repo work, in this order)
1. **Codex parity test.** Run the Codex half of `audits/evidence/2026-10-09-parity-test.md`. Check that Codex lists every skill through `.agents/skills`, answer the same 5 rulebook questions, and follow the three Codex fallbacks. Note what Codex blocks in place of our deny list. Save the results in that file. *Done when:* each question is marked pass or fail with proof. This is Codex's own job, so it suits Codex best.
2. **"Step up to a stronger model" rule.** Add it to `system/model-usage.md`; it's missing (to-do, next-to-build #2). Keep it to the shape of the existing rules. *Done when:* the rule is there and `audit.py` shows 0 errors.
3. **Architect tidy-up.** Link Rules 2 and 3 with concepts 19 and 28 in `research/nate-herk/brain/`, then run `python3 tools/build_brain_map.py`. *Done when:* the map build shows the links and audit is clean. (Codex can rebuild the HTML; republishing the page waits for Claude.)
4. **Log the Corey Haines research** that another session added (`research/corey-haines/`) in `decisions.md`, with one dated line at the top.
5. **Recover the watch path.** Write a question under "Waiting on Charlie": "Bring `nate-watch-path` into main and delete the 8 old branches?" Don't merge or delete anything without his yes.

### ChatGPT can do (research and writing; Charlie or Codex commits the result)
1. **Triage Nate's "Grok Bot Just Got 2 Massive Upgrades" (MgvwZaDPCs4).** Summarise it and say whether it changes how we route models. This has to happen before the model-routing prompt runs. Output a note for `research/nate-herk/`.
2. **Research Boris Cherny as "the Maker"** for the council (to-do #4): who he is, what he teaches, and the 5 best public sources. Output for `research/`.
3. ~~Journey video, Mix style~~: **parked by Charlie 2026-10-09.** Don't work on it until he un-parks it.
4. **Optional:** prices for the 35 Quartermaster tools marked unknown (step 3 of `research/hands/improvement-plan.md`). Each price needs a source link, or it's marked NOT VERIFIED.

### Waits for Claude (needs claude.ai-only tools)
- Republishing any page (artifacts), and anything on the Chief's Desk (its database).
- Checking plugins (`ListPlugins`), running `try-tool` trials, and connectors (Canva, Higgsfield).
- Scheduled tasks, and reading the Saturday and Friday reports.

### Needs Charlie
- Reinstall the 5 plugins (only Small Business is on).
- Branches: keep the watch path, delete the rest?
- Pause the daily flashcard check?
- Audit fixes 2 to 5: yes or later?
- Voice Gym: rewrite 5 or more messages.
- Higgsfield connector, and the rest of the "Needs Charlie" list in `context/todo.md`.

**Now:** paste the Codex prompt into Codex and let it do job 1.
**Done when:** the parity test file shows Codex's results, and `audit.py` is still at 0 errors.
