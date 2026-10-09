---
name: research-creator
description: Researches a YouTube creator end to end: video list, X posts, 3 transcripts, a lesson, then commit. Use when Charlie says "research <creator>", "add a creator", or names a creator to study.
---

# Research a creator

Turns one creator's name into a finished `research/<creator>/` folder: video
inventory, X posts, 3 transcripts, a checked lesson and flashcards.

Before starting, read `context/environment.md` (what works from the cloud) and
`context/current-focus.md` (what Charlie is learning now).
`<creator>` below is the folder name: lower-case, hyphens (e.g. `nick-saraev`).

## Steps

### 1. Find the channel and list its videos
Use the `youtube-ingest` skill, step 1 (find the channel, then list its videos).
In parallel, do (b) below.

### 2. In parallel (fire both at once)
**(a) Video inventory.** Write `research/<creator>/README.md` in the same format as
`research/nick-saraev/README.md`: channel link, focus line, a **Coverage** line
(`N videos listed (date, newest first), M transcribed`), why Charlie wants
them, a **Start with (★)** line, then the table
`| # | Video | Views | Length | Transcript |` with `–` in the Transcript
column until a transcript exists. Mark the 3 starters (step 3) with ★.

**(b) X posts.** Find the creator's X handle with a web search (check it's
their verified/linked account), then:
```bash
python3 research/get_x_posts.py <creator> <handle>
```
It retries the API's random 404s itself. If there's no X account, or it still
fails, note that in the README and move on.

### 3. Pick 3 starters and fetch transcripts — ONE AT A TIME
Choose the 3 videos most relevant to Charlie's current priority in
`context/current-focus.md`, then fetch them with `youtube-ingest` step 3
(one at a time; it queues the rest for GitHub if rate-limited). Update the README's Transcript column to
`✅ [transcript](<title>--<id>-transcript.md)` only for files that actually exist
(`python3 tools/update_coverage.py` does this for you). The script names files
from the video title automatically; never rename them by hand.

### 4. Lesson in the background
Launch the `video-tutor` agent (`.claude/agents/video-tutor.md`) **in the
background**, pointing it at `research/<creator>/` and its transcripts; it
writes `research/<creator>/lesson-<topic>.md`.
While it runs, add or update the creator's row in `research/README.md`
(Creator | Topic | Videos | Transcribed | Lessons), and remove them from the
Parking Lot / "Queued" line if they were there.

### 5. Check, flashcards, commit
When the lesson arrives:
1. **Spot-check 3 quotes/timestamps** against the `*-transcript.md` files
   (grep the quote; open the `&t=` time). Fix anything wrong or unsupported.
   Fill in the Lessons link in `research/README.md`.
2. **Flashcards** (skip while parked: `context/current-focus.md`): add 3–5 multiple-choice cards to the flashcard app's
   `cards` database with the `ArtifactData` tool (app URL is in `AGENTS.md`).
   List the collection first to find the next free number. Each card:
   `id`/doc id `cNN` (next free), `n` (next free number), `q` (plain-English
   question), `choices` (**correct answer first**, 3–4 options), `a` (correct
   answer), `topic` (one of `skills`, `git`, `ai-os`, `environment`, `words`),
   nothing else (no scores: the app just shows right/wrong). Write them in one
   `batch`. Then regenerate the backup table in `learning/flashcards.md`.
3. **Commit:** create a branch (e.g. `claude/research-<creator>`), commit the
   `research/` and `learning/` changes, push it, then fast-forward merge into
   `main` and push `main`. Don't open a pull request unless Charlie asks.

### 6. Report to Charlie
- **Coverage:** `N listed / M transcribed / K unavailable` — exactly what was
  fetched, nothing more.
- Link to the lesson file and the 3 starter videos.
- Finishing a creator is a milestone: give the flashcard app link for the new
  cards (see `context/how-i-learn.md`).
- End with one **Now:** and one **Done when:** (usually: read the lesson and
  do its practice task).

## Rules
- **Public repo:** nothing private, health, financial or client-related goes
  in any file.
- **Skool** needs Charlie's login and forbids scraping: ask him to paste what
  he wants processed.
- **Never claim coverage you don't have.** A video listed is not a video
  watched; only transcribed videos count as "covered".
- Keep the lesson's three buckets separate: **principles** (lasting),
  **preferences** (what works for the creator), **promotion** (sponsors, their
  own products/courses).
