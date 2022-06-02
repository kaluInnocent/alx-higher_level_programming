#!/usr/bin/python3
#defines a state model
#inherits from SQLAlchemy Base
#links to MYSQLtable: states


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer

Base = declarative_base()


class State(Base):
    """A class states that inherits from sqlalchemy declarative_base()

    Attributes:
        __table__ (str): name of SQL table
        id (sqlalchemy.Interger): state id 
        name (sqlalchemy.String): state name (str)
    """

    __tablename__ = 'states'

    id = Column(
            Interger,
            primary_key=True,
            unique=True,
            nullable=False,
            autoincrement=True)

    name = Column(
            String(128),
            nullabe=False)
