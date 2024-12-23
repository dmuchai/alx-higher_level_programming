#!/usr/bin/python3
"""Deletes all State objects with a name containing the letter a."""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            argv[1], argv[2], argv[3]
        ),
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    states_to_delete = session.query(State).filter(
            State.name.like('%a%')
            ).all()
    for state in states_to_delete:
        session.delete(state)
    session.commit()
    session.close()
