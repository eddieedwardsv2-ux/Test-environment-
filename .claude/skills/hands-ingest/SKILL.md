---
name: hands-ingest
description: Feeds the Hands Brain (tools, skills, plugins, MCPs, repos) from a YouTube channel week by week, newest first, then ranks what's best to use now and rebuilds its site. Use for "update the Hands Brain", "update the tools list", "what's new this week", "add <channel> to Hands".
---

# Hands ingest (newest video first, then backfill)

The Hands Brain (`research/hands/`) learns and teaches the tools people use
with AI. First source: The Next New Thing (weekly round-ups). Same idea as
`brain-ingest`, but the unit is a **tool**, and newer tools can replace older ones.

## Order (Charlie, 2026-10-09)
Always take the **newest video not yet in** first, so new tools are tested
against the ones we already know. Backfill older weeks (W38, then earlier)
only when nothing newer is waiting. Each new tool gets a head-to-head with the
current number one in its category (`vs` field below), so we find what we're
missing and close the gap in knowing how to use it.

## Steps
1. **List, free:** `python3 research/hands/pipeline.py --weeks <n>` writes
   `research/hands/sources/<creator>/videos.json`: newest first, ISO week,
   the show's own link list and chapter times from each description.
   Descriptions name almost every tool, so this step alone gives the list.
2. **Transcripts** (to know what they actually *show*): `python3 research/get_transcript.py <creator> <id>`
   in a background loop with pauses; failures go in `research/transcript-queue.txt`.
   A week can be classified once its transcripts are in.
3. **One helper per week** (`model: sonnet`, parallel; each writes only its
   own `research/hands/weeks/<YYYY-Www>.json`, schema below). It reads that
   week's descriptions, chapters and transcripts. Work newest week first.
4. **Merge, rank, build:** `python3 tools/build_hands.py` merges every week
   into `research/hands/tools.json`, ranks each category, marks what's been
   replaced, and builds `research/hands/site/hands.html`; republish it (link
   in `system/pages.md`).
5. **Check:** spot-check 3 tools' timestamps against the transcript, run
   `python3 tools/audit.py`, then commit and push.

## Week file schema (`weeks/<YYYY-Www>.json`)
`{"week", "videos": [ids], "summary": "2-3 plain lines: the week's theme",
"tools": [{"name", "url", "kind": "skill|plugin|mcp|repo|app|model|service",
"category": one of CATEGORIES in tools/build_hands.py,
"what": "one plain line", "shown": "what they actually demonstrated, one line, or ''",
"price": "free|open-source|freemium|paid|unknown",
"for_charlie": 0-3 (3 = use now for Claude Code, his AI OS or YouTube channel),
"replaces": ["older or rival tools it beats, by name"], "video", "t": "m:ss",
"quote": "verbatim line from the transcript that supports 'what' or 'shown', or ''",
"check": "claims to verify (money, 'free', benchmark numbers), or ''",
"vs": {"tool": "current #1 in its category in research/hands/tools.json", "verdict": "newer wins | leader stays | different job", "gap": "what we still don't know about using it, one line"} or null}]}`
Rules: titles are clickbait ("make money"), so judge on what is shown.
Sponsors and the show's own links are not tools. Quotes must be verbatim.
One entry per tool per video; the merge step joins repeats.
