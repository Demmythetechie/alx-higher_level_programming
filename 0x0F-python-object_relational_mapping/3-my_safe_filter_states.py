#!/usr/bin/python3
"""
This does what task 2 does but instead escape the user data
from an sql statement to a string incase it is a sql statement
"""
import sys
import MySQLdb

if __name__ == '__main__':
    """
    This does what task 2 does but instead escape the 
    user data from an sql statement to a string incase
    it is a sql statement
    """


    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
    )

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE states.name= %s", (sys.argv[4], ))
    row = cur.fetchall()
    for i in row:
        print(i)
