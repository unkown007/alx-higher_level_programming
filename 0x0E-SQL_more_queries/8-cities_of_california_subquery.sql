-- lists all the cities of California that can be found in the hbtn_0d_usa database
SELECT c.id, c.name
FROM cities AS c
WHERE c.state_id in (
	SELECT id
	FROM states AS s
	WHERE s.name = "California"
	)
ORDER BY c.id ASC;
