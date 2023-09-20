-- Display the number of shows linked to each genre in the database
SELECT tg.name AS genre, COUNT(*) AS number_of_shows
FROM tv_genres tg
INNER JOIN tv_show_genres tsg
ON tsg.genre_id = tg.id
GROUP BY tsg.genre_id
ORDER BY number_of_shows DESC;
