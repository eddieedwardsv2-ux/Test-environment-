"""Hands Brain pipeline, step 1 (free, no sign-up, no rate limit worth noting).
Lists a channel's videos newest first, fetches each description through
Invidious (descriptions carry the show's own "Links featured" list and
chapters), and writes one JSON per video with the links and chapter times
already parsed. Transcripts are fetched separately (research/get_transcript.py).

Run: python3 research/hands/pipeline.py [--weeks 4] [--channel URL] [--creator the-next-new-thing]
Output: research/hands/sources/<creator>/videos.json  (newest first, ISO week per video)
Next steps (the hands-ingest skill): one helper per week classifies the tools into
research/hands/weeks/<week>.json, then tools/build_hands.py merges, ranks and builds the site."""
import argparse, datetime as dt, json, re, subprocess, time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
ap = argparse.ArgumentParser()
ap.add_argument("--creator", default="the-next-new-thing")
ap.add_argument("--channel", default="https://www.youtube.com/channel/UCNZEktrsM5oJZ-MK4jKPMOQ/videos")
ap.add_argument("--weeks", type=int, default=4)
a = ap.parse_args()

SKIP = re.compile(r"thenextnewthing\.ai|zapier\.com|monid\.ai|utm_source=creator|sponsor", re.I)
LINK = re.compile(r"^\s*[-•]\s*(.+?)\s*(?:[:—–-]\s*)(https?://\S+)\s*$")
CHAP = re.compile(r"^(\d{1,2}:\d{2}(?::\d{2})?)\s+(.+)$")

def curl_json(url):
    for attempt in range(3):
        r = subprocess.run(["curl", "-s", "-m", "40", url], capture_output=True, text=True).stdout
        try: return json.loads(r)
        except ValueError: time.sleep(5 * (attempt + 1))
    return {}

out_file = ROOT / f"research/hands/sources/{a.creator}/videos.json"
old = {v["id"]: v for v in json.loads(out_file.read_text())} if out_file.exists() else {}
since = dt.date.today() - dt.timedelta(weeks=a.weeks)
listing = subprocess.run(["yt-dlp", "--flat-playlist", "--extractor-args", "youtubetab:approximate_date",
    "--print", "%(id)s|%(duration)s|%(upload_date)s|%(title)s", "--playlist-end", str(a.weeks * 8), a.channel],
    capture_output=True, text=True).stdout.splitlines()
videos = []
for line in listing:
    vid, dur, approx, title = line.split("|", 3)
    v = old.get(vid)
    if not v or not v.get("desc"):
        j = curl_json(f"https://invidious.f5.si/api/v1/videos/{vid}")
        time.sleep(1)
        pub = dt.datetime.fromtimestamp(j["published"], dt.UTC).date() if j.get("published") else None
        desc = j.get("description", "")
        v = {"id": vid, "title": title, "duration": int(float(dur or 0)), "views": j.get("viewCount"),
             "date": pub.isoformat() if pub else None, "desc": desc}
        if not pub and approx.isdigit():          # Invidious refused: YouTube's approximate date
            v["date"], v["date_approx"] = f"{approx[:4]}-{approx[4:6]}-{approx[6:]}", True
    if v["date"]:
        d = dt.date.fromisoformat(v["date"])
        if d < since: break                      # list is newest first
        y, w, _ = d.isocalendar(); v["week"] = f"{y}-W{w:02d}"
    v["links"] = [{"name": m.group(1).strip(), "url": m.group(2)} for l in v["desc"].splitlines()
                  if (m := LINK.match(l)) and not SKIP.search(m.group(2))]
    v["chapters"] = [{"t": m.group(1), "title": m.group(2)} for l in v["desc"].splitlines() if (m := CHAP.match(l.strip()))]
    tr = list((ROOT / f"research/{a.creator}").glob(f"*--{vid}-transcript.md"))
    v["transcript"] = str(tr[0].relative_to(ROOT)) if tr else None
    videos.append(v)
out_file.write_text(json.dumps(videos, indent=1, ensure_ascii=False))
weeks = {}
for v in videos: weeks.setdefault(v.get("week", "unknown"), []).append(v["id"])
print(f"{len(videos)} videos since {since}:", {w: len(ids) for w, ids in weeks.items()})
print("missing dates or descriptions:", [v["id"] for v in videos if not v["date"] or not v["desc"]])
