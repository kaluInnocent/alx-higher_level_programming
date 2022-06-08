#!/usr/bin/python3
""" Python file similar to model_state.py named model_city.py that contains the class definition of a City.
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer
from model_state import Base, State


class City(Base):
    """A class states that inherits from sqlalchemy declarative_base()

    Attributes
    -----------
    id: city id (int)
    name: city name (str)
    state_id: state id (int)
    """

    __tablename__ = 'cities'
    id = Column(
            Interger,
            primary_key=True,
            unique=True,
            nullable=False,
            autoincrement=True
            )
    name = Column(
            String(128),
            nullabe=False
            )
    state_id = Column(
            Interger,
            nullable=False,
            ForeignKey('states.id'))
