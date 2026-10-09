# Pages (dashboards Charlie opens)

Every published page, its link, its source and how to rebuild it. Republish
by publishing the same source file again (keeps the link).

| Page | Link | Source | Rebuild, then republish |
|---|---|---|---|
| **Decision Desk**: every question waiting for Charlie (the `decide` skill) | https://claude.ai/artifact/R7efnQ6QZtGKVsyV1fCuxx | `system/decision-desk/decision-desk.html` | none; questions live in its `decisions` database (ArtifactData) |
| **Hands Brain**: best tools to use now: a map (like Charlie's Brain, with ENATE links) and a ranked list | https://claude.ai/artifact/QVni63FtP7cG1z9UrajfCL | `research/hands/site/hands.html` | `python3 research/hands/pipeline.py`, week files (the `hands-ingest` skill), then `python3 tools/build_hands.py` |
| **OS Guide**: plain-English guide (what we built and why, skill groups, words, backtest) | https://claude.ai/artifact/UMdY5JYymKneEhi9ZLhewa | `system/guide/guide.html` | edit by hand when a part is added |
| **Lesson: new findings** (slides, 13): less context, the Desk, skills, ENATE, Hands Brain, backtest | https://claude.ai/artifact/NC9J9KZkE5Wb1vDKgntoGq | its own files on the page (Slides type) | edit slides on the page or ask Claude |
| **Brain dashboard**: our OS and Nate's brain as one map; review cards (keep / confusing / delete) | https://claude.ai/artifact/LhRdXG3KpeBnGpxNhFQsjf | `research/nate-herk/brain/map/brain-map.html` | `python3 tools/build_brain_map.py`; marks are in its `flags` database |
| **Nate-first map**: our OS today vs the same work started from Nate's kit | https://claude.ai/artifact/BM1CEX52wfMKT5G4B8X6ky | `system/merge-map/merge-map.html` | `python3 tools/build_merge_map.py` (rules and reasons in its MOVES table) |
| **Kit Compare**: our blank template vs Nate's kit | https://claude.ai/artifact/62wSZBDKYTLCAq6yfcF1qR | `projects/ai-os-setup-kit/compare/kit-compare.html` | `python3 tools/build_kit_compare.py` |
| **Flashcards** (parked) | https://claude.ai/artifact/BSzHf834mYsTUZJnyVo144 | `learning/flashcards-app.html` | none; its `cards` database is the source of truth. `learning/flashcards.md` is a backup: regenerate it after adding cards |

Check any page looks right: `python3 tools/screenshot.py <page>`, then look
at the PNGs (needs `pip install playwright` each cloud session).

## Older lesson pages (made before this repo's current layout)
Their "In your repo" sections name `MISSION.md` and `NOTES.md` from the first teaching set-up; today's equivalents are `AGENTS.md` and `context/`.

| Page | Link |
|---|---|
| What Makes an Agent (lesson 1, quiz) | https://claude.ai/artifact/CRvv2AY6mrwp2azFjsXHRa |
| The Agent Recipe (reference sheet) | https://claude.ai/artifact/RYSSnQtwR5a7RDqRJELzkZ |
| Nate Herk Watch Path (20 videos, ticks saved in your browser) | https://claude.ai/artifact/GWCvFJTreaJUAXFg9z4Kxr |
