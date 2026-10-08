"""Builds projects/ai-os-setup-kit/compare/kit-compare.html: two connected maps,
our blank template (templates/standard-ai-os-v1/) and Nate's AIS-OS kit
(github.com/nateherkai/AIS-OS, MIT, shown with credit), stacked on a phone and
side by side on a computer. Nodes are files and skills; lines are the links and
routes between them; rings mark what only one kit has.
Run: python3 tools/build_kit_compare.py [path-to-AIS-OS-clone]   then republish.
Without a path it clones Nate's kit (shallow) into a temp folder."""
import json, os, re, subprocess, sys, tempfile
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/"
OURS_DIR = ROOT + "templates/standard-ai-os-v1/"
if len(sys.argv) > 1: NATE_DIR = sys.argv[1].rstrip("/") + "/"
else:
    NATE_DIR = tempfile.mkdtemp() + "/kit/"
    subprocess.run(["git", "clone", "-q", "--depth", "1", "https://github.com/nateherkai/AIS-OS", NATE_DIR], check=True)
NATE_REV = subprocess.run(["git", "-C", NATE_DIR, "log", "-1", "--format=%h %cs"], capture_output=True, text=True).stdout.strip()

def files_of(base, skip_dirs):
    out = []
    for d, ds, fs in os.walk(base):
        rel = os.path.relpath(d, base)
        ds[:] = sorted(x for x in ds if x != ".git" and os.path.normpath(os.path.join(rel, x)) not in skip_dirs)
        for f in sorted(fs):
            p = os.path.normpath(os.path.join(rel, f))
            if f.endswith((".md", ".sh", ".gitignore", ".gitkeep")) or f in ("LICENSE",):
                out.append(p)
    return out

def role(p):
    m = re.match(r"\.claude/skills/([^/]+)/", p)
    if m: return "skill:" + m.group(1) + ("" if p.endswith("SKILL.md") else ":" + os.path.basename(p))
    if p.startswith("context/"): return "context"
    if p in ("decisions.md", "decisions/log.md"): return "decisions"
    return p

def group(p):
    if p.startswith(".claude/skills/"): return "skills"
    if p in ("AGENTS.md", "CLAUDE.md"): return "rulebook"
    if p.startswith("context/") or p in ("aios-intake.md",): return "context"
    if p in ("decisions.md", "decisions/log.md") or p.startswith("projects/") or p.startswith("archives/"): return "work"
    if p in ("connections.md",) or p.startswith("references/") or p.startswith("research/"): return "knowledge"
    return "guides"

def title(p, text):
    if p.endswith("SKILL.md"):
        n = re.search(r"^name:\s*(.+)$", text, re.M)
        return "/" + (n.group(1).strip() if n else p.split("/")[2])
    if p.endswith(".gitkeep"): return p.split("/")[0] + "/ (empty folder)"
    return p

def resolve(src, t, fileset, skills):
    t = t.split("#")[0].strip().rstrip(".,;:")
    if not t or "://" in t or "*" in t or "{" in t or "<" in t: return None
    m = re.fullmatch(r"/?([a-z0-9-]+)", t)
    if m and m.group(1) in skills: return f".claude/skills/{m.group(1)}/SKILL.md"
    for cand in (os.path.normpath(os.path.join(os.path.dirname(src), t)), os.path.normpath(t.lstrip("/"))):
        if cand in fileset: return cand
        for idx in ("README.md", ".gitkeep", "log.md", "SKILL.md"):
            if os.path.join(cand, idx) in fileset: return os.path.join(cand, idx)
    return None

def build(base, skip_dirs):
    fs = files_of(base, skip_dirs); fileset = set(fs)
    skills = {p.split("/")[2] for p in fs if p.startswith(".claude/skills/")}
    nodes, edges = [], set()
    for p in fs:
        text = open(base + p, encoding="utf-8", errors="ignore").read()
        nodes.append({"id": p, "t": title(p, text), "g": group(p), "r": role(p), "text": text[:6000]})
        if p.endswith((".gitkeep", "LICENSE")): continue
        targets = re.findall(r"\]\(([^)\s]+)\)", text) + re.findall(r"`([^`\s]+)`", text)
        targets += re.findall(r"(?<![\w/])/([a-z][a-z0-9-]+)\b", text)
        for t in targets:
            r = resolve(p, t, fileset, skills)
            if r and r != p: edges.add((p, r))
        if p.startswith(".claude/skills/") and not p.endswith("SKILL.md"):
            sk = "/".join(p.split("/")[:3]) + "/SKILL.md"
            if sk in fileset: edges.add((sk, p))
    deg = {}
    for a, b in edges: deg[a] = deg.get(a, 0) + 1; deg[b] = deg.get(b, 0) + 1
    for n in nodes: n["d"] = deg.get(n["id"], 0)
    return nodes, sorted(edges)

ours_n, ours_e = build(OURS_DIR, set())
nate_n, nate_e = build(NATE_DIR, {".agents", "docs", ".claude/skills/3d-brain/assets"})
ours_roles = {n["r"] for n in ours_n}; nate_roles = {n["r"] for n in nate_n}
for n in ours_n: n["only"] = n["r"] not in nate_roles
for n in nate_n: n["only"] = n["r"] not in ours_roles

COMPARE = [
 ("A rulebook that routes to files", "yes", "yes"),
 ("One rulebook for Claude and Codex, no copying", "yes", "no: two copies kept in step by hand"),
 ("Personalises itself with an interview", "partly: grill-me, open-ended", "yes: /onboard, 7 set questions"),
 ("Scored audit, out of 100", "no: os-audit lists problems, no score", "yes: /audit (Four Cs)"),
 ("Finds the next thing to automate", "no", "yes: /level-up (with the bike method)"),
 ("Register of connected tools", "no", "yes: connections.md"),
 ("Fresh-session test (proves it knows you)", "yes: a day-1 step in the README", "partly: checked inside /audit, not a day-1 step"),
 ("Guide for a bigger knowledge base later", "yes: research/README.md", "partly: EXPANSIONS.md"),
 ("3D brain view", "no", "yes: /3d-brain (computer only)"),
]
data = {"ours": {"nodes": ours_n, "edges": ours_e}, "nate": {"nodes": nate_n, "edges": nate_e, "rev": NATE_REV}, "compare": COMPARE}
src = ROOT + "projects/ai-os-setup-kit/compare/template.html"
out = ROOT + "projects/ai-os-setup-kit/compare/kit-compare.html"
open(out, "w").write(open(src).read().replace("__DATA__", json.dumps(data, ensure_ascii=False).replace("</", "<\\/")))
print(f"ours {len(ours_n)} files {len(ours_e)} links | nate {len(nate_n)} files {len(nate_e)} links ({NATE_REV})", file=sys.stderr)
print("only ours:", [n["id"] for n in ours_n if n["only"]], file=sys.stderr)
print("only nate:", [n["id"] for n in nate_n if n["only"]], file=sys.stderr)
