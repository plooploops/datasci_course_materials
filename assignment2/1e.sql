SELECT COUNT(*) FROM
(
SELECT docid, SUM(count) as t
FROM frequency
GROUP BY docid
HAVING SUM(count) > 300
)
WHERE t > 300
;