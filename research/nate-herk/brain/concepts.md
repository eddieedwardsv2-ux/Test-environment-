# Nate's brain: concepts

**Built from:** Ek1NBfnnTH0 (Steal My Exact AI OS Setup), DTCyvo6cC54 (Every Level of a Claude Second Brain Explained), bvGptCLDhyo (I Built Another Andrej Karpathy Using Claude), XNQBCRcwXV4 (I Deleted All My Claude Skills... And Claude Got Smarter), 0WDkwMxj13s (I Turned Claude Opus 4.8 Into My Entire AI Operating System), 8QQ_INxAhRs (I Turned Claude Into the Ultimate Second Brain), 9KOtMsZ9I28 (How to Build Codex Skills Better than 99% of People). All seven transcripts read in full.
**Date:** 2026-10-07 (built). When new transcripts are ingested, add their IDs here and merge or extend entries rather than duplicating them. Chapter links for the AI OS video are also in [README.md](../README.md#chapters).
**Rules for this file:** only what Nate says in these transcripts. Auto-caption mishearings are corrected in the explanations (e.g. "cloudmd" / "claw.md" / "Claude at MD" = CLAUDE.md, "school" = Skool, "Herku"/"Hercule"/"PERC 2" = Herc 2, his AI OS project, "codec"/"codeex" = Codex, "ex article" = X article). Quotes keep the caption wording.
**Tags:** `principle` = lasting idea · `preference` = his personal way · `claim to check` = products, prices, stats, model names, predictions.
**"Charlie's repo"** notes say where this repo already does the idea (see `AGENTS.md`).

---

## Nate's worldview in brief

Nate treats an AI OS as **plain folders and markdown files with a router on top**: the model is a swappable engine, and the lasting value is your own context, skills and routing, which any agent (Claude Code, Codex, Hermes) can read. He builds in order (context, connections, capabilities, cadence) and says pick the **simplest setup that removes a real pain**. He is relaxed about structure ("there's not a right way") but strict about **accuracy**: wrong answers are the only real failure, so audit regularly, make the AI backtrack when it misses something, verify its own work, and limit what it can touch with real permissions, not prompts. Skills are recipes that are never finished: reverse-engineer them from a good output, give each one job, and improve them every run.

---

## AI OS & routing

**1. CLAUDE.md is a router, not a system prompt** — Keep a little "who you are" at the top, then mostly a table saying where everything lives. If the AI doesn't know where something is, it won't search your whole project for it.
> "my cloudmd is essentially just a master routing file, just a master table of context." — [13:47](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=827s)
Also: [4:34](https://www.youtube.com/watch?v=DTCyvo6cC54&t=274s), [5:09](https://www.youtube.com/watch?v=8QQ_INxAhRs&t=309s).
`principle` · **Charlie's repo:** `AGENTS.md` "Where things live" table.

**2. The find-it-yourself test** — Think of something you made and try to find it in your file explorer by clicking through folders. If you can, an agent with routing rules probably can too. If the agent searches for minutes for something you'd find instantly, fix the structure.
> "see if you could find it without searching, without asking Claude" — [18:20](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=1100s)
Also: [5:39](https://www.youtube.com/watch?v=8QQ_INxAhRs&t=339s) ("architecture engineering").
`principle`

**3. The four Cs, in order** — Context (it knows your business), connections (it can reach live data like calendar or email), capabilities (skills), cadence (things run on a schedule while you're away). The first two are the second brain; the last two make it an OS.
> "each of these layers can't happen without the previous one." — [8:09](https://www.youtube.com/watch?v=0WDkwMxj13s&t=489s)
Also: [3:35](https://www.youtube.com/watch?v=8QQ_INxAhRs&t=215s).
`principle` (the framework name is his) · **Charlie's repo:** context is built (`context/`); connections are limited by the cloud setup (`context/environment.md`).

**4. Expertise vs situational context** — Expertise context (who you are, goals, rules) is needed every run, so it's preloaded. Situational context (one customer ticket, one meeting) is fetched just in time; keeping it loaded adds bloat and clashes.
> "expertise context is the rulebook, right? Your policies, your pre-loaded information that needs to be in every single run." — [5:38](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=338s)
`principle` · **Charlie's repo:** `AGENTS.md` stays short and points to detail files.

**5. Four ways context fails** — Poisoning (a false fact), bloat (too much to search), confusion (irrelevant or missing facts, so it guesses), clash (two sources disagree, e.g. an old and new refund policy). Poisoning is easiest to fix: fact-check, or put a human in the loop.
> "the four failure modes, poisoning, bloat, confusion, and clash." — [1:34](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=94s)
`principle`

**6. Tool-agnostic: it's just files and folders** — Keep CLAUDE.md and AGENTS.md as the same content so Claude Code and Codex both read it (CLAUDE.md can simply reference AGENTS.md). Then switching model or tool costs nothing.
> "They're essentially the exact same file. Just so Codex can read this one and Claude code can read this one." — [11:10](https://www.youtube.com/watch?v=DTCyvo6cC54&t=670s)
Also: [22:49](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1369s), [29:39](https://www.youtube.com/watch?v=8QQ_INxAhRs&t=1779s).
`principle` · **Charlie's repo:** `CLAUDE.md` imports `@AGENTS.md`, exactly his level-4 trick.

**7. One repo for everything, pushed to GitHub** — He keeps all projects (including big "other worlds" projects) under one folder so one push backs up and syncs everything, and the main OS can see it all. Client deliverables can live in a separate repo while the OS keeps internal notes about them.
> "push this main folder to GitHub and everything backs up." — [12:46](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=766s)
Also: [7:42](https://www.youtube.com/watch?v=8QQ_INxAhRs&t=462s), [21:21](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=1281s).
`preference` · **Charlie's repo:** one GitHub repo, but it's **public**, so private data stays out (his own rule; Nate also warns that data sent to Claude isn't private, [21:18](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1278s)).

**8. Permissions are keys, not prompts** — Assume that if an agent *can* do something, it will. "Never send emails" means nothing if it holds a send-email tool; use scoped, read-only keys instead. His team's agent once emailed a discount code to a huge list by mistake.
> "A prompt is never a permission layer." — [24:31](https://www.youtube.com/watch?v=8QQ_INxAhRs&t=1471s)
Also: [17:19](https://www.youtube.com/watch?v=0WDkwMxj13s&t=1039s) ("instructions are not the same as capabilities"), [32:43](https://www.youtube.com/watch?v=8QQ_INxAhRs&t=1963s).
`principle` (incident size: `claim to check`, see Contradictions)

---

## Second brain & LLM wiki

**9. Design for how you'll ask** — Decide how data will be retrieved before choosing how to store it, like shaping the ball to fit the hoop.
> "how it's going to be accessed and recalled determines the way that you put it in in the first place." — [2:32](https://www.youtube.com/watch?v=DTCyvo6cC54&t=152s)
`principle`

**10. Five levels: pick the lowest that fits** — 1: CLAUDE.md router + folders. 2: LLM wiki with indexes. 3: semantic (vector) search. 4: knowledge graph. 5: always-on, self-updating brain. Higher isn't better; different folders can sit at different levels. He runs mostly at level 2.
> "If there's not pain, then why create more?" — [4:04](https://www.youtube.com/watch?v=DTCyvo6cC54&t=244s)
Also: [12:11](https://www.youtube.com/watch?v=DTCyvo6cC54&t=731s), [28:53](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1733s).
`principle` (Gbrain, LightRAG, Pinecone etc.: `claim to check`) · **Charlie's repo:** level 1, with level-2 wikis under `research/`.

**11. The LLM wiki: raw files stay, the AI compiles pages** — Keep raw sources untouched; the AI writes linked pages, an index and a log, and updates every page a new source touches. Obsidian is only an optional viewer; he rarely opens it.
> "The raw files don't get touched, but the LLM basically reads through all of them and then links them together" — [4:04](https://www.youtube.com/watch?v=bvGptCLDhyo&t=244s)
Also: [9:38](https://www.youtube.com/watch?v=DTCyvo6cC54&t=578s).
`principle` · **Charlie's repo:** `research/nick-saraev/brain/` (index, log, concepts) and the `brain-ingest` skill.

**12. Vector search is not magic** — Search by meaning chops documents into chunks, so "summarise the March 5th meeting" or "best sales week" may only see a few pieces. For whole-document questions, a plain markdown file the AI reads in full is more accurate.
> "a vector database was some magic solution where it could always pull back what you need, but that is very false." — [16:44](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1004s)
`principle`

**13. Store evergreen data; fetch changing data** — Only ingest what you'd still want in a year (decisions, priorities). Emails, Slack and customer data change weekly, so give the brain access to look them up instead of copying them in.
> "the way that I like to think about my actual second brain is stuff that I'm not going to delete." — [27:23](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1643s)
`principle` · **Charlie's repo:** `decisions.md` is an append-only evergreen log.

**14. The real bottleneck is getting it out of your head** — Before blaming retrieval, check whether your files hold the nuance you carry around. His "grill me" skill (adapted from Matt Pocock) interviews him 15–30 questions deep and saves a brainstorm file.
> "sometimes it seems like the bigger problem is getting everything out of your brain into the system." — [22:18](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1338s)
Also: [27:07](https://www.youtube.com/watch?v=8QQ_INxAhRs&t=1627s).
`principle` (the skill itself: `preference`) · **Charlie's repo:** no grill-me skill yet.

**15. Clone an expert in four steps** — Crawl their public content (one agent per source, in parallel), compile it into an LLM wiki, distil rules that each cite an exact quote (or say "inferring"), then wrap it in an agent and skills and test on real tasks.
> "every rule has to connect with an exact quote from him and where it came from." — [5:34](https://www.youtube.com/watch?v=bvGptCLDhyo&t=334s)
Also: [10:08](https://www.youtube.com/watch?v=bvGptCLDhyo&t=608s).
`principle` (twitterapi.io "about a dollar": `claim to check`) · **Charlie's repo:** `nick-brain` agent, `brain-ingest` and `teach` skills; this file follows the quote rule.

---

## Skills, agents & Codex

**16. A skill is a recipe with one job and one trigger** — A skill is a markdown file: a short header (name, when to use it) plus instructions. Break work down to single tasks ("leaves" of the tree) so each skill fires reliably on its own trigger.
> "have a skill with one very specific job, you can give it one very specific trigger" — [6:05](https://www.youtube.com/watch?v=9KOtMsZ9I28&t=365s)
Also: [0:32](https://www.youtube.com/watch?v=9KOtMsZ9I28&t=32s) (pancake recipe).
`principle` · **Charlie's repo:** `.claude/skills/` each have one named job.

**17. Reverse-engineer skills from a good output** — Do the task once end to end (or hand it a finished example), then ask the AI what it did, used and asked, and turn that into the skill. A skill can also be just a prompt you keep retyping, like his session-handoff summary.
> "I think it's so much easier to run the process, get the output and say, "Okay, let's turn that into a skill."" — [3:03](https://www.youtube.com/watch?v=9KOtMsZ9I28&t=183s)
Also: [20:51](https://www.youtube.com/watch?v=0WDkwMxj13s&t=1251s), [21:54](https://www.youtube.com/watch?v=0WDkwMxj13s&t=1314s), [17:54](https://www.youtube.com/watch?v=8QQ_INxAhRs&t=1074s).
`principle`

**18. Set the freedom level** — Rule-based jobs (copy cells into a CRM) get exact step-by-step instructions. Judgement jobs (write an article) get the goal and standard, not steps, or the output turns generic.
> "can I automate this using rules? Hard rules, hard logic." — [6:36](https://www.youtube.com/watch?v=9KOtMsZ9I28&t=396s)
Also: [8:14](https://www.youtube.com/watch?v=XNQBCRcwXV4&t=494s) (Boris Cherny: describe task, guardrails, exit criteria).
`principle`

**19. Build verification into every skill** — Have the agent (or a second agent) check the output and loop until it passes, and ask for a QA report proving it. Objective checks are countable ("10 screenshots"); subjective ones need a described standard (AI as judge).
> "If you assigned that task to a human, what would you do to basically give it the stamp of approval?" — [12:12](https://www.youtube.com/watch?v=9KOtMsZ9I28&t=732s)
Also: [9:09](https://www.youtube.com/watch?v=9KOtMsZ9I28&t=549s), [28:09](https://www.youtube.com/watch?v=8QQ_INxAhRs&t=1689s), [7:35](https://www.youtube.com/watch?v=bvGptCLDhyo&t=455s) (a hook that blocks "done" until code has run).
`principle` ("75 or 80" vs "95%" quality figures: `claim to check`) · **Charlie's repo:** run-gate hook in `.claude/settings.json` runs `tools/audit.py` before an agent may finish.

**20. Walk it down the model list, then the effort level** — Once a skill works on the strongest model, try cheaper ones and lower effort; keep the cheapest that still meets the standard. Test on several examples: in his demo a cheap model beat a mid one.
> "keep finding basically the simplest model or the lightest and cheapest model that still executes at the level of quality that you're looking for." — [13:43](https://www.youtube.com/watch?v=9KOtMsZ9I28&t=823s)
`principle` (model names Astra, Sol, Terra, Luna and their ranking: `claim to check`)

**21. The bike method: earn trust, never "finished"** — Like teaching a kid to ride, start with your hand on the handlebars, give feedback after every run, update the skill, and only slowly remove supervision. Automate on a schedule only once a skill is battle-tested, and still own it.
> "Almost every single time I run a skill, I give it feedback and I tell it to update." — [14:13](https://www.youtube.com/watch?v=9KOtMsZ9I28&t=853s)
Also: [17:49](https://www.youtube.com/watch?v=0WDkwMxj13s&t=1069s), [23:00](https://www.youtube.com/watch?v=8QQ_INxAhRs&t=1380s), [18:24](https://www.youtube.com/watch?v=8QQ_INxAhRs&t=1104s).
`principle`

**22. Assembly-line sessions and cheap helpers** — Do research, drafting and polishing in separate sessions (clear between them) so context doesn't blur, and send parallel grunt work to cheaper sub-agents that return one summary.
> "I like to bring outputs and chain them together and have different specialized agents." — [19:56](https://www.youtube.com/watch?v=8QQ_INxAhRs&t=1196s)
Also: [22:30](https://www.youtube.com/watch?v=8QQ_INxAhRs&t=1350s).
`preference` · **Charlie's repo:** `.claude/agents/` (video-tutor, nick-brain).

**23. Don't hobble newer models** — Boris Cherny suggests deleting CLAUDE.md, skills and hooks periodically to see what the model does unaided. Nate tested it: keep the routing and brand preferences, but make task skills less prescriptive.
> "it's less in my mind about deleting all your skills, it's more about really thinking about them" — [5:41](https://www.youtube.com/watch?v=XNQBCRcwXV4&t=341s)
Also: [2:04](https://www.youtube.com/watch?v=XNQBCRcwXV4&t=124s), [4:06](https://www.youtube.com/watch?v=XNQBCRcwXV4&t=246s).
`principle` ("deleted over 80% of the system prompt": `claim to check`)

---

## Keeping it accurate (audits)

**24. Have AI audit itself, read-only** — Weekly or monthly, have the AI check every routing rule, index and data feed against what's really on disk, then report a fix list *without changing anything* until you approve. It was an audit that suggested splitting his wikis.
> "have AI audit itself." — [16:49](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=1009s)
Also: [1:04](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=64s), [9:43](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=583s), [9:40](https://www.youtube.com/watch?v=0WDkwMxj13s&t=580s) (`/insights` report).
`principle` · **Charlie's repo:** `tools/audit.py`; Nate's own OS-audit skill is parked in `context/current-focus.md`.

**25. Backtrack, then fix the routing** — When the AI misses something it should have found, make it retrace where it looked and why it failed, then update routing or move files. That beats "don't let it happen again". Also: automate refreshes of regularly updated data (stale static data gave his AI an old subscriber count), and split knowledge into separate wikis as areas grow.
> "And that works a lot better than just saying, "Make no mistakes. Don't let that happen again." — [23:22](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=1402s)
Also: [19:51](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=1191s) (crons), [20:51](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=1251s) (segment), [12:17](https://www.youtube.com/watch?v=8QQ_INxAhRs&t=737s), [32:12](https://www.youtube.com/watch?v=8QQ_INxAhRs&t=1932s).
`principle` · **Charlie's repo:** the backtrack rule is in `AGENTS.md`; knowledge is split per creator under `research/`.

---

## Mindset

**26. No single right way; wrong answers are the only failure** — Don't copy any creator's folder layout. He edits his CLAUDE.md almost daily and moves folders weekly.
> "Don't stress it, because there's not a right way." — [11:10](https://www.youtube.com/watch?v=0WDkwMxj13s&t=670s)
Also: [18:20](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=1100s), [6:34](https://www.youtube.com/watch?v=DTCyvo6cC54&t=394s).
`principle`

**27. Context is king; default to your OS** — Everyone has the same models, so your context is the edge. Do everything (writing, brainstorming, not just code) inside the OS so it keeps learning; accept a short-term dip.
> "Everyone has access to the same AI models. So, if the AI is king, then wouldn't everybody be king? Context is king." — [4:37](https://www.youtube.com/watch?v=0WDkwMxj13s&t=277s)
Also: [2:35](https://www.youtube.com/watch?v=8QQ_INxAhRs&t=155s), [24:25](https://www.youtube.com/watch?v=0WDkwMxj13s&t=1465s) ("20% dip").
`principle`

**28. Take advice from people who work like you** — Boris and Karpathy build harnesses and train models; most viewers do knowledge work. Test advice on your own work before applying it wholesale.
> "you should probably be taking advice from people who are using the AI systems the same way you want to." — [6:11](https://www.youtube.com/watch?v=XNQBCRcwXV4&t=371s)
`principle`

**29. Outsource thinking, never understanding** — Use AI as a thought partner and let agents argue as devil's advocate, but keep your own judgement: models tend to be sycophants.
> "you can outsource your thinking, but you cannot outsource your understanding." — [10:08](https://www.youtube.com/watch?v=bvGptCLDhyo&t=608s)
Also: [11:16](https://www.youtube.com/watch?v=XNQBCRcwXV4&t=676s), [24:57](https://www.youtube.com/watch?v=0WDkwMxj13s&t=1497s), [26:37](https://www.youtube.com/watch?v=8QQ_INxAhRs&t=1597s).
`principle` (quote is Karpathy's, via Nate) · **Charlie's repo:** the `teach` skill.

**30. North Star filter; teams are a people problem** — Only add features that move a monthly goal (he skipped building a dashboard). Team-wide brains fail on habits and adoption, not tools, so master your own first.
> "I don't think it's a tech problem. I think it's a people problem." — [23:52](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=1432s)
Also: [26:58](https://www.youtube.com/watch?v=0WDkwMxj13s&t=1618s), [29:54](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1794s).
`principle`

---

## Contradictions or changed views

- **"I deleted all my skills" — he didn't.** The title says so, and he opens with "more skills and more system prompts are probably breaking your system" ([0:01](https://www.youtube.com/watch?v=XNQBCRcwXV4&t=1s)), but he tested on a duplicate repo and says "I didn't actually go out and sweep delete all of my stuff" ([6:41](https://www.youtube.com/watch?v=XNQBCRcwXV4&t=401s)). Elsewhere skills are "my number one favorite feature" ([7:11](https://www.youtube.com/watch?v=8QQ_INxAhRs&t=431s)) and one skill was iterated "25 or more times" ([5:05](https://www.youtube.com/watch?v=9KOtMsZ9I28&t=305s)). Net view: rework, don't delete.
- **Be specific vs don't over-specify.** Rule-based skills should be "step one do this, step two" ([7:37](https://www.youtube.com/watch?v=9KOtMsZ9I28&t=457s)), while Boris says step-by-step is "really not the way" ([8:14](https://www.youtube.com/watch?v=XNQBCRcwXV4&t=494s)). The freedom-level idea (18) reconciles them; that's our reading.
- **"Who cares about benchmarks" vs model-launch videos.** He says "Who cares Opus 4.8 benchmarks?" ([4:37](https://www.youtube.com/watch?v=0WDkwMxj13s&t=277s)), yet whole videos are built around new models. His model feelings also shift: 4.8 feels like 4.6 ([2:04](https://www.youtube.com/watch?v=0WDkwMxj13s&t=124s)); later Opus 5 felt "degraded" and he went back to 4.8 ([1:34](https://www.youtube.com/watch?v=XNQBCRcwXV4&t=94s)).
- **Slack and email in the brain?** His OS "can read through my Slack threads" ([2:04](https://www.youtube.com/watch?v=0WDkwMxj13s&t=124s)) but he says not to ingest that kind of data ([27:23](https://www.youtube.com/watch?v=DTCyvo6cC54&t=1643s)). Reconcilable: access, not storage.
- **Visual hook vs "I hardly ever open Obsidian"** ([9:38](https://www.youtube.com/watch?v=DTCyvo6cC54&t=578s)–[10:08](https://www.youtube.com/watch?v=DTCyvo6cC54&t=608s)). He admits the visuals are there to hook viewers.
- **Level slip:** while sitting at level two he says he hasn't felt enough pain "to switch over to level two" ([12:11](https://www.youtube.com/watch?v=DTCyvo6cC54&t=731s)); presumably means level three.
- **Email incident size drifts:** "over 150,000 inboxes" ([15:48](https://www.youtube.com/watch?v=0WDkwMxj13s&t=948s)) vs "150,000, 200,000 people" ([24:31](https://www.youtube.com/watch?v=8QQ_INxAhRs&t=1471s)).
- **Team brains:** "I don't have a great answer" ([23:52](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=1432s)) vs a later "Uh yes", everyone builds their own ([33:13](https://www.youtube.com/watch?v=8QQ_INxAhRs&t=1993s)). Possibly a changed view.
- **Karpathy's job:** "one of Anthropic's lead engineers" vs "on the pre-training team" ([0:01](https://www.youtube.com/watch?v=bvGptCLDhyo&t=1s)–[0:31](https://www.youtube.com/watch?v=bvGptCLDhyo&t=31s)). `claim to check`.

---

## Promotion to ignore

- **Sponsor: Hyperagent** (built by the Airtable team), with "$1,000 in free credits" via his link ([6:38](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=398s)–[7:41](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=461s)).
- **Free Skool group as a funnel:** the OS-audit skill, grill-me, session handoff, AIOS course, GitHub repo and AI OS kit are all "in my free school community" ([1:04](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=64s), [7:37](https://www.youtube.com/watch?v=DTCyvo6cC54&t=457s), [6:08](https://www.youtube.com/watch?v=0WDkwMxj13s&t=368s), [10:45](https://www.youtube.com/watch?v=8QQ_INxAhRs&t=645s), [2:02](https://www.youtube.com/watch?v=bvGptCLDhyo&t=122s)). His own flywheel says free feeds paid AIS Plus and coaching ([12:47](https://www.youtube.com/watch?v=8QQ_INxAhRs&t=767s)). Useful resources, but check before installing.
- **Free "first automation client" SOP** with AIS Plus results claims ([8:07](https://www.youtube.com/watch?v=9KOtMsZ9I28&t=487s)–[8:38](https://www.youtube.com/watch?v=9KOtMsZ9I28&t=518s)).
- **His book "Becoming AI Native"** ([5:35](https://www.youtube.com/watch?v=9KOtMsZ9I28&t=335s)) and **second channel** ([26:25](https://www.youtube.com/watch?v=9KOtMsZ9I28&t=1585s)).
- **Credentials as authority:** subscriber counts, "41 videos in 2024, 261 videos in 2025", 13-person team, $200/month plan ([12:17](https://www.youtube.com/watch?v=8QQ_INxAhRs&t=737s)–[13:17](https://www.youtube.com/watch?v=8QQ_INxAhRs&t=797s), [31:10](https://www.youtube.com/watch?v=8QQ_INxAhRs&t=1870s)). Unverified.
- **Model hype:** Fable/Mythos pricing and availability dates ([0:01](https://www.youtube.com/watch?v=8QQ_INxAhRs&t=1s)–[1:04](https://www.youtube.com/watch?v=8QQ_INxAhRs&t=64s)) are launch-day claims. Tools named in passing (Fireflies, ClickUp, Modal, twitterapi.io, Obsidian) are mentions, not endorsements to rely on.
