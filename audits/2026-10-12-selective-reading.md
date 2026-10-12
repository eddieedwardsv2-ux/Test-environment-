# Selective reading and usage investigation

12 October 2026. User asked whether agents must read entire folders of rules/concepts, whether routes are optimal, and what repeated usage is largest.

## Findings

1. A concrete instruction defect existed in `.claude/agents/architect.md`: it required index.md, then the whole rules.md, then concepts.md. The prohibition against reading a whole creator folder did not prevent loading both large brain pages.
2. rules.md + concepts.md contain 105,131 characters, roughly 26,282 tokens using characters/4. This is a rough size estimate, not actual tokenizer output or billed usage.
3. The new official-docs index is 191,457 characters (~47,864 by the same estimate). Its JSON source catalogue is about 1.48 million characters. Those are lookup/catalogue artifacts, not appropriate default model inputs.
4. The root instruction file is modest in line count but optimality is not proved. The repo's context checker estimated ~3.4K always-loaded tokens before these final reading additions, for repo-owned Claude instructions/descriptions only. It does not measure this ChatGPT host’s total system instructions, memory, tools, history or billing.
5. The route-depth tool found 158 current notes: 145 within two hops, 13 at three hops. This is its scoped note set, not proof of correct retrieval across all documentation or every new source.

## Repairs

- Architect now starts at a compact task-to-rule/concept map and reads selected complete sections. It expands for missing evidence, dependencies or contradictions.
- Existing full rules/concepts files remain intact; no architecture rewrite or mass split was needed.
- Official-docs has a small topics.md map and bounded SQLite/source-record queries. The large link index is explicitly for human browsing.
- AI Impact has an explicit selective-record reading route rather than loading all 342 records.
- Root instructions distinguish machine scanning from model context, reuse unchanged session material and require task-specific reads.
- Helpers should receive a focused task, relevant file paths and acceptance criteria; full parent conversation is unnecessary when those suffice.

## Independent trial

A reviewer started with a task-only context and tested:

| Question | Selected rules | Selected rule/concept characters |
|---|---|---:|
| What belongs in the root router? | 5, 41 | 7,504 |
| Where are permissions/secrets enforced? | 25, 26, 36, 37 | 7,815 |
| Fixed code versus an agent loop? | 42 | 5,548 |

All three answers were grounded in selected rule/concept sections and relevant transcript snippets. All 44 rule IDs and 45 concept IDs exist uniquely. The official-docs shortlist SQL executed and returned eight records. The reviewer suggested adding Concept45 to the helper-context route; that was added.

The selected rule/concept payload across all three trials was 20,867 characters, compared with 105,131 characters for one copy of the full rule/concept pair. Including map, source-index route and transcript evidence, the combined trial input was 33,834 characters. These are source-size comparisons; they are not total session input, billed tokens or a measured monetary saving. No universal runtime-compliance claim is made.

## Repeated usage visible in this session

This is a qualitative investigation from observed actions, not a complete account usage ledger.

- Broad background reads for narrow questions: the full Nate lesson and full rules file were returned during the comparison, when selected sections would suffice.
- The first three caption workers inherited the full parent conversation. Their actual source reading was partitioned, but their shared background was duplicated. Later reviewers used focused contexts.
- Large registry/metadata output was returned during discovery, including unrelated tool descriptions. Discovery can return names and only the selected schema instead.
- Some sources/indexes were fetched again, and the docs database was rebuilt several times to correct extraction defects. Downloading/processing bytes locally is distinct from sending those words to a model.
- Broad audit/graph rebuild output repeated established failures. Required checks must still run; summaries should emphasise changed findings and preserve complete diagnostics locally.

No billed-token counts across Claude, Codex or prior conversations were available. Therefore the report cannot rank actual account spend, claim a percentage reduction in bills or prove historical usage totals.

## Remaining verification

- Test fresh Claude Code and Codex sessions on more topics and conflicting-version evidence.
- Record read paths/sections and expand reasons for real tasks. Instructions alone are not enforcement.
- Improve semantic concept relationships only when evidence supports them; shared-topic backlinks are not supports/contradicts relationships.
- Official-docs retains catalogue/extracted facts, not a durable full source-text mirror; its corpus-wide semantic ingestion is unfinished.

NOT VERIFIED for universal reading compliance or optimal total usage.
