#!/usr/bin/python3

"""
This script deletes all State objects with a name
containing the letter a from the database hbtn_0e_6_usa
"""

from sqlalchemy import create_engine
from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    """
    This script deletes all State objects with a name
    containing the letter a from the database hbtn_0e_6_usa
    """

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    instRows = session.query(State).filter(State.name.like('%a%'))
    for row in instRows:
        session.delete(row)
    session.commit()
    session.close()
