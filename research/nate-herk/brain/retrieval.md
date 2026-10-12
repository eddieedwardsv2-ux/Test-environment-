# Nate knowledge — task-specific retrieval

Up: [index.md](index.md). This is a reading guide, not new teaching. The source rules and concepts remain in their existing files.

Start with the row matching the question. Read the selected complete rule/concept sections; expand when a dependency, disagreement or missing answer warrants it. Rule numbers and concept numbers are different identifiers.

| Question | Rule IDs | Concept IDs |
|---|---|---|
| Wrong answers, false facts, conflicting evidence | 1, 2, 3 | 1 |
| Planning and challenging a proposed solution | 32 | 30 |
| Context size, routing, missing information | 4, 5, 6, 9, 11, 41 | 2, 3, 4, 5, 9, 39 |
| Raw sources, wiki structure, provenance, relationships | 12, 13, 14 | 10, 11, 12, 13 |
| Skills and specialist roles | 15, 20, 21, 22, 23, 34 | 14, 21, 22, 32 |
| Verification and acceptance criteria | 16, 17, 27, 33, 43, 44 | 15, 16, 31, 41, 44 |
| Automation, triggers, fixed code versus agent loops | 10, 35, 42 | 6, 33, 42, 43 |
| Permissions and secrets | 25, 26, 36, 37 | 24, 25, 34, 35 |
| Sessions, handoffs, helper context | 24, 29, 31 | 23, 27, 29, 45 |
| Model choice, effort and measured comparisons | 39, 41, 43 | 37, 39, 40, 41 |
| Audits, freshness and index accuracy | 7, 8, 28, 40 | 7, 8, 38 |
| Beginner complexity and understanding | 6, 18, 30, 42 | 4, 17, 20, 26 |

## Read selected sections

Use heading search to locate sections, then read each complete section up to the next peer heading. Do not dump all of rules.md or concepts.md into the model merely to locate a section.

A local selector can read the file bytes without loading all those bytes into the model. Only its printed sections enter the conversation. Example, for a routing question:

```python
from pathlib import Path
import re

path = Path('research/nate-herk/brain/rules.md')
text = path.read_text()
wanted = {4, 5, 6, 9, 11, 41}
heads = list(re.finditer(r'^\*\*Rule (\d+):', text, re.M))
for i, heading in enumerate(heads):
    if int(heading[1]) in wanted:
        end = heads[i + 1].start() if i + 1 < len(heads) else text.find('\n---', heading.start())
        print(text[heading.start():end if end != -1 else len(text)])
```

Concept sections use `^\*\*(\d+)\.`. Source evidence: consult index.md’s question-to-transcript routes, search the named transcript, and read enough surrounding context to verify the claim. An audit of the entire corpus or first ingestion may require broad reads; ordinary advice does not.

## Maintain this route

When new rules/concepts are added or renumbered, update this table alongside index.md. A row is a starting set, not a hard limit: record why additional sections were needed. Shared links alone do not establish supports/contradicts/depends-on relationships; those need source-grounded descriptions.
