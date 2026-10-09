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

## Working on            (the task in hand, in one or two lines)
## Summary points        (what got done; each with its commit or file)
## Key files             (made or changed this session: open these first)
## Where the information lives (files holding facts the next session needs,
                          changed or not: decisions, plans, reports, Desk)
## Decisions made        (what Charlie chose this session, so it isn't re-asked)
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
- Pages: `python3 tools/pages_status.py --build`; republish every page it lists, then
  `--mark` each (`system/pages.md`). Also `Artifact` `list`: any page not in
  `system/pages.md` gets a row there (two were found unlisted on 9 Oct).
- `python3 tools/audit.py`, commit, push, check `git status` is clean.

## 5. The paste-back message (Charlie's routine: hand off, copy, `/clear`, paste)
End the reply with one fenced code block he can copy in one go, under 40 lines,
that works on its own in a blank window:
- First line: `Resuming from a session hand-off. Read context/handoff.md and
  context/current-focus.md first, then continue from "Pick up here".`
- Then the same headings as the file, each as short bullets: Working on, Summary
  points, Key files, Where the information lives, Decisions made, Open decisions,
  Pick up here.
- Plain text only: no links that need the old chat, no "as we discussed".
Above the block: **VERIFIED** / **NOT VERIFIED** for "saved and pushed". Below it,
one line: "Copy this, type `/clear`, paste it in." The file is the backup if the
copy is lost (cloud containers are wiped, so it must be pushed first).
