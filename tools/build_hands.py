"""Hands Brain, step 4: merge every week file into research/hands/tools.json,
rank each category, mark what newer tools have replaced, and build the site
research/hands/site/hands.html from research/hands/site/template.html.
Run: python3 tools/build_hands.py   then republish the page (system/pages.md)."""
import json, re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HANDS = ROOT / "research/hands"
CATEGORIES = ["Coding agents & IDEs", "Claude Code skills & plugins", "Agent orchestration & teams",
              "MCP & connectors", "Knowledge & second brain", "Video, clips & images", "Voice & audio",
              "Marketing, sales & SEO", "Design & websites", "Research & search", "Cost & tokens",
              "Automation & workflows", "Models & LLMs", "Business & finance", "Other"]
PRICE_BONUS = {"free": 1, "open-source": 1, "freemium": 0.5}

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
order = [w["week"] for w in weeks]                        # newest first
tools = {}
for w in weeks:
    for t in w["tools"]:
        k = key(t)
        e = tools.setdefault(k, {"id": k, "name": t["name"], "url": t.get("url", ""), "kind": t.get("kind", ""),
                                 "category": t.get("category") if t.get("category") in CATEGORIES else "Other",
                                 "what": t.get("what", ""), "price": t.get("price", "unknown"),
                                 "for_charlie": 0, "replaces": set(), "sightings": [], "check": ""})
        e["for_charlie"] = max(e["for_charlie"], int(t.get("for_charlie", 0)))
        e["replaces"] |= set(t.get("replaces") or [])
        if t.get("check"): e["check"] = e["check"] or t["check"]
        e["sightings"].append({"week": w["week"], "video": t.get("video"), "t": t.get("t", ""),
                               "shown": t.get("shown", ""), "quote": t.get("quote", "")})

latest = order[0] if order else None
names = {}
for e in tools.values(): names.setdefault(norm(e["name"]), e)
for e in tools.values():
    seen = sorted({s["week"] for s in e["sightings"]}, reverse=True)
    e["weeks"], e["first"], e["last"] = seen, seen[-1], seen[0]
    e["mentions"] = len({s["video"] for s in e["sightings"]})
    age = order.index(e["last"])
    e["score"] = round(3 * e["for_charlie"] + 2 * e["mentions"] + max(0, 3 - age) + PRICE_BONUS.get(e["price"], 0), 1)
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
ranked = sorted(tools.values(), key=lambda e: (e["status"] == "replaced", -e["score"], e["name"].lower()))
for c in CATEGORIES:
    for i, e in enumerate([e for e in ranked if e["category"] == c], 1): e["rank"] = i

(HANDS / "tools.json").write_text(json.dumps(ranked, indent=1, ensure_ascii=False))
# ENATE (Nate's brain) concepts, and links from tools to them (written by a helper; optional).
concepts = [{"n": int(m.group(1)), "title": m.group(2)} for m in
            re.finditer(r"^\*\*(\d+)\. (.+?)\*\*$", (ROOT / "research/nate-herk/brain/concepts.md").read_text(), re.M)]
def opt(name, empty):
    f = HANDS / name
    return json.loads(f.read_text()) if f.exists() else empty
data = {"tools": ranked, "concepts": concepts, "enate": opt("enate-links.json", {}),
        "nate": opt("nate-mentions.json", []), "weeks": [{"week": w["week"], "summary": w.get("summary", ""), "videos": w.get("videos", [])} for w in weeks],
        "videos": videos, "categories": CATEGORIES}
tpl = (HANDS / "site/template.html").read_text()
(HANDS / "site/hands.html").write_text(tpl.replace("__DATA__", json.dumps(data, ensure_ascii=False).replace("</", "<\\/")))
print(f"{len(ranked)} tools from {len(weeks)} weeks ({', '.join(order)}); "
      f"{sum(e['status'] == 'replaced' for e in ranked)} replaced, {sum(e['status'] == 'new' for e in ranked)} new")
