"""Builds system/merge-map/merge-map.html: two connected maps of Charlie's whole OS.
Top/left: the repo as it is today. Bottom/right: the same work as if we had
started from Nate's AIS-OS kit (github.com/nateherkai/AIS-OS, MIT) and placed
everything by his own rules (AGENTS.md "Where things live" and EXPANSIONS.md).
Each dot is coloured by what happens to it: same place, moved, folded into a
kit file, not needed, or new from the kit. The MOVES table holds every rule and
its reason; edit it there, not in the page.
Run: python3 tools/build_merge_map.py [path-to-AIS-OS-clone]   then republish."""
import json, os, re, subprocess, sys, tempfile
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from graph_lib import files_of, skill_title, links_of, parent_skill, degrees
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/"
if len(sys.argv) > 1: NATE_DIR = sys.argv[1].rstrip("/") + "/"
else:
    NATE_DIR = tempfile.mkdtemp() + "/kit/"
    subprocess.run(["git", "clone", "-q", "--depth", "1", "https://github.com/nateherkai/AIS-OS", NATE_DIR], check=True)
NATE_REV = subprocess.run(["git", "-C", NATE_DIR, "log", "-1", "--format=%h %cs"], capture_output=True, text=True).stdout.strip()

# (path or folder prefix, new path or prefix, status, why). First match wins.
# status: moved | merged (folds into an existing kit file) | dropped (not needed if we'd started from the kit)
E = "EXPANSIONS.md"
MOVES = [
 ("decisions.md", "decisions/log.md", "moved", f"The kit keeps decisions in decisions/log.md, and {E} says never to have both."),
 ("system/comparison-vs-nate.md", "archives/comparison-vs-nate.md", "moved", "It's history now. The kit's rule: old files go to archives/, never deleted."),
 ("system/README.md", None, "dropped", "The kit has no system/ folder, so no folder index is needed."),
 ("system/", "references/", "moved", "The kit has no system/ folder. Frameworks and how-it-works guides live in references/."),
 ("context/mac-day.md", "references/sops/mac-day.md", "moved", f"A step-by-step checklist is an SOP; {E} puts those in references/sops/."),
 ("context/environment.md", "references/cloud-environment.md", "moved", "A guide to a tool (cloud sessions), like the kit's references/{tool}-api.md files."),
 ("tools/", "scripts/", "moved", f"{E}: Python or Bash scripts go in scripts/."),
 ("learning/", "projects/learning/", "moved", f"An ongoing workstream with its own context; {E} puts those in projects/."),
 ("exports/", "templates/chatgpt/", "moved", f"A copy-and-paste starting point is a template ({E}: templates/)."),
 ("templates/README.md", None, "dropped", "Our blank-template folder isn't needed: Nate's kit itself is the blank copy."),
 ("templates/standard-ai-os-v1/", None, "dropped", "Started from Nate's kit, the kit is the blank copy. No second template to keep in step."),
 (".claude/skills/os-audit/SKILL.md", ".claude/skills/audit/SKILL.md", "merged", "The kit's /audit already checks routing, stale facts and clashes: one audit skill instead of two."),
]
NEW = {  # files a Nate-first OS would have that ours doesn't (why)
 ".claude/skills/3d-brain/SKILL.md": "Ships with the kit: the 3D brain view (needs a computer).",
 "scripts/sync-codex-skills.sh": "Ships with the kit: copies skills for Codex. (We use one shared folder instead.)",
 "research/CLAUDE.md": f"{E}: a vertical with its own transcripts and scripts becomes a sub-OS with its own short manual.",
}

def new_path(p):
    for src, dst, st, why in MOVES:
        if p == src or (src.endswith("/") and p.startswith(src)):
            if dst is None: return None, st, why
            return (dst + p[len(src):] if src.endswith("/") else dst), st, why
    return p, "same", ""

def group(p):
    if p.startswith((".claude/skills/", ".claude/agents/")): return "skills"
    if p in ("AGENTS.md", "CLAUDE.md", ".claude/settings.json"): return "rulebook"
    if p.startswith(("context/", "brainstorms/")) or p == "aios-intake.md": return "context"
    if p.startswith(("projects/", "learning/", "audits/", "archives/", "decisions")): return "work"
    if p.startswith("research/"): return "research"
    if p.startswith(("references/", "system/")) or p == "connections.md": return "knowledge"
    if p.startswith(("tools/", "scripts/", ".github/")) or p.endswith((".py", ".sh")): return "scripts"
    return "guides"

# --- today's repo ---
tracked = set(subprocess.run(["git", "-C", ROOT, "ls-files"], capture_output=True, text=True).stdout.split())
is_tx = lambda p: p.endswith(("-transcript.md", "-raw.txt"))
fs = [p for p in files_of(ROOT, {".git", ".agents"}, exts=(".md", ".py", ".sh", ".yml", ".json"), names=(),
      skip=lambda p: p not in tracked or is_tx(p))]
fileset = set(fs); skills = {p.split("/")[2] for p in fs if p.startswith(".claude/skills/")}
kit_files = set(files_of(NATE_DIR, {".agents", "docs"}, exts=(".md", ".sh"), names=()))
nodes, edges, byid = [], set(), {}
for p in fs:
    text = open(ROOT + p, encoding="utf-8", errors="ignore").read()
    t = skill_title(p, text) if p.endswith("SKILL.md") else p
    n = {"id": p, "t": t, "g": group(p), "text": text[:5000], "kit": p in kit_files}
    nodes.append(n); byid[p] = n
    edges |= {(p, r) for r in links_of(p, text, fileset, skills, bare=True)}
    sk = parent_skill(p, fileset)
    if sk: edges.add((sk, p))
