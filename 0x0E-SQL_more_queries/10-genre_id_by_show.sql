-- Write a script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
-- Each record should display: tv_shows.title - tv_show_genres.genre_id
-- Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id

SELECT tsh.title, tshg.id
FROM tv_shows AS tsh INNER JOIN tv_show_genres AS tshg
ON tsh.id = tshg.genre_id
ORDER BY tsh.title, tshg.genre_id ASC;
