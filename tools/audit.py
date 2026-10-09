"""Cheap automatic audit of Charlie's AI OS (Nate Herk's OS-audit ideas).

Runs on every push via .github/workflows/audit.yml, and locally with
`python3 tools/audit.py`. Read-only: it reports problems, it never fixes them.
Checks: routing integrity, index truth, freshness, queue health, quotes
(standard, creator brains, Hands Brain), Hands Brain schema and freshness, context size.
Exit code 1 if any ERROR (so GitHub shows a red cross); WARNs don't fail.
"""
import re
import sys
from datetime import date, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
errors, warns = [], []


def err(msg): errors.append(msg)
def warn(msg): warns.append(msg)


# 1. Routing integrity: every backticked repo path in the router exists.
router = (ROOT / "AGENTS.md").read_text()
for path in re.findall(r"`((?:\.claude|\.github|context|research|projects|learning|tools)/[^`<>* ]*|[A-Za-z_-]+\.md)`", router):
    if not (ROOT / path.rstrip("/")).exists():
        err(f"AGENTS.md routes to missing path: {path}")
if "@AGENTS.md" not in (ROOT / "CLAUDE.md").read_text():
    err("CLAUDE.md no longer imports @AGENTS.md")

# 2. Index truth: every local markdown link resolves; ✅ transcript marks
#    match files; coverage counts match the files on disk.
for md in ROOT.glob("**/*.md"):
    if ".git" in md.parts:
        continue
    for link in re.findall(r"\]\(([^)#\s]+)(?:#[^)]*)?\)", md.read_text()):
        if not link.startswith("http") and "<" not in link and not (md.parent / link).exists():
            err(f"{md.relative_to(ROOT)}: broken link -> {link}")
for readme in (ROOT / "research").glob("*/README.md"):
    folder, text = readme.parent, readme.read_text()
    marks_text = text + ((folder / "videos.md").read_text() if (folder / "videos.md").exists() else "")
    files = list(folder.glob("*-transcript.md"))
    marks = set(re.findall(r"✅ \[transcript\]\(([^)]+)\)", marks_text))
    # Any "N transcribed" claim, bold or prose (Nate's README said "3
    # transcribed" with 8 files and the old bold-only check missed it).
    for n in re.findall(r"(\d+)\**\s+transcribed", text):
        if int(n) != len(files):
            err(f"{readme.relative_to(ROOT)} says {n} transcribed, folder has {len(files)}")
    if marks and len(marks) != len(files):
        warn(f"{readme.relative_to(ROOT)}: {len(marks)} ✅ marks but {len(files)} transcript files")

# 2a. Transcript filenames: "<title-slug>--<video-id>-transcript.md" with a
#     matching -raw.txt, so Charlie can read folders by eye and tools find
#     files by ID (research/get_transcript.py names them automatically).
NAME = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*--[\w-]{11}-(transcript\.md|raw\.txt)")
for f in list((ROOT / "research").glob("*/*-transcript.md")) + list((ROOT / "research").glob("*/*-raw.txt")):
    if not NAME.fullmatch(f.name):
        err(f"{f.relative_to(ROOT)}: name should be <title-slug>--<video-id>-transcript.md / -raw.txt")
    elif f.name.endswith("-transcript.md") and not f.with_name(f.name[:-len("transcript.md")] + "raw.txt").exists():
        warn(f"{f.relative_to(ROOT)}: no matching -raw.txt (original kept for re-cleaning)")

# 2c. Brain contract: every creator brain has the four pages an advisor
#     agent and the brain-ingest skill rely on, and an agent that uses it.
for brain in (ROOT / "research").glob("*/brain"):
    for page in ("index.md", "concepts.md", "rules.md", "log.md"):
        if not (brain / page).exists():
            err(f"{brain.relative_to(ROOT)} is missing {page}")
    if not any(str(brain.relative_to(ROOT)) in a.read_text() for a in (ROOT / ".claude/agents").glob("*.md")):
        warn(f"{brain.relative_to(ROOT)} has no agent in .claude/agents/ that reads it")

# 2b. Partial transcripts: last timestamp well before the video's length means
#     the service cut it short (found 2026-10-07 on 3-4 hour courses).
def secs(t):
    n = 0
    for part in t.split(":"):
        n = n * 60 + int(part)
    return n
