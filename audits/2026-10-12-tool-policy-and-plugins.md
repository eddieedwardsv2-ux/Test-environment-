# Tool-policy removal and five approved plugins — 12 October 2026

Charlie's request: delete the trial/keep skill, smallest/simpler-wins policies
and Guardian, then clear the five-plugin activation backlog identified in the
preceding answer. No new direction, signup, payment or social publishing is implied.

## Policy changes

- Deleted the trial skill and separate-reviewer agent. Removed the audit's
  mandatory review trailer/report check, its pause timer and its two fault cases.
- Removed smallest-version-first and simpler-wins policies from active operating,
  teaching and exported instructions. Source-derived research is explicitly
  subordinate to the current policy; original transcripts and old reports remain.
- Updated active tool routes, architecture, guide sources and Codex instructions.
  Codex can finish verified work without waiting for Claude's reviewer.
- Existing authorisation carries forward. Real output checks, secret protection,
  factual evidence, account controls and structural audit remain.
- Selective reading remains. It limits irrelevant context loading, not tool adoption.

## Plugin use in this run

| Plugin | Real use | What this proves / limit |
|---|---|---|
| Context7 | Connected in ChatGPT; resolved Claude Code, then queried `/websites/code_claude` for project plugin installation and settings. Applied the returned official documentation to configuration and CLI installation. | Live documentation retrieval worked. It correctly distinguished enabled project settings from installation of external-source plugins. |
| Superpowers | Installed/enabled in ChatGPT; read and used brainstorming to scope this policy change and verification-before-completion to identify and execute actual checks. | Skill retrieval and application worked here. Charlie's explicit task authorisation takes precedence; withdrawn gates were not reinstated. No paid Claude model session was started. |
| Marketing | Read Anthropic's `marketing/skills/brand-review/SKILL.md`; applied it to Topic 1 practical-teacher article using Draft 1's saved guidelines. Review below. | A useful manual application of the plugin skill to real saved work; not a claim that Claude invoked `/brand-review`. |
| watch-video | Downloaded the existing journey r5 MP4, matched its recorded SHA-256, ran the actual upstream pipeline with eight frames and no transcription. Inspected frames at 0, 21.583 and 50.36 seconds. | Real CLI media extraction and reports worked. 1080×1920, 57.735352 s, H.264/AAC; eight frames; elapsed 2.43 s. Audio transcription, YouTube access, Jira and the Short's full quality gates were not tested. |
| claude-patterns | Read upstream `skills/patterns/SKILL.md`; scanned the current handoff, first 15 decision entries and saved draft. Captured the three grounded findings below. | Manual skill application on the real repo; not a claim of automatic background execution or a Claude `/patterns` session. |

Source repositories inspected: `anthropics/knowledge-work-plugins`,
`MarcinSufa/claude-watch-video`, `adelaidasofia/claude-patterns`.
Exact checked commits are recorded in the evidence directory. Project-level installation succeeded for all five. `installed-plugins.json`
records each ID, version, scope, enabled state and project-enabled state.
CLI version: 2.1.296. Marketplaces were registered first; installation used
`claude plugin install <name>@<marketplace> --scope project`. The installed
watch-video pipeline was also run separately; its receipt is
`watch-video-installed-result.json`. Recreate on a new host with
`tools/install_approved_plugins.sh`; this host’s cache is not portable.

## Marketing brand review — actual saved draft

Input: `brainstorms/2026-10-12-style-guide-test-drafts.md`, Topic 1,
Practical teacher, Article. Guidelines: Draft 1 and shared rules in
`brainstorms/2026-10-12-brand-style-guides.md`.

Outcome: the opening presents the problem and next action; the worked example
preserves the fictional status, dates, current/obsolete distinction and review
requirement. It does not claim a token saving or a successful audience test.
The route and next action are clear. No critical unsupported factual claim found
in this bounded author review; this is not beginner-comprehension validation.

