-- Lists all shows in the database hbtn_0d_tvshows
-- Displays NULL for shows without genres
SELECT t.title, g.genre_id
FROM tv_shows t
LEFT JOIN tv_show_genres g
ON t.id = g.show_id
ORDER BY t.title, g.genre_id;
