# Our AI OS vs Nate's: what to keep, trim or add

Decision page for Charlie (2026-10-08). Built from 35 Nate transcripts: the
20 used for `system/standard-ai-os-v1.md`, plus 13 from his **AI Masterclasses**
playlist and 2 Karpathy videos. Every quote below links to its moment in the
video and was checked against the transcript.

**How to use it:** read each row and mark your choice (Keep / Trim / Add /
Not now) in the last column, or just reply with the row numbers. My
recommendation is in bold.

## Charlie's decisions (2026-10-08, applied the same day)
- **Added:** A11 secret scan (in `tools/audit.py`); A10 cheaper models for
  helper agents (quality-gated model choice, `system/model-usage.md`); A5 a "what this folder is for" README in
  every folder Charlie uses (not AI-only folders like `.claude/`, `tools/`);
  A7 quarterly refresh date in `context/current-focus.md` (audit warns when
  it passes).
- **Not adopted:** A1 plan mode.
- **Changed:** B3 run gate renamed "structure gate"; B4 Karpathy rules
  labelled as second-hand; B7 foundation tests merged into
  `system/standard-ai-os-v1.md`.
- **R14:** option B (95% before big or hard-to-undo work; assume-and-go for
  small, easy-to-undo work). **Router:** confirmed by Charlie "for now", then confirmed as final later the same day (after the full-channel audit).
- Everything else: as suggested (keep as is / not now).

## A. What Nate has that we don't

