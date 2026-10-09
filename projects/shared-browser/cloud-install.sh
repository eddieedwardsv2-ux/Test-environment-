#!/usr/bin/env bash
set -euo pipefail
browser_source=/workspace/Test-environment-/projects/shared-browser
browser_deps=/workspace/browser-tools/shared-browser-deps
mkdir -p "$browser_deps"
cp "$browser_source/package.json" "$browser_source/package-lock.json" "$browser_deps/"
npm --cache /tmp/shared-browser-npm --prefix "$browser_deps" ci --ignore-scripts --no-audit --no-fund
if [ ! -e "$browser_source/node_modules" ]; then
  ln -s "$browser_deps/node_modules" "$browser_source/node_modules"
fi
cd "$browser_source"
npm run build
browser_build_args=()
if [ -n "${HTTPS_PROXY:-}" ]; then browser_build_args+=(--secret id=proxy,env=HTTPS_PROXY); fi
if [ -r "${CODEX_PROXY_CERT:-}" ]; then browser_build_args+=(--secret "id=ca,src=$CODEX_PROXY_CERT"); fi
docker --config /workspace/browser-tools/docker-config build "${browser_build_args[@]}" -t charlie-shared-browser:local .
