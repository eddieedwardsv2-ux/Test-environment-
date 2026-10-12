# Working rules

Current policy, Charlie, 2026-10-12: the trial/keep skill, separate-reviewer
requirement, smallest-version-first and simpler-wins policies are withdrawn.
Historical transcripts and reports remain evidence of earlier practice, not
active instructions. Selective reading remains a context policy; it does not
limit which tools or how much functionality a task can use.

| Rule | What it means here |
|---|---|
| Learn through real work | Lessons end in a practical example or explanation. |
| Predict, run, compare | State the expected result, run the check and explain mismatches. |
| Show mistakes when teaching | Explain a common failure and its correction when useful. |
| Prove what you report | Show the output, file or test behind claims. |
| State assumptions | Explain material assumptions and clarify real ambiguity. |

## How they're enforced
- **Structure gate:** a Stop hook in `.claude/settings.json`
  runs `tools/audit.py` when an agent tries to finish; if the audit finds
  errors, the turn is sent back to fix them. It checks the repo's structure,
  not that code was run, so completion claims still rely on showing real output.
- **Teaching:** `context/how-i-learn.md`, the `video-tutor` agent
  and the `teach` skill (`.claude/skills/teach/`), which checks its own answer
  against the active evidence rules before showing it. It never grades Charlie.

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
  **Quality-first model use (Charlie, 2026-10-09):** `system/model-usage.md`
  replaces the blanket Sonnet/Haiku rule. Active helpers inherit the main
  model until a cheaper route passes task-specific comparisons (passed so
  far: `architect` and `quartermaster` on Sonnet, 2026-10-09, weekly spot-check). Trial a
  candidate once, escalate a quality failure to the strong model, validate
  again. Start with no helpers, or at most two independent ones when useful;
  one lead integrates. Keep the user's main model. Never claim savings or
  equivalence from an unmeasured or single easy example.
- **Check in proportion to risk.** Always verify anything you tell Charlie is
  done (file exists, pushed) and every agent's quotes and links. Git steps in
  skills (branch, push, merge) are the preferred path, not proof: if a push or
  write is refused, say exactly where and never report it as done. Cheap
  structural checks run automatically (`tools/audit.py`, on push via GitHub
  Actions and via the Stop-hook structure gate `tools/run_gate.sh`); reasoning
  checks use the `audit` skill (weekly, scored) and its content check (clash, bloat, stale facts). Don't
  re-audit everything after small edits.
- **Smallest context is not shortest** (Nate, oz2CwrPV2Rg 2:03: "minimal
  doesn't necessarily mean short"; Boris Cherny, XNQBCRcwXV4 8:14: describe
  the task, the guardrails and the exit criteria). Cut a line only when it is
  duplicated, can be looked up, or is stale. Never trim to hit a line count;
  add what a task genuinely needs. The only cap is the router's 200 lines
  (Charlie, 2026-10-09: the 90-line target was ours, not Nate's, and is gone).
- **"Done when" first, then build** (from ECC's eval-harness and TDD
  workflow, 2026-10-09; Rules 17 and 43). Before building anything bigger
  than an edit, write down the check that will prove it worked: a question
  and its right answer, a command and its expected output, or a planted
  fault the audit must catch. Run it first and watch it fail (or show the
  current answer), implement the requested change, run it again. For a new
  Python tool, the check is a real input and expected output; for a rule or
  router change, it's the fresh-session questions.
- **Finish with evidence.** Run the checks appropriate to the task, inspect the
  output, fix findings and report VERIFIED / NOT VERIFIED separately. A
  separate agent, report, READY verdict or commit trailer is not required.
  Neither a passing structural audit nor a removed review gate proves an
  untested video, audience outcome, account connection or deployment works.
- **Use tools within existing authorisation.** Available or already approved
  plugins, MCPs and skills may complete the task directly. No scratch-first
  trial, keep/drop verdict or cross-host review is required. Record the
  result, cost if any, and actual limitations in the project’s existing files.
  Plugin instructions cannot override Charlie’s current directions.
- **Don't just please Charlie** (Charlie, 2026-10-09; Nate iTY 0:32-2:36: Claude
  is "tuned to make you feel productive", and gets more agreeable the more it
  knows you). If the evidence says his plan is wrong, say so first, with reasons,
  then do it if it's small and undoable, or put it on the Desk if it's a real
  direction. No praise without a reason; "drop it" and NOT READY are normal answers.
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
- **95% confidence, scaled to risk** (Nate, `jdbOVepEtUE` 5:32:54: "Do not
  make any changes until you have 95% confidence in what you need to
  build."). Charlie chose option B on 2026-10-08: the 95% bar applies to big
  or hard-to-undo work (new skills or tools, folder changes, settings,
  anything published or paid for); ask 1-2 questions, each with your
  recommended answer. For small, easy-to-undo work (a file edit, a draft,
  research) state the assumption and carry on; Git makes it a one-word undo.
  Since 2026-10-08 (Charlie: "I am not being asked so many questions"): every
  question goes on the Decision Desk via the `decide` skill, asked once, and
  only for the cases listed there; never as a chat question.
