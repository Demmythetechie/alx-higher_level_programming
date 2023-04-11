#!/usr/bin/python3
"""This retrieves all rows in state where the name='Arizona'"""
import sys
import MySQLdb


db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd = sys.argv[2],
        db=sys.argv[3]
)
cur = db.cursor()
cur.execute(f"SELECT * FROM states WHERE states.name='{sys.argv[4]}'")
row = cur.fetchall()
for i in row:
    print(i)

