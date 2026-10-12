#!/usr/bin/env bash
# Recreate the five already-approved project plugins on a new Claude Code host.
set -euo pipefail
cd "$(dirname "$0")/.."
if ! command -v claude >/dev/null 2>&1; then
  printf '%s\n' 'Claude Code CLI is required on this host; no plugin installation attempted.' >&2
  exit 2
fi
claude plugin marketplace add anthropics/claude-plugins-official
claude plugin marketplace add anthropics/claude-plugins-community
claude plugin marketplace add anthropics/knowledge-work-plugins
for approved_plugin in marketing@knowledge-work-plugins context7@claude-plugins-official superpowers@claude-community watch-video@claude-community claude-patterns@claude-community; do
  claude plugin install "$approved_plugin" --scope project
done
claude plugin list --json
