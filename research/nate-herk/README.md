# Nate Herk | AI Automation — research notes

Coverage: **21 transcribed** (with timestamps) via `research/get_transcript.py`.
**Primary (the foundation curriculum):** "Steal My Exact AI OS Setup" and "I
Built Another Andrej Karpathy Using Claude". The rest are supporting evidence.
Brain: [index](brain/index.md). Lesson: [AI OS + second brain](lesson-ai-os-and-second-brain.md).

| Video | Date | Length | Views | Transcript |
|---|---|---|---|---|
| [Steal My Exact AI OS Setup (5 simple tips)](https://www.youtube.com/watch?v=Ek1NBfnnTH0) | 2026-07-23 | 25 min | 56.6k | ✅ [transcript](steal-my-exact-ai-os-setup-5-simple-tips--Ek1NBfnnTH0-transcript.md) |
| [I Built Another Andrej Karpathy Using Claude](https://www.youtube.com/watch?v=bvGptCLDhyo) | 2026-10-05 | 11 min | 58.8k | ✅ [transcript](i-built-another-andrej-karpathy-using-claude--bvGptCLDhyo-transcript.md) |
| [Every Level of a Claude Second Brain Explained](https://www.youtube.com/watch?v=DTCyvo6cC54) | 2026-06-17 | 31 min | 280.5k | ✅ [transcript](every-level-of-a-claude-second-brain-explained--DTCyvo6cC54-transcript.md) (analysed in the lesson) |

## Claims from the descriptions
Both videos: **all confirmed by transcript** (2026-10-07).
- **AI OS video:** CLAUDE.md should be a *routing file* (says where things
  are), not a giant system prompt. Four ways context fails: poisoning, bloat,
  confusion, clash. Separates "expertise" context from "situational" context.
  Demonstrates a free "OS audit" skill (in his free Skool group).
- **Second brain video:** five levels, from a simple CLAUDE.md router (level 1)
  to an always-on autonomous system (level 5). Advice: pick the *lowest* level
  that solves your problem.

## Chapters
- AI OS: [0:39 OS Audit Skill](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=39s) ·
  [1:38 4 Context Failure Modes](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=98s) ·
  [4:34 Expertise vs Situational](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=274s) ·
  [11:56 Tips 1–5](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=716s)
- Second brain: [3:25 Levels overview](https://www.youtube.com/watch?v=DTCyvo6cC54&t=205s) ·
  [4:19 Level 1](https://www.youtube.com/watch?v=DTCyvo6cC54&t=259s) ·
  [28:48 Finding your level](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1728s)

## Promotional content to discount
Sponsor (Hyperagent), affiliate links (Glaido, Hostinger), paid Skool tier and
agency playbook. The free Skool group holds his free resources.

## Key lessons — AI OS video (from transcript)
1. **Four ways context fails:** poisoning (a false fact), bloat (too much to
   search), confusion (irrelevant or missing facts, so it guesses), clash (two
   sources disagree, e.g. old vs new policy).
2. **Expertise vs situational context:** expertise = always needed (who you
   are, rules), lives in CLAUDE.md. Situational = looked up just in time
   (one customer, one job), never kept loaded.
3. **Five tips:** CLAUDE.md as a router (map of where things live) · have AI
   audit itself regularly · automate data that updates on a schedule · split
   knowledge into separate areas as it grows · when the AI misses something,
   make it *backtrack* and explain why, then fix the routing.
4. **Test:** can you find any file yourself without searching? If yes, an
   agent can too.

Not yet checked: his free "OS audit" skill (in his free Skool group).

## Key lessons — Karpathy brain video (bvGptCLDhyo, from transcript)
Four steps to turn an expert's public content into an agent: **crawl**
everything (one agent per source, in parallel), **compile** it into an LLM
wiki with an index and log, **distil rules** each backed by an exact quote
(unsourced = "inferring"), then an **agent + skills** (teach, ingest) and test
on real tasks. Applied here as Nick's brain: `research/nick-saraev/brain/`,
`.claude/agents/nick-brain.md`, `.claude/skills/brain-ingest/`.
Quote worth keeping (Karpathy, via Nate, 10:08): "you can outsource your
thinking, but you cannot outsource your understanding."
