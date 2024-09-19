
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base import Base
from models.aquarium import Aquarium
from models.equipment import Equipment
from models.water_parameter import WaterParameter
from models.fish import Fish
from models.plant import Plant
from models.invertebrate import Invertebrate
from models.store import Store
from models.expense import Expense
from models.income import Income
from models.resource import Resource
from models.user import User  # Import User model

# Create an SQLite database
engine = create_engine('sqlite:///instance/aquatrac.db', echo=True)

# Create all tables at once
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

print("Database initialized and tables created successfully.")
