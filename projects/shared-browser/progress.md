# Build ledger

- Scope approved by Charlie's create/host instructions; no payment/signup.
- Gateway tests written first: 7 failures, then 7 passes. Phone UI test failed
  before implementation; later passed. WS denial and readiness tests added.
- Selkies download exhausted disk and was removed; small noVNC/Xvfb runtime
  reused existing Chromium. Disk recovered; final image ~1 GB, not 30 GB.
- noVNC 1.6 npm packaging failed bundling (CommonJS with top-level await).
  Used pinned official 1.5 package; fixed CommonJS default import interop.
- Independent reviewer added two failing takeover regressions. Fixed active
  action cancellation by disconnecting only the gateway's CDP attachment and
  draining the queue; immediate stream termination/opening lease prevents old
  socket input. Original Chromium/profile stays running. Both regressions pass.
- Reviewer sandbox/readiness findings addressed: non-root sandboxed Chromium,
  upstream Playwright seccomp profile, full browser/display health endpoint.
- Pairing burst regression failed, then passed with per-source limit and Caddy
  overriding X-Real-IP. Suite reached 13/13. Dependencies audit: 0 vulnerabilities.
- Container smoke exposed root-owned mode-0600 sources; fixed /app ownership.
  Hard-killed test container left stale Chromium locks; stopped using that
  temporary test volume, set stable hostname and orderly browser-first shutdown.
- Actual live test confirmed touch/phone typing/same-tab AI/reconnect/cookie
  retention. Explicit close terminates active streams (new regression); suite14/14, live
  test exits0. Service restart retained approved device and browser test cookie.
- Cloud proxy root needed for Chromium external HTTPS; import an explicitly
  supplied trusted CA into NSS normally. Never disable certificate verification.
- External website HTTPS passed with normal certificate checks, before/after
  restart. Cloud install/start scripts executed and configuration draft saved.
- Public hosting blocked: quick tunnel direct connection refused, proxy 403.
  Asked once for Charlie's existing host; external deployment remains pending.

- Post-restart typing timing: live check failed before remote field focus.
  New regression failed on silently dropped text, then passed with explicit
  unfocused-field feedback and retained phone draft. Full suite now15/15; live
  check waits for real touch focus rather than assuming immediate delivery.
- Reviewer reproduced an open-shadow input rejected as unfocused. New focused
  shadow-input regression failed409; descending the active shadow roots fixes
  that compatibility case while keeping unfocused-field feedback.
