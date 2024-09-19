
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Enum
from sqlalchemy.orm import relationship
from .base import Base

class Equipment(Base):
    __tablename__ = 'equipment'

    id = Column(Integer, primary_key=True, autoincrement=True)
    aquarium_id = Column(Integer, ForeignKey('aquariums.id', ondelete='CASCADE'), index=True)
    type = Column(String)  # Changed from Enum to String
    supplier_id = Column(Integer, ForeignKey('suppliers.id'), index=True)
    performance_lph = Column(Float)
    model = Column(String)
    setup_date = Column(String)
    purchase_date = Column(String)
    unit_price = Column(Float)
    quantity = Column(Integer)
    total = Column(Float)
    power_input = Column(Float)
    power_consumption = Column(Float)
    run_time_duration = Column(Float)
    maintenance_interval = Column(Integer)
    maintenance_week_day = Column(Integer)
    replacement_interval = Column(Integer)
    replacement_week_day = Column(Integer)

    aquarium = relationship('Aquarium', back_populates='equipment')  # This line is correct
    store = relationship('Supplier', back_populates='equipment')

    def __init__(self, aquarium_id, type, supplier_id, performance_lph, model, setup_date, purchase_date,
                 unit_price, quantity, total, power_input, power_consumption, run_time_duration,
                 maintenance_interval=None, maintenance_week_day=None, replacement_interval=None,
                 replacement_week_day=None):
        self.aquarium_id = aquarium_id
        self.type = type
        self.supplier_id = supplier_id
        self.performance_lph = performance_lph
        self.model = model
        self.setup_date = setup_date
        self.purchase_date = purchase_date
        self.unit_price = unit_price
        self.quantity = quantity
        self.total = total
        self.power_input = power_input
        self.power_consumption = power_consumption
        self.run_time_duration = run_time_duration
        self.maintenance_interval = maintenance_interval
        self.maintenance_week_day = maintenance_week_day
        self.replacement_interval = replacement_interval
        self.replacement_week_day = replacement_week_day
