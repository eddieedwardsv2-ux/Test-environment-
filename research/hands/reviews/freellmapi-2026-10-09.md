# FreeLLMAPI: is it really a top priority? (2026-10-09)

Charlie saw it second on "Use these now" and asked for a review.

## What it is (from its README, github.com/tashfeenahmed/freellmapi, MIT)
A small server you run yourself (Mac or Windows app, or Docker) that stacks
the free tiers of 34 AI providers (Google, Groq, Mistral, OpenRouter, …)
behind one address. Point Claude Code or Codex at it and they run on those
free models, switching to the next one when a limit is hit. Optional $19 a
year for a faster-updating model list.

## Why it ranked high
The helper that read the videos scored it 3/3 for Charlie ("keep coding when
you hit a limit"), it came up in two weeks, it's free, and it's recent. But our
own note on both sightings said **need: maybe**, and the ranking ignored that.

## Our view
| Question | Answer |
|---|---|
| Does Charlie hit his Claude limits? | Not known: no limit stop recorded so far |
| Can he run it today? | No: it needs a computer running the server (Mac day) |
| Set-up | One sign-up and API key per provider; keys only in `.env` (Rule 26) |
| Privacy | Prompts and files go to free third-party providers, some of which may use them for training. Fine for public repo work, never for anyone's private notes |
| Quality | No Claude models; our skills, audits and helpers are tuned for Claude. Switching models needs a measured test first (Rule 43) |
| Best real use | A fallback when limits stop a session, or cheap bulk jobs (e.g. sorting a Hands week) measured against the Sonnet helper |

**Verdict:** not a "use now" tool. A **Mac-day trial** at most: one small
public task run both ways (free models vs Sonnet), cost and quality
compared, with the `try-tool` skill.

## What changed in the ranking (fix for every tool, not just this one)
- Our own verdict now caps relevance: the newest sighting's need = yes 3,
  maybe 2, no 1 (`tools/build_hands.py`).
- "Use these now" skips anything Charlie marked later or drop, and puts
  need = yes first.
Result: FreeLLMAPI dropped from 2nd to 6th, HyperFrames (tried: later) left
the list, and Impeccable and Claude Code's agents.md support, both marked
need = yes, now lead it.
