"""Save a creator's recent X (Twitter) posts, free and with no sign-up.

Uses FxTwitter's public API (api.fxtwitter.com), which works from cloud
sessions where x.com itself needs a login (tested 2026-10-07). It is a
volunteer-run service, so it may change or rate-limit; if it fails, paste
posts in by hand.

Usage:  python3 research/get_x_posts.py <creator-folder> <x-handle> [pages]
Writes: research/<creator-folder>/x-posts.md (newest first, ~15-19 posts per page)
For a full history (years), TwitterAPI.io costs ~$0.15 per 1,000 posts (2026)
but needs Charlie's sign-up and payment; ask first.
"""
import json
import sys
import time
import urllib.parse
import urllib.error
import urllib.request
from datetime import datetime
from pathlib import Path

API = "https://api.fxtwitter.com/2/profile/{handle}/statuses"


def get(url, tries=5):
    # The API randomly answers 404 about half the time (tested 2026-10-07),
    # for valid requests too, so retry with a growing pause.
    req = urllib.request.Request(url, headers={"User-Agent": "curl/8.5.0", "Accept": "*/*"})
    for attempt in range(tries):
        try:
            return json.loads(urllib.request.urlopen(req, timeout=60).read())
        except urllib.error.HTTPError as e:
            if e.code not in (404, 429, 500, 502, 503) or attempt == tries - 1:
                raise
            time.sleep(2 * (attempt + 1))


def fetch(handle, pages):
    posts, cursor = [], None
    for _ in range(pages):
        url = API.format(handle=handle)
        if cursor:
            url += "?cursor=" + urllib.parse.quote(cursor)
        data = get(url)
        posts += [p for p in data.get("results", []) if p.get("type") == "status"]
        cursor = (data.get("cursor") or {}).get("bottom")
        if not cursor:
            break
        time.sleep(2)  # be gentle with a free service
    return posts


if __name__ == "__main__":
    folder, handle = Path(__file__).parent / sys.argv[1], sys.argv[2].lstrip("@")
    pages = int(sys.argv[3]) if len(sys.argv) > 3 else 25  # 25 pages ≈ 350 posts ≈ 6 months (tested)
    posts = fetch(handle, pages)
    out = [f"# X posts: @{handle}", "",
           f"Fetched {datetime.now():%Y-%m-%d} via FxTwitter (free, no sign-up). "
           f"{len(posts)} most recent posts, newest first. Reposts are marked.", ""]
    for p in posts:
        when = datetime.fromtimestamp(p["created_timestamp"]).strftime("%Y-%m-%d")
        tag = f" (repost of @{p['author']['screen_name']})" if p.get("reposted_by") else ""
        text = p.get("text", "").replace("\n", " ")
        out.append(f"- **[{when}]({p['url']})**{tag} · {p.get('likes', 0)} likes · "
                   f"{p.get('views') or 0} views — {text}")
    folder.mkdir(parents=True, exist_ok=True)
    (folder / "x-posts.md").write_text("\n".join(out) + "\n")
    print(f"@{handle}: {len(posts)} posts -> {folder / 'x-posts.md'}")
