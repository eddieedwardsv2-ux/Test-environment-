"""Hands Brain source 3: Anthropic's plugin marketplaces (free, public, no sign-up).
Saves one snapshot of every plugin listed in Anthropic's three catalogs, used as a
trust layer: a tool listed there passed Anthropic's checks (the community catalog:
"passed automated security scanning, and been approved for distribution"; entries
are pinned to a commit). There are no ratings or reviews in the catalogs.
Run: python3 research/hands/anthropic_market.py  ->  research/hands/sources/anthropic-market/latest.json
tools/build_hands.py then marks matching tools (repo first, then exact name)."""
import datetime as dt, json, re, subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
RAW = "https://raw.githubusercontent.com/anthropics/{}/main/.claude-plugin/marketplace.json"
MARKETS = {"official": "claude-plugins-official", "community": "claude-plugins-community",
           "knowledge-work": "knowledge-work-plugins"}

def repo_of(p, market_repo):
    s = p.get("source")
    url = s.get("url") or s.get("repo") or "" if isinstance(s, dict) else ""
    if isinstance(s, str): url = f"https://github.com/anthropics/{market_repo}"   # lives inside the catalog's own repo
    if isinstance(s, dict) and s.get("source") == "github" and s.get("repo"): url = "https://github.com/" + s["repo"]
    m = re.search(r"github\.com[/:]([\w.-]+/[\w.-]+?)(?:\.git)?/?$", url or "")
    return m.group(1).lower() if m else (url or "")

plugins, counts = [], {}
for market, repo in MARKETS.items():
    out = subprocess.run(["curl", "-sfL", "-m", "90", RAW.format(repo)], capture_output=True, text=True)
    if out.returncode: raise SystemExit(f"could not fetch {repo} (curl exit {out.returncode}); nothing saved")
    rows = json.loads(out.stdout)["plugins"]
    counts[market] = len(rows)
    for p in rows:
        plugins.append({"name": p["name"], "market": market, "repo": repo_of(p, repo),
                        "what": (p.get("description") or "")[:160]})
dest = ROOT / "research/hands/sources/anthropic-market/latest.json"
dest.parent.mkdir(parents=True, exist_ok=True)
dest.write_text(json.dumps({"date": dt.date.today().isoformat(), "counts": counts, "plugins": plugins}, indent=0, ensure_ascii=False))
print(f"saved {len(plugins)} plugins to {dest.relative_to(ROOT)}:", counts)
