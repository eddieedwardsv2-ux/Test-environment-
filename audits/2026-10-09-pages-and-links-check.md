# Pages and relation links check, 9 Oct 2026 (evening)

Charlie: "update all our artifacts and take notes on what was forgotten ... should we update
them regularly ... scan our systems and check for relation links."

## Pages: what was behind, and why
| Page | State found | Why it was missed | Now |
|---|---|---|---|
| Charlie's Brain | repo copy not rebuilt since 17:29; live matched that old build | builders only run when a session remembers to | rebuilt, republished |
| Nate-first map | same (live from 12:28) | same | rebuilt, republished |
| Reading Room | repo build behind the to-do list | same | rebuilt, republished |
| System map | facts stale: Guardian "part-built", "14 skills · 4 agents", "1 card open", council "2 of 6", "model comparisons not run" | written by hand; nothing checks its facts | facts updated, republished |
| OS Guide | stale: "Decision Desk", ENATE 43 ideas, Hands 117 tools, council "planned", no Guardian, hand-off or 5 newer skills | written by hand | updated (9 parts), republished |
| Architect, Quartermaster, Kit Compare | current | | republished |
| Voice Gym, Journey video, Flashcards | live = repo; only the "updated" time is old | | left as they are (nothing to change) |
| AI OS Map, Viral Edition (design canvas) | **never listed** in `system/pages.md` | made in a session that didn't add it | listed; Desk card `old-pages` |
| Thread Notes No1 | **never listed** | made 7 Oct, before the pages list | listed; Desk card `old-pages` (Charlie: keep both); it is a private conversation, so only its link is in this public repo |
| Lesson slides | **not updated**: still uses old names (Decision Desk, ENATE, Hands Brain) | Slides type, edited on the page, not from a repo source | left as is; on the to-do list |
| Nate Herk Watch Path | **not updated**: names old files (`MISSION.md`); its source was only on a branch | made 8 Oct, source never merged | source now on main; refresh on the to-do list |

**Should pages update on a schedule?** No: age isn't the problem, a page is stale only when
its source changed after publishing. New: `system/published.json` holds each source's
fingerprint at publish time; `tools/pages_status.py --build` runs every builder and lists
pages behind their source; the audit warns on each; `/session-handoff` republishes them.
Limit: the two hand-written pages (System map, OS Guide) can still say old facts with an
unchanged source. They need a fact check when a part of the OS changes (now in `system/pages.md`).

## Relation links
- **File links** (`tools/check_links.py`, new): every path a current note names, checked.
  51 raw hits, all false alarms once history files (audits, decisions, logs, plans), other
  repos and Codex's own folder were excluded. **0 broken** in current files, `../` links included.
- **Architect rules ↔ concepts** (new check): 44 rules, 44 concepts, no link to a missing
  number. Fixed: Rules 2 and 3 now link concept 1 (they are its fixes for poisoning and
  clash) and back; concept 31 now names Rule 44 back. Left: concepts 19 (the four Cs) and
  28 (one set of files for every tool) have **no rule yet** (declared, allowed); writing
  rules for them is Charlie's call (to-do).
- **Tools ↔ skills and tools ↔ concepts** (Quartermaster): already checked by the audit; 0 errors.
- Both new checks run in `tools/audit.py` on every push; the fault drill plants one fault
  for each (26 of 26 caught).

**What this won't catch:** links inside `.html` pages and under `templates/` (not scanned); a broken file link only raises a warning, so a push still passes (rule↔concept errors do fail it); a hand-written page saying an old fact; a link that exists
but points at the wrong file; pages made on claude.ai that nobody adds to `system/pages.md`
(the artifact list is the only way to see those; `/session-handoff` could compare it).
