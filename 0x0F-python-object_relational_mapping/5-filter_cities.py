#!/usr/bin/python3
""" Lists all cities from the database """

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(
            host="localhost",
            user=argv[1],
            passwd=argv[2],
            db=argv[3])
    cur = db.cursor()
    cur.execute(
            "SELECT c.name "
            "FROM cities AS c "
            "WHERE c.state_id in ( "
            "SELECT s.id "
            "FROM states AS s "
            "WHERE s.name = %s)",
            (argv[4], ))
    rows = cur.fetchall()
    for i in range(len(rows)):
        print(rows[i][0], end="")
        print(', ', end="") if len(rows) - 1 > i else print()
