# AIS-OS Intake

*Filled 2026-10-08 from existing repo sources (each answer names its source). Q2 needs real writing pasted by Charlie; Q5 and the first half of Q7 are pending. Public repo: no private details.*

This is the source-of-truth file for your AIOS. Fill it in by typing, voice-pasting (Wispr Flow / OS dictation), or running `/onboard` for a guided conversation. Whichever mode, this file is what `/onboard` reads to scaffold your Day-1 setup.

**Hard cap: 7 questions.** Each answerable in under 60 seconds. Don't overthink — you can edit and re-run `/onboard` any time.

---

## Q1 — Who are you, what do you sell, who do you sell it to?

Identity, offer, ICP. One paragraph each is fine.

```
Charlie: UK-based, 34, from a trades background (decorating, drainage, removals, property, landscaping), moving away from physical work. Learning Claude Code and Codex as a beginner while building a YouTube channel as a learner ("student, not teacher"). Offer (pre-launch): helping people brand new to AI set up their own Standard AI OS, first 2-3 free for friends and family. Audience: non-coders who want a working AI OS.
Sources: context/about-me.md; context/current-focus.md; brainstorms/2026-10-08-who-i-am.md
```

---

## Q2 — Paste 1-2 things you've written recently. Don't edit them.

An email, a LinkedIn post, a DM, a doc — anything that sounds like you when you're not trying. **Paste verbatim.** Do not type these mid-conversation with Claude — chat-shaped samples are worse than no samples (voice contamination).

*2026-10-09: no samples yet, so Charlie practises on the Voice Gym (`system/pages.md`): AI-style drafts he rewrites his way. Once 5+ are done, Claude writes the patterns here (what he cuts, adds, his words), with his rewrites as the samples.*

```
[Sample 1 — paste raw]
```

```
[Sample 2 — paste raw]
```

---

## Q3 — What are your 2-3 biggest priorities for the next 90 days?

Quarterly priorities. Not yearly aspirations. Things that, if not done by July, would make you say "I wasted Q2."

```
1. Become confident setting up a Standard AI OS for someone brand new to AI, using a repeatable set-up kit (projects/ai-os-setup-kit/). Done when someone can be set up just by following the plan.
2. First 2-3 free set-ups for friends and family, recorded with consent (recordings in a private repo).
3. YouTube channel: proof videos that non-coders can build a running AI OS.
Source: context/current-focus.md (refresh by 2027-01-08)
```

---

## Q4 — Where does revenue actually land, and where is it tracked?

Multiple answers OK. Stripe? Skool? GoHighLevel? QuickBooks? A spreadsheet?

```
None yet: the channel and set-up kit are pre-launch, and the first set-ups are free. Not applicable until there is revenue (financial details stay out of this public repo).
```

---

## Q5 — Where do you talk to customers, your team, and the outside world day-to-day?

Email (which one — Gmail / Outlook)? Slack? Teams? DMs (Skool / Discord / iMessage)? Phone?

```
Not recorded in the repo yet. Known tools: Gmail and Google Calendar are connected as claude.ai connectors (connections.md). Answer pending from Charlie.
```

---

## Q6 — Where do meeting recordings, notes, and important docs live?

Granola? Otter? Fireflies? Google Drive? Notion? Dropbox? A folder on your desktop you keep meaning to organize?

```
This repo (GitHub) for notes, decisions and research; Google Drive connected; set-up session recordings will go in a private "sessions" repo. Source: connections.md, brainstorms/2026-10-08-who-i-am.md
```

---

## Q7 — What's the one task that eats your week, and where do you currently track work?

The single biggest time-suck or recurring drudgery. Plus where tasks/projects live (ClickUp / Asana / Linear / Notion / a notebook).

```
Work is tracked in this repo: context/current-focus.md (priority, Next step, Parking Lot) and projects/. The task that eats the week: not recorded yet; pending from Charlie.
```

---

When this file is filled, run `/onboard` (or re-run it) and the wizard will scaffold your Day-1 file set: `context/`, `references/voice.md`, populated `connections.md`, and a filled `CLAUDE.md`.
