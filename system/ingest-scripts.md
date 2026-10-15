# Ingest scripts: what to copy into a new repo

Checked 15 Oct 2026. Every file below is on `main` in
`eddieedwardsv2-ux/test-environment-` and pushed (working tree clean, `main`
level with `origin/main`). This repo stays as the master copy. Copy files
out of it rather than moving them.

## Scripts (the code that fetches things)
| File | What it ingests | Needs |
|---|---|---|
| `research/get_transcript.py` | One YouTube transcript (youtube-transcript.ai, free) | nothing |
| `research/process_queue.py` | Works through `research/transcript-queue.txt` every hour | the workflow below |
| `research/get_x_posts.py` | A creator's recent X posts (FxTwitter, free) | nothing |
| `research/hands/pipeline.py` | A channel's videos, descriptions and featured links (Invidious) | nothing |
| `research/hands/skills_sh.py` | skills.sh leaderboard snapshot | nothing |
| `research/hands/anthropic_market.py` | Anthropic plugin catalogs snapshot | nothing |
| `tools/build_hands.py` | Rebuilds the Quartermaster page from the ingested weeks | `tools/graph_lib.py` |
| `tools/update_coverage.py` | Updates brain coverage after an ingest | — |
| `.github/workflows/transcripts.yml` | Runs the transcript queue hourly on GitHub | `research/process_queue.py` |

## Skills and agents (the instructions that use them)
- `.claude/skills/youtube-ingest/`: list, triage, fetch, hand over
- `.claude/skills/brain-ingest/`: new source into a creator brain
- `.claude/skills/hands-ingest/`: Quartermaster tool list
- `.claude/skills/research-creator/`: new creator end to end
- `.claude/agents/video-tutor.md`: transcripts into a lesson

## Not on main yet
- The Scrapling smoke-test workflow sits on the branch
  `codex/next-new-thing-tools-audit-2026-10-15`. It's a test of a scraping
  tool, not an ingest script, but it's saved on GitHub there.

## When copying
Paths inside the scripts assume this repo's layout (`research/<creator>/`,
`research/hands/`). If the new repo uses a different layout, such as
second-brain-os's vault, change the folder paths in each script and test one
real fetch before trusting it.
