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
- **Automatic queue (no phone, no sign-up):** add `<creator> <video-id>` lines
  to `research/transcript-queue.txt` and push. GitHub Actions
  (`.github/workflows/transcripts.yml`) runs hourly at :23, fetches up to 9 (3 jobs x 3)
  from GitHub's own IP (separate allowance) and commits them. Run it now with
  `gh api -X POST repos/eddieedwardsv2-ux/Test-environment-/actions/workflows/transcripts.yml/dispatches -f ref=main`
  (the `gh workflow` shortcut needs GraphQL, which is blocked here).
  yt-dlp on GitHub's runners is blocked by YouTube too (tested).
- Fallbacks: Supadata (~100/month free) or TranscriptAPI (100 trial) need
  Charlie's sign-up; keys go in an environment secret, never in git. On his
  own devices: paste from youtubetotranscript.com on his phone, or on the Mac
  `yt-dlp --skip-download --write-auto-subs --sub-langs en <url>`.

## X (Twitter)
- x.com needs a login, but FxTwitter's free API works with no sign-up:
  `python3 research/get_x_posts.py <creator> <handle>`. It randomly returns
  404 about half the time, so the tool retries.
- Skool: needs Charlie's membership login and its rules forbid scraping;
  he pastes in what he wants processed.

## GitHub
- `gh` / GitHub API works only for this repo; other repos need `add_repo`.
- GitHub GraphQL is not available; use the REST API.

## Tools available
- Chromium + Playwright are pre-installed (`/opt/pw-browsers`).
- Node 22, Python 3.13, ffmpeg.
