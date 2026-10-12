# Official reference collection — continuation

12 October 2026. User requested official Anthropic/OpenAI documentation about current models plus informational and educational content.

## Work completed

Publisher llms.txt indexes and llms-full.txt exports were fetched from Claude Platform, Claude Code, OpenAI API, ChatGPT/Codex product docs, cookbook, learning and developer-blog collections. Canonical page URLs were resolved where export title matching was ambiguous. Model cards were fetched directly from the OpenAI model catalogue. Official engineering and publicly linked academy/training pages were also fetched.

1,959 source URLs, 117 model-reference records and 20 first-pass teaching records are saved. This includes old/restricted model references, short reference/landing pages and two empty training captures, all explicitly classified. The catalogue is not a count of fully reviewed substantive pages. 51 references still do not have their actual external content ingested.

## Review and corrections

An independent reviewer checked the initial 1,902 body hashes/counts, URL/ID uniqueness, SQLite integrity and 22 model extracts, including latest featured Claude/GPT models, multimodal, legacy and restricted examples. Corrections: preserve modality/section labels on pricing tables; expose empty and landing-only captures; include unresolved mapping/reference gaps in coverage. Known index gaps were subsequently fetched by exact URL. Model records now retain source inconsistencies and warn that surrounding pricing conditions must be read. Final structural validation is recorded in result.md. Two descriptive teaching locators are explicitly distinguished from literal section headings.

## Original-text boundary

Working-session evidence lives in the temporary official-docs-work cache on this host: publisher exports, per-page text, `all-sources-private.json` and `runtime-sources.sqlite`. This cache is temporary. No complete original-text mirror was added to the public repo. The durable artifacts are source metadata, factual model extracts and paraphrased teaching. Re-fetch relevant official pages in future sessions; do not imply that the saved public database contains all original text.

## Remaining work

- Resolve empty `/training/hands-on/codex` and `/training/hands-on/work` content through the publisher’s actual learning resources.
- Many API endpoint reference entries in the export contain only headings or very short descriptions; their full parameter schemas have not been recovered. Inspect coverage’s landing_only_pages rather than treating them as fully ingested references.
- Resolve remaining export-mapping history: entries may now be recovered by direct URL, while title-only fragments may be internal headings rather than separate source pages. Do not fabricate source URLs.
- Ingest actual course lessons and educational video contents where public access permits. Learning descriptions and course landing pages are not those lessons.
- Expand research-paper/model-system-card coverage using explicit official inventories. No exhaustive claim about either company’s entire site is supported.
- Read topic-specific sources and derive linked principles, workflows, exceptions and disagreements. The first-pass 20 teaching records do not represent every captured page.
- Make original-text retention a deliberate, permitted design choice if a complete offline corpus is required. Source URLs and hashes alone cannot recreate the old exact wording after a page changes.
- Run task-specific retrieval tests against independently established answers, including version conflicts and API/product differences, before calling this a verified expert brain.

The 90-day priority and previous pending AI Impact slide work remain unchanged. This collection is evidence for future work, not authority to install tools, migrate systems, spend credits or change the user’s model policy.
