# Research wiki — index

One folder per creator. Each folder has a README (video list + coverage
status), `<title>--<video-id>-transcript.md` files (named automatically; the
`-raw.txt` twin is the untouched download), `lesson-*.md` files written by
the `video-tutor` agent, and sometimes a `brain/` (derived knowledge an
advisor agent reads; raw evidence stays in the transcripts). Anything not from a transcript is marked as such.

**Council of elders** (each brain gets a voice, asked side by side): [council-plan.md](council-plan.md).

| Creator | Topic | Videos | Transcribed | Lessons |
|---|---|---|---|---|
| [Nate Herk](nate-herk/README.md) | AI OS, second brain, Claude Code (current foundation) | 360 listed ([all](nate-herk/videos.md)) | 73 | [AI OS + second brain](nate-herk/lesson-ai-os-and-second-brain.md); [smallest context](nate-herk/lesson-smallest-context.md) |
| [Nick Saraev](nick-saraev/README.md) | How to think about and use AI; Claude Code, Codex courses | 316 listed | 10 | [How Nick thinks](nick-saraev/lesson-how-nick-thinks.md) · [Nick's brain](nick-saraev/brain/index.md) |
| [Andrej Karpathy](andrej-karpathy/README.md) | How LLMs work; teaching by building; rigour | 17 listed | 4 | – |
| [AI Impact](ai-impact/README.md) | Company brains, AI OS, OODA, business data and automation | 49 public videos inventoried | 0 | [342 knowledge records](ai-impact/index.md); [visual gap](ai-impact/HANDOFF.md) |
| [Corey Haines](corey-haines/README.md) | Marketing skills; [NewsJack PR relationship](corey-haines/newsjack-relationship.md) (separate authors) | Not catalogued | 0 | – |
| [The Next New Thing](the-next-new-thing/README.md) | Free GitHub tools round-ups | 161 listed | 24 | [Watch plan (top 10)](the-next-new-thing/watch-plan.md); feeds the [Hands Brain](hands/README.md) |

**Official provider references:** [Anthropic + OpenAI](official-docs/README.md): 1,959 source URLs catalogued (1,745 body captures, 212 landing-only, 2 empty), 117 model references and 20 first-pass teaching records. Full source text is temporary; full ingestion/semantic review remains NOT VERIFIED.

**Queued (Parking Lot):** Dan Martell (second brain).

**Commands** (read `context/environment.md` first for any YouTube or GitHub task):
- Transcript: `python3 research/get_transcript.py <creator-folder> <url>` (a few at a time; rate-limited). If UNAVAILABLE, add `<creator-folder> <video-id>` to `transcript-queue.txt` (GitHub fetches hourly).
- X posts: `python3 research/get_x_posts.py <creator-folder> <handle>`.
- Then the `video-tutor` agent for a lesson, or the `brain-ingest` skill for a brain.

Older: a 4-hour watch plan across Karpathy, Nate and Nick (7 Oct, from titles only): [watch-plan-4h.md](watch-plan-4h.md).

**Recent primary-source comparison:** [poteto, Andrej Karpathy and Boris Cherny — five weeks](x-five-weeks/README.md), 7 September–12 October 2026. Available-source inventory, article access labels and targeted comparison; exhaustive coverage NOT VERIFIED.

**Experiments, 12 Oct 2026:** [1 free AI tools](free-ai-tools-experiment-1-2026-10-12.md) ([runtime](free-ai-tools-experiment-1-2026-10-12-runtime.md)) · [2 AI-OS architecture](ai-os-architecture-experiment-2-2026-10-12.md) · [3 quoting](quote-experiment-3-2026-10-12.md) · [4 knowledge-brain accuracy](knowledge-brain-accuracy-experiment-4-2026-10-12.md) · [5 model comparison](ai-model-comparison-experiment-5-2026-10-12.md) · [6 skills, plugins and MCPs](skills-plugins-mcps-experiment-6-2026-10-12.md) · [7 agent reliability](agent-reliability-experiment-7-2026-10-12.md) ([run packet](agent-reliability-experiment-7-agent-run-packet-2026-10-12.md), [cloud execution](agent-reliability-experiment-7-cloud-execution-2026-10-12.md)).
