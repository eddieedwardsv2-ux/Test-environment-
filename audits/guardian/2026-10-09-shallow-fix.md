**READY**

Guardian report on the shallow-clone fix added after `2026-10-09-guardian-enforced.md` (commit 90669a5). Saved word for word, except the list of scratch clones at the end is left out.

Scope: only the shallow-clone fix after the "---" line in audits/guardian/2026-10-09-guardian-enforced.md, and whether the written claims about it match the code. All five "done when" items passed. Nothing is blocking.

**Findings:**
- **note:** Any shallow repo skips section 9, not just GitHub's. A full clone with `.git/shallow` hand-written also skips it: the unchecked big commit went from 1 error to 0. The written limit, "GitHub's shallow clone skips it" (working-rules.md:93, guardian.md:59, audits/README.md:19, todo.md:22, decisions.md:4), is true but narrower than what happens. The code comment at tools/audit.py:263 ("shallow clones … skip this") is accurate. A depth-40 clone also skipped, as designed. Suggest one line in the limits: "any shallow clone, including one made shallow on purpose, skips it".
- **note:** context/todo.md 2b and decisions.md still say the fix "was not Guardian-checked" and "the next Claude session should run the Guardian". Once this report is committed, the maker should update both lines in the same commit.
- **note:** This change did not make either known open item worse (the quoted rule in a commit message; file names with spaces). The fix changes only `_shallow` and the `_log` choice (lines 270–271).

**VERIFIED:**
1. Shallow clone (`git clone --depth 1 file://...`): `--is-shallow-repository` returned `true`. The checked HEAD gave `audit: 0 errors`. An unchecked commit touching 5 files gave `audit: 0 errors` with no Guardian line.
2. Full clone: `--is-shallow-repository` returned `false`. The checked HEAD gave 0 errors. Each of these cases was in a fresh full clone:
   - unchecked commit touching 5 files: `ERROR commit 81d6aeb changes 5 files with no Guardian check`
   - no-ff merge of a big unchecked side branch: 1 error on the side commit
   - backdated big commit (2020-01-01): 1 error
   - reused existing report: "didn't add it: each check needs its own new report"
   - verdict buried on the second line: "doesn't open with that verdict"
   - genuine new READY report: 0 errors
   - unchecked miss followed by a genuine NOT READY check: 0 errors (the later check cleared it)
3. Real repo at 90669a5 (clean tree): `audit: 0 errors, 0 warnings`. `fault_drill.py`: `fault drill: 24 of 24 caught`, including "a big commit nobody checked (Guardian)".
4. The limit text is present in all five files and now matches the code: shallow clones are skipped, and full clones are checked. decisions.md:4 opens "a commit after 0696628 (by ancestry)". .github/workflows/audit.yml uses `actions/checkout@v4` with no fetch-depth, so GitHub checks out a shallow clone at depth 1 and the skip applies there. The live repo is not shallow (`false`, no `.git/shallow`), so the local and Stop-hook checks still run.
5. `git ls-remote origin main` returned `90669a5a990a072744af9d37d4f027cfa46e9c22`, and `git branch -r --contains 90669a5` returned `origin/main`.

**Try to break:**
- Hand-made `.git/shallow` in a full clone: section 9 was skipped (first note above).
- Depth-40 clone: skipped, as designed.
- Merge and backdated commits: still caught, as expected.

**NOT VERIFIED:**
- A real GitHub Actions run of 90669a5. I didn't open the run log; the result above is from local shallow clones.
- Whether this READY report gets committed with a matching `Checked-by` line. That is the maker's step.
- git older than 2.15, which lacks `--is-shallow-repository`. The flag would come back as plain text, so a shallow clone would be treated as full and could raise false errors again. The cloud has git 2.43.
- A machine with no git installed at all: `subprocess` would crash rather than skip. This is a guess from reading the code; I didn't run it.
- That the Stop hook really calls audit.py. I only saw that a `Stop` entry exists in .claude/settings.json.

**Pleasing check:** none found. The draft line "full copies behave as before" is backed by the 7 full-clone cases above. "GitHub's shallow copy now skips the check as the rules say" is true for GitHub. It would be more accurate as "any shallow copy skips it", which is the first note.
