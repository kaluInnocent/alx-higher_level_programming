-- Write a script that lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows.
-- If a show doesn’t have a genre, display NULL in the genre column
-- Each record should display: tv_shows.title - tv_genres.name
-- Results must be sorted in ascending order by the show title and genre name

SELECT t.title AS title, tg.name AS name
FROM tv_shows AS t
LEFT JOIN tv_show_genres AS ts
ON t.id = ts.show_id
INNER JOIN tv_genres AS tg
ON tg.id = ts.genre_id
ORDER BY title, name ASC;
