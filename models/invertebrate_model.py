from sqlalchemy import Column, Integer, String, Float, Enum, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Invertebrate(Base):
    __tablename__ = 'invertebrates'

    id = Column(Integer, primary_key=True, autoincrement=True)
    aquarium_id = Column(Integer, ForeignKey('aquariums.id', ondelete='CASCADE'), index=True)
    scientific_name = Column(String, nullable=False)
    common_name = Column(String, index=True, nullable=False)
    species = Column(String, index=True)
    family = Column(String, index=True)
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
    quantity = Column(Integer, nullable=False)
    size = Column(Float)
    colour = Column(String)
    diet = Column(Enum('Omnivore', 'Carnivore', 'Herbivore'))
    aquarium_type = Column(Enum('Community', 'Species', 'Cichlid', 'Biotype', 'Breeding', 'Planted', 'Shrimp', 'Fish-only', 'Coldwater'))
    temperament = Column(Enum('Peaceful', 'Semi-aggressive', 'Aggressive'))
    purchase_date = Column(String)
    unit_price = Column(Float)
    supplier_id = Column(Integer, ForeignKey('suppliers.id'), index=True)
    death_date = Column(String, nullable=True)
    sale_date = Column(String, nullable=True)
    sale_price = Column(Float, nullable=True)
    species_information = Column(String, nullable=True)
    aquarium_care = Column(String, nullable=True)
    feeding_nutrition = Column(String, nullable=True)
    birth_date = Column(String, nullable=True)
    birth_tank_id = Column(Integer, ForeignKey('aquariums.id'), nullable=True)
    picture = Column(String, nullable=True)

    aquarium = relationship('Aquarium', back_populates='invertebrates', foreign_keys=[aquarium_id])
    store = relationship('Supplier', back_populates='invertebrates')
    birth_tank = relationship('Aquarium', foreign_keys=[birth_tank_id])

    def __init__(self, aquarium_id, scientific_name, common_name, species, family, sub_family, max_size,
                 min_tank_size, min_temp, max_temp, kh_min, kh_max, ph_min, ph_max, origin, quantity,
                 size, colour, diet, aquarium_type, temperament, purchase_date, unit_price, supplier_id,
                 death_date=None, sale_date=None, sale_price=None, species_information=None,
                 aquarium_care=None, feeding_nutrition=None, birth_date=None, birth_tank_id=None, picture=None):
        self.aquarium_id = aquarium_id
        self.scientific_name = scientific_name
        self.common_name = common_name
        self.species = species
        self.family = family
        self.sub_family = sub_family
        self.max_size = max_size
        self.min_tank_size = min_tank_size
        self.min_temp = min_temp
        self.max_temp = max_temp
        self.kh_min = kh_min
        self.kh_max = kh_max
        self.ph_min = ph_min
        self.ph_max = ph_max
        self.origin = origin
        self.quantity = quantity
        self.size = size
        self.colour = colour
        self.diet = diet
        self.aquarium_type = aquarium_type
        self.temperament = temperament
        self.purchase_date = purchase_date
        self.unit_price = unit_price
        self.supplier_id = supplier_id
        self.death_date = death_date
        self.sale_date = sale_date
        self.sale_price = sale_price
        self.species_information = species_information
        self.aquarium_care = aquarium_care
        self.feeding_nutrition = feeding_nutrition
        self.birth_date = birth_date
        self.birth_tank_id = birth_tank_id
        self.picture = picture
