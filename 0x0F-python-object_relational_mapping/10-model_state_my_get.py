#!/usr/bin/python3
"""
This script prints the State object with the name
passed as argument from the database hbtn_0e_6_usa
"""

from sys import argv
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    """
    This script prints the State object with the name
    passed as argument from the database hbtn_0e_6_usa
    """
    inputt = ''
    i = 0
    while i < len(argv[4]):
        if argv[4][i] == '"' or argv[4][i] == "'":
            break
        inputt += argv[4][i]
        i += 1

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]))

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    row = session.query(State).filter(
            State.name == '{}'.format(inputt)).first()
    if row is None:
        print('Not found')
    else:
        print(row.id)
