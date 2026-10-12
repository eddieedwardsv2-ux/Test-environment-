-- sqlite3 reference.sqlite
SELECT provider,collection,count(*) FROM sources GROUP BY provider,collection;
SELECT s.title,s.url,s.review_status FROM source_search f
JOIN sources s ON s.id=f.source_id WHERE source_search MATCH 'prompting';
SELECT name,model_ids,document_status FROM models;
SELECT title,explanation,url FROM teaching;
SELECT title,url,retrieval_status FROM sources WHERE retrieval_status<>'body_captured';
