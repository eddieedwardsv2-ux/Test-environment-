**NOT READY**

Guardian report, round 3 (final), on the change "make the Guardian enforced" (2026-10-09). Saved word for word, except its file list at the end is left out and its case lists are shortened. Earlier rounds: `-round1.md`, `-round2.md`.

All of round 2's findings are fixed. Every earlier break-in now behaves correctly, and ordinary merges no longer raise false errors. One new problem blocks it: on GitHub's shallow checkout, a correctly checked commit fails the audit. Every file says GitHub skips this check, so that claim is false, and CI will go red on the very commit that ships this work. This was the last fix round, so it goes to Charlie as NOT READY.

**Findings**
- **blocking (items 1 and 4; the draft's "GitHub's shallow clone skips it"):** a shallow clone does not skip the check; it cries wolf on a properly checked commit. `.github/workflows/audit.yml` uses `actions/checkout@v4`, which fetches one commit. A full clone of a scratch repo with a checked 5-file commit gives `audit: 0 errors`; `git clone --depth 1` of the same gives `ERROR commit a2c2974 cites audits/guardian/r.md but didn't add it`. Cause: `0696628` isn't in the shallow clone, so the audit falls back to the date filter, and the parentless commit lists nothing for `--diff-filter=A`. Fix idea: skip section 9 when `git rev-parse --is-shallow-repository` prints `true`.
- **note (item 4):** the Codex route is in `AGENTS.md`, `working-rules.md`, `guardian.md` and `audits/README.md`, but not in `context/todo.md` or `decisions.md`.
- **note:** `decisions.md` opens with "a commit after 9 Oct 17:00 UTC"; the code counts commits after `0696628` by ancestry, and uses that time only as a fallback.
- **note (fresh break, crying wolf):** a commit message that quotes the rule as an example (`Checked-by: guardian (READY) audits/guardian/<date>-<slug>.md`) is read as a citation and errors. The regex matches any line, not only the trailers at the end.
- **note (fresh break, crying wolf):** file names with spaces are over-counted (output split on spaces). No tracked file has a space in its name today.
- **note (a stated limit, confirmed):** a one-line `**READY**` report the worker writes itself, in a later small commit, clears an earlier big unchecked commit. This is the documented "not that the Guardian wrote it" limit.

**VERIFIED**
- `python3 tools/audit.py`: `audit: 0 errors, 0 warnings`. `python3 tools/fault_drill.py`: `24 of 24 caught`, including the planted big unchecked commit.
- 21 cases in a clone on top of `0696628` (ancestry path), all as expected: small, unchecked, own check, later check clears, wrong verdict, missing report; X2 merge adding 5 files (counted as 5), X3a, X3b, X4, N1 and N2 backdated, N3 edited old report, N4 report deleted later (0 errors), N4b verdict edited later (0 errors), W1 ordinary merge (0), W2 merge of a checked branch (0).
- `tools/run_gate.sh` exits 0 when `stop_hook_active` is true, so "sends a turn back once" matches. Git 2.43.0 has `--since-as-filter`.

**NOT VERIFIED**
- Pushed: nothing committed or pushed yet. GitHub Actions itself: not run there. The Stop hook firing live. Other git versions. The worker's "12 cases" (ran my own 21 instead). Whether Codex would follow the route.

**Pleasing check**
- "GitHub's shallow clone skips it" is said more confidently than the evidence allows; false for checked commits.
- "All are fixed and re-tested" is wider than what was checked: no shallow-clone control this round.
- The draft doesn't say this is NOT READY after the last fix round. It must reach Charlie as NOT READY, not "done".

---
**Added by the worker after this report (not checked by the Guardian):** the blocking fix it suggested (skip section 9 when the clone is shallow) and the `decisions.md` opening corrected to "after 0696628 (by ancestry)". Tested by the worker only: full clone, checked HEAD 0 errors; shallow clone, checked HEAD 0 errors; full clone, unchecked big HEAD 1 error; shallow clone, unchecked big HEAD 0 errors (skipped by design). The quoted-rule and spaces notes are in `context/todo.md`.
