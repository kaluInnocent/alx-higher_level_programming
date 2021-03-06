#!/usr/bin/python3
"""A script that prints the State object
with the name passed as argument from the database hbtn_0e_6_usa
"""

if __name__ == "__main__":
    import sys
    from mode_state import Base, State
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import (create_engine)

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3]),
        pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = Sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).order_by(State.id).all()
    alert = 0
    for state in states:
        if state.name == sys.argv[4]:
            print("{}".format(state.id))
            alert = 1
            break
        if alert == 0:
            print("Not found")
