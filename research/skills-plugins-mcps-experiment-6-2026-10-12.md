# Research Experiment 6 — Skills vs Plugins vs MCPs
Date: 2026-10-12
Scope: existing repository research, current connected tool capabilities and practical read-only checks. No architecture, permission, plugin-install or configuration changes.

## Core distinction
- Skill: reusable task instructions. It can be applied by a model or combined with tool calls; by itself it does not provide an external service.
- Plugin: packaged functionality, potentially including skills, actions, integrations or bundled setup. Its runtime and scope depend on the plugin host.
- MCP: protocol/interface that exposes tools and resources to an AI client; it supplies capabilities, not necessarily a task's end-to-end acceptance plan.
These categories overlap. An installed plugin may expose tools through MCP and ship skills. There is no fair universal winner across unlike tasks.

## Current-state evidence
- `AGENTS.md`: existing task-specific skills, connector and tool routes.
- `system/capability-map.md`: approved project plugins; already-available connectors and skills. Historical availability is not proof every host exposes them.
- `research/plugin-map.md`: functional groups, caveat that category sorting was approximate.
- `audits/2026-10-12-tool-policy-and-plugins.md`: earlier real testing of five approved plugins in another host. Installed watch-video media frames and Context7 documentation retrieval with separate limits.
- AI Impact `research/ai-impact/videos/8mL3D6ku8MQ.md`: knowledge and execution engine separation (creator suggestion, not comparative benchmark).
- Nate `research/nate-herk/lesson-smallest-context.md`: load procedure when its job appears; do not put every procedure in root prompt.
- The Next New Thing `research/the-next-new-thing/free-on-github-manage-agents-11labs-alternative-incredible--CQhWqUOouYM-transcript.md`: task coordination and broad external integrations (marketing claims unverified).

## Predetermined acceptance criteria
1. Retrieve five task-selected authoritative repo records, expected anchor in each (5/5).
2. Demonstrate live instruction-skill access and live external tool execution without credentials in a public report.
3. Record tool limitations; do not imply independent equal-task skill/plugin/MCP comparison was executed.
4. Identify the correct mechanism for each of five representative needs without inventing capabilities. No new installations, architecture or routing changes.

## Practical execution
A. **5/5 targeted repository reads succeeded** using connected GitHub tool:
1. Current priority: `context/current-focus.md`, text `Active task — TRADEFLOW quote demo`.
2. Skill procedure: `.claude/skills/session-handoff/SKILL.md`, `Carry-forward check`.
3. Existing approved capabilities: `system/capability-map.md`, `Approved plugin capabilities`.
4. AI Impact record: `research/ai-impact/videos/8mL3D6ku8MQ.md`, `Separate execution engine`.
5. Verification instruction: `AGENTS.md`, `Prove what you report`.
These five targeted tests are not blind search or complete task executions; file paths and expected phrases were supplied.

B. **Instruction skill read succeeded**: installed `skills://plugins/data-analytics/validate-data/skill.md`, obtained validation workflow; GitHub repository's `session-handoff` skill read. Reading and interpreting instructions does not prove that a whole handoff ran.
C. **Live plugin-backed documentation capability succeeded**: Context7 resolved Python as `/python/cpython`; queried Path.exists and Path.read_text, retrieved source references to CPython pathlib docs. Not a cost, speed or quality benchmark versus web or native file tools.
D. The connected GitHub MCP tool performed real external reads in five cases. The GitHub connector also writes this report; verify the resulting commit receipt. No third-party account/private business data was changed.

## Which approach matches five representative jobs (reasoned classification)
| Job | Preferred mechanism | Reason |
|---|---|---|
| Repeatable handoff and carry-forward check | Skill + GitHub write tool | Instructions define completeness; tool persists output |
| Read current project truth from GitHub | MCP tool | Requires live repository access |
| Current third-party library API guidance | Context7 plugin/tool | Retrieves live scoped documentation |
| Validate an analysis | Validation skill + evidence/data tools | Skill supplies checks; tools inspect claims and artifacts |
| Transcribe/check media | Media plugin/skill + executable media tool | Needs execution, not prompt text alone |

## Disagreements and cautions
- 'MCP vs plugin' is frequently a false choice: a plugin may expose MCP-powered actions.
- A giant always-on skill is inappropriate for narrow research (Nate), while typed, source-backed knowledge (AI Impact) belongs in relevant records rather than every prompt. These are complementary.
- Plugin installation receipts from a prior Claude host do not prove availability or equal quality in this ChatGPT host.
- The five GitHub retrievals are simple and successful, but comparison across the three modalities with the **same input, quality score, total cost, latency, privileges and failures** was not performed.

## Next valid head-to-head protocol
Select three to five tasks implementable by all candidate routes, e.g. public markdown classification, evidence-backed QA, or a transformation from the same fixed sample. For each, hold input and checklist constant and compare: standalone instruction-only skill; plugin-provided workflow; MCP-backed tool workflow. Run fresh isolated sessions, record exact model, retrieved bytes/tokens, latency, outputs, failures, retries and full cost. One withheld missing-file case and one prompt-injection fixture per route; require 100% critical checks, no unauthorised actions, no invented references. Some tasks require mixing approaches: record 'not applicable' rather than count as failure.

## Verdict
**VERIFIED:** GitHub targeted 5/5; installed data-validation skill readable; Context7 live Python docs query; GitHub external tools operational.
**NOT VERIFIED:** standalone 5×3 equal-input performance contest, real quality/cost superiority of any category, host-wide Claude plugin availability, production workflows, aggregate billed token savings.
No AI-OS redesign or installation.
