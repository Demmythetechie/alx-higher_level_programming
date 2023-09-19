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
    inputt = ''
    i = 0
    while i < len(argv[4]):
        if argv[4][i] == '"' or argv[4][i] == "'":
            break
        inputt += argv[4][i]
        i += 1

    engine = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3]
    )
    cur = engine.cursor()
    cur.execute('''
            SELECT cities.name
            FROM cities
            INNER JOIN states ON cities.state_id = states.id
            WHERE states.name = '{}';
    '''.format(inputt))
    rows = cur.fetchall()
    count = 0
    for row in rows:
        print(row[0], end='')
        if count != len(rows) - 1:
            print(', ', end='')
        count += 1
    print()
