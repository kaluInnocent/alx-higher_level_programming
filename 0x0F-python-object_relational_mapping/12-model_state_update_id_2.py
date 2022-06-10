#!/usr/bin/python3
""" A script that changes the name of a State object from the database hbtn_0e_6_usa"""

import sys
from model_state import State, Base
from sqlalchemy.orm import session
from sqlalchemy import create_engine


if __name__ == "__main__":
    import sys
    from model_state import State
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3]),
        pool_pre_ping=True
        )
    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).order_by(State.id).filter(State.id == 2):
        state.name = "New Mexico"
    session.commit()
    session.close()
