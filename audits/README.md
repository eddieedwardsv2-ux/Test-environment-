# audits/

One report per `audit` run (weekly, Fridays), named `audit-YYYY-MM-DD-HHMMSS-<id>.md`; the `YYYY-MM-DD.md` reports are older `os-audit` runs. Each
new audit reads the last report first to see what's fixed, still open or back.

`evidence/<run-id>/` holds each run's receipts: the commands it ran with their real output (`commands.md`) and screenshots of any page it checked. Every score in a report points to one.

**Reviews of the audit itself:** `2026-10-09-audit-review.md` (what each layer checks, the two "doctors", gaps found and fixed). Backtests of a build go in `evidence/<date>-backtest/`.

**Scoped continuation check:** `2026-10-09-usage-hands-check.md` — Hands
decision controls, model quality gate, connection boundaries; unscored.

**Guardian reports:** `guardian/<date>-<slug>.md`, one per big task, saved word for
word from the `guardian` agent and cited in the commit (`Checked-by: guardian (READY) …`).
`tools/audit.py` fails a commit changing 4+ hand-written files unless it, or a
later commit, adds a new report here whose first line matches the cited verdict.
Codex can't run the Guardian: it commits, leaves the error and notes the commit under
"Waiting on Charlie"; the next Claude session runs the Guardian and clears it.
Limits: it runs locally and in the Stop hook only (any shallow clone, e.g. GitHub's, skips
it); the hook sends a turn back once, and only after the commit exists; it proves
a fresh report with a matching verdict was filed, not that the Guardian wrote it. Read them to see what was
checked, what wasn't, and anything flagged as pleasing you.
