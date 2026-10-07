# Nate's rules: AI OS architecture

**What this is:** operating rules for building and running an AI OS or expert brain, distilled from Nate Herk's two primary videos so the `nate-brain` advisor can check a plan against them. They are rules about *systems*, not an imitation of Nate.
**Sources:** **AI OS** = Ek1NBfnnTH0 ([transcript][os]); **Karpathy** = bvGptCLDhyo ([transcript][kb]). Supporting transcripts are labelled *supporting*.
**Confidence:** **stated** = Nate says it · **demonstrated** = he shows it working on screen · **inference** = our reading, not said or shown.
**Built:** 2026-10-07. Concept numbers refer to [concepts.md](concepts.md).

---

**Rule 1: Name the failure mode before fixing** (stated: the four modes; inference: naming one before any fix)
A wrong answer is poisoning, bloat, confusion or clash. Each has a different fix, so name it first.
> "the four failure modes, poisoning, bloat, confusion, and clash." [1:34](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=94s)
**Agent check:** *Which of the four is this: false fact, too much loaded, something missing, or two sources disagreeing?* (Concept 1)

**Rule 2: Fix poisoning with verification, not hope** (stated)
Cross-check facts against a live source or a search; if the agent isn't sure, put a human in the loop.
> "poisoning is the easiest one to fix because basically it's just a matter of having some verification." [2:36](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=156s)
**Agent check:** *Where does this fact get checked before it's used?*

**Rule 3: One current source per fact** (inference)
Nate describes clash (old and new policies side by side, [4:07](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=247s)) but gives no fix in these videos. Our rule: when a fact changes, update or retire the old copy rather than adding a second one; history goes in a log, not beside the current state.
**Agent check:** *Is this fact written anywhere else? Which one wins?*

**Rule 4: Always-loaded is for expertise only** (stated)
Load who you are, goals and policies every run. Fetch one-off, situational data just in time.
> "the situational context is things that you need just in time." [5:38](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=338s)
**Agent check:** *Is this needed on every run? If not, route to it instead of loading it.* (Concept 2)

**Rule 5: The root file routes; it doesn't store** (stated, demonstrated)
Keep CLAUDE.md / AGENTS.md to a short identity plus a table of where things live.
> "I treat this almost purely as a router." [12:46](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=766s)
Shown on screen at [13:17](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=797s). *Supporting:* [4:34](https://www.youtube.com/watch?v=DTCyvo6cC54&t=274s) ([transcript](../every-level-of-a-claude-second-brain-explained--DTCyvo6cC54-transcript.md)).
**Agent check:** *Could this paragraph be a file plus one routing line?* (Concept 3)

**Rule 6: Judge the layout by whether things can be found, not by copying someone** (stated)
Any structure is fine if you can find things by hand without search; the only failure is ignoring repeated wrong answers.
> "see if you could find it without searching, without asking Claude" [18:20](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=1100s)
**Agent check:** *Could Charlie guess this file's path without searching?* (Concept 4)

**Rule 7: Audit read-only, then wait for approval** (demonstrated)
The audit reports findings and fixes into a dated file and changes nothing until you say yes. For big projects, one sub-agent per check.
> "It won't actually do anything yet." [1:04](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=64s)
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
**Agent check:** *Is there already an agent or skill for this? Is the new one short?* (Concept 14)

**Rule 16: Enforce verification with a gate** (demonstrated)
A hook that blocks "done" until the check has run beats a reminder in the prompt.
> "it's a step that we have to make sure that the agent can't skip" [7:35](https://www.youtube.com/watch?v=bvGptCLDhyo&t=455s)
**Agent check:** *What stops the agent claiming this works without running it?* (Concept 15)

**Rule 17: Test in the real setting before trusting it** (stated, demonstrated)
Define done first, test on real tasks and the real environment, and try to break it. "It works" may only be true where it was tried.
> "saying that it works was only true in one specific setting or terminal." [9:08](https://www.youtube.com/watch?v=bvGptCLDhyo&t=548s)
**Agent check:** *Where was this tested? On Charlie's real device and real data?* (Concept 16)

**Rule 18: Human understanding is the finish line** (stated)
The system should leave Charlie understanding what he built and how his OS is laid out, not just holding output.
> "you can outsource your thinking, but you cannot outsource your understanding." [10:08](https://www.youtube.com/watch?v=bvGptCLDhyo&t=608s) (Nate quoting Karpathy)
> "I actually understand my own second brain" [18:51](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=1131s)
**Agent check:** *Could Charlie explain this change in his own words?* (Concept 17)

---

## Inferring
Advice not backed by a quote here, in `concepts.md` or in a transcript must be labelled **(inference)**. Never invent quotes, timestamps or links. Rule 3 is inference only. Karpathy's 7 teaching rules are his, not Nate's; they live in `context/working-rules.md`.

[os]: ../steal-my-exact-ai-os-setup-5-simple-tips--Ek1NBfnnTH0-transcript.md
[kb]: ../i-built-another-andrej-karpathy-using-claude--bvGptCLDhyo-transcript.md
