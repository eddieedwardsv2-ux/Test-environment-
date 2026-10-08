# Set-up plan: a beginner's first AI OS (draft v0.4, 2026-10-08)

The step-by-step plan for setting someone up from nothing. Follow it in order,
the same way every time; after each set-up, fix this file (see "After each
set-up"). Plain words only: the person may never have opened a terminal.

**Who it's for:** someone brand new to AI, no coding background.
**What they end with:** a private AI OS that knows who they are, what matters
to them now and where things live, checked by a fresh-session test, plus one
small automation they understand how to grow.
**Why the test set-ups are free:** they pay for their own Claude plan;
Charlie's time is free in exchange for honest opinions, above all: did
working the new way (an AI OS that knows them) feel different from the "old"
AI they've used (a blank chat that forgets them)?
**Format:** one 90-minute session. Its heart is three questions:
1. **What annoys you about AI?** (the before question)
2. **What do you wish it could do for you?**
3. **What's one thing in your life we can automate today?** It must be a
   job they repeat, with steps they can explain start to finish in about a
   minute.

They leave with a working AI OS, one small automation running in "training
wheels" mode, and an understanding of the bike method for growing it.
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
4. Start the recording, then ask questions 1 and 2 (keep their exact words):
   - "How do you use AI now (ChatGPT, Gemini or other)? **What annoys you
     about it?**" If they've never used it, note that.
   - "**What do you wish it could do for you?**" Write down every answer:
     the automation in step 8 comes from this list.

## Session 1 (90 minutes)
Each step has **Done when** so you both know it worked before moving on.
Rough timings: steps 1-3 about 15 min, 4-6 about 35 min, 7 about 5 min,
8-9 about 30 min, 10 about 5 min.

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

**Step 8: pick one thing to automate (question 3).**
- Go back to their "I wish it could…" list. Choose **one** job that:
  happens again and again (weekly or more); they can explain start to
  finish in about a minute ("first I…, then I…, finally I…"); and does no
  harm if it goes wrong once (nothing gets sent, paid or deleted).
- Good first picks: a weekly meal plan and shopping list; turning rough
  notes into a tidy email draft; a Monday "what's on this week" summary.
- They explain the steps out loud; Claude writes them down as a numbered
  process in their OS.
- **Done when:** the process is written as numbered steps, and they agree
  "yes, that's how I do it".

**Step 9: build it with training wheels (the bike method).**
- They say: **"turn this process into a skill"**. Then run it once on a real
  example, together.
- Explain the **bike method** (Nate's 3Ms framework,
  `references/3ms-framework.md`; his Codex course, video X-pbJWKmwi0 at
  1:15:06): an automation is never finished, you grow it the way you teach
  a child to ride a bike.
  1. **Training wheels:** you run it yourself and watch everything. (Today.)
  2. **Guided:** it runs, but it only drafts; you check every result.
  3. **Watched:** it runs on its own; you spot-check.
  4. **Hands-off:** helmet on, go ride.
  After **every** run, say what you liked and didn't like, and ask it to
  **update the skill**, so you never fix the same mistake twice. Move up a
  phase only when it's been right several times in a row.
- **Done when:** one real run worked, they gave one piece of feedback, and
  the skill was updated.

**Step 10: the after question, then stop recording.**
- "Compared with how you used AI before, what feels different, if
  anything?" Keep their words.

## Later (designed when we need it)
The days after session 1 (daily use, Friday audits, connecting their tools,
moving the automation up the bike phases) and the day-14 check, including
the "old AI vs your AI OS, would you keep paying?" opinion, get written
before the first person reaches them.

## After each set-up (Charlie)
1. Write anonymised lessons (no names) in `lessons.md` in this folder: where
   they got stuck, how long each step took, what you had to explain.
2. Fix this plan so the next person doesn't hit the same snag, and bump the
   version at the top.
3. The recording and their details stay in the private sessions repo.

## Decided (2026-10-08, Charlie)
- They pay for their own Claude plan from day 1; the set-up is free in
  return for honest opinions on old AI vs the new way.
- One 90-minute session built on three questions: what annoys you about AI,
  what do you wish it could do, and one thing to automate today (with the
  bike method). The 14-day follow-up gets designed later.

## Decided (Charlie, Decision Desk, 2026-10-08)
1. **Base: Nate's AIS-OS kit plus our three additions** (one rulebook for
   Claude and Codex, the day-1 fresh-session test, the research guide).
2. **Audit every set-up until the returns stop.** After each one, run the
   `audit` skill and fix, and repeat until a round finds nothing worth
   changing. Keep only what is best and relevant for a beginner.
3. **Then a wiki brain around their interests and passions.** Found by
   reviewing their past chats (once they're on a paid plan) plus an
   interview.
4. **Their voice, early:** ask for 3 emails, 3 articles, or just 3 spoken
   stories, saved as their voice samples, because the OS uses them all the time.
