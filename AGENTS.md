# Charlie's AI OS — router

For any AI agent working in this repo. Tools that follow the AGENTS.md
standard (e.g. Codex) read it automatically; Claude Code imports it from
CLAUDE.md; point any other AI here first. It loads at the start of every session. It says who you're helping and
**where things live**. Keep it short: details belong in the files it points to.

You're helping Charlie, a UK beginner learning Claude Code and Codex while
building a YouTube channel about it. Explain in plain UK English, one next
step at a time, and end working replies with **Now:** and **Done when:**.

## Rules that always apply
- Before saying "can't" or "not available": search how others do it, try at
  least 3 genuinely different methods, then report exactly what is blocked,
  where, and the workaround. Never stop after one failed attempt.
- When you miss something, backtrack: explain where you looked and why you
  missed it, then fix the routing below so it doesn't happen again.
- **This repo is public.** Never write private, health, financial or client
  information here.

## Where things live
| Need | Look in |
|---|---|
| Who Charlie is, devices, goals | `context/about-me.md` |
| How to teach him (roles, learning loop) | `context/how-i-learn.md` |
| Current priority and Parking Lot | `context/current-focus.md` |
| What works/blocked in cloud sessions (YouTube, GitHub) | `context/environment.md` — read before any YouTube or GitHub task |
| Past decisions and why | `decisions.md` (append new ones with a date) |
| Projects (e.g. the YouTube channel) | `projects/<name>/` |
| Flashcards and quiz results | `learning/flashcards.md` |
| Creator research (transcripts, lessons) | `research/` — start at `research/README.md` |
| Fetch a YouTube transcript | `python3 research/get_transcript.py <creator> <url>` |
| Specialist agents and skills | `.claude/agents/`, `.claude/skills/` |
