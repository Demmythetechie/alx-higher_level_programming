#!/usr/bin/python3

"""
This script takes in an argument and displays
all values in the states table of hbtn_0e_0_usa
where name matches the argument.
"""

import sys
import MySQLdb


if __name__ == '__main__':
    """
    This script takes in an argument and displays
    all values in the states table of hbtn_0e_0_usa
    where name matches the argument.
    """
    engine = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
    )

    cur = engine.cursor()
    cur.execute('''
            SELECT * FROM states WHERE name LIKE BINARY '{}%' ORDER
            BY id ASC;
    '''.format(sys.argv[4]))
    rows = cur.fetchall()
    for row in rows:
        print(row)
