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
| 7 | Knowledge / files | This repo; Notion | local files; `mcp` (claude.ai connector) | GitHub; connector sign-in | repo read 2026-10-09; Notion tools available in ChatGPT, content read not yet tested |
| 8 | Content research: YouTube transcripts | youtube-transcript.ai | `script` (`research/get_transcript.py`; queue `research/transcript-queue.txt`, fetched hourly by GitHub Actions) | none (free, rate-limited) | 2026-10-08 (20 fetched) |
| 9 | Content research: X posts | X | `script` (`research/get_x_posts.py`) | none | not checked |
| 10 | YouTube analytics | vidIQ | `mcp` (claude.ai connector) | connector sign-in | not checked (parked until 5 videos) |
| 11 | Code hosting | GitHub | `git` over the session proxy; GitHub connector for PRs | session credentials; connector needs re-authorising | 2026-10-08 (git push works; connector asked for sign-in) |
| 12 | Video, images, thumbnails | Higgsfield | `mcp` (custom claude.ai connector `https://mcp.higgsfield.ai/mcp`, not in the official directory); or its skills + CLI on the Mac | Higgsfield account sign-in (paid credits) | 2026-10-09: server found and answers, not connected (Charlie adds it) |
| 13 | Video and motion graphics | HyperFrames by HeyGen | `mcp` (claude.ai connector: read tools only from Claude Code; making videos needs its local skills, see `research/hands/tried.json`) | connector sign-in | 2026-10-09: connected; local trial rendered a title card |
| 14 | Slides, designs, social graphics | Moda | `mcp` (claude.ai connector) | connector sign-in | 2026-10-09: connected, not used yet |
| 15 | Notes and pages | Notion | `mcp` (claude.ai connector) | connector sign-in | 2026-10-09: connected, not used yet (this repo stays the source of truth) |
| 16 | Thumbnails, designs | Canva | `mcp` (claude.ai connector) | connector sign-in | 2026-10-09: sign-in not finished (Charlie) |
| 17 | Small business (quotes, invoices, reviews, social posts) | Claude for Small Business (Anthropic plugin, 44 skills) | `plugin` (claude.ai account; desktop app / Cowork, or Claude Code `small-business@knowledge-work-plugins`) | claude.ai plan; its own connectors (Gmail, Calendar, Drive, Canva, Xero, QuickBooks…) sign in separately | 2026-10-09: install card sent; not yet enabled. **Business data stays in the plugin, never in this repo** |

**Creative Claw (requested 2026-10-09):** media MCP/plugin for YouTube flows.
Install listing: https://chatgpt.com/plugins/creativeclaw . Connection and
content access not tested; directory search did not return a matching install
target. Workflow and first-trial checks: `projects/youtube-channel/README.md`.

**Mechanism options:** `mcp` (MCP server or claude.ai connector), `script`
(Python/Bash hitting an API, in `research/` or `tools/`), `export` (CSV/JSON
dump), `key+ref` (key in environment secrets + `references/{tool}-api.md`
guide), `not yet connected`.

When you wire a new tool, add a row here and save `references/{tool}-api.md`
with endpoints, auth flow and common queries: researched once, saved forever.

**Source preference (2026-10-09):** GitHub remains the project entry point.
Use Notion wherever Google Drive would previously have been used. ChatGPT
reported Google Drive not installed when removal was requested; Claude
connection status was not checked. No files were migrated or deleted.
