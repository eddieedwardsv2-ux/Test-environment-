# Environment facts (check the current host)

## ChatGPT Work session, checked 2026-10-09
- GitHub reads and writes work through the connected GitHub integration.
  Command-line clone/fetch work, but push lacked HTTPS credentials. Do not
  ask for a password: use create_tree/create_commit/update_ref with an
  expected-head guard and verify remote content. Successful reference commit:
  3955b69405f442e176e0c0158bce0dee9efdeca0. Never force overwrite concurrent work.
- Claude session/artifact access is separate: browser reached sign-in; no
  ArtifactData or artifact publishing tools are exposed here. A GitHub push
  does not republish a Claude artifact. Report that boundary explicitly.
- Node Playwright package exists but its browser executable was missing.
  Mocked tests do not count as screenshots or a live persistence round-trip.
- Notion tools are exposed; no content read was performed in this session.
  Drive removal returned not installed. Start at GitHub and use Notion instead.

## Earlier Claude cloud session (historical, tested 2026-10-07)
Re-test on the current host before relying on these facts.

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
- Reading Actions runs works with `gh api` (tested 2026-10-08:
  `gh api "repos/eddieedwardsv2-ux/Test-environment-/actions/runs?per_page=3"`),
  so the claude.ai GitHub connector is not needed to check Cadence. If it is
  ever needed (PR reviews in chat), the sign-in link is https://claude.ai/connect-github.
- `claude doctor` runs here (tested 2026-10-08) but only checks the cloud
  container's install; its 3 warnings there are about the container, not this
  repo. For context, use `python3 tools/context_check.py` (our /doctor).
- GitHub GraphQL is not available; use the REST API.

## Tools available
- Chromium is pre-installed (`/opt/pw-browsers`); the Python `playwright`
  library is NOT (tested 2026-10-07): `pip install playwright` (free) each
  session before `tools/screenshot.py`. Never run `playwright install`.
- Node 22, Python 3.13, ffmpeg.
