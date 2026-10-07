---
name: os-audit
description: Read-only audit of this AI OS. Finds broken or missing routes, stale or clashing facts, bloat and duplicates, saves a dated report to audits/, proposes the smallest fixes and waits for approval. Use weekly (e.g. Fridays), after big changes, or when the AI missed something that exists.
---

# OS audit

**Read-only:** report, never fix, rename or delete. Fixes wait for a yes.

## Steps
1. **Read the last report** in `audits/` (if any): which findings are fixed,
   still open, or back again?
2. **Routes:** every path in `AGENTS.md` exists. **Reverse:** every folder,
   skill and agent has a route pointing to it.
3. **Index truth:** any index or README list matches the files on disk.
4. **Freshness:** `context/current-focus.md` and other "now" facts are still
   true; anything time-sensitive has a date.
5. **The four failure modes:** poisoning (a false fact), bloat (too much
   loaded, `AGENTS.md` growing), confusion (missing or wrong route), clash
   (two "current" files disagree).
6. **Save** the report as `audits/YYYY-MM-DD.md` (the only file this skill
   writes): one line per finding with evidence (`path:line`), what wrong
   answer it could cause, severity, and the smallest fix.
7. **Ask:** "Want me to do these? Yes/no per item." After fixing, log big
   changes in `decisions.md`.

## Backtrack (when the AI missed something that exists)
Write down what was asked, where it looked, which route sent it there, and
why it missed. Fix the route in `AGENTS.md`, then ask the question again to
prove the fix.
