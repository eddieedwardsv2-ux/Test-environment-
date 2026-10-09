# Content check (part of the `audit` skill; was `os-audit` until 2026-10-08)

The failure-mode check and the backtrack after a miss. Run it after a wrong or
missed answer, after big structural changes, when Charlie asks "is anything
wrong, stale or clashing?", and after every switch to a new model (Rule 41). Start with
`python3 tools/context_check.py`: what loads into every message, its size,
and anything hidden (parent-folder or user-wide instructions, competing skills).

Based on Nate Herk, "Steal My Exact AI OS Setup"
(`research/nate-herk/steal-my-exact-ai-os-setup-5-simple-tips--Ek1NBfnnTH0-transcript.md`).
His audit is "read only, never fix or rename or delete. Just give a report"
([10:14](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=614s)), and ends with a
fix list that says "await approval"
([8:43](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=523s)).

**Two layers.** Layer 1 is `tools/audit.py`: deterministic and automatic (router
paths exist, local links resolve, transcript counts and ✅ marks match disk,
partial transcripts, environment freshness, queue syntax). Layer 2 is this
skill: judgement about whether the OS would make an agent **give a wrong answer**.

## Contract
- **Read-only.** Diagnose everything before fixing anything.
- Fixes need Charlie's OK, asked once on the Decision Desk (the `decide` skill),
  never as chat yes/no lists. Only exceptions: obvious typos and broken links.
- Every claim gets evidence (quote + `path:line`). Guesses are labelled **(inferring)**.
- Other agents may be mid-edit: run `git status --short` and mark findings on
  modified files as "may be stale".

## Step 0: read the last report
Open the newest dated report, `audits/YYYY-MM-DD.md` (if any). Nate's audit looks "for earlier
reports inside of the audit folder" first
([10:14](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=614s)): note which old
findings are fixed, still open, or came back.

## Step 1: run Layer 1 first
Run `python3 tools/audit.py`. Report its errors/warnings as they are. Do **not**
re-check what it already proves (path existence, link resolution, counts, queue
syntax). Spend your effort on meaning, not structure.

## Step 2: source precedence (use before calling anything a clash)
1. **Current state** wins: `AGENTS.md`, `context/*.md`, skill/agent files,
   brain `index.md` / `rules.md` / `concepts.md`.
2. **History** loses: `decisions.md`, brain `log.md`, dated notes.
An old log or decision entry is **not** a clash if something later or a
current-state file supersedes it. It **is** a clash when two current-state files
disagree, or when history says X and nothing current says otherwise but an
agent would still act on X.

## Step 3: the four failure modes
From Nate ([1:34](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=94s) to
[4:07](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=247s)):
- **Poisoning**: a false fact in context, used confidently ("a false fact that
  gets dropped in amongst these green facts",
  [2:05](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=125s)). Check facts an
  agent would repeat: counts, dates, links, "X is blocked/works", creator quotes.
- **Bloat**: too much loaded or routed ("needle in the haystack",
  [3:06](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=186s)). Check what loads
  every session (`CLAUDE.md` → `AGENTS.md`) and very long files agents must scan.
- **Confusion**: missing or irrelevant context, so the agent fills the gap
  ([3:36](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=216s)). Check for
  vague routes, routes to the wrong file, and questions with no route at all.
- **Clash**: two sources disagree or old data lingers ("in March your policy was
  always refund. In June ... never refund",
  [4:07](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=247s)). Apply Step 2.

## Step 4: the extra checks
- **Context placement**: expertise (needed every run: who Charlie is, rules)
  belongs in the router; situational (needed just in time) belongs in files the
  router points to ([5:38](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=338s)).
  Flag detail sitting in `AGENTS.md` that only one task needs.
- **Stale knowledge**: facts with a date or "currently" that may have moved on
  (tool limits, what's blocked, what's next).
- **Duplicate capabilities**: a new skill, agent or script that repeats an
  existing one (compare `.claude/skills/`, `.claude/agents/`, `tools/`, `research/*.py`).
- **Competing descriptions**: two skills or agents whose descriptions would
  answer the same request (Nate: "make sure two skills aren't competing for
  the same request", HIRDzMtuWFk 4:02).
- **Trigger test** for any skill added or changed since the last report: three
  requests, one obvious, one reworded, one unrelated that must NOT fire it
  (HIRDzMtuWFk 4:33). Say which skill each would load and why.
- **Reverse routing**: important files or capabilities that nothing routes to
  (Nate: "it will also look in the reverse direction",
  [11:15](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=675s)). List every
  skill, agent, script and top-level folder; is each reachable from `AGENTS.md`
  or a README it routes to?
- **Misleading indexes**: an index/README that describes files, statuses or
  next steps differently from what is on disk (beyond the counts Layer 1 checks).
- **Priority clash**: does `decisions.md` (latest entries) agree with
  `context/current-focus.md` about what Charlie is doing now?
- **Wrong-answer test**: for each finding ask "if Charlie asked X today, what
  wrong thing would an agent say or do?" No plausible wrong answer → low severity.

## Step 5: report
Save it as `audits/YYYY-MM-DD.md` (create `audits/` if missing; this
report file is the only write the audit makes) and show it in chat. Nate saves
every audit "so that you can see how you're actually improving"
([49:56](https://www.youtube.com/watch?v=bCljOfCH8Ms&t=2996s)). One block per finding:

| Field | What to write |
|---|---|
| Finding | one line |
| Category | poisoning / bloat / confusion / clash / placement / stale / duplicate / reverse-routing / index / priority |
| Evidence | short quote + `path:line` |
| Wrong behaviour | the wrong answer or action it could cause |
| Severity | high (likely wrong answer soon) / med / low |
| Smallest fix | one edit, one file if possible |

Then an ordered fix list (high first) and stop: put it on the Decision Desk as
one card, one option per fix, pick any (the `decide` skill). If a finding is **deterministic and keeps recurring** (a pattern a
regex or file check could catch), add: "Recommend adding to `tools/audit.py`."

## Backtrack: when an agent missed information that exists
Nate's tip 5: have it "go look through what you did, where you searched, and
... figure out why you didn't find that data right away", then fix the routing
([23:22](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=1402s)). Steps:
1. **Asked**: the exact question or task.
2. **Looked**: every file/tool the agent actually opened, in order.
3. **Route**: which line of `AGENTS.md` (or a README/skill) sent it there, or none.
4. **Why missed**: where the right info really lives, and why that route didn't lead to it.
5. **Defect type**: routing (no/wrong pointer), knowledge (info missing or
   wrong), capability (no skill/script for it), tooling (a tool failed), or
   audit (Layer 1/2 should have caught it).
6. **Smallest durable fix**: usually one router line or one index line. A
   one-line route fix is small and easy to undo: make it, say so, and record it
   in `decisions.md` with the date. Anything bigger goes on the Decision Desk.
   Before a lesson becomes a new rule or skill, score it (from ECC's
   learn-eval): reusable beyond this one case? Not already written somewhere?
   Still needed after a model switch? Any "no": fix the existing file instead.
7. **Retest**: rerun the original question (narrow test), then a related
   question that uses the same route (broader test). Prove both, don't claim.
