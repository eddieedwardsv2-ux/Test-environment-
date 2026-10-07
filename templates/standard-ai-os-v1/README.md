# Standard AI-OS v1 (not yet personalised)

A blank AI operating system built only from Nate Herk's teaching. The full
requirement list, with a quote and timestamp for each, is in
`system/standard-ai-os-v1.md` at the root of this repo. The person's details are
left as _not yet personalised_ placeholders.

## The filing cabinet (level 1: where everyone starts)
```
AGENTS.md            router: who, how to work, where things live (points, doesn't store)
CLAUDE.md            imports AGENTS.md (one router, every tool)
context/             always-true background: about-me, current-focus
decisions.md         dated, append-only decision log
projects/<name>/     one folder per project or client; usually the biggest
.claude/skills/      repeatable procedures   .claude/agents/  specialists
.gitignore           keeps .env (secrets) out of Git
```
Created when first needed: `brainstorms/` (grill-me notes), `audits/` (saved
audit reports), `archives/` (old material), `research/` (level 2 knowledge base).

## Use it
1. Copy this folder to a new private GitHub repo (the repo is the backup).
2. Fill `context/about-me.md` and `context/current-focus.md` with a grill-me
   interview, not a quick brain dump.
3. Add the three core skills (copy from this repo's `.claude/skills/` and
   replace the owner's name): `grill-me`, `os-audit` (weekly, read-only, saved
   to `audits/`), `brain-ingest` (only once you have a `research/` brain).
4. **Test it:** open a fresh session and ask "who am I, what's my priority,
   where would a new project go, where are past decisions?" Every answer
   should name a real path. If one doesn't, backtrack and fix the route.

## Move up a level only when it hurts
Level 2 (`research/` wiki with index and log) when you have about 30+ notes and
keep forgetting what's in them. Semantic search, knowledge graphs and
always-on agents only for a measured problem the level below can't fix.
