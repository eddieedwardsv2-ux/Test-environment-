#!/usr/bin/env python3
"""Screenshot a page so an AI can look at it (Nate's visual validation).

Usage: python3 tools/screenshot.py <page.html or URL> [out-folder]

Takes a phone (390px) and a desktop (1280px) screenshot, and reports script
errors, console errors and whether the page shows any text. The automatic part
catches crashes; the screenshots are then opened and looked at, because only
looking finds overlaps, cut-off text and bad spacing.
Needs the free Python library: pip install playwright (the browser is already
in cloud sessions at /opt/pw-browsers; elsewhere run: playwright install chromium).
"""
import glob
import sys
from pathlib import Path

try:
    from playwright.sync_api import sync_playwright
except ImportError:
    sys.exit("Playwright isn't installed in this session (cloud sessions start fresh).\n"
             "Run: pip install playwright   (free; then re-run this command)")

target = sys.argv[1]
out = Path(sys.argv[2] if len(sys.argv) > 2 else "/tmp/screenshots")
out.mkdir(parents=True, exist_ok=True)
url = target if "://" in target else Path(target).resolve().as_uri()
chrome = glob.glob("/opt/pw-browsers/chromium-*/chrome-linux/chrome")

problems = []
with sync_playwright() as p:
    browser = p.chromium.launch(executable_path=chrome[0] if chrome else None)
    for name, width, height in [("phone", 390, 844), ("desktop", 1280, 800)]:
        page = browser.new_page(viewport={"width": width, "height": height})
        page.on("pageerror", lambda e, n=name: problems.append(f"{n}: script error: {e}"))
        page.on("console", lambda m, n=name: m.type == "error" and problems.append(f"{n}: console error: {m.text}"))
        page.goto(url, wait_until="load")
        page.wait_for_timeout(1500)
        if not page.inner_text("body").strip():
            problems.append(f"{name}: page shows no text")
        if page.evaluate("document.documentElement.scrollWidth > window.innerWidth"):
            problems.append(f"{name}: page scrolls sideways (wider than the screen)")
        shot = out / f"{Path(target).stem}-{name}.png"
        page.screenshot(path=str(shot), full_page=True)
        print("saved", shot)
    browser.close()

print("\n".join(problems) or "no automatic problems found; now look at the screenshots")
sys.exit(1 if problems else 0)