for tr in (ROOT / "research").glob("*/*-transcript.md"):
    text = tr.read_text()
    dur = re.search(r"Duration: ([0-9:]+)", text)
    stamps = re.findall(r"^\*\*\[([0-9:]+)\]", text, re.M)
    if dur and stamps and secs(dur.group(1)) - secs(stamps[-1]) > 300:
        warn(f"{tr.relative_to(ROOT)} is PARTIAL: ends at {stamps[-1]} of {dur.group(1)}; re-fetch it")

# 2d. Reverse routing: every skill and agent is named in the router, so a
#     capability can't exist that no session knows to reuse.
for cap in list((ROOT / ".claude/skills").glob("*/SKILL.md")) + list((ROOT / ".claude/agents").glob("*.md")):
    name = cap.parent.name if cap.name == "SKILL.md" else cap.stem
    if name not in router:
        err(f"{cap.relative_to(ROOT)} is not named in AGENTS.md (nothing routes to it)")

# 3. Freshness: environment facts older than ~3 months should be re-tested.
env = (ROOT / "context/environment.md").read_text()
dates = [datetime.strptime(d, "%Y-%m-%d").date() for d in re.findall(r"\d{4}-\d{2}-\d{2}", env)]
if dates and (date.today() - max(dates)).days > 90:
    warn(f"context/environment.md last tested {max(dates)}: re-test the YouTube/X routes")

# 4. Queue health: every non-comment line is "<creator-folder> <video-id>".
queue = ROOT / "research/transcript-queue.txt"
for n, line in enumerate(queue.read_text().splitlines() if queue.exists() else [], 1):
    if line.strip() and not line.startswith("#") and not re.fullmatch(r"[a-z0-9-]+ [\w-]{11}", line.strip()):
        err(f"transcript-queue.txt line {n} is malformed: {line!r}")

# 4b. Router size (Nate, jdbOVepEtUE 5:36:27: "keep it under 200 lines", it is
#     re-read with every message) and skill/agent front matter (an unclosed
#     quote or missing description silently stops a skill or agent firing).
for router in [ROOT / "AGENTS.md"] + list((ROOT / "templates").glob("*/AGENTS.md")):
    lines = len(router.read_text().splitlines())
    if lines > 200:
        err(f"{router.relative_to(ROOT)} is {lines} lines; Nate's limit is 200")
for cap in list(ROOT.glob(".claude/skills/*/SKILL.md")) + list(ROOT.glob(".claude/agents/*.md")) \
        + list(ROOT.glob("templates/*/.claude/skills/*/SKILL.md")):
    text = cap.read_text()
    fm = re.match(r"---\n(.*?)\n---\n", text, re.S)
    if not fm:
        err(f"{cap.relative_to(ROOT)}: front matter missing or not closed with ---")
        continue
    for key in ("name", "description"):
        m = re.search(rf"^{key}:\s*(.+)$", fm.group(1), re.M)
        if not m:
            err(f"{cap.relative_to(ROOT)}: front matter has no {key}")
        elif m.group(1).count('"') % 2 or (m.group(1).startswith("'") and not m.group(1).rstrip().endswith("'")):
            err(f"{cap.relative_to(ROOT)}: {key} has an unclosed quote")

# 4c. Quarterly refresh: context/current-focus.md carries "Refresh by: YYYY-MM-DD".
m = re.search(r"Refresh by:\*?\*?\s*(\d{4}-\d{2}-\d{2})", (ROOT / "context/current-focus.md").read_text())
if m and date.today() > datetime.strptime(m.group(1), "%Y-%m-%d").date():
    warn(f"context/current-focus.md refresh date {m.group(1)} has passed: review priorities with Charlie, then move the date on 3 months")

# 4d. Secrets: this repo is public, so no keys, tokens or private keys in any
#     file Git would publish, and .env must never be tracked.
import subprocess
SECRET = re.compile(r"(sk-ant-[A-Za-z0-9_-]{20,}|sk-[A-Za-z0-9]{32,}|gh[pousr]_[A-Za-z0-9]{36}|github_pat_[A-Za-z0-9_]{40,}"
                    r"|AKIA[0-9A-Z]{16}|xox[baprs]-[A-Za-z0-9-]{10,}|AIza[0-9A-Za-z_-]{35}|-----BEGIN [A-Z ]*PRIVATE KEY-----)")
files = subprocess.run(["git", "ls-files", "--cached", "--others", "--exclude-standard"], cwd=ROOT,
                       capture_output=True, text=True).stdout.splitlines()
if not files:   # not a Git checkout (a zip or a copy): scan every file instead of none
    import os
    files = [os.path.relpath(os.path.join(d, f), ROOT) for d, ds, fs in os.walk(ROOT)
             if not ds.__setitem__(slice(None), [x for x in ds if x not in {".git", "node_modules", "__pycache__"}]) for f in fs]
