# Charlie's thoughts, 9 October 2026 (gathered from the chat)

Gathered by Claude from what Charlie said in the chat on 9 October. His
walk notes arrived later the same day: see "Walk notes" at the bottom. Nothing here has been acted on beyond what he already asked for.
Public repo: nothing private.

## 1. How he learns
- "I am still just learning in the most streamline way I can as you work much
  faster than watching these videos."
- Wants to save usage "for when we have more spare and are less busy/focused".

## 2. His voice
- "I am struggling to find Charlie's voice."
- Doesn't have stories to tell, so asked for practice: "practice emails. How you
  would send them originally vs what changes I'd make." (Became the Voice Gym.)

## 3. Order of learning: newest first, older for context
- Ingest The Next New Thing "yesterday's first, then the day before… working
  backward to week 38 … so we ingest newer content before older."
- "The older content is just for better context, understanding and relations",
  and to check "we are not missing any old skills that simply just haven't been
  replaced by new ones yet."

## 4. Brains with voices: a council of elders
- Review "the presenters' opinions on each show of each skill … whether they
  would use skills or not and why."
- Compare "the Next New Thing's voice against our own opinions of whether we need
  skills and what we need them for."
- "Eventually when we have ingested a lot more knowledge the brains will also
  have voices, so I kind of want to build my own council of elders of knowledge."
- Keep every opinion "as they will be used for relation references and compared
  against again in the future."

## 5. Relations and routing (to discuss, change nothing yet)
- Wanted Nate's videos checked for concepts "that need more context for best
  routing and relation building".
- After viewing the maps: "is the routing clear, and where is our brains'
  'middle'?" He wants to think about this next session: "do not do anything with
  those thoughts until we discuss more."
- ChatGPT hand-off on intelligent model routing saved alongside this file
  (`2026-10-09-model-routing-handoff.md`), not started. Same theme: pick the
  smallest set of models, skills and tools that does the job reliably.

## 6. The pages he uses most
- "Charlie's Brain, Hands Brain and Nate's brain … are the 3 most used
  artifacts alongside the decision cards", so update them after every run.

## 7. Weekly checks
- Skills he turns off: "add the skills turned off into weekly check to see if we
  could have needed them back on."
- Unknown prices (card 4): "Explain 4 more please, I don't get it."
- skills.sh-only tools: the grey tag "should be checked against new videos
  ingested".

## 8. Where it's heading (Claude's theory, he hasn't confirmed it)
Collect, then try on real work, keep what wins, teach it, set others up. The
set-up kit is the product and the channel is the documentary. The gap: the
OS knows a lot about other people and little about Charlie (voice, his own
results).

## Threads that join up (Claude's reading, for the discussion)
- Sections 4 and 5 may be one question: if each brain has a voice, the
  "middle" could be the place that asks them and decides, which is the
  routing the ChatGPT prompt describes. To discuss before anything is built.

---

# Walk notes (pasted 2026-10-09, about 5am), grouped by Claude

Charlie's points in his own words where possible, with what Claude found
beside them. **Findings** are checked facts; **Proposals** are Claude's
suggestions for discussion, not decisions.

## A. The Hands Brain is bigger than one show
- "The hands brain will not always be just information from the next new things
  content… first one will be Anthropic community plug in marketplace and others."
- Wants a better name than "Hands" (he wrote "EHAND").
- Finding: the build already has a `source` field (The Next New Thing, skills.sh),
  so new sources fit without a rebuild.

## B. One YouTube ingester, as a skill
- "The YouTube ingester could maybe be a skill rather than part of ENATE and hands brain."
- Finding: today YouTube work is spread over `research-creator`, `brain-ingest`
  (triage), `hands-ingest`, `research/get_transcript.py`, `research/hands/pipeline.py`
  and the GitHub transcript queue.
- Proposal: one `youtube-ingest` skill (list, triage, transcript, queue) that hands
  the transcript to whichever brain wants it. The brains keep only the "what does
  this mean for us" step.

## C. Nate's voice, and better names for the elders
- "We should also be taking note of Nate's voice so we no longer need to
  distinguish the real Nate from ENATE."
- Wants names "based on what they do and what type of elder they would be in a
  council of wise elders… based around us… what we do and how best, optimal,
  safest and most audited."
- "Audited" means "properly structured security and safety". Asks: "do the two
  need to be distinguished?"
- Proposal (names by job): Architect (Nate: how to build the OS), Quartermaster
  (tools: what kit to use now, from any source), Maker (Boris Cherny: how Claude
  Code is meant to be used), Teacher (Karpathy: first principles), Builder (Nick,
  parked), Guardian (safety and security), and Charlie as the Chief, who decides.
- Proposal on audit vs safety: two different checks, one elder. "Is it true and
  does it work?" (audit: receipts, tests, quotes) is not the same as "is it safe?"
  (security, privacy, permissions, a public repo). A tidy, well-audited system can
  still leak. The Guardian holds both duties, with separate checklists.

## D. Middle, hands, desk
- "What is our middle, our hands, our desk (desk being later context we haven't
  learnt yet relating to Mac day)."
