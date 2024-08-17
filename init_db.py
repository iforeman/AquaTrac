from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base import Base  # Import Base from base.py
from models.user import User
from models.aquarium import Aquarium
from models.fish import Fish
from models.plant import Plant
from models.invertebrate import Invertebrate
from models.equipment import Equipment
from models.water_parameter import WaterParameter
from models.store import Store
from models.expense import Expense
from models.income import Income
from models.task import Task
from models.resource import Resource
from config import Config  # Import the Config class

# Create an SQLite database and initialize the tables using the URI from config
engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

print("Database initialized and tables created successfully.")
