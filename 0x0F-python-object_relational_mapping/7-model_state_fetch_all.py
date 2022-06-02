#!/usr/bin/python3
"""
Script lists all State objects from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
from model_state import States, Base

#creating a connection
if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    #extract a session
    session = Session()
    #querry a session
    states = (session.querry(State).group_by(State.id).all())
    for state in states:
        print(f"{state.id}: {state.name}")
    session.close()
