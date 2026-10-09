# ENATE triage: Nate's videos not yet transcribed

Started 2026-10-09. The cheap first pass for `brain-ingest` ("Triage first" in
its SKILL.md). Of 360 videos in `videos.md`, 69 are transcribed and in the
brain; **291 are not**. 126 of those are older n8n tutorials; most of the rest
are model tests and news, which date fast (left out on purpose, see
`brain/log.md` 2026-10-08).

## Tier 1 done (title, description and chapters only; no transcript read)
| Video | What the description says | Gap in ENATE | Tier |
|---|---|---|---|
| [YHk45NEpspE](https://www.youtube.com/watch?v=YHk45NEpspE) "Most Powerful Tool to Give to Claude Code" | Printing Press; chapter "CLI vs API vs MCP"; "MCPs eat your tokens", CLIs win for sites with no API | "MCP" is in concepts twice, in no rule; nothing on CLI vs MCP cost | **Queue now** |
| [lnm0PMi-4mE](https://www.youtube.com/watch?v=lnm0PMi-4mE) "Beginner's Guide to Metadata" | Tags each chunk with title, link and timestamp so answers say where they came from; metadata filtering; automatic deletion | "metadata": 0 hits. This is how routing and relations get built (it's what our timestamps and "Used by" lines do by hand) | **Queue now** |
| [Tj3018n5MVg](https://www.youtube.com/watch?v=Tj3018n5MVg) "Stanford's Method… Research Team" | STORM skill: 5 expert lenses, maps where they disagree, verifies sources; chapter "Subagents vs Agent Teams" | Multi-perspective research: not in ENATE (close to the parked "council" idea); agent teams only one quote | **Queue now** |
| [xJ5oz63mIec](https://www.youtube.com/watch?v=xJ5oz63mIec) "Deploy Your Claude Automations (3 Methods)" | /loop, scheduled tasks and routines, Modal / Trigger.dev; pick by where it runs and how agentic | "/loop": 0 hits; Rule 35 covers unattended runs but not how to choose a method | **Queue now** |
| [vcU85OrwuV0](https://www.youtube.com/watch?v=vcU85OrwuV0) "How Anthropic Engineers Actually Prompt Fable 5" | Six habits: context, matching effort, when it hands off to Opus | Partly in Rule 39 (match model and effort); model-specific | Spare time |
| [3QclAjmu5Tw](https://www.youtube.com/watch?v=3QclAjmu5Tw) "Claude Just Solved Session Limits" | Rate-limit news, "five things to do differently" | News; dates fast | Skip |

## Tier 1 still to do (YouTube said "too many requests"; retry later)
ZAaxx3qyT8g (Agent Dashboard), S2ME69hra-k (Why Watching AI Videos Isn't
Enough, 2:36, about how Charlie learns), hem5D1uvy-w (Google model + Claude
Code changed RAG), gQef3d3erOs and gb5TlGw6Uks (Hermes personal assistant).

## Older n8n videos worth one later look
Only for the idea, not the n8n steps: metadata and reranking (xWhX61651H8),
agent memory (kNsX2qu8jHY), multi-agent systems (0iUNOmeU7O4).
