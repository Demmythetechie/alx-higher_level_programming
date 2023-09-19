#!/usr/bin/python3
"""
This script lists all cities from the database hbtn_0e_4_usa
"""
import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    This script lists all cities from the database hbtn_0e_4_usa
    """

    engine = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3]
    )
    cur = engine.cursor()
    cur.execute("""
            SELECT cities.id, cities.name, states.name
            FROM cities
            INNER JOIN states ON cities.state_id = states.id;
    """)
    rows = cur.fetchall()
    for row in rows:
        print(row)
