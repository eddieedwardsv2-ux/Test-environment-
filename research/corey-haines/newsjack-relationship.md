# Corey Haines Marketing Skills ↔ NewsJack — relationship study
Date: 2026-10-09
Status: research comparison, not an installed capability
Source type: public GitHub documentation + Charlie's 85-second screen recording (presenter captions, incomplete verbatim transcript)

## Sources and attribution
- Corey Haines (original): https://github.com/coreyhaines31/marketingskills — reusable marketing agent skills. The shared `product-marketing-context` establishes audience, product, positioning and differentiators before downstream skills.
- NewsJack (Elvis Sun and contributors, separate project): https://github.com/elvisun/newsjack — reusable PR/newsjacking skills for monitoring news, rating opportunities, checking newsworthiness, developing angles, journalist selection and draft pitches.
- Video evidence: user-supplied screen recording, 2026-10-09, approx. 85 seconds. Captions over presenters' faces represent spoken dialogue; onscreen slides/interfaces are separate evidence. No complete verified verbatim transcript has been filed in GitHub.
- Important: **NewsJack is not a Corey Haines skill and no authorship/collaboration is established.** This note links related skill architectures, not people.

## Connections / useful boundaries
| Layer | Corey Haines | NewsJack | Possible integration |
|---|---|---|---|
| Business context | `product-marketing-context`, positioning, customer and voice | Monitoring profile: company standing, beats, competitors, proof assets, spokespeople | Maintain one reviewed business context; transform relevant fields into a NewsJack monitoring profile instead of duplicating facts |
| Opportunity discovery | SEO, growth, customer research and channel selection | Time-sensitive stories and newsworthiness | Use NewsJack only when a PR opportunity fits the positioning and actual evidence |
| Production | Copywriting and landing-page conversion skills | PR angles, headlines, fact-checks and pitches | Produce channel-specific drafts; keep PR claims fact-checked and human-reviewed |
| Measurement | Conversion and marketing analytics | Coverage/PR monitoring | Track PR reach separately from leads, conversions and downstream business outcomes |
| Orchestration | Agent skills invoked for specific marketing tasks | Skills invoked for distinct PR tasks | Existing OS router selects *one* relevant workflow, loads only required context and checks outputs |

## Architecture insights for our AI OS
1. Both projects illustrate *skills as small, retrievable instructions* rather than stuffing every marketing procedure in AGENTS.md.
2. A shared business context can prevent contradictions. Do not auto-synchronise customer facts into multiple files without a clear owner, provenance and refresh policy.
3. NewsJack adds a time-sensitive detect → assess → verify → draft → approve sequence. Corey's skills add positioning, conversion and growth around it.
4. Route by intent: evergreen marketing/website improvement → Corey; news-led PR outreach → NewsJack; mixed campaign → use both serially, passing a concise checked brief.
5. Guardrails: avoid unsupported PR claims, misleading journalist targeting, unapproved outreach, duplicate skill installation and expensive models for trivial filtering. Claims about token savings or 384 headlines/$0.19 in the recording remain unverified until independently reproduced.
6. Evaluation proposal, not an implemented test: supply 10 news stories and a known product brief; measure relevance precision, factual errors, cost, time, human acceptance and any traceable conversions.

## Relation to repo
- Router: [AGENTS.md](../../AGENTS.md); [capability map](../../system/capability-map.md).
- Existing skills: [find-skills](../../.claude/skills/find-skills/SKILL.md), [brain-ingest](../../.claude/skills/brain-ingest/SKILL.md).
- Existing tools inventory: [Hands Brain](../hands/README.md); avoid adding duplicate installs or a second router.
- Original recording can be found in this conversation, not committed to the public repository (media could contain private material).

## Current decision
**Research only; no external skills installed and no outbound PR action authorised.** Assess each skill individually against existing capabilities before adoption.
