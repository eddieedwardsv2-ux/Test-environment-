# The Next New Thing — free agent-tools due diligence (2026-10-15)

Source video: https://www.youtube.com/watch?v=7rVTo_sy4Po
Scope: eight tools named in episode description, correcting earlier seven-item summary. Research and installation suitability for cloud-only Test-environment; no desktop access.

## Evidence and installation status

| Project | Reference | License / caveat | Cloud suitability | Decision |
| --- | --- | --- | --- | --- |
| FluidVoice | https://github.com/altic-dev/FluidVoice | GPLv3; enhanced model privately maintained | Primarily desktop app, not a useful unattended repo install | PARK |
| Fluid Meet | Episode mentions it; exact upstream repo not independently confirmed | UNVERIFIED | Meeting capture generally needs recording input / runtime | HOLD |
| Paperclip | https://github.com/paperclipai/paperclip | Verify LICENSE before redistributing; Node >=24.11, agents need external providers and budgets | Linux server possible; not a GitHub-only service | ISOLATED LATER |
| Basic Memory | https://github.com/basicmachines-co/basic-memory | Verify actual repo LICENSE; MCP, Markdown storage, persistent host needed | Python/uv runtime yes; duplicates knowledge layers | TEST LATER |
| FreeLLMAPI | https://github.com/rodrigoangeloni/free-llm-api | MIT, upstream free tier terms and limits; repo warns experimental only | Node app and provider keys required | NOT PRODUCTION |
| Scrapling | https://github.com/D4Vinci/Scrapling | BSD-3-Clause; requires Python and optional browser deps | Linux CI and remote servers feasible | FIRST TEST |
| VoiceStudio | https://github.com/debpalash/VoiceStudio | AGPL-3.0, downloaded model licenses distinct; considerable compute | Linux / Docker possible, not practical to leave running free in GitHub Actions | PARK |
| Buzz | Episode mentions it; exact upstream repo not independently confirmed | UNVERIFIED | Unknown until repo identified | HOLD |

## Existing system and priority
Read `AGENTS.md`, `context/current-focus.md`, `context/handoff.md`, `context/todo.md` from main. Repo is public; never save keys, customer data or private information. TRADEFLOW quote demo remains current priority; this narrow tools audit is a new direct request, not permission to replace its implementation or add a parallel agent orchestration system.

## Checks performed
- Live GitHub connector successfully fetched Test-environment README/router/priority context (15 Oct).
- Active execution container reports Python 3.13.5, Node 22.16.0.
- Attempted `git ls-remote https://github.com/D4Vinci/Scrapling.git HEAD` in execution container; DNS error `Could not resolve host: github.com`. **No package installed here.**
- GitHub cloud runtime not executed. Storing commands in the repo does not make them active.
- No account secrets collected, no paid plans activated, no repository integrations changed.

## First safe experiment (Scrapling)
Use a disposable Python virtualenv on a network-enabled Linux GitHub Codespace or manually triggered Actions job (never execute automatically on every push). Pin a reviewed release before regular use.
```bash
python -m venv .venv
. .venv/bin/activate
python -m pip install "scrapling[shell]"
python -c "import scrapling; print('import ok')"
```
The full fetcher/crawler requires additional dependencies: `pip install "scrapling[all]"` and `scrapling install`. Do not assume anti-bot success or safety from HTML prompt injection. Start by parsing a known local HTML fixture; only then fetch an explicitly allowed public target. Validate extraction, failure/retry and Markdown quality versus Firecrawl. No unapproved scraping of authenticated sites or circumvention of access restrictions.

## Acceptance criteria for any 'installed' claim
1. Package/container setup completes on an actual persistent or re-runnable cloud environment.
2. Version and dependency records are captured; no secrets printed.
3. A real fixture run outputs expected structured fields and handles an error.
4. Agent invocations/permissions are tested separately; repo commit is not evidence of an active MCP server.
5. Evidence is stored; only then status becomes VERIFIED.

Current overall status: **RESEARCH COMPLETE IN PART; RUNTIME INSTALLATION NOT VERIFIED**. Exact Fluid Meet and Buzz GitHub URLs, current licenses, and operational costs remain unresolved.
