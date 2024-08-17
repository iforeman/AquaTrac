from sqlalchemy import Column, Integer, Float, ForeignKey, Date
from sqlalchemy.orm import relationship
from .base import Base

class WaterParameter(Base):
    __tablename__ = 'water_parameters'
    
    id = Column(Integer, primary_key=True)
    aquarium_id = Column(Integer, ForeignKey('aquariums.id'), nullable=False)
    date = Column(Date)
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

    def __repr__(self):
        return f"<WaterParameter(id={self.id}, aquarium_id={self.aquarium_id}, date={self.date})>"

    def is_in_safe_range(self):
        pass  # Implement safety check logic

    def get_trend(self, days):
        pass  # Implement trend analysis logic