# Charlie's shared browser

A home-screen web app for iPhone 16 Plus: one real Chromium browser shared with
Codex, touch streaming, a phone keyboard, saved profile, reconnect and explicit
human/AI handoff. The interface targets 430 × 932 CSS pixels. noVNC provides the
stream and touch controls; Playwright attaches to the same Chromium for AI work.

**Hosting is not live.** The app runs in this development workspace, but no
external host is connected and Cloudflare quick-tunnel provisioning is blocked.
Opening a localhost address on the phone will not work. No payment or new account
has been made. See `spec.md`, `plan.md` and `verification.md` for scope/evidence.

## Deploy on an always-on Linux server

Use a private VPS with Docker Compose, at least 2 GB RAM and 10 GB free disk.
A stable domain must point to the server. Allow ports 80/443; keep SSH restricted.
Do not use a free service that sleeps after 15 minutes for this browser.

Check out the saved app branch on that server:

```sh
git clone --branch codex/shared-iphone-browser https://github.com/eddieedwardsv2-ux/Test-environment-.git charlie-ai-os
cd charlie-ai-os/projects/shared-browser
```

From this folder on that server:

```sh
printf 'BROWSER_DOMAIN=your-browser-domain.example\n' > .env
docker compose up -d --build
```

Caddy obtains/verifies HTTPS certificates automatically. Only Caddy publishes
ports; the browser/CDP/VNC remain inside the container. Docker volumes hold the
profile, approved devices and certificates. `restart: unless-stopped` restarts
services after a server reboot. Never run `docker compose down -v` unless you
intend to destroy saved browser/login data. Back up the volumes privately.

Docker image bases and npm dependencies are pinned. Rebuild with current browser
security updates; do not run unmaintained browser images indefinitely. Cloud
builds behind a proxy can pass BuildKit secrets `proxy` and `ca`; they are not
embedded in the resulting image. Do not disable TLS or apt signature checks.

## Pair the iPhone

1. Open the HTTPS address in Safari and tap **Connect this iPhone**.
2. Send Codex the displayed device code. The code alone is not an access token;
   only the requesting phone has the HttpOnly session cookie.
3. The server operator approves that exact request:

```sh
docker compose exec browser node admin.mjs pending
docker compose exec browser node admin.mjs approve DISPLAYED_CODE
```

Safari → Share → Add to Home Screen. The installed app can have separate cookie
storage, so pair it separately if asked. Device sessions last up to 30 days;
there is no 15-minute application reset. Websites can expire their own logins.
To revoke a lost phone in this version, stop the browser service, clear its
private `/data/gateway/devices.json` to `{"devices":{}}`, then restart it. This
revokes every paired device; each must pair again. Keep `/data/profile` intact. Do not expose admin-token or
profile files, print them, or send them through chat.

## Use the shared browser

**My turn** enables live touch and keyboard. Tap a website field, open Keyboard,
type locally and tap Send; Enter/Delete are separate controls. Reconnect restores
the stream to the same browser. Portrait gives the largest view; the live browser
currently keeps its portrait resolution when the phone rotates.

**AI’s turn** disconnects phone input and permits the private operator API. Codex
needs a route to that server (for example an approved SSH connection); deploying
the app does not automatically install MCP tools in this chat. This first version
does not start background models, paid runs or website actions on its own.

## Develop and check

In this Codex cloud, use `bash cloud-install.sh` to keep dependency caches
outside the repository, then `bash cloud-start.sh` for the private development
stack. Those commands do not publish an iPhone link. For other local machines:

```sh
npm ci --ignore-scripts --no-audit --no-fund
npm run build
npm test
```

`npm run test:live` requires the dedicated workspace display, running Chromium
CDP on loopback 9222 and gateway on 8787. It changes a controlled test tab; never
run it against someone browsing or entering credentials. See `verification.md`.
Browser data belongs outside this public repository. No service-worker caching
of API responses, credentials or screen frames.

Upstream licences: noVNC MPL-2.0 (`node_modules/@novnc/novnc/LICENSE.txt`),
Playwright Apache-2.0, ws MIT, Chromium and its third-party notices, x11vnc GPL-2.0.
Dependencies and their licence files ship in the Docker image.

The Chromium sandbox remains enabled in production. `chrome-seccomp.json` is
the official Playwright v1.56.1 Docker profile, allowing browser namespaces:
https://github.com/microsoft/playwright/blob/v1.56.1/utils/docker/seccomp_profile.json
An optional `BROWSER_TRUSTED_CA` file imports an operator-supplied proxy root
into the browser user's NSS database. It does not disable certificate checks.

Local operator examples (run on the private host):

```sh
docker compose exec browser node agent.mjs status
docker compose exec browser node agent.mjs navigate https://example.com
```

Actions require Charlie to choose AI’s turn. `snapshot` writes a private local
file, and never includes the bearer token or screen contents in terminal output.
