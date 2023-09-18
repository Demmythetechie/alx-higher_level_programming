#!/usr/bin/python3

"""
This script takes in an argument and displays
all values in the states table of hbtn_0e_0_usa
where name matches the argument.
"""

import sys
import MySQLdb


engine = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
)

cur = engine.cursor()
cur.execute(
        f'SELECT * FROM states WHERE name = "{sys.argv[4]}" ORDER BY id ASC;'
)
row = cur.fetchone()
print(row)
