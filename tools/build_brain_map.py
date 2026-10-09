"""Builds the Brain dashboard: research/nate-herk/brain/map/brain-map.html.
It maps every Markdown file in the repo (our OS + creator research) and Nate's
concepts and rules as one connected graph (the Hands Brain is left out: it has its own site), plus a one-card-at-a-time
review queue. Run after the repo or brain changes, then republish the page:
    python3 tools/build_brain_map.py
Review marks live in the published page's "flags" database, not in this file."""
import re, json, html, sys
import pathlib as _pl
_ROOT = str(_pl.Path(__file__).resolve().parent.parent) + "/"
B = _ROOT + "research/nate-herk/brain/"
GH = "https://github.com/eddieedwardsv2-ux/test-environment-/blob/main/research/nate-herk/"
REFS = {"os": "../steal-my-exact-ai-os-setup-5-simple-tips--Ek1NBfnnTH0-transcript.md",
        "kb": "../i-built-another-andrej-karpathy-using-claude--bvGptCLDhyo-transcript.md"}
def url(u):
    if u.startswith("http"): return u
    if u.startswith("../"): return GH + u[3:]
    return GH + "brain/" + u
def inline(s):
    s = html.escape(s, quote=False)
    s = re.sub(r'\[([^\]]+)\]\[(\w+)\]', lambda m: f'[{m.group(1)}]({REFS.get(m.group(2),"")})', s)
    s = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', lambda m: f'<a href="{url(m.group(2))}" target="_blank" rel="noopener">{m.group(1)}</a>', s)
    s = re.sub(r'`([^`]+)`', r'<code>\1</code>', s)
    s = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', s)
    s = re.sub(r'(?<![\w*])\*([^*]+)\*(?![\w*])', r'<em>\1</em>', s)
    return s
def blocks(lines):
    out=[]
    for l in lines:
        l=l.rstrip()
        if not l or l=="---": continue
        if l.startswith(">"): out.append({"t":"q","h":inline(l.lstrip("> ").strip())})
        elif l.startswith("**Agent check:**"): out.append({"t":"check","h":inline(l[len("**Agent check:**"):].strip())})
        elif l.startswith("**Used by:**"): continue
        else: out.append({"t":"p","h":inline(l)})
    return out
# concepts
cl = open(B+"concepts.md").read().split("\n")
concepts=[]; section=None; cur=None
for l in cl:
    if l.startswith("## Limits"): break
    m=re.match(r'^## ([A-Z])\. (.*)',l)
    if m: section={"id":m.group(1),"title":m.group(2)}; continue
    m=re.match(r'^\*\*(\d+)\. (.*)\*\*$',l)
    if m:
        cur={"n":int(m.group(1)),"title":m.group(2),"sec":section["id"],"secTitle":section["title"],"lines":[],"rules":[]}
        concepts.append(cur); continue
    if cur is not None:
        if l.startswith("**Used by:**"):
            cur["rules"]=[int(x) for x in re.findall(r'Rule (\d+)',l)]
            if not cur["rules"]: cur["note"]=inline(l[len("**Used by:**"):].strip())
        cur["lines"].append(l)
for c in concepts: c["body"]=blocks(c.pop("lines"))
# rules
rl = open(B+"rules.md").read().split("\n")
rules=[]; cur=None
for l in rl:
    if l.startswith("## Inferring"): break
    m=re.match(r'^\*\*Rule (\d+): (.*?)\*\*\s*(\((.*)\))?\s*$',l)
    if m:
        cur={"n":int(m.group(1)),"title":m.group(2),"conf":m.group(4) or "","lines":[],"concepts":[]}
        rules.append(cur); continue
    if cur is not None:
        for g in re.findall(r'\(Concepts? ([\d, and]+)\)',l):
            cur["concepts"]+= [int(x) for x in re.findall(r'\d+',g)]
        cur["lines"].append(l)
for r in rules:
    r["body"]=blocks(r.pop("lines"))
# union links
for c in concepts:
    for rn in c["rules"]:
        r=next((x for x in rules if x["n"]==rn),None)
        if r and c["n"] not in r["concepts"]: r["concepts"].append(c["n"])
for r in rules:
    for cn in r["concepts"]:
        c=next((x for x in concepts if x["n"]==cn),None)
        if c and r["n"] not in c["rules"]: c["rules"].append(r["n"])
    r["concepts"].sort()
for c in concepts: c["rules"].sort()
print(len(concepts),len(rules),file=sys.stderr)
print("orphan rules",[r["n"] for r in rules if not r["concepts"]],file=sys.stderr)
print("orphan concepts",[c["n"] for c in concepts if not c["rules"]],file=sys.stderr)

# ---------- whole-repo graph ----------
import os
ROOT = _ROOT
REPO = "https://github.com/eddieedwardsv2-ux/test-environment-/blob/main/"
SKIP = {".git", "node_modules", "__pycache__"}
# The Hands Brain has its own site (system/pages.md), so it stays off this map.
HANDS = ("research/hands/", ".claude/skills/hands-ingest/", ".claude/agents/hands-brain.md", "research/the-next-new-thing/")
files = []
for d, ds, fs in os.walk(ROOT):
    ds[:] = sorted(x for x in ds if x not in SKIP)
    for f in sorted(fs):
        rel = os.path.relpath(os.path.join(d, f), ROOT)
        if f.endswith(".md") and not rel.startswith(HANDS):
            files.append(rel)
