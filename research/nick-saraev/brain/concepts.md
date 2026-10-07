# Nick's brain: concepts

**Built from:** FSXHk4hMrY8 (How I Learn Complex Skills… with AI), 45K3zHckCnQ (I Spent $31,141 & 1,000 Hours On Claude Code…), 638GQZ9UZ4w (Here's What I'd Learn Instead of AI Automation in 2027), x55Fj_syFcI (Why You Should Stop Listening To AI News), YIl-awY250k (What I'd Learn Instead of Automation in 2026), IJS08TVGut0 (I Found a Way To Use AI Agents Like Codex Completely For FREE). All six transcripts read in full.
**Date:** 2026-10-07 (built; refreshed same day, see [log.md](log.md)). When new transcripts are ingested, add their IDs here and merge or extend entries rather than duplicating them.
**Rules for this file:** only what Nick says in these transcripts. Auto-caption mishearings are corrected (e.g. "Claude at MD" / "Claude that MD" = CLAUDE.md, "sim link" = symlink, "A&N" = n8n, "Ghost TTY" = Ghostty, "Maker Square" = Maker School, "leak code" = LeetCode, "naden" = n8n, "school" = Skool, "Alex Ramosi" = Alex Hormozi, "Free buff" = Freebuff, "Nick Seraf" = Nick Saraev). Quotes keep the caption wording otherwise.
**Tags:** `principle` = lasting idea · `preference` = his personal way · `claim to check` = products, prices, stats, model names, predictions.

---

## Nick's worldview in brief

Nick sees learning as **production, not consumption**: you only really know something once you have recalled it, explained it or done it yourself, so AI is most useful when it makes you work (interviewing, quizzing, checking you), and harmful when it just hands you answers. He treats AI models as powerful but **non-deterministic contractors**: don't trust the first output, give them a definition of done and a way to check their own work, diagnose before fixing, and guard their context like a scarce resource. On careers, he thinks the **floor is always rising**: technical skill is being commoditised by agents, so the durable value is in sales, marketing, strategy and teaching others, and the safest place to stand is inside the industry doing the automating. He is candid that predictions past the near term are guesses.

---

## How to learn

**1. Learning is production, not consumption** — Reading, watching or being told only *feels* like learning. Memory is built by actively recalling, predicting, explaining and attempting things, which feels harder, so the brain avoids it. Using AI well means using it to make you produce. He cites an unnamed study: re-readers kept about 40% after a week, self-testers about 61%.
> "the way that human beings actually learn… is based off of production" — [1:02](https://www.youtube.com/watch?v=FSXHk4hMrY8&t=62s)
`principle` (40%/61% study figures: `claim to check`, study not named)

**2. Ten roles for AI, not just the Explainer** — Most people only use AI to explain things, which is still passive. He lists nine other roles that make you produce: Interviewer, Mapmaker, Socratic questioner, Examiner, Checker, Listener, Diagnostician, Sparring partner, Clerk.
> "most people will only have ever used one. They use the explainer role." — [2:35](https://www.youtube.com/watch?v=FSXHk4hMrY8&t=155s)
`principle` (the role names are his framing)

**3. Interview first, then map** — Before learning, have the AI question you about your goal and level, because your real goal is often narrower than you think (pass the interview, not "learn coding"). Then ask for a map: main parts, dependencies and where people get stuck. Without a plan, energy goes into anxiety about what to do next.
> "the goal is not actually learn coding, the goal is pass the interview." — [9:08](https://www.youtube.com/watch?v=FSXHk4hMrY8&t=548s)
Also: [7:39](https://www.youtube.com/watch?v=x55Fj_syFcI&t=459s) (ask yourself what you want to know and the shortest path to it; see 28).
`principle`

**4. Redo it without help** — The step most people skip. After AI explains something and you get to the end, go back to the start and do the whole thing yourself. It costs roughly 10–15% more time but is what turns reading into knowing.
> "you have not learned that thing. You have merely read about that thing." — [11:40](https://www.youtube.com/watch?v=FSXHk4hMrY8&t=700s)
`principle`

**5. Make the AI test you, not tell you** — Socratic questioner (ask until I find the gap), Examiner (one question at a time, each harder), Checker (grade my steps, don't rewrite), Listener (grade my own explanation against the source). He personally speaks, then sketches, then writes a short version, and has AI compare all three to the source. For real-world skills, add a Sparring partner (tough simulated interviewer or client, on a timer) and AI-built practice apps.
> "Don't just give me the answer. Ask me questions until I find what I don't know myself." — [14:13](https://www.youtube.com/watch?v=FSXHk4hMrY8&t=853s)
`principle` (speak–sketch–write routine: `preference`)

**6. Diagnose the shared root mistake** — Repeated errors across topics often come from one underlying misunderstanding. Feed AI your past attempts or conversations and ask what they have in common, then learn that root thing.
> "What misunderstanding do all of these things have in common?" — [19:46](https://www.youtube.com/watch?v=FSXHk4hMrY8&t=1186s)
`principle`

**7. Spaced repetition, with AI as the clerk** — Memory decays along the forgetting curve unless you review at intervals; each review makes it decay more slowly. AI can write flashcards, keep the schedule (or use Anki) and turn your mistakes into new cards. The Clerk only organises *your* notes, so the thinking stays yours.
> "the reason I like the clerk is cuz all of the thinking is your own." — [22:18](https://www.youtube.com/watch?v=FSXHk4hMrY8&t=1338s)
`principle` ("5 to 10X" efficiency figure: `claim to check`)

**8. Work at your level and find the best human explanation** — Learn in the zone just beyond your reach: have AI quiz you easy-to-hard and stop when you start guessing. Then ask it to find the best existing explanations for your level, because humans are still the best at the perfect metaphor.
> "when you find that perfect explanation… you can usually save yourself days, weeks, or months" — [24:51](https://www.youtube.com/watch?v=FSXHk4hMrY8&t=1491s)
`principle`

**9. The case against AI: struggle is where learning happens** — AI lets you skip the hard "hump", so you remember nothing. Like GPS weakening your sense of place, outsourcing the thinking weakens the brain's logic. Watch for AI agreeing when you're half right or inventing numbers and sources. Don't use AI the "default way".
> "AI allows you to shortcut that a lot of the time, and that leads to you ultimately remembering nothing." — [27:23](https://www.youtube.com/watch?v=FSXHk4hMrY8&t=1643s)
`principle` (GPS study: `claim to check`)

---

## How to use AI and agents

**10. Don't trust the first output; run evals** — Models aren't deterministic: the same prompt can give great or terrible results. Before building a prompt into a workflow, run it ~10 times, count successes, change the prompt, count again, and keep the better version. Also give it a way to check its own work (a screenshot, an example, a test) and a revision loop, because one attempt is just a first draft.
> "run it 10 times, count the number of times out of 10 that it actually worked." — [2:35](https://www.youtube.com/watch?v=45K3zHckCnQ&t=155s)
Also: [9:07](https://www.youtube.com/watch?v=YIl-awY250k&t=547s) ("most people just prompt once"; refine "based on some sort of eval", the A in CLEAR, see 32).
`principle`

**11. Let Claude write the prompt (meta-prompting)** — AI is now better at prompting than people. For anything large, say what you want and ask Claude to help write the prompt; it will ask who it's for and what great looks like. For quick daily tasks, just ask directly.
> "the unfortunate reality is AI is better than us at it now." — [6:36](https://www.youtube.com/watch?v=45K3zHckCnQ&t=396s)
`principle`

**12. Treat it like a contractor: definition of done** — Drop step-by-step instructions and long lists of "never" rules written for older models. Give a clear definition of done and permission to ask if unsure.
> "treat Claude more like a contractor than an in-house employee." — [10:09](https://www.youtube.com/watch?v=45K3zHckCnQ&t=609s)
Also: [8:07](https://www.youtube.com/watch?v=YIl-awY250k&t=487s) (the C in CLEAR: "a precise problem definition with measurable outcomes", see 32).
`principle`

**13. Diagnose before you fix** — Don't say "it's broken, fix it". Ask it to list all problems without changing anything, cross out the ones you don't care about, then have it fix the rest. Saves tokens, time and undoing unwanted changes.
> "List all of the problems with this app." Don't rewrite or do anything yet. — [11:41](https://www.youtube.com/watch?v=45K3zHckCnQ&t=701s)
`principle`

**14. Fan out, fan in** — Researching a problem first improves the result, but is expensive with a strong model. Send cheap sub-agents wide to gather information, then hand a combined summary to a strong model to decide.
> "pay a little bit of money to a really cheap model to scan the search space as widely as humanly possible." — [19:19](https://www.youtube.com/watch?v=45K3zHckCnQ&t=1159s)
`principle` (model names Opus 5.5/6, Fable, Mythos: `claim to check`)

---

## Claude Code & Codex practice

**15. Protect the context window** — Use `/context` to see what fills it; he eyeballs ~30% gone before you type (system prompt, tools, MCP connectors, memories, skills). Longer chats cost more and get dumber (context rot). Turn off unused MCPs and skills; move to a fresh window when it's full or misbehaving. He runs `/compact` much earlier than auto-compact.
> "about 30% of the context is already taken up before I say anything." — [8:37](https://www.youtube.com/watch?v=45K3zHckCnQ&t=517s)
`principle` (30% figure, `/compact` behaviour: `claim to check`; early compacting: `preference`)

**16. Start fresh with a handoff note** — Long sessions collect contradictory instructions and the model splits the difference. Ask for a summary (done, decisions needed, next, open problems), correct it, and paste it into a new session. Higher quality and cheaper. For side questions mid-task he uses `/btw`, so answers don't pollute the main context.
> "Summarize where we are." So, give me what is done, give me all the decisions I need to make — [17:15](https://www.youtube.com/watch?v=45K3zHckCnQ&t=1035s)
`principle` (heavy `/btw` use: `preference`; command names: `claim to check`)

**17. Let the code be the context** — Separate spec, notes and log files drift out of date as code goes v1→v4, so the model works from stale context. Put the explanation as inline comments in the code itself, which the model must read anyway. CLAUDE.md is the exception, for preferences and lessons.
> "the two sources drift apart." — [5:36](https://www.youtube.com/watch?v=45K3zHckCnQ&t=336s)
`principle`

**18. MCP to prototype, lean custom skill to scale** — Connectors/plugins (MCP underneath) are one click to prove something works, but they're context-heavy and add startup time. Once it works, replace it with a lean custom skill. He prunes MCPs to save 3–5 seconds per startup.
> "it gets you up and running really quick, but the downside to MCP is it's typically very heavy on context" — [13:42](https://www.youtube.com/watch?v=45K3zHckCnQ&t=822s)
`principle` (startup-time pruning: `preference`)

**19. Run scoped tasks in parallel** — Rather than one task at a time, scope non-overlapping tasks and have sub-agents do them simultaneously, then merge. He accepts a slightly higher error rate for speed.
> "do this in parallel by running mutually exclusive scope to tasks." — [15:13](https://www.youtube.com/watch?v=45K3zHckCnQ&t=913s)
`preference`

**20. Keep CLAUDE.md lean, current and positive** — Stale information (his old revenue figures) caused bad advice. Keep a summary of what's where (`/init`), preferences (full file paths, use Python), and lessons; review after every model update. Record the fix ("batch the file reads"), not just a ban, and ask Claude "How could you have done that faster with fewer tokens?"
> "Instead of giving it like negatives… instead give it positives." — [23:53](https://www.youtube.com/watch?v=45K3zHckCnQ&t=1433s)
`principle` (his specific preferences: `preference`; "saves 3–4 hours a week": `claim to check`)

**21. Keep a backup tool ready** — Claude Code has outages and quality dips. He keeps Codex in the same folder, with CLAUDE.md symlinked to AGENTS.md so both share instructions. He says Claude now reads AGENTS.md too.
> "I will always have a backup model like Codex or another model in the same folder with me." — [22:22](https://www.youtube.com/watch?v=45K3zHckCnQ&t=1342s)
`principle` (symlink setup: `preference`; Claude reading AGENTS.md: `claim to check`)

---

## Careers & business in the AI age

**22. The floor is always rising** — Standing still means going backwards relative to what AI and everyone else can now do, like money losing value to inflation. You must keep improving just to hold position. Part of this is closing knowledge asymmetry: service businesses are paid on the gap between what they and the customer know, and that gap is shrinking as people learn what AI can do.
> "if you stay in the same place, okay, and the floor is always rising… you're actually going down." — [7:10](https://www.youtube.com/watch?v=638GQZ9UZ4w&t=430s)
`principle` (AI-usage stats "80%… now 70%": `claim to check`)

**23. Sales and marketing beat technical skill** — Technical skill has "virtually evaporated" as a differentiator because everyone can simulate it with agents. Spend far more time on funnels, pitching, authority, follow-up. In a commoditised market you win by being extraordinary at one thing, usually selling.
> "If you spend any of your time improving your technical skills, you need to spend 100x… on… sales, marketing, and delivery systems." — [20:49](https://www.youtube.com/watch?v=638GQZ9UZ4w&t=1249s)
Also: [9:09](https://www.youtube.com/watch?v=x55Fj_syFcI&t=549s) (new tools depreciate fast, sales gets more valuable with every development: "soft skills are literally all we have left"); [9:39](https://www.youtube.com/watch?v=x55Fj_syFcI&t=579s) ("Learn outbound"); [0:31](https://www.youtube.com/watch?v=YIl-awY250k&t=31s) ("technical skills are becoming obsolete").
`principle` (the 10x/100x/1,000x multipliers: `claim to check`)

**24. Be in the industry that does the automating** — Every white-collar field is being transformed, not just automation. If labour is being automated, the safest place is the industry doing the automating. Value shifts from building to deciding what to build, upskilling teams and workshops.
> "is there any industry you would rather be in than the one that is literally doing the automating?" — [11:42](https://www.youtube.com/watch?v=638GQZ9UZ4w&t=702s)
`principle` (his framing; strongly tied to what he sells)

**25. His near-term predictions** — Benchmarks (Automation Bench, GDPval) saturating within months; business owners waking up in early 2027 and wanting a human guide; drag-and-drop builders (Make, Zapier, n8n, Power Automate) fading; demand moving to higher-bandwidth outputs (video, 3D, simulation), workshops and Claude Cowork rollouts; 2027 as the most profitable year for AI automation and possibly the start of its decline. Beyond 2027 he says he doesn't know, and warns that people flock to those who merely *seem* certain.
> "2027 will probably be the most profitable year of AI automation to date. But, it may also be the beginning of its decline" — [21:49](https://www.youtube.com/watch?v=638GQZ9UZ4w&t=1309s)
Also: his earlier 2026 video's timeline: natural language creating "more than 50% of workflows" in about 12 months, complete systems from business requirements in 24 ([6:37](https://www.youtube.com/watch?v=YIl-awY250k&t=397s)); stop learning drag-and-drop modules ([5:37](https://www.youtube.com/watch?v=YIl-awY250k&t=337s)).
`claim to check` (all predictions; "Gemini Argon 4" model name as captioned)

---

## Attention, news and hype

**26. Most AI news is entertainment, not education** — Model releases are now decimal-point upgrades that rarely change what you can do. AI, like automation, only does two things: same output with less input, or more output with the same input, and most of life doesn't need either. He compares following every release to following every political story: water-cooler talk with near-zero impact.
> "the vast majority of the AI news updates that you guys are probably seeing are more akin to entertainment" — [2:03](https://www.youtube.com/watch?v=x55Fj_syFcI&t=123s)
`principle`

**27. The hype is paid for: follow the incentives** — Much "organic" buzz is bought. He says he gets around 500 paid pitches a month; creators, labs, fundraisers and hardware firms are all incentivised to make news look bigger. He admits he has done clickbait himself.
> "Do you have any idea how much money is behind pushing even the most mundane of tools these days?" — [5:06](https://www.youtube.com/watch?v=x55Fj_syFcI&t=306s)
`principle` ("500 pitches" figure: `claim to check`)

**28. Seek learning out; don't scroll for it** — Learning that you go looking for (outbound) fits your goal far better than what a feed pushes at you (inbound). Decide what you want to know, find the shortest path to it, and use search instead of the For You page. Older tutorials are fine. Be intentional about what you consume. He says this is why he makes long courses optimised for YouTube search, and admits it sounds biased.
> "If you want to learn something, genuinely take a step back and ask yourself what it is that I want to know" — [7:39](https://www.youtube.com/watch?v=x55Fj_syFcI&t=459s)
Also: [10:10](https://www.youtube.com/watch?v=x55Fj_syFcI&t=610s) ("where do I want to go and why?").
`principle`

**29. Don't chase the cutting edge; get better at one thing** — The people most up to date on the latest tools tend to use them least. For real business results, look a couple of generations back, at what tested business owners are adopting. In his experience the richest people he knows ignore releases and keep getting better at the one thing that pays.
> "the richest people I know, the people that make the absolute most money do not know what model just dropped." — [4:05](https://www.youtube.com/watch?v=x55Fj_syFcI&t=245s)
`principle` (based on his personal circle: anecdote, not data)

---

## Skills that last (from his 2026 video)

**30. Skills at the margins get wiped out** — His "Sarah the Seamstress" story: hand-stitching, then looms, then CAD, then prompting. Each technical revolution makes the hands-on execution skills of the last one worthless and moves value up a level. He says he no longer needs to know every Make.com module or n8n node; he pastes the docs into ChatGPT.
> "every major technical revolution invalidates the skills at the margins of the previous." — [4:06](https://www.youtube.com/watch?v=YIl-awY250k&t=246s)
`principle` (the story is made up by him, he says so)

**31. Be the interface between a business and AI** — The valuable skill is knowing what a business is suffering from and explaining it to a model, not knowing tool features. Stop memorising tool features and API docs; learn business systems and to spot problems worth more than about $50,000 to solve. Moving up a level of abstraction also moves you up a level of leverage.
> "You need to stop memorizing tool features and API documentation." — [5:37](https://www.youtube.com/watch?v=YIl-awY250k&t=337s)
`principle` ($50,000 threshold and "10x" leverage: `claim to check`)

**32. The CLEAR prompt framework** — Clarity (a precise problem with measurable outcomes), Logic (steps with clear decision points), Examples (scenarios and edge cases, e.g. lead-score thresholds), Adaptation (refine back and forth against an eval), Results (check the output meets the business need: can you measure success?). A vague prompt ("Build me a lead generation system") gives a generic, inconsistent template; a specific one acts like bowling-lane guard rails. Business, he says, pays for consistency.
> "The C stands for clarity. The L stands for logic. The E stands for examples." — [8:07](https://www.youtube.com/watch?v=YIl-awY250k&t=487s)
`principle` (the unnamed "research paper" origin: `claim to check`)

**33. Learn the shape of a business** — Systems thinking travels across tools, like an elite athlete who understands movement rather than one sport's techniques. A marketing agency and an AI automation agency are the same shape with a different deliverable. Every business follows marketing → sales → onboarding → delivery → reactivation/retention. He says he reused his content agency's shape to grow his automation agency.
> "marketing leads to sales which leads to onboarding which leads to delivery which leads to reactivation" — [12:41](https://www.youtube.com/watch?v=YIl-awY250k&t=761s)
`principle` (his revenue figures, $92,000 and $72,000 a month: `claim to check`)

---

## Tools and access

**34. Better models need money: free, ad-funded agents narrow the gap** — Frontier models cost a lot, so people who can't pay conclude "AI's not really that good". He tried Freebuff, an agent coding app paid for by watching ads (a daily allowance spent on any model, plan/build modes, parallel tabs, phone mirroring). Verdict: works, nothing groundbreaking, ads not too intrusive yet; he says he isn't affiliated. He deliberately made a "real" review rather than a hype one.
> "No, dude, you got to use the new ones." And they're like, "What do you mean? Oh, that's super expensive. I can't afford it." — [8:40](https://www.youtube.com/watch?v=IJS08TVGut0&t=520s)
`principle` (access gap) · `claim to check` (Freebuff, its prices, hours and all model names and scores, e.g. "GPT 5.6 Luna", "GLM 5.3 flash", "Claude fable 5.1")


---

## Where Nick contradicts himself or changed his mind

- **Skills: outdated or the goal?** He says skills "really are not the best way of doing things anymore" ([4:36](https://www.youtube.com/watch?v=45K3zHckCnQ&t=276s)), then recommends turning MCP connectors *into* "a lean custom skill" ([13:42](https://www.youtube.com/watch?v=45K3zHckCnQ&t=822s)–[14:13](https://www.youtube.com/watch?v=45K3zHckCnQ&t=853s)), and describes building skills for teams' Claude Cowork ([19:17](https://www.youtube.com/watch?v=638GQZ9UZ4w&t=1157s)). Reading it as "keep task notes in the code, keep skills lean" is our interpretation, not his words.
- **"AI automation won't last forever" vs "most staying power".** He opens by saying it "is not going to last forever" ([0:01](https://www.youtube.com/watch?v=638GQZ9UZ4w&t=1s)), then says it "has probably the most staying power out of any industry on Earth" ([11:42](https://www.youtube.com/watch?v=638GQZ9UZ4w&t=702s)), and calls that "a fact", not a thesis ([11:11](https://www.youtube.com/watch?v=638GQZ9UZ4w&t=671s)).
- **Technical skill "evaporated" vs 1,000 hours on Claude Code technique.** One video tells you to spend 100x more on sales than technical skill ([20:49](https://www.youtube.com/watch?v=638GQZ9UZ4w&t=1249s)); another is a deep technical how-to built from "over 1,000 hours" ([0:02](https://www.youtube.com/watch?v=45K3zHckCnQ&t=2s)).
- **Confident forecasts vs "I don't know".** He predicts specific months for benchmark saturation ([2:04](https://www.youtube.com/watch?v=638GQZ9UZ4w&t=124s)) but later says forecasting past 2027 would be "intellectually dishonest" ([15:15](https://www.youtube.com/watch?v=638GQZ9UZ4w&t=915s)).
- **Drop the "never" rules, but add "never skip tests".** He says you don't need "never never statements" yet suggests adding "never skip tests" to CLAUDE.md in the same breath ([11:10](https://www.youtube.com/watch?v=45K3zHckCnQ&t=670s)–[11:41](https://www.youtube.com/watch?v=45K3zHckCnQ&t=701s)). Minor.
- **Changed view over time:** he references a video "about a year ago" on what to learn instead of automation in 2026 ([1:34](https://www.youtube.com/watch?v=638GQZ9UZ4w&t=94s)); his sales-vs-tech multiplier went from 10x "last year" to 100x now ([21:19](https://www.youtube.com/watch?v=638GQZ9UZ4w&t=1279s)). That earlier video is now ingested (YIl-awY250k): there, learning automation in 2026 is "one of the worst career moves" ([0:01](https://www.youtube.com/watch?v=YIl-awY250k&t=1s)) and the skill is "well on the verge of becoming worthless" ([0:31](https://www.youtube.com/watch?v=YIl-awY250k&t=31s)). A year later he says AI automation has "the most staying power" of any industry ([11:42](https://www.youtube.com/watch?v=638GQZ9UZ4w&t=702s)). Partly reconcilable (he means the *implementation* skill is dying, [2:03](https://www.youtube.com/watch?v=YIl-awY250k&t=123s)), but the tone flipped.
- **Ignore the news and the cutting edge vs "use the new ones".** He says don't look at the cutting edge ([3:04](https://www.youtube.com/watch?v=x55Fj_syFcI&t=184s)) and new-tool hype is mostly paid ([5:06](https://www.youtube.com/watch?v=x55Fj_syFcI&t=306s)), yet he also reviews a brand-new free agent and tells people who think AI is weak "you got to use the new ones" ([8:40](https://www.youtube.com/watch?v=IJS08TVGut0&t=520s)). One way to read it: model *quality* matters, chasing every release doesn't. That is our reading, not his words.
- **Criticises hype and clickbait while using it.** He says creators are incentivised to oversell and admits "I've done some click-baity" ([5:36](https://www.youtube.com/watch?v=x55Fj_syFcI&t=336s)); the 2026 video opens with "I made 400 grand last month" and "one of the worst career moves" ([0:01](https://www.youtube.com/watch?v=YIl-awY250k&t=1s)).
- **Revenue figures don't line up.** The 2026 video says "$400,000 a month" for the business that was "disappearing" ([1:02](https://www.youtube.com/watch?v=YIl-awY250k&t=62s)) and also that he scaled his own business "to over $90,000 in a month in 2025" ([4:36](https://www.youtube.com/watch?v=YIl-awY250k&t=276s)), a year-label that looks garbled in the captions. Treat all his revenue numbers as unverified.

---

## Promotion to ignore

- **Maker School** — his paid 90-day "first customer or your money back" programme; pitched at the end of all three videos ([28:54](https://www.youtube.com/watch?v=FSXHk4hMrY8&t=1734s), [25:25](https://www.youtube.com/watch?v=45K3zHckCnQ&t=1525s), [22:50](https://www.youtube.com/watch?v=638GQZ9UZ4w&t=1370s)), plus mid-video mentions ([16:17](https://www.youtube.com/watch?v=638GQZ9UZ4w&t=977s), [18:17](https://www.youtube.com/watch?v=638GQZ9UZ4w&t=1097s)). Claims of "over 2,000 people" and "$20,000 in discounts" are sales copy.
- **Self-credentials used as authority:** "$400,000 a month" ([0:01](https://www.youtube.com/watch?v=FSXHk4hMrY8&t=1s)), "close to 10 million dollars" ([0:01](https://www.youtube.com/watch?v=638GQZ9UZ4w&t=1s)), "$31,141"/"over $30,000" spend and "multi-billion dollar" clients ([0:02](https://www.youtube.com/watch?v=45K3zHckCnQ&t=2s)). Unverifiable; don't repeat as fact.
- **Sales-call sparring examples and his framing of AI automation as a career** are tied to what he sells ([20:47](https://www.youtube.com/watch?v=FSXHk4hMrY8&t=1247s)). Keep the method, discount the pitch.
- **Maker School and Leftclick in the 2026 video:** "Obligatory pitch" for Maker School ([13:41](https://www.youtube.com/watch?v=YIl-awY250k&t=821s)) and his agency Leftclick ("book a call", [14:13](https://www.youtube.com/watch?v=YIl-awY250k&t=853s)); credentials "400 grand last month", Leftclick clients and speaking "alongside" big names ([0:01](https://www.youtube.com/watch?v=YIl-awY250k&t=1s)).
- **His own courses:** in the AI-news video he plugs his search-optimised long courses and admits it "is going to sound biased" ([7:08](https://www.youtube.com/watch?v=x55Fj_syFcI&t=428s)–[8:09](https://www.youtube.com/watch?v=x55Fj_syFcI&t=489s)).
- **Freebuff:** the whole of IJS08TVGut0 is a demo of one product. He says "we're not affiliated whatsoever" ([0:01](https://www.youtube.com/watch?v=IJS08TVGut0&t=1s)); the ads shown inside it (e.g. The Farmer's Dog, [4:04](https://www.youtube.com/watch?v=IJS08TVGut0&t=244s)) are the product's own ads, not Nick's sponsors.
- No other third-party sponsors appear in these six transcripts. Tools named in passing (Ghostty, Orca, Hostinger, Wix, Squarespace, Anki) are mentions, not endorsements to rely on.