| # | Nate's way | His words | Ours today | My suggestion | Your choice |
|---|---|---|---|---|---|
| A1 | **Plan mode first**: Claude maps the approach and asks questions before building (Boris does it too) | "Boris Cherny, the creator of Claude Code, starts every single session in plan mode. I do the same thing." — [13:48](https://www.youtube.com/watch?v=_qZvORxGqI0&t=828s) | Our 95% rule asks questions, but plan mode isn't named | **Add** one line to the router: start real build tasks in plan mode | |
| A2 | **Challenge before building**: make the AI argue against the plan | "You ask Claude to start challenging you and pushing back and playing devil's advocate before it builds anything or before it approves any plan." — [2:36](https://www.youtube.com/watch?v=iTY8Q449YNQ&t=156s) | Nothing | **Add** a short "roast this plan" step to `grill-me`, not a new skill | |
| A3 | **Session hand-off skill** before clearing a chat | "before I ever clear anything, I run session handoff." — [18:21](https://www.youtube.com/watch?v=iTY8Q449YNQ&t=1101s) | A router rule ("update Next step") that relies on me remembering | **Add** a small `session-handoff` skill | |
| A4 | **The checker isn't the worker**: a separate judge checks against an objective finish line | "it literally separates the worker from the judge" — [22:55](https://www.youtube.com/watch?v=iTY8Q449YNQ&t=1375s) | Helper agents' work is checked by me, plus `tools/audit.py` | **Keep as is** (already how we work); write it into the standard | |
| A5 | **A README in every folder** saying why it exists | "it basically is just creating this read me so that your agent always understands why does this folder exist" — [1:32:56](https://www.youtube.com/watch?v=X-pbJWKmwi0&t=5576s) | READMEs in `research/` and projects only; none in `context/`, `system/`, `tools/` | **Add** 3 short READMEs | |
| A6 | **Rules folder**: rules needed only sometimes live in their own folder; the router just points | "The cloudmd is not a know all file. It is a I know where everything I need to find lives file." — [3:07:28](https://www.youtube.com/watch?v=mpALXah_PBg&t=11248s) | `context/working-rules.md` does this job | **Keep as is** (same idea, different name) | |
| A7 | **Upkeep schedule**: daily memory, monthly and quarterly reviews | "We have auto memory for daily learnings. Monthly, we'll update this stuff. Quarterly, we'll update this stuff." — [5:53:08](https://www.youtube.com/watch?v=mpALXah_PBg&t=21188s) | Weekly audit only; priorities have no refresh date | **Add** one line: refresh `current-focus.md` each quarter | |
| A8 | **Audit gives a score** and a "level up" step suggests what to build next | "you can just keep running this loop of auditing, leveling up, building" — [54:46](https://www.youtube.com/watch?v=X-pbJWKmwi0&t=3286s) | Audit lists findings, no score, no level-up | **Not now**: worth it once you use the OS daily | |
| A9 | **Codex set-up**: `.codex/` holds Codex's config, agents and its own blocks on risky actions | "it can work things into those config files like we talked about earlier with the codeex that it can certainly like block things out" — [26:23](https://www.youtube.com/watch?v=X-pbJWKmwi0&t=1583s) | Codex sees the router and skills, but not our 3 agents or the safety lock | **Add** when you next use Codex (ask Codex to set itself up from its docs) | |
| A10 | **Cheaper models for helper agents** | "Every task gets routed to the cheapest model that can actually handle that task." — [13:45](https://www.youtube.com/watch?v=7WZ6XldxX0U&t=825s) | All helpers use the main model | **Add** cheaper models for the read-only agents (saves your usage limit, which we hit today) | |
| A11 | **Security review before publishing** | "do a full security review of anything that I've pushed to GitHub" — [4:07:58](https://www.youtube.com/watch?v=mpALXah_PBg&t=14878s) | "Repo is public" rule, nothing checks it | **Add** a key/secret scan to `tools/audit.py` (this repo is public) | |
| A12 | **Evals**: a small set of known-good answers to score changes against | "even if you just have to start with 20 good examples, and then score every version against them" — [10:14](https://www.youtube.com/watch?v=7WZ6XldxX0U&t=614s) | Routing tests are similar but ad hoc | **Not now**: our fresh-agent routing tests already do this job | |
| A13 | **Archives, templates, references folders** | "We've got templates, references, projects, decisions, context, archives, and the claude" — [5:50:35](https://www.youtube.com/watch?v=mpALXah_PBg&t=21035s) | We have `templates/`; research does references; no archives yet | **Not now**: create each when first needed | |

## B. What we've added on top of Nate

| # | Ours | Pro | Con | My suggestion | Your choice |
|---|---|---|---|---|---|
| B1 | **One router, imported** (`CLAUDE.md` → `AGENTS.md`) and skills linked for Codex | Can't drift apart. Nate keeps copies: "I made a copy of my cloud.mmd and called it agents.mmd. So I have two of those now." — [14:16](https://www.youtube.com/watch?v=X-pbJWKmwi0&t=856s) | None | **Keep** | |
| B2 | **Quote checker** (`tools/check_quotes.py`) | Makes Nate's own provenance rule automatic: "every rule has to connect with an exact quote from him and where it came from" — [5:34](https://www.youtube.com/watch?v=bvGptCLDhyo&t=334s) | Only checks the strict citation format | **Keep** | |
| B3 | **Run gate** (audit before finishing) | Catches broken links and stale counts every time | It checks structure, not "did the code run", which is what Nate's gate does: "if it wrote code and it never ran it, the hook will basically block the answer" — [7:35](https://www.youtube.com/watch?v=bvGptCLDhyo&t=455s) | **Keep, rename** to "structure gate" so it isn't oversold | |
| B4 | **"Karpathy's 7 rules"** file | Good habits, clearly written | Secondhand (via Nate's agent); our "build to learn" reading is ours; the 95% rule sits in it but is Nate's | **Keep, relabel** sources honestly | |
| B5 | **Capability map** (check before building) | Stops duplicate tools | Another file to keep current | **Keep** | |
| B6 | **Standard checklist + blank template** | The "not yet personalised" OS you asked for | Long (92 rows) | **Keep** | |
| B7 | **Foundation tests** (old `system/foundation-tests.md`, now merged) | Earlier gate | Mostly covered by the checklist now | **Trim**: fold into the checklist | |
| B8 | **ChatGPT copy** (`exports/`) | ChatGPT works the same way | A copy that can drift (Nate's own drift risk) | **Keep** while you use ChatGPT; the audit should check it | |
| B9 | **Three creator brains + agents, teach, video-tutor, research-creator** | Strong learning set-up | Heavy while Nick and Karpathy are parked; Nate warns "If there's not pain, then why create more?" — [4:04](https://www.youtube.com/watch?v=DTCyvo6cC54&t=244s) | **Keep, no new ones** until the channel needs them | |
| B10 | **Deny list** (no force-push, `rm -rf`) | Nate does the same | None | **Keep** | |

## C. Karpathy and Boris Cherny, and how Nate uses them

- **Karpathy: the LLM wiki.** No fancy search, just markdown with an index:
  "I thought that I had to reach for fancy rag, but the LLM has been pretty good about auto maintaining index files and brief summaries of all documents" — [2:34](https://www.youtube.com/watch?v=sboNwYmH3AY&t=154s).
  Nate uses it for his knowledge base and reads it only when needed. **We do this** (`research/`, brain `index.md`).
- **Karpathy: understanding.**
  "you can outsource your thinking, but you cannot outsource your understanding" — [10:08](https://www.youtube.com/watch?v=bvGptCLDhyo&t=608s).
  **We half do this**: you haven't yet walked through your own router (see D2).
- **Boris: verification is the big one.**
  "the verification, I think, is probably the single most important thing that people do not get right" — [10:15](https://www.youtube.com/watch?v=XNQBCRcwXV4&t=615s).
  **We do this** (checks, fresh-agent tests).
- **Boris: give harder tasks with guardrails and an exit test**, not step-by-step:
  "you should give the model slightly harder tasks than what you think it can do" — [7:44](https://www.youtube.com/watch?v=XNQBCRcwXV4&t=464s).
  **Partly**: we define "Done when", not guardrails.
- **Boris: prune the set-up when models change.** Nate rejects deleting everything. He keeps the router and reworks skills instead:
  "that's important we still need that context of hey Mr. Claude code here's where you find your things" — [4:06](https://www.youtube.com/watch?v=XNQBCRcwXV4&t=246s).
  **We follow Nate**: re-test at each new model.
- **Boris: plan mode every session.** See A1.

## D. My recommendation (in order)
1. **Do the quick, high-value adds:** A1 plan mode, A11 secret scan, A10 cheaper helpers, A5 folder READMEs and A7 quarterly refresh. Each is one line or one small file.
2. **A 10-minute walkthrough:** you explain the router back to me (Karpathy's "understanding" point). Anything you can't explain gets simplified.
3. **Then stop building and start using it:** personalise with `grill-me`, then back to the YouTube channel.
4. A2/A3 (roast, hand-off) when you next feel the need; A8/A9/A12 later.
