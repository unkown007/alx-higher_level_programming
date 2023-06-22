#!/usr/bin/python3
""" lists all State objects, and corresponding City objects,
contained in the database """


from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost/{}".format(
                argv[1],
                argv[2],
                argv[3]),
            pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    cities = session.query(City).order_by(City.state_id, City.id).all()
    tmp = cities[0].state
    print("{}: {}".format(tmp.id, tmp.name))
    for city in cities:
        if city.state.id != tmp.id:
            tmp = city.state
            print("{}: {}".format(tmp.id, tmp.name))
        print("\t{}: {}".format(city.id, city.name))
    session.commit()
    session.close()
