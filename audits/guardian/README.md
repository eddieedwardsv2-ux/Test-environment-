# audits/guardian/

One report per Guardian check (`guardian` agent), named `YYYY-MM-DD-<what-was-checked>.md`,
first line **READY** or **NOT READY**. A big commit cites its report in a
`Checked-by: guardian (...)` line; `tools/audit.py` checks that (paused until the end of 10 Oct).
