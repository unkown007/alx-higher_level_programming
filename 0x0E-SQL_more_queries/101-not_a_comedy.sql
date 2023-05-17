-- lists all shows without Comedy genry
SELECT sh.title
FROM tv_shows AS sh
WHERE sh.id NOT IN (
	SELECT s.id
	FROM tv_shows AS s
	INNER JOIN tv_show_genres AS sg
	ON s.id = sg.show_id
	INNER JOIN tv_genres AS g
	ON sg.genre_id = g.id AND g.name = 'Comedy'
	ORDER BY s.title ASC
)
ORDER BY sh.title ASC;
