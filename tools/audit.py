"""Cheap automatic audit of Charlie's AI OS (Nate Herk's OS-audit ideas).

Runs on every push via .github/workflows/audit.yml, and locally with
`python3 tools/audit.py`. Read-only: it reports problems, it never fixes them.
Checks: routing integrity, index truth, freshness, queue health.
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

# 5. Poisoning: every quote in a requirements doc is verbatim at its timestamp.
sys.path.insert(0, str(ROOT / "tools"))
from check_quotes import check, check_linked
for doc in [ROOT / "system/standard-ai-os-v1.md"]:
    if doc.exists():
        for f in check(doc)[1]:
            err(f)
#    Every brain quote cited as "quote" — [m:ss](youtube link) is checked too.
for page in ROOT.glob("research/*/brain/*.md"):
    for f in check_linked(page)[1]:
        err(f)

for w in warns:
    print("WARN ", w)
for e in errors:
    print("ERROR", e)
print(f"audit: {len(errors)} errors, {len(warns)} warnings")
sys.exit(1 if errors else 0)
