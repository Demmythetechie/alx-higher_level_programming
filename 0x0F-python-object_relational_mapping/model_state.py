#!/usr/bin/python3
"""
This script defines a class State and an instance of declarative base
which is inheritrd by the class State
"""

from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    State class

     Attribute:
     id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
     name = Column(String(128), nullable=False)
    """

    __tablename__ = "states"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
