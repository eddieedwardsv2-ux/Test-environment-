---
name: grill-me
description: Interviews Charlie one question at a time until his knowledge of a process, plan or decision is fully written down, saving every answer to brainstorms/ as it goes. Use when Charlie says "grill me", "interview me about…", when building a skill or context file that needs knowledge only he has, or when a brain dump would be too thin.
---

# Grill me (get knowledge out of Charlie's head)

From Nate Herk, "The Skill That 10x'd My Claude Code Projects"
(`research/nate-herk/the-skill-that-10x-d-my-claude-code-projects--c0kaKxM2pHg-transcript.md`).
The hard part of an AI OS is "getting everything from your head into the AI
system" ([0:32](https://www.youtube.com/watch?v=c0kaKxM2pHg&t=32s)); a 5-minute
brain dump is "not ever good enough"
([1:02](https://www.youtube.com/watch?v=c0kaKxM2pHg&t=62s)). The original is
Matt Pocock's short prompt; Nate added a checkpoint after every answer so long
sessions don't lose early answers ([2:33](https://www.youtube.com/watch?v=c0kaKxM2pHg&t=153s)).

## Steps
1. **Open the capture file first:** `brainstorms/YYYY-MM-DD-<topic>.md`
   (create `brainstorms/` if missing). If one exists for the topic, continue it.
   Sections: Summary · Key decisions · Q&A log · Open flags.
2. **Ask one question at a time**, walking each branch of the plan and settling
   decisions that others depend on first. Give your recommended answer with each
   question. If the repo can answer it, look there instead of asking.
3. **Checkpoint after every answer:** append the Q and A to the Q&A log and
   update Summary / Key decisions. Nothing lives only in chat.
4. **Flag what Charlie can't answer** (someone else knows it, or it needs
   checking) under Open flags, rather than guessing.
5. **Stop when you share the same understanding** (5 or 30 questions, whatever
   it takes) or when Charlie says stop.
6. **Offer the follow-through:** name the skills, context files or router lines
   this changes and ask before updating them. A new decision goes in
   `decisions.md` with the date.

## Rules
- This repo is public: if an answer is private (health, money, clients,
  other people), keep it out of the file and say so.
- Plain UK English, one question per message; end with **Now:** / **Done when:**.
