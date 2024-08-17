from sqlalchemy import Column, Integer, String, Float, Enum, ForeignKey, Date
from sqlalchemy.orm import relationship
from .base import Base

class Aquarium(Base):
    __tablename__ = 'aquariums'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    name = Column(String(150), nullable=False)
    model = Column(String(150))
    tank_type = Column(Enum('Community', 'Species', 'Cichlid', 'Biotype', 'Breeding', 'Planted', 'Shrimp', 'Fish-only', 'Coldwater'), nullable=False)
    shape = Column(Enum('Cube/Rectangular', 'Bow-Front', 'Hexagonal', 'Cylinder', 'L-shaped', 'Pentagon', 'Column'), nullable=False)
    length = Column(Float)
    width = Column(Float)
    depth = Column(Float)
    capacity = Column(Float)
    substrate = Column(Enum('Gravel', 'Sand', 'Planted tank substrates', 'Clay-based substrates', 'Rocks', 'Fluorite', 'None'))
    setup_date = Column(Date)
    price = Column(Float)
    store_id = Column(Integer, ForeignKey('stores.id'))
    picture = Column(String)

    user = relationship('User', back_populates='aquariums')
    fish = relationship('Fish', back_populates='aquarium')
    plants = relationship('Plant', back_populates='aquarium')
    invertebrates = relationship('Invertebrate', back_populates='aquarium')
    equipment = relationship('Equipment', back_populates='aquarium')
    water_parameters = relationship('WaterParameter', back_populates='aquarium')
    expenses = relationship('Expense', back_populates='aquarium')
    incomes = relationship('Income', back_populates='aquarium')
    tasks = relationship('Task', back_populates='aquarium')

    def __repr__(self):
        return f"<Aquarium(id={self.id}, name={self.name}, user_id={self.user_id})>"

    def calculate_volume(self):
        return self.length * self.width * self.depth

    def add_fish(self, fish):
        self.fish.append(fish)

    def remove_fish(self, fish):
        self.fish.remove(fish)