# End-to-end test (2026-10-09, about 05:25 UK)

Charlie's Desk answer (next-big-step): prove the system works before building
on it. One real question, router → brain → answer, run in a session that
knows nothing about this one.

**Question:** `question.txt` (when to use a cheaper model and when to step up).
It is also research question 7-8 of ChatGPT's model-routing prompt
(`brainstorms/2026-10-09-model-routing-handoff.md`).
**Raw answer:** `claude-answer.md`.

## Result
| Part | Result | Receipt |
|---|---|---|
| Claude: fresh session reads the router | **Works.** `CLAUDE.md` imports `AGENTS.md`; it loaded with no tool call | answer, files list item 1 |
| Claude: router → right files | **Works.** 2 hops to the brain: `context/working-rules.md` and `system/standard-ai-os-v1.md` → `brain/index.md` → `concepts.md`, `rules.md` → transcript | answer, files list |
| Claude: brain → sourced answer | **Works.** Quote checked word for word: 7eo-11K2e3c line 20, [1:33](https://www.youtube.com/watch?v=7eo-11K2e3c&t=93s). Concepts 37, 40, 41 and rules 39, 41, 43 exist and match the topic; H13, S29, S11 are in `system/standard-ai-os-v1.md` lines 202, 212, 246 | grep in this session |
| Claude: says what it inferred | **Works.** 3 lines marked (inferring) | answer, part 5 |
| Claude: ends with **Now:** / **Done when:** | **Works.** | answer |
| Codex in this repo | **On paper only.** `codex` isn't installed here (`which codex`: nothing) and needs an OpenAI sign-in. Ready for it: `AGENTS.md` (Codex reads it), `.agents/skills -> ../.claude/skills` | `ls -la .agents` |
| ChatGPT side | **On paper only.** `exports/chatgpt-instructions.md`, last synced 2026-10-08, not re-tested | file date |

## What the test found (a real gap, not a failure)
- There is **no written rule for stepping up** to a stronger model. The repo
  says helpers run on Sonnet and the main session keeps the main model; Nate's
  brain says "objective definition of done → cheaper model; vague, needs a
  thought partner → stronger model" and "measure before you switch" (Rule 43).
  Nothing says "if the cheaper model fails, re-run on the stronger one". That
  belongs in the model-routing talk (part of "the middle"), not a quick edit.
- The fresh session skipped the session-start reads (current-focus, the Desk)
  because the question didn't need them. Correct for a one-off question.

## How to repeat it
`claude -p "$(cat question.txt)" --model sonnet --allowedTools "Read,Grep,Glob"`
from the repo root, then check the quote with `grep` in the transcript.
For Codex, on the Mac: `codex exec "$(cat question.txt)"` from the repo root
(after Codex is installed and signed in: Charlie's step).
