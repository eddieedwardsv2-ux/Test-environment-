"""Fetch a YouTube transcript for free, with no sign-up, from a cloud session.

Why this service: YouTube blocks cloud servers directly (see context/environment.md), but
youtube-transcript.ai runs a free, keyless MCP endpoint on servers YouTube
still serves. If it stops working, fall back to pasting from a phone or
running yt-dlp on the Mac.

The free endpoint is rate-limited (on 2026-10-07 it refused after ~4 calls,
then again after 2 more an hour later), so fetch a few videos per session.

Usage:  python3 research/get_transcript.py <creator-folder> <url-or-id> [...]
Writes: research/<creator-folder>/<id>-transcript.md
"""
import json
import re
import sys
import urllib.request
from pathlib import Path

ENDPOINT = "https://youtube-transcript.ai/mcp"
# The site rejects Python's default user agent with a 403.
HEADERS = {"Content-Type": "application/json",
           "Accept": "application/json, text/event-stream",
           "User-Agent": "curl/8.5.0"}


def rpc(method, params=None, msg_id=1):
    body = {"jsonrpc": "2.0", "method": method}
    if params is not None:
        body["params"] = params
    if msg_id is not None:
        body["id"] = msg_id
    req = urllib.request.Request(ENDPOINT, json.dumps(body).encode(), HEADERS)
    text = urllib.request.urlopen(req, timeout=180).read().decode()
    if "data:" in text[:30]:  # server-sent-events framing
        text = "".join(l[5:] for l in text.splitlines() if l.startswith("data:"))
    return json.loads(text) if text.strip() else None


def fetch(video):
    rpc("initialize", {"protocolVersion": "2025-06-18", "capabilities": {},
                       "clientInfo": {"name": "charlie-research", "version": "1"}})
    rpc("notifications/initialized", msg_id=None)
    res = rpc("tools/call", {"name": "get_youtube_transcript",
                             "arguments": {"video": video, "lang": "en"}}, msg_id=2)
    if "error" in res or res["result"].get("isError"):
        raise RuntimeError(json.dumps(res)[:300])
    text = "".join(c.get("text", "") for c in res["result"]["content"])
    if "## Transcript" not in text:  # e.g. rate-limit notice after a few calls
        raise RuntimeError(text.strip()[:200])
    return text


def dedupe(words):
    """Auto-captions roll each line 2-3 times; drop the rolled-over repeats.

    Phrases of 3+ words are dropped when doubled. Short phrases (1-2 words) are
    only dropped when tripled, because people really do say "more knowledge,
    more knowledge" but almost never say a phrase three times running.
    """
    out = []
    for w in words:
        out.append(w)
        for n in range(min(30, len(out) // 2), 0, -1):
            copies = 2 if n >= 3 else 3
            if len(out) >= copies * n and all(
                    out[-n:] == out[-(k + 1) * n:-k * n] for k in range(1, copies)):
                del out[-(copies - 1) * n:]
                break
    return out


def clean(raw):
    header, _, body = raw.partition("## Transcript")
    # The service's word count includes the caption repeats we remove.
    header = re.sub(r" · Words: \d+", "", header)
    lines, tail = [], []
    for stamp, text in re.findall(r"^\[(\d+:\d+(?::\d+)?)\]\s*(.*)$", body, re.M):
        words = dedupe(tail + text.split())[len(tail):] if tail else dedupe(text.split())
        tail = words[-30:]
        lines.append((stamp, " ".join(words)))
    return header.strip(), lines


def seconds(stamp):
    secs = 0
    for part in stamp.split(":"):
        secs = secs * 60 + int(part)
    return secs


if __name__ == "__main__":
    folder = Path(__file__).parent / sys.argv[1]
    folder.mkdir(parents=True, exist_ok=True)
    failed = 0
    for arg in sys.argv[2:]:
        vid = re.search(r"(?:v=|youtu\.be/|^)([\w-]{11})", arg).group(1)
        url = f"https://www.youtube.com/watch?v={vid}"
        try:
            raw = fetch(vid)
        except Exception as e:
            print(f"{vid}: UNAVAILABLE ({e})")
            failed += 1
            continue
        (folder / f"{vid}-raw.txt").write_text(raw)  # keep the original for re-cleaning
        header, lines = clean(raw)
        body = [header, "", "Fetched via youtube-transcript.ai (free, no sign-up).",
                "Auto-captions: names may be misheard; repeats removed.", "", "---", ""]
        body += [f"**[{s}]({url}&t={seconds(s)}s)** {t}\n" for s, t in lines]
        out = folder / f"{vid}-transcript.md"
        out.write_text("\n".join(body))
        print(f"{vid}: OK {sum(len(t.split()) for _, t in lines)} words -> {out}")
    # Non-zero exit so chained commands (&&) don't treat a failure as success.
    sys.exit(1 if failed else 0)
