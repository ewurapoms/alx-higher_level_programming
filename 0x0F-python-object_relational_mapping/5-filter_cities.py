#!/usr/bin/python3
"""  lists all states from the database """
import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(
                        host="localhost",
                        user=sys.argv[1],
                        passwd=sys.argv[2],
                        db=sys.argv[3],
                        port=3306,
                        charset="utf8"
                        )
    cur = db.cursor()
    cur.execute("""SELECT cities.name FROM
                cities INNER JOIN states ON states.id=cities.state_id
                WHERE states.name=%s""", (sys.argv[4],))
    rows = cur.fetchall()
    new = list(r[0] for r in rows)
    print(*new, sep=", ")
    cur.close()
    db.close()
