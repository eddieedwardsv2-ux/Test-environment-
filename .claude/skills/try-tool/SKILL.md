---
name: try-tool
description: Gives one tool from the Quartermaster's list (was the Hands Brain) a safe, real trial on Charlie's own work and records his keep or drop verdict, which changes its rank. Use for "try <tool>", "test this tool", "is <tool> any good for me".
---

# Try a tool (built from the HyperFrames trial, 2026-10-09)

The Hands Brain ranks tools from what a show says. This skill adds what
happened when Charlie actually used one. ENATE Rules 23, 34 and 43: a new
tool reports only until tested, on our own work, cost counted.

1. **Pick:** ask `quartermaster` for the #1 tool for the job that Charlie
   doesn't already have. Read its page and its `check` flag. Say price, what
   it installs, and the risks.
2. **Ask once:** a Decision Desk card for the install (the `decide` skill),
   unless Charlie already said yes to this tool.
3. **Install in a scratch folder first** (the scratchpad), never globally.
   Count what it adds: files, size, and skill descriptions that would load
   every message (`grep -m1 '^description:'` over its SKILL.md files).
   Afterwards check `~/.claude/skills/` too: HyperFrames' own CLI quietly
   added 10 skills there (machine-wide, gone when a cloud session ends).
   Say so; deleting outside the repo needs Charlie's OK.
   HyperFrames added 21 skills, about 6,000 characters: too much to keep in
   the repo, so the trial ran in scratch only.
4. **One real task** from Charlie's work (a channel clip, a page, a script).
   Run the tool's own checks, fix what they flag, and look at the result
   (a frame, a screenshot). Time it.
5. **Show Charlie** the output (`SendUserFile`) and put his verdict on the
   Desk: keep / drop / later, with what keeping it would add to the repo.
6. **Record** in `research/hands/tried.json`: `{name, date, task, result,
   time, cost, adds, verdict: "keep|drop|later|pending", why}`. Then run
   `python3 tools/build_hands.py` (keep = +5 to its score, drop = bottom of
   its category with the reason shown), and republish the main pages.
7. Nothing stays installed in the repo unless the verdict is "keep".
