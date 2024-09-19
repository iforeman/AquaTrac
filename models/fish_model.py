
from sqlalchemy import Column, Integer, String, Float, Enum, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

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
    supplier_id = Column(Integer, ForeignKey('suppliers.id'), index=True)
    death_date = Column(String, nullable=True)
    sale_date = Column(String, nullable=True)
    sale_price = Column(Float, nullable=True)
    birth_date = Column(String, nullable=True)
    father_fish_id = Column(Integer, ForeignKey('fish.id'), nullable=True)
    mother_fish_id = Column(Integer, ForeignKey('fish.id'), nullable=True)
    birth_tank_id = Column(Integer, ForeignKey('aquariums.id'), nullable=True)  # Added this line
    picture = Column(String, nullable=True)

    aquarium = relationship('Aquarium', back_populates='fish', foreign_keys=[aquarium_id])
    store = relationship('Supplier', back_populates='fish')
    father_fish = relationship('Fish', remote_side=[id], foreign_keys=[father_fish_id])
    mother_fish = relationship('Fish', remote_side=[id], foreign_keys=[mother_fish_id])
    birth_tank = relationship('Aquarium', foreign_keys=[birth_tank_id])  # Added this line

    def __init__(self, aquarium_id, scientific_name, common_name, species, origin, quantity, max_size,
                 min_tank_size, min_temp, max_temp, kh_min, kh_max, ph_min, ph_max, species_information,
                 aquarium_care, feeding_nutrition, diet, aquarium_type, care_level, temperament,
                 purchase_date, unit_price, supplier_id, death_date=None, sale_date=None, sale_price=None,
                 birth_date=None, father_fish_id=None, mother_fish_id=None, birth_tank_id=None, picture=None):
        self.aquarium_id = aquarium_id
        self.scientific_name = scientific_name
        self.common_name = common_name
        self.species = species
        self.origin = origin
        self.quantity = quantity
        self.max_size = max_size
        self.min_tank_size = min_tank_size
        self.min_temp = min_temp
        self.max_temp = max_temp
        self.kh_min = kh_min
        self.kh_max = kh_max
        self.ph_min = ph_min
        self.ph_max = ph_max
        self.species_information = species_information
        self.aquarium_care = aquarium_care
        self.feeding_nutrition = feeding_nutrition
        self.diet = diet
        self.aquarium_type = aquarium_type
        self.care_level = care_level
        self.temperament = temperament
        self.purchase_date = purchase_date
        self.unit_price = unit_price
        self.supplier_id = supplier_id
        self.death_date = death_date
        self.sale_date = sale_date
        self.sale_price = sale_price
        self.birth_date = birth_date
        self.father_fish_id = father_fish_id
        self.mother_fish_id = mother_fish_id
        self.birth_tank_id = birth_tank_id  # Added this line
        self.picture = picture