- Proposal (to discuss): head = the router (`AGENTS.md`, picks the route);
  middle = the brains and the council, where knowledge meets and a recommendation
  is made; hands = what acts (skills, plugins, MCPs, scripts, routines);
  desk = the Mac workspace (local files, Obsidian, desktop apps), not built yet.
  The Decision Desk is a different thing (Charlie's inbox) and may need a new
  name so the two don't clash.

## E. Why skills weren't found
- "I feel like you had access to a lot of these already. Find out why you couldn't
  find and use all these skills originally and make sure you can going forward."
- Finding: `system/capability-map.md` (which the rulebook says to check first)
  listed only our own skills and scripts. Connectors (HyperFrames, vidIQ, Moda,
  Notion…) and claude.ai skills (pdf, pptx, skill-creator, deep-research) were
  in no file, so the Hands Brain ranked pdf and pptx as "new". `connections.md`
  also misses HyperFrames, Moda, Notion and Canva.
- Fixed 2026-10-09: the capability map now has "Already available, nothing to
  build", the Hands build treats those as already owned, and `connections.md`
  now lists HyperFrames, Moda, Notion and Canva (rows 13 to 16).

## F. Stop ingesting older shows
- "Maybe we don't need to ingest anymore skills from older videos as we already
  have the last 3 months of the next new things information."
- Finding: we hold about 4 weeks of the show, not 3 months: videos from 11 Sep
  (listed) and 14 Sep (ingested) to 8 Oct. Card on the Desk: stop here, or go back
  to 3 months.

## G. Nate's kit, newest thesis first, plus Boris and Karpathy
- "Nate's kit should be created starting from his newest thesis first and working
  backwards to reverse engineer the system."
- "Find who Boris is… Boris is where Nate got this new 10x Claude thesis… how
  he's using AI for the best type of router at the start/entry of the brain and
  each of its sections."
- Finding: Boris Cherny (captions also spell it Churnney/Cherney) is named in 10 of
  Nate's 69 saved transcripts, including the newest (oz2CwrPV2Rg, "Anthropic
  Engineers Just 10x'd"), where Nate turns "this interview with Boris" into a
  guide. From Claude's own knowledge (not yet sourced in the repo): Boris Cherny
  created Claude Code at Anthropic. Next: research him like a creator, then
  check which of ENATE's newest rules come from him.

## H. Claude and ChatGPT/Codex kept in step
- "We need to update Claude/Claude Code and ChatGPT/Codex so they get updated on
  each others work when sessions end or hand off so neither are left behind…
  the router to point them both the right way to act the same."
- Finding: both read the same `AGENTS.md` (Codex directly, Claude through
  `CLAUDE.md`). But ChatGPT only sees `exports/chatgpt-instructions.md`, updated by
  hand. And at 04:04 today a non-Claude session changed `AGENTS.md` and added
  `research/corey-haines/` without a `decisions.md` or hand-off entry, so Claude
  only found it by chance when a push was refused. That is the gap.
- Proposal: one session-end rule for every agent (update `context/handoff.md`
  and `decisions.md`), and an audit warning when the router changes with no log
  entry.

## I. Is it working, or just theory?
- "Is our current system actually working or is it all just theory." / "Check our
  fully working system is working from router to Brain and so forth."
- Finding (today's evidence):
  - Working: the router (fresh-session test 10/10); `tools/audit.py` on every push
    and before finishing; the Decision Desk (cards answered and acted on); the
    GitHub transcript queue (7 fetched today); the Hands pipeline end to end;
    the maps; quote checking.
  - Not yet proven: both weekly routines (first runs today at 8:59 and tomorrow);
    Codex in this repo (never run; on Mac day); the ChatGPT side; the Voice Gym
    (no rewrites yet); `try-tool` (one run); the council (a plan only); the set-up
    kit (never tried on a real person).
  - Theory only: the "middle", the council, model routing.
- Proposal: one end-to-end test, router to brain to answer, run fresh in both
  Claude and Codex, before building anything new. That also answers the ChatGPT
  routing prompt's first question.

## J. A kit for blank accounts
- "Create a plan for how we make our own up to date kit of the best way to set
  up your router and your LLM wiki brain to take over to blank accounts."
- "The template should consist of core thesis, not all the actual data… just the
  correct routes, workflows and skills/plugins needed to get going."
- Finding: this is the 90-day priority (`projects/ai-os-setup-kit/plan.md`, v0.4),
  with a blank template in `templates/standard-ai-os-v1/`. Not yet rebuilt from
  Nate's newest thesis.

## K. Lessons to YouTube
- "Create some kind of pipeline output to maximize our growing knowledge,
  especially about all of skills and plugins and MCPs, to take our lessons
  straight to YouTube shorts and also into filming plans with prompt cards for
  filming and professional editing."
- "How to turn our lessons to content & create our first YouTube short."
- Proposal: lesson, then a short script (hook, 3 beats, call to action), then
  prompt cards for filming, then an edit plan; HyperFrames for titles and
  overlays (tried today). First short: "I let AI build my second brain" or
  "The 3 pages I open every day".
