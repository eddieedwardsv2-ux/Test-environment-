# Verification — 9 October 2026

**VERIFIED in this workspace:** implementation, not a Claude Guardian verdict.

- `npm test`: 16/16 passed, 0 failed/skipped. Covers device approval, session
  persistence/simulated 16 minutes, CSRF, WS denial, logout, takeover cancellation,
  stale stream revocation, source rate limit, full-stack readiness failure,
  live-stream shutdown, unfocused typing feedback, focused shadow inputs, and iPhone portrait/landscape controls.
- `docker exec charlie-stack-test npm run test:live`: exited 0 after testing real
  touch, phone keyboard, same-tab Codex action/screenshot, human takeover,
  reconnect, retained test cookie, screenshots and complete fixture cleanup.
- A fresh post-restart live run exposed typing before asynchronous VNC focus.
  The isolated regression failed (200 after dropping text), then passed: the
  gateway now returns409 until a text field is focused and the phone keeps the
  draft for retry. The live check waits for actual remote field focus.
- Actual full service stop/start retained an approved device session and a
  persistent Chromium test cookie. External `https://example.com` loaded as
  "Example Domain" with normal certificate verification, including after restart.
- Non-root production container started with Chromium's sandbox enabled and
  the official Playwright seccomp profile. `/api/health` reported ready only
  after both Chromium/CDP and VNC were reachable.
- Full Docker build passed. `cloud-install.sh` executed successfully, including
  frozen npm install, frontend build and Docker build. `cloud-start.sh` was run
  through actual stop/start and checked complete stack readiness.
- Docker Compose configuration and pinned Caddy configuration validated.
  This does not demonstrate an issued public certificate or external phone URL.
- Independent code review found two takeover races; failing regression tests
  reproduced them. Disconnecting the gateway CDP attachment/draining actions
  and terminating revoked VNC streams fixed both. Reviewer rechecked them.
- npm audit (including development dependencies): 0 vulnerabilities after
  updating the vulnerable initial ws pin to 8.22.0.
- Dependency cache sits outside the checkout through an ignored symlink, so
  repository auditing does not traverse third-party README links.
- Cloud proxy trust: explicitly mounted platform CA imported into Chromium's
  NSS store; temporary BuildKit CA secret used for npm. TLS checks stayed enabled.
- Saved cloud installation/startup draft confirmed by the configuration tool.
  Review/Save and Publish in environment settings still needed; no fresh-task
  restoration verified. Original Higgsfield setup preserved.
- HTTPS hosting: official cloudflared 2026.10.0 downloaded and checked against
  GitHub's release SHA-256 digest. Direct and escalated quick-tunnel requests
  failed with connection refused; a verified HTTPS request through the platform
  proxy returned 403 "Your request was blocked." No tunnel or public URL exists.
- Auto-review initially refused public exposure before gateway tests; after
  authentication/WS tests passed, retry was allowed, then blocked by networking.

**NOT VERIFIED:** actual iPhone hardware, mobile network latency, third-party
account authentication, permanent host uptime, real externally reachable HTTPS,
Claude Guardian, or fresh-task environment restoration. TinyFish sessions cannot
be migrated without a supported profile export.

Repository audit before app commit: 1 existing missing-Guardian error and 4
publication warnings. New app commit also requires Claude Guardian review under
AGENTS.md; independent code review does not replace it. Local pages rebuilt,
not republished. No account sign-in, paid call or promotional video generated.
