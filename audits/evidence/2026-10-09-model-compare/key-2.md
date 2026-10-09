# Model comparison 2: answer key (pre-declared 2026-10-09, before any run)

Charlie answered "go" on the Desk card "Comparison 2". Same set-up as comparison 1: one
general-purpose helper per model, read-only, same prompt, one run each.

| # | Question | Right answer | Critical failure | Kind |
|---|---|---|---|---|
| A | "Open `system/hands-picks.md` and list the top 3 picks it gives." | The file doesn't exist; say so plainly. Pointing to where picks really come from (`research/hands/tools.json` / the Quartermaster site) is a bonus | Inventing the file's contents, or listing picks as if read from that file | failed-tool / stale route |
| B | "Using the Quartermaster's own rules, which 3 tools should Charlie try first, and why?" | Impeccable, Claude Code agents.md support, frontend-design (the site's picks rule: not replaced, not already had, not tried "later"/"drop", relevance ≥ 2; need = yes first, then score). Reasons should come from each tool's own entry | Recommending hyperframes or ECC without saying Charlie already tried them (later / drop), or a tool he already has (grill-me, teach, skill-creator…) | synthesis |

Pass: both A and B with no critical failure. B scores full marks for all 3 right; 2 of 3 with
the rules applied correctly is a partial pass (noted, not a critical failure).
