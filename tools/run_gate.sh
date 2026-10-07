#!/usr/bin/env bash
# Stop hook "run gate" (Karpathy rule 5: prove it, don't claim it).
# Blocks an agent from finishing while tools/audit.py reports errors.
# stop_hook_active=true means we already blocked once this turn: let it stop
# rather than loop forever.
input=$(cat)
[ "$(printf '%s' "$input" | jq -r '.stop_hook_active // false')" = "true" ] && exit 0
cd "${CLAUDE_PROJECT_DIR:-.}" || exit 0
out=$(python3 tools/audit.py 2>&1) && exit 0
jq -n --arg r "$(printf '%s' "$out" | tail -8)" \
  '{decision: "block", reason: ("Run gate (rule 5, prove it): tools/audit.py found errors. Fix them, re-run it, then finish.\n" + $r)}'
