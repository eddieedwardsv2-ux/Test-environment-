# Standard AI-OS v1: Nate's requirements and how this repo meets them

What a basic, working AI OS needs according to Nate Herk, with no personal
content. The blank copy is `templates/standard-ai-os-v1/`; this repo is that
standard plus Charlie's personal details. Decision: `decisions.md`, 2026-10-07.

**Sources.** The four core videos are Ek1, DTC, 3XI and bvG. (Charlie named
three links; bvG is assumed to be the fourth because the brain was already
built from it.) Supporting: the other 16 saved Nate transcripts (all 20 read; 9hetShMMp2s,
Claude Code mods, added nothing new). Rows 2026-10-07b come from the 6 added
last: jdb (6h course), RzL, e18, zKB, kB9, HIR.
When videos disagree, the newer one wins (upload order is in `research/nate-herk/videos.md`).

| Code | Video (transcript) |
|---|---|
| Ek1 | [Steal My Exact AI OS Setup](../research/nate-herk/steal-my-exact-ai-os-setup-5-simple-tips--Ek1NBfnnTH0-transcript.md) |
| DTC | [Every Level of a Claude Second Brain](../research/nate-herk/every-level-of-a-claude-second-brain-explained--DTCyvo6cC54-transcript.md) |
| 3XI | [Learn These 6 AI Skills](../research/nate-herk/learn-these-6-ai-skills-now-before-everyone-else-does--3XIGcM7VICc-transcript.md) |
| bvG | [I Built Another Andrej Karpathy](../research/nate-herk/i-built-another-andrej-karpathy-using-claude--bvGptCLDhyo-transcript.md) |
| bCl | [Build & Sell Claude Code OSs (2h course)](../research/nate-herk/build-sell-claude-code-operating-systems-2-hour-course--bCljOfCH8Ms-transcript.md) |
| c0k | [The Skill That 10x'd My Projects (grill me)](../research/nate-herk/the-skill-that-10x-d-my-claude-code-projects--c0kaKxM2pHg-transcript.md) |
| Lrg | [Claude Code Memory 2.0](../research/nate-herk/claude-code-just-dropped-memory-2-0--LrgfmZkl3nc-transcript.md) |
| yys | [GPT-6 Astra Ultimate Second Brain](../research/nate-herk/i-turned-gpt-6-astra-into-the-ultimate-ai-second-brain--yysILVsfLFM-transcript.md) |
| hQv | [Karpathy's LLM Wiki](../research/nate-herk/fable-5-karpathy-s-llm-wiki-is-basically-cheating--hQvwMj7IJe4-transcript.md) |
| 8QQ | [Ultimate Second Brain](../research/nate-herk/i-turned-claude-into-the-ultimate-second-brain--8QQ_INxAhRs-transcript.md) |
| 0WD | [Opus 4.8 Entire AI OS](../research/nate-herk/i-turned-claude-opus-4-8-into-my-entire-ai-operating-system--0WDkwMxj13s-transcript.md) |
| 9KO | [Codex Skills](../research/nate-herk/how-to-build-codex-skills-better-than-99-of-people--9KOtMsZ9I28-transcript.md) |
| XNQ | [I Deleted All My Claude Skills](../research/nate-herk/i-deleted-all-my-claude-skills-and-claude-got-smarter--XNQBCRcwXV4-transcript.md) |
| jdb | [Claude Code for Non-Coders (6h course)](../research/nate-herk/claude-code-for-non-coders-6-hour-course--jdbOVepEtUE-transcript.md) |
| RzL | [Claude Code Better Than 98% (mostly guest Cole Medin)](../research/nate-herk/how-to-use-claude-code-better-than-98-of-people--RzLV8sfFdMM-transcript.md) |
| e18 | [Claude Subagents Better Than 99%](../research/nate-herk/how-to-build-claude-subagents-better-than-99-of-people--e18sdZLwP7o-transcript.md) |
| kB9 | [Claude Code Projects in Codex](../research/nate-herk/how-to-use-your-claude-code-projects-in-codex-in-5-mins--kB9iMD0EjT8-transcript.md) |
| HIR | [What to Build Instead of AI Agents](../research/nate-herk/anthropic-engineer-explains-what-to-build-instead-of-ai--HIRDzMtuWFk-transcript.md) |

**Status:** ✅ met · 🔧 fixed 2026-10-07 · ⏳ open · ➖ deliberately not now (reason given).
Quotes are verbatim auto-captions, so mishearings such as "cloudmd" and
"claw.md" are left as spoken.

## The filing cabinet (what this repo looks like)
```
AGENTS.md / CLAUDE.md   router (CLAUDE.md imports AGENTS.md)
context/                always-true background: about-me, current-focus (priorities),
                        environment (stack), how-i-learn, working-rules
decisions.md            dated decision log
projects/<name>/        deliverables
research/<creator>/     level 2: raw transcripts + brain/ (index, log, concepts, rules)
system/                 how the OS is built, capability map, this standard
tools/                  deterministic checks (audit.py, run gate, coverage)
.claude/                skills, agents, settings (Stop-hook run gate)
templates/              the blank Standard AI-OS v1
brainstorms/ audits/    created by grill-me and os-audit when first used
```

## 1. Router
| # | Requirement | Nate's words | Src | Here |
|---|---|---|---|---|
| R1 | The root file is a router: it points rather than stores | "I treat this almost purely as a router" | Ek1 12:46 | ✅ `AGENTS.md` |
| R2 | A short role line, then a "where things live" table | "But here is where you actually go to find data." | Ek1 13:17 | ✅ |
| R3 | One route per topic. Without a route the AI won't look there | "you probably just didn't give Claude the knowledge to go look there" | DTC 4:34 | ✅ `tools/audit.py` checks every route exists |
| R4 | Keep it lean | "if it grows too big, it can start to get messy and feel ignored" | DTC 5:04 | ✅ 67 lines; R13 gives the limit. The template is about 45 |
| R5 | One router for every tool (import rather than copy) | "you can literally just reference inside of your claude.md at agents.md" | DTC 22:49 | ✅ `CLAUDE.md` = `@AGENTS.md` |
| R6 | Tool-agnostic: just files and folders | "you're building things to be tool agnostic" | bCl 2:04 | ✅ plus `exports/chatgpt-instructions.md` |
| R7 | Routes to decisions, projects and the knowledge base | "Here's where decisions live. Here's templates. Here's references. Here's projects." | Ek1 13:47 | ✅ |
| R8 | Lists skills and when to use them; a new skill gets registered and logged | "It's going to register the skill in claw.md and it's going to log its decisions." | bCl 1:30:08 | ✅ audit errors if a skill isn't routed |
| R9 | Update the router whenever you add folders or files | "you're going to just want to make sure that your claused file is getting updated as well" | bCl 28:34 | ✅ capability-map rule plus audit |
| R10 | Read the wiki only when needed | "I said don't read from the wiki unless you actually need it." | bCl 2:20:23 | ✅ smallest-context rule |
| R11 | Shape: one identity line, a few core rules, then mostly a routing map | "I go into a routing map and that's the majority of my agents.mmd" | yys 6:07 | 🔧 rules cut to one line each (router 94 → 67 lines); details in `context/working-rules.md` |
| R12 | Each wiki has its own routing rules inside it | "inside the wiki, what happens is there are routing rules set up" | hQv 12:40 | ✅ each `brain/index.md` says which transcript to load |
| R13 | Router under 200 lines: it is re-read with every message | "So keep it under 200 lines." | jdb 5:36:27 | 🔧 `tools/audit.py` errors above 200 (now 94) |
| R14 | Don't build until 95% sure what's wanted; ask follow-ups first | "Do not make any changes until you have 95% confidence in what you need to build." | jdb 5:32:54 | 🔧 merged into the "Aim for the outcome" rule; also in the template |
| R15 | The router keeps decisions, not conversations | "Save decisions, not conversations." | jdb 5:44:05 | ✅ `decisions.md` |
| R16 | Turn repeated failures into a one-line lesson | "When something fails repeatedly, when Nate has to reexplain, or when a workaround is found for a platform tool or limitation, add a oneline bullet here." | jdb 5:44:36 | ✅ done as a fix to the right file (backtrack rule) rather than a lessons list |
| R17 | Router edits only apply in a new session | "the edit actually doesn't apply until you restart that session." | jdb 5:55:15 | ✅ helper agents told to re-read `AGENTS.md` from disk |

## 2. Filing cabinet
| # | Requirement | Nate's words | Src | Here |
|---|---|---|---|---|
| F1 | Start at level 1: router plus folders | "level one is pretty simple and this is where you always start." | DTC 4:04 | ✅ |
| F2 | `context/` holds always-true background, starting with about-me | "In the context folder, always true background about you and how you work, read this first." | DTC 5:34 | ✅ |
| F3 | A priorities file, refreshed each planning cycle | "I think the best way to be doing this would be at the start of every quarter." | bCl 35:09 | ✅ `context/current-focus.md` |
| F4 | Decision log with dates | "have your Claude at MD always append new decisions and dates whenever you make a big change" | DTC 6:04 | ✅ `decisions.md` |
| F5 | `projects/`, one per project; usually the biggest folder | "I've got a folder called projects, which is the largest one." | Ek1 14:48 | ✅ |
| F6 | `.claude/` holds skills, agents and settings | "I've got my cloud with all of my pretty much global skills and global sub aents and my settings" | Ek1 14:17 | ✅ |
| F7 | `brainstorms/` for interview output | "I've got my brainstorms folder, which is anytime I run a grill me session, it saves it here." | Ek1 14:17 | 🔧 `grill-me` skill |
| F8 | `audits/` for audit reports | "It will also create this folder at the root of your project if you don't have one." | Ek1 1:04 | 🔧 `os-audit` saves there |
| F9 | `archives/` for old documents | "we've got an archives folder, which is where Claude will put old documents or things that you don't need" | bCl 27:02 | ➖ nothing to archive yet; history stays in logs |
| F10 | Back up the whole folder to GitHub | "push this main folder to GitHub and everything backs up" | Ek1 12:46 | ✅ (public repo, so nothing private: an `AGENTS.md` rule) |
| F11 | No layout is proven; routing is what matters | "there is not yet a standard way that has been proven the best way" | DTC 6:34 | ✅ we follow his example |
| F12 | Browse test: can you find a thing without searching? | "see if you could find it without searching, without asking Claude" | Ek1 18:20 | ✅ fresh-session routing test (below) |
| F13 | Codex reads `AGENTS.md`, `.codex/` for config, `.agents/` for skills | "you'd have your agents at MD with the dot codex folder for your config and your agents. And then you'd have a separate folder for your skills called dot agents" | kB9 3:04 | 🔧 `.agents/skills` links to `.claude/skills` (one copy, both tools) |
| F14 | Shared skills and agents live in the repo, not the global folder | "If you want to share them with your team, keep them in your projects, keep them in your repo." | e18 24:57 | ✅ cloud sessions wipe the global folder anyway |

## 3. Knowledge base (level 2)
| # | Requirement | Nate's words | Src | Here |
|---|---|---|---|---|
| K1 | Move to level 2 at about 30+ notes | "If you have 30 plus notes and you keep forgetting what's in them, look at level two." | DTC 28:53 | ✅ `research/` |
| K2 | Raw sources, one folder per source, never edited | "The raw files don't get touched" | bvG 4:04 | ✅ transcripts plus `-raw.txt` |
| K3 | Compile the raw dump into a wiki with an index and a log | "keeps an index, keeps a log" | bvG 4:04 | ✅ `brain/index.md`, `log.md` |
| K4 | Ingest updates every page a source touches | "it will update every page that post touches" | bvG 9:38 | ✅ `brain-ingest` |
| K5 | Every rule has an exact quote; unsourced means inference | "every rule has to connect with an exact quote from him and where it came from" | bvG 5:34 | ✅ `rules.md` confidence labels |
| K6 | Split distinct knowledge into separate wikis | "the more you can segment stuff out, the better." | Ek1 20:21 | ✅ one brain per creator |
| K7 | Expertise (always) vs situational (just in time) | "situational context is things that you need just in time" | Ek1 5:38 | ✅ `system/architecture.md` |
| K8 | Only lasting knowledge, chosen by the human | "in a year, will it be good for me to have this memory in here?" | DTC 27:23 | 🔧 `brain-ingest` step 1 |
| K9 | Getting knowledge out of your head is the bottleneck: interview | "the bigger problem is getting everything out of your brain into the system" | DTC 22:18 | 🔧 `grill-me` |
| K10 | Markdown wiki is enough until hundreds of pages | "if you have hundreds of pages with good indexes, you're fine with wiki graph" | bCl 2:23:27 | ✅ no vector DB |
| K11 | Memory is an index, not a dump | "it's an index, not a dump" | Lrg 5:34 | ✅ repo is the memory; brain `index.md` |
| K12 | After each ingest, check there are new index and log entries | "We should see a new record in the index as well as a new record in the log" | hQv 10:38 | ✅ `brain-ingest` steps 4–5 |
| K13 | The router holds rules; memory holds learned facts | "cloudmd is the rules. Memory is, you know, learned facts." | jdb 2:04:50 | ✅ facts in `context/` and brains, not the router |
| K14 | Save a working set-up so it's never researched again | "save the endpoint so you understand like we've done this before. I don't want you to research it every time" | jdb 1:07:47 | ✅ `context/environment.md`, `tools/` |

## 4. Maintenance
| # | Requirement | Nate's words | Src | Here |
|---|---|---|---|---|
| M1 | The audit is read-only and waits for approval | "Read only, never fix, or rename" | Ek1 9:43 | ✅ `os-audit` |
| M2 | Audits are saved, and earlier reports are read first | "look for earlier reports inside of the audit folder" | Ek1 10:14 | 🔧 `audits/YYYY-MM-DD.md` |
| M3 | Check routes, the reverse direction, indexes and freshness (and every quote here: `tools/check_quotes.py`, inside the audit) | "Do the indexes match the disk." | Ek1 11:15 | ✅ `tools/audit.py` plus `os-audit` |
| M4 | Audit every week | "Maybe every single Friday, you run an audit" | bCl 2:28:30 | 🔧 weekly in `os-audit`; `audit.py` also runs on every push |
| M5 | Diagnose with the four failure modes | "poisoning, bloat, confusion, and clash" | Ek1 1:34 | ✅ `system/architecture.md` |
| M6 | Crons keep recurring data fresh | "set up some sort of crons to pull in the data that you want to always be living inside of your local project" | Ek1 19:51 | ✅ hourly transcript workflow |
| M7 | Backtrack after a miss, then fix the route | "Have it update the routing." | Ek1 23:22 | ✅ `AGENTS.md` rule, `os-audit` backtrack |
| M8 | Feed every correction back into the system | "every time you correct AI, you feed that correction back into the system" | 3XI 6:37 | ✅ backtrack rule |
| M9 | Test in a fresh session: teammate or stranger? | "does this answer like a teammate" | bCl 12:44; 0WD 7:09 | ✅ routing test below |
| M10 | Check skill and agent front matter is valid (an unclosed quote stops it firing) | "You have to close off the quotes if you open them up" | jdb 2:37:42; e18 16:21 | 🔧 `tools/audit.py` checks name, description and closing `---` |
| M11 | Trigger-test a skill: obvious, reworded and unrelated requests | "The first one is an obvious request that should trigger it." | HIR 4:33 | 🔧 `os-audit` step for new or changed skills |
| M12 | Fix a failure in the smallest lasting place | "update the skill in the smallest durable place" | HIR 6:05 | ✅ `os-audit` backtrack step 6 |

## 5. Skills, agents, tools
| # | Requirement | Nate's words | Src | Here |
|---|---|---|---|---|
| S1 | Package expertise as a subagent plus a skill | "it has Claude turn them into two files for us" | bvG 6:34 | ✅ `nate-brain` + `brain-ingest` |
| S2 | A hook stops "done" until it has been run | "It adds a hook, which is a little script that runs right when the agent tries to finish its turn." | bvG 7:35 | ✅ `tools/run_gate.sh` |
| S3 | One agent per source, in parallel | "I told it to run one agent per source, so they all go at once" | bvG 3:03 | ✅ parallel rule |
| S4 | SKILL.md: front matter, under 500 lines | "keep the skill.md under 500 lines" | bCl 1:21:28 | ✅ largest is 144 |
| S5 | A repeated process becomes a skill; skills can be tiny | "They could literally just be a 50line markdown file." | bCl 1:25:34 | ✅ `system/capability-map.md` |
| S6 | Check third-party skills before installing | "make sure that no one's trying to, you know, give you a skill that has any malicious intent" | bCl 1:18:55 | ✅ `find-skills` plus Charlie's OK |
| S7 | Simplest tool; deterministic over agents | "deterministic workflows, beat AI agents nine times out of 10" | bCl 2:29:00 | ✅ `tools/` scripts |
| S8 | Sub-agents for context-heavy searches | "so that you don't blow your own context window" | bCl 1:23:32 | ✅ parallel rule |
| S9 | Every skill has a verification step | "every single skill that I build works in some sort of verification loop" | 9KO 9:40 | ✅ each skill ends with a check |
| S10 | Hand off before clearing: what was done, files, open decisions, next step | "here's what we did. Here's the files that were created. Here are open decisions. Here's what's next." | 0WD 22:24 | 🔧 router: update `current-focus.md` Next step before a session ends |
| S12 | Check visual output by screenshotting it and looking | "we built a plan to add visual validation" | bCl 1:03:37 | 🔧 `tools/screenshot.py` (phone + desktop, script errors); flashcards app passed 2026-10-07 |
| S13 | Define acceptance criteria and check against real evidence | "Before returning the final output, define the acceptance criteria." | HIR 8:05 | ✅ **Done when:**, run gate, quote checker |
| S14 | Descriptions use the words a person would say; no two skills compete | "Put the words a real person would use inside the description and make sure two skills aren't competing for the same request." | HIR 4:02 | 🔧 `os-audit` checks for overlapping descriptions |
| S15 | New skills report only; earn autonomy after many runs | "Once we've ran the skill 10, 20, 30 times and we've kind of like battle tested it and we feel more confident in it, then we can maybe make it a little bit more autonomous." | jdb 1:47:37 | ✅ `os-audit` read-only; `grill-me` asks before changing files |
| S16 | Use a sub-agent when the output is a pile you'd never re-read | "is this about to dump a pile of stuff into my chat that I'll never read again?" | jdb 2:43:47 | ✅ smallest-context and parallel rules |
| S17 | Don't overuse sub-agents (not for quick or dependent steps) | "if you're forcing too many sub agents, you're going to get worse results" | e18 24:57 | ✅ parallel rule: plan dependencies first |
| S18 | Sub-agents are made read-only by their tools, not by a prompt | "you can put that so that these sub-agents are explicitly read-only" | e18 7:10 | ✅ `nate-brain`, `nick-brain`: Read, Glob, Grep only |
| S19 | Keep scripts that worked in files, not in the chat | "don't leave that code trapped inside the chat" | HIR 2:02 | ✅ `tools/`, `research/*.py` |
| S11 | Re-test skills when a new model arrives | "run you this model through your skills. Make sure they all still work." | XNQ 1:34 | ➖ do it at the next model change |

## 6. Secrets and connections
| # | Requirement | Nate's words | Src | Here |
|---|---|---|---|---|
| X1 | Secrets in `.env`, excluded from Git, never pasted in chat | "gets excluded from anytime we do a public push" | bCl 41:50 | 🔧 `.gitignore`; `AGENTS.md` secrets row |
| X2 | The AI gets its own account and least-privilege keys; prompts aren't permissions | "A prompt is never a permission layer." | 8QQ 24:31; bCl 38:44 | ➖ no connections yet; apply when connecting |
| X3 | API plus a reference .md rather than many MCPs | "having a bunch of MCP servers loaded into your project actually eats more tokens" | bCl 39:45 | ➖ apply when connecting |
| X4 | Block risky actions in settings (a deny list), not by asking nicely | "Can you help me update the settings file so that you physically cannot do those things?" | jdb 1:14:28 | 🔧 `.claude/settings.json` denies force-push, hard reset, git clean and `rm -rf` (tested: blocked) |
| X5 | Keys in `.env` beat app connectors, which are lost when you switch tools | "If you rely on these connections, that is not great" | jdb 1:37:24 | ✅ Git and scripts, not connectors, do the repo's work |

## 7. Working habits
| # | Requirement | Nate's words | Src | Here |
|---|---|---|---|---|
| H1 | Define done before starting | "You have to define what done looks like before you even start building." | 3XI 12:40 | ✅ **Done when:** |
| H2 | Build the ugly version fast | "Just build the ugly version fast." | 3XI 12:09 | ✅ Karpathy rule 2 |
| H3 | Ask why; run it before saying it works | "Never accept AI output without asking why" | bCl 6:37 | ✅ Karpathy rule 5 |
| H4 | Keep your own understanding | "you can outsource your thinking, but you cannot outsource your understanding" | bvG 10:08 | ✅ `teach` skill, flashcards |
| H5 | Get your own OS working before a team's | "You can't scale a system if you haven't lived in it yourself." | bCl 2:31:32 | ✅ |
| H6 | `/clear` between unrelated tasks | "Use slashclear between unrelated tasks." | jdb 5:30:53 | ✅ one task per session; hand-off rule |
| H7 | Hand off to a new session at about 250-300k tokens | "if we get past 250,000 300,000, I'm going to do a session handoff" | jdb 2:00:48 | ✅ `current-focus.md` Next step hand-off |
| H8 | Watch agents while they work | "Watch your agents as they're working and they're building things." | jdb 4:38:33 | ✅ check every agent's output (`AGENTS.md`) |

## Deliberately not adopted (Nate's tensions)
- **Levels 3–5** (semantic search, graph, always-on). "If there's not pain, then why create more?" (DTC 4:04)
- **Agent teams** (agents talking to each other): "they're very very expensive. So try to use them very sparingly." (jdb 5:42:35). Sub-agents only.
- **Bypass permissions.** He uses them (bCl 43:21) but flags "you do run that risk of full autonomy". This public repo keeps asking first.
- **Ingesting emails or Slack into the brain.** "you don't want to ingest into a second brain because that's just noise" (DTC 27:23): fetch live instead.
- **Auto Dream.** Nate says it isn't confirmed (Lrg 6:05). Our memory is this repo plus the weekly audit.

## Routing test (run in a fresh session after router changes)
Ask: who is Charlie, and what's his priority? Where would a new project go?
Where are past decisions? How do I add a video to Nate's brain? Where do audit
reports go? **Pass:** every answer names a real path from the router.
