-- Script lists number of records with the same score in a table

SELECT score, count(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
