# Five-week X research: poteto, Karpathy and Boris Cherny

Window: **7 September 2026 00:00–12 October 2026 20:51 UK**.

[Comparison and lessons](comparison.md) · [Article notes and access status](articles.json) · [Source inventory in Eddie-Ed](https://github.com/eddieedwardsv2-ux/eddie-ed/tree/main/social/x/2026-09-07--2026-10-12).

| Timeline | Entries | Own posts | Reposts | Pages |
|---|---:|---:|---:|---:|
| @poteto (Lauren Tan; formerly @potetotes) | 368 | 168 | 200 | 20 |
| @karpathy | 4 | 3 | 1 | 2 |
| @bcherny | 73 | 34 | 39 | 5 |
| Total timeline memberships | 445 | 205 | 240 | 27 |

Deduplication and individual reply supplements produce **448 unique source records**. Reposts preserve their original author. Five attached X article bodies were retrieved; the effort article also has a publisher mirror. Twenty associated/supporting reading records have individual access/review labels in articles.json. Source bodies were examined transiently; durable ingestion retains short excerpts, metadata, hashes and analytical summaries, not full-text republication.

## Coverage limits

The free FxTwitter timeline API was paginated until every returned post on a later page predated the window. This proves the traversal, not that X supplied every post. Replies can be omitted; separately found replies supplement the timelines. Reposts are filtered by original creation date, so older material reshared in-window can be missed. Search timestamps and quoted authorship were not trusted as final evidence. Media URLs are inventoried; video speech and image pixels have not been reviewed. Paid/blocked article bodies are explicitly incomplete. Not every repost has a semantic analysis.

Selected relevant Nate transcripts/concept sections, AI Impact's caption-derived knowledge records, Karpathy's existing source corpus and current repo mechanisms were compared. This is a targeted cross-source comparison, not a fresh complete rereading of all archived scripts. AI Impact slides remain unavailable.

## Retrieval route

Used the existing `research/get_x_posts.py` FxTwitter mechanism with a bounded date traversal and individual-post endpoint. Public X pages returned 403. Timeline retries worked; no paid API or new account was required. The Hands Brain's Agent Reach entry is a fallback candidate, not needed for this capture; no new tool was installed. Native article bodies on individual posts recovered text unavailable in timeline previews. A moved Anthropic CI article was recovered at its current `/resources/articles/` URL. Tavily required reauthentication; built-in search recovered the publisher route.

## Continuation

Next step: recover the blocked MacStories body where authorised access exists; ingest the linked public interviews/talk speech and review media, then broaden reply coverage if exhaustive capture is required. Use the practical lessons on the existing TRADEFLOW demo when that project resumes. No architecture rewrite, plugin installation, auto-merge or new schedule was activated.

Status: **PARTIAL — exhaustive all-post/all-article ingestion NOT VERIFIED**. Available-source inventory and selected comparison are complete and checked; runtime adoption remains untested.

## Validation receipt

448 IDs are unique; every retained post excerpt is at most 20 words; all five attached article bodies have nonempty retrieval counts and hashes. Fresh repository audit: 0 errors, 10 warnings (existing Hands catalogue synchronisation and external page publication). Page rebuild was attempted locally; no external Claude page was published or marked published. Eddie-Ed archive commit: `4f9c6d6022ecfc6a9c94e9d0b9de51647504eea5`.
