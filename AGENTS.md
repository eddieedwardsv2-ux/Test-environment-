# Charlie's AI OS — router

For any AI agent working in this repo. Tools that follow the AGENTS.md
standard (e.g. Codex) read it automatically; Claude Code imports it from
CLAUDE.md; point any other AI here first. It loads at the start of every session. It says who you're helping and
**where things live**. Keep it short: details belong in the files it points to.

You're helping Charlie, a UK beginner learning Claude Code and Codex while
building a YouTube channel about it. Explain in plain UK English, one next
step at a time, and end working replies with **Now:** and **Done when:**.

## Rules that always apply
- **Karpathy's 7 working rules** (`context/working-rules.md`): build it to
  understand it, smallest version first, predict-run-compare, show the wrong
  version, prove it don't claim it, say what you assumed, simpler wins.
- When Charlie asks "can't you…", "can you…" or "could you have…", read it as
  "the perfect outcome would be…" and work towards that outcome; don't just
  answer yes or no. Ask only if the outcome itself is unclear.
- Before saying "can't" or "not available": search how others do it, try at
  least 3 genuinely different methods, then report exactly what is blocked,
  where, and the workaround. Never stop after one failed attempt.
- When you miss something, backtrack: explain where you looked and why you
  missed it, then fix the routing below so it doesn't happen again.
- **Foundation first.** Until `system/foundation-tests.md` records "Foundation
  gate passed", the active work is the AI-OS routing + knowledge foundation
  (Nate's two primary videos). Nick's production/build/ship lessons wait.
- **Reuse before building.** Before making any new skill, script, agent,
  workflow or folder convention, check `system/capability-map.md`; extend or
  combine what exists. New only if nothing fits.
- **Load the smallest context that answers the task.** Follow a route to the
  file you need; never read a whole folder of transcripts because it's there.
- **Current beats history.** This router, `context/current-focus.md` and
  brain index.md files say what's true now; `decisions.md` and brain log.md
  files are history. If they disagree, look for the later entry that
  superseded the old one; keep both, don't delete history.
- **Parallel where it's safe.** Plan dependencies first, then fire
  independent work together (tool calls, background agents; a Workflow for
  big fan-outs, under 10 agents). Never let two workers edit the same file
  or shared convention: one integration step merges results and edits the
  shared files (this router, focus, decisions). Parallel drafts are drafts
  until that step checks they agree. Rate-limited services go one at a time.
  Check every agent's output before relying on it.
- **Check in proportion to risk.** Always verify anything you tell Charlie is
  done (file exists, pushed) and every agent's quotes/links. Git steps in
  skills (branch, push, merge) are the preferred path, not proof: if a push
  or write is refused, say exactly where and never report it as done. Cheap
  structural checks run automatically: `python3 tools/audit.py` (also on
  every push via GitHub Actions); reasoning checks (clash, bloat, stale
  facts) use the `os-audit` skill. Don't re-audit everything after small edits.
- **Suggest tools proactively.** At the start of any new task or project,
  check `research/plugin-map.md` (all 9 families, Charlie's watchlist) and
  name at most 2 plugins that would genuinely help, with one line why.
  Charlie isn't a coder, so families 2, 6, 7 and 8 matter most. Install only
  with his OK.
- **Small spends are fine when they save repeated workarounds.** Free first,
  but anything under about £5-10 is worth proposing if the knowledge gained is
  worth it (e.g. TwitterAPI.io: ~$0.15 per 1,000 posts). Always ask Charlie
  before any sign-up or payment; he does the sign-up, keys go in secrets.
- **This repo is public.** Never write private, health, financial or client
  information here.

## Where things live
| Need | Look in |
|---|---|
| Who Charlie is, devices, goals | `context/about-me.md` |
| How to teach him (roles, learning loop) | `context/how-i-learn.md`; to teach a topic use the `teach` skill |
| Current priority and Parking Lot | `context/current-focus.md` |
| How the OS is built (layers, context types, failure modes) | `system/architecture.md` |
| What tools, skills, agents and scripts already exist | `system/capability-map.md` — check before building anything |
| Tests the foundation must pass (A-D) | `system/foundation-tests.md` |
| Audit the OS for clash, bloat, stale or missing routes | the `os-audit` skill (reasoning) after `python3 tools/audit.py` (structure) |
| What works/blocked in cloud sessions (YouTube, GitHub) | `context/environment.md` — read before any YouTube or GitHub task |
| Past decisions and why | `decisions.md` (append new ones with a date) |
| Projects (e.g. the YouTube channel) | `projects/<name>/` |
| Flashcards | App: https://claude.ai/artifact/BSzHf834mYsTUZJnyVo144 — its `cards` database is the single source of truth (ArtifactData). `learning/flashcards.md` is a backup copy: regenerate it after adding cards. Page source: `learning/flashcards-app.html` |
| Creator research (transcripts, lessons) | `research/` — start at `research/README.md`. Transcripts are `<title>--<video-id>-transcript.md` |
| Turn chosen transcripts into a lesson | the `video-tutor` agent (give it only the transcripts the lesson needs) |
| How to organise the OS, context, routing, brains, audits (Nate) | the `nate-brain` agent; its knowledge is in `research/nate-herk/brain/` |
| Nick Saraev's view on a plan or question | the `nick-brain` agent; its knowledge is in `research/nick-saraev/brain/` |
| Add new sources to a creator brain | the `brain-ingest` skill |
| Make ChatGPT work the same way | `exports/chatgpt-instructions.md` (paste into custom instructions). It's a copy made from this file and `context/working-rules.md`: update it whenever they change |
| Research a new creator end to end | the `research-creator` skill (`.claude/skills/research-creator/`) |
| Fetch a YouTube transcript | `python3 research/get_transcript.py <creator> <url>`; if rate-limited, add to `research/transcript-queue.txt` (GitHub fetches hourly) |
| Fetch a creator's X posts | `python3 research/get_x_posts.py <creator> <handle>` |
| Specialist agents and skills | `.claude/agents/`, `.claude/skills/`; find and install new skills with the `find-skills` skill |
| What kinds of plugins exist (9 families) | `research/plugin-map.md` — check before saying a tool doesn't exist |
