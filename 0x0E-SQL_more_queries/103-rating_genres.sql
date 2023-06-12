-- lists all genres by their rating
SELECT g.name, SUM(r.rate) AS rating
FROM tv_shows AS s
INNER JOIN tv_show_ratings AS r
ON s.id = r.show_id
INNER JOIN tv_show_genres AS sg
ON sg.show_id = s.id
INNER JOIN tv_genres AS g
ON sg.genre_id = g.id
GROUP BY g.name
ORDER BY rating DESC;
