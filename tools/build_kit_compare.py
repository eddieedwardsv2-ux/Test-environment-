"""Builds projects/ai-os-setup-kit/compare/kit-compare.html: our blank template
(templates/standard-ai-os-v1/, full text) side by side with Nate's AIS-OS kit
(github.com/nateherkai/AIS-OS, MIT; file purposes only).
Run: python3 tools/build_kit_compare.py   then republish the page."""
import json, os, html
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/"
T = ROOT + "templates/standard-ai-os-v1/"
OURS = [  # path, plain purpose, filled by
 ("AGENTS.md", "The rulebook and map. Loads with every message: who you're helping, how to work, and where every file lives. It points to things instead of storing them.", "Ready to use; the interview adds your details"),
 ("CLAUDE.md", "One line that pulls in AGENTS.md, so Claude Code and Codex read the same rulebook and the two can never drift apart.", "Ready to use"),
 ("context/about-me.md", "Who you are: role, goals, tools, how you like answers.", "Empty; filled by the grill-me interview"),
 ("context/current-focus.md", "The one place that says what matters now: 90-day priority, next step, parked ideas, and a refresh-by date.", "Empty; filled by the grill-me interview"),
 ("context/README.md", "Explains the context folder.", "Ready to use"),
 ("decisions.md", "A dated log of big decisions and why. Never deleted, only added to.", "Empty; grows as you decide things"),
 ("projects/README.md", "One folder per project or client. Usually the biggest part of the OS.", "Empty; a folder per project"),
 ("research/README.md", "Instructions for a level-2 knowledge base (raw sources plus a derived brain), for later, once you have 30+ notes.", "Empty until needed"),
 (".claude/skills/grill-me/SKILL.md", "Skill: interviews you one question at a time and writes the answers down.", "Ready to use"),
 (".claude/skills/os-audit/SKILL.md", "Skill: checks the OS for broken routes and stale or clashing facts, and changes nothing until you say yes.", "Ready to use"),
 (".gitignore", "Keeps secret keys (.env) out of GitHub.", "Ready to use"),
 ("README.md", "How to start: copy it into a private repo, run grill-me, audit on Fridays, and do the fresh-session test.", "Ready to use"),
]
NATE = [
 ("AGENTS.md + CLAUDE.md", "Two copies of the same rulebook (identity, skills, where things live). You update both together.", "Placeholders; filled by /onboard"),
 ("aios-intake.md", "Your answers to the 7 onboarding questions. Edit it and re-run /onboard any time.", "Filled by /onboard"),
 ("context/", "About you, your business and your priorities.", "Filled by /onboard"),
 ("connections.md", "A register of every tool the OS can reach (email, calendar, files...), with the date each one last worked.", "Grows as you connect tools"),
 ("decisions/log.md", "Dated decisions with why and alternatives.", "Grows as you decide"),
 ("references/3ms-framework.md", "Nate's Mindset, Method, Machine way of thinking about automations.", "Ready to use"),
 ("EXPANSIONS.md", "What to add as you grow, and what not to bother with.", "Ready to use"),
 ("archives/", "Old files get moved here, never deleted.", "Empty"),
 ("skill: /onboard", "The 7-question interview that personalises the whole kit in one go (who you are, a pasted writing sample, priorities, where your work lives).", "Run on day 1"),
 ("skill: /audit", "The scored Four Cs audit (out of 100), saved with history.", "Weekly"),
 ("skill: /grill-me", "The interview skill, for going deeper later.", "Any time"),
 ("skill: /level-up", "Weekly: finds one job to automate and builds it.", "Weekly"),
 ("skill: /link", "Makes a new file or folder findable from the rulebook.", "When you add things"),
 ("skill: /3d-brain", "A 3D globe of your knowledge, like Nate's Herk Brain (runs on a computer).", "Optional"),
 ("scripts/sync-codex-skills.sh", "Copies skills across so Codex sees them too.", "When skills change"),
]
COMPARE = [  # feature, ours, nate
 ("A rulebook that routes to files", "yes", "yes"),
 ("One rulebook for Claude and Codex, no copying", "yes", "no: two copies kept in step by hand"),
 ("Personalises itself with an interview", "partly: grill-me, open-ended", "yes: /onboard, 7 set questions"),
 ("Scored audit, out of 100", "no: os-audit lists problems, no score", "yes: /audit (Four Cs)"),
 ("Finds the next thing to automate", "no", "yes: /level-up"),
 ("Register of connected tools", "no", "yes: connections.md"),
 ("Fresh-session test (proves it knows you)", "yes: a day-1 step in the README", "partly: checked inside /audit, not a day-1 step"),
 ("Guide for a bigger knowledge base later", "yes: research/README.md", "partly: EXPANSIONS.md"),
 ("3D brain view", "no", "yes: /3d-brain (computer only)"),
 ("Size for a beginner to read", "12 files, about 200 lines", "about 15 files plus 6 skills, larger"),
]
def read(p):
    try: return open(T + p, encoding="utf-8").read()
    except FileNotFoundError: return ""
data = {
 "ours": [{"p": p, "why": w, "fill": f, "text": read(p)} for p, w, f in OURS],
 "nate": [{"p": p, "why": w, "fill": f} for p, w, f in NATE],
 "compare": COMPARE,
}
src = ROOT + "projects/ai-os-setup-kit/compare/template.html"
out = ROOT + "projects/ai-os-setup-kit/compare/kit-compare.html"
open(out, "w").write(open(src).read().replace("__DATA__", json.dumps(data, ensure_ascii=False).replace("</", "<\\/")))
print("wrote", out)
