# Nate's rules: AI OS architecture

**What this is:** operating rules for building and running an AI OS or expert brain, distilled from Nate Herk transcripts (two primary, the rest supporting) so the `architect` advisor can check a plan against them. They are rules about *systems*, not an imitation of Nate.
**Sources:** primary **AI OS** = Ek1NBfnnTH0 ([transcript][os]); **Karpathy** = bvGptCLDhyo ([transcript][kb]). Supporting: DTCyvo6cC54, 8QQ_INxAhRs, hQvwMj7IJe4, XNQBCRcwXV4, and from 2026-10-07 3XIGcM7VICc, bCljOfCH8Ms (2h course), c0kaKxM2pHg (grill me), LrgfmZkl3nc, yysILVsfLFM, 0WDkwMxj13s, 9KOtMsZ9I28, jdbOVepEtUE (6h course), RzLV8sfFdMM, e18sdZLwP7o, kB9iMD0EjT8, HIRDzMtuWFk, 9hetShMMp2s, zKBPwDpBfhs. Rules 31-40 come from 35 more transcripts (2026-10-08 full-channel audit; codes in `system/standard-ai-os-v1.md`). Rule 41 comes from oz2CwrPV2Rg (2026-10-08). Rules 42-43 come from 13 more newest transcripts (2026-10-08: model tests, a Codex automations tutorial and a guest interview with Dave of Glido, l8y). Each quote links to its video; transcripts are `../<title>--<id>-transcript.md`. When videos disagree the newer wins (order: `../videos.md`, smaller # = newer).
**Confidence:** **stated** = Nate says it · **demonstrated** = he shows it working on screen · **inference** = our reading, not said or shown.
**Built:** 2026-10-07. Concept numbers refer to [concepts.md](concepts.md); new rules name concepts in brackets until numbered.
Updated 2026-10-08: +13 newest transcripts (Rules 42-43 added; Rule 41 gained a second source; Also lines on 17, 26, 33, 35, 37, 39).
Updated 2026-10-08: +35 transcripts (Rules 31-40 added).
Updated 2026-10-07: +14 transcripts (Rules 19-30 added; Rules 2, 4, 5, 7, 11, 15, 16, 17 gained support).

---

**Rule 1: Name the failure mode before fixing** (stated: the four modes; inference: naming one before any fix)
A wrong answer is poisoning, bloat, confusion or clash. Each has a different fix, so name it first.
> "the four failure modes, poisoning, bloat, confusion, and clash." [1:34](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=94s)
**Agent check:** *Which of the four is this: false fact, too much loaded, something missing, or two sources disagreeing?* (Concept 1)

**Rule 2: Fix poisoning with verification, not hope** (stated)
Cross-check facts against a live source or a search; if the agent isn't sure, put a human in the loop.
> "poisoning is the easiest one to fix because basically it's just a matter of having some verification." [2:36](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=156s)
> Also: "Never accept AI output without asking why" [6:37](https://www.youtube.com/watch?v=bCljOfCH8Ms&t=397s)
**Agent check:** *Where does this fact get checked before it's used?*

**Rule 3: One current source per fact** (inference)
Nate describes clash (old and new policies side by side, [4:07](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=247s)) but gives no fix in these videos (none of the 14 added on 2026-10-07 gives one either, so this stays inference). Our rule: when a fact changes, update or retire the old copy rather than adding a second one; history goes in a log, not beside the current state.
**Agent check:** *Is this fact written anywhere else? Which one wins?*

**Rule 4: Always-loaded is for expertise only** (stated)
Load who you are, goals and policies every run. Fetch one-off, situational data just in time.
> "the situational context is things that you need just in time." [5:38](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=338s)
> Also: "I said don't read from the wiki unless you actually need it." [2:20:23](https://www.youtube.com/watch?v=bCljOfCH8Ms&t=8423s); "cloudmd is the rules. Memory is, you know, learned facts." [2:04:50](https://www.youtube.com/watch?v=jdbOVepEtUE&t=7490s)
**Agent check:** *Is this needed on every run? If not, route to it instead of loading it.* (Concept 2)

**Rule 5: The root file routes; it doesn't store** (stated, demonstrated)
Keep CLAUDE.md / AGENTS.md to a short identity plus a table of where things live.
> "I treat this almost purely as a router." [12:46](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=766s)
> Also: "I go into a routing map and that's the majority of my agents.mmd" [6:07](https://www.youtube.com/watch?v=yysILVsfLFM&t=367s); "it's an index, not a dump" [5:34](https://www.youtube.com/watch?v=LrgfmZkl3nc&t=334s)
Shown on screen at [13:17](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=797s). *Supporting:* [4:34](https://www.youtube.com/watch?v=DTCyvo6cC54&t=274s) ([transcript](../every-level-of-a-claude-second-brain-explained--DTCyvo6cC54-transcript.md)).
**Agent check:** *Could this paragraph be a file plus one routing line?* (Concept 3)

**Rule 6: Judge the layout by whether things can be found, not by copying someone** (stated)
Any structure is fine if you can find things by hand without search; the only failure is ignoring repeated wrong answers.
> "see if you could find it without searching, without asking Claude" [18:20](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=1100s)
**Agent check:** *Could Charlie guess this file's path without searching?* (Concept 4)

**Rule 7: Audit read-only, then wait for approval** (demonstrated)
The audit reports findings and fixes into a dated file and changes nothing until you say yes. For big projects, one sub-agent per check.
> "It won't actually do anything yet." [1:04](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=64s)
> Also: "Maybe every single Friday, you run an audit" [2:28:30](https://www.youtube.com/watch?v=bCljOfCH8Ms&t=8910s)
Fix list "await approval" at [8:43](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=523s); fan-out at [10:14](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=614s).
**Agent check:** *Does this audit only report? Who approves the fixes?* (Concept 7)

**Rule 8: Treat every index and route as a claim to check against the disk** (stated, demonstrated)
Check that routes point to things that exist, that nothing is misrouted, that index counts match reality, and that feeds are fresh.
> "Indexes and wiks are claims about what exists and what's current. The audit checks every claim against reality." [9:43](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=583s)
Demo: 55 folders in the index vs 79 on disk, [8:12](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=492s); freshness grades, [11:15](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=675s).
**Agent check:** *Which claims in this index could a script check? Which feeds have a last-updated date?* (Concepts 7, 8)

**Rule 9: Segment knowledge that is distinct and growing** (stated, demonstrated)
Split it into its own wiki or folder so the agent searches less.
> "the more you can segment stuff out, the better." [20:21](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=1221s)
Claude suggested his own split, [17:19](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=1039s).
**Agent check:** *Is this folder mixing two kinds of growing material? Would splitting it narrow the search?* (Concept 5)

**Rule 10: Automate what arrives on a schedule** (stated)
If you keep asking for the same pull, make it a cron or routine.
> "Build automations to update data." [18:51](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=1131s)
**Agent check:** *Has Charlie asked for this same fetch again and again? Then schedule it.* (Concept 6)

**Rule 11: Backtrack every miss, then fix the route** (stated)
Have the agent explain where it looked and why it missed, then update the routing or move files. Just telling it not to let that happen again is weaker.
> "Have it update the routing." [23:22](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=1402s)
> Also: "every time you correct AI, you feed that correction back into the system" [6:37](https://www.youtube.com/watch?v=3XIGcM7VICc&t=397s); "update the skill in the smallest durable place" [6:05](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=365s)
**Agent check:** *Where did it look, why did it miss, and what line in the router changes?* (Concept 9)

**Rule 12: Raw evidence stays untouched; the brain is derived from it** (demonstrated)
Keep transcripts and posts as-is in raw files; build the wiki pages on top and record what was fetched.
> "The raw files don't get touched" [4:04](https://www.youtube.com/watch?v=bvGptCLDhyo&t=244s)
**Agent check:** *Is anyone editing a raw transcript? Is there a record of what was fetched?* (Concept 10)

**Rule 13: No source, no rule; label inference** (stated, demonstrated)
Every rule links to an exact quote and where it came from; unsourced reasoning says it is inferred.
> "if there is no source, the agent has to say explicitly that it's inferring" [6:34](https://www.youtube.com/watch?v=bvGptCLDhyo&t=394s)
**Agent check:** *Can each claim be clicked back to a timestamp?* (Concept 12)

**Rule 14: Ingest relationally** (demonstrated)
A new source updates every page it touches plus the index and log. A one-source rule is provisional until a second source backs it.
> "it will update every page that post touches." [9:38](https://www.youtube.com/watch?v=bvGptCLDhyo&t=578s)
**Agent check:** *Which concepts and rules does this new source change? Did index and log get updated?* (Concepts 11, 13)

**Rule 15: Turn distilled knowledge into an agent plus a skill** (demonstrated)
The agent holds the rules and runs in its own context; the skill is the entry point and grades answers against the rules.
> "So, those are the two things we have, a Karpathy agent and a Karpathy skill." [7:05](https://www.youtube.com/watch?v=bvGptCLDhyo&t=425s)
*Supporting, a challenge:* keep skills less specific so they don't hold newer models back, [5:41](https://www.youtube.com/watch?v=XNQBCRcwXV4&t=341s) ([transcript](../i-deleted-all-my-claude-skills-and-claude-got-smarter--XNQBCRcwXV4-transcript.md)).
> Also: "They could literally just be a 50line markdown file." [1:25:34](https://www.youtube.com/watch?v=bCljOfCH8Ms&t=5134s)
*Newer wins:* XNQ is #54 in upload order; the newer 9KO (#16) and HIR (#22) still build skills, now with verification loops and trigger tests (Rules 16, 21), so read XNQ as "less specific", not "no skills".
**Agent check:** *Is there already an agent or skill for this? Is the new one short?* (Concept 14)

**Rule 16: Enforce verification with a gate** (demonstrated)
A hook that blocks "done" until the check has run beats a reminder in the prompt.
> "it's a step that we have to make sure that the agent can't skip" [7:35](https://www.youtube.com/watch?v=bvGptCLDhyo&t=455s)
> Also: "every single skill that I build works in some sort of verification loop" [9:40](https://www.youtube.com/watch?v=9KOtMsZ9I28&t=580s)
**Agent check:** *What stops the agent claiming this works without running it?* (Concept 15)

**Rule 17: Test in the real setting before trusting it** (stated, demonstrated)
Define done first, test on real tasks and the real environment, and try to break it. "It works" may only be true where it was tried.
> "saying that it works was only true in one specific setting or terminal." [9:08](https://www.youtube.com/watch?v=bvGptCLDhyo&t=548s)
> Also: "You have to define what done looks like before you even start building." [12:40](https://www.youtube.com/watch?v=3XIGcM7VICc&t=760s); "Before returning the final output, define the acceptance criteria." [8:05](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=485s); "does this answer like a teammate" [12:44](https://www.youtube.com/watch?v=bCljOfCH8Ms&t=764s)
> Also: "fixing just one example doesn't prove the whole agent is reliable" [5:06](https://www.youtube.com/watch?v=QDsenEcAJIk&t=306s); "I don't think that just giving Astra seven trading days was enough to really know if this is a viable strategy." [17:22](https://www.youtube.com/watch?v=eg_1NXDcoPk&t=1042s) (Concept 41)
**Agent check:** *Where was this tested? On Charlie's real device and real data?* (Concepts 16, 41)

**Rule 18: Human understanding is the finish line** (stated)
The system should leave Charlie understanding what he built and how his OS is laid out, not just holding output.
> "you can outsource your thinking, but you cannot outsource your understanding." [10:08](https://www.youtube.com/watch?v=bvGptCLDhyo&t=608s) (Nate quoting Karpathy)
> "I actually understand my own second brain" [18:51](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=1131s)
**Agent check:** *Could Charlie explain this change in his own words?* (Concept 17)

**Rule 19: Keep the router under 200 lines** (stated)
*Replaced by Rule 41 (2026-10-09, Charlie's choice on the Decision Desk).*
*Newer wins:* the aim is no longer a line count but Rule 41, the smallest context that works ("minimal doesn't necessarily mean short"). A router can be longer when the extra lines are things only Charlie can supply; 200 lines stays only as the hard ceiling `tools/audit.py` errors at. Quotes kept below as history.
It is re-read with every message, so every line costs on every turn; past the limit it gets ignored.
> "So keep it under 200 lines." [5:36:27](https://www.youtube.com/watch?v=jdbOVepEtUE&t=20187s)
> Also: "if it grows too big, it can start to get messy and feel ignored" [5:04](https://www.youtube.com/watch?v=DTCyvo6cC54&t=304s)
**Agent check:** *Use Rule 41's check instead.* (Concept 18, now part of Concept 39)

**Rule 20: Register every new skill or folder in the router, and log it** (stated)
A skill or folder the router doesn't mention is one the agent won't find; the decision to add it goes in the log.
> "It's going to register the skill in claw.md and it's going to log its decisions." [1:30:08](https://www.youtube.com/watch?v=bCljOfCH8Ms&t=5408s)
> Also: "you're going to just want to make sure that your claused file is getting updated as well" [28:34](https://www.youtube.com/watch?v=bCljOfCH8Ms&t=1714s)
**Agent check:** *Is the new skill routed and logged with a date?* (Concept 3)

**Rule 21: Skill descriptions are triggers: user's words, no overlap, trigger-tested** (stated)
Write the description in the words Charlie would say, make sure no two skills compete, then test obvious, reworded and unrelated requests.
> "Put the words a real person would use inside the description and make sure two skills aren't competing for the same request." [4:02](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=242s)
> Also: "The first one is an obvious request that should trigger it." [4:33](https://www.youtube.com/watch?v=HIRDzMtuWFk&t=273s)
**Agent check:** *Which other skill could fire on this request? Did a reworded request trigger it?* (Concept 21)

**Rule 22: Validate skill and agent front matter** (stated)
A small syntax slip such as an unclosed quote stops a skill or agent firing, silently; check it with a script.
> "You have to close off the quotes if you open them up" [2:37:42](https://www.youtube.com/watch?v=jdbOVepEtUE&t=9462s)
**Agent check:** *Does the front matter have a name, a description and a closing `---`?* (Concept 21)

**Rule 23: New skills report only until battle-tested** (stated)
A new skill proposes and asks; it earns permission to act on its own after many good runs.
> "Once we've ran the skill 10, 20, 30 times and we've kind of like battle tested it and we feel more confident in it, then we can maybe make it a little bit more autonomous." [1:47:37](https://www.youtube.com/watch?v=jdbOVepEtUE&t=6457s)
**Agent check:** *How many times has this skill run? Should it still wait for a yes?* (Concept 22)

**Rule 24: Sub-agents for bulky output, read-only by their tools, and not overused** (stated)
Send context-heavy searches to a sub-agent; limit its tools rather than asking nicely; skip it for quick or dependent steps.
> "is this about to dump a pile of stuff into my chat that I'll never read again?" [2:43:47](https://www.youtube.com/watch?v=jdbOVepEtUE&t=9827s)
> Also: "you can put that so that these sub-agents are explicitly read-only" [7:10](https://www.youtube.com/watch?v=e18sdZLwP7o&t=430s); "if you're forcing too many sub agents, you're going to get worse results" [24:57](https://www.youtube.com/watch?v=e18sdZLwP7o&t=1497s)
**Agent check:** *Would this output flood the main chat? Is the sub-agent's tool list read-only?* (Concept 23)

**Rule 25: Block risky actions with settings and keys, not prompts** (stated)
A deny list in settings or a least-privilege key physically stops the action; an instruction in a prompt only asks.
> "A prompt is never a permission layer." [24:31](https://www.youtube.com/watch?v=8QQ_INxAhRs&t=1471s)
> Also: "Can you help me update the settings file so that you physically cannot do those things?" [1:14:28](https://www.youtube.com/watch?v=jdbOVepEtUE&t=4468s)
**Agent check:** *What actually stops this action if the agent ignores the instruction?* (Concept 24)

**Rule 26: Secrets live in `.env`, never in chat or Git** (stated)
Put keys in an `.env` file excluded from pushes, not in the conversation history.
> "It's it's much more secure for you to paste in your API key into the ENV rather than you know giving it in the chat history" [41:50](https://www.youtube.com/watch?v=bCljOfCH8Ms&t=2510s)
> Also: "You don't want to paste it right in here into the chat thread, you want to paste it into the .env file." [2:35](https://www.youtube.com/watch?v=oWCcN6hSFjA&t=155s); "I like to put all my API keys in there so that if I ever need to move them over to cloud code or if I need to move them over to trigger.dev, I already have them in one spot" [8:38](https://www.youtube.com/watch?v=FqnNL8fnUWo&t=518s)
**Agent check:** *Is any key in the chat, a committed file or this public repo?* (Concept 25)

**Rule 27: Look at visual output before calling it done** (demonstrated)
For pages and apps, take a screenshot and check it; code that runs can still look broken.
> "we built a plan to add visual validation" [1:03:37](https://www.youtube.com/watch?v=bCljOfCH8Ms&t=3817s)
**Agent check:** *Has anyone looked at a screenshot of this on phone and desktop?* (Concept 16)

**Rule 28: Save every audit and read the last one first** (stated)
Dated reports in an audits folder let the next audit see what was found and whether it was fixed.
> "look for earlier reports inside of the audit folder" [10:14](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=614s)
**Agent check:** *Where is the last audit, and were its fixes done?* (Concept 7)

**Rule 29: Hand off and clear before context rots** (stated)
Clear between unrelated tasks; in long sessions write a hand-off (done, files, open decisions, next) and start fresh.
> "here's what we did. Here's the files that were created. Here are open decisions. Here's what's next." [22:24](https://www.youtube.com/watch?v=0WDkwMxj13s&t=1344s)
> Also: "Use slashclear between unrelated tasks." [5:30:53](https://www.youtube.com/watch?v=jdbOVepEtUE&t=19853s); "if we get past 250,000 300,000, I'm going to do a session handoff" [2:00:48](https://www.youtube.com/watch?v=jdbOVepEtUE&t=7248s)
**Agent check:** *Is this session still on one task? Is the next step written down for a fresh one?* (Concept 27)

**Rule 30: Extract knowledge by interview, not brain dump** (stated, demonstrated)
Have the agent ask one question at a time until it understands, and save the answers; a quick dump leaves gaps.
> "Interview me relentlessly about every aspect of this plan until we reach a shared understanding" [1:32](https://www.youtube.com/watch?v=c0kaKxM2pHg&t=92s)
> Also: "the bigger problem is getting everything out of your brain into the system" [22:18](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1338s)
**Agent check:** *Did this knowledge come from Charlie answering questions, and is it saved?* (Concept 26)

**Rule 31: Context costs money and rots: act at about half the window** (stated)
Every message re-reads the whole chat, so long chats cost more and get worse; check what fills the window and act at about half, not when auto-compact fires.
> "Claude rereads the entire conversation from the beginning, and all of those are tokens that it's charging you for" [1:04](https://www.youtube.com/watch?v=49V-5Ock8LU&t=64s)
> Also: "somewhere around halfway through your context window, it starts to fall apart." [4:32](https://www.youtube.com/watch?v=eRS3CmvrOvA&t=272s)
**Agent check:** *Is this chat past about half the window, and do we know what is filling it?* (Concept 29)

**Rule 32: Plan, let the AI attack the plan, then build** (stated)
Nate says plan first and have the AI play devil's advocate on the plan before building; save big plans to a file and work phase by phase. Charlie declined plan mode on 2026-10-08, so the 1-2 questions from the router stand in for it.
> "You ask Claude to start challenging you and pushing back and playing devil's advocate before it builds anything or before it approves any plan" [2:36](https://www.youtube.com/watch?v=iTY8Q449YNQ&t=156s)
> Also: "Have one for discovery where you can have Claude read through PDFs and read through the code base" [21:25](https://www.youtube.com/watch?v=_qZvORxGqI0&t=1285s)
**Agent check:** *Did we ask 1-2 questions or have the AI attack the plan before a big build?* (Concept 30)

**Rule 33: A separate checker decides "done"; then try to break it** (stated)
The worker doesn't mark its own homework: a different checker looks at it, then you stress test it for edge cases. When output is bad, ask whether it is the model, the tool or our own organisation.
> "Claude doesn't get to declare itself done. A different model has to look at it with a different persona" [22:25](https://www.youtube.com/watch?v=iTY8Q449YNQ&t=1345s)
> Also: "by the time it tells you it's done, you stress test it more. and you try to find those edge cases" [9:43](https://www.youtube.com/watch?v=iTY8Q449YNQ&t=583s)
> Also: "creating alignment between the human reviewer and the LLM." [38:04](https://www.youtube.com/watch?v=l8ywUsEJ2XQ&t=2284s) (a guest: an AI judge is trusted only after it agrees with a human); "spin up 50 different sub aents and have all of them test this thing, try to break it" [22:20](https://www.youtube.com/watch?v=FqnNL8fnUWo&t=1340s)
**Agent check:** *Who other than the builder checked this, and what did we try to break?* (Concepts 31, 41)

**Rule 34: Skills do one job, are built from a real run, and retire when they stop earning** (stated)
One skill, one job; build it by walking the AI through a real task first, then turn that into the skill. Retire any skill that no longer adds value.
> "the whole idea is that you want a skill to do one very specific job" [1:06:25](https://www.youtube.com/watch?v=X-pbJWKmwi0&t=3985s)
> Also: "The way that I build my skills is I have Claude Code do something with me. I walk it through the steps" [6:21:32](https://www.youtube.com/watch?v=mpALXah_PBg&t=22892s)
**Agent check:** *Does this skill do one job, come from a real run, and still earn its place?* (Concept 32)

**Rule 35: Unattended runs: one-shot, stateless, bounded, tested by hand first, fixed parts in scripts** (stated)
A scheduled job can't stop and ask, only sees the repo, APIs and secrets, and needs a bounded scope. Test it by hand and prove one live run before switching on the schedule; put fixed steps in a script so the agent can't drift.
> "You're not around. So, you probably want to make sure that it doesn't ever have to stop and ask you questions." [1:33](https://www.youtube.com/watch?v=ehg4fhydTgs&t=93s)
> Also: "the agent was just interpreting the message different every time and it just acted differently" [3:00:25](https://www.youtube.com/watch?v=X-pbJWKmwi0&t=10825s)
> Also: "I actually did this before where I had a routine that was very simple like this and after about a month, it started to just go rogue." [10:08](https://www.youtube.com/watch?v=FqnNL8fnUWo&t=608s); "every time an agent wakes up, it's going to leave some sort of handoff message" [1:31](https://www.youtube.com/watch?v=eg_1NXDcoPk&t=91s); "we want to have Codex do as much verification on it as possible." [9:38](https://www.youtube.com/watch?v=FqnNL8fnUWo&t=578s)
**Agent check:** *Could this run finish with nobody there, and was it tested by hand first?* (Concepts 33, 42)

**Rule 36: Permissions in layers: deny plus allow, start strict, helpers inherit, read-only and drafts first** (stated)
Deny the destructive commands and allow the safe ones; helpers inherit the main session's permissions; start read-only and draft-only with a human approving outward actions. Auto mode and bypass permissions are not adopted here.
> "go into your permissions and explicitly allow the commands that you know are safe" [14:07](https://www.youtube.com/watch?v=jqoFP9QapXI&t=847s)
> Also: "they inherit the permissions from the main session. So, if you're on bypass permissions, then all of your agents are going to be on bypass permissions" [12:11](https://www.youtube.com/watch?v=vDVSGVpB2vc&t=731s)
**Agent check:** *Which commands are denied, which allowed, and does the helper inherit the same limits?* (Concept 34)

**Rule 37: Check before anything goes public: security review, private-data hook, untrusted content, plugin vetting** (stated)
Run a security review before publishing, strip private data with a hook rather than a rule, treat web pages and transcripts as possibly hostile, and vet any plugin first.
> "I basically told it to run a security review and make sure that my API keys aren't exposed and that there's no vulnerabilities" [30:01](https://www.youtube.com/watch?v=saggDHHnmtQ&t=1801s)
> Also: "that there's a hook that fires to remove any PII, any sensitive data of that client that I don't want living on my GitHub." [23:59](https://www.youtube.com/watch?v=6LNlCpQPYFc&t=1439s)
> Also (a guest): "security breach that's one thing that you like cannot take back" [20:07](https://www.youtube.com/watch?v=l8ywUsEJ2XQ&t=1207s); "if you protect your secrets and your credentials you have rowle security on" [1:01:05](https://www.youtube.com/watch?v=l8ywUsEJ2XQ&t=3665s)
**Agent check:** *Has a security and private-data check run before this goes public?* (Concepts 35, 43)

**Rule 38: File hygiene: scratch apart from deliverables, folder READMEs, project first, start every task in the project** (stated)
Tell the AI where throwaway files go, give each folder a short README, keep everything in the project until it earns going global, and start tasks inside the project.
> "if we don't tell Claude how to organize its files, it's going to get messy quick to the point where I don't understand where things are" [7:08](https://www.youtube.com/watch?v=3GAxd90fEE4&t=428s)
> Also: "so that your agent always understands why does this folder exist and where should it look for different things" [1:32:56](https://www.youtube.com/watch?v=X-pbJWKmwi0&t=5576s)
**Agent check:** *Is scratch work kept apart from deliverables, and does the folder explain itself?* (Concept 36)

**Rule 39: Operator habits: paste the whole error, make it do its own chores, match model and effort, adopt tools only for real pain, cap parallel sessions, use the OS for everything** (stated)
Small habits: paste the full error, ask the AI to do chores it lists for you, use the cheapest model and effort that does the job, adopt a tool only for a real pain point, and keep to three or four parallel sessions.
> "this is the error that I got. And then I paste in all that messy stuff and shoot it off" [33:04](https://www.youtube.com/watch?v=saggDHHnmtQ&t=1984s)
> Also: "do not automatically run everything at maximum effort or even just high." [4:39](https://www.youtube.com/watch?v=FBVNS1l5Vb8&t=279s)
> Also: "they said to just start on medium and scale it up or down if you need." [7:10](https://www.youtube.com/watch?v=QCkHIyEPIYo&t=430s); "using Opus 5.5 as the orchestrator that spins up and sends off very specific instructions to a bunch of little GBD6 soul workers." [33:35](https://www.youtube.com/watch?v=eF3yeJuifoQ&t=2015s); "you're not using a slower and more expensive model to actually categorize all of those comments in the first place." [4:04](https://www.youtube.com/watch?v=ymgH8jS6Wb8&t=244s)
**Agent check:** *Is the model and effort matched to the task, and is this tool solving a real pain?* (Concepts 37, 40)

**Rule 40: Parts rot at different speeds; score each audit** (stated)
Different parts of the OS go stale at different rates, so review each at its own pace and keep a score from every audit to see whether the OS is improving.
> "All of these different parts decay, become obsolete or rot at different rates." [22:57](https://www.youtube.com/watch?v=6LNlCpQPYFc&t=1377s)
> Also: "it will store your scores every time so that you can see how you're actually improving your system" [53:15](https://www.youtube.com/watch?v=X-pbJWKmwi0&t=3195s)
**Agent check:** *Which part of the OS is stalest, and what did the last audit score?* (Concept 38)

**Rule 41: Smallest context that works; prune after every new model** (stated)
Keep what only you can supply (voice, goals, audience, how the work runs, the reason, the gotchas). Cut what the model can look up, anything said twice, and rules written for older models. Load one-job procedures only for that job, and re-audit the set-up whenever the model changes.
> "the best context is the smallest amount of context that gets you the highest quality result at the cheapest cost." [2:03](https://www.youtube.com/watch?v=oz2CwrPV2Rg&t=123s)
> Also: "every time a new model drops and you switch into it, you should probably just run this sort of audit anyways" [10:40](https://www.youtube.com/watch?v=oz2CwrPV2Rg&t=640s)
> Also (a second, guest source; Rule 41 no longer rests on one video): "the better models and harnesses get, the easier all the things that we have to do as developers get." [32:27](https://www.youtube.com/watch?v=l8ywUsEJ2XQ&t=1947s)
**Agent check:** *Is this line something only Charlie can tell it, or something it could find or no longer needs? Is it written anywhere else?* (Concept 39)

**Rule 42: Start at the lowest rung: the simplest build that works, fixed flows as code, more users means more care** (stated)
Build the simplest thing that does the job and move up only when you truly need to. A predictable flow is code run on a schedule or trigger, with AI only for the steps that need judgment; an agent loop is for work that must decide how often to look again. The more people rely on it, the more care it needs: a private tool is low stakes, a client's or the public's is not, and a leak cannot be undone.
> "build the simplest solution possible and only move up the sort of AI systems pyramid as I call it when you truly need that functionality." [29:24](https://www.youtube.com/watch?v=FqnNL8fnUWo&t=1764s)
> Also: "the more deterministic your automation gets, the more of a waste it would be to use codeex to host that." [6:07](https://www.youtube.com/watch?v=FqnNL8fnUWo&t=367s); "If there's not pain, then why create more?" [4:04](https://www.youtube.com/watch?v=DTCyvo6cC54&t=244s); a guest: "it gets more complex and the stakes are bigger." [14:29](https://www.youtube.com/watch?v=l8ywUsEJ2XQ&t=869s)
**Agent check:** *Could a fixed script do this instead of an agent? Who will rely on it, and what could not be undone if it went wrong?* (Concepts 42, 43, 20)

**Rule 43: Measure before you switch: same prompt, your own work, isolated, cost counted, known-right answers** (stated, demonstrated)
Before changing a model, effort level or prompt for real work, run the same task both ways in separate folders on your own examples and compare quality, time and cost. One result is not proof. For anything automated, keep a small golden set of known-right answers and re-run it after every change.
> "you got to get in there and you got to test it on your own skills and your own prompts and your own processes." [25:17](https://www.youtube.com/watch?v=7eo-11K2e3c&t=1517s)
> Also: "I put them in different work trees so they literally can't touch." [1:02](https://www.youtube.com/watch?v=GmLcJVzkxPA&t=62s); "What you're really going to want to do is run evals, meaning you're going to have a golden data set of 100 use cases and 100 correct answers" [12:43](https://www.youtube.com/watch?v=ymgH8jS6Wb8&t=763s)
**Agent check:** *Was the change tried on Charlie's real tasks, in isolation, with cost counted and a known-right answer to compare with?* (Concepts 40, 41)

---

## Inferring
Advice not backed by a quote here, in `concepts.md` or in a transcript must be labelled **(inference)**. Never invent quotes, timestamps or links. Rule 3 is inference only. Karpathy's 7 teaching rules are his, not Nate's; they live in `context/working-rules.md`.

[os]: ../steal-my-exact-ai-os-setup-5-simple-tips--Ek1NBfnnTH0-transcript.md
[kb]: ../i-built-another-andrej-karpathy-using-claude--bvGptCLDhyo-transcript.md
