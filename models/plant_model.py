from sqlalchemy import Column, Integer, String, Float, Enum, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Plant(Base):
    __tablename__ = 'plants'

    id = Column(Integer, primary_key=True, autoincrement=True)
    aquarium_id = Column(Integer, ForeignKey('aquariums.id', ondelete='CASCADE'), index=True)
    scientific_name = Column(String, nullable=False)
    common_name = Column(String, index=True, nullable=False)
    family = Column(String, index=True)
    origin = Column(String)
    quantity = Column(Integer, nullable=False)
    max_size = Column(Float)
    height = Column(Float)
    colour = Column(String)
    care_level = Column(Enum('Easy', 'Moderate', 'Intermediate to Expert', 'Expert'))
    lighting = Column(Enum('Low', 'Medium', 'Medium to High', 'High'))
    placement = Column(Enum('Foreground', 'Midground', 'Midground to Background', 'Background', 'Floating'))
    purchase_date = Column(String)
    min_temp = Column(Float)
    max_temp = Column(Float)
    kh_min = Column(Float)
    kh_max = Column(Float)
    ph_min = Column(Float)
    ph_max = Column(Float)
    unit_price = Column(Float)
    supplier_id = Column(Integer, ForeignKey('suppliers.id'), index=True)  # Changed from supplier_id to supplier_id
    multiplication_date = Column(String, nullable=True)
    removal_date = Column(String, nullable=True)
    removal_reason = Column(String, nullable=True)
    sale_date = Column(String, nullable=True)
    sale_price = Column(Float, nullable=True)
    mother_plant_id = Column(Integer, ForeignKey('plants.id'), nullable=True)
    birth_tank_id = Column(Integer, ForeignKey('aquariums.id'), nullable=True)
    picture = Column(String, nullable=True)
    supplements = Column(String, nullable=True)
    co2 = Column(String, nullable=True)
    species_information = Column(String, nullable=True)
    aquarium_care = Column(String, nullable=True)
    feeding_nutrition = Column(String, nullable=True)

    aquarium = relationship('Aquarium', back_populates='plants', foreign_keys=[aquarium_id])
    supplier = relationship('Supplier', back_populates='plants')  # Changed from store to supplier
    mother_plant = relationship('Plant', remote_side=[id])
    birth_tank = relationship('Aquarium', foreign_keys=[birth_tank_id])

    def __init__(self, aquarium_id, scientific_name, common_name, family, origin, quantity, max_size,
                 height, colour, care_level, lighting, placement, purchase_date, min_temp, max_temp,
                 kh_min, kh_max, ph_min, ph_max, unit_price, supplier_id, multiplication_date=None,
                 removal_date=None, removal_reason=None, sale_date=None, sale_price=None,
                 mother_plant_id=None, birth_tank_id=None, picture=None, supplements=None, co2=None,
                 species_information=None, aquarium_care=None, feeding_nutrition=None):
        # ... (rest of the init method remains the same, just change supplier_id to supplier_id)
        self.supplier_id = supplier_id
        # ...
