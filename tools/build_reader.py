"""Reading Room: turns plan and brainstorm files (Markdown) into one easy-to-read
page in the Hands Brain's dark style, newest plan first, with a link to answer on
the Decision Desk. Run: python3 tools/build_reader.py  then republish
system/reader/reader.html (link in system/pages.md). Add files to DOCS below."""
import json, re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DESK = "https://claude.ai/artifact/R7efnQ6QZtGKVsyV1fCuxx"
DOCS = [  # (file, short label, Desk card it feeds or None)
    ("brainstorms/2026-10-09-middle-plans.md", "The middle: two plans", "middle-go"),
    ("context/todo.md", "Everything unfinished", None),
    ("research/council-plan.md", "The council plan", None),
    ("system/model-usage.md", "How we choose models", None),
]
SUMMARY = {  # plain-English "in short" box shown above a document
    "brainstorms/2026-10-09-middle-plans.md": [
        "Plan 1: give the brains job titles. ENATE becomes the Architect, the Hands Brain the Quartermaster. Names only; folders and links stay.",
        "Plan 2: one skill fetches YouTube videos for every brain, instead of the same steps copied into three skills.",
        "Recommended: do Plan 2 first (nothing gets renamed, easy to test), then Plan 1. Each is about one session.",
    ],
}
docs = []
for path, label, card in DOCS:
    p = ROOT / path
    if not p.exists(): continue
    text = p.read_text()
    words = len(re.findall(r"\w+", text))
    docs.append({"path": path, "label": label, "card": card, "md": text, "mins": max(1, round(words / 220)), "summary": SUMMARY.get(path, [])})
tpl = (ROOT / "system/reader/template.html").read_text()
out = tpl.replace("__DATA__", json.dumps({"docs": docs, "desk": DESK}, ensure_ascii=False).replace("</", "<\\/"))
(ROOT / "system/reader/reader.html").write_text(out)
print(f"{len(docs)} documents:", ", ".join(d["label"] for d in docs))
