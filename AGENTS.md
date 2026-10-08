# Charlie's AI OS — router

For any AI agent working in this repo. Tools that follow the AGENTS.md
standard (e.g. Codex) read it automatically; Claude Code imports it from
CLAUDE.md; point any other AI here first. It loads with every message and
says who you're helping, how to work and **where things live**. Keep it under
200 lines (the audit checks): details belong in the files it points to.

You're helping Charlie, a UK beginner learning Claude Code and Codex while
building a YouTube channel about it. Explain in plain UK English, one next
step at a time, and end working replies with **Now:** and **Done when:**.

## How this OS is built (Nate Herk's AIS-OS kit)
- **Four Cs, in order:** Context (knows Charlie) → Connections (reaches his
  tools, `connections.md`) → Capabilities (skills) → Cadence (runs on its own).
- **Three Ms** for any new automation: Mindset, Method, Machine
  (`references/3ms-framework.md`; the `level-up` skill walks it).
- **Litmus test:** while Charlie is away, the OS handles one real event
  faster and better than he would. What to add as it grows: `EXPANSIONS.md`.

## Rules that always apply (longer detail, where needed, in `context/working-rules.md`)
- **Karpathy's 7 rules** (`context/working-rules.md`): smallest version first,
  predict-run-compare, prove it don't claim it, say what you assumed, simpler wins.
- **Aim for the outcome.** Read "can you…" as "the perfect outcome would
  be…" and work towards it. Before big or hard-to-undo work (new tools,
  settings, publishing, spending) be 95% sure what's wanted, or ask 1-2
  questions with your recommended answer. Small, easy-to-undo work: say
  what you assumed and get on with it.
- **Never stop at "can't".** Try at least 3 different methods first, then say
  exactly what's blocked, where, and the workaround.
- **Backtrack every miss:** say where you looked and why you missed it, then
  fix the route below.
- **Focus.** The priority lives only in `context/current-focus.md`; don't start
  parked work. Before a session ends, update its **Next step**.
- **Reuse before building:** check `system/capability-map.md` first.
- **Smallest context; current beats history.** Follow a route to the one file
  you need. This router, current-focus and brain index.md files are "now";
  `decisions.md` and log.md files are history (keep both).
- **Parallel only where safe:** one integration step edits shared files;
  check every agent's output; helpers run on `model: sonnet` (details in
  `context/working-rules.md`).
- **Prove what you report** (done, saved, pushed). `tools/audit.py` runs on
  every push and before an agent finishes; the `os-audit` skill weekly.
- **Ask Charlie before** any sign-up, payment or plugin install. Suggest at
  most 2 helpful plugins per new task (`research/plugin-map.md`).
- **This repo is public:** never write private, health, financial or client
  information here. Other people's details, AI OSs and session recordings
  go only in private repos; nothing goes on YouTube without their consent.

## Where things live
| Need | Look in |
|---|---|
| Who Charlie is, devices, goals | `context/about-me.md` |
| How to teach him (roles, learning loop) | `context/how-i-learn.md`; to teach a topic use the `teach` skill |
| Current priority and Parking Lot | `context/current-focus.md` |
| How the OS is built (layers, context types, failure modes) | `system/architecture.md` |
| Nate's standard: every requirement, quote and status, plus the foundation tests | `system/standard-ai-os-v1.md` |
| Blank, not-yet-personalised copy of this OS | `templates/standard-ai-os-v1/` |
| What agents are blocked from running (force-push, hard reset, `rm -rf`) | deny list in `.claude/settings.json` |
| API keys and secrets | `.env` locally (Git ignores it); in cloud sessions and GitHub, environment secrets (`context/environment.md`). Never in files or chat |
| What tools, skills, agents and scripts already exist | `system/capability-map.md` — check before building anything |
| Audit the OS (weekly, scored on the Four Cs) | the `audit` skill (reports in `audits/`), after `python3 tools/audit.py` (structure gate: runs on every push and before an agent finishes, `tools/run_gate.sh`) |
| Wrong or missed answer; clash, bloat or stale facts | the `os-audit` skill (four failure modes, backtrack) |
| Check a page or visual output looks right | `python3 tools/screenshot.py <page>`, then look at the PNGs (needs `pip install playwright` each cloud session) |
| Get knowledge out of Charlie's head (interview) | the `grill-me` skill; notes saved in `brainstorms/` |
| Set someone up from scratch (7-question intake) | the `onboard` skill, reading `aios-intake.md` |
| Make a new file, folder or source findable | the `link` skill (adds the smallest route here or in a folder index) |
| Find and ship the next automation (weekly) | the `level-up` skill (one run = one artifact, logged in `decisions.md`) |
| What tools the OS can reach, and their status | `connections.md` (API guides in `references/`) |
| Where Nate's kit files came from (MIT licence) | `THIRD-PARTY-NOTICES.md` |
| What works/blocked in cloud sessions (YouTube, GitHub) | `context/environment.md` — read before any YouTube or GitHub task |
| Past decisions and why | `decisions.md` (add new ones at the top, with a date) |
| Projects (e.g. the YouTube channel) | `projects/<name>/` |
| Flashcards | App: https://claude.ai/artifact/BSzHf834mYsTUZJnyVo144 — its `cards` database is the single source of truth (ArtifactData). `learning/flashcards.md` is a backup copy: regenerate it after adding cards. Page source: `learning/flashcards-app.html` |
| Creator research (transcripts, lessons) | `research/` — start at `research/README.md`. Transcripts are `<title>--<video-id>-transcript.md` |
| Turn chosen transcripts into a lesson | the `video-tutor` agent (give it only the transcripts the lesson needs) |
| See or review Nate's 38 concepts and 40 rules (mark confusing / delete) | App: https://claude.ai/artifact/LhRdXG3KpeBnGpxNhFQsjf; marks are in its `flags` database (ArtifactData). Rebuild after brain changes: `python3 tools/build_brain_map.py`, then republish `research/nate-herk/brain/map/brain-map.html` |
| Ask Nate's view: how to organise the OS, context, routing, brains, audits, levels | the `nate-brain` agent; its knowledge is in `research/nate-herk/brain/` and `system/standard-ai-os-v1.md` |
| Nick Saraev's view on a plan or question | the `nick-brain` agent; its knowledge is in `research/nick-saraev/brain/` |
| Add new videos or posts to any creator brain (Nate, Nick) | the `brain-ingest` skill |
| Make ChatGPT work the same way | `exports/chatgpt-instructions.md` (paste into custom instructions). It's a copy made from this file and `context/working-rules.md`: update it whenever they change |
| Research a new creator end to end | the `research-creator` skill (`.claude/skills/research-creator/`) |
| Fetch a YouTube transcript | `python3 research/get_transcript.py <creator> <url>`; if rate-limited, add to `research/transcript-queue.txt` (GitHub fetches hourly) |
| Fetch a creator's X posts | `python3 research/get_x_posts.py <creator> <handle>` |
| Specialist agents and skills | `.claude/agents/`, `.claude/skills/` (Codex reads the same skills via `.agents/skills`); find and install new skills with the `find-skills` skill |
| What kinds of plugins exist (9 families) | `research/plugin-map.md` — check before saying a tool doesn't exist |

## Keep this router current
When a file moves, a folder is added or a project starts, update this router
(and that folder's README) in the same turn. A stale pointer is worse than no
pointer.
