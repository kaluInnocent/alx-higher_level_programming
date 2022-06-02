#!/usr/bin/python3
"""defines a class State and instance of Base"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class States(Base):
    """class definition of a State and an instance Base = declarative_base()

    Attributes:
        __tablename__ (str): Name of SQL table
        id (sqlalchemy.Integer): state id
        name (sqlalchemy.String): state name
        """

        __tablename__ = 'states'
        id = Column(
                Integer,
                primary_key,
                unique=True,
                autoincrement=True,
                nullable=False)
        name = Column(
                String(128),
                nullable=False)
