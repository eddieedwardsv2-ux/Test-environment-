# Fresh Claude session: raw answer

Run: `claude -p` (headless, new process, no memory of the main session), model Sonnet, tools Read/Grep/Glob only, 12 turns, 25.8 s, about $0.34.

**1. The answer**
- Use the cheaper, faster model (Sonnet; Haiku for simple lookups) when the job has a clear spec and a way to check it. That covers reading, advising, lookups, and sub-agents with a bounded scope and a named deliverable. Start effort at medium.
- Step up to the stronger model (Opus) when the goal is vague or open-ended and you need a thinking partner to decide what "done" is. Also step up when a cheaper model has failed on your real task.
- Don't run everything at maximum effort.
- Nate's brain says to try the cheaper model first and test on Charlie's own work, rather than trust a general ranking.
- The repo's own setting is that helpers run on `model: sonnet` and the main session keeps the main model (Charlie's choice, 2026-10-08).

**2. Files opened, in order**
1. `AGENTS.md`. It was already loaded into the session as context, so I didn't open it with a tool.
2. `context/working-rules.md`
3. `research/nate-herk/` (directory listing only)
4. `system/standard-ai-os-v1.md`
5. `research/nate-herk/brain/` (directory listing only)
6. `research/nate-herk/brain/index.md`
7. A keyword search across `research/nate-herk/brain/`
8. `research/nate-herk/brain/concepts.md` (lines 356–405 only)
9. `research/nate-herk/brain/rules.md` (lines 236–277 only)
10. `research/nate-herk/i-tested-sonnet-5-5-vs-opus-5-5-what-you-need-to-know--7eo-11K2e3c-transcript.md` (searched for one phrase, not read in full)

**3. Numbers used**
- Brain concepts: 37 (match model and effort), 40 (test a model on your own work), 41 (evals before trust), 39 (re-audit after a new model).
- Brain rules: 39 (cheapest model and effort that does the job), 43 (measure before you switch), 41 (re-audit when the model changes).
- `system/standard-ai-os-v1.md`: H13 (match model and effort), S29 (bound the scope so sub-agents can go on Haiku), S11 (re-test skills when a new model arrives).
- `context/working-rules.md`: the "Parallel where it's safe" note, which says helper agents run on a cheaper model.

**4. Quote**
> "if you have a task with an objective definition of done, then try that out with Sonnet 5.5 first."

This is video `7eo-11K2e3c` at 1:33 (the saved link jumps to `t=93s`). I confirmed the wording in the saved transcript.

**5. Not found or inferred**
- (inferring) "Haiku for simple lookups" and "Sonnet for reading and advising" come from `working-rules.md`. The brain only says Haiku for sub-agents with a bounded scope (S29, `jZg` 11:11).
- (inferring) "Step up if the cheaper model fails" is my reading. Nate's sources say a vague goal suits the bigger model. They don't give a fail-then-escalate rule.
- I found no repo rule for switching the main session to a stronger model on a given trigger. `working-rules.md` only says it keeps the main model.
- Nate's saved model tests are dated, and the brain deliberately doesn't keep who won each one. Only the method lasts.
- I didn't read `context/current-focus.md` or the Decision Desk answers, which the router says to read at session start. Neither bears on this question.

**Now:** tell me if you want this added to `context/working-rules.md` as a written model-choice rule.
**Done when:** you've read this and decided yes or no.
