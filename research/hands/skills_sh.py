"""Hands Brain source 2: the skills.sh leaderboard (free, public, no sign-up).
Saves today's snapshot: every listed skill with its repo and all-time installs.
Run: python3 research/hands/skills_sh.py   ->  research/hands/sources/skills-sh/leaderboard-<date>.json
The hands-ingest skill then classifies the top skills into a week file
(weeks/<YYYY-Www>-skills-sh.json, "source": "skills.sh")."""
import datetime as dt, json, re, subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
html = subprocess.run(["curl", "-sL", "-m", "60", "https://skills.sh"], capture_output=True, text=True).stdout
rows = re.findall(r'\\"source\\":\\"([^\\"]+)\\",\\"skillId\\":\\"([^\\"]+)\\",\\"name\\":\\"([^\\"]+)\\",\\"installs\\":(\d+)', html)
seen, skills = set(), []
for src, sid, name, inst in rows:
    if (src, sid) in seen: continue
    seen.add((src, sid))
    skills.append({"rank": len(skills) + 1, "repo": src, "skill": sid, "name": name, "installs": int(inst),
                   "url": f"https://skills.sh/{src}/{sid}"})
today = dt.date.today().isoformat()
out = ROOT / f"research/hands/sources/skills-sh/leaderboard-{today}.json"
out.write_text(json.dumps({"date": today, "source": "https://skills.sh", "skills": skills}, indent=1))
print(f"{len(skills)} skills saved to {out.relative_to(ROOT)}; top 5:", [s["name"] for s in skills[:5]])
