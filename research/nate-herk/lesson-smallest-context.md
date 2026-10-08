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
   Cut rows whose answer is just the folder name. Target: about 55 lines.
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
