"""Hands Brain, step 4: merge every week file into research/hands/tools.json,
rank each category, mark what newer tools have replaced, and build the site
research/hands/site/hands.html from research/hands/site/template.html.
Run: python3 tools/build_hands.py   then republish the page (system/pages.md).
`--check` writes nothing and exits 1 if tools.json is out of date (the audit uses it)."""
import json, re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HANDS = ROOT / "research/hands"
CATEGORIES = ["Coding agents & IDEs", "Claude Code skills & plugins", "Agent orchestration & teams",
              "MCP & connectors", "Knowledge & second brain", "Video, clips & images", "Voice & audio",
              "Marketing, sales & SEO", "Design & websites", "Research & search", "Cost & tokens",
              "Automation & workflows", "Models & LLMs", "Business & finance", "Other"]
# Small bonus: free to use or open source 1, a free tier 0.5, anything paid 0 (price-plan, 2026-10-09)
def price_bonus(e):
    m = (e["cost"] or {}).get("model", "")
    return 1 if m == "free" or e["open_source"] == "yes" else 0.5 if m == "free tier + paid" else 0

def key(t):
    u = (t.get("url") or "").lower()
    m = re.search(r"github\.com/([^/\s?#]+/[^/\s?#]+)", u)
    if m: return "gh:" + m.group(1).removesuffix(".git")
    return "n:" + re.sub(r"[^a-z0-9]", "", t["name"].lower())

def norm(name): return re.sub(r"[^a-z0-9]", "", name.lower())

videos = {}
for f in (HANDS / "sources").glob("*/videos.json"):
    for v in json.loads(f.read_text()):
        videos[v["id"]] = {"id": v["id"], "title": v["title"], "date": v.get("date"), "week": v.get("week"),
                           "duration": v.get("duration"), "creator": f.parent.name}
weeks = sorted((json.loads(p.read_text()) for p in (HANDS / "weeks").glob("*.json")), key=lambda w: w["week"], reverse=True)
order = sorted({w["week"] for w in weeks}, reverse=True)   # newest first; a week can have several sources
import math
tools = {}
for w in weeks:
    for t in w["tools"]:
        k = key(t)
        e = tools.setdefault(k, {"id": k, "name": t["name"], "url": t.get("url", ""), "kind": t.get("kind", ""),
                                 "category": t.get("category") if t.get("category") in CATEGORIES else "Other",
                                 "what": t.get("what", ""), "open_source": t.get("open_source", "unknown"),
                                 "repo": t.get("repo", ""), "cost": t.get("cost"),
                                 "for_charlie": 0, "replaces": set(), "sightings": [], "check": "", "vs": None})
        e["for_charlie"] = max(e["for_charlie"], int(t.get("for_charlie", 0)))
        e["replaces"] |= set(t.get("replaces") or [])
        if t.get("check"): e["check"] = e["check"] or t["check"]
        if t.get("cost") and not e["cost"]: e["cost"] = t["cost"]
        if e["open_source"] == "unknown": e["open_source"] = t.get("open_source", "unknown")
        e["repo"] = e["repo"] or t.get("repo", "")
        if t.get("vs") and not e["vs"]: e["vs"] = t["vs"]
        e["relates"] = sorted(set(e.get("relates", [])) | set(t.get("relates") or []))   # our own skills it maps to
        if t.get("plugin"): e["plugin"] = t["plugin"]          # its exact name in an Anthropic catalog
        if t.get("installs"): e["installs"] = max(e.get("installs", 0), int(t["installs"]))
        e["sightings"].append({"week": w["week"], "source": w.get("source", "The Next New Thing"), "video": t.get("video"), "t": t.get("t", ""),
                               "shown": t.get("shown", ""), "quote": t.get("quote", ""),
                               "opinion": t.get("opinion"), "our_view": t.get("our_view")})

