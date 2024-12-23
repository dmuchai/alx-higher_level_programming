#!/usr/bin/python3
"""
Contains class definition of a State and instance of Base = declarative_base().
"""
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    Represents a state for a MySQL database.

    Attributes:
        id (int): The state's id, primary key, auto-generated.
        name (str): The state's name, max 128 characters, non-nullable.
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
