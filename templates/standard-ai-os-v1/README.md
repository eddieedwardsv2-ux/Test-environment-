# Standard AI-OS v1 (not yet personalised)

A blank AI operating system built from Nate Herk's teaching (the full
requirement list, with quotes, lives in the repo this was copied from:
`system/standard-ai-os-v1.md`). Everything here is self-contained. The
person's details are left as _not yet personalised_ placeholders.

## The filing cabinet (level 1: where everyone starts)
```
AGENTS.md            router: who, how to work, where things live (points, doesn't store)
CLAUDE.md            imports AGENTS.md (one router, every tool)
context/             always-true background: about-me, current-focus
decisions.md         dated, append-only decision log
projects/<name>/     one folder per project or client; usually the biggest
.claude/skills/      grill-me (interview) and os-audit (weekly check), ready to use
.claude/agents/      specialists (create when first needed)
.gitignore           keeps .env (secrets) out of Git
```
Created when first needed: `brainstorms/` (grill-me notes), `audits/` (saved
audit reports), `archives/` (old material). `research/` holds only a guide
until you need a level 2 knowledge base.

## Use it
1. Copy this folder into a new private GitHub repo (the repo is the backup).
   Not sure how? Open it in Claude Code or Codex and ask: "make this folder a
   private GitHub repo".
2. Say "grill me about who I am and what I'm working on" to fill
   `context/about-me.md` and `context/current-focus.md`.
3. Every Friday, say "audit the OS" (or schedule it). Reports go in `audits/`.
4. **Test it:** open a fresh session and ask "who am I, what's my priority,
   where would a new project go, where are past decisions?" Every answer
   should name a real path. If one doesn't, backtrack and fix the route.

## Move up a level only when it hurts
Level 2 (`research/` wiki with index and log) when you have about 30+ notes and
keep forgetting what's in them. Semantic search, knowledge graphs and
always-on agents only for a measured problem the level below can't fix.
