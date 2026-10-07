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
