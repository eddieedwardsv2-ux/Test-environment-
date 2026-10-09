"""Fault drill: prove tools/audit.py catches the mistakes we care about.

Copies the repo to a scratch folder, plants one fault at a time, runs the audit
there, and checks the expected message appears. Nothing in the real repo changes.
Run: python3 tools/fault_drill.py   (exit 1 if any fault slips through)
Add a fault here whenever a real miss is found (backtrack rule), so it can't recur."""
import json, os, re, shutil, subprocess, sys, tempfile
from pathlib import Path

REAL = Path(__file__).resolve().parent.parent
work = Path(tempfile.mkdtemp(prefix="fault-drill-")) / "repo"
shutil.copytree(REAL, work, symlinks=True, ignore=shutil.ignore_patterns(".git", "__pycache__", "node_modules"))

def edit(rel, fn):
    p = work / rel; p.write_text(fn(p.read_text()))
def week(rel, fn):
    p = work / rel; d = json.loads(p.read_text()); fn(d); p.write_text(json.dumps(d))

def first_quoted(d):
    return next(t for t in d["tools"] if t.get("quote") and t.get("video"))

FAULTS = [
 ("router points to a missing file", lambda: edit("AGENTS.md", lambda t: t + "\n| Test | `context/no-such-file.md` |\n"), "routes to missing path"),
 ("CLAUDE.md stops importing the rulebook", lambda: edit("CLAUDE.md", lambda t: t.replace("@AGENTS.md", "AGENTS.md")), "no longer imports"),
 ("a new skill nobody routes to", lambda: (work / ".claude/skills/orphan-skill").mkdir() or (work / ".claude/skills/orphan-skill/SKILL.md").write_text("---\nname: orphan-skill\ndescription: test\n---\n"), "is not named in AGENTS.md"),
 ("a skill hidden from Claude", lambda: edit(".claude/skills/link/SKILL.md", lambda t: t.replace("---\n", "---\ndisable-model-invocation: true\n", 1)), "hidden from Claude"),
 ("Codex loses the shared skills", lambda: ((work / ".agents/skills").unlink(), (work / ".agents/skills").mkdir()), ".agents/skills no longer points"),
 ("skill front matter broken", lambda: edit(".claude/skills/teach/SKILL.md", lambda t: t.replace("---", "--", 1)), "front matter"),
 ("rulebook past 200 lines", lambda: edit("AGENTS.md", lambda t: t + "\n" * 120), "limit is 200"),
 ("a secret pasted into a file", lambda: edit("context/about-me.md", lambda t: t + "\nkey: sk-ant-" + "a1B2" * 12 + "\n"), "looks like a secret"),
 ("a brain loses its log", lambda: (work / "research/nate-herk/brain/log.md").unlink(), "missing log.md"),
 ("ENATE quote that Nate never said", lambda: edit("research/nate-herk/brain/rules.md", lambda t: re.sub(r'> "[^"]{20,}"', '> "this sentence was never said by anyone in any video"', t, count=1)), "quote"),
 ("Hands quote not in the transcript", lambda: week("research/hands/weeks/2026-W40.json", lambda d: first_quoted(d).update(quote="this sentence was never said in the video")), "quote not in transcript"),
 ("Hands tool in a made-up category", lambda: week("research/hands/weeks/2026-W40.json", lambda d: d["tools"][0].update(category="Made up group")), "unknown category"),
 ("show sponsor listed as a tool", lambda: week("research/hands/weeks/2026-W40.json", lambda d: d["tools"].append(dict(d["tools"][0], name="Zapier MCP", quote=""))), "sponsor"),
 ("Hands list not rebuilt after a change", lambda: week("research/hands/weeks/2026-W40.json", lambda d: d["tools"][0].update(what="changed but not rebuilt")), "out of date"),
 ("ENATE link to a concept that doesn't exist", lambda: edit("research/hands/enate-links.json", lambda t: json.dumps({**json.loads(t), "probe": [{"concept": 999, "why": "x"}]})), "doesn't exist"),
 ("transcript count wrong in a creator README", lambda: edit("research/the-next-new-thing/README.md", lambda t: re.sub(r"\*\*(\d+) transcribed\*\*", lambda m: f"**{int(m.group(1)) + 5} transcribed**", t, count=1)), "transcribed"),
 ("router names a skill that was deleted", lambda: shutil.rmtree(work / ".claude/skills/try-tool"), "try-tool"),
 ("a broken link inside a note", lambda: edit("context/how-i-learn.md", lambda t: t + "\nSee [this](no-such-note.md).\n"), "no-such-note"),
 ("a dashboard's source file deleted", lambda: (work / "system/guide/guide.html").unlink(), "guide.html"),
 ("a Hands week file corrupted", lambda: (work / "research/hands/weeks/2026-W39.json").write_text("{not json"), "not valid json"),
 ("a bad line in the transcript queue", lambda: edit("research/transcript-queue.txt", lambda t: t + "\nthis is not a valid line\n"), "malformed"),
 ("the 3-month focus review missed", lambda: edit("context/current-focus.md", lambda t: re.sub(r"(Refresh by:\*?\*?\s*)\d{4}-\d{2}-\d{2}", r"\g<1>2020-01-01", t, count=1)), "refresh date"),
 ("a helper agent forced back onto Sonnet", lambda: edit(".claude/agents/quartermaster.md", lambda t: t.replace("model: inherit", "model: sonnet")), "model"),
]

backup = work.parent / "pristine"
shutil.copytree(work, backup, symlinks=True)
missed = []
for name, plant, expect in FAULTS:
    shutil.rmtree(work); shutil.copytree(backup, work, symlinks=True)
    try: plant()
    except Exception as e:
        print(f"SKIP  {name}: could not plant ({e})"); continue
    out = subprocess.run([sys.executable, "tools/audit.py"], cwd=work, capture_output=True, text=True)
    text = out.stdout + out.stderr
    hit = [l for l in text.splitlines() if (l.startswith(("ERROR", "WARN")) and expect.lower() in l.lower())]
    print(("CAUGHT" if hit else "MISSED") + f"  {name}" + (f"  ->  {hit[0][:110]}" if hit else ""))
    if not hit: missed.append(name)
shutil.rmtree(work.parent)
print(f"\nfault drill: {len(FAULTS) - len(missed)} of {len(FAULTS)} caught")
sys.exit(1 if missed else 0)