for rel in files:
    if rel == ".env" or rel.endswith("/.env"):
        err(f"{rel} would be published: secrets belong in an untracked .env")
    f = ROOT / rel
    if not f.is_file() or f.is_symlink() or f.suffix in {".png", ".jpg", ".pdf"}:
        continue
    try:
        hit = SECRET.search(f.read_text(errors="ignore"))
    except OSError:
        continue
    if hit:
        err(f"{rel}: looks like a secret ({hit.group(0)[:8]}…); remove it and rotate the key")

# 5. Poisoning: every quote in a requirements doc is verbatim at its timestamp.
sys.path.insert(0, str(ROOT / "tools"))
from check_quotes import check, check_linked
for doc in [ROOT / "system/standard-ai-os-v1.md", *sorted(ROOT.glob("research/hands/voices/**/*.md"))]:   # + the presenters' voice files
    if doc.exists():
        for f in check(doc)[1]:
            err(f)
#    Every brain quote cited as "quote" — [m:ss](youtube link) is checked too.
for page in ROOT.glob("research/*/brain/*.md"):
    for f in check_linked(page)[1]:
        err(f)

#    Every rule and concept must reach the maps (a title line the map builder
#    can't read drops it silently, as Rule 19 did on 2026-10-09).
import subprocess as _sp
_out = _sp.run([sys.executable, str(ROOT / "tools/build_brain_map.py"), "--stats"], capture_output=True, text=True).stderr.split()
_bd = ROOT / "research/nate-herk/brain"
_want = (len(re.findall(r"^\*\*\d+\. ", (_bd / "concepts.md").read_text(), re.M)), len(re.findall(r"^\*\*Rule \d+:", (_bd / "rules.md").read_text(), re.M)))
if _out[:2] != [str(_want[0]), str(_want[1])]:
    err(f"research/nate-herk/brain: the map builder reads {_out[:2]} concepts/rules but the files have {list(_want)}; fix the title line it can't read")

# 6. Hands Brain (research/hands/): week files follow the schema, every quote is
#    verbatim in its transcript, ENATE links point at real concepts, and the
#    built list matches the week files (else: rebuild and republish the site).
import json, subprocess
hands = ROOT / "research/hands"
if hands.exists():
    src = (ROOT / "tools/build_hands.py").read_text()
    cats = set(re.findall(r'"([^"]+)"', src[src.index("CATEGORIES"):src.index("]", src.index("CATEGORIES"))]))
    flat = lambda s: " ".join(re.sub(r"\*\*\[[^\]]*\]\([^)]*\)\*\*", " ", s).replace("’", "'").replace("“", '"').replace("”", '"').lower().split())
    texts = {}
    def transcript(vid):
        if vid not in texts:
            f = list(ROOT.glob(f"research/*/*--{vid}-transcript.md"))
            texts[vid] = flat(f[0].read_text()) if f else None
        return texts[vid]
    n_q = 0
    for wf in sorted((hands / "weeks").glob("*.json")):
        rel = wf.relative_to(ROOT)
        try: wk = json.loads(wf.read_text())
        except ValueError as e: err(f"{rel}: not valid JSON ({e})"); continue
        for tl in wk.get("tools", []):
            if re.search(r"zapier|monid", tl.get("name", ""), re.I): warn(f"{rel}: {tl['name']} is a show sponsor, not a tool (hands-ingest rule)")
            if tl.get("category") not in cats: err(f"{rel}: {tl.get('name')} has unknown category {tl.get('category')!r}")
            q, vid = tl.get("quote", ""), tl.get("video")
            if q and vid:
                n_q += 1
                body = transcript(vid)
                parts = [x for x in re.split(r"…|\.\.\.", flat(q)) if len(x.strip(" .,")) > 3]
                if body is None: err(f"{rel}: {tl['name']} cites {vid} but no transcript is saved")
                elif not all(x.strip(" .,") in body for x in parts): err(f"{rel}: {tl['name']} quote not in transcript {vid}: \"{q[:50]}\"")
    nm = hands / "nate-mentions.json"
    for m in (json.loads(nm.read_text()) if nm.exists() else []):
        n_q += 1
        body = transcript(m.get("video"))
        if body is None or flat(m.get("quote", "")).strip(" .,") not in body:
            err(f"research/hands/nate-mentions.json: {m.get('name')} quote not found in {m.get('video')}")
    _skills = {p.parent.name for p in ROOT.glob(".claude/skills/*/SKILL.md")}
    for wf in sorted((hands / "weeks").glob("*.json")):
        try: _tl = json.loads(wf.read_text()).get("tools", [])
        except ValueError: continue   # already reported as not valid JSON above
        for tl in _tl:
            for sk in tl.get("relates") or []:
                if sk not in _skills: err(f"{wf.relative_to(ROOT)}: {tl['name']} relates to missing skill {sk!r}")
    n_concepts = len(re.findall(r"^\*\*\d+\. ", (ROOT / "research/nate-herk/brain/concepts.md").read_text(), re.M))
    el = hands / "enate-links.json"
    for k, arr in (json.loads(el.read_text()) if el.exists() else {}).items():
        for x in arr or []:
            if not 1 <= int(x.get("concept", 0)) <= n_concepts: err(f"research/hands/enate-links.json: {k} links to concept {x.get('concept')}, which doesn't exist")
    if subprocess.run([sys.executable, str(ROOT / "tools/build_hands.py"), "--check"], capture_output=True).returncode:
        warn("research/hands/tools.json is out of date with the week files: run python3 tools/build_hands.py, then republish the Hands Brain")

