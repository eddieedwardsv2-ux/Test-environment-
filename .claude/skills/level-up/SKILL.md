---
name: level-up
description: Use when someone asks to level up their AIOS, close an audit gap, find what to automate next, or improve one workflow. Walks the 3Ms from choosing the constraint to shipping one useful artifact or verified repair.
---

> *Adapted from The Three Ms of AI™. © 2026 Nate Herk. All rights reserved.*

One interview = one artifact. Mindset phase always runs first. Background and checks: `reference.md`. Framework: `references/3ms-framework.md`.

## Inputs
Resolve paths via `AGENTS.md` (see the last block). Read priorities, about-me (top pain), `connections.md`, the decisions log, skill frontmatter and any recent `audits/` report. Ask only for what those lack.

## Coming from an audit
If an `/audit` finding is supplied or recent, carry its evidence, affected workflow and completion check into Phase 1 as the first candidate. Ask only for missing context. Use `/link` for routing-only fixes. Repair the existing workflow rather than duplicating it; a verified repair counts as the one artifact. Close with acceptance evidence and recommend `/audit` again; claim no higher score until it verifies.

## Phase 1: Mindset interview
Ask in order, conversationally:
1. What did you do 3+ times this week? (frequency)
2. Anything manual, boring or copy-paste? (drudgery)
3. Anything a smart intern could handle? (delegation)
4. If 500 new clients showed up tomorrow, what breaks first? (constraint)
5. What would give you 500 more? (growth lever)

Quote Mindset principles where they fit (Default Shift, Function Breakdown, "AI is better than you think"). Output: 1-3 candidates, one line each on why it is leverage. Ask which one to scope.

## Phase 2: Method interview
1. **Constraint.** Which bottleneck or growth lever does it serve?
2. **EAD.** Eliminate first: "what if we just stop?" If nothing breaks, exit cheerfully, log the win. Automate second (about 60% deterministic, 30% AI-assisted, 10% manual). Delegate third: if too variable or judgement-heavy, suggest a person, log it, exit.
3. **Map the process:** trigger, data sources, transformations, decision points, destination. If any is unclear, stop: "sketch it on paper first".
4. **Autonomy level.** L0 Manual, L1 Suggested, L2 Drafted, L3 Supervised, L4 Autonomous. Default to the lowest that solves it; push back on L4 unless lower levels have run first. Workflows beat agents.
5. **KPI.** Name a bucket (more customers, more value per customer, less cost) and a metric. If not, stop.

Output: a dated entry in the decisions log with all answers, level and KPI.

## Phase 3: Machine handoff
Ask how to ship; default to the highest non-AI option that works:
1. Prompt-only template. 2. Deterministic skill (script). 3. AI-assisted skill. 4. Sub-agent (last resort).

Scaffold with `skill-creator` or `skill-builder` if available, else write the file inline. Every scaffolded artifact starts with:

```markdown
---
bike-method-phase: 1  # Training wheels. Run manually first; advance only by explicit edit.
three-ms-attribution: |
  Adapted from The Three Ms of AI™ © 2026 Nate Herk.
---
```

Machine principles: Lego (smallest steps, zero-AI first), Validation Chain (test each step), Iteration (ship the proof of concept, expand from use).

### When the job was just done in this chat (from Anthropic's `build-agent`)
Turning a repeated job into a skill (Nate: build it the second time, Rule 44):
1. **The chat is the spec.** Don't re-interview; Charlie's corrections are the
   rules he'd never think to state ("skip anything under X" = a rule; "hmm,
   depends" = an approval step).
2. **Split each step:** fixed (order, sources, output shape), varies (dates, names,
   files), judgment (his call). Never hard-code the example.
3. **Gate only what matters:** anything that sends, spends, publishes or deletes,
   and the steps he hesitated over. Nine approvals is worse than doing it by hand.
4. **Write it in his words**, as numbered instructions to a future agent, with a
   fallback when a connection is missing and "missing data is reported, never
   invented".
5. **Test on a case with a known answer** (ideally the one just done), side by
   side. A near-miss is fixed and re-run, not accepted.
6. **Register** its trigger phrases in his words (`link`), then offer a schedule
   only after it has matched a known answer.
(Adapted from anthropics/knowledge-work-plugins `small-business/skills/build-agent`,
Apache 2.0; see `THIRD-PARTY-NOTICES.md`.)

## Output contract
1. One dated decisions-log entry with the Method spec.
2. One delivered artifact (prompt, skill or agent file) or verified repair.
3. A one-screen close: what was scoped, what was built, Bike Method Phase 1 reminder.

Edits: only the decisions log and the selected artifact.

## In Charlie's repo

Adapted from Nate Herk's AIS-OS kit (MIT, see `THIRD-PARTY-NOTICES.md`). Follow this repo's routes in `AGENTS.md` instead of the kit's default paths: priorities are in `context/current-focus.md`, decisions in `decisions.md`, about Charlie in `context/about-me.md`. The repo is public: no private, financial or other people's details.
