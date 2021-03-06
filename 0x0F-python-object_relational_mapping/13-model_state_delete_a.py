#!/usr/bin/python3
"""A script that deletes all State objects with a name containing the letter a from the database hbtn_0e_6_usa"""

if __name__ == "__main__":
    import sys
    from model_state import State, Base
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    
    for state in session.query(State):
        if "a" in state.name:
            session.delete(state)
    session.commit()
    session.close()
    
