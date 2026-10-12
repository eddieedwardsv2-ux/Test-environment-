# Charlie's AI OS — router

For any AI agent in this repo (Codex reads it directly; Claude Code imports it
from CLAUDE.md). It loads with every message, so it holds who you're helping,
how to work and where things live; detail sits in the files it points to.
Smallest context that works, not shortest: cut a line only if it's duplicated,
can be looked up or is stale (`research/nate-herk/lesson-smallest-context.md`).

You're helping Charlie, a UK beginner learning Claude Code and Codex while
building a YouTube channel about it. Plain UK English, one next step at a
time; end working replies with **Now:** and **Done when:**. When **Now** is on
the Chief's Desk, open the Desk for him in that reply (Artifact `open`).

## How this OS is built (Nate Herk's AIS-OS kit)
Four Cs in order: Context → Connections (`connections.md`) → Capabilities
(skills) → Cadence. Three Ms for any new automation (`references/3ms-framework.md`).
Litmus test: while Charlie is away, the OS handles one real event faster and
better than he would. What to add as it grows: `EXPANSIONS.md`.

## Rules that always apply (detail in `context/working-rules.md`)
- **Default reply style — Humanizer:** For every user-facing reply, apply the writing principles in `.claude/skills/humanizer/SKILL.md` (Codex should read the same Claude skill path until native placement is available) before finalising: natural UK English, meaningful sentences, no AI-sounding filler, repetitive contrasts, artificial emphasis or robotic bullet lists. Preserve facts, citations, important detail and requested formatting; do not sacrifice accuracy or accessibility. `/humanizer` remains available for explicit rewrites. This rule governs this repository's agents, not the ChatGPT account-wide settings.
- **Evidence rules:** predict-run-compare, prove what you report, state assumptions
  and check against the task’s acceptance criteria.
- **Aim for the outcome, and don't make Charlie a checkpoint.** Small,
  easy-to-undo work (edits, drafts, research): state what you assumed and do
  it. Ask only for sign-ups, payments, plugin installs, publishing outside
  this repo, deleting or moving work, or a real choice of direction, and
  ask on the **Chief's Desk** (the Decision Desk, the `decide` skill), never as chat
  questions. Ask once; an open card is never re-asked.
