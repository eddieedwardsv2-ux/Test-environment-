"""Fetch transcripts for videos waiting in research/transcript-queue.txt.

Run hourly by .github/workflows/transcripts.yml on GitHub's computers, whose
IP gets its own allowance from the free transcript service. Each line of the
queue is "<creator-folder> <video-id-or-url>"; lines starting with # are notes.
Fetched videos are removed from the queue; failures stay for the next run.

Usage: python3 research/process_queue.py [max-videos-per-run]
"""
import subprocess
import sys
from pathlib import Path

QUEUE = Path(__file__).parent / "transcript-queue.txt"
limit = int(sys.argv[1]) if len(sys.argv) > 1 else 3

lines = QUEUE.read_text().splitlines() if QUEUE.exists() else []
keep, done = [], 0
for line in lines:
    parts = line.split()
    if len(parts) != 2 or line.startswith("#") or done >= limit:
        keep.append(line)
        continue
    creator, video = parts
    ok = subprocess.run([sys.executable, str(Path(__file__).parent / "get_transcript.py"),
                         creator, video]).returncode == 0
    if ok:
        done += 1
    else:
        keep.append(line)
        break  # rate-limited: stop and leave the rest for the next hourly run
QUEUE.write_text("\n".join(keep) + "\n")
print(f"fetched {done}; {sum(1 for l in keep if l.split() and not l.startswith('#'))} still queued")
