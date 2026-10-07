# Lesson: how Nick Saraev thinks about learning and using AI

Sources (both read in full):
- **L** = [How I Learn Complex Skills & Difficult Subjects So Fast with AI](https://www.youtube.com/watch?v=FSXHk4hMrY8) (29:34)
- **C** = [I Spent $31,141 & 1,000 Hours On Claude Code To Learn This](https://www.youtube.com/watch?v=45K3zHckCnQ) (25:57)

---

## 1. The big idea in 3 sentences

You learn by **producing**: recalling, explaining and doing things yourself. Reading or being told is **consuming**, and it only *feels* like learning, so Nick uses AI mostly to make him produce (quiz him, question him, check him), not to explain. When he works with Claude Code he does the same thing. He doesn't trust the first answer, he makes the AI check its own work, he asks for a diagnosis before any fix, and he keeps its "working memory" clean and free of clutter.

---

## 2. Glossary

| Term | Plain meaning |
|---|---|
| Consumption vs production | Taking information in (reading, watching) vs getting it back out (recalling, explaining, doing). |
| Spaced repetition | Testing yourself on something at growing gaps (next day, 3 days, a week…) so it sticks. |
| Forgetting curve (Ebbinghaus) | The pattern of memory fading fast after you learn something unless you review it. |
| Anki | A free flashcard app that schedules spaced repetition for you. |
| Zone of proximal development | The "just out of reach" level where you learn most: not too easy, not too hard. |
| Deterministic | Same input, same output every time. AI models are **not**: the same prompt gives different answers. |
| Prompt | The instruction you type to the AI. |
| Evals (evaluations) | Running the same prompt many times and counting how often it works, e.g. 7 out of 10. |
| Meta-prompting | Asking the AI to help you *write* the prompt, instead of writing it all yourself. |
| Context window | How much the AI can "hold in its head" in one conversation. It fills up as you go. |
| Context rot | The AI getting worse as a conversation gets long and cluttered with old or contradictory instructions. |
| Token | A small chunk of text. It's how AI usage is measured and billed. |
| `/context`, `/compact`, `/btw`, `/init` | Claude Code slash commands: show what's filling memory, squash the conversation into a summary, ask a side question, create a starter CLAUDE.md. |
| MCP / connector / plugin | A plug-in link that lets the AI reach another service (Gmail, GitHub). MCP = Model Context Protocol, the standard underneath. |
| Skill | A saved, readable set of instructions for a task that Claude loads when needed. |
| Sub-agents | Helper AIs that Claude sends off to do separate parts of a job at the same time. |
| Fan out, fan in | Send lots of cheap helpers to gather information (fan out), then one strong model decides (fan in). |
| Handoff note | A short summary of where a job stands, used to start a fresh conversation cleanly. |
| CLAUDE.md / AGENTS.md | Instruction files the AI reads at the start of every session (Claude Code / Codex). |
| Symlink | A shortcut that makes two file names point at the same file. |

---

## 3. Key ideas

### Part A: How Nick learns (video L)

**1. Learning is production, not consumption.**
Most people think reading or watching is learning, but memory actually builds when you are "recalling things actively, predicting things actively, explaining things actively" ([L 1:02](https://www.youtube.com/watch?v=FSXHk4hMrY8&t=62s)). He quotes a study (unnamed): a week later, re-readers kept about 40% and people who tested themselves kept about 61% ([L 2:04](https://www.youtube.com/watch?v=FSXHk4hMrY8&t=124s)). *Check before relying on the exact figures. He doesn't name the study.*
*Analogy:* watching someone hang wallpaper on YouTube five times doesn't teach your hands. Hanging one wall badly does.

**2. Most people only use one of ten AI roles: the Explainer.**
Pasting something in and saying "explain this differently" is still passive reading. The other nine roles make *you* produce: Interviewer, Mapmaker, Socratic questioner, Examiner, Checker, Listener, Diagnostician, Sparring partner, Clerk ([L 2:35](https://www.youtube.com/watch?v=FSXHk4hMrY8&t=155s), [L 3:35](https://www.youtube.com/watch?v=FSXHk4hMrY8&t=215s)).
*Analogy:* using AI only to explain is like owning a full van of tools and only ever using the tape measure.

**3. Start with the Interviewer, then the Mapmaker.**
Before learning anything, say "ask me questions about my goal, my level" so the AI works out the *real* goal: "the goal is not actually learn coding, the goal is pass the interview" ([L 8:08](https://www.youtube.com/watch?v=FSXHk4hMrY8&t=488s)). Then get a map, because without one your energy goes into "the almost emotional anxiety of not knowing what you are going to do next" ([L 10:09](https://www.youtube.com/watch?v=FSXHk4hMrY8&t=609s)). Ask for the main parts, what depends on what, and "where people usually get stuck" ([L 11:10](https://www.youtube.com/watch?v=FSXHk4hMrY8&t=670s)).
*Analogy:* a site survey and a job sheet before you start, not turning up and seeing what happens.

**4. After being helped, redo it without help.**
This is the step "most people don't do". If AI explains it and you nod along, "you have merely read about that thing." Go back to the start and do it yourself. It costs about "10 or 15%" more time ([L 11:40](https://www.youtube.com/watch?v=FSXHk4hMrY8&t=700s), [L 12:42](https://www.youtube.com/watch?v=FSXHk4hMrY8&t=762s)).
*Analogy:* the apprentice watches the gaffer cut in a ceiling line, then does the next room alone.

**5. Make the AI question, quiz and grade you.**
- Socratic: "Don't just give me the answer. Ask me questions until I find what I don't know myself" ([L 14:13](https://www.youtube.com/watch?v=FSXHk4hMrY8&t=853s)).
- Examiner: "one question at a time. Make every question harder" ([L 15:13](https://www.youtube.com/watch?v=FSXHk4hMrY8&t=913s)).
- Checker: grade your *steps*, "Don't rewrite any of it" ([L 16:44](https://www.youtube.com/watch?v=FSXHk4hMrY8&t=1004s)).
- Listener: explain it in your own words (he speaks, sketches, then writes) and have AI grade it "against the source" ([L 17:45](https://www.youtube.com/watch?v=FSXHk4hMrY8&t=1065s)).
*Analogy:* a snagging inspection. Someone else walks the job and points at what you missed.

**6. Diagnostician: find the one root mistake.**
Repeated errors often share a single misunderstanding. Ask the AI to read your past attempts and say "what misunderstanding do all of these things have in common?" ([L 18:46](https://www.youtube.com/watch?v=FSXHk4hMrY8&t=1126s), [L 19:16](https://www.youtube.com/watch?v=FSXHk4hMrY8&t=1156s)).
*Analogy:* three rooms with flaking paint aren't three problems. It's one damp problem.

**7. Sparring partner and Clerk.**
Rehearse real situations (interviews, sales calls) against a tough AI, with a timer ([L 19:46](https://www.youtube.com/watch?v=FSXHk4hMrY8&t=1186s)). Use the Clerk to tidy *your own* notes into outlines or flashcards: "Don't add anything I didn't write", so "all of the thinking is your own" ([L 22:18](https://www.youtube.com/watch?v=FSXHk4hMrY8&t=1338s)).

**8. Work at your level, and find the best human explanations.**
Ask AI to quiz you easy-to-hard and "stop when I start guessing" to find your level ([L 23:21](https://www.youtube.com/watch?v=FSXHk4hMrY8&t=1401s)). Then ask it to find the best existing explanations for *your* level, because a perfect metaphor can save "days, weeks, or months" ([L 24:21](https://www.youtube.com/watch?v=FSXHk4hMrY8&t=1461s)).

**9. The case against AI: struggle is where learning happens.**
AI lets you skip the hard "hump", "and that leads to you ultimately remembering nothing". He compares it to GPS weakening your sense of direction. Watch for AI agreeing when you're half right, or inventing numbers and sources ([L 27:23](https://www.youtube.com/watch?v=FSXHk4hMrY8&t=1643s)). Don't fall into "the default way" people use it ([L 27:53](https://www.youtube.com/watch?v=FSXHk4hMrY8&t=1673s)).
*Analogy:* sat-nav gets you there but you never learn the roads.

### Part B: How Nick works with Claude Code (video C)

**10. Don't trust the first output. Measure it.**
The same prompt gives different results each time. Run it 10 times, count successes ("seven out of 10"), change the prompt, count again, keep the better one. "You're basically a scientist" ([C 0:33](https://www.youtube.com/watch?v=45K3zHckCnQ&t=33s), [C 2:35](https://www.youtube.com/watch?v=45K3zHckCnQ&t=155s)).
*Analogy:* one good coat from a new paint brand doesn't prove it. You'd want it to go on well on several walls.

**11. Give the AI a way to check its own work.**
One attempt is "just like you've only ever had a first draft". Give it something to compare against (a screenshot, an example, a test) and let it revise ([C 3:36](https://www.youtube.com/watch?v=45K3zHckCnQ&t=216s)).

**12. Let Claude write the prompt, and give a definition of done.**
Say what you want and ask Claude to help write the prompt. It will ask you questions ([C 6:36](https://www.youtube.com/watch?v=45K3zHckCnQ&t=396s)). Treat it "more like a contractor than an in-house employee": skip the step-by-step and say "you're done when this is true…" ([C 10:09](https://www.youtube.com/watch?v=45K3zHckCnQ&t=609s), [C 11:10](https://www.youtube.com/watch?v=45K3zHckCnQ&t=670s)).
*Analogy:* you tell a good plasterer "smooth, ready for paint by Friday". You don't tell him how to hold the trowel.

**13. Diagnose before you fix.**
Don't say "it's broken, fix it." Say "List all of the problems… Don't rewrite or do anything yet", cross out the ones you don't care about, then fix the rest ([C 11:41](https://www.youtube.com/watch?v=45K3zHckCnQ&t=701s)).
*Analogy:* a quote with an itemised list before any work starts.

**14. Protect the context window.**
About 30% can be used up "before I say anything" by built-in tools, connectors and skills. Long chats get pricier and "dumber" (context rot), so turn off unused connectors and skills ([C 8:07](https://www.youtube.com/watch?v=45K3zHckCnQ&t=487s), [C 9:07](https://www.youtube.com/watch?v=45K3zHckCnQ&t=547s)). When it drifts, ask it to summarise what's done, the decisions, what's next and open problems, correct that, and start fresh with it ([C 16:45](https://www.youtube.com/watch?v=45K3zHckCnQ&t=1005s)). Use `/btw` for side questions so they don't clutter the main job ([C 17:45](https://www.youtube.com/watch?v=45K3zHckCnQ&t=1065s)).
*Analogy:* a van loaded with every tool you own has no room for the job's materials. Load for today's job.

**15. Keep CLAUDE.md lean and current, and teach it fixes, not bans.**
Old info in CLAUDE.md led to bad advice (his out-of-date revenue figures) ([C 20:50](https://www.youtube.com/watch?v=45K3zHckCnQ&t=1250s)). Keep "a summary of what's where" plus preferences ([C 21:21](https://www.youtube.com/watch?v=45K3zHckCnQ&t=1281s)). When it makes a mistake, record the *solution* ("batch the file reads"), not just "don't do X". Ask it: "How could you have done that faster with fewer tokens?" ([C 23:53](https://www.youtube.com/watch?v=45K3zHckCnQ&t=1433s)).

**16. Keep a backup tool.**
Have Codex ready in the same folder, sharing the same instructions, so an outage doesn't stop you ([C 22:22](https://www.youtube.com/watch?v=45K3zHckCnQ&t=1342s)).

**Also in video C (advanced, for later):** start with an MCP connector to prove something works, then swap it for a lean custom skill ([C 12:42](https://www.youtube.com/watch?v=45K3zHckCnQ&t=762s)). Run separate, non-overlapping tasks in parallel with sub-agents ([C 14:43](https://www.youtube.com/watch?v=45K3zHckCnQ&t=883s)). Use fan out, fan in research with cheap models ([C 19:19](https://www.youtube.com/watch?v=45K3zHckCnQ&t=1159s)).

**One inconsistency to notice:** at [C 4:36](https://www.youtube.com/watch?v=45K3zHckCnQ&t=276s) he says skills "really are not the best way of doing things anymore" (he prefers keeping notes as comments inside the code). At [C 14:13](https://www.youtube.com/watch?v=45K3zHckCnQ&t=853s) he recommends turning connectors *into* lean skills. Read it as "skills shouldn't drift away from the real code", not "never use skills". That's our interpretation, not his words.

---

## 4. Principle vs preference vs promotion

| Claim | Type | Note |
|---|---|---|
| Learning = production, not consumption | **Principle** | Well-established learning science. His exact % figures: check before relying on them |
| Spaced repetition beats cramming | **Principle** | |
| Redo the task without help | **Principle** | |
| Use many AI roles, not just Explainer | **Principle** | The 10 role names are his framing |
| Struggle matters; AI can shortcut learning | **Principle** | GPS study is his summary. Check before quoting |
| AI output varies; test more than once | **Principle** | |
| Diagnose before fix; definition of done | **Principle** | |
| Long, cluttered chats get worse | **Principle** | Exact behaviour varies by model. Check before relying on it |
| Speak, then sketch, then write to self-test | Preference | "what I will typically do" |
| Compact "way earlier" than auto-compact | Preference | He also says compact has known issues "that might be fixed". Check docs |
| Prune MCPs to save 3–5 seconds startup | Preference | |
| Parallel tasks, accepting "slightly higher error rate" | Preference | Speed over accuracy is his business choice |
| Symlink CLAUDE.md to agents.md | Preference | Charlie's setup does the same job with an `@AGENTS.md` import |
| "Claude now understands agents.md" | **Product claim — verified** | True per the official docs (Claude Code v2.1.277+ reads AGENTS.md when there is no CLAUDE.md; this repo imports it instead). Checked 2026-10-07 |
| `/context`, `/compact`, `/btw`, `/init`, `/insights` | **Product claim** | Commands change. Check docs |
| Model names (Opus 5.5, Astra, Fable, Mythos), $31,141 spend, $400k/month business | **Product/self claims** | Check before relying on them. Not verifiable from the video |
| Maker School (90-day programme, money-back guarantee) | **Promotion** | His own paid product, at the end of both videos ([L 28:54](https://www.youtube.com/watch?v=FSXHk4hMrY8&t=1734s), [C 25:25](https://www.youtube.com/watch?v=45K3zHckCnQ&t=1525s)) |
| Sales-call sparring examples | Partly promotion | Tied to selling AI services, which his business teaches |

---

## 5. What this means for Charlie: your way vs Nick's way

### The comparison

| | Typical beginner, and what Charlie has done so far | How Nick thinks |
|---|---|---|
| Starting a topic | Asks a broad question ("how do I use Claude Code?") | Gets *interviewed* first, then gets a map of parts, order and sticking points |
| Learning style | Researches lots: more videos, more creators, more lessons | Consumption only *feels* like learning. Produce something after every input |
| When stuck | Asks AI to explain, nods, moves on | Asks for an explanation of *just the stuck bit*, then **redoes the whole thing without help** |
| Direction | Switches ideas when a new one appears | A plan, even an imperfect one, beats the anxiety of "what next?" |
| Tools | Collects tools and plugins (context7, superpowers, watch-video…) | Every connector and skill uses up memory and startup time. Turn off what you aren't using |
| Trusting output | Takes the first answer | Runs it again, compares, makes AI check its own work |
| Fixing things | "It's broken, fix it" | "List the problems, change nothing yet", then picks which to fix |
| Long chats | One endless conversation | Handoff note, then a fresh session |

### Where Nick overlaps with your setup (good news)
- **`context/how-i-learn.md` already uses Nick's ten roles, word for word.** Your tutor is meant to say "(Examiner mode)" and so on. You can ask for a role by name.
- **The learning loop** ("he attempts → check → feedback → practise again → revisit later") is Nick's production idea plus "redo without help" plus spaced repetition.
- **Flashcards (`learning/flashcards.md` + `flashcards-app.html`)** follow the spaced-repetition schedule (next day, 3 days, 1 week, 1 month). Nick suggests AI turn your mistakes into cards ([L 7:38](https://www.youtube.com/watch?v=FSXHk4hMrY8&t=458s)), and that's already a rule in your setup. Note: card 3 has a ❌. That's the system working.
- **AGENTS.md as a short router** matches Nick's "summary of what's where". **Codex sharing the same file** is his backup-tool idea, already done.
- **Parking Lot + one priority** is the Mapmaker cure for idea-switching.

### Where Nick pushes against your setup (be honest)
- **The research wiki risks becoming consumption.** Lessons like this one are the Explainer and Clerk doing the work. Reading them is input, so it doesn't count as learning until you produce something. Nick's Clerk rule ("all of the thinking is your own") isn't met when the AI wrote the notes.
- **The video-tutor agent stops at explaining.** It ends with a practice task, which is good, but nothing *tests* you afterwards. Add an Examiner or Listener step after every lesson.
- **The Parking Lot holds 4 plugins/tools.** Nick's advice says leave them there until a real task needs one.

### What to skip for now, and why
- **Evals with 10 runs, fan out/fan in, parallel sub-agents, MCP-to-skill conversion:** these are for people building repeated workflows for businesses. You have one project and no business data yet. A light version (below) is enough.
- **Sparring for sales calls:** that's tied to his paid programme. Sparring for *explaining on camera* is useful later for the channel.
- **The Diagnostician over 100 conversations:** you need a pile of mistakes first. Try it once you have 30+ flashcards with ❌ marks.

### 5 habit changes to start this week
1. **Redo without help.** After any task Claude walks you through (a commit, a branch, a new file), do it again from scratch on your own. Only then is it learned.
2. **Start every new topic with "Interview me first."** Instead of a broad question, say: *"Before you teach me anything about X, ask me questions about my goal and my level, one at a time."* Then: *"Map it: main parts, order, where beginners get stuck."*
3. **Produce after every input.** For each video or lesson you read, explain it in your own words (voice note on your iPhone is fine) and ask: *"Listener mode: grade this against the source and tell me exactly what I missed. Don't rewrite it."*
4. **Diagnose before fix, and a definition of done.** Say *"List the problems, change nothing yet,"* then pick which to fix. When you ask for work, end with *"Done when: …"*. (Your AGENTS.md already makes the AI do this for you. Now you do it for the AI.)
5. **No new tool until a task needs it.** Before installing any plugin or connector, write down the job it's for. If you can't name one, it goes in the Parking Lot.

---

## 6. Flashcards

| # | Question | Answer |
|---|---|---|
| 1 | Consumption vs production: which one builds memory? | Production: recalling, explaining, doing. Consumption only feels like learning. |
| 2 | What step does Nick say most people skip after AI explains something? | Redoing the whole task from the start without help. |
| 3 | Name Nick's first two roles for a brand-new topic. | Interviewer (finds your goal and level), then Mapmaker (makes the plan). |
| 4 | What does the Socratic questioner do differently from the Explainer? | It asks you questions until you find the gap yourself, instead of giving the answer. |
| 5 | Why shouldn't you trust Claude's first output? | AI isn't deterministic: the same prompt gives different results each time. |
| 6 | What is an eval, in Nick's simple version? | Run a prompt ~10 times, count how many worked, and compare after each change. |
| 7 | "Diagnose before fix": what do you say? | "List all the problems. Don't change anything yet." Then choose which to fix. |
| 8 | What is context rot? | The AI getting worse as a long chat fills with old or clashing instructions. |
| 9 | What goes in a handoff note? | What's done, decisions needed, what's next, open problems. Then start a fresh session. |
| 10 | When adding a lesson to CLAUDE.md, positive or negative? | Positive: write the fix to do, not just "don't do X". |

---

## 7. Practice task (about 15 minutes)

**Listener + Examiner on this lesson.** You'll produce, not consume.

1. Close this file. On your iPhone, record a 2-minute voice note explaining in your own words: (a) consumption vs production, (b) the "redo without help" step, (c) why you shouldn't trust the first output. Use the iPhone's dictation to turn it into text.
2. Paste the text into Claude with: *"Listener mode: grade my explanation against `research/nick-saraev/lesson-how-nick-thinks.md`. Tell me exactly what I missed or got wrong. Don't rewrite it."*
3. Then: *"Examiner mode: 5 questions on this lesson, one at a time, each harder than the last."*
4. Add every point you missed or got wrong as a new card in `learning/flashcards.md` (one fact per card).

**Done when:** you have recorded your own explanation, Claude has graded it, you've answered 5 Examiner questions, and at least one card from your own mistakes is in `learning/flashcards.md`.
