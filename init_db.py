import os
from sqlalchemy import create_engine, Index
from sqlalchemy.orm import sessionmaker
from models.base import Base
from models.user import User
from models.supplier import Supplier
from models.aquarium import Aquarium
from models.equipment import Equipment
from models.water_parameter import WaterParameter
from models.fish import Fish
from models.plant import Plant
from models.invertebrate import Invertebrate
from models.expense import Expense
from models.income import Income
from models.resource import Resource
from models.task import Task  # Added Task model

# Determine the environment
FLASK_ENV = os.environ.get('FLASK_ENV', 'development')

# Ensure the instance directory exists
instance_dir = '/Users/ian/Documents/Dev/aquatrac/instance'
os.makedirs(instance_dir, exist_ok=True)

# Define the database engine based on the environment
if FLASK_ENV == 'testing':
    database_path = os.path.join(instance_dir, 'test_aquatrac.db')
else:
    database_path = os.path.join(instance_dir, 'aquatrac.db')

engine = create_engine(f'sqlite:///{database_path}', connect_args={'check_same_thread': False})

# Create all tables
Base.metadata.create_all(engine)

# Create indexes
Index('idx_aquarium_store', Aquarium.store_id)
Index('idx_supplier_name', Supplier.name)
Index('idx_equipment_supplier', Equipment.store_id)
Index('idx_equipment_aquarium', Equipment.aquarium_id)
Index('idx_water_quality_aquarium', WaterParameter.aquarium_id)
Index('idx_water_quality_date', WaterParameter.date)
Index('idx_fish_catalog_common_name', Fish.common_name)
Index('idx_fish_catalog_scientific_name', Fish.scientific_name)
Index('idx_plant_catalog_common_name', Plant.common_name)
Index('idx_plant_catalog_scientific_name', Plant.scientific_name)
Index('idx_invertebrate_catalog_common_name', Invertebrate.common_name)
Index('idx_invertebrate_catalog_scientific_name', Invertebrate.scientific_name)
Index('idx_expenses_aquarium', Expense.aquarium_id)
Index('idx_expenses_date', Expense.date)
Index('idx_expenses_supplier', Expense.store_id)
Index('idx_incomes_aquarium', Income.aquarium_id)
Index('idx_incomes_date', Income.date)
Index('idx_task_aquarium', Task.aquarium_id)  # Added index for Task
Index('idx_task_due_date', Task.due_date)  # Added index for Task

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

def init_db():
    """Initialize the database."""
    Base.metadata.create_all(engine)

def get_session():
    """Get a new session."""
    return Session()

if __name__ == '__main__':
    init_db()
    print(f"Database initialized at {database_path}")
