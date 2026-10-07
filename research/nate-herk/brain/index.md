# Nate's brain: index

The knowledge base behind the `nate-brain` advisor (`.claude/agents/nate-brain.md`): a source-grounded guide to AI-OS architecture (routing, context, second-brain organisation, audits, ingestion, verification). Built from Nate Herk's public videos only. It summarises his methods with sources; it is not Nate.

**This page is the current state.** What changed and when is in [log.md](log.md).

| File | What's in it |
|---|---|
| [rules.md](rules.md) | **18 operating rules**, each with a confidence (stated / demonstrated / inference) and a check the agent asks. 1 is inference only (rule 3, clash). |
| [concepts.md](concepts.md) | **17 concepts** in six groups: why an OS gives wrong answers, organising it, keeping it true, building an expert brain, turning knowledge into behaviour, human understanding. Each with exact quotes and timestamp links. Plus limits and promotion to ignore. |
| [log.md](log.md) | History of what was added. |
| [../README.md](../README.md) | Nate's video list and which are transcribed. |

## Sources
**Primary (read in full, every concept rests on these):**
- [Steal My Exact AI OS Setup (5 simple tips)](../steal-my-exact-ai-os-setup-5-simple-tips--Ek1NBfnnTH0-transcript.md), Ek1NBfnnTH0, 25:02: failure modes, expertise vs situational, router, audit, freshness, segmentation, cadence, backtracking.
- [I Built Another Andrej Karpathy Using Claude](../i-built-another-andrej-karpathy-using-claude--bvGptCLDhyo-transcript.md), bvGptCLDhyo, 10:43: raw vs derived brain, index/log, provenance, relational ingestion, agent + skill, run gate, real-world testing, understanding.

**Supporting (cited only to back up or challenge a point):** DTCyvo6cC54 (Every Level of a Claude Second Brain), 8QQ_INxAhRs (Ultimate Second Brain), hQvwMj7IJe4 (Karpathy's LLM Wiki), XNQBCRcwXV4 (I Deleted All My Claude Skills). Transcripts in `research/nate-herk/`.

## Which transcript to load for which question
| Question about… | Load |
|---|---|
| wrong answers, context, routing, audits, freshness, folders, crons, clients, backtracking | Ek1NBfnnTH0 |
| building a creator brain, ingestion, provenance, agents/skills, hooks, testing | bvGptCLDhyo |
| levels of second-brain complexity, semantic search, when to move up a level | DTCyvo6cC54 (supporting); summary in `system/standard-ai-os-v1.md` |
| LLM-wiki set-up step by step | hQvwMj7IJe4 (supporting) |
| whether skills are too specific | XNQBCRcwXV4 (supporting) |

## Coverage and gaps (2026-10-07)
- **In the brain:** 2 primary videos; 4 supporting videos cited for single points.
- **Read but not ingested yet (2026-10-07):** all 14 saved transcripts were read for `system/standard-ai-os-v1.md`, which lists 66 verified requirements with quotes. The other 8 transcripts (9KOtMsZ9I28, 0WDkwMxj13s, 3XIGcM7VICc, bCljOfCH8Ms, yysILVsfLFM, c0kaKxM2pHg, LrgfmZkl3nc, 9hetShMMp2s) and the X posts are not yet in concepts.md or rules.md: use the `brain-ingest` skill. No X themes page: not yet verified.
- **Adding to the brain:** use the `brain-ingest` skill; it updates every page a source touches, then this index and the log.
