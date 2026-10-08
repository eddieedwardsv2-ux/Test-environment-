---
name: find-skills
description: Finds and installs agent skills. Use for "find a skill for X", "is there a skill that...", or when a task might already have an installable skill.
---

> Adapted from the open `find-skills` skill (skills.sh ecosystem); see `THIRD-PARTY-NOTICES.md`.

## Search
- Browse the leaderboard at https://skills.sh/ first, then run `npx skills find [query] [--owner <owner>]`. Use specific keywords ("react testing", not "testing") and try alternative terms.
- Also check `research/plugin-map.md` for plugin families already mapped.
- Nothing found: say so, do the task directly, and mention `npx skills init` for a custom skill.

## Judge before recommending
Never recommend from search results alone. Check the source (official such as `anthropics` or `vercel-labs` beats unknown authors), installs (prefer 1K+, be wary under 100) and the repo's stars (under 100 is a warning), then read its SKILL.md. Present: name, what it does, installs, source, the install command and the skills.sh link.

## Charlie's rules
- Install only with his OK, asked on the Decision Desk via the `decide` skill, never in chat.
- Install into this project: `npx skills add <owner/repo@skill> -y`. Never use `-g`; user-wide installs are wiped with each cloud session.
- Only Anthropic-reviewed or well-known skills.
