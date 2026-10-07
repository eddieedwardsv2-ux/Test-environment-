"""Fetch transcripts for videos waiting in research/transcript-queue.txt.

Run hourly by .github/workflows/transcripts.yml on GitHub's computers, whose
IP gets its own allowance from the free transcript service. Each line of the
queue is "<creator-folder> <video-id-or-url>"; lines starting with # are notes.
Fetched videos are removed from the queue; failures stay for the next run.

Usage: python3 research/process_queue.py [max-videos-per-run] [shard/shards]
       python3 research/process_queue.py --cleanup
With shard/shards (e.g. 1/3), only every 3rd queue entry is fetched and the
queue file is left alone, so several GitHub jobs can run at once; a final
--cleanup run removes entries whose transcript now exists.
"""
import subprocess
import sys
from pathlib import Path

from get_transcript import find_transcript

QUEUE = Path(__file__).parent / "transcript-queue.txt"
lines = QUEUE.read_text().splitlines() if QUEUE.exists() else []
entries = lambda: [l for l in lines if len(l.split()) == 2 and not l.startswith("#")]

if sys.argv[1:] == ["--cleanup"]:
    def fetched(line):
        creator, video = line.split()
        vid = video[-11:]
        f = find_transcript(Path(__file__).parent / creator, vid)
        return f is not None and "truncated at" not in f.read_text()[-2000:]
    keep = [l for l in lines if l not in entries() or not fetched(l)]
    QUEUE.write_text("\n".join(keep) + "\n")
    print(f"cleanup: {len(lines) - len(keep)} removed, {sum(1 for l in keep if l in entries())} still queued")
    sys.exit(0)

limit = int(sys.argv[1]) if len(sys.argv) > 1 else 3
if len(sys.argv) > 2:  # shard mode: fetch only this job's share, don't touch the queue file
    i, n = map(int, sys.argv[2].split("/"))
    for line in entries()[i - 1::n][:limit]:
        creator, video = line.split()
        subprocess.run([sys.executable, str(Path(__file__).parent / "get_transcript.py"), creator, video])
    sys.exit(0)

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
