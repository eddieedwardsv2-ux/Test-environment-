# AI OS — router

Loads at the start of every session, for any AI tool (Claude Code reads it via
`CLAUDE.md`; Codex and others read `AGENTS.md` directly). It says who you're
helping, how to work and **where things live**. It points; it doesn't store.
Keep it under 200 lines (it's re-read with every message): details belong in
the files below. Edits take effect in a new session.

You're helping the person described in `context/about-me.md`. Their current
priority is in `context/current-focus.md`.

## Rules that always apply
- **Follow the routes.** Load the smallest context that answers the task:
  this table first, then the one file or folder it points to. Never read a
  whole folder because it's there. Look local first, live sources last.
- **Current beats history.** This file and `context/current-focus.md` say
  what's true now; `decisions.md` and `log.md` files are history.
- **Before big or hard-to-undo work, be 95% sure what's wanted** (ask if
  not); small, easy-to-undo work: say what you assumed and carry on. **Define done before starting**; build the simplest version first. Prefer a
  script or a fixed workflow over an AI agent when either would do.
- **Prove it, don't claim it.** Run or check something before saying it works.
  Quote sources exactly; label anything unsourced as inference.
- **Feed corrections back.** When corrected, update the file or skill that
  caused it so it doesn't happen again.
- **Backtrack every miss.** If you didn't find something that exists, say
  where you looked and why you missed it, then fix the route in this file.
- **Keep this file current.** Add a row when you add a folder, skill or tool;
  log the change in `decisions.md`.
- **Secrets** live in `.env` (ignored by Git); never paste keys into chat or files.

## Where things live
| Need | Look in |
|---|---|
| Who I am, my goals, stack, preferences | `context/about-me.md` |
| What matters now, what's parked | `context/current-focus.md` |
| Past decisions and why (add a dated entry at the top) | `decisions.md` |
| Ongoing work and deliverables | `projects/<name>/` (how to start one: `projects/README.md`) |
| Secrets and API keys | `.env` (ignored by Git) |
| Knowledge base: raw sources (transcripts, articles) + derived brain (level 2, add when needed) | `research/README.md` |
| Skills: `grill-me` (interview me), `os-audit` (weekly check) | `.claude/skills/` (Codex reads the same files via `.agents/skills`) |
| Specialist agents (create when first needed) | `.claude/agents/` |
| How to set this OS up | `README.md` |
| Interview notes from grill-me sessions | `brainstorms/` (created by the skill) |
| Audit reports (read the latest before a new audit) | `audits/` (created by the audit) |
| Old material that's no longer current | `archives/` (create when first needed) |
