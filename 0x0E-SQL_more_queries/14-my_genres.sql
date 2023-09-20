-- Lists genre for Dexter in the database hbtn_0d_tvshows
SELECT tg.name
FROM tv_genres tg
INNER JOIN tv_show_genres tsg
ON tg.id = tsg.genre_id
INNER JOIN tv_shows ts
ON ts.id = tsg.show_id
WHERE ts.title = "Dexter"
ORDER BY tg.name;
