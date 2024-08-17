from sqlalchemy import Column, Integer, String, Float, Enum, ForeignKey, Date, Text
from sqlalchemy.orm import relationship
from .base import Base

class Invertebrate(Base):
    __tablename__ = 'invertebrates'
    
    id = Column(Integer, primary_key=True)
    aquarium_id = Column(Integer, ForeignKey('aquariums.id'), nullable=False)
    scientific_name = Column(String)
    common_name = Column(String)
    species = Column(String)
    family = Column(String)
    sub_family = Column(String)
    max_size = Column(Float)
    min_tank_size = Column(Float)
    min_temp = Column(Float)
    max_temp = Column(Float)
    kh_min = Column(Float)
    kh_max = Column(Float)
    ph_min = Column(Float)
    ph_max = Column(Float)
    origin = Column(String)
    quantity = Column(Integer)
    size = Column(Float)
    colour = Column(String)
    diet = Column(Enum('Omnivore', 'Carnivore', 'Herbivore'))
    aquarium_type = Column(String)
    temperament = Column(Enum('Peaceful', 'Semi-aggressive', 'Aggressive'))
    purchase_date = Column(Date)
    unit_price = Column(Float)
    store_id = Column(Integer, ForeignKey('stores.id'))
    death_date = Column(Date)
    sale_date = Column(Date)
    sale_price = Column(Float)
    species_information = Column(Text)
    aquarium_care = Column(Text)
    feeding_nutrition = Column(Text)
    birth_date = Column(Date)
    birth_tank_id = Column(Integer, ForeignKey('aquariums.id'))
    picture = Column(String)

    aquarium = relationship('Aquarium', back_populates='invertebrates')

    def __repr__(self):
        return f"<Invertebrate(id={self.id}, common_name={self.common_name}, aquarium_id={self.aquarium_id})>"