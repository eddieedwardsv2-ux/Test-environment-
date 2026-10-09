# Connections

Registry of every system this AI OS can reach (Nate's AIS-OS kit layout; see
`THIRD-PARTY-NOTICES.md`). The `audit` skill checks it for coverage and
freshness. "Last checked" means a successful read on that date, not just
"configured". Public repo: tool names and status only, never keys or account
details (keys: `context/environment.md`).

| # | Domain | Tool | Mechanism | Auth | Last checked |
|---|---|---|---|---|---|
| 1 | Revenue / Financials | — | not applicable yet (no revenue; channel and set-up kit are pre-launch) | — | — |
| 2 | Customer interactions | YouTube channel (later) | not yet connected | — | — |
| 3 | Calendar | Google Calendar | `mcp` (claude.ai connector) | connector sign-in | not checked |
| 4 | Communication | Gmail | `mcp` (claude.ai connector) | connector sign-in | not checked |
| 5 | Project / task tracking | This repo: `context/current-focus.md`, `projects/` | local files | GitHub | 2026-10-08 (push works) |
| 6 | Meeting intelligence | — | not applicable yet (set-up session recordings will live in a private repo) | — | — |
| 7 | Knowledge / files | This repo; Google Drive | local files; `mcp` (claude.ai connector) | GitHub; connector sign-in | repo 2026-10-08; Drive not checked |
| 8 | Content research: YouTube transcripts | youtube-transcript.ai | `script` (`research/get_transcript.py`; queue `research/transcript-queue.txt`, fetched hourly by GitHub Actions) | none (free, rate-limited) | 2026-10-08 (20 fetched) |
| 9 | Content research: X posts | X | `script` (`research/get_x_posts.py`) | none | not checked |
| 10 | YouTube analytics | vidIQ | `mcp` (claude.ai connector) | connector sign-in | not checked (parked until 5 videos) |
| 11 | Code hosting | GitHub | `git` over the session proxy; GitHub connector for PRs | session credentials; connector needs re-authorising | 2026-10-08 (git push works; connector asked for sign-in) |
| 12 | Video, images, thumbnails | Higgsfield | `mcp` (custom claude.ai connector `https://mcp.higgsfield.ai/mcp`, not in the official directory); or its skills + CLI on the Mac | Higgsfield account sign-in (paid credits) | 2026-10-09: server found and answers, not connected (Charlie adds it) |

**Mechanism options:** `mcp` (MCP server or claude.ai connector), `script`
(Python/Bash hitting an API, in `research/` or `tools/`), `export` (CSV/JSON
dump), `key+ref` (key in environment secrets + `references/{tool}-api.md`
guide), `not yet connected`.

When you wire a new tool, add a row here and save `references/{tool}-api.md`
with endpoints, auth flow and common queries: researched once, saved forever.
