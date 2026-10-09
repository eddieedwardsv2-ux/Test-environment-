# Charlie's AI OS — router

For any AI agent in this repo (Codex reads it directly; Claude Code imports it
from CLAUDE.md). It loads with every message, so it holds who you're helping,
how to work and where things live; detail sits in the files it points to.
Smallest context that works, not shortest: cut a line only if it's duplicated,
can be looked up or is stale (`research/nate-herk/lesson-smallest-context.md`).

You're helping Charlie, a UK beginner learning Claude Code and Codex while
building a YouTube channel about it. Plain UK English, one next step at a
time; end working replies with **Now:** and **Done when:**.

## How this OS is built (Nate Herk's AIS-OS kit)
Four Cs in order: Context → Connections (`connections.md`) → Capabilities
(skills) → Cadence. Three Ms for any new automation (`references/3ms-framework.md`).
Litmus test: while Charlie is away, the OS handles one real event faster and
better than he would. What to add as it grows: `EXPANSIONS.md`.

## Rules that always apply (detail in `context/working-rules.md`)
- **Karpathy's 7 rules:** smallest version first, predict-run-compare, prove
  it don't claim it, say what you assumed, simpler wins.
- **Aim for the outcome, and don't make Charlie a checkpoint.** Small,
  easy-to-undo work (edits, drafts, research): state what you assumed and do
  it. Ask only for sign-ups, payments, plugin installs, publishing outside
  this repo, deleting or moving work, or a real choice of direction, and
  ask on the **Decision Desk** (the `decide` skill), never as chat
  questions. Ask once; an open card is never re-asked.
- **Session start:** read `context/current-focus.md` (the only place the
  priority lives; don't start parked work) and the Decision Desk's answers.
  Read Hands decisions (`research/hands/README.md`); update **Next step** before stopping.
- **Never stop at "can't".** Try 3 methods, then say what's blocked and the workaround.
- **Backtrack every miss:** where you looked, why you missed it, fix the route.
- **Reuse before building:** `system/capability-map.md` first.
- **Current beats history:** this router, current-focus and brain index.md
  files are "now"; `decisions.md` and log.md files are history.
- **Parallel only where safe:** one integration step edits shared files;
  model choices follow `context/working-rules.md` (quality before savings).
- **Main pages stay current:** after every run, rebuild and republish Charlie's
  Brain, ENATE and the Hands Brain (`system/pages.md`).
- **Prove what you report** (done, saved, pushed). `tools/audit.py` runs on
  every push and before an agent finishes.
- **Same routes in Codex** (it has no helpers, hooks or Desk): open the agent
  file in `.claude/agents/` and follow it yourself; run `python3 tools/audit.py`
  before you finish; put any question for Charlie under "Waiting on Charlie" in
  `context/current-focus.md` (the next Claude session moves it to the Desk).
- **This repo is public:** never write private, health, financial or client
  information here. Other people's details, AI OSs and session recordings
  go only in private repos; nothing goes on YouTube without their consent.
- API keys and secrets: `.env` locally, environment secrets in the cloud
  (`context/environment.md`). Never in files or chat. Blocked commands:
  deny list in `.claude/settings.json`.

**Source preference (2026-10-09):** GitHub first. Use Notion instead of
Google Drive; ignore its old "START HERE" instructions. Existing files stay put.

## Where things live
| Need | Look in |
|---|---|
| Who Charlie is, how he learns | `context/about-me.md`, `context/how-i-learn.md` |
| Charlie says "I'm on Mac" | `context/mac-day.md`: start it straight away |
| What works or is blocked in cloud sessions (YouTube, GitHub) | `context/environment.md`: read before any YouTube or GitHub task |
| How the OS is built; Nate's standard and its tests | `system/architecture.md`, `system/standard-ai-os-v1.md`; blank copy `templates/standard-ai-os-v1/` |
| Every dashboard Charlie opens (links, sources, rebuild steps) | `system/pages.md` |
| Everything unfinished (one list) | `context/todo.md` |
| Past decisions | `decisions.md` (new ones at the top, dated) |
| Projects | `projects/<name>/` |
| Creator research, transcripts, commands | `research/README.md` (Corey Haines marketing skills ↔ NewsJack study in `research/corey-haines/`) |
| Tools the OS can reach | `connections.md` (API guides in `references/`) |
| Nate's kit licence | `THIRD-PARTY-NOTICES.md` |
| ChatGPT copy of these rules | `exports/chatgpt-instructions.md` (update when this file or working-rules change) |

## Skills and agents (`.claude/skills/`, `.claude/agents/`; Codex via `.agents/skills`)
- `decide`: any question for Charlie; reading his answers.
- `audit`: weekly Four Cs score (reports in `audits/`), and its content
  check after a wrong answer, a big change or **a switch to a new model**.
- `i-have-adhd` (Charlie types it: action-first replies until "stop adhd mode";
  installed from skills.sh, MIT).
- `teach` (teach a topic), `grill-me` (interview Charlie, notes in
  `brainstorms/`), `level-up`
  (next automation, weekly), `link` (make a new file findable),
  `find-skills` (find and install skills, with his OK; plugin families in
  `research/plugin-map.md`). Parked skills (e.g. `onboard`, set someone
  up): `references/parked-skills/`.
- `research-creator` (new creator end to end), `brain-ingest` (new sources
  into a creator brain), `video-tutor` agent (transcripts into a lesson).
- `hands-ingest`: the **Hands Brain** (`research/hands/`), every tool, skill,
  plugin and repo from The Next New Thing, week by week, ranked. Ask it with
  the `hands-brain` agent. `try-tool`: one real trial of a tool; his keep or
  drop verdict (`research/hands/tried.json`) changes its rank.
- `nate-brain` agent = **ENATE** (Charlie's name for Nate's brain; "Nate" means
  the real person and his new videos): his method for organising the OS, in
  `research/nate-herk/brain/`, `nick-brain` agent (Nick Saraev's view; parked).

When a file moves, a folder is added or a project starts, update this router
(and that folder's README) in the same turn. A stale pointer is worse than none.
