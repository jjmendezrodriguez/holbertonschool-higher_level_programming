#!/usr/bin/python3
"""
This module connects to a MySQL database and retrieves
all cities sorted by id in ascending order.
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

def list_cities(username, password, dbname):
    """
    Connects to MySQL database and lists all cities
    Args:
        username (str): The MySQL username
        password (str): The MySQL password
        dbname (str): The name of the database
    """
    # Create a connection string
    conn_str = f"mysql+mysqldb://{username}:{password}@localhost:3306/{dbname}"
    
    # Create an engine
    engine = create_engine(conn_str)
    
    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)
    
    # Create a session
    session = Session()
    
    # Query all cities and order by id
    cities = session.query(City).order_by(City.id.asc()).all()
    
    # Print each city
    for city in cities:
        print(f"({city.id}, '{city.name}', {city.state_id})")
    
    session.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./list_cities.py <mysql_username> <mysql_password> <database_name>")
    else:
        # Get command line arguments
        username = sys.argv[1]
        password = sys.argv[2]
        dbname = sys.argv[3]
        
        # Call the function to list cities
        list_cities(username, password, dbname)
