"""Shared code for the map builders (build_kit_compare.py, build_merge_map.py):
walk a folder's files, find the links between them, return nodes and edges."""
import os, re

def files_of(base, skip_dirs=(), exts=(".md", ".sh", ".gitignore", ".gitkeep"), names=("LICENSE",), skip=lambda p: False):
    out = []
    for d, ds, fs in os.walk(base):
        rel = os.path.relpath(d, base)
        ds[:] = sorted(x for x in ds if x != ".git" and os.path.normpath(os.path.join(rel, x)) not in skip_dirs)
        for f in sorted(fs):
            p = os.path.normpath(os.path.join(rel, f))
            if (f.endswith(exts) or f in names) and not skip(p):
                out.append(p)
    return out

def skill_title(p, text):
    n = re.search(r"^name:\s*(.+)$", text, re.M)
    return "/" + (n.group(1).strip() if n else p.split("/")[2])

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

BARE = r"(?<![\w./-])((?:\.?[\w-]+/)+[\w.-]+\.(?:md|py|sh|yml|json))"

def links_of(p, text, fileset, skills, bare=False):
    """Every file p points at: markdown links, `backtick` paths, /skill names (and bare paths if asked)."""
    targets = re.findall(r"\]\(([^)\s]+)\)", text) + re.findall(r"`([^`\s]+)`", text)
    targets += re.findall(r"(?<![\w/])/([a-z][a-z0-9-]+)\b", text)
    if bare: targets += re.findall(BARE, text)
    out = set()
    for t in targets:
        r = resolve(p, t, fileset, skills)
        if r and r != p: out.add(r)
    return out

def parent_skill(p, fileset):
    """A skill's extra files (rubric, templates) hang off its SKILL.md."""
    if p.startswith(".claude/skills/") and not p.endswith("SKILL.md"):
        sk = "/".join(p.split("/")[:3]) + "/SKILL.md"
        if sk in fileset: return sk

def degrees(nodes, edges):
    deg = {}
    for a, b in edges: deg[a] = deg.get(a, 0) + 1; deg[b] = deg.get(b, 0) + 1
    for n in nodes: n["d"] = deg.get(n["id"], 0)
