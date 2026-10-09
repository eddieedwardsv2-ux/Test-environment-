**NOT READY**

Guardian report, round 2, on the uncommitted change "make the Guardian enforced" (2026-10-09). Saved word for word, except its file list at the end is left out. The fixes are in the same commit; the final round is `2026-10-09-guardian-enforced.md`.

All three round-1 break-ins are now caught, and the limits now appear in every file. But the merge fix cries wolf on ordinary merges, and this repo merges `origin/main` often. Some written claims are also still wider than the code.

**Findings**
- **blocking (item 3, no crying wolf):** a normal merge is counted as a big unchecked commit.
  - Git 2.43's `git diff-tree -m --first-parent` ignores `--first-parent` and lists the files against both parents. The X2 merge adds 5 files; the audit counted 10, with mg1–mg4 listed twice.
  - W1: local commit with 2 files, remote with 2 files, a clean merge, nothing big anywhere: `ERROR commit d19dd15 changes 4 files with no Guardian check`.
  - W2: merging a branch whose big commit was properly checked (`Checked-by: guardian (READY) audits/guardian/w2.md`) still gives `ERROR commit 3cfb270 changes 5 files`.
  - This repo's log has many `Merge remote-tracking branch 'origin/main'` commits, so the next routine pull-merge will trip the Stop hook.
  - Fix idea: `git diff --name-only <sha>^1 <sha>` for merges.
- **blocking (item 1 and the draft's "one that is new"):** the code accepts a report that is "added **or changed**" (`m.group(2) not in _changed(sha)`), not a new one.
  - N3: a big unchecked commit, then a commit that appends one blank line to the old round-1 report and cites it: `audit: 0 errors`.
  - `working-rules.md` ("must be new"), `guardian.md` ("is new in that commit"), `todo.md` and `decisions.md` all say "new", so they claim more than the code does.
  - Fix idea: `--diff-filter=A` for the report.
- **blocking (item 4, no claim wider than the code):** `decisions.md` says "merges count against their first parent; every commit since the start point is read". The first part is false (above). The second is false too: see N2 below.
- **note (fresh break, N2):** `git log --since` stops walking at the first commit with an old committer date.
  - A big unchecked commit with one small commit on top, backdated with `GIT_COMMITTER_DATE=2020-01-01`: `audit: 0 errors`. The big commit is hidden.
  - N1, the big commit itself backdated, also escapes.
  - Doing this on purpose needs intent, but a Mac with a wrong clock could do it by accident. Either state it as a limit or use `--since-as-filter` (git 2.37+).
- **note:** the first line is read from the working-tree copy of the report, not from the copy in the citing commit.
  - N4: deleting the report later turns a genuine check back into 2 errors. That is safe (it errors), but editing the report later can also flip the result.
- **note (Codex route):** the route ("commit it, leave the audit's Guardian error, note it under Waiting on Charlie, the next Claude session clears it") is only in `AGENTS.md`. `guardian.md`, `working-rules.md` and `audits/README.md` don't mention Codex. That is acceptable because the router is what Codex reads, but item 4 asks all six files to give the route.
- **note:** `AGENTS.md` changed, but `exports/chatgpt-instructions.md` was not updated, although the router's own table says to update it when this file changes.
- **note:** `decisions.md` cites `audits/guardian/2026-10-09-guardian-enforced.md` as the receipt, but that file doesn't exist yet (only round 1 is on disk). Fine if this report is saved there before commit.

**VERIFIED**
- `python3 tools/audit.py` on the working tree: `audit: 0 errors, 0 warnings`, exit 0.
- `python3 tools/fault_drill.py`: `fault drill: 24 of 24 caught`, including `a big commit nobody checked (Guardian) -> ERROR commit 8347e2d changes 5 files with no Guardian check`.
- Scratch clone with the diff applied and committed, citing the round-1 report as NOT READY: 0 errors. Results by case:
  - X2 merge adding files: caught (but over-counted).
  - X3a, report outside `audits/guardian/`: caught (`isn't a file in audits/guardian/`).
  - X3b, reused unchanged report: caught (`doesn't add or change it`).
  - X4, buried verdict: caught (`doesn't open with that verdict`).
  - Controls all behaved as expected: big commit with its own check, 0 errors; big unchecked, 1 error; later genuine check, cleared; 3-file commit, 0 errors.
- `tools/run_gate.sh`: exits 0 when `stop_hook_active` is true, so "sends a turn back once" matches the code.
- The limits sentence is now in `working-rules.md`, `guardian.md`, `audits/README.md`, `todo.md` and `decisions.md`; `AGENTS.md` says "its Guardian check runs locally only".

**Try to break it (new this round)**
- W1 and W2 (ordinary merges): false errors. Blocking.
- N3 (touch an old report): escaped.
- N1 and N2 (backdated committer date): escaped.
- N4 (report deleted later): held, with errors.

**NOT VERIFIED**
- Pushed: nothing is committed or pushed yet.
- The Stop hook firing in a live session: I read the script but did not trigger it.
- GitHub Actions' real checkout: not run there; the shallow-clone limit was proven locally in round 1 and not re-run this round.
- Merge behaviour on other git versions: only 2.43.0 was tested.
- Whether a Codex session would actually follow the AGENTS.md route.

**Pleasing check**
- The draft's "all three are now caught" is true, but the draft leaves out that the merge fix introduced false errors on routine merges. "Done" is wider than what was checked: no ordinary-merge control was run.
- "One that is new" is wider than the code (added or changed).
- Not user-facing, so the generic check doesn't apply.
