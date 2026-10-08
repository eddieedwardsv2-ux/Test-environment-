# Research wiki — index

One folder per creator. Each folder has a README (video list + coverage
status), `<title>--<video-id>-transcript.md` files (named automatically; the
`-raw.txt` twin is the untouched download), `lesson-*.md` files written by
the `video-tutor` agent, and sometimes a `brain/` (derived knowledge an
advisor agent reads; raw evidence stays in the transcripts). Anything not from a transcript is marked as such.

| Creator | Topic | Videos | Transcribed | Lessons |
|---|---|---|---|---|
| [Nate Herk](nate-herk/README.md) | AI OS, second brain, Claude Code (current foundation) | 359 listed ([all](nate-herk/videos.md)) | 23 | [AI OS + second brain](nate-herk/lesson-ai-os-and-second-brain.md) |
| [Nick Saraev](nick-saraev/README.md) | How to think about and use AI; Claude Code, Codex courses | 316 listed | 10 | [How Nick thinks](nick-saraev/lesson-how-nick-thinks.md) · [Nick's brain](nick-saraev/brain/index.md) |
| [Andrej Karpathy](andrej-karpathy/README.md) | How LLMs work; teaching by building; rigour | 17 listed | 4 | – |
| [The Next New Thing](the-next-new-thing/README.md) | Free GitHub tools round-ups | 159 listed | 2 | [Watch plan (top 10)](the-next-new-thing/watch-plan.md) |

**Queued (Parking Lot):** Dan Martell (second brain).

**Add a creator:** `python3 research/get_transcript.py <creator-folder> <url>`
(a few videos at a time — rate-limited), then ask the `video-tutor` agent.
