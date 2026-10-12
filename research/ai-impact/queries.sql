-- Open with sqlite3 knowledge.sqlite, then .read queries.sql
-- Evidence-linked full-text search. Replace OODA with your topic.
SELECT k.title, k.explanation, k.source_url, k.verification
FROM knowledge_search s JOIN knowledge k ON k.id=s.record_id
WHERE knowledge_search MATCH 'OODA';

-- Confirm actual coverage.
SELECT caption_status, visual_status, count(*) FROM videos
GROUP BY caption_status, visual_status;

-- Workflows rather than promotions.
SELECT v.title AS video,k.title,k.explanation,k.source_url
FROM knowledge k JOIN videos v ON v.id=k.video_id
WHERE k.kind='workflow';

-- Topic backlinks are shared-topic relationships, not proof of agreement.
SELECT * FROM topic_backlinks LIMIT 20;

-- Spoken visual cues to help resume visual review; not all slides.
SELECT v.title,q.start_seconds,q.status,q.url
FROM visual_review_queue q JOIN videos v ON v.id=q.video_id;
