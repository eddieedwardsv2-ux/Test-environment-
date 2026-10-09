**NOT READY**

Guardian report, round 1, on the uncommitted change "make the Guardian enforced" (2026-10-09, about 17:15 UTC). Saved word for word, except its two tables are written as lists and its file list at the end is left out; the fixes are in the same commit, and round 2's verdict is in `2026-10-09-guardian-enforced.md`.

The code works. Items 1–3 pass, and I reproduced them in a throwaway clone. Item 4 fails: the limits appear only in decisions.md. The other four files either leave the limits out or claim more than the audit enforces. This is a small text fix, not a code fix.

**Findings**
- **blocking (item 4, "same limits, no wider claims"):** the limits are written only in `decisions.md`: a shallow clone (GitHub) skips the check, and a fake report gets through. The other four files leave them out:
  - `context/working-rules.md:103` says "the audit forces it for big commits". In fact it forces a cited file whose opening matches the verdict, and only on local runs.
  - `context/working-rules.md:91` says "the Stop-hook gate sends the turn back". That only happens after the work is committed, and only once: `tools/run_gate.sh` lets the turn stop on the second try (`stop_hook_active`).
  - `audits/README.md` says the audit "fails a 4+ file commit without one". It leaves out "or a later commit", "hand-written" and every limit.
  - `context/todo.md` 2b gives no limits.
  - `.claude/agents/guardian.md` gives no limits and shows only the `(READY)` form.

  Fix: add the same one-line limits sentence to each of those four files.
- **note (draft claim wider than checked):** the headline "The Guardian is now enforced" is wider than the code. The check proves a file is cited, not that the Guardian ran. My try-to-break run (below) cleared a big unchecked commit using an empty later commit that cited a 1-line file outside `audits/guardian/`. The draft's "a worker could still fake a report" understates how easy this is. Possible fix: require the path to start with `audits/guardian/`, and require each report to be new to the commit that cites it.
- **note (verdict check is loose):** `tools/audit.py` searches the first 400 characters for `**READY**`, not the first line. A report that opens `**NOT READY**` but says `**READY**` later in those 400 characters passes when the commit cites it as READY (case X4 below). Checking the first line only would fix it.
- **note (holes not stated anywhere):**
  - A merge commit that itself adds 4+ files escapes. `git diff-tree` without `-m`/`--cc` lists nothing for merges (case X2).
  - Only the last 40 commits are read, so older unchecked commits drop out.
  - `AGENTS.md` still says `tools/audit.py` "runs on every push". For this check that is now misleading, because the shallow clone on GitHub skips it.
- **note (Codex route):** `AGENTS.md:44` says Codex can't run the Guardian. A Codex session that commits 4+ files will now hit an audit ERROR it has no honest way to clear. No file says what Codex should do: leave the error and log it under "Waiting on Charlie"?
- **note:** the claim "5 control cases" has no receipt in the repo. `decisions.md` lists 6 cases, and some of them are meant to fail rather than "pass". I re-ran them myself (below).

**VERIFIED**
- `python3 tools/audit.py` on the working tree: `audit: 0 errors, 0 warnings`, exit 0.
- `python3 tools/fault_drill.py`: `fault drill: 24 of 24 caught`, including `a big commit nobody checked (Guardian) -> ERROR commit a4867d4 changes 5 files with no Guardian check`.
- Start point: `GUARD_FROM` 1791565228 is Fri 9 Oct 2026 17:00:28 UTC. The last real commits are earlier (0696628 at 16:56:52), so the current repo passes.
- Scratch clone with the diff applied: 2-file commit applying the diff, 0 errors (expected). A: 3 files, 0 errors (expected). B: 4 files, no Guardian line, `ERROR commit b8a1aeb changes 4 files with no Guardian check` (expected). C: case B, then a later commit citing a READY report, 0 errors (expected). D: 4 files, own commit cites NOT READY with a matching report, 0 errors (expected). E: cites READY, report says NOT READY, `ERROR … doesn't open with that verdict` (expected). F: cites a missing report, `ERROR … nope.md, which doesn't exist` (expected). X1: big unchecked commit on a branch, then merged: caught (expected).
- Shallow clone (`--depth 1`) of a repo whose top commit is big and unchecked: 0 errors. The full clone of the same repo gives 1 error, so the "shallow clone skips the check" limit is real.
- `.claude/settings.json` has the Stop hook calling `tools/run_gate.sh`, and that script blocks when the audit exits non-zero.

**Try to break it**
- X2: a merge commit that itself adds 4 files: **escaped**, 0 errors.
- X3: big unchecked commit, then an empty commit citing `audits/old.md` (contents just `**READY**`): **escaped**, 0 errors.
- X4: a report opening `**NOT READY**` that also says `**READY**` lower down, cited as READY: **escaped**, 0 errors.
- X5: a citation pointing outside the repo (`../../../etc/hostname`): held, error.

**NOT VERIFIED**
- Pushed: nothing is committed or pushed yet, and there is no `audits/guardian/` folder yet. This change touches 7 hand-written files, so its own commit needs a `Checked-by:` line.
- That the Stop hook fires in a live Claude session. I read the script but did not trigger it.
- How GitHub Actions behaves in practice. I copied its default shallow checkout locally; I did not run it there.
- Whether Codex sessions will follow any route for this error.

**Pleasing check**
- "The Guardian is now enforced" is wider than what was checked. It is a local check that a cited file exists and matches the verdict, and a 1-line file or a reused file clears it.
- "5 control cases pass" mixes cases that are meant to pass with cases that are meant to fail, and has no receipt.
- Nothing quietly skipped from Charlie's "Go". Not user-facing, so the generic check doesn't apply.
