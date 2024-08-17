from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker
from models.base import Base
from models.user import User
from models.store import Store
from models.aquarium import Aquarium
from models.fish import Fish
from models.plant import Plant
from models.invertebrate import Invertebrate
from models.equipment import Equipment
from models.water_parameter import WaterParameter
from models.expense import Expense
from models.income import Income
from models.task import Task
from models.resource import Resource

# Create an SQLite database
engine = create_engine('sqlite:///instance/aquatrac.db', echo=True)

# Debug: Print all tables in Base.metadata
print("Tables in Base.metadata:")
for table in Base.metadata.tables:
    print(f"- {table}")

# Debug: Print foreign keys for Aquarium
print("\nForeign keys for Aquarium:")
for fk in Aquarium.__table__.foreign_keys:
    print(f"- {fk}")

# Create all tables at once
Base.metadata.create_all(engine)

# Debug: Check if tables were created
inspector = inspect(engine)
print("\nCreated tables:")
for table_name in inspector.get_table_names():
    print(f"- {table_name}")

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

print("\nDatabase initialized and tables created successfully.")