Two improvements identified: spell out AI on first use for a new reader; the
last sentence repeats the earlier bounded-question advice. Those are editorial
suggestions, not changes to the controlled comparison drafts. The guideline's
"smallest useful example" wording is updated to "worked example" so it no
longer imports the withdrawn operating policy.

## Patterns capture — evidence and action

1. **Stale status sends work backwards.** Decision `2026-10-10: backtrack: a
   stale hand-off sent me to done work` records that later commits had already
   finished the audit fix and helper tests. Action: current handoff supersedes
   old entries; retain the existing git-log-before-resuming route.
2. **Already-approved tools wait on outdated availability.** The old todo
   recorded an empty Claude plugin list, while this host exposes Superpowers
   and now Context7. Action: record host-specific live checks and install all
   five approved plugins at project scope instead of requesting approval again.
3. **Process requirements become unfinished-work records.** Baseline audit
   produced 11 missing-review errors. Action: remove the explicitly withdrawn
   review gate and retire that requirement; leave actual media, deployment,
   slide capture and reader tests accurately unverified.

These observations concern workflow files, not an assessment of Charlie.
No additional permanent restriction is inferred from them.

## Verification

Baseline: audit exit 1, 11 mandatory-review errors and one catalogue warning.
After policy changes: audit exit 0, no mandatory-review errors. Final structural,
fault-drill, installation and remote-saving receipts are recorded below.
A green structural audit does not prove all historical deliverables work.

External Claude artifact pages still require a publishing-capable host. Updated
page sources and rebuilt generated pages can be committed here; no publication
fingerprint is marked without a real publication.

## Final local results

- Installed/enabled plugin inventory: 5/5, project scope, each projectEnabled=true.
- Installed Marketing and patterns skill text hashes match the reviewed sources.
- Installed watch-video pipeline: eight frames and report files from the actual
  journey Short; no transcription or publishing.
- Structural audit: 0 errors, 8 warnings, all remaining warnings are stale
  external Claude artifact pages. Page sources were rebuilt; no publication
  status was forged. Baseline catalogue warning was repaired by rebuilding.
- Fault drill: 25/25 remaining faults caught. Two tests for the deliberately
  deleted reviewer gate were removed; the deleted-skill routing case now uses
  the still-active connect skill.
- Link/brain-relation checks: 0 broken links, 0 errors, 0 warnings.
- Installer shell syntax and git diff whitespace check passed.

VERIFIED: requested active mechanisms removed; five plugins installed/enabled
on this host; the practical uses and local checks above ran.
NOT VERIFIED: a fresh Claude model session/Mac plugin load, optional third-party
account connections, audio transcription, real beginner understanding, full
Short quality gates, external browser hosting and external page publication.
No payment or new account was used. These are separate output/access checks,
not reasons to restore the removed policy gates.

## Resumed-session verification — 12 October 2026

Fresh branch checkout at `972ad1f9cc8ec315cce15787c253489b95956b59`.
PR #4 checked live: open, draft, unmerged, mergeable; GitHub audit check
completed successfully at this head. The three commits after `515f763`
change only handoff, current-focus and todo; implementation is unchanged.
The legacy combined-status endpoint has no statuses and says pending; that
is not a failed check and does not replace the successful audit check run.

Fresh commands completed: context doctor (123 router lines, no warnings),
structural audit (0 errors, 8 publication warnings), fault drill (25/25 caught,
no skips), link/brain-relation checks (0 broken, 0 errors/warnings), installer
shell syntax and whitespace checks. Page builders completed; eight external
Claude pages still need actual republication. Rebuilt files are local previews;
no publication fingerprint changed and no external publication is claimed.

This resumed host has no `claude` executable. Five-plugin installation/load
on the earlier host remains a dated receipt, not a fresh runtime claim here.
No Mac loading, new account connection or merge attempted. Existing approvals
carry forward; removed gates remain removed. Next: merge only following
Charlie's explicit approval and a fresh current-head/check review; on a Claude
host replay the approved installer and verify actual plugin load.
