# TRADEFLOW quote demo

**Goal:** show a painter and decorator going from a customer's enquiry to an
approved, itemised quote and a follow-up message, with the AI only reading the
enquiry and fixed, tested code doing all the money.

**Done when:** one sample enquiry runs the whole way (missing details found,
itemised price checked to the penny, owner edits and approves, follow-up
drafted) on phone and desktop, then a new enquiry not used in building it
works too. Real pricing, real customers and sending are out of scope.

## The page
**TRADEFLOW Quote Lab** (Claude artifact, private):
https://claude.ai/artifact/UbhWogxi5n8EJXzTA8oUNE
Source: `quote-lab/quote-lab.html`. Built 15 Oct 2026 on Charlie's choice to
build it in Claude instead of extending the ChatGPT-hosted Quote Lab, which is
left as it was.

How it works (rules from `research/quote-experiment-3-2026-10-12.md`):
1. **Enquiry.** "Read it with Claude" fills the job details from the message;
   anything not clearly stated stays blank. The sample job opens pre-read.
2. **Job details.** Rooms in metres, what to paint, doors, windows, condition,
   access, furniture and who supplies paint. Unknowns show amber.
3. **What we still need.** Any unknown blocks the price and drafts a message
   asking the customer. "Use the sample customer's reply" fills the sample's
   answers.
4. **The quote.** Integer-pence maths, half-up rounding, every line shows what
   it was worked out from. Rates are editable **sample** rates. VAT only when
   ticked. Owner-only approval. Any change to the job or rates after approval
   voids it (old version kept); re-approving makes the next version.
5. **Follow-up.** Drafted from the latest approved version only. Never sent.

Quotes are saved in the page's `quotes` database (one document per quote).

## Tests
```
cd projects/tradeflow/tests
python3 expected.py      # independent Decimal pricing -> cases.json
node test_pricing.mjs    # the page's own pricing code against it
node test_approval.mjs   # approval, revision and version rules
```
Results 15 Oct: pricing 79/79 (20 priced jobs to the penny, 12 missing/bad-input
cases, rounding); approval 10/10. Sample job total after the customer's reply:
£1,504.61 (sample rates, no VAT). Receipt: `evidence-2026-10-15.md`.

## Not verified yet
Sample job verified live on Charlie's device 15 Oct (see the receipt). Still open:
Claude's reading of a new enquiry, the unseen-enquiry test, keyboard use, desktop.
Any real business pricing, VAT position, privacy or sending.
