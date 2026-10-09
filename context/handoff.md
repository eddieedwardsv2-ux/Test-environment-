# Session hand-off

Overwritten by `session-handoff`; history stays in `decisions.md` and Git.
**Written:** 2026-10-09, 17:54 EDT, by Codex; updated after Charlie’s app/hosting request.

## Working on
Charlie's latest request is a smoother browser shared by him and the AI, fitted
to iPhone 16 Plus, with fewer repeated logins. App and deployment package built
and tested. External hosting remains blocked: no account/server connected and
this cloud blocks Cloudflare tunnel provisioning.
The original Higgsfield/Katana AI OS map promo remains open behind this connection work.

## Summary points
- Updated this checkout to `2830a32` before checking where Claude stopped.
- Repo checks passed: audit 0 errors/0 warnings; fault drill 26/26; Hands adapter tests 14/14 (mocked); file links 0 broken. This is not a new scored audit.
- Installed official Higgsfield CLI 1.1.26 at `/workspace/higgsfield-tools/node_modules/.bin/higgsfield`; verified its archive against the official npm SHA-256 manifest. Repeatable setup: `/workspace/higgsfield-tools/setup.sh`.
- Saved install/start instructions and network additions in environment configuration. Latest config read has no pending draft, retains both scripts, and reports unrestricted network access; no fresh-task restoration test performed.
- Higgsfield MCP returned HTTP 401; its Clerk OAuth metadata returned HTTP 200. Direct Codex MCP login discovered OAuth and displayed its secure sign-in flow; cancelled without account authorisation or token creation.
- This cloud's Codex connector configuration is platform-managed/read-only. A separate CLI connection would not automatically add tools to this chat.
- Intelligent UI and TinyFish control tools were not exposed here; no access to Charlie's signed-in screen. Re-check actual tools next session rather than assuming account-wide absence.
- Created `projects/shared-browser/`: paired iPhone PWA, live noVNC touch/keyboard, saved Chromium profile, reconnect, human/AI handoff and private Codex API/CLI. Selkies image filled the disk and was removed; noVNC reused a much smaller runtime.
- Verified 16/16 tests and full live test exit0: real touch, phone typing, same-tab AI action, takeover, reconnect and cookie retention. Full service restart retained the approved device and browser test cookie. External Example Domain loaded with normal TLS verification.
- Final typing fix `baa609d`: unfocused inputs report409 and keep the phone draft; open-shadow inputs supported. Fresh live test exited0 after waiting for actual VNC focus; shadow case passed the isolated regression.
- Independent code review found/rechecked takeover fixes; production Chromium sandbox enabled. Signed apt/npm checks preserved; trusted proxy CA imported normally. Caddy/Compose validated. No external HTTPS deployment, actual iPhone, Higgsfield login, paid call or video verified.
- Hosting attempt: direct quick-tunnel connection refused, verified HTTPS proxy request returned403. Asked once for existing hosting provider; no secret values requested.
- Cloud install/start scripts tested and draft save confirmed, preserving Higgsfield setup. Environment settings Review/Save and Publish still required; fresh-task restoration unverified.
- Hand-off rebuild completed: Quartermaster, Reading Room, Brain dashboard and Nate-first map need live republishing. Pre-commit audit: 0 errors/4 warnings; after commit `975420c`: 1 missing-Guardian error/4 publication warnings. Review remains outstanding.

## Key files
- App commit `c0b51c5`, branch `codex/shared-iphone-browser`; main is unchanged.
  Claude Guardian review required; independent code review is not that gate.
