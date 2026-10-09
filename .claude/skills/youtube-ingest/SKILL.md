---
name: youtube-ingest
description: Gets YouTube videos into any brain: lists a channel newest first, triages what's worth reading, fetches transcripts (queueing them when rate-limited), then hands each one to the brain that asked. Use for "get the new videos from <channel>", "fetch this video", "list <creator>'s videos".
---

# YouTube ingest (getting videos in, for every brain)

One place for the YouTube steps (Charlie, 2026-10-09, "middle-go"). Each brain
skill keeps only "what does this mean for us". Read `context/environment.md`
first: what works from the cloud. `<creator>` is the folder name in
`research/` (lower case, hyphens, e.g. `nick-saraev`).

## 1. List (free)
- A new creator's channel:
  ```bash
  yt-dlp --flat-playlist --playlist-end 3 --print "%(channel)s | %(channel_url)s | %(title)s" "ytsearch3:<name>"
  ```
  If the results show more than one plausible channel, or none matches the
  name, ask Charlie which one before going on (on the Decision Desk).
- A channel's videos, newest first:
  ```bash
  yt-dlp --flat-playlist --print $'%(id)s\t%(title)s\t%(view_count)s\t%(duration)s' "<channel_url>/videos"
  ```
  (`$'...'` makes `\t` a real tab. Duration is in seconds: convert to `m:ss` or `XhYY`.)
- The Next New Thing for the Hands Brain: `python3 research/hands/pipeline.py --weeks <n>`
  (descriptions, the show's link list and chapter times, ISO week per video).

## 2. Triage: read as little as possible (Charlie, 2026-10-09)
Spend usage only where the brain has a gap. Record every call in
`research/<creator>/triage.md`.
- **Tier 0 (free):** titles from the video list. Drop news, model tests and
  how-tos for tools we don't use.
- **Tier 1 (cheap):** description and chapters (`yt-dlp --skip-download
  --print "%(description)s"`). `grep` the brain for each chapter's topic; a
  topic with 0 or 1 hits is a gap.
- **Tier 2 (free fetch):** add gap videos to `research/transcript-queue.txt`
  and push; GitHub fetches them with no Claude usage.
- **Tier 3 (spend):** when Charlie has time to spare (or says "ingest the
  queue"), read only the chapters that matched, then hand over (step 4).
Everything else stays listed as "Spare time" or "Skip" in the triage file.

## 3. Fetch transcripts: one at a time
```bash
python3 research/get_transcript.py <creator> <video-id>
```
Run them as separate, sequential calls (the free service is rate-limited
after ~4 calls; never in parallel; a background loop with pauses is fine for
many). If a call prints `UNAVAILABLE`, stop and add the rest to
`research/transcript-queue.txt` (`<creator> <video-id>` per line), commit,
push, and trigger the queue (command in `context/environment.md`). GitHub
fetches them within the hour; pull, then continue. The script names files
from the video title; never rename them by hand. Then run
`python3 tools/update_coverage.py` to tick the README's Transcript column.

## 4. Hand over to the brain that asked
- A known creator's brain (Nate = ENATE, Nick): `brain-ingest`, from its step 3.
- The Hands Brain (tools): `hands-ingest`, from its step 3.
- A new creator: `research-creator`, from its step 4.
