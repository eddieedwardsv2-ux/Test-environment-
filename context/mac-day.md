# Mac day checklist

Read this when Charlie says **"I'm on Mac"** (or that the Mac has arrived).
It collects everything parked "for the Mac" in one place. Go through it one
item at a time, with **Now:** / **Done when:**, and ask before any install,
sign-up or payment. Tick items off here and log each one in `decisions.md`.

1. **Clone the repo on the Mac** (free): GitHub Desktop or `git clone`, so
   Claude Code and Codex run locally, not only in the cloud.
2. **Obsidian** (free on the Mac, no account needed): open the repo folder as
   a vault and look at Graph view. Compare it with the Brain dashboard
   (https://claude.ai/artifact/LhRdXG3KpeBnGpxNhFQsjf). Known gap: Obsidian
   only draws proper Markdown links (square brackets then the file in round brackets), and our router names files in
   backticks, so decide whether to add real links or keep the dashboard.
   Obsidian Sync (paid) is only needed to put the vault on the iPhone.
3. **Nate's `3d-brain` skill** (from his AIS-OS kit; local 3D view of the
   knowledge, like his "Herk Brain").
4. **Plugins:** context7 and superpowers; test the watch-video plugin.
5. **Codex check** (audit finding AIOS-b9f5-05; test plan `audits/evidence/2026-10-09-parity-test.md`):
   confirm Codex lists every skill through `.agents/skills`, answers the 5
   rulebook questions from test 1, and follows the three Codex fallbacks
   (agent file by hand, `tools/audit.py` before finishing, "Waiting on Charlie"). Also check what Codex blocks instead of our deny list.
- **Small Business plugin** (after Charlie's own choice to upgrade to Pro; his call, not ours): Claude desktop app → Customize → Plugins → + → Small Business, then say "get me started" (`smb-onboard`). Business details stay in the plugin, never this repo. Then one real trial with `try-tool` (e.g. a quote from job photos). Review: `research/hands/reviews/anthropic-marketplaces-2026-10-09.md`.
- **Optional: FreeLLMAPI trial** (only if Claude limits have started stopping sessions): one small public task on free models vs the Sonnet helper, with `try-tool`. Review: `research/hands/reviews/freellmapi-2026-10-09.md`.
