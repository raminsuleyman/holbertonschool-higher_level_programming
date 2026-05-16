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
    s = Session()
    n = sys.argv[4]
    st = s.query(State).filter(State.name == n).order_by(State.id).first()
    if st is not None:
        print(st.id)
    else:
        print("Not found")
    session.close()
