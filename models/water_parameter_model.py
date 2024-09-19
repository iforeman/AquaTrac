
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class WaterParameter(Base):
    __tablename__ = 'water_parameters'

    id = Column(Integer, primary_key=True, autoincrement=True)
    aquarium_id = Column(Integer, ForeignKey('aquariums.id', ondelete='CASCADE'), index=True)
    date = Column(String, index=True)
    temperature_min = Column(Float)
    temperature_max = Column(Float)
    ph_min = Column(Float)
    ph_max = Column(Float)
    gh_min = Column(Float)
    gh_max = Column(Float)
    kh_min = Column(Float)
    kh_max = Column(Float)
    nitrite_min = Column(Float)
    nitrite_max = Column(Float)
    nitrate_min = Column(Float)
    nitrate_max = Column(Float)
    ammonium_min = Column(Float)
    ammonium_max = Column(Float)
    copper_min = Column(Float)
    copper_max = Column(Float)
    oxygen_min = Column(Float)
    oxygen_max = Column(Float)
    conductivity_min = Column(Float)
    conductivity_max = Column(Float)
    phosphate_min = Column(Float)
    phosphate_max = Column(Float)
    iron_min = Column(Float)
    iron_max = Column(Float)
    co2_min = Column(Float)
    co2_max = Column(Float)
    chlorine_min = Column(Float)
    chlorine_max = Column(Float)

    aquarium = relationship('Aquarium', back_populates='water_parameters')

    def __init__(self, aquarium_id, date, temperature_min=None, temperature_max=None, ph_min=None, ph_max=None,
                 gh_min=None, gh_max=None, kh_min=None, kh_max=None, nitrite_min=None, nitrite_max=None,
                 nitrate_min=None, nitrate_max=None, ammonium_min=None, ammonium_max=None, copper_min=None,
                 copper_max=None, oxygen_min=None, oxygen_max=None, conductivity_min=None, conductivity_max=None,
                 phosphate_min=None, phosphate_max=None, iron_min=None, iron_max=None, co2_min=None, co2_max=None,
                 chlorine_min=None, chlorine_max=None):
        self.aquarium_id = aquarium_id
        self.date = date
        self.temperature_min = temperature_min
        self.temperature_max = temperature_max
        self.ph_min = ph_min
        self.ph_max = ph_max
        self.gh_min = gh_min
        self.gh_max = gh_max
        self.kh_min = kh_min
        self.kh_max = kh_max
        self.nitrite_min = nitrite_min
        self.nitrite_max = nitrite_max
        self.nitrate_min = nitrate_min
        self.nitrate_max = nitrate_max
        self.ammonium_min = ammonium_min
        self.ammonium_max = ammonium_max
        self.copper_min = copper_min
        self.copper_max = copper_max
        self.oxygen_min = oxygen_min
        self.oxygen_max = oxygen_max
        self.conductivity_min = conductivity_min
        self.conductivity_max = conductivity_max
        self.phosphate_min = phosphate_min
        self.phosphate_max = phosphate_max
        self.iron_min = iron_min
        self.iron_max = iron_max
        self.co2_min = co2_min
        self.co2_max = co2_max
        self.chlorine_min = chlorine_min
        self.chlorine_max = chlorine_max
