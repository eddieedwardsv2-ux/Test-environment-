# Hand-off prompt from ChatGPT: intelligent model routing (saved 2026-10-09)

Charlie wrote this with ChatGPT on a walk. **Not started.** It overlaps his own
question from earlier the same day ("is the routing clear, and where is our
brains' middle?", `context/handoff.md`), which he wants to discuss before
anything changes. His spoken notes from the walk are still to come.

Notes for whoever runs it:
- The video (Nate Herk, "Grok Bot Just Got 2 Massive Upgrades", MgvwZaDPCs4) is
  not in `research/nate-herk/videos.md` yet (that list stops at 2026-10-08), so
  it has no transcript; it goes through the `brain-ingest` triage first.
- It asks for read-only research, audit and a plan only, then a stop for approval.

---

## The prompt (as Charlie pasted it)

**Claude Code Handoff — Intelligent Model Routing for Our AI OS**

**Starting point.** Repository: eddieedwardsv2-ux/Test-environment-. Start by reading AGENTS.md and follow its routing instructions. Then read context/current-focus.md, context/handoff.md, system/capability-map.md. Inspect relevant skills and architecture documentation as directed by the repository. Do not use Google Drive. GitHub is the working environment.

**Background.** We have been studying Nate Herk's video "Grok Bot Just Got 2 Massive Upgrades. Do These Things Now." (https://youtu.be/MgvwZaDPCs4). The video discusses automatic model routing. A screenshot at approximately 0:23 shows a post attributed to Elon Musk describing a system that selects different back-end models and APIs according to the task, including examples such as Claude Opus, Midjourney and Suno. We want to understand the underlying architecture, not purchase or reproduce Grok Bot. Our objective is to learn whether the same principles can improve our existing AI OS. Important: we have not verified the complete video transcript or its second advertised upgrade. Do not assume the entire video has been analysed. If accessible, retrieve the transcript, verify the actual claims and distinguish demonstrated functionality from speculation or marketing.

**Core thesis.** Build an AI OS that understands a user's request, identifies the required capabilities, retrieves relevant knowledge, and routes the work to the most suitable available model, skill or tool. The system should aim for the best verified balance of quality, reliability, speed, cost, context efficiency, and security and permissions. The objective is not to use as many models or agents as possible. It is to use the smallest effective combination of capabilities that reliably completes the task.

**Research questions.**
1. What does automatic model routing actually mean technically?
2. What principles can we adopt independently of Grok Bot?
3. How should a router distinguish between selecting a model, invoking a skill, using a tool and delegating to a subagent?
4. How can the router identify task complexity and required capabilities?
5. What information should the router retrieve from our second brain before execution?
6. When should tasks run sequentially versus in parallel?
7. When should an inexpensive or fast model be used?
8. Under what conditions should execution escalate to a stronger model?
9. How do we verify output quality rather than assuming a model succeeded?
10. How do we prevent extra routing logic from making the system slower, more expensive or less reliable?

Look for established engineering practices and available evidence. Do not treat the video as sufficient technical validation.

**Phase 1 — Audit our current foundations.** Perform a read-only audit of the existing GitHub system. Establish what is currently implemented versus what is merely documented or planned. Examine: the existing router and its decision rules; model and tool availability; skills, their triggers and overlapping responsibilities; subagent delegation and orchestration; context retrieval and second-brain structure; parallel execution rules and dependencies; permission boundaries; error handling, retries and fallback behaviour; existing tests, benchmarks and execution logs. Do not install dependencies, replace the router, create additional skills or reorganise existing knowledge during this phase. Document evidence using exact repository paths and relevant line references.

**Phase 2 — Gap analysis.** Compare the existing architecture against the proposed intelligent-routing principles. For each capability, classify it as: Working (implemented and supported by observable evidence); Partial (some implementation exists, but functionality or reliability is incomplete); Documented only (instructions or plans exist without demonstrated execution); Missing (no relevant implementation identified); Unverified (insufficient evidence to determine status). Identify duplicated responsibilities, unnecessary context loading, routing conflicts and features that may already be adequately handled by Claude Code, Codex or ChatGPT. Do not recommend rebuilding functionality that already works.

**Phase 3 — Proposed architecture.** Design the smallest practical improvement to our existing system. The proposed workflow should follow this general pattern: User request → Task classification → Capability selection → Relevant context retrieval → Execution → Validation → Escalation if necessary → Result and audit trail. Treat this as a hypothesis, not a mandatory architecture. If the existing router would work better with a different sequence, explain why. Distinguish clearly between: a router that chooses workflows; a skill containing instructions; a model performing inference; a tool performing an external operation; a subagent completing delegated work; a knowledge store supplying relevant context. Explain how these components interact without introducing unnecessary additional routing layers.

**Phase 4 — Testing strategy.** Design repeatable tests that establish whether the proposed architecture improves the existing one. Include representative tasks involving: 1) simple factual retrieval; 2) research across multiple sources; 3) GitHub code inspection; 4) complex reasoning and architecture review; 5) knowledge retrieval from our second brain; 6) a task requiring multiple specialised capabilities; 7) a task with missing information or a failed tool. Compare the current approach against proposed changes. Measure quality, accuracy, latency, cost where observable, context consumption, execution failures and human intervention. Do not invent cost estimates, performance results or test outcomes. Where measurements are unavailable, explicitly mark them as unmeasured. Define pass/fail criteria before recommending implementation.

**Phase 5 — Implementation roadmap.** Produce an incremental roadmap with: dependencies and correct implementation order; smallest useful first improvement; existing files that would need changes; any new files genuinely required; risks and potential regressions; verification and rollback procedures; estimated complexity; clear approval checkpoints. Prefer modifying or extending existing components over introducing new architecture. Parallelise independent research and analysis where this genuinely saves time. Keep dependent work sequential and avoid competing edits. Do not implement the roadmap yet.

**Deliverables.** A) Plain-English explanation of automatic model routing for a beginner, without unnecessary jargon. B) Current architecture map: how our router, tools, skills, subagents and knowledge system interact, verified implementation clearly separated from intended design. C) Gap analysis: what works, what is missing, what overlaps, what remains unverified. D) Proposed workflow: a clear pipeline showing how a request could move through capability selection and execution. E) Test plan: exactly how we would measure whether the changes are genuine improvements. F) Prioritised implementation plan: smallest, safest improvements first.

**Operating constraints.** GitHub is the source of project context. Follow AGENTS.md before investigating the architecture. Do not use Google Drive. Do not purchase or subscribe to Grok Bot. Do not assume access to models, APIs or capabilities that are not available. Do not introduce another competing router. Do not duplicate existing skills. Do not modify production behaviour. Do not make unapproved external changes. Do not claim a feature works merely because an instruction file describes it. Keep research findings separate from verified system behaviour. Preserve existing work and follow repository conventions. Maintain a clear distinction between facts, hypotheses and recommendations.

**Final instruction.** Before proposing improvements, answer: Does our current AI OS actually work as designed? How do we know? What specific limitation would intelligent model routing solve that our existing router does not already solve? Would introducing this capability improve the system measurably, or merely make the architecture more complicated? If our foundations are not demonstrably reliable, recommend fixing those first. Stop after the research, audit and proposed plan. Present the findings for approval before making implementation changes.
