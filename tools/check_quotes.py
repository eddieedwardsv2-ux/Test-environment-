#!/usr/bin/env python3
"""Check every quote in a requirements doc against its transcript timestamp.

Usage: python3 tools/check_quotes.py [doc.md]   (default: system/standard-ai-os-v1.md)

The doc has a code table, `| Ek1 | [title](path/to/...-transcript.md) |`, and
requirement rows, `| R1 | requirement | "quote" | Ek1 12:46; DTC 4:34 | status |`.
A row passes when its quote appears verbatim in the transcript chunk that starts
at one of its timestamps. Prose like "quote" (Ek1 12:46) is checked too.
Exit code 1 if anything fails, so tools/audit.py can count it as an error.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def check(doc_path):
    doc_path = Path(doc_path).resolve()
    doc = doc_path.read_text()
    codes = {c: (doc_path.parent / p).resolve()
             for c, p in re.findall(r"^\| (\w{3}) \| \[[^\]]*\]\(([^)]+-transcript\.md)\) \|", doc, re.M)}
    cache = {}

    def chunks(code):
        if code not in cache:
            text = codes[code].read_text() if code in codes and codes[code].exists() else ""
            cache[code] = {m.group(1): m.group(2) for m in
                           re.finditer(r"\*\*\[([0-9:]+)\]\([^)]*\)\*\*(.*)", text)}
        return cache[code]

    failures, n = [], 0
    items = [(rid, q, src) for rid, q, src in
             re.findall(r'^\| ([A-Z]\d+) \|[^|]*\| "(.*?)" \| ([^|]+) \|', doc, re.M)]
    items += [("prose", q, src) for q, src in re.findall(r'"([^"]{8,})" \((\w{3} \d+:\d+(?::\d+)?)\)', doc)]
    for rid, quote, src in items:
        n += 1
        refs = re.findall(r"(\w{3}) (\d+:\d+(?::\d+)?)", src)
        if not any(quote in chunks(c).get(t, "") for c, t in refs):
            failures.append(f"{doc_path.relative_to(ROOT)} {rid}: quote not found at {src.strip()}: \"{quote[:60]}\"")
    return n, failures


if __name__ == "__main__":
    n, failures = check(sys.argv[1] if len(sys.argv) > 1 else ROOT / "system/standard-ai-os-v1.md")
    print("\n".join(failures) or f"quotes: {n} checked, 0 failed")
    sys.exit(1 if failures else 0)


def check_linked(md_path):
    """Check quotes cited as "quote" — [m:ss](youtube link) in any page.

    The quote must appear in the transcript chunk that starts at that
    timestamp (or the next one, for quotes that cross a chunk break). Parts
    joined by … are checked separately. Returns (count, failures).
    """
    md_path = Path(md_path).resolve()
    text = md_path.read_text()
    failures, n = [], 0
    # Strict citation format only: a quote, then (within a few characters,
    # e.g. " — ") its own link. Prose with several links isn't checked.
    pat = re.compile(r'"([^"\n]{12,})"[ \u2014\-:,.]{0,4}\[(\d+:\d+(?::\d+)?)\]\(https://(?:www\.)?youtube\.com/watch\?v=([\w-]{11})&t=\d+s\)')
    cache = {}
    for quote, ts, vid in pat.findall(text):
        files = list(ROOT.glob(f"research/*/*--{vid}-transcript.md"))
        if not files:
            continue
        if vid not in cache:
            t = files[0].read_text()
            cache[vid] = [(m.group(1), m.group(2)) for m in re.finditer(r"\*\*\[([0-9:]+)\]\([^)]*\)\*\*(.*)", t)]
        chunks = cache[vid]
        idx = next((i for i, (s, _) in enumerate(chunks) if s == ts), None)
        n += 1
        window = " ".join(c for _, c in chunks[idx:idx + 2]) if idx is not None else ""
        parts = [p.strip(" .,") for p in re.split(r"…|\.\.\.", quote) if len(p.strip(" .,")) > 3]
        norm = lambda s: " ".join(s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"').lower().split())
        if idx is None or not all(norm(p) in norm(window) for p in parts):
            failures.append(f"{md_path.relative_to(ROOT)}: quote not found at {vid} {ts}: \"{quote[:60]}\"")
    return n, failures
