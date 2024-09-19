
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Expense(Base):
    __tablename__ = 'expenses'

    id = Column(Integer, primary_key=True, autoincrement=True)
    aquarium_id = Column(Integer, ForeignKey('aquariums.id', ondelete='CASCADE'), index=True)
    date = Column(String, index=True)
    item = Column(String)
    category = Column(String)
    supplier_id = Column(Integer, ForeignKey('suppliers.id'), index=True)
    unit_price = Column(Float)
    quantity = Column(Integer)
    total = Column(Float)
    notes = Column(String)

    aquarium = relationship('Aquarium', back_populates='expenses')
    store = relationship('Supplier', back_populates='expenses')

    def __init__(self, aquarium_id, date, item, category, supplier_id, unit_price, quantity, total, notes=None):
        self.aquarium_id = aquarium_id
        self.date = date
        self.item = item
        self.category = category
        self.supplier_id = supplier_id
        self.unit_price = unit_price
        self.quantity = quantity
        self.total = total
        self.notes = notes
