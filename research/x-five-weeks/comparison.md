# What the combined research teaches us

The useful shift is from collecting instructions to building a system that can demonstrate its work. Nate contributes context and routing; AI Impact connects knowledge to business operations; poteto supplies concrete engineering loops; Boris describes delegation and verification; Karpathy addresses human understanding and uneven capability. These are complementary mechanisms, not proof that one complete framework should replace ours.

## 1. Put recurring mistakes into the environment

Poteto's [12 October post](https://x.com/poteto/status/2109699980248408574) treats existing code and constraints as memory. Her [verification post](https://x.com/poteto/status/2109436202554372476) asks agents to exercise the real surface and return reviewable evidence.

**Relation:** Nate already teaches a run-and-check loop ([bvGptCLDhyo, 7:35](https://www.youtube.com/watch?v=bvGptCLDhyo&t=455s)). Our fault drill checks planted structural failures; it does not prove an actual customer journey. Add a regression check for each demonstrated recurring error, instead of endlessly expanding global instructions. Existing code also teaches bad habits, so copying a pattern is not evidence that it is sound.

**TRADEFLOW inference:** a quote total should come from a tested calculation; editing an approved quote should invalidate the old approval. These are project behaviours to prove, not additions to the main router.

## 2. A short prompt still needs a strong brief

[Boris, 6 October](https://x.com/bcherny/status/2107565388250874193), emphasises outcome, effort and verification. Poteto's attached [pstack Pt. 2 article](https://x.com/i/article/2094940651607715840) asks agents to restate intent and investigate mechanisms and reasons before acting.

**Relation:** Nate's [newer prompting transcript, 1:32](https://www.youtube.com/watch?v=oz2CwrPV2Rg&t=92s) similarly gives outcome and constraints. This supports selective context loading. It does not justify deleting business facts, source provenance or the user's decisions. One entry point can route to task-specific instructions without loading the whole brain.

**Inference:** a small prompt works when the runtime already has the right tools, relevant context and a working way to verify. Copying a short prompt without those conditions can produce a weak result.

## 3. Resolve uncertainty with observable prototypes

The pstack article contrasts abstract design debate with interfaces and runnable alternatives. Its durable lesson is to test uncertain assumptions before committing to implementation, then plan the execution around proof.

**Relation:** Nate's [concepts 30 and 45](../nate-herk/brain/concepts.md) favour challenging plans; his later sources also describe direct building and iteration. Keep the useful challenge, but target something testable. AI Impact's [reviewed workflow record](../ai-impact/videos/_X5jSMka5e4.md) also establishes quality before repetition.

**Decision:** MODIFY. Use a short intent statement and constraints, prototype the genuinely uncertain parts, and keep enough documentation to continue safely. Do not copy poteto's preference for deleting completed plans: Charlie explicitly wants decisions and project history preserved.

## 4. Measure the result the user experiences

Boris shared the [performance sprint article](https://claude.dev/blog/how-we-made-claude-ai-faster/). Its strongest mechanism is a chain from a real journey to a benchmark, measured improvement and regression protection. The team checked that proxy counts correlated with felt latency.

**Relation:** AI Impact's [company-brain record, 2:39](../ai-impact/videos/8mL3D6ku8MQ.md) describes the OODA cycle. Measurements supply the Observe step; comparison interprets them; a scoped change implements the decision; a fresh measurement closes the loop.

**TRADEFLOW inference:** measure missing-detail detection, arithmetic errors, time to an editable draft and whether the owner understands the approval state. PR counts and generated files are secondary evidence. Poteto's own volume argument combines volume with impact; copying the headline would lose that qualification.

## 5. Evaluate the evaluator

The [eval-design article](https://claude.dev/blog/automating-eval-design-and-hillclimbing/) recommends realistic tasks, consistent graders, unseen cases and changes large enough to distinguish from noise. Treat infrastructure failures separately.

**Relation:** Nate's [Rule 43](../nate-herk/brain/rules.md) already covers model testing. This adds clearer checks for a test that rewards superficial fixes. Our 25 planted faults are useful but known; add a fresh final sample that the implementer has not tuned against. Keep high quality as the condition for a cheaper model or effort setting. No new model promotion was measured in this research.

**Caution:** repeatedly choosing variants using a held-out set can turn that set into another tuning set. Reserve a fresh acceptance set for the final claim.

## 6. Verification claims have a scope

[Boris's clarification](https://x.com/bcherny/status/2102898067133595992) explains that formal models exposed suspected bugs in selected tricky code, then those bugs were reproduced and fixed. It was not a proof of the whole SDK.

**Relation:** this sharpens our VERIFIED / NOT VERIFIED reporting. Separate structural checks, real behaviour, persistent side effects and unseen cases. Lean/TLA+ may help a genuinely complex state machine, but the quote demo's first need is observable approval/revision behaviour and calculation checks.

**Decision:** KEEP scoped evidence; REJECT interpreting a test pass or impressive demo as proof of every system property. No Guardian role or mandatory separate-reviewer gate is recreated.

## 7. Native projects can supply orchestration

[Cursor's Projects article](https://cursor.com/blog/projects) describes a coordinator, shared context, worker environments and ongoing signals. [Claude's Projects article](https://claude.com/resources/articles/projects-redesigned) describes related coordination with independent branches and possible merge conflicts.

**Relation:** AI Impact [separates portable context from execution](../ai-impact/videos/8mL3D6ku8MQ.md). Keep GitHub knowledge and decisions portable while using available native runtimes for execution. This research provides no evidence that Hermes, Paperclip or another framework is necessary for our task.

**Decision:** VERIFY FURTHER account access, restoration, cost and real phone control. Do not confuse a product announcement with a tested workflow on Charlie's account.

## 8. Make understanding part of the deliverable

[Karpathy's 2 October post](https://x.com/karpathy/status/2105819303471976479) proposes clearer constrained language and richer visual explanations. His [11 October post](https://x.com/karpathy/status/2109361546505966046) argues that people's experience differs by task, access and ambition; its population estimates are explicitly informal.

**Relation:** Nate's creator-brain lesson includes explanation and source links; our nine style-guide drafts have not yet passed a real beginner comprehension test. A beautiful visual is not a substitute for that test.

**TRADEFLOW inference:** show the calculation and state change, then ask a beginner to explain the price, what is missing and what happens next. For Charlie's teaching work, a small interactive explanation can make a complex lesson inspectable on a phone.

## What should change first

Apply these lessons to the existing quote demo: one labelled sample enquiry, explicit missing fields, tested itemised arithmetic, an editable draft, an approval state that responds correctly to revisions, and a reviewable proof of the journey. Then test a new enquiry not used during development. Keep the existing private access and owner approval before customer delivery.

This is a recommendation derived from the combined sources. Research alone does not verify that the demo implements it. The system's architecture and removed tool policies were not changed.

Status: **comparison complete for selected reviewed evidence; full corpus and runtime adoption NOT VERIFIED**.
