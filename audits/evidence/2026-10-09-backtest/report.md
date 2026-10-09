# Backtest of 2026-10-08 build (run 2026-10-09)

Method: read-only checks; descriptions read with `grep -H "^description:" .claude/skills/*/SKILL.md .claude/agents/*.md`.

## 1. Trigger tests (judged from descriptions, not a live model run)
| Request | Would fire | Competes? | Result |
|---|---|---|---|
| "I need Charlie to pick a base kit" (obvious) | `decide` ("need Charlie to choose") | no | PASS |
| "should I ask him which plugin?" (reworded) | `decide` (plugin install is on its ask list) | weak: `hands-brain` ("which tool/plugin") and `find-skills` | PASS, mild overlap |
| "what's the best free voice tool?" | `hands-brain` ("best tool for X") | no (`find-skills` is skills only) | PASS |
| "update the tools list for this week" | `hands-ingest` only by "this week"; no "Hands Brain" words, and `hands-brain` ("try this week") also pulls | yes | FAIL (ambiguous) |
| "write a lesson on Nate's video" (unrelated to Hands) | `video-tutor` / `teach` / `nate-brain`; none of `decide`, `hands-ingest`, `hands-brain` | video-tutor vs teach compete, not the Hands trio | PASS for the trio |
| "what's the weather" (unrelated) | none | no | PASS |

## 2. Acting as hands-brain (tools.json only; links built as youtube.com/watch?v=<video>&t=<t>)
- Q1 "best free tool to make short clips?" -> **OpenShorts**, Video, clips & images rank 1, open-source, score 15, last seen 2026-W41. Runner-up InvokeAI (rank 2) is an image tool, so a weak runner-up. Shown at 19:30, video GZtLsvklYBI; quote "This is a free clip maker that you can host yourself or you can go to their website and use for free." Check flag: free hosted tier is 20 min/month with watermark. Matches data. PASS.
- Q2 "anything newer than ElevenLabs?" -> ElevenLabs rank 5, status replaced, replaced_by **VoiceStudio** (rank 1, W41, free, 0:27 in GZtLsvklYBI; also W40 5:35 CQhWqUOouYM). Matches data. PASS on data. Caveat: ElevenLabs is recorded as a voice-agent platform (W39), VoiceStudio as a clone/TTS app, so "replaced" is loose; and VoiceStudio's default model is non-commercial (check flag). Answer must say so.
- Q3 "which skills pack should I start with?" -> **ECC**, Claude Code skills & plugins rank 1, open-source, score 17, W41 (0:33, BcNAQynKUk4) and W39 (17:26, hlOk-EFUITQ). Runner-up Claude Code Templates (rank 2, score 16). Check flag: 271k stars and exit claims are the guest's. Matches data. PASS.

## 3. Data checks
- tools.json entries: 64. Category not in CATEGORIES: 0. PASS.
- Score recomputed (3*for_charlie + 2*mentions + max(0,3-week age) + price bonus free/open-source 1, freemium 0.5), matches the SKILL.md/README formula and build_hands.py: 0 mismatches of 64. PASS. (README says "recency, price" without numbers; the exact weights are only in the code.)
- Quotes: 74 quotes across weeks/*.json checked against each transcript, whitespace-normalised exact match: 73 match, 1 differs (Pexo, c5ZkPhzaLdA: "It's an AI video agent that turns your ideas into videos."; the transcript has "AI video agent" but my strict match failed, likely punctuation/line wrap). `python3 tools/check_quotes.py` says "148 checked, 0 failed". Random 3 (Claude Code Templates CQhWqUOouYM, OpenManus GZtLsvklYBI, Skillry c5ZkPhzaLdA) all verbatim. PASS (minor: Pexo to eyeball).
- Sponsors (Zapier, Monid) in names/urls: 0. PASS.

## 4. Scripts
- `python3 tools/audit.py` -> "audit: 0 errors, 0 warnings". PASS.
- `python3 tools/context_check.py` -> "Always loaded: about 8,405 characters (~2,101 tokens). No warnings." PASS.

## 5. Router
- Every backticked path in AGENTS.md (except the `projects/<name>/` pattern): all exist, 0 missing. PASS.
- system/pages.md: 6 links; all 6 source files exist. Artifact IDs seen elsewhere (decide skill, handoff, how-i-learn, mac-day, flashcards, setup-kit README, brain-map, merge-map) all match one of the six in pages.md; no stray IDs. PASS (cannot check the live pages are published; no network check done).

## 6. Fresh-session check (AGENTS.md alone)
- (a) Ask Charlie: yes. AGENTS.md rules + `decide` skill; opened `AGENTS.md`, `.claude/skills/decide/SKILL.md` (Decision Desk link and card format). PASS.
- (b) Hands Brain location and add a week: AGENTS.md table row and `hands-ingest` bullet point to `research/hands/`; opened `.claude/skills/hands-ingest/SKILL.md` (steps 1-5, schema) and `research/hands/README.md`. PASS.
- (c) Week 38 pause: AGENTS.md says read `context/current-focus.md` first; opened it, lines 20-24 give W38 paused, 3 missing transcript IDs (ehab5PtgRo8, pkwnJcETgfE, ANJTdT0Ggrw). PASS. Weakness: AGENTS.md never names current-focus as holding the Hands pause; it is a one-hop find.

## Summary
| Test | Result | Fix needed (smallest) |
|---|---|---|
| 1 Trigger: decide x3 | pass | none |
| 1 Trigger: "update the tools list for this week" | FAIL (ambiguous with hands-brain) | add "update the tools list" to hands-ingest description |
| 1 Trigger: hands-brain "best free voice tool" | pass | none |
| 2 Answers vs data (3 questions) | pass | tell hands-brain to flag loose `replaced_by` (ElevenLabs vs VoiceStudio) |
| 3 Categories / score / sponsors | pass | none |
| 3 Quotes | pass (1 strict-match miss, Pexo; check_quotes 0 failed) | eyeball Pexo quote |
| 4 audit.py / context_check.py | pass | none |
| 5 Router paths / pages links | pass | none |
| 6 Fresh-session a, b, c | pass | none |
