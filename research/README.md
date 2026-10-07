# Research wiki — index

One folder per creator. Each folder has a README (video list + coverage
status), `<video-id>-transcript.md` files, and `lesson-*.md` files written by
the `video-tutor` agent. Anything not from a transcript is marked as such.

| Creator | Topic | Videos | Transcribed | Lessons |
|---|---|---|---|---|
| [Nate Herk](nate-herk/README.md) | AI OS, second brain, Claude Code | 2 | 2 | [AI OS + second brain](nate-herk/lesson-ai-os-and-second-brain.md) |

**Queued (Parking Lot):** Dan Martell (second brain), The Next New Thing
(GitHub tools roundups; 159 videos listed, none transcribed).

**Add a creator:** `python3 research/get_transcript.py <creator-folder> <url>`
(a few videos at a time — rate-limited), then ask the `video-tutor` agent.
