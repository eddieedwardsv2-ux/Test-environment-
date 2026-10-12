# Research Experiment 4 — Knowledge Brain Accuracy
Date: 2026-10-12. Scope: read-only source retrieval and targeted evidence checks. No architecture changes.

## Question
Can the currently stored research support twenty specific questions with recoverable evidence, while avoiding whole-corpus reading?

## Success criteria (predefined)
- >= 18/20 (90%) questions have inspectable evidence in task-selected records.
- 20/20 questions have an explicit source path and distinguish creator claims from established facts.
- No invented source links; failures retained and backtracked.
- Do not claim live semantic search or autonomous agent correctness without testing them.
- Do not change existing architecture, AGENTS.md or research originals.

## Retrieval run and results
Used connected GitHub `fetch_file`, targeting selected small notes from `research/ai-impact/videos/`, `research/nate-herk/lesson-smallest-context.md`, and Nate README, guided by their indexes. Read five distinct content files plus indexes/router rather than loading the creator corpora.
**First-pass literal evidence matching: 19/20 (95%).**
**Backtracked lookup: 20/20 (100% evidence locatable across indexed sources)** after retrieving `research/nate-herk/README.md`.
Failure #15: question 'What happens when an AI misses something?'; expected phrase 'fix the routing' was absent from selected `lesson-smallest-context.md` (it refers to backtracking and routing differently), and present in Nate `README.md` section 'Key lessons — AI OS video'. This was a **literal-string/source-selection miss**, not proof the answer was absent from the corpus.

## Full question/test cases
Each entry is ID | expected source | question | evidence anchor | first-pass result. All facts are summary-note facts; speaker claims are attributed.
1 | ai-impact/videos/z02Y-1OvWSM.md | How are knowledge links labelled? | Describe relationships; supports/contradicts/depends on | PASS
2 | same | What is suggested note size? | Keep notes small; 50–300 lines | PASS
3 | same | Read full notes first? | Retrieve progressively; summary first | PASS
4 | ai-impact/videos/8mL3D6ku8MQ.md | Where are live numerical datasets stored? | Database references; databases | PASS
5 | same | Who approves early business decisions? | Human bridge first | PASS
6 | same | How represent secrets? | Secret aliases and vault | PASS
7 | ai-impact/videos/yP4p3reZUcU.md | What comes before changes? | Write a wager; expected impact | PASS
8 | same | Promote all new inputs? | Capture then filter; archive noise | PASS
9 | same | Can a tidy graph compensate for weak content? | Quality of inputs; weak content | PASS
10 | ai-impact/videos/jWYzTLUEk7g.md | Did local coding match Claude? | Coding trial limitation; ineffectively | PASS
11 | same | Does local service run when PC stops? | Keep local service running; interruption | PASS
12 | nate-herk/lesson-smallest-context.md | Which instructions always load? | Keep only what model cannot infer; who you are | PASS
13 | same | When load video-editing procedure? | Load only on relevant task | PASS
14 | same | Was router trimmed? | 93 to 76 lines historical measurement | PASS
15 | nate-herk/lesson-smallest-context.md FIRST, nate-herk/README.md RECOVERY | What happens on AI miss? | Backtrack then fix routing | FIRST FAIL, RECOVERED
16 | ai-impact/videos/z02Y-1OvWSM.md | Is 600 vs 9000 independently proven? | Not reproducibly benchmarked | PASS
17 | ai-impact/videos/jWYzTLUEk7g.md | Is Gemma model equivalence independently proven? | No | PASS
18 | ai-impact/videos/8mL3D6ku8MQ.md | One context/execution engine? | Separate data from runtime | PASS
19 | ai-impact/videos/yP4p3reZUcU.md | Every event deeply reasoned? | Deterministic handling route | PASS
20 | ai-impact/videos/z02Y-1OvWSM.md | Proposed knowledge note types? | Decisions/questions/facts | PASS

## Interpretation
This is a **guided known-document literal-evidence availability check**, NOT a blinded question-only retrieval test: paths and answer anchors were supplied by the test author, and test cases were developed from accessible notes. The result cannot be called 95%/100% knowledge brain semantic retrieval accuracy, answer accuracy, or model generalisation. Questions are not independently sampled, and cited AI Impact visual slides have not been captured. AI Impact notes contain creator claims, not validated performance evidence.

## What was NOT run
- `knowledge.sqlite` ranking or query runtime, or cross-creator semantic/keyword search;
- blind questions with no reference paths;
- LLM generated answers independently graded for truthfulness and citation precision;
- independent adversarial contradiction sets;
- repeat tests on fresh Claude and Codex sessions;
- context token cost benchmark / model comparison.
These remain **NOT VERIFIED**.

## Next measurable experiment
Use a held-out set of 20 questions written without source paths, balanced across AI Impact, Nate and Next New Thing and including five contradiction/outdated-claim questions. Run the actual cross-source search method in fresh sessions, log first 5 returned records, and compare against separately authored gold citations. Target recall >= 90%, correct attribution and support 20/20, no unsupported assertions, measure actual tokens and latency. Revisit misses by adjusting source pointers only if they are genuine, without redesign.

## Verdict
**VERIFIED: 19/20 first-pass expected literal anchors and 20/20 after source-index backtrack; reproducible source paths enumerated.**
**NOT VERIFIED: independent real knowledge-brain answer accuracy, cross-source ranking, contradiction handling, context efficiency or runtime robustness.**
