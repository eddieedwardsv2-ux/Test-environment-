# Session hand-off

Overwritten by `session-handoff`; history stays in `decisions.md` and Git.
**Written:** 2026-10-09, 17:00 EDT, by Codex; Charlie requested `/session-handoff`.

## Working on
Charlie's latest request is a smoother browser shared by him and the AI, fitted
to iPhone 16 Plus, with fewer repeated logins. Design proposed; not approved or built.
The original Higgsfield/Katana AI OS map promo remains open behind this connection work.

## Summary points
- Updated this checkout to `2830a32` before checking where Claude stopped.
- Repo checks passed: audit 0 errors/0 warnings; fault drill 26/26; Hands adapter tests 14/14 (mocked); file links 0 broken. This is not a new scored audit.
- Installed official Higgsfield CLI 1.1.26 at `/workspace/higgsfield-tools/node_modules/.bin/higgsfield`; verified its archive against the official npm SHA-256 manifest. Repeatable setup: `/workspace/higgsfield-tools/setup.sh`.
- Saved install/start instructions and network additions in environment configuration. Latest config read has no pending draft, retains both scripts, and reports unrestricted network access; no fresh-task restoration test performed.
- Higgsfield MCP returned HTTP 401; its Clerk OAuth metadata returned HTTP 200. Direct Codex MCP login discovered OAuth and displayed its secure sign-in flow; cancelled without account authorisation or token creation.
- This cloud's Codex connector configuration is platform-managed/read-only. A separate CLI connection would not automatically add tools to this chat.
- Intelligent UI and TinyFish control tools were not exposed here; no access to Charlie's signed-in screen. Re-check actual tools next session rather than assuming account-wide absence.
- Researched TinyFish saved profiles and mobile alternatives. Recommended private home-screen web app reusing LinuxServer Chromium/Selkies; no app code, deployment, paid calls or video generated.
- Hand-off rebuild completed: Quartermaster, Reading Room, Brain dashboard and Nate-first map need live republishing. Pre-commit audit: 0 errors/4 warnings; after commit `975420c`: 1 missing-Guardian error/4 publication warnings. Review remains outstanding.

## Key files
- `context/handoff.md`, `context/current-focus.md`, `context/todo.md`, `decisions.md`.
- `references/higgsfield-api.md` and `system/system-map/system-map.html` (the promo's real map reference).
- `/workspace/higgsfield-tools/setup.sh` is current-instance setup outside the checkout; saved environment scripts are the reproduction route if that file is absent.

## Where the information lives
- Priority: `context/current-focus.md`; older unfinished work: `context/todo.md`.
- Chief's Desk and published dashboards: `system/pages.md`; neither Desk answers nor live pages were read in this Codex session.
- Last scored audit remains `audits/audit-2026-10-09-112239-a7c3.md` (64/100, fixes 2-5 open).
- TinyFish [profiles](https://docs.tinyfish.ai/key-concepts/browser-context-profiles) save login data for later Agent runs; ordinary [Live Preview](https://docs.tinyfish.ai/live-preview) is read-only. Its documented [15-minute default](https://docs.tinyfish.ai/browser-api/index) concerns inactivity/account limits, not proof of every active session resetting.
- [LinuxServer Chromium](https://docs.linuxserver.io/images/docker-chromium/) supports persistent storage and Chromium flags; [Selkies mobile controls](https://docs.linuxserver.io/selkies/user-guide/web-client/) include touch and device keyboard. Same-browser Codex control and device performance still need implementation/testing.
- Browserbase [Live View](https://docs.browserbase.com/platform/browser/observability/session-live-view) is interactive, but mobile keyboards are not officially supported. Its paid keep-alive and persistent contexts are an alternative; neither service was connected.
- Docker daemon is available here (28.4.0); this task workspace is not established as durable public hosting. Browser profiles/credentials must stay private and outside this public repo. Websites can expire their own logins.

## Decisions made
- Stay in Codex; do not send Charlie to Claude for the browser/Higgsfield workflow.
- Promo: cinematic glowing map, intended for Instagram and X. Proposed 20 seconds: signal enters, routes to an Elder, Guardian/Chief's Desk, network reveal and "follow the build". Style approved; full storyboard/cost not approved.
- Browser must be shared by Charlie and the AI. Proposed first version: phone-sized home-screen web app, large controls/keyboard, saved browser profile, reconnect, and My turn / AI's turn takeover.
- Browser design approval is still pending. Then write/review the spec and implementation plan before coding; consult the brainstorming skill. Hosting and spend require a concrete proposal first.

## Open decisions
- Desk `qm-frontend-design`: Charlie's keep / later / drop for the first Elder trial (comes before pilot step 2).
- Desk `shared-browser-design`: approve/change that first browser design.
- Desk `higgsfield-signin`: only Charlie can sign in.
- Secure Higgsfield sign-in and a supported persistent connector/browser route; Katana availability and exact credit cost unverified. Never ask for tokens or OAuth callback URLs in chat.
- Claude Guardian review and live page republishing will remain outstanding after this hand-off commit; current-focus records the commit once saved.
- Branch review: `claude/nate-brain-wip` has 1 unmerged commit including `research/nate-herk/brain/x-themes.md` (unverified); `elder-councils-plan` has 3; `nate-watch-path` has 2. The Elder plan and Watch Path source are already on main. Historical branches also contain old renamed files; no branches merged/deleted.

## Pick up here
1. Read this hand-off and current-focus; re-check exposed browser/UI tools. Resolve the pending browser design approval, then write its spec for review. Do not claim an app already exists.
2. Prototype the approved shared browser locally; test phone sizing, keyboard, takeover and reconnect before quoting/approving private always-on hosting. Measure performance and real login retention.
3. Resume Higgsfield in Codex once secure access works: verify Katana/catalog access, obtain an exact credit quote, then seek approval for one 5-second trial before the full promo.

## Carried forward / dropped
- Elder pilot: mini-router done; trial 1 done by Claude the same evening (frontend-design, Guardian READY, `research/hands/reviews/frontend-design-2026-10-09.md`), verdict on Desk card `qm-frontend-design`; next is pilot step 2. Do not silently replace the 90-day set-up-kit priority.
- Prior Desk reads, scheduled Quartermaster/audit reports, the six older Needs Charlie items, paused set-up kit, side-project Bitcoin newsletter and parked journey video remain in todo/current-focus; no fresh Desk or scheduler verification.
- Prior branch-only WIP preserved above; dropped-item/session-review list remains in todo. Nothing dropped or declared complete without evidence.
- Pages: republished by Claude after the merge (`tools/pages_status.py`: 0 behind); Codex's commits checked by the Guardian (READY).
