-- Write a script that lists all shows without the genre Comedy in the database hbtn_0d_tvshows.
-- The tv_genres table contains only one record where name = Comedy (but the id can be different)
-- Each record should display: tv_shows.title
-- Results must be sorted in ascending order by the show title

SELECT DISTINCT t.title AS title
FROM tv_shows AS t
LEFT JOIN tv_show_genres AS ts
ON t.id = ts.show_id
LEFT JOIN tv_genres AS tg
ON tg.id = ts.genre_id
WHERE t.title NOT IN (
	SELECT title
	FROM tv_shows AS t
	INNER JOIN tv_show_genres AS ts
	ON t.id = ts.show_id
	INNER JOIN tv_genres AS tg
	ON tg.id = ts.genre_id
	WHERE tg.name = "Comedy"
)
ORDER BY title;
