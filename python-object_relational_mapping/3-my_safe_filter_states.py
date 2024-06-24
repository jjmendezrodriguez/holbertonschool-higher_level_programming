#!/usr/bin/python3
"""
This module connects to a MySQL database and retrieves
all states where the name matches the argument, sorted by id in ascending order,
safe from SQL injections.
"""

import sys
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class State(Base):
    """
    State class mapped to the states table
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(256), nullable=False)

def list_states_matching_name(username, password, dbname, state_name):
    """
    Connects to MySQL database and lists states matching the given name
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
    
    # Query all states where name matches the argument and order by id
    states = session.query(State).filter(State.name == state_name).order_by(State.id.asc()).all()
    
    # Print each state
    for state in states:
        print(f"({state.id}, '{state.name}')")
    
    session.close()

if __name__ == "__main__":
        # Get command line arguments
        username = sys.argv[1]
        password = sys.argv[2]
        dbname = sys.argv[3]
        state_name = sys.argv[4]
        
        # Call the function to list states
        list_states_matching_name(username, password, dbname, state_name)
