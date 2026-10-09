"""Which published pages are behind their source? (Charlie, 2026-10-09)

A page's age doesn't matter; a page is stale only when its source file changed after it
was last published. system/published.json holds each source's fingerprint at publish time.
  python3 tools/pages_status.py            list pages whose source changed since publishing
  python3 tools/pages_status.py --build    run every page builder first, then list
  python3 tools/pages_status.py --mark F   record F as just published (run after each publish)
The audit warns on every stale page; the session-handoff skill republishes them.
"""
import hashlib, json, sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REC = ROOT / "system/published.json"
fp = lambda p: hashlib.sha256((ROOT / p).read_bytes()).hexdigest()[:16]


def stale():
    rec = json.loads(REC.read_text())
    return [(src, r["page"] + ("" if (ROOT / src).exists() else " (source file missing)")) for src, r in rec.items()
            if not (ROOT / src).exists() or fp(src) != r["sha256"]]


BUILDERS = ["build_brain_map", "build_hands", "build_reader", "build_merge_map", "build_kit_compare"]

if __name__ == "__main__":
    if "--build" in sys.argv:
        import subprocess
        for b in BUILDERS:
            subprocess.run([sys.executable, str(ROOT / "tools" / f"{b}.py")], cwd=ROOT, capture_output=True, check=True)
    if "--mark" in sys.argv:
        rec = json.loads(REC.read_text())
        srcs = [a for a in sys.argv[sys.argv.index("--mark") + 1:] if not a.startswith("--")]
        if not srcs: sys.exit("--mark needs the source file(s) you just published")
        unknown = [s for s in srcs if s not in rec]
        if unknown: sys.exit(f"not in system/published.json (add its row to system/pages.md and here first): {unknown}")
        for src in srcs:
            rec[src]["sha256"], rec[src]["published"] = fp(src), date.today().isoformat()
        REC.write_text(json.dumps(rec, indent=1) + "\n")
    for src, page in stale():
        print(f"STALE {page}: {src} " + ("is missing" if page.endswith("missing)") else "changed since it was last published"))
    print(f"pages: {len(stale())} behind their source")
