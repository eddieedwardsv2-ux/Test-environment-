---
name: research-creator
description: Researches a YouTube creator end to end for Charlie — finds the channel, lists every video, saves X posts, fetches 3 starter transcripts, gets the video-tutor agent to write a lesson, adds flashcards and commits it all. Use when Charlie says "research <creator>", "add a creator", "look into <name>'s channel", or just gives a creator's name to study.
---

# Research a creator

Turns one creator's name into a finished `research/<creator>/` folder: video
inventory, X posts, 3 transcripts, a checked lesson and flashcards.

Before starting, read `context/environment.md` (what works from the cloud) and
`context/current-focus.md` (what Charlie is learning now).
`<creator>` below is the folder name: lower-case, hyphens (e.g. `nick-saraev`).

## Steps

### 1. Find the channel
```bash
yt-dlp --flat-playlist --playlist-end 3 --print "%(channel)s | %(channel_url)s | %(title)s" "ytsearch3:<name>"
```
If the results show more than one plausible channel, or none matches the name,
ask Charlie which one before going on.

### 2. In parallel (fire both at once)
**(a) Video inventory.**
```bash
yt-dlp --flat-playlist --print $'%(id)s\t%(title)s\t%(view_count)s\t%(duration)s' "<channel_url>/videos"
```
(`$'...'` makes `\t` a real tab. Duration is in seconds: convert to `m:ss`
or `XhYY` like the example.)
Write `research/<creator>/README.md` in the same format as
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
`context/current-focus.md`. Run them as separate, sequential calls (the free
service is rate-limited after ~4 calls; never in parallel):
```bash
python3 research/get_transcript.py <creator> <video-id>
```
If a call prints `UNAVAILABLE`, stop fetching. Tell Charlie which videos are
missing and ask him to paste the transcript from youtubetotranscript.com on
his phone. Update the README's Transcript column to
`✅ [transcript](<id>-transcript.md)` only for files that actually exist.

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
2. **Flashcards:** add 3–5 multiple-choice cards to the flashcard app's
   `cards` database with the `ArtifactData` tool (app URL is in `AGENTS.md`).
   List the collection first to find the next free number. Each card:
   `id`/doc id `cNN` (next free), `n` (next free number), `q` (plain-English
   question), `choices` (**correct answer first**, 3–4 options), `a` (correct
   answer), `topic` (one of `skills`, `git`, `ai-os`, `environment`, `words`),
   `box: 1`, `due: <tomorrow's date>`, `right: 0`, `wrong: 0`. Write them in one
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
