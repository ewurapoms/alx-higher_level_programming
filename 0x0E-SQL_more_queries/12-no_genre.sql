-- Lists all shows in hbtn_0d_tvshows database with no genre linked
SELECT t.title, g.genre_id
FROM tv_shows t
LEFT JOIN tv_show_genres g
ON t.id = g.show_id
WHERE g.show_id IS NULL
ORDER BY t.title, g.genre_id;