# Source 4 (Charlie, 2026-10-09): the tools Nate Herk himself uses, from the Architect's
# brain (nate-mentions.json: exact quote, timestamp, concept numbers). Each adds one sighting
# "Nate Herk (Architect)" dated to the OLDEST week in the window, so it counts as a mention
# but never as news (his video dates aren't recorded). Tools not yet in the list are added.
NATE_SRC = "Nate Herk (Architect)"
for m in (json.loads((HANDS / "nate-mentions.json").read_text()) if (HANDS / "nate-mentions.json").exists() else []):
    k = m.get("in_hands") or "n:" + norm(m["name"])
    e = tools.setdefault(k, {"id": k, "name": m["name"], "url": f"https://www.youtube.com/watch?v={m['video']}",
                             "kind": m.get("kind", ""), "category": m.get("category") if m.get("category") in CATEGORIES else "Other",
                             "what": m.get("what", ""), "open_source": "unknown", "repo": "", "cost": None,
                             "for_charlie": 2, "replaces": set(), "sightings": [], "check": "Added from Nate's own toolkit; not yet seen on the weekly show or skills.sh.", "vs": None})
    e.setdefault("relates", [])
    e["nate"] = {"quote": m.get("quote", ""), "video": m["video"], "t": m.get("t", ""), "concepts": m.get("concepts", [])}
    if order:
        e["sightings"].append({"week": order[-1], "source": NATE_SRC, "video": m["video"], "t": m.get("t", ""),
                               "shown": "Nate uses it himself", "quote": m.get("quote", ""), "opinion": None, "our_view": None})
latest = order[0] if order else None
names = {}
for e in tools.values(): names.setdefault(norm(e["name"]), e)
for e in tools.values():
    seen = sorted({s["week"] for s in e["sightings"]}, reverse=True)
    e["weeks"], e["first"], e["last"] = seen, seen[-1], seen[0]
    e["mentions"] = len({s["video"] or s["source"] for s in e["sightings"]})
    age = order.index(e["last"])
    # Our own verdict beats the presenter's excitement (Charlie, 2026-10-09): the newest
    # sighting's our_view.need caps relevance (yes 3, maybe 2, no 1).
    needs = [s["our_view"]["need"] for s in sorted(e["sightings"], key=lambda s: s["week"], reverse=True)
             if (s.get("our_view") or {}).get("need")]
    e["need"] = needs[0] if needs else None
    e["relevance"] = min(e["for_charlie"], {"yes": 3, "maybe": 2, "no": 1}.get(e["need"], 3))
    e["score"] = round(3 * e["relevance"] + 2 * e["mentions"] + max(0, 3 - age) + price_bonus(e)
                       + min(3, max(0, math.log10(e.get("installs", 1)) - 3)), 1)   # skills.sh installs: 10k=1, 100k=2, 1M+=3
    e["replaced_by"] = None
for e in tools.values():                                  # newer tool says it replaces an older one
    for old in e["replaces"]:
        o = names.get(norm(old))
        if o and o is not e and order.index(o["last"]) >= order.index(e["last"]):
            o["replaced_by"] = e["name"]
for e in tools.values():
    e["status"] = ("replaced" if e["replaced_by"] else "new" if e["first"] == latest
                   else "rising" if e["mentions"] >= 2 and order.index(e["last"]) <= 1 else "steady")
    e["replaces"] = sorted(e["replaces"])
ours = {p.parent.name for p in ROOT.glob(".claude/skills/*/SKILL.md")} | {p.parent.name for p in ROOT.glob("references/parked-skills/*/SKILL.md")}
# Built into Claude already (Anthropic's own skills): nothing to install, so they leave the ranking too.
BUILTIN = {"pptx", "pdf", "docx", "xlsx", "skill-creator", "deep-research", "docs", "code-review", "security-review", "simplify", "dataviz"}   # see system/capability-map.md
# Features this OS already runs on (found stale by model comparison 2, 2026-10-09).
IN_USE = {"Claude Code agents.md support"}   # CLAUDE.md imports @AGENTS.md
for e in tools.values():
    e["ours"] = norm(e["name"]) in {norm(o) for o in ours}   # we already have a skill by this name
    e["have"] = e["ours"] or norm(e["name"]) in {norm(b) for b in BUILTIN} or e["name"] in IN_USE
    e["shown"] = any(s["video"] for s in e["sightings"])     # False = skills.sh only, never shown in a video
tried = {norm(t["name"]): t for t in (json.loads((HANDS / "tried.json").read_text()) if (HANDS / "tried.json").exists() else [])}
for e in tools.values():                                  # Charlie's own trials (the try-tool skill)
    t = tried.get(norm(e["name"]))
    e["tried"] = t
    if t and t["verdict"] == "keep": e["score"] = round(e["score"] + 5, 1)
