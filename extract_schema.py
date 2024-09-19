
from sqlalchemy import create_engine, Column, Integer, String, Float, Enum, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
import json

# Create a base class for SQLAlchemy models
Base = declarative_base()

# Define the Fish model
class Fish(Base):
    __tablename__ = 'fish'

    id = Column(Integer, primary_key=True, autoincrement=True)
    aquarium_id = Column(Integer, ForeignKey('aquariums.id', ondelete='CASCADE'), index=True)
    scientific_name = Column(String)
    common_name = Column(String, index=True)
    species = Column(String, index=True)
    origin = Column(String, index=True)
    quantity = Column(Integer)
    max_size = Column(Float)
    min_tank_size = Column(Float)
    min_temp = Column(Float)
    max_temp = Column(Float)
    kh_min = Column(Float)
    kh_max = Column(Float)
    ph_min = Column(Float)
    ph_max = Column(Float)
    species_information = Column(String)
    aquarium_care = Column(String)
    feeding_nutrition = Column(String)
    diet = Column(Enum('Omnivore', 'Carnivore', 'Herbivore'))
    aquarium_type = Column(Enum('Community', 'Species', 'Cichlid', 'Biotype', 'Breeding', 'Planted', 'Shrimp', 'Fish-only', 'Coldwater'))
    care_level = Column(Enum('Easy', 'Moderate', 'Difficult'))
    temperament = Column(Enum('Peaceful', 'Semi-aggressive', 'Aggressive'))
    purchase_date = Column(String)
    unit_price = Column(Float)
    store_id = Column(Integer, ForeignKey('stores.id'), index=True)
    death_date = Column(String, nullable=True)
    sale_date = Column(String, nullable=True)
    sale_price = Column(Float, nullable=True)
    birth_date = Column(String, nullable=True)
    father_fish_id = Column(Integer, ForeignKey('fish.id'), nullable=True)
    mother_fish_id = Column(Integer, ForeignKey('fish.id'), nullable=True)
    picture = Column(String, nullable=True)

    aquarium = relationship('Aquarium', back_populates='fish')
    store = relationship('Store', back_populates='fish')
    father_fish = relationship('Fish', remote_side=[id], foreign_keys=[father_fish_id])
    mother_fish = relationship('Fish', remote_side=[id], foreign_keys=[mother_fish_id])

# Define the Expense model
class Expense(Base):
    __tablename__ = 'expenses'

    id = Column(Integer, primary_key=True, autoincrement=True)
    aquarium_id = Column(Integer, ForeignKey('aquariums.id', ondelete='CASCADE'), index=True)
    date = Column(String, index=True)
    item = Column(String)
    category = Column(String)
    store_id = Column(Integer, ForeignKey('stores.id'), index=True)

    aquarium = relationship('Aquarium', back_populates='expenses')
    store = relationship('Store', back_populates='expenses')

# Define the Equipment model
class Equipment(Base):
    __tablename__ = 'equipment'

    id = Column(Integer, primary_key=True, autoincrement=True)
    aquarium_id = Column(Integer, ForeignKey('aquariums.id', ondelete='CASCADE'), index=True)
    type = Column(String)
    store_id = Column(Integer, ForeignKey('stores.id'), index=True)
    performance_lph = Column(Float)
    model = Column(String)

    aquarium = relationship('Aquarium', back_populates='equipment')
    store = relationship('Store', back_populates='equipment')

# Define the Aquarium model
class Aquarium(Base):
    __tablename__ = 'aquariums'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    model = Column(String, nullable=True)
    tank_type = Column(Enum('Community', 'Species', 'Cichlid', 'Biotype', 'Breeding', 'Planted', 'Reef', 'Other'), nullable=False)

    fish = relationship('Fish', back_populates='aquarium')
    expenses = relationship('Expense', back_populates='aquarium')
    equipment = relationship('Equipment', back_populates='aquarium')

# Define the Invertebrate model
class Invertebrate(Base):
    __tablename__ = 'invertebrates'

    id = Column(Integer, primary_key=True, autoincrement=True)
    aquarium_id = Column(Integer, ForeignKey('aquariums.id', ondelete='CASCADE'), index=True)
    scientific_name = Column(String)
    common_name = Column(String, index=True)
    species = Column(String, index=True)
    family = Column(String, index=True)

    aquarium = relationship('Aquarium', back_populates='invertebrates')

