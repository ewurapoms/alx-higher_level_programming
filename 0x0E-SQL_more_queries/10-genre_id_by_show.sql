-- Lists all hbtn_0d_tvshows that have at least one genre linked
SELECT t.title, g.genre_id
FROM tv_shows t, tv_show_genres g
WHERE t.id = g.show_id AND g.genre_id > 0
ORDER BY t.title, g.genre_id;
