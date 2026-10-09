# Hands Brain

The OS's "hands": every tool, skill, plugin, MCP server and repo worth
knowing, learned week by week and ranked so the best one to use **now** is
always on top. Started 2026-10-08 (Charlie). Site: see `system/pages.md`.

**Sources:** The Next New Thing (weekly round-ups), newest week first, and the
skills.sh leaderboard (most-installed agent skills; `skills_sh.py`). More later
(e.g. the Anthropic community marketplace), same pipeline.

| File | What |
|---|---|
| `pipeline.py` | Step 1: video list + descriptions (free; the show lists its own links and chapters) |
| `sources/<creator>/videos.json` | One entry per video: date, ISO week, links, chapters, transcript path |
| `weeks/<YYYY-Www>.json` | One helper's classification of that week (schema in `.claude/skills/hands-ingest/SKILL.md`) |
| `tools.json` | Built: every tool merged, ranked per category, replaced ones marked |
| `enate-links.json`, `nate-mentions.json` | Each tool's links to ENATE concepts; tools Nate himself uses (verbatim quotes) |
| `site/` | `template.html` + built `hands.html` (`python3 tools/build_hands.py`) |

**Why this is the efficient route:** the descriptions already name every tool
with its link and chapter time, so the tool list costs nothing and isn't
rate-limited. Transcripts (free, slower) are only needed for what each video
actually *shows*, and they download in the background while earlier weeks are
classified. Ranking: Charlie's relevance × 3, mentions × 2, recency, price, and for skills.sh
skills up to 3 points for installs (10k = 1, 100k = 2, 1M+ = 3).
Ask it questions with the `hands-brain` agent.
