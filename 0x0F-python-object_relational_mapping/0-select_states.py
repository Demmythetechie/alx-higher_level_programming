#!/usr/bin/python3
"""This pyfile retirves data from hbtn_0d_usa database"""
import sys
import MySQLdb


db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
)
cur = db.cursor()
cur.execute("SELECT * FROM states ORDER BY states.id ASC")
rows = cur.fetchall()
for i in rows:
    print(i)