fileset = set(files)
CREATORS = {"nate-herk": "Nate Herk", "nick-saraev": "Nick Saraev", "andrej-karpathy": "Andrej Karpathy", "the-next-new-thing": "The Next New Thing"}
def group(p):
    parts = p.split("/")
    if p.endswith("-transcript.md"): return "transcripts"
    if parts[0] == "research" and len(parts) > 2 and parts[1] in CREATORS: return "creators"
    if parts[0] in (".claude", ".agents"): return "skills"
    if parts[0] in ("audits",) or p == "decisions.md": return "audits"
    if parts[0] == "projects": return "projects"
    if parts[0] == "templates": return "templates"
    if parts[0] in ("learning", "brainstorms", "exports"): return "learning"
    if parts[0] == "research": return "research"
    return "core"
def title_of(p, text):
    m = re.search(r"^#\s+(.+)$", text, re.M)
    if p.endswith("SKILL.md"):
        n = re.search(r"^name:\s*(.+)$", text, re.M)
        if n: return n.group(1).strip() + " (skill)"
    if p.startswith(".claude/agents/"):
        return os.path.basename(p)[:-3] + " (agent)"
    if m: return re.sub(r"[*`]", "", m.group(1)).replace("Transcript: ", "").strip()
    return p
def excerpt(text):
    t = re.sub(r"^---\n.*?\n---\n", "", text, flags=re.S)
    t = re.sub(r"^#.*$", "", t, flags=re.M)
    t = re.sub(r"\*\*\[\d+:\d+(?::\d+)?\]\([^)]*\)\*\*", "", t)
    t = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", t)
    t = re.sub(r"[*_`>|]", "", t)
    t = re.sub(r"\s+", " ", t).strip()
    return t[:420] + ("…" if len(t) > 420 else "")
vid_to_file = {}
nodes, edges = [], set()
for p in files:
    text = open(ROOT + p, encoding="utf-8", errors="ignore").read()
    m = re.search(r"--([A-Za-z0-9_-]{11})-transcript\.md$", p)
    if m: vid_to_file[m.group(1)] = p
    creator = next((CREATORS[k] for k in CREATORS if p.startswith("research/" + k + "/")), "")
    nodes.append({"id": p, "kind": "file", "g": group(p), "t": title_of(p, text), "ex": excerpt(text),
                  "u": REPO + p, "cr": creator})
def resolve(src, target):
    target = target.split("#")[0].strip()
    if not target or "://" in target or "*" in target or "<" in target: return None
    for cand in (os.path.normpath(os.path.join(os.path.dirname(src), target)), os.path.normpath(target)):
        cand = cand.lstrip("./") if cand.startswith("./") else cand
        if cand in fileset: return cand
        if os.path.isdir(ROOT + cand):
            for idx in ("README.md", "index.md", "SKILL.md"):
                if os.path.join(cand, idx) in fileset: return os.path.join(cand, idx)
    return None
for p in files:
    if p.endswith("-transcript.md"): continue
    text = open(ROOT + p, encoding="utf-8", errors="ignore").read()
    targets = re.findall(r"\]\(([^)\s]+)\)", text) + re.findall(r"`([^`\s]+)`", text)
    targets += [REFS_PATH for REFS_PATH in re.findall(r"^\[\w+\]:\s*(\S+)", text, re.M)]
    for t in targets:
        r = resolve(p, t)
        if r and r != p: edges.add((p, r, "link"))
    # skills named in prose, e.g. "the `audit` skill"
    for s in re.findall(r"`([a-z-]+)` (?:skill|agent)", text):
        for cand in (f".claude/skills/{s}/SKILL.md", f".claude/agents/{s}.md"):
            if cand in fileset and cand != p: edges.add((p, cand, "link"))
    if not p.startswith("research/nate-herk/brain/"):
        for vid in set(re.findall(r"watch\?v=([A-Za-z0-9_-]{11})", text)):
            if vid in vid_to_file: edges.add((p, vid_to_file[vid], "cites"))
CB = "research/nate-herk/brain/concepts.md"; RB = "research/nate-herk/brain/rules.md"
def vids(o):
    return set(re.findall(r"watch\?v=([A-Za-z0-9_-]{11})", " ".join(b["h"] for b in o["body"])))
for c in concepts:
    nid = f"c{c['n']}"
    nodes.append({"id": nid, "kind": "concept", "g": "nate", "t": c["title"], "n": c["n"], "sec": c["sec"], "secTitle": c["secTitle"],
                  "body": c["body"], "rules": c["rules"], "note": c.get("note", ""), "u": REPO + CB})
    edges.add((CB, nid, "has"))
    for v in vids(c):
        if v in vid_to_file: edges.add((nid, vid_to_file[v], "cites"))
    for rn in c["rules"]: edges.add((nid, f"r{rn}", "feeds"))
for r in rules:
    nid = f"r{r['n']}"
    nodes.append({"id": nid, "kind": "rule", "g": "nate", "t": r["title"], "n": r["n"], "conf": r["conf"],
                  "body": r["body"], "concepts": r["concepts"], "u": REPO + RB})
    edges.add((RB, nid, "has"))
    for v in vids(r):
        if v in vid_to_file: edges.add((nid, vid_to_file[v], "cites"))
ids = {n["id"] for n in nodes}
edges = sorted(e for e in edges if e[0] in ids and e[1] in ids)
deg = {}
for a, b, _ in edges: deg[a] = deg.get(a, 0) + 1; deg[b] = deg.get(b, 0) + 1
for n in nodes: n["d"] = deg.get(n["id"], 0)
print(len(nodes), "nodes", len(edges), "connections", "unlinked:", sum(1 for n in nodes if not n["d"]), file=sys.stderr)
T = B + "map/template.html"; out = B + "map/brain-map.html"
if "--stats" in sys.argv: sys.exit(0)
data = {"nodes": nodes, "edges": [list(e) for e in edges]}
open(out, "w").write(open(T).read().replace("__DATA__", json.dumps(data, ensure_ascii=False).replace("</", "<\\/")))
print("wrote", out, file=sys.stderr)
