# Anthropic's plugin marketplaces and the Small Business plugin (2026-10-09)

Charlie asked for Anthropic's new small-business skills and the 2,000+ community plugin
marketplace to feed the Quartermaster, as a safety-checked layer next to tools heard about
on YouTube. Researched on the web and from the raw catalogs; nothing installed.

## The catalogs (fetched by `research/hands/anthropic_market.py`)
| Catalog | Plugins (9 Oct) | Repo | Add in Claude Code |
|---|---|---|---|
| Official | 315 | `anthropics/claude-plugins-official` | built in |
| Community | 2,284 | `anthropics/claude-plugins-community` | `/plugin marketplace add anthropics/claude-plugins-community` |
| Knowledge work (incl. Small Business) | 123 | `anthropics/knowledge-work-plugins` | `/plugin marketplace add anthropics/knowledge-work-plugins` |

**What "safety checked" means:** the community README says every plugin "has been submitted via
claude.ai, passed automated security scanning, and been approved for distribution", and calls the
repo a "read-only mirror… synced nightly from Anthropic's internal review pipeline"
(https://raw.githubusercontent.com/anthropics/claude-plugins-community/main/README.md). Entries
are pinned to a commit, and Claude Code won't install a different one
(https://code.claude.com/docs/en/plugins/security). Nothing says a person reviews each plugin.

**Ratings and reviews: none.** The catalog files have names, descriptions and sources only. The
website (https://claude.com/marketplace/plugins) shows install counts and an "Anthropic
verified" mark, but there's no file for those, so we don't use them yet.

**How the Quartermaster uses it:** a tool whose repo (or exact name) is in a catalog gets a gold
"✓ Anthropic" badge and +1 (+2 for the official list). On 9 Oct, 28 of 118 tools matched. A
"(by name)" badge is weaker: a plugin of that name is listed, but it may not be the same code
(e.g. PostHog's listed plugin is `posthog/ai-plugin`, not the analytics product's repo).

## Claude for Small Business
- Announced 13 May 2026 (https://anthropic.com/news/claude-for-small-business); now one plugin,
  `small-business` v1.35.1 with **44 skills** (https://github.com/anthropics/knowledge-work-plugins/tree/main/small-business), Apache 2.0.
- Install: Claude desktop app (Cowork) → Customize → Plugins → Small Business (paid plan), or in
  Claude Code `claude plugin install small-business@knowledge-work-plugins`.
- Most useful for a UK decorator: **proposal-builder** (costed quote from notes or job photos),
  **invoice-chase**, **review-reputation**, **social-content-engine**. Works in GBP. UK tax isn't
  covered (tax-prep only builds an accountant packet). Every skill pauses before anything is sent,
  posted or paid.

## Verdict
- Catalogs: **adopted as a source** (trust layer, weekly with the Saturday run).
- Small Business plugin: **later, need maybe**. The decorating business is parked, so it isn't
  for now. But it's a strong fit for the set-up kit when a friend runs a small business. Try it
  first with `try-tool` (one real quote from job photos) before offering it.

VERIFIED: the catalogs were fetched from this container (HTTP 200, no sign-in, 2,722 entries);
the build marks 28 tools; Small Business matches as `small-business`.
NOT VERIFIED: install counts and "verified" marks (website only); whether a person reviews
community plugins; Small Business on claude.ai web chat.
