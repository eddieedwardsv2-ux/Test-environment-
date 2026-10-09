# Capability map — check this before building anything

Reuse order: existing route → existing script → existing skill → existing
agent → combine them → new capability only if nothing fits (then add it here
and to `AGENTS.md`; `tools/audit.py` fails if a skill or agent isn't routed).

| I need to… | Use | It produces | Checked by |
|---|---|---|---|
| Find where something lives | `AGENTS.md` | the right path | following it |
| Ask Charlie a question; read his answers | `decide` skill, Decision Desk (`system/pages.md`) | a card he answers by tapping | `ArtifactData` list at session start |
| Open any dashboard, rebuild it | `system/pages.md` | link, source, rebuild command | `tools/screenshot.py` |
| Research a new creator | `research-creator` skill | video list, X posts, 3 transcripts, lesson | coverage + quote spot-check |
| Fetch a transcript | `research/get_transcript.py` | `<title>--<id>-transcript.md` + raw | audit (name, partial check) |
| Fetch when rate-limited | `research/transcript-queue.txt` → GitHub Actions hourly | committed transcripts | queue cleanup + audit |
| Fetch X posts | `research/get_x_posts.py` | `x-posts.md` | post count |
| Tick coverage / counts | `tools/update_coverage.py` | README ticks and counts | audit counts |
| Add sources to a brain | `brain-ingest` skill | updated concepts, rules, index, log | quote + link checks |
| Turn transcripts into a lesson | `video-tutor` agent | `lesson-*.md` | timestamp spot-check |
| OS / routing / brain design advice | `architect` agent | sourced advice | links to transcripts |
| Nick's view on a plan | `nick-brain` agent | sourced advice | links to transcripts |
| Teach Charlie a topic | `teach` skill | active lesson, flashcards | 7-rule self-check |
| Find or install a new skill | `find-skills` skill | install command | Charlie's OK |
| Check a page looks right (visual validation) | `tools/screenshot.py <page>` then open the PNGs | phone + desktop screenshots, script errors | looking at them |
| Structural audit (incl. every checklist quote, `tools/check_quotes.py`) | `tools/audit.py` (runs on push and as the Stop-hook structure gate `tools/run_gate.sh`; includes the secret scan) | errors/warnings | GitHub Actions |
| Get YouTube videos into any brain (list, triage, fetch, hand over) | `youtube-ingest` skill | transcripts + triage file | coverage ticks, audit |
| Show a plan or list as an easy-to-read page | `tools/build_reader.py` → Reading Room (`system/pages.md`) | one page, a tab per document | screenshot on phone |
| Prove the audit catches mistakes (23 planted faults) | `tools/fault_drill.py` | caught / missed list | weekly audit; add a fault after every real miss |
| What loads into every message, hidden instructions (our /doctor) | `tools/context_check.py` | sizes + warnings | run after big changes and model switches |
| Scored audit (weekly, Four Cs rubric v2) | `audit` skill (Nate's AIS-OS kit) | `audits/audit-<date>-<id>.md` with score, findings ledger, top 3 fixes | next run rechecks each finding |
| Failure-mode check, backtrack after a miss | `audit` skill, `content-check.md` | smallest fixes | Charlie approves on the Decision Desk |
| Set someone up (7-question intake) | `onboard` skill, parked in `references/parked-skills/onboard/` (each person runs the one in Nate's kit) | `aios-intake.md` + Day-1 context files | the "what should I focus on this week?" test |
| Replies he can act on fast (on request) | `i-have-adhd` skill (`/i-have-adhd`, off with "stop adhd mode") | next action first, numbered steps, state each turn | Charlie trying it |
| Make something findable | `link` skill | one route in `AGENTS.md` or a folder index | following the route |
| Ship the next automation | `level-up` skill (`references/3ms-framework.md`) | one artifact + `decisions.md` entry | rerun `audit` |
| What the OS can reach | `connections.md` | domain, mechanism, last checked | `audit` freshness check |
| Interview Charlie to capture what he knows | `grill-me` skill | `brainstorms/YYYY-MM-DD-<topic>.md` | Charlie confirms the summary |
| Start a new, blank AI OS | `templates/standard-ai-os-v1/` | router + filing cabinet | fresh-session routing test |
| Flashcards | app + `cards` database (see `AGENTS.md`) | cards | backup in `learning/flashcards.md` |
| Compare our blank template with Nate's kit | Kit Compare app (see `projects/ai-os-setup-kit/README.md`); built by `tools/build_kit_compare.py` | `templates/standard-ai-os-v1/` | page source in `projects/ai-os-setup-kit/compare/` |
| See and review both brains (graph + review cards) | Brain dashboard app + `flags` database (see `AGENTS.md`); built by `tools/build_brain_map.py` | every .md in the repo + concepts.md, rules.md | marks read back with ArtifactData |
| Compare our OS with a Nate-first version of it | Nate-first map (see `AGENTS.md`); built by `tools/build_merge_map.py` | whole repo + Nate's kit | page source in `system/merge-map/` |
| Draw any set of files as a connected map | `tools/graph_lib.py` (files, links, degrees), plus a `template.html` with `__DATA__` filled in by a small builder | nodes + links JSON | screenshot both screen sizes |
| YouTube media production and Shorts | Creative Claw preflight in `projects/youtube-channel/README.md` | media assets after connection and cost approval | first real trial; not yet connected/tested |
| Choose a model and handle failed cheaper outputs | `system/model-usage.md`, existing `try-tool` | task-specific comparison and bounded escalation | saved input/output/check receipts; no unmeasured savings |
| Test Hands decision state handling | `node tools/test_hands_actions.cjs` | adapter test results | real artifact round-trip still required |
| A deliverable (e.g. a video plan) | `projects/<name>/` | project files | the project's own done-when |

## Already available, nothing to build (check at session start)
Added 2026-10-09 after a miss: this map only listed our own skills, so tools
Charlie already had (connectors, claude.ai skills) were missed or ranked as new.
Live check each session: `ListConnectors` (connectors), the session's skill
list (`/skills`, or `/skill-doctor`). Update this table when they change.

| Kind | What's there (2026-10-09) | Use for |
|---|---|---|
| claude.ai connectors (connected) | GitHub, Gmail, Google Calendar, Google Docs, HyperFrames by HeyGen, Moda (slides and designs), Notion, vidIQ | email, calendar, docs, video projects, designs, notes, YouTube research |
| claude.ai connectors (not finished) | Canva (sign-in incomplete), Higgsfield (not added yet) | thumbnails, images |
| claude.ai skills | docs, deep-research, skill-creator, google-workspace; pdf, pptx, docx, xlsx (Charlie switching these off; weekly audit checks if missed) | documents, research reports, building skills, Office files |
| Claude Code built-in skills | artifact-design, dataviz, code-review, security-review, simplify, loop, run, update-config | pages, charts, reviews, recurring jobs, settings |
| Routines (scheduled) | "Weekly AI OS audit" (Fri 8:59 UK), "Weekly Hands Brain update" (Sat 8:47 UK), "Flashcard check" (daily, parked feature) | things that run without Charlie |
| Tried, kept out of the repo | HyperFrames skills (`research/hands/tried.json`) | channel videos, installed in scratch when needed |

**Override (Charlie, 2026-10-09):** use Notion instead of Google Drive;
start project work from GitHub. The table above records Claude connections
from that session, not verified availability in every host. ChatGPT reports
Drive not installed; Notion tools are exposed, with content access untested.
