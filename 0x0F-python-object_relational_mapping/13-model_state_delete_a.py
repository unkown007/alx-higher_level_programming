#!/usr/bin/python3
""" delete all State object that contain the letter 'a'from the database """


import sys
from model_state import Base, State
from sqlalchemy import create_engine, delete
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.format(
                sys.argv[1],
                sys.argv[2],
                sys.argv[3]),
            pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    session.query(State).filter(State.name.like('%a%'))\
                        .delete(synchronize_session="fetch")
    session.commit()
    session.close()
