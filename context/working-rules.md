# Working rules: Karpathy's 7 (via Nate Herk)

How every agent in this repo works and teaches. Source: Nate Herk, "I Built
Another Andrej Karpathy Using Claude", rules at
[5:34–6:34](https://www.youtube.com/watch?v=bvGptCLDhyo&t=334s); transcript in
`research/nate-herk/bvGptCLDhyo-transcript.md`. Nate's own summary:
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
| 6 | **Say what you assumed** | State assumptions before acting on them (e.g. "I'm reading 'X-ray' as Saraev"). If a request is thin, ask one or two questions instead of guessing. |
| 7 | **Simpler wins** | Prefer the simplest thing that works; cut what isn't earning its place. |

Anything not backed by a source is labelled **(inferring)**.

## How they're enforced
- **Run gate (rule 5):** a Stop hook in `.claude/settings.json` runs
  `tools/audit.py` when an agent tries to finish; if the audit finds errors,
  the turn is sent back to fix them.
- **Teaching (rules 1-4):** `context/how-i-learn.md`, the `video-tutor` agent
  and the `teach` skill (`.claude/skills/teach/`), which checks its own answer
  against all 7 rules before showing it. It never grades Charlie.