# Define the Income model
class Income(Base):
    __tablename__ = 'incomes'

    id = Column(Integer, primary_key=True, autoincrement=True)
    aquarium_id = Column(Integer, ForeignKey('aquariums.id', ondelete='CASCADE'), index=True)
    date = Column(String, index=True)
    designation = Column(String)
    amount = Column(Float)
    notes = Column(String)
    store_id = Column(Integer, ForeignKey('stores.id'), index=True)

    aquarium = relationship('Aquarium', back_populates='incomes')
    store = relationship('Store', back_populates='incomes')

# Define the Resource model
class Resource(Base):
    __tablename__ = 'resources'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    name = Column(String, nullable=False)
    type = Column(Enum('Food', 'Medication', 'Supplement', 'Other'), nullable=False)
    quantity = Column(Integer, nullable=False)
    unit_price = Column(Float, nullable=False)

# Define the Store model
class Store(Base):
    __tablename__ = 'stores'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

    fish = relationship('Fish', back_populates='store')
    expenses = relationship('Expense', back_populates='store')
    equipment = relationship('Equipment', back_populates='store')
    incomes = relationship('Income', back_populates='store')

# Define the Task model
class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True)
    aquarium_id = Column(Integer, ForeignKey('aquariums.id'), nullable=False)
    description = Column(String)
    due_date = Column(Date)
    completed = Column(Boolean, default=False)
    type = Column(String)
    interval = Column(Integer)
    week_day = Column(Integer)

    aquarium = relationship('Aquarium', back_populates='tasks')

# Define the Plant model
class Plant(Base):
    __tablename__ = 'plants'

    id = Column(Integer, primary_key=True, autoincrement=True)
    aquarium_id = Column(Integer, ForeignKey('aquariums.id', ondelete='CASCADE'), index=True)
    scientific_name = Column(String)
    common_name = Column(String, index=True)
    family = Column(String, index=True)
    origin = Column(String)

    aquarium = relationship('Aquarium', back_populates='plants')

# Define the User model
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    password_hash = Column(String, nullable=True)

# Define the WaterParameter model
class WaterParameter(Base):
    __tablename__ = 'water_parameters'

    id = Column(Integer, primary_key=True, autoincrement=True)
    aquarium_id = Column(Integer, ForeignKey('aquariums.id', ondelete='CASCADE'), index=True)
    date = Column(String, index=True)
    temperature_min = Column(Float)
    temperature_max = Column(Float)
    ph_min = Column(Float)
    ph_max = Column(Float)

    aquarium = relationship('Aquarium', back_populates='water_parameters')

# Function to extract schema details
def extract_schema_details(models):
    schema_details = []
    for model in models:
        table_name = model.__tablename__
        columns = model.__table__.columns
        foreign_keys = model.__table__.foreign_keys
        indexes = model.__table__.indexes
        
        # Collect column details
        column_details = []
        for column in columns:
            col_info = {
                "name": column.name,
                "type": str(column.type),
                "nullable": column.nullable,
                "primary_key": column.primary_key,
                "autoincrement": column.autoincrement,
                "default": column.default,
                "unique": column.unique
            }
            column_details.append(col_info)
        
        # Collect foreign key details
        foreign_key_details = []
        for fk in foreign_keys:
            fk_info = {
                "column": fk.parent.name,
                "references": fk.target_fullname,
                "ondelete": fk.ondelete,
                "onupdate": fk.onupdate
            }
            foreign_key_details.append(fk_info)
        
        # Collect index details
        index_details = []
        for index in indexes:
            index_info = {
                "name": index.name,
                "columns": [col.name for col in index.columns],
                "unique": index.unique
            }
            index_details.append(index_info)
        
        # Append table schema details
        schema_details.append({
            "table_name": table_name,
            "columns": column_details,
            "foreign_keys": foreign_key_details,
            "indexes": index_details
        })
    
    return schema_details

# List of all models
models = [Fish, Expense, Equipment, Aquarium, Invertebrate, Income, Resource, Store, Task, Plant, User, WaterParameter]

# Extract schema details
schema_details = extract_schema_details(models)

# Save the schema details to a JSON file
with open('schema_details.json', 'w') as json_file:
    json.dump(schema_details, json_file, indent=4)

print("Schema details extracted and saved to schema_details.json")
