SELECT 
  c.docid
  ,SUM(c.val) as S
FROM
(
SELECT 
  a.docid
  ,b.term
  ,SUM(a.count * b.count) as val
FROM 
(SELECT 
  docid
  ,term
  ,count
FROM frequency as f1) as a, 
(
SELECT 'q' as docid, 'washington' as term, 1 as count 
UNION
SELECT 'q' as docid, 'taxes' as term, 1 as count
UNION 
SELECT 'q' as docid, 'treasury' as term, 1 as count
) as b
WHERE a.term = b.term
AND a.docid < b.docid
GROUP BY a.docid, b.term) as c
GROUP BY c.docid
ORDER BY S DESC
LIMIT 10
;