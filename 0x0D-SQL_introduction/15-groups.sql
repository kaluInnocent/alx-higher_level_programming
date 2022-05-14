-- Script lists number of records with the same score in a table

SELECT count(distinct(score)) AS number
FROM second_table
ORDER BY score DESC;
