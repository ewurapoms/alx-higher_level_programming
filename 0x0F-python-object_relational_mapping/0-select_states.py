#!/usr/bin/python3
""" Module lists all states from database"""
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
    cur.execute("SELECT * FROM states")
    rows = cur.fetchall()
    for r in rows:
        print(r)
    cur.close()
    db.close()
