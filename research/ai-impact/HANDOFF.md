# Coverage and continuation

Snapshot: 12 October 2026. User request: ingest every public AI Impact video’s scripts and on-screen slides into a knowledge database.

## Actual coverage

- Channel resolved directly to `UCnNA2EuEVybpo3WGEace4HQ` (`@aiimpact1`). Public Videos tab listed 49 unique videos. Shorts and Streams tabs returned “This channel does not have a … tab”. Private, deleted, members-only and future uploads are outside this snapshot.
- All 49 English caption sources retrieved using the free native `youtube-transcript-api` route. Source captions were read and transformed into timestamp-linked knowledge records. 14,650 caption entries; approximately 105,165 words. These are captions, not confirmed original author scripts.
- Timing check: every last caption ends within 10 seconds of the listed video duration; no last caption overshoots by more than 5 seconds. This checks truncation at the tail, not transcription accuracy or every spoken word.
- Original source captions were working evidence; this public database contains derived paraphrases, source links, timing coverage and SHA-256 hashes rather than verbatim copies of the channel.
- 45 spoken references to a slide, diagram or on-screen visual were identified as review cues. They are not visual evidence and are not an exhaustive slide inventory.
- **Zero slides captured or OCR-verified.** Full visual ingestion remains BLOCKED.

## What failed

1. Existing `research/get_transcript.py` free keyless service now reports that an API key is needed. No account or key was created. Native YouTube captions worked instead.
2. A 720p video download reported success but saved a 195-byte HTML “Site Unavailable” page. `ffprobe` rejected it; it was not counted as a video.
3. Storyboard requests also returned a 195-byte error page and failed image decoding. No thumbnails were accepted as slides.
4. Browser playback showed a black player at 0:00; repeated Play did not yield readable video frames. No sign-in or paid-credit tools were used.

## Finish the visual layer

Use an environment with working video-media access, or user-provided video files. Start with the 45 entries in SQLite `visual_review_queue`, then inspect each whole video for additional slide changes. Captions do not reliably announce slides.

For each distinct slide or material screen change, retain video ID, frame timestamp, image hash, readable source frame, OCR text, diagram description, OCR corrections and reviewer status. Merge narration and visuals by timestamp, preserving differences. A slide stays pending until a reviewer checks its text against the original image; diagrams need visual interpretation as well as OCR. An inaccessible video remains explicitly blocked.

Original scripts or slide decks supplied by the creator can be ingested as additional sources. Do not assume a linked repository is identical to a slide without checking the video.

## Retrieve useful knowledge

Start with [index.md](index.md), read only relevant [video notes](videos/), then follow each evidence timestamp. Use [queries.sql](queries.sql) for SQLite searches. Shared topics create backlinks; a backlink means shared topic, not independent confirmation. Product claims, prices, security statements, model comparisons and income outcomes need current primary-source checks before implementation.

## Completion gate

Caption retrieval and first-pass derived knowledge extraction are complete for this 49-video snapshot; exhaustive spoken-content coverage and transcription accuracy are not verified. The full request is **NOT VERIFIED** until every video has visual coverage recorded, readable slides checked, and combined records reviewed. Do not report “all scripts and slides ingested” from caption coverage alone.
