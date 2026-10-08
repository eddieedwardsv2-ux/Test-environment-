# AI OS set-up kit

**Goal:** a repeatable kit for setting up a Standard AI-OS for someone brand
new to AI: prompts, skills, plugins and a step-by-step plan, built on the
blank copy in `templates/standard-ai-os-v1/`.

**Base (2026-10-08):** Nate's free AIS-OS kit (github.com/nateherkai/AIS-OS,
MIT). Each person clones it and runs its `onboard` interview; our job is the
beginner's step-by-step plan around it (accounts, first session, what to do in
week 1-2), not a rebuilt kit. Its parts are now in this repo too, so we use
what we teach.

**Done when:** someone can be set up just by following the plan, and the
next person gets the same result. Tested on 2-3 free set-ups with friends
and family.

**Privacy (public repo):**
- Each person's AI OS lives in its own private repo.
- Session recordings and transcripts go in one private "sessions" repo.
- Only the generic kit and anonymised lessons go here. No names.
- Nothing goes on YouTube without that person's consent.

**Files:** the step-by-step plan is [`plan.md`](plan.md) (draft v0.1); anonymised lessons from each set-up go in `lessons.md` (created after the first one).
Background: `brainstorms/2026-10-08-who-i-am.md`.

**Kit Compare** (our blank template and Nate's kit as two connected maps): https://claude.ai/artifact/62wSZBDKYTLCAq6yfcF1qR. Page source `compare/`; rebuild with `python3 tools/build_kit_compare.py` (it fetches Nate's kit), then republish.
