from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Income(Base):
    __tablename__ = 'incomes'

    id = Column(Integer, primary_key=True, autoincrement=True)
    aquarium_id = Column(Integer, ForeignKey('aquariums.id', ondelete='CASCADE'), index=True)
    date = Column(String, index=True)
    designation = Column(String)
    amount = Column(Float)
    notes = Column(String, nullable=True)  # Added nullable=True for consistency
    supplier_id = Column(Integer, ForeignKey('suppliers.id'), index=True)

    store = relationship('Supplier', back_populates='incomes')
    aquarium = relationship('Aquarium', back_populates='incomes')

    def __init__(self, aquarium_id, date, designation, amount, supplier_id, notes=None):
        self.aquarium_id = aquarium_id
        self.date = date
        self.designation = designation
        self.amount = amount
        self.supplier_id = supplier_id
        self.notes = notes
