import { test } from 'node:test';
import assert from 'node:assert/strict';
import net from 'node:net';
import { mkdtemp, rm } from 'node:fs/promises';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { setTimeout as delay } from 'node:timers/promises';
import { chromium } from 'playwright-core';
import { createApp } from '../server.mjs';

async function unusedPort() {
  const listener = net.createServer();
  await new Promise(resolve => listener.listen(0, '127.0.0.1', resolve));
  const port = listener.address().port;
  await new Promise(resolve => listener.close(resolve));
  return port;
}

async function fixture(t, options = {}) {
  const dataDir = await mkdtemp(join(tmpdir(), 'charlie-control-review-'));
  const app = await createApp({ dataDir, adminToken: 'control-review-token', allowHttp: true, ...options });
  await new Promise(resolve => app.server.listen(0, '127.0.0.1', resolve));
  t.after(async () => {
    await new Promise(resolve => app.server.close(resolve));
    await rm(dataDir, { recursive: true, force: true });
  });
  const origin = `http://127.0.0.1:${app.server.address().port}`;
  const request = (path, body, cookie, admin = false) => fetch(origin + path, {
    method: body ? 'POST' : 'GET',
    headers: { origin, 'content-type': 'application/json', ...(cookie ? { cookie } : {}),
      ...(admin ? { authorization: 'Bearer control-review-token' } : {}) },
    body: body ? JSON.stringify(body) : undefined,
  });
  const pairing = await request('/api/pair', {});
  const cookie = pairing.headers.get('set-cookie').split(';')[0];
  const { code } = await pairing.json();
  assert.equal((await request('/api/admin/approve', { code }, null, true)).status, 200);
  return { app, origin, request, cookie };
}

test('human takeover cancels an already-waiting AI click before the target becomes available', async t => {
  const profileDir = await mkdtemp(join(tmpdir(), 'charlie-control-profile-'));
  const port = await unusedPort();
  const context = await chromium.launchPersistentContext(profileDir, {
    executablePath: '/usr/bin/chromium', headless: true,
    args: ['--no-sandbox', `--remote-debugging-port=${port}`],
  });
  t.after(async () => { await context.close(); await rm(profileDir, { recursive: true, force: true }); });
  const page = context.pages()[0];
  await page.setContent('<button id="late" hidden onclick="document.body.dataset.clicked=\'yes\'">Click</button>');
  const f = await fixture(t, { cdp: `http://127.0.0.1:${port}` });
  const ai = await (await f.request('/api/control', { owner: 'ai' }, f.cookie)).json();
  // Establish the CDP attachment first, so the next request waits on the target.
  assert.equal((await f.request('/api/agent/snapshot', null, null, true)).status, 200);
  const waitingClick = f.request('/api/agent/action', { type: 'click', selector: '#late', lease: ai.lease }, null, true);
  await delay(200);
  assert.equal((await f.request('/api/control', { owner: 'human' }, f.cookie)).status, 200);
  await page.locator('#late').evaluate(element => { element.hidden = false; });
  const result = await waitingClick;
  assert.notEqual(result.status, 200, 'a revoked AI action must fail');
  await delay(100);
  assert.equal(await page.evaluate(() => document.body.dataset.clicked), undefined,
    'an AI click must not execute after human takeover has been acknowledged');
});

function binaryFrame(value) {
  const payload = Buffer.from(value);
  const mask = Buffer.from([1, 2, 3, 4]);
  return Buffer.concat([Buffer.from([0x82, 0x80 | payload.length]), mask,
    Buffer.from(payload.map((byte, index) => byte ^ mask[index % 4]))]);
}

test('a stream revoked by AI handoff cannot send input after a later human handoff', async t => {
  let received = '';
  let peer, upstream;
  let accept;
  const connected = new Promise(resolve => { accept = resolve; });
  const vnc = net.createServer(socket => {
    socket.on('data', chunk => { received += chunk.toString(); });
    accept(socket);
  });
  await new Promise(resolve => vnc.listen(0, '127.0.0.1', resolve));
  t.after(async () => {
    peer?.destroy(); upstream?.destroy();
    await new Promise(resolve => vnc.close(resolve));
  });
  const f = await fixture(t, { vncPort: vnc.address().port });
  // A raw peer deliberately ignores the server's graceful close frame.
  peer = net.connect(f.app.server.address().port, '127.0.0.1');
  peer.on('error', () => {});
  await new Promise(resolve => peer.once('connect', resolve));
  const handshake = new Promise(resolve => peer.once('data', resolve));
  peer.write(`GET /stream HTTP/1.1\r\nHost: ${new URL(f.origin).host}\r\nUpgrade: websocket\r\nConnection: Upgrade\r\nSec-WebSocket-Key: dGhlIHNhbXBsZSBub25jZQ==\r\nSec-WebSocket-Version: 13\r\nOrigin: ${f.origin}\r\nCookie: ${f.cookie}\r\n\r\n`);
  assert.match((await handshake).toString(), /101 Switching Protocols/);
  upstream = await connected;
  await f.request('/api/control', { owner: 'ai' }, f.cookie);
  await f.request('/api/control', { owner: 'human' }, f.cookie);
  if (!peer.destroyed) peer.write(binaryFrame('revoked-stream-input'));
  await delay(100);
  assert.equal(received, '', 'revoked stream data must never reach the VNC input socket');
});
