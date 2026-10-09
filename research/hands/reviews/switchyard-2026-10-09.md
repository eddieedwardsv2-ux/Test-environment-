# NVIDIA Switchyard: do we need it? (2026-10-09)

Charlie asked to find and research "/Switchyard by NVIDIA". Researched on the web, not
installed. Every claim below has its link; anything unconfirmed is marked.

## What it is
**NVIDIA NeMo Switchyard** is an open-source **model router**, not a skill or slash command
(no source mentions one). It sits between an agent (Claude Code, Codex) and the AI models.
For each request it picks a model, sending cheap models the easy steps and frontier models
the hard ones, tuned for quality, speed or cost. It also translates between the OpenAI and
Anthropic API formats.
- Repo: https://github.com/NVIDIA-NeMo/Switchyard (Apache 2.0; about 3.3k stars; commits as
  recent as 2026-10-09; pre-1.0, with parts labelled Alpha/Beta and the server labelled
  "Demo, Not for production").
- Announced 2026-08-11 with Nemotron 3.5 Lightning:
  https://blogs.nvidia.com/blog/nemotron-lightning-switchyard-rtx-dgx/ ; technical post:
  https://developer.nvidia.com/blog/route-ai-agent-workloads-across-models-with-nvidia-nemo-switchyard
- PyPI `nemo-switchyard`, latest 0.3.0 (2026-09-22): https://pypi.org/project/nemo-switchyard/
- Also hosted as `nvidia/switchyard` on OpenRouter: https://openrouter.ai/nvidia/switchyard
- Use with Claude Code: run the local server (`cargo install --locked switchyard-server`, port
  4000), then point Claude Code at it with `ANTHROPIC_BASE_URL=http://localhost:4000` and
  `ANTHROPIC_MODEL=switchyard` (INSTALLATION.md in the repo).
- **Not confirmed:** a one-step `switchyard launch claude` command (seen only in search
  snippets; the docs page is missing); a paywalled article saying it routes Claude Code on
  hard-coded strings rather than reading the prompt (unread).

## Our view
| Question | Answer |
|---|---|
| Same job as something we have? | Yes: it's the same family as FreeLLMAPI ([review](freellmapi-2026-10-09.md)), a server that swaps the model under Claude Code. Our rule is `model: inherit` until a cheaper route passes a comparison (`system/model-usage.md`, Rule 43) |
| Does it save Charlie money? | Probably not today: he works on a Claude subscription, and Switchyard routes **pay-per-use API** calls. Routing Claude Code through it moves work off the plan onto API bills |
| Can he run it today? | No: it needs a computer running the server (Mac day) and API keys in `.env` |
| Risk | Pre-1.0, "not for production"; every prompt goes to whichever provider it routes to |
| Who it's for | Teams paying API prices at volume, where cheap models handling easy steps saves real money |

## Verdict: watch, don't install (later)
Not worth a Mac-day slot now. Look again if Charlie moves any routine onto pay-per-use API
keys. Then run it Rule-43 style: the same task both ways on his own work, with cost counted
and a known-right answer, before trusting it.

VERIFIED: links and facts from the repo, PyPI and NVIDIA pages, read on 2026-10-09.
NOT VERIFIED: routing quality on Charlie's tasks (not installed); star and commit figures
are from the repo web page, as GitHub API access isn't enabled in this session.