# transcripts: one dot per creator, linked from every file that cites one of its videos
tx = {}
for p in tracked:
    m = re.match(r"research/([^/]+)/.+--([\w-]{11})-(?:transcript\.md|raw\.txt)$", p)
    if m: tx.setdefault(m.group(1), set()).add(m.group(2))
for c, ids in sorted(tx.items()):
    cid = f"research/{c}/transcripts"
    nodes.append({"id": cid, "t": f"research/{c}/ ({len(ids)} transcripts)", "g": "research", "kit": False,
                  "text": f"{len(ids)} saved video transcripts from {c}, shown as one dot to keep the map readable."})
    byid[cid] = nodes[-1]; edges.add((f"research/{c}/README.md", cid)) if f"research/{c}/README.md" in fileset else None
    pat = re.compile("|".join(map(re.escape, ids)))
    for n in nodes:
        if n["id"] != cid and not n["id"].endswith("transcripts") and pat.search(open(ROOT + n["id"], errors="ignore").read()):
            edges.add((n["id"], cid))
# our blank template: one dot (it all goes the same way)
TPL = "templates/standard-ai-os-v1/"
tpl = [n for n in nodes if n["id"].startswith(TPL)]
nodes = [n for n in nodes if not n["id"].startswith(TPL)]
nodes.append({"id": TPL, "t": f"{TPL} ({len(tpl)} files)", "g": "guides", "kit": False,
              "text": "Our blank, not-yet-personalised copy of the OS. Files: " + ", ".join(n["id"][len(TPL):] for n in tpl)})
cl = lambda p: TPL if p.startswith(TPL) else p
edges = {(cl(a), cl(b)) for a, b in edges}
edges = {(a, b) for a, b in edges if a != b}

# --- the same work, Nate-first ---
moves, hyp, hmap = [], {}, {}
for n in nodes:
    np_, st, why = new_path(n["id"]) if not n["id"].endswith("transcripts") else (n["id"], "same", "")
    if st == "same" and n["kit"]: st = "kit"
    n["st"], n["to"], n["why"] = st, np_, why
    if st in ("moved", "merged", "dropped"): moves.append([n["id"], np_ or "", st, why])
    if np_ is None: continue
    hmap[n["id"]] = np_
    if np_ in hyp:  # folded into an existing file
        hyp[np_]["from"].append(n["id"]); continue
    hyp[np_] = {"id": np_, "t": skill_title(np_, n["text"]) if np_.endswith("SKILL.md") else np_, "g": group(np_),
                "text": n["text"], "st": st, "why": why, "from": [n["id"]], "kit": n["kit"]}
for p, why in NEW.items():
    src = NATE_DIR + p
    text = open(src, errors="ignore").read()[:5000] if os.path.exists(src) else "(A new short manual for the research vertical: what lives here, how to add a creator, which skills and agents to use.)"
    hyp[p] = {"id": p, "t": skill_title(p, text) if p.endswith("SKILL.md") else p, "g": group(p), "text": text, "st": "new", "why": why, "from": [], "kit": p in kit_files}
hedges = {(hmap[a], hmap[b]) for a, b in edges if a in hmap and b in hmap and hmap[a] != hmap[b]}
hedges |= {("AGENTS.md", ".claude/skills/3d-brain/SKILL.md"), ("AGENTS.md", "scripts/sync-codex-skills.sh"),
           ("research/CLAUDE.md", "research/README.md"), ("AGENTS.md", "research/CLAUDE.md")}
for s in ("brain-ingest", "research-creator"): hedges.add(("research/CLAUDE.md", f".claude/skills/{s}/SKILL.md"))
for a in ("video-tutor", "nate-brain", "nick-brain"): hedges.add(("research/CLAUDE.md", f".claude/agents/{a}.md"))
hedges = {e for e in hedges if e[0] in hyp and e[1] in hyp}
hnodes = list(hyp.values())
for n in nodes: n.pop("kit", None)
degrees(nodes, edges); degrees(hnodes, hedges)
count = lambda xs: {k: sum(1 for n in xs if n["st"] == k) for k in ("kit", "same", "moved", "merged", "dropped", "new")}
data = {"now": {"nodes": nodes, "edges": sorted(edges)}, "nate": {"nodes": hnodes, "edges": sorted(hedges)},
        "moves": sorted(moves, key=lambda m: ("moved", "merged", "dropped").index(m[2])), "rev": NATE_REV,
        "counts": {"now": count(nodes), "nate": count(hnodes)}}
if "--stats" in sys.argv: print(json.dumps(data["counts"])); sys.exit()
src = ROOT + "system/merge-map/template.html"; out = ROOT + "system/merge-map/merge-map.html"
open(out, "w").write(open(src).read().replace("__DATA__", json.dumps(data, ensure_ascii=False).replace("</", "<\\/")))
print(f"now {len(nodes)} dots {len(edges)} links | nate-first {len(hnodes)} dots {len(hedges)} links ({NATE_REV})", file=sys.stderr)
print(data["counts"], file=sys.stderr)
for m in data["moves"]: print("  ", m[2], m[0], "->", m[1], file=sys.stderr)
