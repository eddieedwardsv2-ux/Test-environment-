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
| Does Charlie hit his Claude limits? | Yes: Charlie reported a Claude session stopped by usage limits on 2026-10-09 |
| Can he run it today? | No: it needs a computer running the server (Mac day) |
| Set-up | One sign-up and API key per provider; keys only in `.env` (Rule 26) |
| Privacy | Prompts and files go to free third-party providers, some of which may use them for training. Fine for public repo work, never for anyone's private notes |
| Quality | Model coverage claims conflict across the official docs; sustained quality equivalence is unverified. Switching requires a measured strongest-model comparison (Rule 43) |
| Best real use | A fallback when limits stop a session, or cheap bulk jobs (e.g. sorting a Hands week) measured against the strongest available baseline |

**Verdict:** not a "use now" tool. A **Mac-day trial** at most: one small
public task run both ways (explicit free model/provider vs strongest baseline), cost and quality
compared, with the `try-tool` skill.

## What changed in the ranking (fix for every tool, not just this one)
- Our own verdict now caps relevance: the newest sighting's need = yes 3,
  maybe 2, no 1 (`tools/build_hands.py`).
- "Use these now" skips anything Charlie marked later or drop, and puts
  need = yes first.
Result: FreeLLMAPI dropped from 2nd to 6th, HyperFrames (tried: later) left
the list, and Impeccable and Claude Code's agents.md support, both marked
need = yes, now lead it.

## Updated evidence and trial gate (2026-10-09)
Official README: https://github.com/tashfeenahmed/freellmapi . The software
is MIT; the free catalogue trails the live feed by 30 days. Paid catalogue
updates are optional. A free endpoint is not a guarantee of strongest-model
quality or sustained capacity. Its automatic fallbacks may reduce quality.

The linked architecture document contradicts the README's blanket model-class
claim: https://github.com/tashfeenahmed/freellmapi/blob/main/docs/en/architecture/00-high-level-index.md .
It describes limited frontier-class availability, queues and variable latency.
Do not repeat either catalogue claim as a measured result on our tasks.

**Current verdict:** the limit stop makes a trial relevant; it does not prove
this is the best replacement. Reuse `try-tool` with one explicit provider/model
on public inputs, no untested fallback chain or Fusion panel. Compare with
`system/model-usage.md`; inspect provider terms before sending data. No
installation, credentials, live output test or savings measurement occurred
in this review. Run locally only after the required environment exists.

Two existing alternatives checked: [Context Mode](https://github.com/mksglu/context-mode)
is context-management software, not free inference; its current licence is
source-available Elastic License 2.0. Its savings claims have not been tested
here. The [Claude startup programme](https://claude.com/programs/startups)
currently says its free Team/$1,000 credit offers are over capacity; it is not
an immediate guaranteed quota workaround. Prefer existing narrow reads and
short handoffs before adding another layer of hooks.
