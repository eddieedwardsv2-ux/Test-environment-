---
name: brain-ingest
description: Adds a new source to a creator brain (research/<creator>/brain/) and updates every page it touches. Use for "ingest <link>", "add this to Nate's brain", "brain refresh".
---

# Ingest into a creator brain

Nate Herk's "ingest" step (research/nate-herk/i-built-another-andrej-karpathy-using-claude--bvGptCLDhyo-transcript.md,
9:08–9:38): one new source in, every affected page updated, nothing edited by
hand. A brain lives in `research/<creator>/brain/`:
`index.md` (coverage), `concepts.md` (ideas from videos), `x-themes.md`
(opinions from X), `rules.md` (operating rules, each with quotes),
`log.md` (what was added when).

## Steps
1. **Work out what's new.** Read `brain/index.md` and `brain/log.md`. New
   sources are transcripts in `research/<creator>/` not listed as ingested,
   or a link Charlie gives. Charlie decides what goes in; ingest only what
   will still be useful in a year (Nate, DTCyvo6cC54 27:23); fast-changing
   data is fetched live instead.
2. **Get the raw source** (parallel where possible):
   - YouTube link: `python3 research/get_transcript.py <creator> <id>`; if
     UNAVAILABLE, queue it (`research/transcript-queue.txt`) and trigger
     GitHub (see `context/environment.md`), then continue when it lands.
   - X: `python3 research/get_x_posts.py <creator> <handle>`.
   - Anything else (blog, post, Skool): Charlie pastes it; save it as
     `research/<creator>/<short-name>-source.md` with its link and date.
3. **Update the pages** with a background agent (one per page if several
   pages are affected, so they run in parallel; never two agents on one file):
   - `concepts.md`: add new ideas; add "Also: <link>" to ideas the source
     supports; add contradictions.
   - `rules.md`: a provisional rule that gains a second independent source
     becomes confirmed; a new recurring principle becomes a provisional rule.
   - `x-themes.md`: only for X sources.
   Quotes must be verbatim (trim with "…"); never put a summary in quote marks.
   Parallel page updates are drafts until step 4 has checked they agree.
4. **Check** before saving (one integration step, after all page agents
   finish): `index.md`, `concepts.md`, `rules.md`, `log.md` and the source
   links agree with each other (same sources, same rule status); then every new link appears in a source file (grep),
   and spot-read 3 new quotes. Fix anything unsupported.
5. **Bookkeeping:** update `index.md` coverage, add a dated `log.md` entry
   (source, pages changed, rules promoted), update the creator's README
   Transcript column, run `python3 tools/audit.py`.
6. **Save:** branch, commit, push, fast-forward merge into main. If any Git
   step is refused (no write access), stop, say exactly which step failed,
   and don't report the brain as updated.
7. **Report** in 3 lines: what went in, what changed, any rule promoted.
   A brain update is a milestone: mention new flashcards if you added any. Skip while flashcards are parked (`context/current-focus.md`).
