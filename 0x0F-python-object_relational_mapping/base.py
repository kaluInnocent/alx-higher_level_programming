#!/usr/bin/python3
"""
Contains all import files
"""

import system
from model_state import Base, State
from sqlalchemy import (create_engine)

#creating a connection
if __name__ == "__main__":
    engine = create_engine(
            'mysql+mysqldb://{}:\
            {}@localhost/{}'
            .format(
                sys.argv[1],
                sys.argv[2],
                sys.argv[3]
                ),
            pool_pre_ping=True
            )
    Base.metadata.create_all(engine)




