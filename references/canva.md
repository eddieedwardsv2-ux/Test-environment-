# Canva (claude.ai connector): read guide

- **Reaches:** Charlie's Canva designs (search, read, copy, export, comment), brand kits,
  templates; can create and edit designs and generate images.
- **Can't / won't:** publish anywhere by itself. Edits, exports and new designs are drafts
  Charlie approves; nothing is posted or shared without him.
- **Read it:** `mcp__Canva__search-designs` (`ownership: owned`, `sort_by: modified_descending`,
  `limit: 3`) lists recent designs; `read-design` opens one.
- **First real read:** 2026-10-09, 3 designs returned (`connect` skill test). Titles and
  contents stay out of this public repo.
- **How it breaks:** the sign-in expires or is revoked → `ListConnectors` shows
  `connected: false` / `connect_incomplete`, and tools return auth errors (that's a
  sign-in problem, not "no designs"). Fix: Desk card with
  https://claude.ai/settings/connectors → Canva → Connect.
- **Serves:** thumbnails and channel graphics (`projects/youtube-channel/`), the
  Marketing plugin if installed.
