# Plugin map: the 2,284 community plugins in 9 families

Source: Anthropic's community marketplace catalogue (`claude-community`,
connected in `.claude/settings.json`), sorted 2026-10-07 by each plugin's name
and first sentence. Shares are rough: a hand check of 30 random plugins put
about 7 in 10 in the right family. Use this to know *what kinds of thing
exist*, then search the catalogue for the specific one.

| # | Family | Rough share | What it does for you | Real examples |
|---|---|---|---|---|
| 1 | **Coding helpers** | ~1 in 3 | Review, test, fix and structure code; one per language or framework | `code-architecture-review`, `great-cto` (7-agent dev team), `consistent-ui` |
| 2 | **Claude's own habits** | ~1 in 8 | Change *how* Claude works: plans, multi-agent teams, cost and token tracking, session tools, suggesting skills | `superpowers`, `cost-guard`, `claude-lens`, `claude-codex-loop`, `skillers` |
| 3 | **App connectors** | ~1 in 10 | Let Claude use an app you already have | `notion`, `stripe`, `supabase`, `shopify-skills` |
| 4 | **Job & industry packs** | scattered (~50+) | Ready-made know-how for one profession: health, legal, education, property, e-commerce, HR, product management | `prepkit-product`, `claude-education-skills-library`, `learn-with-coursera` |
| 5 | **Research & web reading** | ~1 in 20 | Search Google/Amazon, read any web page as clean text, drive a browser | `serpapi-claude-plugin`, `markgrab`, `brightdata-plugin`, `hubcap` |
| 6 | **Make & understand media** | ~1 in 20 | Transcribe and "watch" videos, make images, video, slides, diagrams | `youtube-transcriber`, `watch-video`, `claude-transcribe` |
| 7 | **Memory & second brain** | ~1 in 20 | Give Claude lasting memory or a notes wiki (Obsidian) | `mindwright`, `obsidian-vault-for-claude-code`, `skill-seekers` |
| 8 | **Business: marketing, data, money** | ~1 in 7 together | Post and schedule social media, SEO, sales leads, dashboards, payments, crypto | `post-bridge`, `upload-post`, `claude-meeting-todos` |
| 9 | **Safety & going live** | ~1 in 10 together | Security checks before you trust code; put a site or app on the internet | `cybrix-deploy`, security scanners |

## How to ask for one
Describe the **job**, not the plugin: *"Is there a plugin that [does X] to
[thing] so I can [goal]?"* e.g. "…that posts a video to TikTok and YouTube
Shorts so I can share clips." Claude searches the catalogue (`find-skills`,
or `.claude-plugin/marketplace.json` in anthropics/claude-plugins-community),
reads the shortlist, and installs only what you approve.

## Charlie's watchlist (checked against current work, 2026-10-07)
Nothing installed yet; read each plugin before installing. Memory plugins save
to the computer they run on, so they only pay off on the Mac (cloud sessions
are wiped; this repo is the memory there).

| When | Plugin | Family | Why it fits |
|---|---|---|---|
| Now | `build-loud` | 2 / 8 | Turns work sessions into a build-in-public journal: raw material for "learning in public" videos |
| Now | `claude-patterns` | 2 | Scans sessions, journals and decisions for recurring patterns: could spot idea-switching and over-research early |
| Mac | `youtube-transcriber`, `watch-video` | 6 | Transcripts without rate limits; Claude "watches" demos the transcript misses |
| Mac | `claude-mem` or `bedrock` (Obsidian) | 7 | Lasting memory / Obsidian second brain, only if the repo approach starts to hurt (Nate: lowest level that fixes a pain) |
| Channel live | `postiz` or `post-bridge` | 8 | Schedule and post clips to YouTube, TikTok, Instagram and X from one place |
| Channel live | `vidIQ` (connector, not plugin) | 8 | YouTube keyword and channel research |

Families 1 (coding), 3 (app connectors), 4 (industry packs), 5 (research), 9
(safety) stay on the radar: e.g. if the decorating business returns, family 4
and 3 (job/quote software connectors) come first.
