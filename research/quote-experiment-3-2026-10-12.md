# Quote Research Experiment 3 — 2026-10-12

Status: **RESEARCH VERIFIED / SYNTHETIC ARITHMETIC 8/8 / LIVE WORKFLOW NOT VERIFIED**

## Scope
Cross-source selected evidence; no system redesign. AI Impact:
- https://www.youtube.com/watch?v=uVVMg9l20TI&t=138s operations interview and workflow selection; creator admits untested automations at 5:23.
- https://www.youtube.com/watch?v=8mL3D6ku8MQ&t=244s human bridge and https://www.youtube.com/watch?v=8mL3D6ku8MQ&t=831s numeric data separate from prose.
- https://www.youtube.com/watch?v=yP4p3reZUcU&t=725s hypothesis and review horizon.
Nate:
- https://www.youtube.com/watch?v=Ek1NBfnnTH0 context router vs situational knowledge.
- https://www.youtube.com/watch?v=iTY8Q449YNQ&t=583s screenshot, errors, revision checks.
The Next New Thing:
- https://www.youtube.com/watch?v=uWnQLASl95U&t=129s agent drafts based on past business performance, but demo-store evidence not real customer uplift; marketing not quoting.
- https://www.youtube.com/watch?v=CQhWqUOouYM&t=123s workflow orchestration can operate with subscriptions; this does not prove cost-free inference.

Official tax evidence:
- https://www.gov.uk/guidance/buildings-and-construction-vat-notice-708 (updated Aug 2026): ordinary landscaping standard-rated; exceptions for certain construction situations; verify registration and supply rather than auto applying VAT.
- https://www.gov.uk/vat-builders/houses-flats
Additional operational practice, not independent evidence of uplift:
- https://www.getservicebox.com/features/quotes-invoicing-software
- https://opsmadesimple.net/guides/how-to-choose-quoting-software-for-service-businesses/

## Findings
1. AI interprets enquiries and drafts questions/wording; deterministic code calculates money using approved rates.
2. Missing measurements/unknown access must block a final priced quote.
3. Owner signs off on versioned scope, exclusions, rates and sending; follow-ups remain drafts.
4. Keep context knowledge separate from customer records and actual numerical pricing.
5. Claims of faster quoting or higher acceptance are hypotheses, not observed customer outcomes.

## Synthetic fixture (illustrative only, NOT a commercial tariff)
Clearance £35 per m²; turf installation £18.50 per m²; waste disposal £85 per load. 40 m² and two loads: (40 × 35) + (40 × 18.50) + (2 × 85) = £2,310.00 before VAT. If VAT is explicitly set to 20%: £2,772.00.

Local Python decimal arithmetic fixture on 2026-10-12: **8/8 checks passed**:
- missing waste_loads flags NEEDS_INFO
- correct £2,310 subtotal
- explicit 20% VAT yields £2,772
- automatic output stays DRAFT
- negative quantity rejected
- zero quantity safe
- text quantity rejected
- manual approved flag sets APPROVED (illustrative flag only; not a verified approval trail)

These tests do NOT establish any live website, model extraction, persistence, authentication, owner identity, true approval, quote revision or external sending control. The fixture does not implement production approval checks; approval flag is a unit-test input.

## Next test plan and acceptance thresholds
Reuse existing private TRADEFLOW Quote Lab, do not create another site.
1. Intake: 10 cases, including 4 incomplete/ambiguous -> 10/10 correct completeness classification and 0 invented fields.
2. Pricing: 20 independently computed cases, unusual decimal quantities, invalid inputs, discounts, VAT configurations -> 20/20 exact pence with half-up policy documented and explicit business-approved rates.
3. Revision/approval: 5 cases -> 5/5 revisions recalculate, preserve prior version and approve only by owner; 0 sends before approval.
4. Follow-up: 5 cases -> 5/5 drafts refer to correct version and never dispatch automatically.
5. UI: phone and desktop real-browser checks, keyboard navigation, invalid-input handling and persistence after reload.
6. Practical benefit: time 10 real or representative cases with existing vs improved workflow; report median quote preparation time and error/rework rate; target >=25% median time reduction with no increase in critical errors. Target is an experiment goal, not a result.
7. Public/production protection: privacy, authentication, retention, secrets, VAT status and licence audit before any business deployment.

## Reconciliation
AI Impact suggests a broader self-hosted automation layer, Nate argues for selective context and testing, The Next New Thing showcases integrations. None shows controlled independent evidence that an AI quoting agent raises revenue. The smallest useful demo is deterministic pricing and human approval, with AI confined to interpretation and drafts.

Result: **NOT VERIFIED** as a production or deployed quoting workflow. Research comparison and synthetic test evidence only.