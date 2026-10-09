# Lesson: the smallest context that works (and a cleaner brain for us)

From Nate's newest video, [Anthropic Engineers Just 10x'd Everyone's Claude Code](anthropic-engineers-just-10xd-everyones-claude-code--oz2CwrPV2Rg-transcript.md)
(oz2CwrPV2Rg, 12 min), checked against the Anthropic article it's based on
([source note](anthropic-context-engineering-claude-5-source.md)). In the brain:
concept 39 and Rule 41 (`brain/`). Written 2026-10-08.

## The key information, in plain words
1. **Newer models need less telling.** Anthropic cut over 80% of Claude Code's
   own built-in instructions and measured no loss.
2. **Keep only what Claude can't work out alone:** who you are, your voice,
   goals, audience, how your work runs, *why* you want something, and the
   traps to avoid.
3. **Cut three kinds of line:**
   - things it can look up (long folder lists);
   - the same rule written in two places;
   - old rules added to fix an older model's mistake.
4. **Load a procedure only when its job comes up.** The video-editing steps
   don't need to be loaded while you write a script: put them in a skill.
5. **Say the outcome, the reason and the limits, then get out of the way.**
   Heavy guard rails made Nate's output *worse* than a bare, fresh session's.
6. **Check it regularly.** Run Claude Code's `/doctor`, then a read-only
   "show me the smallest change" audit. Do it monthly, or quarterly, and
   **every time you switch to a new model**. Schedule it once you trust it.
7. **Look for hidden extras.** Instructions can load from other places
   (user-wide files, other folders) without you knowing.

## What it means for our OS (measured 2026-10-08)
Loaded into **every** message today:
- `AGENTS.md`: 93 lines, about 8,100 characters (about 2,000 tokens).
- 10 skill descriptions: about 3,500 characters.
- 3 agent descriptions: about 1,100 characters.

That's small next to Claude Code's own prompt, but we can still cut it.

**Proposed clean-up (nothing changed yet; each one is Charlie's call):**
1. **Slim the router.** Keep the rules and the routes that aren't obvious.
   Move the rebuild commands, URLs and step lists (Brain dashboard,
   Nate-first map, flashcards backup, transcript and X commands) into
   their own folder READMEs or skills, where they load only when needed.
   Cut rows whose answer is just the folder name. (A line target was dropped on 2026-10-09: cut for a reason, never for length.)
2. **Say each rule once.** For example, "prove it, don't claim it" is in
   `AGENTS.md` and `context/working-rules.md`. The router keeps a
   one-line pointer only. (The ChatGPT export stays a copy on purpose.)
3. **One audit skill, not two.** Fold `os-audit` (our longest skill
   description) into `/audit`, carrying its "backtrack a miss" routine
   across. This also matches the Nate-first map.
4. **Re-audit after every model switch.** Add that trigger to the
   `audit` skill and to the Friday routine.
5. **Find hidden context.** Charlie types `/doctor` here once to see
   whether it runs in cloud sessions; on the Mac it's on the
   `context/mac-day.md` list.
6. **Prove nothing was lost.** Before and after the trim, run the
   fresh-session test (who am I, my priority, where would a new project
   go, where are decisions kept) and compare the answers. This is Nate's
   own method: the same task with the full set-up vs a fresh one.

**Then, a cleaner-looking brain:** once the trim is done, rebuild the
Brain dashboard in the radial style Charlie liked from Nate's video:
`CLAUDE.md`/`AGENTS.md` at the centre, a ring of skills around it, and
the main areas (context, projects, research, audits, tools) as hubs on
the outside. With fewer, clearer links, the picture shows the trim.

## Applied 2026-10-08 (Charlie: "use Nate's new information to improve our system so I am not being asked so many questions")
Done: proposals 1, 2, 3, 4 and 6. Proposal 5 (`/doctor`) is a card on the Decision Desk.
- **Router:** 93 → 76 lines, about 8,100 → 4,800 characters. Dashboards moved to
  `system/pages.md`; research commands to `research/README.md`.
- **One audit skill:** `os-audit` is now `.claude/skills/audit/content-check.md`;
  `audit` also runs after a model switch.
- **Descriptions** over 300 characters cut (6 of them), so less loads every message.
- **Fresh-session test:** before and after in `audits/evidence/2026-10-08-smallest-context/`.

### What I asked Charlie most (this session, 16 "Now:" lines)
| Kind of ask | Times | Fix |
|---|---|---|
| "Say go" / approve small, easy-to-undo work | 6 | Not a question any more: state the assumption and do it (router rule) |
| The same open question again (the base kit) | 4 | Asked once, waits on the Decision Desk |
| "Open the page, tap around, then tell me 'read my marks'" | 4 | `decide` skill reads the marks and answers at session start |
| Things only Charlie can do (`/context`, `/doctor`) | 2 | "For you to do" cards on the Desk |
Result: one new skill, `decide`, and the Decision Desk (`system/pages.md`).

### Thin and thick skills
| Skill | Size | Verdict | Done / proposed |
|---|---|---|---|
| audit | 17k chars | thick, kit text | now also holds the content check |
| level-up | 11k | thick, kit text | trim: Desk card |
| onboard | 8k | thick; needed for set-ups | keep (Desk card) |
| grill-me | 7.5k | thick but its job | keep; description cut |
| find-skills | 5k | thick, mostly generic | trim to ~10 lines: Desk card |
| research-creator | 5k | right-sized | description cut |
| brain-ingest | 3k | right-sized | description cut |
| link | 2k | right-sized | keep |
| teach | 1.7k | thin (repeats working-rules) | stops asking: picks a reading and goes |
| decide | new, 2k | thin on purpose | the only "ask Charlie" route |
Skill bodies only load when used; descriptions load every time, so cutting descriptions saves the most.
