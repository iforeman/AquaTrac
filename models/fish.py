from sqlalchemy import Column, Integer, String, Float, Enum, ForeignKey, Date
from sqlalchemy.orm import relationship
from .base import Base

class Fish(Base):
    __tablename__ = 'fish'
    
    id = Column(Integer, primary_key=True)
    aquarium_id = Column(Integer, ForeignKey('aquariums.id'), nullable=False)
    scientific_name = Column(String)
    common_name = Column(String)
    species = Column(String)
    origin = Column(String)
    quantity = Column(Integer)
    max_size = Column(Float)
    min_tank_size = Column(Float)
    min_temp = Column(Float)
    max_temp = Column(Float)
    kh_min = Column(Float)
    kh_max = Column(Float)
    ph_min = Column(Float)
    ph_max = Column(Float)
    species_information = Column(Text)
    aquarium_care = Column(Text)
    feeding_nutrition = Column(Text)
    diet = Column(Enum('Omnivore', 'Carnivore', 'Herbivore'))
    aquarium_type = Column(String)
    care_level = Column(Enum('Easy', 'Moderate', 'Intermediate to Expert', 'Expert'))
    temperament = Column(Enum('Peaceful', 'Semi-aggressive', 'Aggressive'))
    purchase_date = Column(Date)
    unit_price = Column(Float)
    store_id = Column(Integer, ForeignKey('stores.id'))
    death_date = Column(Date)
    sale_date = Column(Date)
    sale_price = Column(Float)
    birth_date = Column(Date)
    father_fish_id = Column(Integer, ForeignKey('fish.id'))
    mother_fish_id = Column(Integer, ForeignKey('fish.id'))
    picture = Column(String)

    aquarium = relationship('Aquarium', back_populates='fish')

    def __repr__(self):
        return f"<Fish(id={self.id}, common_name={self.common_name}, aquarium_id={self.aquarium_id})>"

    def record_birth(self, parent1, parent2):
        self.father_fish_id = parent1.id
        self.mother_fish_id = parent2.id

    def record_death(self):
        self.death_date = Date.today()

    def record_sale(self):
        self.sale_date = Date.today()