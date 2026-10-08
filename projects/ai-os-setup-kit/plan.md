# Set-up plan: a beginner's first AI OS (draft v0.1, 2026-10-08)

The step-by-step plan for setting someone up from nothing. Follow it in order,
the same way every time; after each set-up, fix this file (see "After each
set-up"). Plain words only: the person may never have opened a terminal.

**Who it's for:** someone brand new to AI, no coding background.
**What they end with:** a private AI OS that knows who they are, what matters
to them now and where things live, checked by a fresh-session test, plus a
weekly habit that keeps it true.
**Base:** Nate Herk's free AIS-OS kit (github.com/nateherkai/AIS-OS, MIT) and
its `onboard` interview. We don't rebuild the kit; this plan is the beginner's
path around it.

## Before the session (Charlie, about 15 minutes)
1. **Consent:** ask whether they're happy to be recorded, and say where it
   goes: the private "sessions" repo, and YouTube only with their OK after
   they've seen the cut. Note their answer.
2. **What they'll need:** a phone or computer with a browser; an email
   address; 60-90 minutes; one thing they wrote recently (an email or post)
   to paste in.
3. **Their device decides the route:** phone or tablet only → Claude Code on
   the web (claude.ai/code), which is how this OS was built. Computer → same
   web route first; desktop apps can come later.
4. Start the recording.

## Session 1: set-up (60-90 minutes)
Each step has **Done when** so you both know it worked before moving on.

**Step 1: accounts.**
- A free GitHub account (github.com). This holds their OS and is the backup.
- A paid Claude plan that includes Claude Code (check the current price on
  claude.com together; don't quote one from memory). If they already pay for
  ChatGPT Plus, Codex is an alternative: the kit works with both.
- **Done when:** they can sign in to both on their own device.

**Step 2: their own private copy of the kit.**
- In GitHub, create a new **private** repo from Nate's AIS-OS kit (use
  "Use this template" if offered, otherwise import it). Name it something
  like `my-ai-os`.
- **Done when:** the repo shows as Private and has `AGENTS.md` in it.

**Step 3: open it in Claude Code.**
- At claude.ai/code, connect GitHub when asked, and allow access to that one
  repo only. Start a session on it.
- **Done when:** they type "what is this repo?" and the answer mentions the AI
  OS kit.

**Step 4: the interview (`onboard`).**
- They type: **"onboard me"**. Claude asks 7 questions, one at a time, and
  saves each answer in `aios-intake.md` as it goes.
- Q2 is the one hard rule: they **paste** something they wrote earlier,
  unedited. No typing fresh text.
- Questions that don't fit them (revenue, meetings): answer "not yet" and
  move on.
- **Done when:** all 7 have an answer (or "not yet") and the Day-1 files
  have been created.

**Step 5: the wow moment.**
- They ask: **"what should I focus on this week?"**
- **Done when:** the answer uses their own priorities from the interview,
  not generic advice.

**Step 6: the fresh-session test (proof, not trust).**
- Start a **new** session on the same repo and ask: "Who am I? What's my
  priority? Where would a new project go? Where are past decisions kept?"
- **Done when:** every answer names a real file in their repo. If one doesn't,
  ask Claude to fix that route, then re-test.

**Step 7: save.**
- They type: **"save everything to GitHub"**.
- **Done when:** the GitHub page shows the new files with today's date.

## Week 1: use it (10 minutes a day)
- **Day 2-3:** start each day with "what should I focus on today?". When
  something changes (new goal, new project), tell it and ask it to update
  the right file.
- **Once in week 1:** "grill me about <one thing in my head>" to get more of
  their knowledge written down.
- **Friday:** "audit my AI OS". Keep the saved report: it's the first score
  to compare against.
- **Charlie checks in once** (a message, not a session): did they use it at
  least 3 days? What confused them?

## Week 2: make it reach their tools
- **One connection:** link the tool they use most (often Gmail or Google
  Calendar) as a claude.ai connector, read-only first. Add it to
  `connections.md` with the date it first worked.
- **One automation:** "level up my AI OS". It picks one small job to take
  off their plate and builds it.
- **Friday:** audit again and compare with week 1.

## It worked when (day 14)
- [ ] The fresh-session test still passes without Charlie's help.
- [ ] They used it on at least 5 of the 14 days.
- [ ] Two saved audit reports, and the second one isn't lower.
- [ ] One connection reads successfully.
- [ ] They can say in one sentence what the AI OS does for them.

## After each set-up (Charlie)
1. Write anonymised lessons (no names) in `lessons.md` in this folder: where
   they got stuck, how long each step took, what you had to explain.
2. Fix this plan so the next person doesn't hit the same snag, and bump the
   version at the top.
3. The recording and their details stay in the private sessions repo.

## Open questions (Charlie's call)
1. **Which base?** This draft uses Nate's AIS-OS kit, as the project README
   says. `context/current-focus.md` still says "built on
   `templates/standard-ai-os-v1/`" (our blank copy). Recommended: Nate's kit,
   with our template kept as a reference for what "good" looks like.
2. **Paid plan:** who pays during the free test set-ups? Recommended: they
   use their own plan from day 1, so the test is realistic.
3. **Session length:** one 90-minute session, or two 45-minute ones?
   Recommended: one session for steps 1-7, so they leave with a working OS.
