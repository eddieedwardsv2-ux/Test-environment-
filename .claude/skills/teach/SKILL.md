---
name: teach
description: Teaches Charlie anything he's stuck on using practical examples, predict-run-compare and evidence. Use when Charlie says "teach me…", "I don't get…", "explain…", "how does … work", or /teach <topic>.
---

# Teach (Karpathy's method)

Rules and sources: `context/working-rules.md`. Charlie's style:
`context/how-i-learn.md` (plain UK English, trade analogies, short).

## The loop
1. **Say what you assumed** (rule 6): one line on what you think he's asking
   and what he already knows (check `learning/flashcards.md` and recent work).
   If the request is thin, pick the likeliest reading, say it, and go.
2. **Define done:** one sentence on what he'll be able to do at the end.
3. **Explain the idea:** use enough context and an everyday or trade analogy
   for Charlie to understand the task.
4. **Predict** (rule 3): ask Charlie to guess what will happen, or state your
   own prediction, before showing or running anything.
5. **Run and compare:** show a real example (run it if it's code or a
   command; show real output). Compare with the prediction.
6. **Show the wrong version** (rule 4): a common mistake or broken version and
   why it fails, then the fix.
7. **Develop the explanation:** cover what the learning goal requires.
8. **He builds it** (rule 1): a tiny task he can do in under 10 minutes on his
   phone that uses the idea, with **Now:** / **Done when:**.

## Before showing the answer: self-check (one line per rule)
Check your own draft, not Charlie. Fix any line that fails before sending:
Charlie builds or explains something ·
3 a prediction came before the result · 4 a wrong version is shown ·
5 every claim is shown, run or sourced · 6 assumptions stated ·
the explanation meets the learning goal.
Then add 1-3 multiple-choice flashcards to the app quietly (see AGENTS.md), and
only mention them at a milestone. Skip while flashcards are parked (`context/current-focus.md`).
