# Three topics to test the draft style guides

Prepared 12 October 2026. Status: TEST BRIEFS PREPARED; audience tests not run.

Guides: [three draft styles](2026-10-12-brand-style-guides.md). These test teaching quality, not the creators' engagement rankings.

## Common test setup

Use each topic in all three styles: Practical teacher, Visual explainer and Evidence-led analyst. This makes nine matched comparisons, not one topic assigned to each style.

For each comparison prepare a 230–270-word article and a 100–130-word spoken script intended for approximately 45–60 seconds. Actual duration must be checked when recorded; word count does not prove runtime. Keep the same factual packet, audience, useful result and requested next action in all three versions. Do not add research, claims or facts to make one version more impressive.

Audience: a UK beginner using AI for real work. Use connected prose and plain UK English. Show the versions as A/B/C with labels hidden first, rotating their order across readers. Reveal the styles after responses. Do not reveal the earlier recommendation before scoring.

All scenarios below are invented teaching fixtures. They are not customer data, market prices or receipts of tests performed on Charlie's system. State this in the outputs. Do not publish, send a quote or change the OS as part of these writing tests.

## Topic 1 — Why AI misses notes you have already saved

**Question:** how can a small index help AI find the right evidence?

**Useful result:** a reader can describe the retrieval route and ask AI to show its source.

### Fixed facts

In this fictional knowledge base, the main router points to `projects/example/index.md`. That index points to two documents:

- `policy-current.md`: updated 10 October; review required before sending a draft.
- `policy-archived.md`: updated 1 September; obsolete and marked archived.

The task asks for the current review requirement. The correct source is `policy-current.md`. Loading the entire knowledge base is unnecessary for this question. An index is a pointer, not proof: its links and the selected document's status must still be checked. The fixture does not establish a token saving or guarantee accuracy.

**Demonstration:** show router → project index → current document → answer with its source. An optional wrong example selects the archived document, then shows what must be corrected. Do not invent that this happened in the real repo.

**Reader questions / answer key:**
1. Which document should supply the answer? `policy-current.md`.
2. Why is the archived answer unacceptable? It is obsolete, despite still existing.
3. What is the next action? Ask AI to show the route/source and check its status.

**Style differences to test:** direct steps; a librarian/map analogy with its limits; a comparison of correct and incorrect retrieval.

## Topic 2 — Turn a customer enquiry into a reviewable quote

**Question:** what should AI calculate, and what should it leave for a person to confirm?

**Useful result:** a reader can recognise a useful quote draft without mistaking it for an approved price.

### Fixed facts

All quantities and prices are invented inputs, not market rates. A fictional decorating enquiry specifies 20 square metres of walls. The supplied demonstration labour rate is £12 per square metre. Supplied materials cost is £45.

- Labour calculation: 20 × £12 = £240.
- Illustrative subtotal: £240 + £45 = £285.
- Ceiling, doors and additional preparation are not in the stated scope.
- Tax treatment, access, final surface condition and start date are unknown.
- The AI may draft the calculation and list unknowns. A person must confirm the scope and approve the quote before it is sent.

**Demonstration:** show the enquiry, extract supplied fields, calculate the subtotal and mark unknowns. Never silently include tax, invent dates or present £285 as an approved final quote.

**Reader questions / answer key:**
1. What is the illustrative subtotal? £285.
2. Name one thing still to confirm. Tax treatment, access, surface condition or start date.
3. Can the draft be sent immediately? No; scope confirmation and approval are required.

**Style differences to test:** practical checklist; enquiry-to-draft visual explanation; assumptions and approval boundaries.

## Topic 3 — An AI says it works: how do you check?

**Question:** what distinguishes a claim of success from a tested result?

**Useful result:** a reader can name a measurable finish line, inspect evidence and spot a failure.

### Fixed facts

This is a simulated test log, not an actual run. A task must retrieve the current policy, cite its file, and leave the response as a draft. Those are three separate acceptance checks.

| Check | Simulated observation | Result |
|---|---|---|
| Current policy retrieved | The response uses the archived September document | Fail |
| Source cited | The response includes the archived file path | Pass for citation presence; it does not fix the wrong source |
| Draft preserved | The response is saved without being sent | Pass |

The task fails overall because one required check fails. The phrase "all done" cannot override the evidence. After repairing the source choice, rerun the failed retrieval check and any other checks affected by the change. Record expected and actual results. A narrow pass does not establish universal reliability.

**Demonstration:** compare the success claim with the log; find the failed requirement; specify the correction and repeat check. No live code execution is required for these writing drafts.

**Reader questions / answer key:**
1. Did the task pass overall? No.
2. Which required behaviour failed? Retrieving the current policy.
3. What should happen next? Correct source selection and rerun affected checks, retaining evidence.

**Style differences to test:** an actionable check sequence; a labelled expected/actual diagram; evidence and limits of the conclusion.

## Evaluation and finish line

For every topic/style, award one point for each of its three comprehension questions answered correctly: 0–3 points. Record a separate "would use again" choice with a reason; preference must not replace accuracy. Also record any confusing term and reading time if available. Do not turn a tiny convenience sample into a statistically proven winner.

Before audience testing, check every output against its packet. Reject factual drift, unlabelled invented evidence, incorrect arithmetic, promises of unmeasured savings or success, and any suggestion to send/publish without the stated approval.

**Prepared when:** all three briefs have fixed inputs, answer keys and a common protocol. This file satisfies preparation only.

**Test complete when:** nine articles and nine scripts exist, each passes the factual check, real beginner responses are recorded, and the conclusion distinguishes comprehension from preference. Each style gets all three topics. No audience results have been collected yet.

Recommended order: Topic 1 first (closest to the existing examples), Topic 2 next (practical business value), Topic 3 last (tests whether clarity survives caveats).

**NOT VERIFIED** — audience comprehension, recording duration and engagement benefit.
