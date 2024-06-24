#!/usr/bin/python3
"""
This module connects to a MySQL database and retrieves
all cities of a given state, sorted by id in ascending order,
safe from SQL injections.
"""

import sys
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

class State(Base):
    """
    State class mapped to the states table
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(256), nullable=False)

class City(Base):
    """
    City class mapped to the cities table
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(256), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    state = relationship("State")

def list_cities_by_state(username, password, dbname, state_name):
    """
    Connects to MySQL database and lists all cities of the given state
    Args:
        username (str): The MySQL username
        password (str): The MySQL password
        dbname (str): The name of the database
        state_name (str): The name of the state to search for
    """
    # Create a connection string
    conn_str = f"mysql+mysqldb://{username}:{password}@localhost:3306/{dbname}"
    
    # Create an engine
    engine = create_engine(conn_str)
    
    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)
    
    # Create a session
    session = Session()
    
    # Query cities of the given state and order by city id
    cities = session.query(City).join(State).filter(State.name == state_name).order_by(City.id.asc()).all()
    
    # Print each city
    for city in cities:
        print(f"({city.id}, '{city.name}', {city.state_id})")
    
    session.close()

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: ./list_cities_by_state.py <mysql_username> <mysql_password> <database_name> <state_name>")
    else:
        # Get command line arguments
        username = sys.argv[1]
        password = sys.argv[2]
        dbname = sys.argv[3]
        state_name = sys.argv[4]
        
        # Call the function to list cities
        list_cities_by_state(username, password, dbname, state_name)
