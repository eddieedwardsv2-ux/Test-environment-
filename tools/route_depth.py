"""Router steps: how many hops from AGENTS.md to every current note (Charlie, 2026-10-09:
"show how many steps our router is going through"). A hop = one file naming the next (a
markdown link, a `path`, a bare `file.md`, or a skill/agent named in backticks; skills and
agents are found by name through the skill list). History files are skipped, and never used as a hop.
Run: python3 tools/route_depth.py [file ...]   (the audit warns on any unreached note)."""
import collections, re, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import check_links as cl
ROOT = cl.ROOT.resolve()
def refs(note):
    text=note.read_text(errors='ignore'); out=set()
    for p in cl.MD_LINK.findall(text)+cl.TICK.findall(text)+re.findall(r'`([A-Za-z0-9_.~-]+\.(?:md|json|py|html))`',text)+[f'.claude/skills/{s}/SKILL.md' for s in re.findall(r'`([a-z][a-z0-9-]+)`',text)]+[f'.claude/agents/{s}.md' for s in re.findall(r'`([a-z][a-z0-9-]+)`',text)]:
        if p.startswith(cl.OUTSIDE) or cl.PLACEHOLDER.search(p): continue
        for c in cl.candidates(note,p):
            try: c=c.resolve()
            except Exception: continue
            if c.exists() and (c==ROOT or ROOT in c.parents):
                if c.is_dir():
                    r=c/'README.md'
                    if r.exists(): out.add(r)
                    break
                out.add(c); break
    return out


def route():
    start = ROOT / "AGENTS.md"
    depth, parent, q = {start: 0}, {}, collections.deque([start])
    while q:
        n = q.popleft()
        if n.suffix != ".md": continue
        # History is a record, not a route (Charlie, 10 Oct: "not very efficient when looking at
        # paths"): a note reachable only through decisions.md or a brainstorm has no real route.
        if n != start and cl.HISTORY.search(n.relative_to(ROOT).as_posix()): continue
        for r in refs(n):
            if r not in depth: depth[r] = depth[n] + 1; parent[r] = n; q.append(r)
    cur = [p.resolve() for p in ROOT.rglob("*.md") if ".git" not in p.parts and "templates" not in p.parts
           and not cl.SKIP_NAME.search(p.name) and not cl.HISTORY.search(p.relative_to(ROOT).as_posix())]
    return depth, parent, cur


def path(f, depth, parent):
    p = ROOT / f
    if p not in depth: return f"{f} (no route)"
    out = []
    while p in parent: out.append(p.relative_to(ROOT).as_posix()); p = parent[p]
    return " <- ".join(out + ["AGENTS.md"])


if __name__ == "__main__":
    depth, parent, cur = route()
    hist = collections.Counter(depth.get(p, "unreached") for p in cur)
    print(f"{len(cur)} current notes; hops from the router: " + ", ".join(f"{k}: {v}" for k, v in sorted(hist.items(), key=lambda x: str(x[0]))))
    for p in sorted(cur):
        d = depth.get(p)
        if d is None or d >= 3: print(f"{d if d is not None else 'unreached'} | {path(p.relative_to(ROOT).as_posix(), depth, parent)}")
    for f in sys.argv[1:]: print(depth.get(ROOT / f, "-"), "|", path(f, depth, parent))
