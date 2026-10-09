---
name: session-handoff
description: Writes the end-of-session hand-off in context/handoff.md (summary, key files, where info lives, open decisions) without dropping open items. Use for "/session-handoff", "hand off", "wrap up", "near the usage limit", or before a long session stops.
---

# Session hand-off

One file, `context/handoff.md`, overwritten each time; history stays in
`decisions.md` and Git. Every agent reads it first (Claude, Codex, ChatGPT).
Built 2026-10-09 after a hand-off rewrite silently dropped about 8 open items
and an Elder plan sat on an unmerged branch while three Desk cards pointed at it.

## 1. Gather (cheap reads, no helpers)
- The **old** `context/handoff.md`: read it before overwriting.
- `git log --oneline` since its "Written" date; `git status` (anything unsaved?).
- Branches with work not on main: `git fetch --unshallow` if the clone is
  shallow, then for each `origin/*` branch list files it has that main lacks.
- Desk: `ArtifactData` `list` `decisions`; note every `open` or `answered` card
  and check each card's linked file exists on main.
- `context/todo.md`, the **Next step** in `context/current-focus.md`, and
  "Waiting on Charlie" there (Codex's questions).
- What this session did (your own context).

## 2. Carry-forward check (the rule that stops things getting lost)
Every open item in the old hand-off must land in exactly one place: the new
hand-off, `context/todo.md`, or closed with proof (commit or file). Anything
you drop goes under "Dropped" with one-line why. Never shorten the file by
deleting items that are still open.

## 3. Write `context/handoff.md` (about 60 lines, plain UK English)
```
# Session hand-off
**Written:** <date, time UK>, by <Claude/Codex/ChatGPT>; why it stopped.

## Summary points        (what got done; each with its commit or file)
## Key files             (made or changed this session: open these first)
## Where the information lives (files holding facts the next session needs,
                          changed or not: decisions, plans, reports, Desk)
## Open decisions        (Desk card ids still open; choices not yet on the
                          Desk; anything waiting on Charlie)
## Pick up here          (1-3 steps, in order)
## Carried forward / dropped
```

## 4. Tidy, save, prove
- New unfinished items go into `context/todo.md`; one-line **Next step** in
  `current-focus.md` points to the hand-off. Real decisions go at the top of
  `decisions.md`.
- A choice that needs Charlie becomes a Desk card (`decide` skill), not just a
  line here. Codex has no Desk: write it under "Waiting on Charlie".
- Work stranded on a branch: bring the file to main, or list it under Open decisions.
- Only when Charlie says Codex or ChatGPT is next: also refresh the hand-off in `exports/`.
- `python3 tools/audit.py`, commit, push, check `git status` is clean.
- Reply in chat with the 4 headings as short bullets, then **VERIFIED** /
  **NOT VERIFIED** for "saved and pushed".
