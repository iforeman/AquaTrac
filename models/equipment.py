from sqlalchemy import Column, Integer, String, Float, Enum, ForeignKey, Date
from sqlalchemy.orm import relationship
from .base import Base

class Equipment(Base):
    __tablename__ = 'equipment'
    
    id = Column(Integer, primary_key=True)
    aquarium_id = Column(Integer, ForeignKey('aquariums.id'), nullable=False)
    type = Column(Enum('Filter', 'Light', 'Pump', 'Heater', 'Other'))
    performance_lph = Column(Float)
    model = Column(String)
    setup_date = Column(Date)
    purchase_date = Column(Date)
    store_id = Column(Integer, ForeignKey('stores.id'))
    unit_price = Column(Float)
    quantity = Column(Integer)
    total = Column(Float)
    power_input = Column(Enum('220v', '110v'))
    power_consumption = Column(Float)
    run_time_duration = Column(Float)
    maintenance_interval = Column(Integer)
    maintenance_week_day = Column(Integer)
    replacement_interval = Column(Integer)
    replacement_week_day = Column(Integer)

    aquarium = relationship('Aquarium', back_populates='equipment')

    def __repr__(self):
        return f"<Equipment(id={self.id}, type={self.type}, aquarium_id={self.aquarium_id})>"

    def schedule_maintenance(self):
        pass  # Implement scheduling logic

    def record_replacement(self):
        pass  # Implement replacement logic