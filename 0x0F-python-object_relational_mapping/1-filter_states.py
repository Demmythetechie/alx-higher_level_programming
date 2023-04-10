#!/usr/bin/python3
"""This list all states starting with N"""
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
cur.execute("SELECT * FROM states WHERE name LIKE 'N%'")
row = cur.fetchall()
for i in row:
    print(i)
