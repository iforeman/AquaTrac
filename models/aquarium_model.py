
from sqlalchemy import Column, Integer, String, Float, Enum, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base
from .invertebrate import Invertebrate
from .equipment import Equipment
from .fish import Fish
from .plant import Plant
from .water_parameter import WaterParameter  # Importing WaterParameter class

class Aquarium(Base):
    __tablename__ = 'aquariums'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    model = Column(String, nullable=True)
    tank_type = Column(Enum('Community', 'Species', 'Cichlid', 'Biotype', 'Breeding', 'Planted', 'Shrimp', 'Fish-only', 'Coldwater'), nullable=False)
    shape = Column(Enum('Cube/Rectangular', 'Bow-Front', 'Hexagonal', 'Cylinder', 'L-shaped', 'Pentagon', 'Column'), nullable=False)
    length = Column(Float, nullable=False)
    width = Column(Float, nullable=False)
    depth = Column(Float, nullable=False)
    capacity = Column(Float, nullable=False)
    substrate = Column(Enum('Gravel', 'Sand', 'Planted tank substrates', 'Clay-based substrates', 'Rocks', 'Fluorite', 'None'), nullable=False)
    setup_date = Column(String, nullable=True)
    price = Column(Float, nullable=True)
    supplier_id = Column(Integer, ForeignKey('suppliers.id'), nullable=False, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    picture = Column(String, nullable=True)

    # Relationships
    store = relationship('Supplier', back_populates='aquariums')
    resources = relationship('Resource', back_populates='aquarium')
    expenses = relationship('Expense', back_populates='aquarium')
    incomes = relationship('Income', back_populates='aquarium')
    user = relationship('User', back_populates='aquariums')
    fish = relationship('Fish', back_populates='aquarium', foreign_keys=[Fish.aquarium_id])
    plants = relationship('Plant', back_populates='aquarium', foreign_keys=[Plant.aquarium_id])
    invertebrates = relationship('Invertebrate', back_populates='aquarium', foreign_keys=[Invertebrate.aquarium_id])
    tasks = relationship('Task', back_populates='aquarium')
    equipment = relationship("Equipment", back_populates="aquarium")
    water_parameters = relationship("WaterParameter", back_populates="aquarium")  # Added this line

    def __init__(self, name, model, tank_type, shape, length, width, depth, capacity, substrate, setup_date=None, price=None, supplier_id=None, user_id=None, picture=None):
        self.name = name
        self.model = model
        self.tank_type = tank_type
        self.shape = shape
        self.length = length
        self.width = width
        self.depth = depth
        self.capacity = capacity
        self.substrate = substrate
        self.setup_date = setup_date
        self.price = price
        self.supplier_id = supplier_id
        self.user_id = user_id
        self.picture = picture
