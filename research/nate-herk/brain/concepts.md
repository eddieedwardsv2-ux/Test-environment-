# Nate's brain: concepts

**Built from (primary, both read in full):**
- **AI OS** = "Steal My Exact AI OS Setup (5 simple tips)", Ek1NBfnnTH0, 25:02 ([transcript][os])
- **Karpathy** = "I Built Another Andrej Karpathy Using Claude", bvGptCLDhyo, 10:43 ([transcript][kb])

**Supporting** sources (other Nate transcripts in `research/nate-herk/`) are cited only to back up or challenge a point, and are labelled *supporting*.
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

**2. Expertise context vs situational context**
Expertise context is what the agent needs on every run (who you are, goals, what the business does, policies): the rulebook, like a system prompt. Situational context is pulled in just in time for one task (a support ticket from yesterday). His analogy: the principal knows how classrooms run; the teacher knows each student. Keeping situational data always loaded adds bloat, confusion and even clash. In his "four C's" framework he maps *context* to expertise and *connections* to situational.
> "I think of context as expertise and I think of connections as situational." [4:37](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=277s)
> "expertise context is the rulebook" [5:38](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=338s)
> "go use that live lookup, pull the data in because you need it" [6:08](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=368s)
Source: AI OS ([transcript][os]).

## B. Organising the OS

