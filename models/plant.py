from sqlalchemy import Column, Integer, String, Float, Enum, ForeignKey, Date, Text
from sqlalchemy.orm import relationship
from .base import Base

class Plant(Base):
    __tablename__ = 'plants'
    
    id = Column(Integer, primary_key=True)
    aquarium_id = Column(Integer, ForeignKey('aquariums.id'), nullable=False)
    scientific_name = Column(String)
    common_name = Column(String)
    family = Column(String)
    origin = Column(String)
    quantity = Column(Integer)
    max_size = Column(Float)
    height = Column(Float)
    colour = Column(String)
    care_level = Column(Enum('Easy', 'Moderate', 'Intermediate to Expert', 'Expert'))
    lighting = Column(Enum('Low', 'Medium', 'Medium to High', 'High'))
    placement = Column(Enum('Foreground', 'Midground', 'Midground to Background', 'Background', 'Floating'))
    purchase_date = Column(Date)
    min_temp = Column(Float)
    max_temp = Column(Float)
    kh_min = Column(Float)
    kh_max = Column(Float)
    ph_min = Column(Float)
    ph_max = Column(Float)
    unit_price = Column(Float)
    store_id = Column(Integer, ForeignKey('stores.id'))
    multiplication_date = Column(Date)
    removal_date = Column(Date)
    removal_reason = Column(String)
    sale_date = Column(Date)
    sale_price = Column(Float)
    mother_plant_id = Column(Integer, ForeignKey('plants.id'))
    picture = Column(String)
    supplements = Column(String)
    co2 = Column(String)
    species_information = Column(Text)
    aquarium_care = Column(Text)
    feeding_nutrition = Column(Text)

    aquarium = relationship('Aquarium', back_populates='plants')

    def __repr__(self):
        return f"<Plant(id={self.id}, common_name={self.common_name}, aquarium_id={self.aquarium_id})>"

    def record_multiplication(self):
        self.multiplication_date = Date.today()

    def record_removal(self):
        self.removal_date = Date.today()