# 7. Context doctor (tools/context_check.py, our /doctor): what loads every message.
cc = subprocess.run([sys.executable, str(ROOT / "tools/context_check.py")], capture_output=True, text=True).stdout
for line in cc.split("Warnings:")[1].splitlines() if "Warnings:" in cc else []:
    if line.strip().startswith("- "): warn("context: " + line.strip()[2:])

# 8. Claude/Codex parity: a skill the router expects agents to use must not be
#    user-only (disable-model-invocation hides it from Claude; found 2026-10-09
#    with `link`). Skills only Charlie starts are listed here on purpose.
USER_ONLY = {"i-have-adhd"}
#    ...and every skill or agent the router names still exists (found by tools/fault_drill.py).
_r = (ROOT / "AGENTS.md").read_text(); sec = _r[_r.find("## Skills and agents"):]
for name in set(re.findall(r"`([a-z][a-z0-9-]+)`", sec)):
    if not any((ROOT / p).exists() for p in (f".claude/skills/{name}", f".claude/agents/{name}.md", f"references/parked-skills/{name}")):
        err(f"AGENTS.md names `{name}` as a skill or agent, but it doesn't exist")
#    ...and every page's source file in system/pages.md exists, so each page can be rebuilt.
for path in re.findall(r"`([\w./-]+\.(?:html|md|json|py))`", (ROOT / "system/pages.md").read_text()):
    if "/" in path and not (ROOT / path).exists():
        err(f"system/pages.md: page source {path} is missing, so that page can't be rebuilt")
#    ...and helper agents follow system/model-usage.md: inherit the main model until a
#    cheaper route has passed its comparison (ChatGPT's rule, 2026-10-09).
for ag in ROOT.glob(".claude/agents/*.md"):
    m = re.search(r"^model:\s*(\S+)", ag.read_text(), re.M)
    if m and m.group(1) != "inherit" and ag.stem not in (ROOT / "system/model-usage.md").read_text():
        warn(f"{ag.relative_to(ROOT)} uses model {m.group(1)} without a passed comparison in system/model-usage.md")
for cap in ROOT.glob(".claude/skills/*/SKILL.md"):
    if re.search(r"^disable-model-invocation:\s*true", cap.read_text(), re.M) and cap.parent.name not in USER_ONLY:
        err(f"{cap.relative_to(ROOT)} is hidden from Claude (disable-model-invocation); remove it or add it to USER_ONLY in tools/audit.py")
if not (ROOT / ".agents/skills").resolve() == (ROOT / ".claude/skills").resolve():
    err(".agents/skills no longer points at .claude/skills: Codex would see different skills")

