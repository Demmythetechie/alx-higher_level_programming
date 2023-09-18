#!/usr/bin/python3

"""
This script lists all states with a name starting
with N (upper N) from the database hbtn_0e_0_usa
"""

import sys
import MySQLdb

if __name__ == '__main__':
    """
    This script lists all states with a name starting
    with N (upper N) from the database hbtn_0e_0_usa
    """
    engine = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
    )
    cur = engine.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' OR name LIKE 'n%' ORDER BY id ASC;")
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    engine.close()
