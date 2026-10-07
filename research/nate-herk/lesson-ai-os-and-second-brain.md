# Lesson: Organising an AI OS / second brain (Nate Herk, two videos)

Sources:
- **AI OS** = [Steal My Exact AI OS Setup (5 simple tips)](https://www.youtube.com/watch?v=Ek1NBfnnTH0) (2026-07-23). Links go to the nearest **chapter**; the transcript now has exact timestamps if you want the precise second.
- **Second Brain** = [Every Level of a Claude Second Brain Explained](https://www.youtube.com/watch?v=DTCyvo6cC54) (2026-06-17). Links go to the exact moment.

Everything below comes from the transcripts unless marked *(tutor's note)*.

---

## 1. The big idea in 3 sentences

A "second brain" is just folders of plain text files that you and your AI can both find things in. It's "just files and folders" ([Second Brain 1:32](https://www.youtube.com/watch?v=DTCyvo6cC54&t=92s)). The most important file is CLAUDE.md, and it should work like a **map that says where things live**, not a giant instruction manual. Most AI mistakes come from badly organised context, so keep the always-needed facts small, look up the changing facts only when you need them, and pick the **simplest level** of system that fixes a problem you actually have.

---

## 2. Glossary

| Term | Plain meaning |
|---|---|
| **Context** | Everything the AI has in front of it while it answers: your message, files it has read, instructions. |
| **Context window** | The AI's working memory for one chat. It has a limit, and quality drops as it fills ("context rot"). |
| **CLAUDE.md** | A file Claude Code reads automatically at the start of every session in that folder. |
| **AGENTS.md** | The same idea for Codex and other tools. Nate keeps a copy of CLAUDE.md under this name. |
| **Router / routing file** | A file that says "for X, look in folder Y". Like a contents page. |
| **AI OS (AI operating system)** | Nate's name for his whole setup: files, skills, connections and automations working together. |
| **Second brain** | The memory part of an AI OS: your saved notes, decisions and knowledge. |
| **Skill** | A saved set of instructions Claude can run on request (e.g. "audit my setup"). |
| **Hallucination** | When the AI confidently makes something up. |
| **Markdown (.md)** | Plain text with simple formatting (`#` for headings). What all of this is written in. |
| **LLM wiki** | A folder of linked markdown pages that the AI writes and keeps up to date from your raw material. Credited to Andrej Karpathy. |
| **Index** | A page listing what's in a folder or wiki, so the AI knows where to start. |
| **Obsidian** | A free app that shows markdown files as linked notes and a graph. Optional. |
| **Semantic search** | Searching by *meaning* rather than exact words ("feedback" finds "test results"). |
| **Vector database / embeddings** | How semantic search works: text is cut into chunks and each chunk is stored as numbers that represent its meaning. |
| **Knowledge graph** | Stores things *and how they're related* ("Jordan works at Acme"). |
| **Cron** | A timer that runs a job on a schedule (e.g. every Monday at 9am). |
| **Sub-agent** | A helper AI that Claude sends off to do one part of a job. |
| **Human in the loop** | A person checks something before the AI acts on it. |

---

## 3. Key ideas

**1. CLAUDE.md is a router, not a rulebook.**
Nate's top-level CLAUDE.md is "almost purely" a routing table: "if you need this, you go here" ([AI OS, Tips chapter 11:56](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=716s)). Claude is "not just going to go search your entire code base automatically", so if it doesn't know where something lives, it won't find it ([Second Brain 4:34](https://www.youtube.com/watch?v=DTCyvo6cC54&t=274s)). Set up properly, "you will stop having to re-explain things" ([5:04](https://www.youtube.com/watch?v=DTCyvo6cC54&t=304s)).
*Analogy:* the job sheet pinned in the van that says "paint in the back left, dust sheets under the seat". It doesn't hold the paint. It tells you where to find it.

**2. The four ways context fails** ([AI OS, chapter 1:38](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=98s))

| Failure | What happens | Trade analogy | Fix Nate gives |
|---|---|---|---|
| **Poisoning** | A false fact is in the files, so the AI repeats it confidently | A wrong measurement written on the plan | Fact-check it, cross-check it, or have a person check it. "The easiest to fix." |
| **Bloat** | So much data that the AI can't pick out what matters ("needle in the haystack") | A van so rammed you can't find the one tool you need | Keep expertise and situational context apart (idea 3) |
| **Confusion** | Facts are irrelevant or missing, so the AI fills the gap with a guess | A customer's vague brief, so you guess the colour | Make sure the right facts exist and are routed to |
| **Clash** | Two sources disagree (March: "always refund", June: "never refund") | Two versions of the quote, and you don't know which the customer signed | Remove or clearly date old versions |

**3. Expertise vs situational context, which the second video calls context vs connections.**
- **Expertise** (called *context* in the second video) is what's needed every time: who you are, your goals, your rules. It goes in CLAUDE.md. It's "the rulebook" ([AI OS, chapter 4:34](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=274s)).
- **Situational** (called *connections*) is looked up "just in time": one customer ticket, last week's Slack chat. Keeping it loaded all the time adds "bloat and confusion".
- In the second video he says changing data like emails and Slack threads should *not* be copied into the second brain, "because that's just noise". The test is: "in a year, will it be good for me to have this memory in here?" ([Second Brain 27:23](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1643s)). The brain should still know *where to go and get it* ([27:53](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1673s)).
*Analogy (Nate's):* the head teacher knows how a classroom should run (expertise). The class teacher knows which pupil needs to sit at the front today (situational).

**4. Start with the end in mind.**
Organise data by *how you'll ask for it later*: "how it's going to be accessed and recalled determines the way that you put it in" ([Second Brain 2:32](https://www.youtube.com/watch?v=DTCyvo6cC54&t=152s)). His example is that you wouldn't make a square basketball for a round hoop.

**5. The five levels** ([overview 3:02](https://www.youtube.com/watch?v=DTCyvo6cC54&t=182s))

| Level | Question it answers | What it is | Link |
|---|---|---|---|
| 1 | Can I find it by an exact word or name? | CLAUDE.md as router + a few folders (context, projects, decisions log) | [4:04](https://www.youtube.com/watch?v=DTCyvo6cC54&t=244s) |
| 2 | Can I pull everything on one topic together? | Add an LLM wiki, references and a memory file | [8:07](https://www.youtube.com/watch?v=DTCyvo6cC54&t=487s) |
| 3 | Can I find it using different words than I wrote? | Semantic (meaning) search with a vector database | [12:41](https://www.youtube.com/watch?v=DTCyvo6cC54&t=761s) |
| 4 | Can I follow a chain of relationships? | Knowledge graph | [19:16](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1156s) |
| 5 | Can it run without me thinking about it? | Always-on, self-updating (e.g. Garry Tan's Gbrain) | [25:22](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1522s) |

Key points:
- "Find the simplest level or the lowest level that actually fits your needs … If there's not pain, then why create more?" ([4:04](https://www.youtube.com/watch?v=DTCyvo6cC54&t=244s)).
- Nate runs nearly everything at **level 2** himself ([12:11](https://www.youtube.com/watch?v=DTCyvo6cC54&t=731s)). He doesn't use knowledge graphs day to day ([19:47](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1187s)) or Gbrain ([25:52](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1552s)).
- Different folders can sit at different levels ([28:48](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1728s)).
- Vector search is not magic. It only reads *chunks*, so "summarise the March 5th meeting" or "which week had the highest sales" can come back wrong. A plain markdown file read in full is more accurate there ([16:14](https://www.youtube.com/watch?v=DTCyvo6cC54&t=974s)).

*Analogy:* tools in the van. You don't buy a mini digger (level 4) to plant one shrub. A spade (level 1) does it.

**6. The LLM wiki (level 2).**
Raw material goes in (for Nate, YouTube transcripts) and Claude Code "auto-creates" linked pages for concepts, sources and techniques ([8:38](https://www.youtube.com/watch?v=DTCyvo6cC54&t=518s)). Each wiki has an **index**, so the AI starts there and drills down ([11:41](https://www.youtube.com/watch?v=DTCyvo6cC54&t=701s)). Obsidian only *displays* the files: "I hardly ever open Obsidian" ([9:38](https://www.youtube.com/watch?v=DTCyvo6cC54&t=578s)). The links work like "see also" references. They are not a true knowledge graph ([12:41](https://www.youtube.com/watch?v=DTCyvo6cC54&t=761s)).
*Analogy:* a well-labelled filing cabinet with a contents card on the front of each drawer.

**7. The five tips** ([AI OS, chapter 11:56](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=716s))
1. **CLAUDE.md as a router** (idea 1). Flat or nested folders both work. "All that matters is that you have the right routing rules in place."
2. **Have AI audit itself.** Weekly or monthly, ask it to "open up every file, look through my routing rules, and just make sure that everything's still accurate". Nate's own test: can you find a file yourself *without searching*? If you can, an agent can too.
3. **Automate data that updates on a schedule.** If you keep asking it to pull the same thing (e.g. every Monday's meeting), set up a cron.
4. **Segment knowledge.** Once a topic keeps growing, give it its own folder or wiki. He split one wiki into "YouTube transcripts" and "meeting transcripts", which made answers quicker, more accurate and cheaper. Client work: keep internal notes in the OS, and keep client-facing deliverables in a separate repo.
5. **Backtrack.** When it misses something it should have found, don't just say "don't do that again". Make it retrace where it searched, explain why it missed it, and then *fix the routing*.

*Analogy for tip 5:* after a snagging issue, you don't just say "be more careful". You work out which step went wrong and change the method.

**8. Getting it out of your head is the hard part.**
"Sometimes the bigger problem is getting everything out of your brain into the system" ([22:18](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1338s)). He uses a "Grill Me" skill (from Matt Pocock) that interviews him until it knows a topic ([20:18](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1218s)).

**9. Privacy.**
Anything you process with Claude goes to Anthropic, "so that's not private". He says you might not want to send client data, and could use open-source models instead ([21:18](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1278s)).

**Features checked against official docs** ([code.claude.com/docs/en/memory](https://code.claude.com/docs/en/memory), 2026-10-07):
- ✅ Auto memory exists and is toggled in `/memory` ([10:39](https://www.youtube.com/watch?v=DTCyvo6cC54&t=639s)). It's stored on the machine (`~/.claude/projects/<project>/memory/`), so **cloud sessions lose it**: keep anything important in the repo.
- ✅ `@AGENTS.md` inside CLAUDE.md imports that file ([22:49](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1369s)). The docs recommend this: shared instructions in AGENTS.md, CLAUDE.md imports them. This repo now does exactly that.
- The model name "Opus 4.8" in the demo is just the model he used in July; not important.

---

## 4. Principle vs preference vs promotion

| Lasting principle | Nate's personal preference | Promotion / sponsor |
|---|---|---|
| CLAUDE.md routes; it isn't a dumping ground | One giant "Herk 2" folder pushed to GitHub ("this works for me right now") | **Hyperagent** sponsor segment (AI OS video) |
| Four failure modes: poisoning, bloat, confusion, clash | Two separate wikis (YouTube, meetings) | Free **OS audit** skill, **Grill Me** skill and "7-day challenge" in his free Skool group |
| Always-needed vs just-in-time context | Staying at level 2; not using graphs or Gbrain | Paid Skool tier / agency (per README) |
| Pick the lowest level that solves real pain | Folders called brainstorms, projects, other worlds, brand assets | Affiliate links in descriptions (Glaido, Hostinger, per README) |
| Design for how you'll ask later | Keeping CLAUDE.md and AGENTS.md as identical copies | |
| If you can't find it by hand, nor can the AI | Feeding his business data to Claude (he accepts the privacy trade-off) | |
| Make the AI backtrack, then fix the routing | Visual tools (Obsidian, LightRAG) are optional | |
| Team syncing is "a people problem", not a tech one | | |

---

## 5. What this means for Charlie

**Where you are:** level 1, with `research/` as a small level-2 wiki. That's the right fit. *(Updated by the main session after this lesson was drafted: the "do now" steps below are already done.)*

**Your pain point matches level 1 exactly.** Nate's guide says: "If you were re-explaining your setup … look at level one" ([28:53](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1733s)). You keep re-explaining yourself between chats, so you need better **routing**, not a fancier system.

**Already done (2026-10-07):**
- ✅ CLAUDE.md rewritten as a router, with a "Where things live" table.
- ✅ `context/` (about-me, how-i-learn, current-focus, environment), `decisions.md`, `projects/youtube-channel/`, `learning/flashcards.md`.
- ✅ `research/README.md` as the wiki index, plus one README per creator.
- ✅ The router lives in AGENTS.md (Codex reads it); CLAUDE.md imports it with `@AGENTS.md` (one source of truth, so they never drift).

**Keep doing:** use the backtrack trick whenever Claude says it can't find something you know is there, and add a dated line to `decisions.md` when you change direction.

**Do later (and the trigger for each):**
- **Level 2 / LLM wiki:** when you have about 30+ notes and keep forgetting what's in them (Nate's own threshold, [28:53](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1733s)). Your creator research will get there. Then give "creator research" its own wiki with an index (tip 4: segment).
- **Monthly self-audit (tip 2):** once you have 3+ creator folders. For now, a one-line prompt is enough. You don't need Nate's skill.

**Skip for now, and why:**
- **Vector search, knowledge graphs, Gbrain (levels 3–5):** they fix pains you don't have yet. Nate barely uses them himself, and they add cost and complexity.
- **Crons / automations (tip 3):** you have no data that arrives on a schedule yet. Also, transcript fetching is rate-limited and blocked on cloud servers (see CLAUDE.md).
- **Obsidian:** optional eye candy. Revisit when the Mac arrives, if you fancy the graph view.
- **Team syncing:** you're a team of one.

**WARNING: your repo is PUBLIC.** Anyone on the internet can read every file in it. Nate flags privacy even for *private* setups ([21:18](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1278s)). For you it's stricter:
- No client names, addresses, phone numbers, quotes or invoices from trade work. No personal details you wouldn't put on a YouTube video. No API keys (CLAUDE.md already says keys go in an environment secret).
- Keep `about-me.md` to things you'd say on camera.
- If you ever need private notes, keep them in a separate **private** repo, or off GitHub entirely, and route to them only by name.
- Remember: deleting a file later doesn't remove it from git history.

---

## 6. Flashcards

1. **Q:** What is Nate's main job for CLAUDE.md? **A:** A router: it says where things live, rather than holding everything.
2. **Q:** Name the four context failure modes. **A:** Poisoning, bloat, confusion, clash.
3. **Q:** Which failure mode is easiest to fix, and how? **A:** Poisoning. Verify facts (cross-check, or have a person check).
4. **Q:** Old policy says "always refund", new one says "never". Which failure is that? **A:** Clash.
5. **Q:** Expertise vs situational context? **A:** Expertise is always needed and lives in CLAUDE.md. Situational is looked up just in time.
6. **Q:** The second video's names for those two? **A:** Context (expertise) and connections (situational).
7. **Q:** Which level should you choose? **A:** The lowest one that fixes a real pain point.
8. **Q:** What level does Nate mostly run at? **A:** Level 2 (routing + LLM wikis).
9. **Q:** Why can vector search give a bad meeting summary? **A:** It only pulls a few similar chunks, never the whole transcript.
10. **Q:** What does "backtrack" mean? **A:** Make the AI retrace why it missed something, then fix the routing.

---

## 7. Practice task (under 20 minutes): test the router

Nate's test: if the system is organised well, both **you** and a **fresh AI** can find things without being told.

1. **You, without searching:** in the GitHub app or website, open this repo and find (a) your flashcards and (b) Nate's second-brain transcript by clicking through folders only. Time yourself.
2. **A fresh AI:** start a **brand-new** Claude Code session on this repo and ask, with no other explanation: *"What am I working on right now, where would notes on a new creator go, and how do I fetch a transcript?"*
3. If either test fails, tell the AI to **backtrack** (tip 5) and fix the routing.

**Done when:** you found both files in under a minute each, and the new session answered all three questions correctly from the files alone.

**Now:** do step 1.

---

### Parking Lot
- Codex: confirm which file it reads (AGENTS.md?) and whether `@file` references work.
- Check Claude Code's `/memory` and auto memory against the official docs.
- A "Grill Me" style interview to write `about-me.md` (on-camera details only).
- Possible YouTube episode: "A tradesman's van-sheet for AI: CLAUDE.md as a router."
- Level 2 wiki for creator research once there are about 30 notes.
