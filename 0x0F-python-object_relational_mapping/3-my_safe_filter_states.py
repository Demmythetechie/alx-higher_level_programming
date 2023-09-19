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
    inputt = ''
    i = 0
    while i < len(sys.argv[4]):
        if sys.argv[4][i] == '"' or sys.argv[4][i] == "'":
            break
        inputt += sys.argv[4][i]
        i += 1

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
    '''.format(inputt))
    rows = cur.fetchall()
    for row in rows:
        print(row)