# Trust layer (Charlie, 2026-10-09): listed in one of Anthropic's plugin catalogs means it
# passed Anthropic's checks (community: automated security scan + approval; official: Anthropic's
# own list). No ratings exist there, so it is a small bonus, not a verdict. Source 3:
# research/hands/anthropic_market.py. Match on the tool's GitHub repo, else its exact name.
CATALOG_REPOS = {"anthropics/claude-plugins-official", "anthropics/claude-plugins-community", "anthropics/knowledge-work-plugins"}
mk = opt_market = json.loads((HANDS / "sources/anthropic-market/latest.json").read_text()) if (HANDS / "sources/anthropic-market/latest.json").exists() else {"plugins": []}
RANK_M = {"official": 0, "knowledge-work": 1, "community": 2}
by_repo, by_name = {}, {}
for p in sorted(mk["plugins"], key=lambda p: RANK_M[p["market"]]):
    if p["repo"] and p["repo"] not in CATALOG_REPOS: by_repo.setdefault(p["repo"], p)
    by_name.setdefault(norm(p["name"]), p)
def repo_key(url):
    m = re.search(r"github\.com/([\w.-]+/[\w.-]+?)(?:\.git)?/?$", url or "")
    return m.group(1).lower() if m else None
for e in tools.values():
    p, how = by_repo.get(repo_key(e["repo"])), "repo"   # its repo (or part of it) is listed
    if not p and e.get("plugin"): p, how = by_name.get(norm(e["plugin"])), "plugin"   # named in the week file
    if not p and len(norm(e["name"])) >= 5: p, how = by_name.get(norm(e["name"])), "name"   # a plugin of the same name is listed
    e["anthropic"] = {"market": p["market"], "plugin": p["name"], "match": how} if p else None
    if p: e["score"] = round(e["score"] + (2 if p["market"] == "official" else 1), 1)
dropped = lambda e: bool(e["tried"]) and e["tried"]["verdict"] == "drop"
ranked = sorted(tools.values(), key=lambda e: (e["status"] == "replaced", e["have"], dropped(e), -e["score"], e["name"].lower()))
for c in CATEGORIES:                                      # what you already have gets no rank: each #1 is new to you
    for i, e in enumerate([e for e in ranked if e["category"] == c and not e["have"]], 1): e["rank"] = i
for e in ranked:
    if e["have"]: e["rank"] = None

import sys
new_json = json.dumps(ranked, indent=1, ensure_ascii=False)
if "--check" in sys.argv:                                  # used by tools/audit.py: is the site up to date?
    old = (HANDS / "tools.json").read_text() if (HANDS / "tools.json").exists() else ""
    sys.exit(0 if old == new_json else 1)
(HANDS / "tools.json").write_text(new_json)
# ENATE (Nate's brain) concepts, and links from tools to them (written by a helper; optional).
concepts = [{"n": int(m.group(1)), "title": m.group(2)} for m in
            re.finditer(r"^\*\*(\d+)\. (.+?)\*\*$", (ROOT / "research/nate-herk/brain/concepts.md").read_text(), re.M)]
def opt(name, empty):
    f = HANDS / name
    return json.loads(f.read_text()) if f.exists() else empty
data = {"tools": ranked, "concepts": concepts, "enate": opt("enate-links.json", {}),
        "nate": [dict(m, in_hands=m.get("in_hands") or "n:" + norm(m["name"])) for m in opt("nate-mentions.json", [])], "weeks": [{"week": wk, "summary": " ".join(w.get("summary", "") for w in weeks if w["week"] == wk),
                   "videos": [v for w in weeks if w["week"] == wk for v in w.get("videos", [])]} for wk in order],
        "videos": videos, "categories": CATEGORIES,
        "market": {"date": mk.get("date"), "counts": mk.get("counts", {})}}
tpl = (HANDS / "site/template.html").read_text()
(HANDS / "site/hands.html").write_text(tpl.replace("__DATA__", json.dumps(data, ensure_ascii=False).replace("</", "<\\/")))
print(f"{len(ranked)} tools from {len(weeks)} weeks ({', '.join(order)}); "
      f"{sum(e['status'] == 'replaced' for e in ranked)} replaced, {sum(e['status'] == 'new' for e in ranked)} new")
