# Second Brain OS test

Charlie, 15 Oct 2026: start undefined-ui/second-brain-os **as it is and as
intended**, then add the ingest scripts we already have (`system/ingest-scripts.md`)
and see whether it's better at backlinks and related-note links than this repo.

## The test
1. New private repo from second-brain-os, unchanged. Follow its own setup guide.
2. Copy our ingest scripts in, pointed at its vault folders.
3. Ingest the same small set of sources into both: 3 Nate Herk transcripts
   already in `research/nate-herk/`.
4. Measure both with `python3 tools/link_count.py <folder>`. Then open 5
   notes in each and check by hand whether the related links make sense.

## Baseline (this repo, 15 Oct)
373 notes, 1,075 links, 2.9 per note, 90% have a backlink, 12 orphans (3%).
Almost all are plain Markdown links; only 2 `[[wiki links]]`, so Obsidian's
backlinks pane would show little here.

## Better means
More links per note **and** the hand check finds them useful (not just more).