# 9. The Guardian (Charlie, 2026-10-09; Nate iTY8Q449YNQ 22:25: "Claude doesn't get to
#    declare itself done"). A big commit (GUARD_FILES+ hand-written files) needs a line
#    "Checked-by: guardian (READY) audits/guardian/<report>.md" (or NOT READY), in it or in a
#    later commit. The report must be added (not edited) by the commit that cites it, live
#    in audits/guardian/, and have the cited verdict as its first line in that commit.
#    A later genuine check clears an earlier miss (history is never rewritten).
#    Commits after GUARD_BASE count, by ancestry, so dates can't hide one. A merge counts
#    only files it changed against every parent (its own additions or conflict fixes).
#    Limits: shallow clones (GitHub Actions) and copies without Git skip this; it proves a
#    report was filed, not that the Guardian wrote it.
GUARD_BASE, GUARD_FROM, GUARD_FILES = "0696628b090127431a86dfbb011f5fcadca50a37", 1791565228, 4
# Paused by Charlie (2026-10-09) until the end of 10 Oct to close broken loops and prove the
# system works first: Guardian problems warn instead of fail. Back on by itself on 11 Oct.
GUARD_PAUSED_UNTIL = date(2026, 10, 10)
guard_flag = warn if date.today() <= GUARD_PAUSED_UNTIL else err
GENERATED = re.compile(r"(brain/map/|system/reader/reader\.html|research/hands/site/|research/hands/tools\.json|audits/guardian/)")
TRAILER = re.compile(r"^Checked-by: guardian \((READY|NOT READY)\) (\S+)", re.M)
def _git(*a): return subprocess.run(["git", *a], cwd=ROOT, capture_output=True, text=True)
_fmt = "--format=%H%x00%P%x00%B%x1e"
_shallow = _git("rev-parse", "--is-shallow-repository").stdout.strip() == "true"  # GitHub's checkout: history missing, skip
_log = _git("log", "-n", "0") if _shallow else _git("log", f"{GUARD_BASE}..HEAD", _fmt) if _git("cat-file", "-e", GUARD_BASE + "^{commit}").returncode == 0 \
    else _git("log", f"--since-as-filter=@{GUARD_FROM}", _fmt)  # e.g. the fault drill's fresh history
def _changed(sha, merge, *extra):
    return _git("diff-tree", "--no-commit-id", "--name-only", "-r", *(["--cc"] if merge else []), *extra, sha).stdout.split()
checked_later = False
for entry in (_log.stdout.split("\x1e") if _log.returncode == 0 else []):
    if "\x00" not in entry:
        continue
    sha, parents, body = entry.strip("\n").split("\x00", 2)
    merge = len(parents.split()) > 1
    m = TRAILER.search(body)
    if m:
        path = m.group(2)
        shown = _git("show", f"{sha}:{path}")
        first = next((l.strip() for l in shown.stdout.splitlines() if l.strip()), "") if shown.returncode == 0 else ""
        problem = (f"cites Guardian report {path}, which isn't a file in audits/guardian/"
                   if not path.startswith("audits/guardian/") or shown.returncode != 0
                   else f"cites {path} but didn't add it: each check needs its own new report"
                   if path not in _changed(sha, merge, "--diff-filter=A")
                   else f"says Guardian {m.group(1)}, but {path} doesn't open with that verdict"
                   if first != f"**{m.group(1)}**" else "")
        if problem and not checked_later:
            guard_flag(f"commit {sha[:7]} {problem}")
        checked_later = checked_later or not problem
        continue
    if checked_later:
        continue
    hand = [f for f in _changed(sha, merge) if not GENERATED.search(f)]
    if len(hand) >= GUARD_FILES:
        guard_flag(f"commit {sha[:7]} changes {len(hand)} files with no Guardian check: run the guardian agent, "
            f"save its report in audits/guardian/, and commit with 'Checked-by: guardian (READY|NOT READY) <report>'")

# 10. Relation links (Charlie, 2026-10-09: "scan our systems and check for relation links").
#     Every file path a current note names exists; the Architect's rules and concepts link
#     both ways. History files (audits, decisions, logs, plans) are skipped: they name old paths on purpose.
sys.path.insert(0, str(ROOT / "tools"))
import check_links
for b in check_links.scan(): warn(f"broken link {b}")
_re, _rw = check_links.brain_relations()
for x in _re: err(f"research/nate-herk/brain: {x}")
for x in _rw: warn(f"research/nate-herk/brain: {x}")

#     ...and every current note can be reached from the router (tools/route_depth.py).
import route_depth
_d, _p, _cur = route_depth.route()
for _n in _cur:
    if _n not in _d: warn(f"{_n.relative_to(ROOT)} can't be reached from AGENTS.md (no current file points to it)")
#     ...and no published page is behind its source (age alone is fine; changed-but-not-republished isn't).
import pages_status
for src, page in pages_status.stale(): warn(f"page {page} is behind {src}: republish it, then `python3 tools/pages_status.py --mark {src}`")

for w in warns:
    print("WARN ", w)
for e in errors:
    print("ERROR", e)
print(f"audit: {len(errors)} errors, {len(warns)} warnings")
sys.exit(1 if errors else 0)
