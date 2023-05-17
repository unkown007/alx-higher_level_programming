-- lists all shows catained in hbtn_0d_tvshows that have at least one genre linked
SELECT s.title, sg.genre_id
FROM tv_shows AS s
LEFT JOIN tv_show_genres AS sg ON s.id = sg.show_id
ORDER BY s.title, sg.genre_id;
