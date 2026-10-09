"""Reading Room: turns plan and brainstorm files (Markdown) into one easy-to-read
page in the Hands Brain's dark style, newest plan first, with a link to answer on
the Decision Desk. Run: python3 tools/build_reader.py  then republish
system/reader/reader.html (link in system/pages.md). Add files to DOCS below."""
import json, re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DESK = "https://claude.ai/artifact/R7efnQ6QZtGKVsyV1fCuxx"
DOCS = [  # (file, short label, Desk card it feeds or None)
    ("audits/2026-10-09-advisors-and-router.md", "Architect, Quartermaster, router steps", None),
    ("audits/audit-2026-10-09-112239-a7c3.md", "Audit 9 Oct: 64/100", "audit-fixes-2026-10-09"),
    ("brainstorms/2026-10-09-elder-councils-plan.md", "Elder councils plan", "elder-pilot-go"),
    ("brainstorms/2026-10-09-middle-plans.md", "The middle: two plans", "middle-go"),
    ("context/todo.md", "Everything unfinished", None),
    ("research/council-plan.md", "The council plan", None),
    ("system/model-usage.md", "How we choose models", None),
]
SUMMARY = {  # plain-English "in short" box shown above a document
    "audits/2026-10-09-advisors-and-router.md": [
        "They didn't really work together: Nate's own 30 tools were almost missing from the Quartermaster (2 of 30). Now all 30 are in, with his quotes and gold rings.",
        "Each advisor now reads the other's notes; live from the next session.",
        "The router is fine: 85 of 99 notes are 2 steps or fewer away, none unreachable. What was wrong was disconnected knowledge and too much checking per small change.",
    ],
    "brainstorms/2026-10-09-elder-councils-plan.md": [
        "Each Elder gets a council of experts (one is always a contrarian) and a separate guardian who checks the work without seeing the makers' reasoning.",
        "New (3b): each Elder gets a mini-router (its own \"where things live\", links up and across) and a mini-desk (what it settles, what comes to you, same card shape).",
        "Built in so it doesn't just please you: drop is a normal verdict, NOT VERIFIED is never empty, disagreement is said first with reasons. You still decide.",
    ],
    "audits/audit-2026-10-09-112239-a7c3.md": [
        "Score 64/100, up from 49: \"working, with gaps\". Connections is the weakest area (11/25).",
        "Biggest fix: current-focus still tells a new session to answer cards that are already closed.",
        "Five small fixes in all, on one Desk card. The next audit runs by itself on Friday 16 Oct.",
    ],
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
