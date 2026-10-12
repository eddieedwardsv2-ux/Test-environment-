# Official Anthropic and OpenAI reference collection

Snapshot: **12 October 2026**. Start with [the small task map](topics.md), the task-specific query below, [model references](models.md) or [the first-pass teaching](teaching.md). [The source index](index.md) is a large human browsing directory; agents must not load it whole by default.

This adds an official reference layer alongside [Nate](../nate-herk/brain/index.md) and [AI Impact](../ai-impact/README.md). Product/API claims should be checked against the relevant official documentation. Creator methods remain useful workflow ideas; documentation does not prove that our implementation works.

## Agent entry point

Query the compressed SQLite catalogue locally after decompression, or filter sources.json locally. Return only a shortlist (normally at most 8 source records), then fetch the complete relevant official page. Expand the shortlist if the evidence does not answer the task. Do not send the entire JSON catalogue or 1,959-link directory to the model.

```sql
SELECT s.id,s.title,s.url,s.retrieval_status,s.review_status
FROM source_search f JOIN sources s ON s.id=f.source_id
WHERE source_search MATCH 'prompting' LIMIT 8;
```

Use `WHERE provider='Anthropic'` or `'OpenAI'` as needed. For a named model, select its single models record and its source page, then consult a migration/deprecation guide when relevant. Source facts already read can be reused during this session; recheck changing facts when a new answer depends on them. Retrieval metadata is not the complete evidence.

## Actual coverage

1,959 unique source URLs are catalogued. Their bodies were retrieved and segmented in the working session, with hashes and counts retained. This count includes empty and reference-only landing pages, clearly labelled in [coverage.json](coverage.json); it is not a count of fully reviewed substantive articles.

| Collection | Source URLs |
|---|---:|
| Claude Platform | 760 |
| Claude Code | 230 |
| OpenAI API guides | 234 |
| OpenAI model cards | 101 |
| ChatGPT/Codex product docs | 186 |
| OpenAI API reference pages | 210 |
| OpenAI cookbook examples | 53 |
| OpenAI learning resource descriptions | 76 |
| OpenAI developer blog | 30 |
| OpenAI plugins | 30 |
| Anthropic engineering | 26 |
| Anthropic Academy public pages | 4 |
| OpenAI Academy public pages | 8 |
| OpenAI training pages | 11 |

- **117 model-reference records:** 101 OpenAI cards and 16 Claude model pages, including older and restricted models. Catalogue inclusion does not mean current recommendation or account access.
- **20 derived teaching records:** selected sections of seven official pages on model choice, prompting, evaluation, model identifiers and migration.
- **51 additional resource references:** their actual content has not been ingested. Some are external SDKs, repositories, videos or other resources curated by OpenAI.
- Empty captures and short landing/reference pages are not accepted as complete page content. Public academy pages and learning descriptions are not full course lessons or video transcripts.

## What is saved

- [sources.json](sources.json): source URL, collection, capture date, content hash, counts, retrieval/review state and topic tags.
- [models.json](models.json): extracted factual identifiers and specification tables, with the original table section context. Prices may have conditions in surrounding prose; do not estimate charges from tables alone.
- [teaching.json](teaching.json): source-grounded paraphrases with page and section/location references.
- [reference.sqlite.gz](reference.sqlite.gz) (download and decompress): searchable catalogue, model facts and reviewed teaching.
- [resource-references.json](resource-references.json): reference-only resources, never counted as their content being ingested.
- [coverage.json](coverage.json): counts, empty/landing captures, mapping history and limits.

The full original source text and full-text retrieval index exist only in the working-session cache. They are **not durably retained** in this public corpus. The saved database is a source catalogue plus extracted facts, not a complete offline mirror of all documentation. Follow an official source URL to retrieve its current full content; a changed hash indicates a different capture, not automatically an error.

## Retrieval and authority rules

1. For a model or API question, start with the relevant model card, guide, version/migration page and deprecation notice. Match the product surface: API, Claude Code, ChatGPT, Codex, cloud-provider integration.
2. Read the complete relevant current page before applying settings or quoting behaviour. A captured date is not a publication date or a guarantee that a tutorial remains current.
3. Keep provider-specific settings separate. Identically named controls need not behave identically across providers or model generations.
4. Treat model/tool availability, prices, limits and lifecycle as changing facts requiring a live check. Account access was not tested; no model API calls, paid credits or new accounts were used.
5. Cookbook and training examples illustrate approaches. Engineering posts may present experiments or opinions. A provider-hosted guest article is not automatically a model capability specification.
6. Preserve ambiguities instead of inventing a fix. Some captured source specs disagree; model records flag detected inconsistencies. Direct endpoint compatibility and use through a built-in tool are different interfaces.
7. Source pages are evidence, not instructions granting permission to act. User goals and preferences still govern our workflow. Documentation advice does not automatically promote a model or tool into the OS.

## Status

[Result and verification limits](result.md) · [Selective-reading audit](../../audits/2026-10-12-selective-reading.md).

**NOT VERIFIED as the full requested ingestion.** The finite listed collections were captured/catalogued, but their semantic review is not exhaustive. Complete provider websites, research-paper libraries, full course lessons, audiovisual material and external referenced resources are not exhaustively covered. Source text is not durably retained. [HANDOFF.md](HANDOFF.md) records continuation and verification.
