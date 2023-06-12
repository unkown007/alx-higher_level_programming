-- lists all genres not linked to the show Dexter
SELECT gen.name
FROM tv_genres AS gen
WHERE gen.id NOT IN (
	SELECT g.id
	FROM tv_genres AS g
	INNER JOIN tv_show_genres AS sg
	ON g.id = sg.genre_id
	INNER JOIN tv_shows AS s
	ON s.id = sg.show_id
	WHERE s.title = 'Dexter'
	ORDER BY g.name ASC
)
ORDER BY gen.name ASC;	
