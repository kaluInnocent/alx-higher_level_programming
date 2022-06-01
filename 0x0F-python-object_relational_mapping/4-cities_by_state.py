#!/usr/bin/python3
"""Script lists all cities in a database
Usage: ./0-select_states.py username password database-name"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            charset="utf8"
            )
    cur = db.cursor()
    cur.execute(
            """SELECT *
            FROM cities
            GROUP BY state_id
            ORDER BY id ASC
            """
            )
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
