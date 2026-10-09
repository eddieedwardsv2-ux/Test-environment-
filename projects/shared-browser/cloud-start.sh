#!/usr/bin/env bash
# Private development instance only; this does not publish a phone URL.
set -euo pipefail
browser_source=/workspace/Test-environment-/projects/shared-browser
browser_container=charlie-stack-test
browser_state=$(docker inspect --format '{{.State.Status}}' "$browser_container" 2>/dev/null || true)
if [ "$browser_state" = exited ]; then
  docker start "$browser_container"
elif [ -z "$browser_state" ]; then
  browser_ca_args=()
  if [ -r "${CODEX_PROXY_CERT:-}" ]; then browser_ca_args=(-e BROWSER_TRUSTED_CA=/run/browser-proxy-ca.crt -v "$CODEX_PROXY_CERT:/run/browser-proxy-ca.crt:ro"); fi
  docker run -d --name "$browser_container" --hostname charlie-browser --restart unless-stopped --stop-timeout 30 --shm-size=1g --security-opt "seccomp=$browser_source/chrome-seccomp.json" -p 127.0.0.1:8790:8787 -e ALLOW_HTTP=1 "${browser_ca_args[@]}" -v charlie-stack-verified-data:/data charlie-shared-browser:local
elif [ "$browser_state" != running ]; then
  echo 'Existing private browser container needs inspection; no profile was removed.' >&2
  exit 1
fi
docker update --restart unless-stopped "$browser_container" >/dev/null
docker exec -i "$browser_container" node --input-type=module - <<'JS'
import {setTimeout as delay} from 'node:timers/promises';
for(let i=0;i<120;i++){try{if((await fetch('http://127.0.0.1:8787/api/health')).ok){console.log('Private browser/display ready');process.exit(0);}}catch{}await delay(250);}console.error('Browser stack not ready');process.exit(1);
JS
