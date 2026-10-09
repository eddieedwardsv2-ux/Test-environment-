"""Our /doctor for context (Nate, oz2CwrPV2Rg; Rule 41): lists everything that
loads into EVERY message, how big it is, and anything hidden or too long.
Claude Code's own `claude doctor` checks the install; this checks our context.
Run: python3 tools/context_check.py   (after any big change and every model switch)."""
import json, os, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HOME = Path.home()
rows, warns = [], []

def add(label, path, text):
    rows.append((label, str(path).replace(str(HOME), "~"), len(text.splitlines()), len(text)))

def desc_of(p):
    m = re.search(r"^description:\s*(.*)$", p.read_text(errors="ignore"), re.M)
    return m.group(1).strip() if m else ""

# 1. Instruction files: project, its imports, parents, user-wide, local.
for p in [ROOT / "CLAUDE.md", ROOT / "CLAUDE.local.md", HOME / ".claude/CLAUDE.md"]:
    if p.exists():
        t = p.read_text()
        add("instructions", p, t)
        for imp in re.findall(r"^@(\S+)", t, re.M):
            q = (p.parent / imp)
            if q.exists(): add("  imported", q, q.read_text())
for parent in ROOT.parents:
    for name in ("CLAUDE.md", "AGENTS.md"):
        if (parent / name).exists():
            add("parent folder (hidden?)", parent / name, (parent / name).read_text())
            warns.append(f"{parent / name} also loads: is it meant to?")
for d in [ROOT / ".claude/rules", HOME / ".claude/rules"]:
    for p in sorted(d.glob("**/*.md")) if d.exists() else []:
        add("rules file", p, p.read_text())

# 2. Skill and agent descriptions (always loaded; bodies load only when used).
seen = {}
for base, where in [(ROOT / ".claude", "project"), (HOME / ".claude", "user")]:
    for p in sorted(base.glob("skills/*/SKILL.md")) + sorted(base.glob("agents/*.md")):
        d = desc_of(p)
        name = p.parent.name if p.name == "SKILL.md" else p.stem
        add(f"{where} {'skill' if p.name == 'SKILL.md' else 'agent'} description", p, d)
        if len(d) > 300: warns.append(f"{name}: description is {len(d)} chars (aim under 300)")
        if name in seen: warns.append(f"{name} exists in both {seen[name]} and {where}: two may compete")
        seen[name] = where

# 3. Hooks, plugins and MCP servers that add context or run on their own.
for p in [ROOT / ".claude/settings.json", ROOT / ".claude/settings.local.json", HOME / ".claude/settings.json"]:
    if not p.exists(): continue
    s = json.loads(p.read_text())
    for event, items in s.get("hooks", {}).items():
        for it in items:
            for h in it.get("hooks", []):
                rows.append((f"hook ({event})", h.get("command", "")[:60], 0, 0))
    for plug, on in s.get("enabledPlugins", {}).items():
        if on: rows.append(("plugin (adds skills/agents)", plug, 0, 0))
for p in [ROOT / ".mcp.json"]:
    if p.exists():
        for name in json.loads(p.read_text()).get("mcpServers", {}):
            rows.append(("MCP server (adds tools)", name, 0, 0))

# 4. Router size. Nate's ceiling is 200 lines (audit.py errors past it). There is no
#    lower target: "minimal doesn't necessarily mean short" (Nate, oz2CwrPV2Rg 2:03).
#    Cut a line only when it is duplicated, can be looked up, or is stale; never for
#    length alone (Charlie, 2026-10-09). This only reports the size.
router = (ROOT / "AGENTS.md").read_text().splitlines()
print(f"AGENTS.md: {len(router)} lines (ceiling 200)")

total = sum(r[3] for r in rows)
print(f"{'What':34} {'Lines':>5} {'Chars':>6}  Where")
for label, path, lines, chars in rows:
    print(f"{label:34} {lines or '':>5} {chars or '':>6}  {path}")
print(f"\nAlways loaded: about {total:,} characters (~{total // 4:,} tokens).")
print("Warnings:" if warns else "No warnings.")
for w in warns: print(" -", w)
sys.exit(0)
