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

for w in warns:
    print("WARN ", w)
for e in errors:
    print("ERROR", e)
print(f"audit: {len(errors)} errors, {len(warns)} warnings")
sys.exit(1 if errors else 0)
