# Nate's brain: index

The knowledge base behind the `architect` advisor (`.claude/agents/architect.md`): a source-grounded guide to AI-OS architecture (routing, context, second-brain organisation, audits, ingestion, verification). Built from Nate Herk's public videos only. It summarises his methods with sources; it is not Nate.

**This page is the current state.** What changed and when is in [log.md](log.md).

| File | What's in it |
|---|---|
| [rules.md](rules.md) | **43 operating rules**, each with a confidence (stated / demonstrated / inference) and a check the agent asks. 1 is inference only (rule 3, clash: no video gives a fix). |
| [concepts.md](concepts.md) | **43 concepts** in nine groups: why an OS gives wrong answers, organising it, keeping it true, building an expert brain, turning knowledge into behaviour, human understanding, (G) the wider course and newer videos, (H) the full-channel audit, and (I) the newest videos. Each with exact quotes and timestamp links. Plus limits, videos that disagree (newer wins) and promotion to ignore. |
| [log.md](log.md) | History of what was added. |
| [../README.md](../README.md) | Nate's video list and which are transcribed. |

## Sources
**Primary (read in full, every concept rests on these):**
- [Steal My Exact AI OS Setup (5 simple tips)](../steal-my-exact-ai-os-setup-5-simple-tips--Ek1NBfnnTH0-transcript.md), Ek1NBfnnTH0, 25:02: failure modes, expertise vs situational, router, audit, freshness, segmentation, cadence, backtracking.
- [I Built Another Andrej Karpathy Using Claude](../i-built-another-andrej-karpathy-using-claude--bvGptCLDhyo-transcript.md), bvGptCLDhyo, 10:43: raw vs derived brain, index/log, provenance, relational ingestion, agent + skill, run gate, real-world testing, understanding.

**Newest (2026-10-08, 14 videos):** oz2CwrPV2Rg (concept 39), then 13 more: l8ywUsEJ2XQ (guest interview, Dave of Glido), pY5_Ux_YJjo, 7eo-11K2e3c, BvvfZKKz4Yo, eg_1NXDcoPk, 7jHXoPGnA4c, QCkHIyEPIYo, GmLcJVzkxPA, eF3yeJuifoQ, ymgH8jS6Wb8, QDsenEcAJIk, oWCcN6hSFjA, FqnNL8fnUWo. Model tests keep only the lasting method (concepts 40-41); new ideas are concepts 42-43.

**Supporting (all 18 other saved transcripts, ingested 2026-10-07; titles and codes in the code table of `system/standard-ai-os-v1.md`):** DTCyvo6cC54, 8QQ_INxAhRs, hQvwMj7IJe4, XNQBCRcwXV4, 3XIGcM7VICc, bCljOfCH8Ms (2h course), jdbOVepEtUE (6h Non-Coders course), yysILVsfLFM, 0WDkwMxj13s, 9KOtMsZ9I28, c0kaKxM2pHg, LrgfmZkl3nc, RzLV8sfFdMM (mostly guest Cole Medin), e18sdZLwP7o, zKBPwDpBfhs, kB9iMD0EjT8, HIRDzMtuWFk, 9hetShMMp2s (added nothing new). When videos disagree the newer one wins (upload order: `../videos.md`).

## Which transcript to load for which question
| Question about… | Load |
|---|---|
| wrong answers, context, routing, audits, freshness, folders, crons, clients, backtracking | Ek1NBfnnTH0 |
| building a creator brain, ingestion, provenance, agents/skills, hooks, testing | bvGptCLDhyo |
| levels of second-brain complexity, semantic search, when to move up a level | DTCyvo6cC54 (supporting); summary in `system/standard-ai-os-v1.md` |
| LLM-wiki set-up step by step | hQvwMj7IJe4 (supporting) |
| whether skills are too specific | XNQBCRcwXV4, then the newer 9KOtMsZ9I28 and HIRDzMtuWFk |
| router size, the 4 C's, onboarding, connections, routines, beginner habits | jdbOVepEtUE (6h) or bCljOfCH8Ms (2h); concepts 18-19, 24-27 |
| skills: anatomy, descriptions, trigger tests, verification | zKBPwDpBfhs, HIRDzMtuWFk, 9KOtMsZ9I28; concepts 21-22 |
| sub-agents | e18sdZLwP7o; concept 23 |
| using the same project in Codex | kB9iMD0EjT8; concept 28 |
| getting knowledge out of your head | c0kaKxM2pHg (grill me); concept 26 |
| memory, Auto Dream | LrgfmZkl3nc (unconfirmed feature) |
| trimming CLAUDE.md, skills and instructions; what to keep; auditing after a new model | oz2CwrPV2Rg; concept 39, Rule 41 |
| testing a new model, effort level or prompt; golden sets and AI judges | 7eo, GmL, QCk, ymg, l8y; concepts 40-41, Rule 43 |
| scheduled or triggered automations, agent loop or fixed code, who will use it | Fqn, l8y; concepts 42-43, Rule 42 |
| everything, as a checklist with status in this repo | `system/standard-ai-os-v1.md` |

## Coverage and gaps (2026-10-08)
- **In the brain:** all 69 saved transcripts (20 from 2026-10-07, 35 from the full-channel audit, 14 newest on 2026-10-08) (2 primary, the rest supporting). Every quote is checked automatically by `tools/audit.py`.
- **Full-channel audit (2026-10-08):** 35 more transcripts ingested into concepts 29-38 (section H) and Rules 31-40; the same teachings are rows R18, F15+, K15+, M13+, S20+, X6+, H9+ in `system/standard-ai-os-v1.md`. Brain now covers all 55 saved transcripts.
- **2026-10-08, newest:** oz2CwrPV2Rg (Anthropic Engineers Just 10x'd Everyone's Claude Code) → concept 39, Rule 41. Then the other 13 newest transcripts (Charlie chose all, on the Decision Desk) → concepts 40-43 and "Also" lines on 15, 16, 25, 31, 32, 33, 35, 37, 39; Rules 42-43; Rule 41 gained a second source. Who won which model test is deliberately not kept.
- **Not ingested:** Nate's X posts (`../x-posts.md`; no X themes page, not yet verified) and his untranscribed videos (mostly model news, n8n and single-tool demos).
- **Adding to the brain:** use the `brain-ingest` skill; it updates every page a source touches, then this index and the log.

**Overlap review (2026-10-09):** `overlap-review.md`: about 14 rules and 5 concepts repeat each other; merging is a Decision Desk card.
