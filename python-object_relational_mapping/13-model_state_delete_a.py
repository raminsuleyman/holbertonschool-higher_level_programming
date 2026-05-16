#!/usr/bin/python3
"""prints the first State object"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3]
        )
    )
    Session = sessionmaker(bind=engine)
    d = Session()

    s = d.query(State).filter(State.name.like("%a%")).order_by(State.id).all()
    for t in s:
        d.delete(t)
    d.commit()
    d.close()
