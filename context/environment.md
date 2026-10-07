# Environment facts (cloud sessions)

Tested 2026-10-07. Re-test anything older than a few months before relying on it.

## YouTube
- YouTube blocks this cloud server's IP. These all FAILED for transcripts:
  yt-dlp (4 player clients), youtube-transcript-api, Invidious caption
  endpoints, transcript websites (plain fetch AND headless Chromium via
  Playwright: Cloudflare/login walls), WebFetch.
- WORKS for listing: video lists, titles, descriptions, chapters
  (yt-dlp `--flat-playlist`; Invidious `https://invidious.f5.si/api/v1/videos/<id>`).
- WORKS for transcripts, no sign-up: `python3 research/get_transcript.py <creator> <url>`
  (youtube-transcript.ai's free keyless endpoint). Rate-limited after ~4 calls,
  so fetch a few videos at a time.
- Fallbacks: Supadata (~100/month free) or TranscriptAPI (100 trial) need
  Charlie's sign-up; keys go in an environment secret, never in git. On his
  own devices: paste from youtubetotranscript.com on his phone, or on the Mac
  `yt-dlp --skip-download --write-auto-subs --sub-langs en <url>`.

## GitHub
- `gh` / GitHub API works only for this repo; other repos need `add_repo`.
- GitHub GraphQL is not available; use the REST API.

## Tools available
- Chromium + Playwright are pre-installed (`/opt/pw-browsers`).
- Node 22, Python 3.13, ffmpeg.
