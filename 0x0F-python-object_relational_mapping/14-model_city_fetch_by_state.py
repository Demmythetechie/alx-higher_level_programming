#!/usr/bin/python3

"""
This script prints all City objects from the database hbtn_0e_14_usa
"""

from sqlalchemy import create_engine
from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker, relationship

if __name__ == '__main__':
    """
    This script prints all City objects from the database hbtn_0e_14_usa
    """

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    rows = session.query(City, State).join(State).all()
    for cities, state in rows:
        print('{}: ({}) {}'.format(state.name, cities.id, cities.name))