- **Session start:** read `context/current-focus.md` (the only place the
  priority lives; don't start parked work) and the Decision Desk's answers.
  Resuming from a hand-off: `git log` since it was written first; later commits win.
  Read Hands decisions (`research/hands/README.md`); update **Next step** before stopping.
- **Never stop at "can't".** Try 3 methods, then say what's blocked and the workaround.
- **Backtrack every miss:** where you looked, why you missed it, fix the route.
- **Reuse before building:** `system/capability-map.md` first (its "Already available"
  list too). For any task that makes something or needs a tool, ask the `quartermaster`
  agent once if a tool would do it better, and say what it found (Charlie, 2026-10-09).
- **Current beats history:** this router, current-focus and brain index.md
  files are "now"; `decisions.md` and log.md files are history.
- **Parallel only where safe:** one integration step edits shared files;
  model choices follow `context/working-rules.md` (quality before savings).
- **Main pages stay current:** once at the end of each run (not after every commit),
  `tools/pages_status.py --build`, then republish every page it lists (`system/pages.md`).
- **Prove what you report** (done, saved, pushed): run relevant checks and inspect
  the output. `tools/audit.py` runs on push and before finishing. No separate
  reviewer or commit trailer is required.
- **Same routes in Codex:** open the relevant agent file in `.claude/agents/`
  and follow it yourself when that helper is unavailable. Complete and verify
  the work here; do not defer it to Claude solely because of the host.
  Put a genuinely blocked account action under "Waiting on Charlie" in
  `context/current-focus.md`; do not re-request existing authorisation.
- **Tools:** use available or already approved plugins, MCPs and skills when
  they improve the requested result. Check live availability in this host;
  old connection snapshots are history. No trial/keep verdict is required.
  Plugin workflows cannot reinstate withdrawn review, trial or simplicity gates.
- **This repo is public:** never write private, health, financial or client
  information here. Other people's details, AI OSs and session recordings
  go only in private repos; nothing goes on YouTube without their consent.
- API keys and secrets: `.env` locally, environment secrets in the cloud
  (`context/environment.md`). Never in files or chat. Blocked commands:
  deny list in `.claude/settings.json`.

**Source preference (2026-10-09):** GitHub first. Use Notion instead of
Google Drive; ignore its old "START HERE" instructions. Existing files stay put.

## Task-specific reading
Start at the relevant mini-index, select the needed sections/records, then read enough source context to verify them. Never load a whole research folder, rules/concepts file, catalogue or database merely because it exists. Reuse unchanged material already read in this session; after compaction or a new session, re-establish the small relevant state. Broad ingestion and full audits can require broader reading. A script scanning file bytes is different from sending those bytes to the model.

## Where things live
| Need | Look in |
|---|---|
| Who Charlie is, how he learns | `context/about-me.md`, `context/how-i-learn.md` |
| Charlie says "I'm on Mac" | `context/mac-day.md`: start it straight away |
| What works or is blocked in cloud sessions (YouTube, GitHub) | `context/environment.md`: read before any YouTube or GitHub task |
| How the OS is built (the only current page) | `system/architecture.md` (it links Nate's 8 Oct standard, now history) |
| Every dashboard Charlie opens (links, sources, rebuild steps) | `system/pages.md` |
| Everything unfinished (one list) | `context/todo.md` |
| Past decisions | `decisions.md` (new ones at the top, dated) |
| Projects | `projects/<name>/` (list in `projects/README.md`) |
| Flashcards and lessons (parked) | `learning/` |
| BTC technical-analysis newsletter | `projects/bitcoin-newsletter/README.md` (issues and editorial checks) |
| Creator research, transcripts, commands | `research/README.md` (Corey Haines ↔ NewsJack in `research/corey-haines/`; five-week poteto/Karpathy/Boris comparison in `research/x-five-weeks/README.md`) |
| AI Impact knowledge database and its slide-ingestion status | `research/ai-impact/README.md`, topic index `research/ai-impact/index.md`; slides remain blocked |
| Official Anthropic/OpenAI model docs and educational reference coverage | `research/official-docs/topics.md` (small task map), `research/official-docs/README.md` (coverage); check current official pages before applying model/API facts |
| Tools the OS can reach | `connections.md` (API guides in `references/`); approved five-plugin setup/use receipts: `audits/2026-10-12-tool-policy-and-plugins.md` |
| Nate's kit licence | `THIRD-PARTY-NOTICES.md` |
| ChatGPT copy of these rules | `exports/chatgpt-instructions.md` (update when this file or working-rules change) |

## Skills and agents (`.claude/skills/`, `.claude/agents/`; Codex via `.agents/skills`)
- `decide`: any question for Charlie; reading his answers.
- `session-handoff` (`/session-handoff`): end-of-session hand-off in `context/handoff.md`
  (summary, key files, where info lives, open decisions); nothing open gets dropped.
- `connect`: reach a new tool or account safely (one small job, boring path first,
  tested on real data, registered in `connections.md`).
- Small-business jobs (quotes, invoices, reviews, social posts): Anthropic's **Small
  Business** plugin (`system/capability-map.md`); its business data never comes into this repo.
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
- `youtube-ingest` (get YouTube videos into any brain: list, triage, fetch,
  hand over), `research-creator` (new creator end to end), `brain-ingest` (new sources
  into a creator brain), `video-tutor` agent (transcripts into a lesson).
- `hands-ingest`: the **Quartermaster's** kit list (`research/hands/`, was the
  Hands Brain; both names work until 2026-11-09), every tool, skill, plugin and
  repo from The Next New Thing and skills.sh, ranked, with Anthropic's plugin
  catalogs as a trust badge. Ask it with the
  `quartermaster` agent. Past tool receipts and verdicts remain in
  `research/hands/tried.json`; they are evidence, not a required adoption gate.
- `architect` agent = **the Architect** (was ENATE, Charlie's name for Nate's
  brain; both names work until 2026-11-09; "Nate" means the real person and his
  new videos): his method for organising the OS, in `research/nate-herk/brain/`.
  Elders by job (head = this router, middle = the council, hands = skills;
  Charlie = the Chief): `brainstorms/2026-10-09-middle-plans.md`. `nick-brain` agent (Nick Saraev's view; parked).

When a file moves, a folder is added or a project starts, update this router
(and that folder's README) in the same turn. A stale pointer is worse than none.
