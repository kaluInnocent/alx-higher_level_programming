#!/usr/bin/python3
"""Script lists all states starting with N in a database
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
            FROM states
            WHERE name LIKE BINARY '{}'
            ORDER BY id ASC
            """
            .format(sys.argv[4])
            )
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
