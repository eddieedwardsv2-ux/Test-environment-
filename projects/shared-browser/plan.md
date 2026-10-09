# Shared browser implementation plan

> Inline execution; existing isolated cloud checkout. Specification: spec.md.

1. Write failing tests for protected stream, device approval, session retention,
   CSRF, AI lease revocation, unsafe navigation and logout.
2. Implement gateway/private Playwright bridge. Run full test suite.
3. Build responsive PWA around noVNC and verify the real shared browser.
4. Verify phone portrait/landscape and keyboard. Inspect screenshots.
5. Start HTTPS tunnel, check external access and authenticated WebSockets.
6. Save tested startup instructions, routes and handoff; audit and commit.
   Record required Claude Guardian review without claiming it passed.

Review: keep display/CDP loopback-only, tie approval to the requesting device,
reject cross-site actions/streams, disconnect manual input on AI handoff,
recheck lease before queued actions; describe hosting lifetime accurately.
