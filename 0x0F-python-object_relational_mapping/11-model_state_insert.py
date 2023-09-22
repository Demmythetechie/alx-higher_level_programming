#!/usr/bin/python3

"""
This script adds the State object “Louisiana” to the database hbtn_0e_6_usa
"""

from sys import argv
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    """
    This script adds the State object “Louisiana” to the database hbtn_0e_6_usa
    """

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    newState = State(name='Louisiana')
    session.add(newState)
    session.commit()
    # printing state id

    row = session.query(State).filter(State.name == 'Louisiana').first()
    print(row.id)
