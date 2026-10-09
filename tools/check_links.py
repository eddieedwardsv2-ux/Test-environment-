"""Relation-link scan: every file path a note points to must exist.

Checks markdown links [text](path) and `backticked/paths.ext` in every .md file
(transcripts and raw text skipped). A path counts if it exists relative to the
note's folder, the repo root, or the note's nearest README folder. Placeholders
(<x>, {x}, *, YYYY) are skipped. Run: python3 tools/check_links.py [--quiet]
Exit code 1 when a broken link is found; the audit runs it as a warning list.
"""
import re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKIP_DIRS = {".git", "node_modules", "__pycache__", "templates"}
SKIP_NAME = re.compile(r"(-transcript\.md|-raw\.txt)$")
# History and plans name old or not-yet-built paths on purpose ("current beats history").
HISTORY = re.compile(r"^(audits/|brainstorms/|decisions\.md$|EXPANSIONS\.md$|references/parked-skills/|research/hands/reviews/|\.claude/skills/audit/history\.md$)|(^|/)log\.md$")
# A path just after these words is named as gone or old on purpose.
GONE = re.compile(r"\b(old|was|merged|renamed|retired|doesn't exist|does not exist|would|planned|branch)\b\W{0,3}\S{0,4}$", re.I)
MD_LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
TICK = re.compile(r"`([A-Za-z0-9_.~/-]+/[A-Za-z0-9_.~/-]*)`")
PLACEHOLDER = re.compile(r"[<>{}*]|YYYY|<|\.\.\.|…")
EXT = re.compile(r"\.(md|py|json|html|txt|cjs|js|sh|csv|yml|yaml|toml)$|/$")
# Paths outside this repo that notes legitimately name (Nate's kit, the home folder, other machines).
OUTSIDE = ("~/", "/", "http", "mailto:", "#", "scripts/", "archives/", ".codex/", ".claude-plugin/")
# Named on purpose though not on main: what Nate's onboard wizard creates; WIP kept on a branch.
ALLOW = {("aios-intake.md", "references/voice.md"), ("context/handoff.md", "research/nate-herk/brain/x-themes.md")}


def candidates(note, p):
    p = p.split("#")[0].rstrip(".,;:")
    yield note.parent / p
    yield ROOT / p
    for parent in note.parents:
        if (parent / "README.md").exists() and parent != ROOT:
            yield parent / p
        if parent == ROOT:
            break


FILES = [p.relative_to(ROOT).as_posix() + ("/" if p.is_dir() else "") for p in ROOT.rglob("*") if ".git" not in p.parts]
FILES = [f.rstrip("/") for f in FILES]


def scan():
    broken = []
    for note in sorted(ROOT.rglob("*.md")):
        rel = note.relative_to(ROOT)
        if set(rel.parts) & SKIP_DIRS or SKIP_NAME.search(note.name) or HISTORY.search(rel.as_posix()):
            continue
        text = note.read_text(errors="ignore")
        found = [(m, "link") for m in MD_LINK.findall(text)] + [(m, "path") for m in TICK.findall(text)]
        for p, kind in found:
            if p.startswith(OUTSIDE) or PLACEHOLDER.search(p) or (kind == "path" and not EXT.search(p)):
                continue
            if (rel.as_posix(), p) in ALLOW:
                continue
            spots = [m.start() for m in re.finditer(re.escape(p), text)] or [0]
            if all(GONE.search(text[max(0, s - 40):s].rstrip("`( ")) for s in spots):
                continue
            at = spots[0]
            # A short generic path ("brain/index.md") counts when some real file ends with it.
            if any(c.exists() for c in candidates(note, p)) or any(f.endswith("/" + p.strip("/")) for f in FILES):
                continue
            line = text[:at].count("\n") + 1
            broken.append(f"{rel}:{line}: {p}")
    return broken


def brain_relations(brain=ROOT / "research/nate-herk/brain"):
    """Rule <-> concept links in a creator brain: every target exists, every link is
    echoed on the other side (a replaced rule is exempt), and a concept with no rule
    says so ("no rule yet"). Returns (errors, warnings)."""
    R, C = (brain / "rules.md").read_text(), (brain / "concepts.md").read_text()
    def blocks(text, pat):
        ms = list(re.finditer(pat, text, re.M))
        return {int(m.group(1)): text[m.start():(ms[i + 1].start() if i + 1 < len(ms) else len(text))] for i, m in enumerate(ms)}
    rb, cb = blocks(R, r"^\*\*Rule (\d+):"), blocks(C, r"^\*\*(\d+)\. ")
    nums = lambda s: {int(n) for n in re.findall(r"\d+", s)}
    r2c = {r: set().union(*[nums(g) for g in re.findall(r"[Cc]oncepts? ((?:\d+(?:, | and )?)+)", b)] or [set()]) for r, b in rb.items()}
    c2r = {c: set().union(*[nums(g) for g in re.findall(r"Rules? ((?:\d+(?:, | and |-)?)+)", b.split("**Used by:**")[-1])] or [set()])
           if "**Used by:**" in b else set() for c, b in cb.items()}
    errs, warns = [], []
    for r, cs in r2c.items():
        replaced = "Replaced by Rule" in rb[r]
        for c in cs:
            if c not in cb: errs.append(f"Rule {r} names concept {c}, which doesn't exist")
            elif r not in c2r[c] and not replaced: errs.append(f"Rule {r} links concept {c}, but concept {c}'s 'Used by' doesn't name Rule {r}")
        if not cs and not replaced: warns.append(f"Rule {r} links to no concept")
    for c, rs in c2r.items():
        for r in rs:
            if r not in rb: errs.append(f"concept {c} names Rule {r}, which doesn't exist")
        if not rs and "no rule yet" not in cb[c]: warns.append(f"concept {c} is used by no rule and doesn't say 'no rule yet'")
    return errs, warns


if __name__ == "__main__":
    e, w = brain_relations()
    for x in e: print("ERROR", x)
    for x in w: print("WARN ", x)
    print(f"brain relations: {len(e)} errors, {len(w)} warnings")
    broken = scan()
    if "--quiet" not in sys.argv:
        print("\n".join(broken))
    print(f"links: {len(broken)} broken")
    sys.exit(1 if broken else 0)
