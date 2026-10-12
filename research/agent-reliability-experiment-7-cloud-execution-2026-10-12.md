# Experiment 7 — Cloud execution route
Date: 2026-10-12

## Selected route
GitHub-hosted execution, keeping user Mac off. The existing five-test packet is `research/agent-reliability-experiment-7-agent-run-packet-2026-10-12.md`.
Status: **RUN NOT STARTED**. This session's connected GitHub toolset can fetch and create repository files, and inspect some workflow runs, but exposes no workflow-dispatch action and no hosted shell with both authenticated agent runtimes.

## Official supported methods, verified as documentation not live capability
- GitHub workflow_dispatch runs from GitHub Actions tab or authenticated CLI/API (https://docs.github.com/en/actions/how-tos/manage-workflow-runs/manually-run-a-workflow). A manual-dispatch workflow must exist on default branch.
- OpenAI Codex GitHub action (https://github.com/openai/codex-action) requires model API credential stored as a GitHub Actions secret such as OPENAI_API_KEY. ChatGPT paid plan does not itself establish such a key.
- Anthropic Claude Code action (https://github.com/anthropics/claude-code-action/blob/main/docs/setup.md) supports ANTHROPIC_API_KEY, CLAUDE_CODE_OAUTH_TOKEN in documented situations, or supported workload identity setups. The token is not to be placed in a public repository.
- Hosted GitHub Actions runtime may have metering/plan constraints. Do not assert zero cost or unlimited minutes.

## Before starting agents
1. Obtain a **restricted runner environment** with checked-out public repository and no unrelated write permission. Do not use personal/customer fixtures; use only packet's synthetic cases.
2. Choose supported authentication for each CLI, store in runner secret manager, never git commit or chat.
3. Prepare a manual-only workflow to call each agent CLI **for real**, not merely launch a Python simulation. Require distinct session identifiers and real fresh-session reset per tool.
4. Upload sanitized stdout/stderr, model/version identity, prompt and fixture SHA, tool receipts, artifact hashes, results, time and token/cost data, as workflow artifacts.
5. Run ten actual tests (5 Claude + 5 Codex) including two real fresh-session resumptions; classify incomplete or unavailable runs as NOT VERIFIED.
6. Prevent network-side sends, production changes and unapproved changes in test prompts; runner should have read-only repo permission by default and write only to disposable local fixtures.

## User-actionable options
- For a cloud development computer that can do interactive sign-in, open GitHub Codespaces on the repository: https://github.com/codespaces/new?repo=eddieedwardsv2-ux/Test-environment- . Availability and CLI login still need confirmation; never suggest that Codespaces alone authenticates either provider.
- For non-interactive Actions automation, configure credentials and manual workflow only after selection of authentication. Run via repository Actions tab after workflow is on main.

## Execution status
NOT VERIFIED: no new Claude Code session launched; no new Codex session launched; no agent restart; no live five-fault runs; no measured usage or costs. Prior Python 5/5 fixture checks must not be reused as model results.
No architecture changes or automated run were made.
