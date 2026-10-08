# audits/

One report per `audit` run (weekly, Fridays), named `audit-YYYY-MM-DD-HHMMSS-<id>.md`; the `YYYY-MM-DD.md` reports are older `os-audit` runs. Each
new audit reads the last report first to see what's fixed, still open or back.

`evidence/<run-id>/` holds each run's receipts: the commands it ran with their real output (`commands.md`) and screenshots of any page it checked. Every score in a report points to one.
