# Nate's brain: concepts

**Built from (primary, both read in full):**
- **AI OS** = "Steal My Exact AI OS Setup (5 simple tips)", Ek1NBfnnTH0, 25:02 ([transcript][os])
- **Karpathy** = "I Built Another Andrej Karpathy Using Claude", bvGptCLDhyo, 10:43 ([transcript][kb])

**Supporting** sources (other Nate transcripts in `research/nate-herk/`) are cited only to back up or challenge a point, and are labelled *supporting*.
**Wider course and newer videos (ingested 2026-10-07):** the other 14 saved transcripts (bCl, jdb, 3XI, c0k, Lrg, yys, 0WD, 9KO, RzL, e18, kB9, HIR, zKB, plus 9hetShMMp2s which added nothing). They feed section G and the "Also: [code m:ss]" lines. Codes are defined in the table in [standard-ai-os-v1.md](../../../system/standard-ai-os-v1.md); zKB (not in that table) is [Master 95% of Claude Code Skills in 28 Minutes](../master-95-of-claude-code-skills-in-28-minutes--zKBPwDpBfhs-transcript.md). When videos disagree, the newer one wins: upload order is in [videos.md](../videos.md) (smaller # = newer). 35 more transcripts from the 2026-10-08 full-channel audit feed section H (codes in the standard's code table).
**Date:** 2026-10-07. History of changes is in [log.md](log.md); current coverage is in [index.md](index.md).
**Rules for this file:** text in quote marks is the exact caption wording (caption slips kept: "cloudmd" = CLAUDE.md, "wiks" = wikis, "crrons" = crons, "Herk 2" = Nate's own AI OS project). Everything else is paraphrase. Our own reading is marked **(inference)**.

---

## A. Why an AI OS gives wrong answers

**1. Four context failure modes: poisoning, bloat, confusion, clash**
When an agent is wrong because of its context, it is one of four things. *Poisoning*: a false fact sits in the context and the agent repeats it confidently. *Bloat*: so much is loaded that the agent can't pick out what's relevant (needle in a haystack). *Confusion*: something is irrelevant or missing, so the agent fills the gap itself (classic hallucination). *Clash*: old and new sources, or two sources, disagree, so the agent can't tell which to trust. Poisoning is the easiest to fix (verify: web search, cross-check a live source, or a human in the loop); bloat is harder and is handled by the expertise/situational split (concept 2).
> "the four failure modes, poisoning, bloat, confusion, and clash." [1:34](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=94s)
> "Poisoning means you have a false fact somewhere in the context." [2:05](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=125s)
> "In March your policy was always refund. In June your policy is now to never refund." [4:07](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=247s)
Also: verification fix [2:36](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=156s); bloat [3:06](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=186s); confusion [3:36](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=216s). Source: AI OS ([transcript][os]).
Nate gives no specific fix for clash or confusion in this video. **(inference)** Clash is fixed by keeping one current source per fact and marking or retiring old ones; confusion by making sure the missing thing has a route.
**Used by:** Rule 1 ([rules.md](rules.md)).

**2. Expertise context vs situational context**
Expertise context is what the agent needs on every run (who you are, goals, what the business does, policies): the rulebook, like a system prompt. Situational context is pulled in just in time for one task (a support ticket from yesterday). His analogy: the principal knows how classrooms run; the teacher knows each student. Keeping situational data always loaded adds bloat, confusion and even clash. In his "four C's" framework he maps *context* to expertise and *connections* to situational.
> "I think of context as expertise and I think of connections as situational." [4:37](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=277s)
> "expertise context is the rulebook" [5:38](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=338s)
> "go use that live lookup, pull the data in because you need it" [6:08](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=368s)
Source: AI OS ([transcript][os]).
Also: [bCl 2:20:23](https://www.youtube.com/watch?v=bCljOfCH8Ms&t=8423s) "I said don't read from the wiki unless you actually need it."; second brain = the first two C's, [yys 2:04](https://www.youtube.com/watch?v=yysILVsfLFM&t=124s).
**Used by:** Rule 4 ([rules.md](rules.md)).

## B. Organising the OS

**3. The root file is a router, not a warehouse**
His main CLAUDE.md says who the agent is in a line or two and is otherwise a routing table: if you need X, go here (wiki path, hot cache, index, memory, tools, skills and agents, decisions, templates, projects). Sub-folders can have their own CLAUDE.md for project-level instructions. Because it is all plain files and folders, other agents (Codex, Hermes) can use the same setup.
> "I treat this almost purely as a router." [12:46](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=766s)
> "my cloudmd is essentially just a master routing file, just a master table of context." [13:47](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=827s)
> "a bunch of files and folders, which means you can plug in Hermes, you can plug in codecs" [15:19](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=919s)
Also: he shows the routing table at [13:17](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=797s). Source: AI OS ([transcript][os]).
*Supporting:* the same idea in [Every Level of a Claude Second Brain](../every-level-of-a-claude-second-brain-explained--DTCyvo6cC54-transcript.md), "the claw.md is kind of treated as a router" [4:34](https://www.youtube.com/watch?v=DTCyvo6cC54&t=274s), and in [I Turned Claude Into the Ultimate Second Brain](../i-turned-claude-into-the-ultimate-second-brain--8QQ_INxAhRs-transcript.md), "I think of my Claude and MD file as my router" [5:09](https://www.youtube.com/watch?v=8QQ_INxAhRs&t=309s).
Also: "I go into a routing map and that's the majority of my agents.mmd" [yys 6:07](https://www.youtube.com/watch?v=yysILVsfLFM&t=367s); new skills get registered in it [bCl 1:30:08](https://www.youtube.com/watch?v=bCljOfCH8Ms&t=5408s); "cloudmd is the rules. Memory is, you know, learned facts." [jdb 2:04:50](https://www.youtube.com/watch?v=jdbOVepEtUE&t=7490s). Length limit: concept 18.
**Used by:** Rule 5, Rule 20 ([rules.md](rules.md)).

**4. No single right layout; the test is whether you (and the agent) can find things**
Flat or deeply nested doesn't matter. What matters is routing rules good enough that you and the agent can find things. His check: think of something you made and find it in the file explorer without searching or asking Claude. If you can, an agent with routing rules probably can too. The only wrong setup is one that keeps giving wrong answers while you do nothing.
> "routing rules in place so that you and your agents can find it." [16:49](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=1009s)
> "see if you could find it without searching, without asking Claude" [18:20](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=1100s)
> "the only way that you're doing this wrong is if you're constantly getting wrong answers and you're not doing anything about it." [18:20](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=1100s)
Source: AI OS ([transcript][os]).
*Supporting:* "can your agent find it again, and could you find it again" [2:02](https://www.youtube.com/watch?v=DTCyvo6cC54&t=122s) ([transcript](../every-level-of-a-claude-second-brain-explained--DTCyvo6cC54-transcript.md)).
**Used by:** Rule 6 ([rules.md](rules.md)).

**5. Segment knowledge that is distinct and growing**
When separate bodies of knowledge keep growing (his YouTube transcripts and his meeting transcripts), split them into their own wikis so the agent knows where to look and searches far fewer files: faster, more accurate and cheaper on tokens. Claude Code itself suggested his split. Clients: keep internal knowledge (dates, price, scope, calls) in the OS, segmented by client; keep client-facing deliverables in a separate repo, while the OS still knows the engagement exists.
> "the more you can segment stuff out, the better." [20:21](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=1221s)
> "how can you narrow the actual context that your agent is going to be looking through?" [20:51](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=1251s)
> "it still needs to know about this engagement." [22:21](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=1341s)
Also: the split Claude suggested [17:19](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=1039s)–[17:50](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=1070s). Source: AI OS ([transcript][os]).
**Used by:** Rule 9 ([rules.md](rules.md)).

**6. Cadence: automate data that arrives on a schedule**
If you keep asking the agent to pull the same data, it isn't really just-in-time situational context. Data that lands on a fixed rhythm (his Monday Q&A, Tuesday leadership meeting) should be pulled in by a cron or routine, so it is there even if you forget. Natural language plus an API key is usually enough to set it up.
> "Build automations to update data." [18:51](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=1131s)
> "this isn't sort of like a just in time sort of situational context thing" [19:21](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=1161s)
Also: the audit's "durability" suggestion of weekly crons [9:13](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=553s). Source: AI OS ([transcript][os]).
Also: of much-used skills, "If they're getting used so often, why not just automate them?" [bCl 2:28:30](https://www.youtube.com/watch?v=bCljOfCH8Ms&t=8910s). Cadence is the fourth C and comes last: concept 19.
**Used by:** Rule 10 ([rules.md](rules.md)).

## C. Keeping it true

**7. The OS audit: indexes are claims, check them against reality**
His `OS audit` skill reads the whole project and reports what is weak. It is read-only: it lists findings and fixes, writes a dated report into an `audits/` folder, reads the previous report first, and waits for a yes before fixing anything. Checks include routing integrity (does everything the router points to exist, and is anything misrouted in reverse), index truth (does the index match the disk), freshness, memory, bloat, duplication and organisation. On big projects it fans out one explore sub-agent per check and merges their reports. His demo found the index said 55 folders while the disk had 79, and listed the wrong answers that would cause.
> "It won't actually do anything yet." [1:04](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=64s)
> "Indexes and wiks are claims about what exists and what's current. The audit checks every claim against reality." [9:43](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=583s)
> "Index says 55 folders, but disk has 79." [8:12](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=492s)
Also: fix list marked await approval [8:43](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=523s); checks [10:14](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=614s)–[11:46](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=706s). Before the skill, he did the same thing by asking weekly or monthly in plain chat: "have AI audit itself." [16:49](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=1009s). Source: AI OS ([transcript][os]).
Also: reports are saved and the skill should "look for earlier reports inside of the audit folder" [10:14](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=614s); run it weekly, "Maybe every single Friday, you run an audit" [bCl 2:28:30](https://www.youtube.com/watch?v=bCljOfCH8Ms&t=8910s).
**Used by:** Rule 7, Rule 8, Rule 28 ([rules.md](rules.md)).

**8. Freshness is a separate check from accuracy**
Data can be correct but stale. The audit grades each data feed as fresh, drifting, frozen, retired or on demand. His demo's knowledge was current only to 29 June, so any later business question would get a confident but wrong answer.
> "Are all the data feeds current?" [11:15](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=675s)
> "fresh, drifting, frozen, retired, or if they're on demand." [11:15](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=675s)
> "would give me a confident June state answer, which would be wrong." [8:43](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=523s)
Source: AI OS ([transcript][os]).
**Used by:** Rule 8 ([rules.md](rules.md)).

**9. Backtrack retrieval misses, then fix the route**
When the agent searches for ages, or says it has no access to something you know is there, don't just tell it not to let that happen again. Make it retrace what it did and where it looked, explain why it missed, and then update the routing or reorganise files based on what it found.
> "you searched, and help me figure out why you didn't find that data right away." [23:22](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=1402s)
> "Have it update the routing. Have it maybe even move stuff or reorganize stuff based on what it found when it was backtracking." [23:22](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=1402s)
Also: "number five is to backtrack" [22:51](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=1371s). Source: AI OS ([transcript][os]).
*Supporting:* a 5-minute search for a file he knows the location of means the architecture needs updating, [5:39](https://www.youtube.com/watch?v=8QQ_INxAhRs&t=339s) ([transcript](../i-turned-claude-into-the-ultimate-second-brain--8QQ_INxAhRs-transcript.md)).
Also: "every time you correct AI, you feed that correction back into the system" [3XI 6:37](https://www.youtube.com/watch?v=3XIGcM7VICc&t=397s); fix it where it lasts, "update the skill in the smallest durable place" [HIR 6:05](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=365s).
**Used by:** Rule 11 ([rules.md](rules.md)).

## D. Building an expert brain

**10. Raw evidence vs derived brain**
Step one gathers everything the expert has said into one raw folder, one sub-folder per source (he used free YouTube caption tools, and a paid X API that cost about a dollar), with one agent per source in parallel and a written record of what was fetched so it can be checked. Raw text alone is too messy to search well, so an LLM compiles it into a wiki (Karpathy's LLM-wiki idea). The raw files are never edited; the wiki is the derived layer on top. Obsidian is only a viewer.
> "I told it to write down what it got, so that you can actually check it." [3:34](https://www.youtube.com/watch?v=bvGptCLDhyo&t=214s)
> "It's like finding a needle in a haystack." [3:34](https://www.youtube.com/watch?v=bvGptCLDhyo&t=214s)
> "The raw files don't get touched" [4:04](https://www.youtube.com/watch?v=bvGptCLDhyo&t=244s)
Also: crawl set-up [3:03](https://www.youtube.com/watch?v=bvGptCLDhyo&t=183s); Obsidian as the visual layer [4:34](https://www.youtube.com/watch?v=bvGptCLDhyo&t=274s). Source: Karpathy ([transcript][kb]).
*Supporting:* raw → wiki → index and log, shown step by step in [Karpathy's LLM Wiki Is Basically Cheating](../fable-5-karpathy-s-llm-wiki-is-basically-cheating--hQvwMj7IJe4-transcript.md), [8:38](https://www.youtube.com/watch?v=hQvwMj7IJe4&t=518s).
**Used by:** Rule 12 ([rules.md](rules.md)).

**11. The brain's pages: index, log, source pages, concepts and rules**
The wiki keeps an index and a log, has one page per thing the expert wrote or said, and topic pages (principles, rules, methods, how he explains, how he debugs). He also mentions a "hot page". **(inference)** In this repo that maps to `index.md` (current state, what's covered), `log.md` (history), `concepts.md` (ideas) and `rules.md` (operating rules), with the transcripts as the source pages.
> "keeps an index, keeps a log" [4:04](https://www.youtube.com/watch?v=bvGptCLDhyo&t=244s)
Also: page types [4:34](https://www.youtube.com/watch?v=bvGptCLDhyo&t=274s)–[5:04](https://www.youtube.com/watch?v=bvGptCLDhyo&t=304s); index, hot page and log updated on ingest [9:38](https://www.youtube.com/watch?v=bvGptCLDhyo&t=578s). Source: Karpathy ([transcript][kb]).
*Supporting:* the index and log let the AI "incrementally build and maintain this wiki" [9:38](https://www.youtube.com/watch?v=hQvwMj7IJe4&t=578s) ([transcript](../fable-5-karpathy-s-llm-wiki-is-basically-cheating--hQvwMj7IJe4-transcript.md)).
Also: on memory files, "it's an index, not a dump" [Lrg 5:34](https://www.youtube.com/watch?v=LrgfmZkl3nc&t=334s).
**Used by:** Rule 14 ([rules.md](rules.md)).

**12. Provenance and inference labels**
Rules are what make the agent think like the expert, not just recall him. Each rule must link to an exact quote and where it came from, so you can click through and check it. If there is no source, the agent must say it is inferring.
> "what makes it think like him instead of just knowing what he said in the past." [5:34](https://www.youtube.com/watch?v=bvGptCLDhyo&t=334s)
> "every rule has to connect with an exact quote from him and where it came from. Because we don't want Claude to just make things up." [5:34](https://www.youtube.com/watch?v=bvGptCLDhyo&t=334s)
> "if there is no source, the agent has to say explicitly that it's inferring" [6:34](https://www.youtube.com/watch?v=bvGptCLDhyo&t=394s)
Source: Karpathy ([transcript][kb]).
**Used by:** Rule 13 ([rules.md](rules.md)).

**13. Relational ingestion**
The wiki links pages to each other: every rule links to its sources and every source to the rules it supports, so you query a relationship map, not a pile of notes. Adding one new link via an ingest command writes a source page, updates every page that source touches, and updates the index, hot page and log. In his demo a rule that had one source got a second and was promoted to a real rule. He never edited the wiki by hand.
> "Every rule links back to the source that it came from" [5:04](https://www.youtube.com/watch?v=bvGptCLDhyo&t=304s)
> "it will update every page that post touches." [9:38](https://www.youtube.com/watch?v=bvGptCLDhyo&t=578s)
> "a rule that was sitting on the bench with one source behind it got its second source and became a real rule." [9:38](https://www.youtube.com/watch?v=bvGptCLDhyo&t=578s)
Also: relationships make querying work [4:04](https://www.youtube.com/watch?v=bvGptCLDhyo&t=244s). Source: Karpathy ([transcript][kb]).
**Used by:** Rule 14 ([rules.md](rules.md)).

## E. Turning knowledge into behaviour

**14. Specialist agents and skills**
The rules become two files. A sub-agent holds the rules, how it talks and the loop it runs on every task; being a separate Claude with its own context, it doesn't drag your whole conversation along. A skill (a slash command) is the entry point: it sends your question to the agent and grades the answer against a checklist, one line per rule. The same knowledge can then feed your other skills, agents and workflows.
> "it doesn't drag your whole conversation along with it." [6:34](https://www.youtube.com/watch?v=bvGptCLDhyo&t=394s)
> "grades the answer against a checklist, one line per rule" [7:05](https://www.youtube.com/watch?v=bvGptCLDhyo&t=425s)
> "I can wire that knowledge into my own skills and my own agents and my own workflows" [2:02](https://www.youtube.com/watch?v=bvGptCLDhyo&t=122s)
Source: Karpathy ([transcript][kb]).
*Supporting, a challenge:* in [I Deleted All My Claude Skills](../i-deleted-all-my-claude-skills-and-claude-got-smarter--XNQBCRcwXV4-transcript.md) he warns over-specific skills can hold newer models back and suggests "making versions of them that aren't as specific" [5:41](https://www.youtube.com/watch?v=XNQBCRcwXV4&t=341s). **(inference)** Make skills for repeatable procedures, but keep them short.
Also: skill anatomy and triggering, concept 21; sub-agents in depth, concept 23.
**Used by:** Rule 15 ([rules.md](rules.md)).

**15. Run gates: enforce verification, don't just ask for it**
A hook runs when the agent tries to finish its turn. If it wrote code it never ran, the hook blocks the answer and sends it back. Verification becomes a step the agent can't skip.
> "a little script that runs right when the agent tries to finish its turn." [7:35](https://www.youtube.com/watch?v=bvGptCLDhyo&t=455s)
> "if it wrote code and it never ran it, the hook will basically block the answer" [7:35](https://www.youtube.com/watch?v=bvGptCLDhyo&t=455s)
> "baking in like a verification loop." [7:35](https://www.youtube.com/watch?v=bvGptCLDhyo&t=455s)
Source: Karpathy ([transcript][kb]).
Also: "every single skill that I build works in some sort of verification loop" [9KO 9:40](https://www.youtube.com/watch?v=9KOtMsZ9I28&t=580s).
*Supporting:* "You verify yourself so that I don't have to verify." [9:15](https://www.youtube.com/watch?v=XNQBCRcwXV4&t=555s) ([transcript](../i-deleted-all-my-claude-skills-and-claude-got-smarter--XNQBCRcwXV4-transcript.md)).
**Used by:** Rule 16 ([rules.md](rules.md)).

**16. Real-world testing**
The last step is testing on real things. Teaching test: it writes down what done means first, builds the smallest version, predicts, runs, shows a broken version, then lists what it ran and which rule drove each move. Review test: "would the client accept this?" on a script that had passed Claude's own test; the agent predicted a crash on an emoji in a normal Windows terminal, ran it that way, and it crashed. It then trimmed what wasn't earning its place and proved the trimmed version behaved the same by running both side by side.
> "the last step, of course, is just to test it." [8:05](https://www.youtube.com/watch?v=bvGptCLDhyo&t=485s)
> "saying that it works was only true in one specific setting or terminal." [9:08](https://www.youtube.com/watch?v=bvGptCLDhyo&t=548s)
> "we make it test on things that are real." [10:08](https://www.youtube.com/watch?v=bvGptCLDhyo&t=608s)
Also: the emoji crash [8:37](https://www.youtube.com/watch?v=bvGptCLDhyo&t=517s). Source: Karpathy ([transcript][kb]).
Also: a slides skill that couldn't see its own output got Chrome so it could "open the page screenshot it look at it" [bCl 1:03:37](https://www.youtube.com/watch?v=bCljOfCH8Ms&t=3817s); "Before returning the final output, define the acceptance criteria." [HIR 8:05](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=485s).
Also: "But, if Claude has your files and your examples and your workflows and your style guides and the actual success criteria for what good looks like" [brB 5:34](https://www.youtube.com/watch?v=brB-hSiV2iU&t=334s)
**Used by:** Rule 17, Rule 27 ([rules.md](rules.md)).

## F. The point of it all

**17. Human understanding is the finish line**
The brain is not a voice clone or impression; it condenses how an expert thinks so you can talk to it until you understand. You can't be expert in everything, but you must understand what you ship, and your own system: he still finds his own files by hand to make sure he understands his OS. Team-wide AI OS sync is, for him, unsolved and a people and habit problem more than a tech one; mastering your own system first makes that easier.
> "you can outsource your thinking, but you cannot outsource your understanding." [10:08](https://www.youtube.com/watch?v=bvGptCLDhyo&t=608s) (Nate quoting Karpathy)
> "then I can just talk to it until I understand it." [2:02](https://www.youtube.com/watch?v=bvGptCLDhyo&t=122s)
> "I actually understand my own second brain" [18:51](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=1131s)
> "I don't think it's a tech problem. I think it's a people problem." [23:52](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=1432s)
Also: not an impression [0:31](https://www.youtube.com/watch?v=bvGptCLDhyo&t=31s); master your own systems first [24:23](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=1463s). Sources: Karpathy ([transcript][kb]), AI OS ([transcript][os]).
Also: "Never accept AI output without asking why" [bCl 6:37](https://www.youtube.com/watch?v=bCljOfCH8Ms&t=397s); "You can't scale a system if you haven't lived in it yourself." [bCl 2:31:32](https://www.youtube.com/watch?v=bCljOfCH8Ms&t=9092s).
*Supporting:* for rolling an OS out to a team, "you have to learn it first" [33:13](https://www.youtube.com/watch?v=8QQ_INxAhRs&t=1993s) ([transcript](../i-turned-claude-into-the-ultimate-second-brain--8QQ_INxAhRs-transcript.md)).
**Used by:** Rule 18 ([rules.md](rules.md)).

## G. From the wider course and newer videos

**18. The router is re-read every message, so keep it under 200 lines**
CLAUDE.md is loaded as system context at the start of every chat, so every extra line costs on every turn. Edits to it only take effect in a new session.
> "Claude auto reads it at the start of every single chat as system context. So keep it under 200 lines." [jdb 5:36:27](https://www.youtube.com/watch?v=jdbOVepEtUE&t=20187s)
> "the edit actually doesn't apply until you restart that session." [jdb 5:55:15](https://www.youtube.com/watch?v=jdbOVepEtUE&t=21315s)
Also: keep decisions, not chat history, in it: "Save decisions, not conversations." [jdb 5:44:05](https://www.youtube.com/watch?v=jdbOVepEtUE&t=20645s).
**Used by:** Rule 19 ([rules.md](rules.md)).

**19. The four C's, built in order: context, connections, capabilities, cadence**
Context is what the AI knows about you; connections are the live data it can reach; capabilities are the skills that make it useful; cadence is when it acts on its own. The first two are the second brain. Each layer needs the one before it.
> "You can't have cadence without connections. You can't have capability without context. And you have to go in this order." [bCl 12:14](https://www.youtube.com/watch?v=bCljOfCH8Ms&t=734s)
> "each of these layers can't happen without the previous one." [0WD 8:09](https://www.youtube.com/watch?v=0WDkwMxj13s&t=489s)
Also: [yys 2:04](https://www.youtube.com/watch?v=yysILVsfLFM&t=124s), [jdb 4:19:40](https://www.youtube.com/watch?v=jdbOVepEtUE&t=15580s). Links concept 2 (context/connections) and concept 6 (cadence).
Also: "So these four things really come one after the other, context, connections, capabilities, and cadence." [Xpb 45:42](https://www.youtube.com/watch?v=X-pbJWKmwi0&t=2742s)
**Used by:** no rule yet; links concepts 2 and 6 (above).

**20. Levels of a second brain: start at level 1, move up only when it hurts**
Level 1 is a router plus folders. Move to a compiled wiki (level 2) when notes pile up and you forget what's in them; a markdown wiki with good indexes is enough until hundreds of pages. Only keep knowledge that will still matter in a year.
> "If you have 30 plus notes and you keep forgetting what's in them, look at level two." [DTC 28:53](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1733s)
> "if you have hundreds of pages with good indexes, you're fine with wiki graph" [bCl 2:23:27](https://www.youtube.com/watch?v=bCljOfCH8Ms&t=8607s)
Also: "If there's not pain, then why create more?" [DTC 4:04](https://www.youtube.com/watch?v=DTCyvo6cC54&t=244s); "in a year, will it be good for me to have this memory in here?" [DTC 27:23](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1643s).
> "My wiki has links, isn't that a knowledge graph? Not exactly." — [12:41](https://www.youtube.com/watch?v=DTCyvo6cC54&t=761s)
Added 2026-10-08: links between wiki pages are level 2, "it's like a a see also. It's like backlinks"; level 4 knowledge graphs record *how* things relate, and he plays with them but doesn't use them day to day. So "fully connected" at our level means every page links to related pages, not a graph tool.
**Used by:** no rule yet; level 1 is concept 3's router (inference).

**21. Skills: progressive loading, and the description is the trigger**
Claude reads only each skill's name and description (front matter, about 100 tokens) to pick one, then the full SKILL.md, then extra files only if needed. So the description must use the words a person would actually say, two skills mustn't compete, and broken front matter (an unclosed quote) stops it firing. Test with an obvious request, a reworded one and an unrelated one. Keep SKILL.md under 500 lines.
> "it would only read the YAML front matter." [zKB 12:10](https://www.youtube.com/watch?v=zKBPwDpBfhs&t=730s)
> "a skill that Claude can't find is basically a skill that you don't have." [HIR 4:33](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=273s)
Also: [zKB 11:40](https://www.youtube.com/watch?v=zKBPwDpBfhs&t=700s)–[12:41](https://www.youtube.com/watch?v=zKBPwDpBfhs&t=761s); [HIR 4:02](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=242s); "You have to close off the quotes if you open them up" [jdb 2:37:42](https://www.youtube.com/watch?v=jdbOVepEtUE&t=9462s); "keep the skill.md under 500 lines" [bCl 1:21:28](https://www.youtube.com/watch?v=bCljOfCH8Ms&t=4888s).
**Used by:** Rule 21, Rule 22 ([rules.md](rules.md)).

**22. Skills start small, keep working code, and earn autonomy**
A skill can be a short prompt you were tired of retyping. When a script works, save it as a file the skill points to rather than letting Claude rewrite it each run. New skills report and ask; give them more freedom only after many runs.
> "A skill can just be a prompt that you don't want to have to say every single time." [c0k 2:02](https://www.youtube.com/watch?v=c0kaKxM2pHg&t=122s)
> "don't leave that code trapped inside the chat" [HIR 2:02](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=122s)
Also: "battle tested" first [jdb 1:47:37](https://www.youtube.com/watch?v=jdbOVepEtUE&t=6457s); "They could literally just be a 50line markdown file." [bCl 1:25:34](https://www.youtube.com/watch?v=bCljOfCH8Ms&t=5134s); vet third-party skills [bCl 1:18:55](https://www.youtube.com/watch?v=bCljOfCH8Ms&t=4735s).
**Used by:** Rule 23 ([rules.md](rules.md)).

**23. Sub-agents: for piles of output, read-only by their tools, never forced**
Use a sub-agent when a job would flood your chat with output you won't re-read (many files, big searches). Make one read-only through its tool list, not by asking. Don't use them for one quick step: too many gives worse results. Shared agents live in the repo.
> "is this about to dump a pile of stuff into my chat that I'll never read again? If that's ever yes, delegate it to a sub agent." [jdb 2:43:47](https://www.youtube.com/watch?v=jdbOVepEtUE&t=9827s)
> "if you're forcing too many sub agents, you're going to get worse results" [e18 24:57](https://www.youtube.com/watch?v=e18sdZLwP7o&t=1497s)
Also: "explicitly read-only" via disallowed tools [e18 7:10](https://www.youtube.com/watch?v=e18sdZLwP7o&t=430s); "so that you don't blow your own context window" [bCl 1:23:32](https://www.youtube.com/watch?v=bCljOfCH8Ms&t=5012s).
**Used by:** Rule 24 ([rules.md](rules.md)).

**24. Permissions are keys and deny lists, not prompts**
Assume the agent will do anything it is able to. Safety comes from what it physically can't do: scoped API keys that only allow the needed actions, and a settings deny list for risky commands. His 150,000-email accident came from too many tools, not the permission mode.
> "A prompt is never a permission layer. You basically have to have the assumption that if it can, it will." [8QQ 24:31](https://www.youtube.com/watch?v=8QQ_INxAhRs&t=1471s)
> "Can you help me update the settings file so that you physically cannot do those things?" [jdb 1:14:28](https://www.youtube.com/watch?v=jdbOVepEtUE&t=4468s)
Also: "there's no point in giving the agent that actual tool to be able to do so." [jdb 1:10:54](https://www.youtube.com/watch?v=jdbOVepEtUE&t=4254s); per-key permissions [bCl 38:44](https://www.youtube.com/watch?v=bCljOfCH8Ms&t=2324s).
**Used by:** Rule 25 ([rules.md](rules.md)).

**25. Secrets in .env; your own keys travel, app connectors don't**
Keys live in a `.env` file kept out of Git and out of chat. Prefer an API key plus a reference .md over app connectors or piles of MCP servers: connectors are lost when you change tool, and loaded MCPs eat tokens.
> "If you rely on these connections, that is not great" [jdb 1:37:24](https://www.youtube.com/watch?v=jdbOVepEtUE&t=5844s)
> "if you switch off to a different desktop app or a different harness, you lose everything." [jdb 1:37:24](https://www.youtube.com/watch?v=jdbOVepEtUE&t=5844s)
Also: "gets excluded from anytime we do a public push" [bCl 41:50](https://www.youtube.com/watch?v=bCljOfCH8Ms&t=2510s); MCP token cost [bCl 39:45](https://www.youtube.com/watch?v=bCljOfCH8Ms&t=2385s).
**Used by:** Rule 26 ([rules.md](rules.md)).

**26. Grill me: interview the knowledge out of your head**
The bottleneck is getting what you know into the system; a quick brain dump is never enough. The grill-me skill asks one question at a time, checkpoints every answer to a doc in `brainstorms/`, flags gaps to chase with others, and can be re-run when things change. Up-front time gets a skill close to right on the first try.
> "It's not ever good enough." [c0k 1:02](https://www.youtube.com/watch?v=c0kaKxM2pHg&t=62s)
> "the bigger problem is getting everything out of your brain into the system" [DTC 22:18](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1338s)
Also: checkpointing to brainstorms [c0k 2:33](https://www.youtube.com/watch?v=c0kaKxM2pHg&t=153s); open flags [c0k 6:07](https://www.youtube.com/watch?v=c0kaKxM2pHg&t=367s); ask until 95% sure [jdb 5:32:54](https://www.youtube.com/watch?v=jdbOVepEtUE&t=19974s).
**Used by:** Rule 30 ([rules.md](rules.md)).

**27. Session hygiene: clear between tasks, hand off before it degrades**
Each message in a long chat costs more than in a fresh one, so start fresh for unrelated tasks. Before clearing (he says around 250-300k tokens, as autocompact comes too late), have the agent write a hand-off: what was done, files made, open decisions, next step.
> "Use slashclear between unrelated tasks." [jdb 5:30:53](https://www.youtube.com/watch?v=jdbOVepEtUE&t=19853s)
> "Here are open decisions. Here's what's next." [0WD 22:24](https://www.youtube.com/watch?v=0WDkwMxj13s&t=1344s)
Also: "But the autocompact kicks in way too late." [jdb 2:00:48](https://www.youtube.com/watch?v=jdbOVepEtUE&t=7248s).
**Used by:** Rule 29 ([rules.md](rules.md)).

**28. One set of files for every tool (Claude Code and Codex)**
Build tool-agnostic. Codex reads AGENTS.md, keeps config and agents in `.codex/` and skills in `.agents/`; skill files are identical between the two, only agent files differ (TOML vs markdown). A CLAUDE.md can simply reference AGENTS.md.
> "you're building things to be tool agnostic" [bCl 2:04](https://www.youtube.com/watch?v=bCljOfCH8Ms&t=124s)
> "the skill files, which are the markdown files with the YAML front matter, are the exact same." [kB9 3:04](https://www.youtube.com/watch?v=kB9iMD0EjT8&t=184s)
Also: [DTC 22:49](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1369s); shared skills and agents go in the repo [e18 24:57](https://www.youtube.com/watch?v=e18sdZLwP7o&t=1497s).
**Used by:** no rule yet; concept 3 says the same files serve Codex.

## H. From the full-channel audit (2026-10-08)

**29. Context costs money and rots: act at about half the window**
Every new message makes Claude re-read the whole chat from the start, so long chats cost more and, past roughly half the window, the answers get worse. Look at what is filling the context (run /context in a fresh session, delete unused tools, skills and servers) before blaming the model, convert documents to markdown because it is cheaper for AI, and check your usage allowance. When a path has gone wrong, rewind or restart rather than piling corrections on top of the failed attempt.
> "somewhere around halfway through your context window, it starts to fall apart." [eRS 4:32](https://www.youtube.com/watch?v=eRS3CmvrOvA&t=272s)
> "go into a fresh session, do /context, and see what you're sitting at before you even send off anything" [_qZ 1:04](https://www.youtube.com/watch?v=_qZvORxGqI0&t=64s)
> "Claude rereads the entire conversation from the beginning, and all of those are tokens that it's charging you for" [49V 1:04](https://www.youtube.com/watch?v=49V-5Ock8LU&t=64s)
**Used by:** Rule 31 ([rules.md](rules.md)).

**30. Plan, let the AI attack the plan, then build**
Before anything non-trivial, plan first, then ask Claude to push back and play devil's advocate on the plan before it builds. Big plans are saved to a file and worked phase by phase, one session each. Nate teaches plan mode for this; Charlie declined plan mode itself on 2026-10-08, and this repo's 95%-or-ask rule (R14: be 95% sure or ask 1-2 questions) does the same job.
> "You ask Claude to start challenging you and pushing back and playing devil's advocate before it builds anything or before it approves any plan" [iTY 2:36](https://www.youtube.com/watch?v=iTY8Q449YNQ&t=156s)
> "Have one for discovery where you can have Claude read through PDFs and read through the code base" [_qZ 21:25](https://www.youtube.com/watch?v=_qZvORxGqI0&t=1285s)
> "So what you always want to do when you're creating an idea is you want to go on plan mode." [mpA 2:01:40](https://www.youtube.com/watch?v=mpALXah_PBg&t=7300s)
**Used by:** Rule 32 ([rules.md](rules.md)).

**31. A separate checker decides "done"; then try to break it**
The worker should not mark its own homework: a different model or persona checks the result, and after "done" you stress test it for edge cases. When output is bad, first ask whether it is a model, harness or organisation problem. Verification steps also go into the to-do list, not just the end.
> "is this a model problem, is this a harness problem? Or is this an organization problem?" [6LN 32:07](https://www.youtube.com/watch?v=6LNlCpQPYFc&t=1927s)
> "Claude doesn't get to declare itself done. A different model has to look at it with a different persona" [iTY 22:25](https://www.youtube.com/watch?v=iTY8Q449YNQ&t=1345s)
> "by the time it tells you it's done, you stress test it more. and you try to find those edge cases" [iTY 9:43](https://www.youtube.com/watch?v=iTY8Q449YNQ&t=583s)
**Used by:** Rule 33 ([rules.md](rules.md)).

**32. Skills do one job, are built from a real run, and retire when they stop earning**
Each skill or agent does one specific job. Build it by doing the task together once, then turning that run into a skill, and keep adding a line to a "don'ts" list for each real failure. Write instructions specifically, not vaguely. Retire a skill that no longer adds value, which matters once you have around ten.
> "the whole idea is that you want a skill to do one very specific job" [Xpb 1:06:25](https://www.youtube.com/watch?v=X-pbJWKmwi0&t=3985s)
> "So you want to make sure that your skill is actually adding value and not holding" [6LN 24:29](https://www.youtube.com/watch?v=6LNlCpQPYFc&t=1469s)
> "The way that I build my skills is I have Claude Code do something with me. I walk it through the steps" [mpA 6:21:32](https://www.youtube.com/watch?v=mpALXah_PBg&t=22892s)
**Used by:** Rule 34 ([rules.md](rules.md)).

**33. Unattended runs: one-shot, stateless, bounded, tested by hand first, fixed parts in scripts**
A scheduled or background run must never need to stop and ask, can only see the repo, APIs and environment secrets, and needs a bounded scope with a named deliverable. Test it by hand and prove one live run before switching the schedule on. Put the fixed details in a script, because an agent left to interpret the same message will drift.
> "the agent was just interpreting the message different every time and it just acted differently" [Xpb 3:00:25](https://www.youtube.com/watch?v=X-pbJWKmwi0&t=10825s)
> "So, bound the scope, name the deliverable, and then all your sub agents can be put on Haiku." [jZg 11:11](https://www.youtube.com/watch?v=jZgcWCzxh1I&t=671s)
> "You're not around. So, you probably want to make sure that it doesn't ever have to stop and ask you questions." [ehg 1:33](https://www.youtube.com/watch?v=ehg4fhydTgs&t=93s)
**Used by:** Rule 35 ([rules.md](rules.md)).

**34. Permissions in layers: deny plus allow, start strict, helpers inherit, read-only and drafts first**
Deny the destructive commands and also explicitly allow the safe ones. Start with read-only access and drafts, with a human approving anything outward, and remember that helper agents inherit the main session's permissions. Nate also describes auto mode (a classifier approves safe commands); auto mode is not adopted here, so the deny list stays the safety layer.
> "So, I would always start with like read-only access whenever you can, have the agent only do drafts" [Ktn 10:40](https://www.youtube.com/watch?v=Ktnwygcnd8U&t=640s)
> "go into your permissions and explicitly allow the commands that you know are safe" [jqo 14:07](https://www.youtube.com/watch?v=jqoFP9QapXI&t=847s)
> "they inherit the permissions from the main session. So, if you're on bypass permissions, then all of your agents are going to be on bypass permissions" [vDV 12:11](https://www.youtube.com/watch?v=vDVSGVpB2vc&t=731s)
**Used by:** Rule 36 ([rules.md](rules.md)).

**35. Check before anything goes public: security review, private-data hook, untrusted content, plugin vetting**
Before publishing, run a security review and use a hook to strip private data, not just a rule. Web pages and transcripts are untrusted content that could trick an agent into sending data out. Vet a plugin against a checklist (network calls, exfiltration, shell injection, secrets) before installing it.
> "that there's a hook that fires to remove any PII, any sensitive data of that client that I don't want living on my GitHub." [6LN 23:59](https://www.youtube.com/watch?v=6LNlCpQPYFc&t=1439s)
> "if Claude reads malicious content during a run, then it theoretically could be tricked into sending data to an external server." [ehg 11:41](https://www.youtube.com/watch?v=ehg4fhydTgs&t=701s)
> "I basically told it to run a security review and make sure that my API keys aren't exposed and that there's no vulnerabilities" [sag 30:01](https://www.youtube.com/watch?v=saggDHHnmtQ&t=1801s)
**Used by:** Rule 37 ([rules.md](rules.md)).

**36. File hygiene: scratch apart from deliverables, folder READMEs, project first, start every task in the project**
Tell the AI where throwaway files go so they stay apart from deliverables, and give every folder a short README saying why it exists. Everything starts in the project and is promoted to global only when earned, and every task starts inside the project, not a plain chat. "Remember this" has to end up in a file in the repo, since cloud auto-memory is wiped.
> "so that your agent always understands why does this folder exist and where should it look for different things" [Xpb 1:32:56](https://www.youtube.com/watch?v=X-pbJWKmwi0&t=5576s)
> "Everything is project until deserves to be promoted to global so that I know at all times what is the running total of everything that's running globally." [6LN 31:37](https://www.youtube.com/watch?v=6LNlCpQPYFc&t=1897s)
> "if you want your assistant to remember something permanently, just tell it remember that I always prefer X." [mpA 5:53:08](https://www.youtube.com/watch?v=mpALXah_PBg&t=21188s)
**Used by:** Rule 38 ([rules.md](rules.md)).

**37. Operator habits: paste the whole error, make it do its own chores, match model and effort, adopt tools only for real pain, cap parallel sessions, use the OS for everything**
Small habits that add up: paste the whole error, ask the AI to do the chores it lists for you, and use the cheapest model and effort that does the job. Adopt a new tool only for a real pain point and trial it on real work, run no more than three or four parallel sessions, and use your OS for everything for a week.
> "try to force yourself to do everything from here, from this interface" [Xpb 45:12](https://www.youtube.com/watch?v=X-pbJWKmwi0&t=2712s)
> "do not automatically run everything at maximum effort or even just high." [FBV 4:39](https://www.youtube.com/watch?v=FBVNS1l5Vb8&t=279s)
> "it has some action items, it actually just tells you to do some stuff that it could do itself" [sag 15:17](https://www.youtube.com/watch?v=saggDHHnmtQ&t=917s)
**Used by:** Rule 39 ([rules.md](rules.md)).

**38. Parts rot at different speeds; score each audit**
Different parts of an OS go stale at different rates, so review each at its own pace. Score every audit and keep the scores, so you can see the system improving over time.
> "it will store your scores every time so that you can see how you're actually improving your system" [Xpb 53:15](https://www.youtube.com/watch?v=X-pbJWKmwi0&t=3195s)
> "All of these different parts decay, become obsolete or rot at different rates." [6LN 22:57](https://www.youtube.com/watch?v=6LNlCpQPYFc&t=1377s)
**Used by:** Rule 40 ([rules.md](rules.md)).

---

## Limits and things to treat carefully
- **Karpathy's 7 teaching rules** (build it, first-order term first, predict-run-compare, and so on, [5:34](https://www.youtube.com/watch?v=bvGptCLDhyo&t=334s)–[6:34](https://www.youtube.com/watch?v=bvGptCLDhyo&t=394s)) are Karpathy's, relayed by Nate. They live in `context/working-rules.md`, not in Nate's rules here.
- **Counting slip:** he says "four steps" but also "six prompts" ([2:33](https://www.youtube.com/watch?v=bvGptCLDhyo&t=153s), [10:08](https://www.youtube.com/watch?v=bvGptCLDhyo&t=608s)). The method matters, not the count.
- **Claims to check:** Karpathy's job titles ([0:01](https://www.youtube.com/watch?v=bvGptCLDhyo&t=1s)–[0:31](https://www.youtube.com/watch?v=bvGptCLDhyo&t=31s)), the X API costing "about a dollar" ([3:03](https://www.youtube.com/watch?v=bvGptCLDhyo&t=183s)), model names such as Opus 4.8 ([9:13](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=553s)).
- **Videos that disagree (newer wins; # in [videos.md](../videos.md), smaller = newer):**
  - *Bypass permissions.* In bCl (#118) he warns "you do run that risk of full autonomy" [bCl 43:21](https://www.youtube.com/watch?v=bCljOfCH8Ms&t=2601s); in jdb (#67) he runs bypass but only with a settings deny list, and says auto mode is "really solid" for most people [jdb 1:14:28](https://www.youtube.com/watch?v=jdbOVepEtUE&t=4468s)–[1:14:59](https://www.youtube.com/watch?v=jdbOVepEtUE&t=4499s). Current view: deny list first (concept 24).
  - *Auto Dream* (automatic memory clean-up, Lrg #152): "Now, this isn't confirmed with official documentation." [Lrg 6:05](https://www.youtube.com/watch?v=LrgfmZkl3nc&t=365s). Treat as unconfirmed.
  - *Agent teams:* "they're very very expensive. So try to use them very sparingly." [jdb 5:42:35](https://www.youtube.com/watch?v=jdbOVepEtUE&t=20555s). Sub-agents (concept 23) are the default.
  - *Skills:* bCl (#118) and zKB (#170) teach detailed skills; XNQ (#54) warns over-specific ones hold newer models back (concept 14). Newer wins: keep skills short.
- **Not Nate:** most of [RzL](../how-to-use-claude-code-better-than-98-of-people--RzLV8sfFdMM-transcript.md) is guest Cole Medin talking; don't cite it as Nate's view unless the line is clearly Nate's.
- **Token-budget numbers** (250-300k hand-off point, peak hours, the 200-line limit's exact figure) are tied to today's models and plans; the habits matter more than the numbers.
- **Promotion to ignore:** the Hyper Agent sponsor slot ([6:38](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=398s)–[7:41](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=461s)); free Skool and AI OS kit links ([1:04](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=64s), [2:02](https://www.youtube.com/watch?v=bvGptCLDhyo&t=122s)).

[os]: ../steal-my-exact-ai-os-setup-5-simple-tips--Ek1NBfnnTH0-transcript.md
[kb]: ../i-built-another-andrej-karpathy-using-claude--bvGptCLDhyo-transcript.md
