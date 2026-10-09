# tools/

Scripts the OS runs (Python unless noted). Nate's kit calls this folder `scripts/`; renaming
it is parked (`context/todo.md`). Every script says what it does and how to run it in its
first lines.

| Script | Job |
|---|---|
| `audit.py` | The structure check on every push and before an agent finishes |
| `fault_drill.py` | Plants faults in a copy of the repo and proves the audit catches each |
| `check_links.py` | File links and the Architect's rule-concept links |
| `route_depth.py` | How many steps from the router to every current note |
| `context_check.py` | What loads into every message, and how big it is |
| `pages_status.py` | Which published pages are behind their source (`--build`, `--mark`) |
| `build_*.py` | Build one page each (Brain and Architect maps, Quartermaster, Reading Room, Nate-first map, Kit Compare) |
| `graph_lib.py` | Shared helper for the map builders |
| `check_quotes.py` | Every brain quote matches its transcript |
| `update_coverage.py` | Transcript coverage ticks in creator video lists |
| `screenshot.py` | Phone and desktop screenshots of a page |
| `run_gate.sh` | The Stop hook: blocks finishing while the audit fails |
| `test_hands_actions.cjs` | Tests for the Quartermaster page's Search / Check / Implement buttons (Node) |