**3. The root file is a router, not a warehouse**
His main CLAUDE.md says who the agent is in a line or two and is otherwise a routing table: if you need X, go here (wiki path, hot cache, index, memory, tools, skills and agents, decisions, templates, projects). Sub-folders can have their own CLAUDE.md for project-level instructions. Because it is all plain files and folders, other agents (Codex, Hermes) can use the same setup.
> "I treat this almost purely as a router." [12:46](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=766s)
> "my cloudmd is essentially just a master routing file, just a master table of context." [13:47](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=827s)
> "a bunch of files and folders, which means you can plug in Hermes, you can plug in codecs" [15:19](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=919s)
Also: he shows the routing table at [13:17](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=797s). Source: AI OS ([transcript][os]).
*Supporting:* the same idea in [Every Level of a Claude Second Brain](../every-level-of-a-claude-second-brain-explained--DTCyvo6cC54-transcript.md), "the claw.md is kind of treated as a router" [4:34](https://www.youtube.com/watch?v=DTCyvo6cC54&t=274s), and in [I Turned Claude Into the Ultimate Second Brain](../i-turned-claude-into-the-ultimate-second-brain--8QQ_INxAhRs-transcript.md), "I think of my Claude and MD file as my router" [5:09](https://www.youtube.com/watch?v=8QQ_INxAhRs&t=309s).

**4. No single right layout; the test is whether you (and the agent) can find things**
Flat or deeply nested doesn't matter. What matters is routing rules good enough that you and the agent can find things. His check: think of something you made and find it in the file explorer without searching or asking Claude. If you can, an agent with routing rules probably can too. The only wrong setup is one that keeps giving wrong answers while you do nothing.
> "routing rules in place so that you and your agents can find it." [16:49](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=1009s)
> "see if you could find it without searching, without asking Claude" [18:20](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=1100s)
> "the only way that you're doing this wrong is if you're constantly getting wrong answers and you're not doing anything about it." [18:20](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=1100s)
Source: AI OS ([transcript][os]).
*Supporting:* "can your agent find it again, and could you find it again" [2:02](https://www.youtube.com/watch?v=DTCyvo6cC54&t=122s) ([transcript](../every-level-of-a-claude-second-brain-explained--DTCyvo6cC54-transcript.md)).

**5. Segment knowledge that is distinct and growing**
When separate bodies of knowledge keep growing (his YouTube transcripts and his meeting transcripts), split them into their own wikis so the agent knows where to look and searches far fewer files: faster, more accurate and cheaper on tokens. Claude Code itself suggested his split. Clients: keep internal knowledge (dates, price, scope, calls) in the OS, segmented by client; keep client-facing deliverables in a separate repo, while the OS still knows the engagement exists.
> "the more you can segment stuff out, the better." [20:21](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=1221s)
> "how can you narrow the actual context that your agent is going to be looking through?" [20:51](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=1251s)
> "it still needs to know about this engagement." [22:21](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=1341s)
Also: the split Claude suggested [17:19](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=1039s)–[17:50](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=1070s). Source: AI OS ([transcript][os]).

**6. Cadence: automate data that arrives on a schedule**
If you keep asking the agent to pull the same data, it isn't really just-in-time situational context. Data that lands on a fixed rhythm (his Monday Q&A, Tuesday leadership meeting) should be pulled in by a cron or routine, so it is there even if you forget. Natural language plus an API key is usually enough to set it up.
> "Build automations to update data." [18:51](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=1131s)
> "this isn't sort of like a just in time sort of situational context thing" [19:21](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=1161s)
Also: the audit's "durability" suggestion of weekly crons [9:13](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=553s). Source: AI OS ([transcript][os]).

## C. Keeping it true

**7. The OS audit: indexes are claims, check them against reality**
His `OS audit` skill reads the whole project and reports what is weak. It is read-only: it lists findings and fixes, writes a dated report into an `audits/` folder, reads the previous report first, and waits for a yes before fixing anything. Checks include routing integrity (does everything the router points to exist, and is anything misrouted in reverse), index truth (does the index match the disk), freshness, memory, bloat, duplication and organisation. On big projects it fans out one explore sub-agent per check and merges their reports. His demo found the index said 55 folders while the disk had 79, and listed the wrong answers that would cause.
> "It won't actually do anything yet." [1:04](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=64s)
> "Indexes and wiks are claims about what exists and what's current. The audit checks every claim against reality." [9:43](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=583s)
> "Index says 55 folders, but disk has 79." [8:12](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=492s)
Also: fix list marked await approval [8:43](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=523s); checks [10:14](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=614s)–[11:46](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=706s). Before the skill, he did the same thing by asking weekly or monthly in plain chat: "have AI audit itself." [16:49](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=1009s). Source: AI OS ([transcript][os]).

**8. Freshness is a separate check from accuracy**
Data can be correct but stale. The audit grades each data feed as fresh, drifting, frozen, retired or on demand. His demo's knowledge was current only to 29 June, so any later business question would get a confident but wrong answer.
> "Are all the data feeds current?" [11:15](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=675s)
> "fresh, drifting, frozen, retired, or if they're on demand." [11:15](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=675s)
> "would give me a confident June state answer, which would be wrong." [8:43](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=523s)
Source: AI OS ([transcript][os]).

**9. Backtrack retrieval misses, then fix the route**
When the agent searches for ages, or says it has no access to something you know is there, don't just tell it not to let that happen again. Make it retrace what it did and where it looked, explain why it missed, and then update the routing or reorganise files based on what it found.
> "you searched, and help me figure out why you didn't find that data right away." [23:22](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=1402s)
> "Have it update the routing. Have it maybe even move stuff or reorganize stuff based on what it found when it was backtracking." [23:22](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=1402s)
Also: "number five is to backtrack" [22:51](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=1371s). Source: AI OS ([transcript][os]).
*Supporting:* a 5-minute search for a file he knows the location of means the architecture needs updating, [5:39](https://www.youtube.com/watch?v=8QQ_INxAhRs&t=339s) ([transcript](../i-turned-claude-into-the-ultimate-second-brain--8QQ_INxAhRs-transcript.md)).

## D. Building an expert brain

**10. Raw evidence vs derived brain**
Step one gathers everything the expert has said into one raw folder, one sub-folder per source (he used free YouTube caption tools, and a paid X API that cost about a dollar), with one agent per source in parallel and a written record of what was fetched so it can be checked. Raw text alone is too messy to search well, so an LLM compiles it into a wiki (Karpathy's LLM-wiki idea). The raw files are never edited; the wiki is the derived layer on top. Obsidian is only a viewer.
> "I told it to write down what it got, so that you can actually check it." [3:34](https://www.youtube.com/watch?v=bvGptCLDhyo&t=214s)
> "It's like finding a needle in a haystack." [3:34](https://www.youtube.com/watch?v=bvGptCLDhyo&t=214s)
> "The raw files don't get touched" [4:04](https://www.youtube.com/watch?v=bvGptCLDhyo&t=244s)
Also: crawl set-up [3:03](https://www.youtube.com/watch?v=bvGptCLDhyo&t=183s); Obsidian as the visual layer [4:34](https://www.youtube.com/watch?v=bvGptCLDhyo&t=274s). Source: Karpathy ([transcript][kb]).
*Supporting:* raw → wiki → index and log, shown step by step in [Karpathy's LLM Wiki Is Basically Cheating](../fable-5-karpathy-s-llm-wiki-is-basically-cheating--hQvwMj7IJe4-transcript.md), [8:38](https://www.youtube.com/watch?v=hQvwMj7IJe4&t=518s).

**11. The brain's pages: index, log, source pages, concepts and rules**
The wiki keeps an index and a log, has one page per thing the expert wrote or said, and topic pages (principles, rules, methods, how he explains, how he debugs). He also mentions a "hot page". **(inference)** In this repo that maps to `index.md` (current state, what's covered), `log.md` (history), `concepts.md` (ideas) and `rules.md` (operating rules), with the transcripts as the source pages.
> "keeps an index, keeps a log" [4:04](https://www.youtube.com/watch?v=bvGptCLDhyo&t=244s)
Also: page types [4:34](https://www.youtube.com/watch?v=bvGptCLDhyo&t=274s)–[5:04](https://www.youtube.com/watch?v=bvGptCLDhyo&t=304s); index, hot page and log updated on ingest [9:38](https://www.youtube.com/watch?v=bvGptCLDhyo&t=578s). Source: Karpathy ([transcript][kb]).
*Supporting:* the index and log let the AI "incrementally build and maintain this wiki" [9:38](https://www.youtube.com/watch?v=hQvwMj7IJe4&t=578s) ([transcript](../fable-5-karpathy-s-llm-wiki-is-basically-cheating--hQvwMj7IJe4-transcript.md)).

**12. Provenance and inference labels**
Rules are what make the agent think like the expert, not just recall him. Each rule must link to an exact quote and where it came from, so you can click through and check it. If there is no source, the agent must say it is inferring.
> "what makes it think like him instead of just knowing what he said in the past." [5:34](https://www.youtube.com/watch?v=bvGptCLDhyo&t=334s)
> "every rule has to connect with an exact quote from him and where it came from. Because we don't want Claude to just make things up." [5:34](https://www.youtube.com/watch?v=bvGptCLDhyo&t=334s)
> "if there is no source, the agent has to say explicitly that it's inferring" [6:34](https://www.youtube.com/watch?v=bvGptCLDhyo&t=394s)
Source: Karpathy ([transcript][kb]).

**13. Relational ingestion**
The wiki links pages to each other: every rule links to its sources and every source to the rules it supports, so you query a relationship map, not a pile of notes. Adding one new link via an ingest command writes a source page, updates every page that source touches, and updates the index, hot page and log. In his demo a rule that had one source got a second and was promoted to a real rule. He never edited the wiki by hand.
> "Every rule links back to the source that it came from" [5:04](https://www.youtube.com/watch?v=bvGptCLDhyo&t=304s)
> "it will update every page that post touches." [9:38](https://www.youtube.com/watch?v=bvGptCLDhyo&t=578s)
> "a rule that was sitting on the bench with one source behind it got its second source and became a real rule." [9:38](https://www.youtube.com/watch?v=bvGptCLDhyo&t=578s)
Also: relationships make querying work [4:04](https://www.youtube.com/watch?v=bvGptCLDhyo&t=244s). Source: Karpathy ([transcript][kb]).

## E. Turning knowledge into behaviour

**14. Specialist agents and skills**
The rules become two files. A sub-agent holds the rules, how it talks and the loop it runs on every task; being a separate Claude with its own context, it doesn't drag your whole conversation along. A skill (a slash command) is the entry point: it sends your question to the agent and grades the answer against a checklist, one line per rule. The same knowledge can then feed your other skills, agents and workflows.
> "it doesn't drag your whole conversation along with it." [6:34](https://www.youtube.com/watch?v=bvGptCLDhyo&t=394s)
> "grades the answer against a checklist, one line per rule" [7:05](https://www.youtube.com/watch?v=bvGptCLDhyo&t=425s)
> "I can wire that knowledge into my own skills and my own agents and my own workflows" [2:02](https://www.youtube.com/watch?v=bvGptCLDhyo&t=122s)
Source: Karpathy ([transcript][kb]).
*Supporting, a challenge:* in [I Deleted All My Claude Skills](../i-deleted-all-my-claude-skills-and-claude-got-smarter--XNQBCRcwXV4-transcript.md) he warns over-specific skills can hold newer models back and suggests "making versions of them that aren't as specific" [5:41](https://www.youtube.com/watch?v=XNQBCRcwXV4&t=341s). **(inference)** Make skills for repeatable procedures, but keep them short.

**15. Run gates: enforce verification, don't just ask for it**
A hook runs when the agent tries to finish its turn. If it wrote code it never ran, the hook blocks the answer and sends it back. Verification becomes a step the agent can't skip.
> "a little script that runs right when the agent tries to finish its turn." [7:35](https://www.youtube.com/watch?v=bvGptCLDhyo&t=455s)
> "if it wrote code and it never ran it, the hook will basically block the answer" [7:35](https://www.youtube.com/watch?v=bvGptCLDhyo&t=455s)
> "baking in like a verification loop." [7:35](https://www.youtube.com/watch?v=bvGptCLDhyo&t=455s)
Source: Karpathy ([transcript][kb]).
*Supporting:* "You verify yourself so that I don't have to verify." [9:15](https://www.youtube.com/watch?v=XNQBCRcwXV4&t=555s) ([transcript](../i-deleted-all-my-claude-skills-and-claude-got-smarter--XNQBCRcwXV4-transcript.md)).

**16. Real-world testing**
The last step is testing on real things. Teaching test: it writes down what done means first, builds the smallest version, predicts, runs, shows a broken version, then lists what it ran and which rule drove each move. Review test: "would the client accept this?" on a script that had passed Claude's own test; the agent predicted a crash on an emoji in a normal Windows terminal, ran it that way, and it crashed. It then trimmed what wasn't earning its place and proved the trimmed version behaved the same by running both side by side.
> "the last step, of course, is just to test it." [8:05](https://www.youtube.com/watch?v=bvGptCLDhyo&t=485s)
> "saying that it works was only true in one specific setting or terminal." [9:08](https://www.youtube.com/watch?v=bvGptCLDhyo&t=548s)
> "we make it test on things that are real." [10:08](https://www.youtube.com/watch?v=bvGptCLDhyo&t=608s)
Also: the emoji crash [8:37](https://www.youtube.com/watch?v=bvGptCLDhyo&t=517s). Source: Karpathy ([transcript][kb]).

## F. The point of it all

**17. Human understanding is the finish line**
The brain is not a voice clone or impression; it condenses how an expert thinks so you can talk to it until you understand. You can't be expert in everything, but you must understand what you ship, and your own system: he still finds his own files by hand to make sure he understands his OS. Team-wide AI OS sync is, for him, unsolved and a people and habit problem more than a tech one; mastering your own system first makes that easier.
> "you can outsource your thinking, but you cannot outsource your understanding." [10:08](https://www.youtube.com/watch?v=bvGptCLDhyo&t=608s) (Nate quoting Karpathy)
> "then I can just talk to it until I understand it." [2:02](https://www.youtube.com/watch?v=bvGptCLDhyo&t=122s)
> "I actually understand my own second brain" [18:51](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=1131s)
> "I don't think it's a tech problem. I think it's a people problem." [23:52](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=1432s)
Also: not an impression [0:31](https://www.youtube.com/watch?v=bvGptCLDhyo&t=31s); master your own systems first [24:23](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=1463s). Sources: Karpathy ([transcript][kb]), AI OS ([transcript][os]).
*Supporting:* for rolling an OS out to a team, "you have to learn it first" [33:13](https://www.youtube.com/watch?v=8QQ_INxAhRs&t=1993s) ([transcript](../i-turned-claude-into-the-ultimate-second-brain--8QQ_INxAhRs-transcript.md)).

---

## Limits and things to treat carefully
- **Karpathy's 7 teaching rules** (build it, first-order term first, predict-run-compare, and so on, [5:34](https://www.youtube.com/watch?v=bvGptCLDhyo&t=334s)–[6:34](https://www.youtube.com/watch?v=bvGptCLDhyo&t=394s)) are Karpathy's, relayed by Nate. They live in `context/working-rules.md`, not in Nate's rules here.
- **Counting slip:** he says "four steps" but also "six prompts" ([2:33](https://www.youtube.com/watch?v=bvGptCLDhyo&t=153s), [10:08](https://www.youtube.com/watch?v=bvGptCLDhyo&t=608s)). The method matters, not the count.
- **Claims to check:** Karpathy's job titles ([0:01](https://www.youtube.com/watch?v=bvGptCLDhyo&t=1s)–[0:31](https://www.youtube.com/watch?v=bvGptCLDhyo&t=31s)), the X API costing "about a dollar" ([3:03](https://www.youtube.com/watch?v=bvGptCLDhyo&t=183s)), model names such as Opus 4.8 ([9:13](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=553s)).
- **Promotion to ignore:** the Hyper Agent sponsor slot ([6:38](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=398s)–[7:41](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=461s)); free Skool and AI OS kit links ([1:04](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=64s), [2:02](https://www.youtube.com/watch?v=bvGptCLDhyo&t=122s)).

[os]: ../steal-my-exact-ai-os-setup-5-simple-tips--Ek1NBfnnTH0-transcript.md
[kb]: ../i-built-another-andrej-karpathy-using-claude--bvGptCLDhyo-transcript.md
