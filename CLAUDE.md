# Working with Charlie

Charlie is a beginner learning Claude Code and Codex, building towards a YouTube
channel. Explain in plain UK English, one next step at a time, ending with
**Now:** and **Done when:**. Keep a Parking Lot for new ideas.

## Before saying "can't" or "not available"
1. Search the web/GitHub for how others do it.
2. Try at least 3 genuinely different methods.
3. Report exactly what is blocked, where, and the workaround.
Never stop after a single failed attempt.

## Known environment facts (cloud sessions)
- YouTube blocks this cloud server's IP: yt-dlp, youtube-transcript-api,
  Invidious caption endpoints, transcript websites (plain fetch AND headless
  Chromium via Playwright: Cloudflare/login walls) and WebFetch all failed
  for transcripts (tested 2026-10-07). Video lists, titles and descriptions
  DO work (yt-dlp `--flat-playlist`, Invidious `/api/v1/videos/<id>`).
- WORKS (no sign-up): `python3 research/get_transcript.py <creator> <url>`
  uses youtube-transcript.ai's free keyless endpoint. Rate-limited after
  ~4 calls, so fetch a few videos at a time. Fallbacks needing sign-up:
  Supadata (~100/month free), TranscriptAPI (100 trial); key goes in an
  environment secret, never in git.
- Transcripts work on Charlie's own devices: paste from a transcript site
  opened on his phone, or on his Mac run
  `yt-dlp --skip-download --write-auto-subs --sub-langs en <url>`.
- `gh` / GitHub API is limited to this repo; other repos need `add_repo`.

## Layout
- `research/<creator>/` — one folder per creator: video inventory,
  coverage status, notes. Mark anything not from a transcript as such.
- `.claude/skills/` — project skills (e.g. find-skills from vercel-labs/skills).
