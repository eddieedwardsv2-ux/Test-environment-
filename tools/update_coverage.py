"""Tick transcribed videos and update coverage counts in each creator's notes.

For every research/<creator>/*--<id>-transcript.md, marks that video's row
"✅ [transcript](<file>)" in README.md (and videos.md if present),
then sets "**N transcribed**" and the research/README.md index count.
Run after transcripts land: `python3 tools/update_coverage.py` (the GitHub
transcripts workflow runs it too). Safe to run any time.
"""
import re
import sys
from pathlib import Path

RESEARCH = Path(__file__).resolve().parent.parent / "research"
sys.path.insert(0, str(RESEARCH))
from get_transcript import video_id  # noqa: E402
index = RESEARCH / "README.md"
index_text = index.read_text()

for folder in sorted(p for p in RESEARCH.iterdir() if p.is_dir() and not p.name.startswith(("_", "."))):
    files = {video_id(f): f.name for f in folder.glob("*-transcript.md") if video_id(f)}
    ids = sorted(files)
    for notes in (folder / "README.md", folder / "videos.md"):
        if not notes.exists():
            continue
        text = notes.read_text()
        for vid in ids:
            text = re.sub(r"(\(https://www\.youtube\.com/watch\?v=" + re.escape(vid) + r"\)[^\n]*\| )– \|",
                          r"\g<1>✅ [transcript](" + files[vid] + ") |", text)
            # Re-point ticks made before a file was renamed.
            text = re.sub(r"\]\((?:[\w-]*--)?" + re.escape(vid) + r"-transcript\.md\)", "](" + files[vid] + ")", text)
        text = re.sub(r"\*\*\d+ transcribed\*\*", f"**{len(ids)} transcribed**", text)
        notes.write_text(text)
    # Index row: "| [Name](<folder>/README.md) | topic | videos | N... |"
    index_text = re.sub(r"(\]\(" + re.escape(folder.name) + r"/README\.md\) \|[^|\n]*\|[^|\n]*\| )\d+[^|\n]*\|",
                        rf"\g<1>{len(ids)} |", index_text)
    print(f"{folder.name}: {len(ids)} transcribed")
index.write_text(index_text)
