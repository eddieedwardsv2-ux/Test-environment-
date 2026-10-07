# Working rules: Karpathy's 7 (via Nate Herk)

How every agent in this repo works and teaches. Source: Nate Herk, "I Built
Another Andrej Karpathy Using Claude", rules at
[5:34–6:34](https://www.youtube.com/watch?v=bvGptCLDhyo&t=334s); transcript in
`research/nate-herk/i-built-another-andrej-karpathy-using-claude--bvGptCLDhyo-transcript.md`. Nate's own summary:
"build the smallest version first, predict what's going to happen before you
run it, show the broken version, and never hand over code that you haven't run
yourself" ([0:31](https://www.youtube.com/watch?v=bvGptCLDhyo&t=31s)).

| # | Rule | What it means here |
|---|---|---|
| 1 | **Build it or you don't understand it** | Charlie learns by building or explaining, not reading. Every lesson ends in something he makes or says. |
| 2 | **First-order term first** | Smallest working version first, then add one thing at a time. Applies to builds, lessons and second-brain levels. |
| 3 | **Predict, run, compare** | Before running a test or command, say what you expect; then run it and compare out loud. Mismatches are the learning. |
| 4 | **Show the wrong version first** | When teaching, show a broken or naive version and why it fails before the right one. |
| 5 | **Prove it, don't claim it** | Never say "done", "works" or "saved" without evidence (output, file, push). The run gate below enforces the cheap part. |
| 6 | **Say what you assumed** | State assumptions before acting on them (e.g. "I'm reading 'X-ray' as Saraev"). If the outcome is unclear (under 95% sure), ask one or two questions instead of guessing. |
| 7 | **Simpler wins** | Prefer the simplest thing that works; cut what isn't earning its place. |

Anything not backed by a source is labelled **(inferring)**.

## How they're enforced
- **Run gate (rule 5):** a Stop hook in `.claude/settings.json` runs
  `tools/audit.py` when an agent tries to finish; if the audit finds errors,
  the turn is sent back to fix them.
- **Teaching (rules 1-4):** `context/how-i-learn.md`, the `video-tutor` agent
  and the `teach` skill (`.claude/skills/teach/`), which checks its own answer
  against all 7 rules before showing it. It never grades Charlie.

## Detail for router rules that need more than one line
- **Parallel where it's safe.** Plan dependencies first, then fire
  independent work together (tool calls, background agents; a Workflow for
  big fan-outs, under 10 agents). Never let two workers edit the same file or
  shared convention: one integration step merges results and edits the shared
  files (the router, focus, decisions). Parallel drafts are drafts until that
  step checks they agree. Rate-limited services go one at a time. Helper
  agents get the router as it was at session start: if it changed since, tell
  them to re-read `AGENTS.md` from disk. Nate: don't overuse sub-agents, and
  agent teams are expensive (`system/standard-ai-os-v1.md` S16-S17).
- **Check in proportion to risk.** Always verify anything you tell Charlie is
  done (file exists, pushed) and every agent's quotes and links. Git steps in
  skills (branch, push, merge) are the preferred path, not proof: if a push or
  write is refused, say exactly where and never report it as done. Cheap
  structural checks run automatically (`tools/audit.py`, on push via GitHub
  Actions and via the Stop-hook run gate `tools/run_gate.sh`); reasoning
  checks (clash, bloat, stale facts) use the `os-audit` skill. Don't
  re-audit everything after small edits.
- **Suggest tools proactively.** At the start of any new task or project,
  check `research/plugin-map.md` (all 9 families, Charlie's watchlist) and
  name at most 2 plugins that would genuinely help, with one line why.
  Charlie isn't a coder, so families 2, 6, 7 and 8 matter most. Install only
  with his OK.
- **Small spends are fine when they save repeated workarounds.** Free first,
  but anything under about £5-10 is worth proposing if the knowledge gained
  is worth it (e.g. TwitterAPI.io: ~$0.15 per 1,000 posts). Always ask
  Charlie before any sign-up or payment; he does the sign-up, keys go in
  secrets (`.env` locally, environment secrets in the cloud).
- **95% confidence** (Nate, `jdbOVepEtUE` 5:32:54): "Do not make any changes
  until you have 95% confidence in what you need to build." Merged with
  Charlie's rule: aim for the outcome; ask only when the outcome is unclear.
