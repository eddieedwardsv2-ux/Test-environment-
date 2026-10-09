# Nate's brain: log

**This is history.** It records what was added and when; it may be out of date about what the brain holds now. The current state is in [index.md](index.md). Newest first.

## 2026-10-09: six-phrases Instagram DM (1 source, not a video)
**Ingested:** "The 6 Phrases That Make Claude Build 10x Faster", an Instagram auto-DM Charlie pasted, saved verbatim as `../six-phrases-instagram-source.md` (attributed to Nate; date sent unknown).
**Pages changed:** `concepts.md` new section J and concept 44; `rules.md` Rule 44 (stated); `index.md` counts (44 concepts, 44 rules), sources and question table.
**Promoted:** none. It is a second source for concepts 22, 23, 26, 31 and 42 (they were already stated). New: the VERIFIED / NOT VERIFIED report shape, "what the check would NOT catch", "the three decisions you'd disagree with" in a spec, and automations that write to one place.
**Applied to the OS:** `context/working-rules.md` READY / NOT READY now ends with VERIFIED / NOT VERIFIED lines (the DM's own checklist asks for this in CLAUDE.md; ours lives in working-rules, which the router points to).
**Left out:** the "comment PHRASES" promotion. "Do not write code until I say go" isn't adopted as written: it would make Charlie a checkpoint on small work; real choices go on the Desk.
**Checked:** every quote found word for word in the source file (script, 12/12); `tools/audit.py`.

## 2026-10-09: clashes fixed (Charlie's choice: no merge)
**Pages changed:** `rules.md` Rule 19 marked replaced by Rule 41 (a "Newer wins" line; quotes kept); `concepts.md` concept 18 marked replaced by concept 39, concept 3's length pointer moved to 39; `overlap-review.md` records the choice. Nothing else merged.

## 2026-10-08: +13 newest transcripts (all of them, Charlie's choice)
**Ingested:** l8ywUsEJ2XQ (guest Dave of Glido, 1h09), pY5_Ux_YJjo, 7eo-11K2e3c, BvvfZKKz4Yo, eg_1NXDcoPk, 7jHXoPGnA4c, QCkHIyEPIYo, GmLcJVzkxPA, eF3yeJuifoQ, ymgH8jS6Wb8, QDsenEcAJIk, oWCcN6hSFjA, FqnNL8fnUWo, each read in full. Brain now covers all 69 saved transcripts.
**Pages changed:** `concepts.md` +4 concepts (40 test a model on your own work, 41 evals and AI judges, 42 fixed flows in code vs agent loop, 43 stakes ladder), "Also" lines on concepts 15, 16, 25, 31, 32, 33, 35, 37, 39, a planning clash and a model-results note under limits, concept 20's "Used by"; `rules.md` +2 rules (42, 43) and "Also" lines on Rules 17, 26, 33, 35, 37, 39, 41; `index.md` counts (43 concepts, 43 rules), sources, question table, coverage; `../README.md` coverage line.
**Rules promoted:** none changed label (no rule carries a provisional label). Rule 41 gained a second, independent source (l8y) and is noted as no longer resting on one video. New: Rule 42 (lowest rung; Fqn, with l8y and DTC) and Rule 43 (measure before you switch; 7eo, GmL, ymg, QDs).
**Left out on purpose:** who won each model test (Sonnet 5.5 vs Opus 5.5, Opus vs GPT-6 Astra/Sol, effort levels, Dots vs Muse, Jev, Higgsfield, Ultrafast prices and the 7-day discount), the trading-challenge results, and sponsor, Skool and event plugs. Planning: l8y says go straight to building, Nate (Fqn) still does a short planning chat, iTY wants the plan attacked; recorded under "Videos that disagree" (newer wins).
**Checked:** every new quote was matched to its transcript chunk by script before saving; `tools/audit.py` run.

## 2026-10-08: +35 transcripts (full-channel audit; now all 55 saved)
**Ingested:** the 35 videos read for `audits/2026-10-08-nate-channel.md` (codes in the standard's code table).
**Pages changed:** `concepts.md` +10 concepts (29-38, section H) and "Also" lines on concepts 16 and 19; `rules.md` +10 rules (31-40, all "stated"); `index.md`.
**Rules promoted:** none. Plan mode recorded as declined by Charlie (concept 30, Rule 32).
**Checked:** every concept's "Used by" matches the rules' concept numbers; `tools/audit.py` 0 errors (all linked quotes pass); 3 quotes spot-read in the transcripts.

## 2026-10-08: concepts linked to rules ("fully connected", level 2)
**Why:** Charlie wants each brain to be a connected map, as in DTCyvo6cC54. Nate's level 2 is pages linked "like backlinks" (12:41), not a knowledge graph.
**Pages changed:** `concepts.md`: every concept ends with a "Used by" line listing the rules that cite it (built from the concept numbers in `rules.md`; concepts 19, 20, 28 have no rule yet and point to related concepts instead); concept 20 gained the level 2 vs level 4 point with a checked quote.
**Checked:** `tools/audit.py` 0 errors; the new quote passes and a planted fake one fails.

## 2026-10-07: +14 transcripts (now all 20 saved)
**Ingested:** 3XIGcM7VICc, bCljOfCH8Ms, jdbOVepEtUE, yysILVsfLFM, 0WDkwMxj13s, 9KOtMsZ9I28, c0kaKxM2pHg, LrgfmZkl3nc, RzLV8sfFdMM, e18sdZLwP7o, zKBPwDpBfhs, kB9iMD0EjT8, HIRDzMtuWFk, 9hetShMMp2s (nothing new). Built from the quote-checked requirements in `system/standard-ai-os-v1.md`.
**Pages changed:** `concepts.md` +11 concepts (18-28, section G), "Also" lines on concepts 2, 3, 6, 7, 9, 11, 14, 15, 16, 17, and a "videos that disagree" block; `rules.md` +12 rules (19-30), "Also" lines on rules 2, 4, 5, 7, 11, 15, 16, 17, and a newer-wins note on rule 15; `index.md`.
**Rules promoted:** none changed label; rule 3 (clash) stays inference, because none of the 14 gives a fix.
**Checked:** every cited quote is in its transcript chunk (`tools/check_quotes.py`, now run by `tools/audit.py` on every push); concept numbers in rules match concept titles.

## 2026-10-07: foundation build (2 primary videos)
**Ingested (primary, read in full):** Ek1NBfnnTH0 (Steal My Exact AI OS Setup), bvGptCLDhyo (I Built Another Andrej Karpathy Using Claude).
**Supporting, cited for single points only:** DTCyvo6cC54, 8QQ_INxAhRs, hQvwMj7IJe4, XNQBCRcwXV4.

**Created:**
- `concepts.md`: 17 concepts (failure modes, expertise vs situational, router, findability, segmentation, cadence, audit, freshness, backtracking, raw vs derived, brain pages, provenance, relational ingestion, agents and skills, run gates, real-world testing, human understanding).
- `rules.md`: 18 rules, each labelled stated, demonstrated or inference.
- `index.md`, and the `nate-brain` agent (`.claude/agents/nate-brain.md`).

**Checked:** every quote found in its transcript (case and spacing ignored); every timestamp within the video's length and matching a transcript line; every relative link resolves; `tools/audit.py` run.

**Reused from earlier drafts, after checking:** structure and several quotes from an interrupted Claude draft (branch `claude/nate-brain-wip`) and a ChatGPT draft.
**Left out:** the earlier draft's equal weighting of 7 transcripts (scope is now 2 primary), its X-themes page (not verified), its rules resting mainly on supporting videos or X posts, and ChatGPT draft claims that were unsourced or pointed to files that weren't part of this build.

## 2026-10-08: newest video (1 source)
**Ingested:** oz2CwrPV2Rg, "Anthropic Engineers Just 10x'd Everyone's Claude Code" (12:23), read in full; checked against the Anthropic article it is based on (`../anthropic-context-engineering-claude-5-source.md`).
**Changed:** `concepts.md` new section I and concept 39 (smallest context that works); concept 14's skills note now says the newest video confirms "keep skills short". `rules.md` Rule 41 (stated). `index.md` counts (39 concepts, 41 rules), question table and coverage.
**Promoted:** none (Rule 41 is new and stated). Supports Rule 18's audit cadence.
**Left out:** the Hyper Agent sponsor slot (3:04–4:05) and the community plug (9:08–9:39). The 2025 paper's percentages: he says himself they don't predict what trimming your own file will do.
**Saved, not ingested (at the time):** 13 other newest transcripts (model tests and demos); Charlie decided to ingest all of them later the same day (see the entry above).
