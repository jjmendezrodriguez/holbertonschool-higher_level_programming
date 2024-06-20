#!/usr/bin/python3
"""List all states with a name starting with N from the database hbtn_0e_0_usa"""
import MySQLdb
import sys
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class State(Base):
    """State class mapped to the states table"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(256), nullable=False)

def list_states_starting_with_N(username, password, dbname):
    """Connects to MySQL database and lists states starting with N"""
    # Create a connection string
    conn_str = f"mysql+mysqldb://{username}:{password}@localhost:3306/{dbname}"
    
    # Create an engine
    engine = create_engine(conn_str)
    
    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)
    
    # Create a session
    session = Session()
    
    # Query all states with a name starting with N and order by id
    states = session.query(State).filter(State.name.like('N%')).order_by(State.id.asc()).all()
    
    # Print each state
    for state in states:
        print(f"({state.id}, '{state.name}')")
    
    session.close()

if __name__ == "__main__":
        # Get command line arguments
        username = sys.argv[1]
        password = sys.argv[2]
        dbname = sys.argv[3]
        
        # Call the function to list states
        list_states_starting_with_N(username, password, dbname)
