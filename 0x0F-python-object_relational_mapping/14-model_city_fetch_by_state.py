#!/usr/bin/python3
""" prints all City objects from the database """

from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship


if __name__ == '__main__':
    State.cities = relationship("City",
                                order_by=City.id, back_populates="state")
    engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost/{}".format(
                argv[1],
                argv[2],
                argv[3]),
            pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    for state, city in session.query(State, City)\
            .filter(State.id == City.state_id).all():
        print('{}: {:d} {}'.format(state.name, city.id, city.name))
    session.close()
