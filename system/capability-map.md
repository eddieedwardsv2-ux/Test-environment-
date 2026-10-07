# Capability map — check this before building anything

Reuse order: existing route → existing script → existing skill → existing
agent → combine them → new capability only if nothing fits (then add it here
and to `AGENTS.md`; `tools/audit.py` fails if a skill or agent isn't routed).

| I need to… | Use | It produces | Checked by |
|---|---|---|---|
| Find where something lives | `AGENTS.md` | the right path | following it |
| Research a new creator | `research-creator` skill | video list, X posts, 3 transcripts, lesson | coverage + quote spot-check |
| Fetch a transcript | `research/get_transcript.py` | `<title>--<id>-transcript.md` + raw | audit (name, partial check) |
| Fetch when rate-limited | `research/transcript-queue.txt` → GitHub Actions hourly | committed transcripts | queue cleanup + audit |
| Fetch X posts | `research/get_x_posts.py` | `x-posts.md` | post count |
| Tick coverage / counts | `tools/update_coverage.py` | README ticks and counts | audit counts |
| Add sources to a brain | `brain-ingest` skill | updated concepts, rules, index, log | quote + link checks |
| Turn transcripts into a lesson | `video-tutor` agent | `lesson-*.md` | timestamp spot-check |
| OS / routing / brain design advice | `nate-brain` agent | sourced advice | links to transcripts |
| Nick's view on a plan | `nick-brain` agent | sourced advice | links to transcripts |
| Teach Charlie a topic | `teach` skill | active lesson, flashcards | 7-rule self-check |
| Find or install a new skill | `find-skills` skill | install command | Charlie's OK |
| Check a page looks right (visual validation) | `tools/screenshot.py <page>` then open the PNGs | phone + desktop screenshots, script errors | looking at them |
| Structural audit (incl. every checklist quote, `tools/check_quotes.py`) | `tools/audit.py` (runs on push and as the Stop-hook gate `tools/run_gate.sh`) | errors/warnings | GitHub Actions |
| Reasoning audit (weekly) | `os-audit` skill | `audits/YYYY-MM-DD.md` + smallest fixes | Charlie approves fixes |
| Interview Charlie to capture what he knows | `grill-me` skill | `brainstorms/YYYY-MM-DD-<topic>.md` | Charlie confirms the summary |
| Start a new, blank AI OS | `templates/standard-ai-os-v1/` | router + filing cabinet | fresh-session routing test |
| Flashcards | app + `cards` database (see `AGENTS.md`) | cards | backup in `learning/flashcards.md` |
| A deliverable (e.g. a video plan) | `projects/<name>/` | project files | the project's own done-when |