- `context/handoff.md`, `context/current-focus.md`, `context/todo.md`, `decisions.md`.
- `projects/shared-browser/README.md`, `verification.md`, `cloud-install.sh`, `cloud-start.sh`, Docker Compose/Caddy files and tests. Private development container `charlie-stack-test`; profile/device data in its Docker volume, never the public repo. Use `docker exec charlie-stack-test node agent.mjs status`; no public phone URL exists.
- `references/higgsfield-api.md` and `system/system-map/system-map.html` (the promo's real map reference).
- `/workspace/higgsfield-tools/setup.sh` is current-instance setup outside the checkout; saved environment scripts are the reproduction route if that file is absent.

## Where the information lives
- Priority: `context/current-focus.md`; older unfinished work: `context/todo.md`.
- Chief's Desk and published dashboards: `system/pages.md`; neither Desk answers nor live pages were read in this Codex session.
- Last scored audit remains `audits/audit-2026-10-09-112239-a7c3.md` (64/100, fixes 2-5 open).
- TinyFish [profiles](https://docs.tinyfish.ai/key-concepts/browser-context-profiles) save login data for later Agent runs; ordinary [Live Preview](https://docs.tinyfish.ai/live-preview) is read-only. Its documented [15-minute default](https://docs.tinyfish.ai/browser-api/index) concerns inactivity/account limits, not proof of every active session resetting.
- Initial LinuxServer/Selkies design replaced with Chromium/noVNC after the image exhausted disk. Same-tab Codex control/touch/keyboard verified in `projects/shared-browser/test/live.mjs`; actual iPhone/network performance remains unverified.
- Browserbase [Live View](https://docs.browserbase.com/platform/browser/observability/session-live-view) is interactive, but mobile keyboards are not officially supported. Its paid keep-alive and persistent contexts are an alternative; neither service was connected.
- Docker daemon is available here (28.4.0); sandboxed browser development container tested, but this task workspace is not durable public hosting. Browser profiles/credentials must stay private and outside this public repo. Websites can expire their own logins.

## Decisions made
- Stay in Codex; do not send Charlie to Claude for the browser/Higgsfield workflow.
- Promo: cinematic glowing map, intended for Instagram and X. Proposed 20 seconds: signal enters, routes to an Elder, Guardian/Chief's Desk, network reveal and "follow the build". Style approved; full storyboard/cost not approved.
- Browser must be shared by Charlie and the AI. Proposed first version: phone-sized home-screen web app, large controls/keyboard, saved browser profile, reconnect, and My turn / AI's turn takeover.
- Charlie explicitly asked to create the app and complete hosting: build and deployment authorised; paid hosting/sign-up requires a concrete proposal. Spec/plan saved in the project. No public endpoint created.

## Open decisions
- Existing hosting provider/server and secure deployment access are needed (asked once asynchronously); do not request passwords/keys in chat. Actual device pairing and public HTTPS verification follow deployment.
- Secure Higgsfield sign-in and a supported persistent connector/browser route; Katana availability and exact credit cost unverified. Never ask for tokens or OAuth callback URLs in chat.
- Claude Guardian review is outstanding for `975420c`, app `c0b51c5` and typing fix `baa609d`; audit currently reports 3 missing-review errors and4 publication warnings before the final notes commit. Code is on `codex/shared-iphone-browser`, not merged into main.
- Branch review: `claude/nate-brain-wip` has 1 unmerged commit including `research/nate-herk/brain/x-themes.md` (unverified); `elder-councils-plan` has 3; `nate-watch-path` has 2. The Elder plan and Watch Path source are already on main. Historical branches also contain old renamed files; no branches merged/deleted.

## Pick up here
1. Read this hand-off/current-focus and `projects/shared-browser/verification.md`. Preserve saved profiles and device records. Do not restart browser trials while someone is entering credentials.
2. Resolve the already asked hosting-provider question, securely connect that host, deploy Docker Compose/Caddy behind real HTTPS, and pair the exact phone code Charlie identifies. Verify actual iPhone performance and longer login retention. This cloud's private loopback port is not a phone link.

3. Resume Higgsfield in Codex once secure access works: verify Katana/catalog access, obtain an exact credit quote, then seek approval for one 5-second trial before the full promo.

## Carried forward / dropped
- Elder pilot: mini-router done; first plugin trial/council/Guardian still open in todo. Do not silently replace the 90-day set-up-kit priority.
- Prior Desk reads, scheduled Quartermaster/audit reports, the six older Needs Charlie items, paused set-up kit, side-project Bitcoin newsletter and parked journey video remain in todo/current-focus; no fresh Desk or scheduler verification.
- Prior branch-only WIP preserved above; dropped-item/session-review list remains in todo. Nothing dropped or declared complete without evidence.
- Rebuilt local pages need live republishing where flagged; no publishing tools here, so publication fingerprints must not be marked current without a real publish.
