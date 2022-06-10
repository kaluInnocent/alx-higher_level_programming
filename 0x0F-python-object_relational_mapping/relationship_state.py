#!/usr/bin/python3
""" python file that contains the class definition of a State
and an instance Base = declarative_base()
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from relationship_city import City

Base = declarative_base()


class State(Base):
    """A class states that inherits from sqlalchemy declarative_base()

    Attributes
    -----------
    id: state id (int)
    name: state name (str)
    """

    __tablename__ = 'states'
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
    cities = relationship("City", backref="state", cascade="all, delete")
