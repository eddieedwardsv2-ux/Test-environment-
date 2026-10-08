# Nate's brain: log

**This is history.** It records what was added and when; it may be out of date about what the brain holds now. The current state is in [index.md](index.md). Newest first.

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
