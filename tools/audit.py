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
    files = list(folder.glob("*-transcript.md"))
    marks = re.findall(r"✅ \[transcript\]\(([^)]+)\)", text)
    m = re.search(r"\*\*(\d+) transcribed\*\*", text)
    if m and int(m.group(1)) != len(files):
        err(f"{readme.relative_to(ROOT)} says {m.group(1)} transcribed, folder has {len(files)}")
    if marks and len(marks) != len(files):
        warn(f"{readme.relative_to(ROOT)}: {len(marks)} ✅ marks but {len(files)} transcript files")

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

for w in warns:
    print("WARN ", w)
for e in errors:
    print("ERROR", e)
print(f"audit: {len(errors)} errors, {len(warns)} warnings")
sys.exit(1 if errors else 0)
