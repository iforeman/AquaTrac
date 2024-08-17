from sqlalchemy import Column, Integer, String, Float, ForeignKey, Date, Text
from sqlalchemy.orm import relationship
from .base import Base

class Expense(Base):
    __tablename__ = 'expenses'
    
    id = Column(Integer, primary_key=True)
    aquarium_id = Column(Integer, ForeignKey('aquariums.id'), nullable=False)
    date = Column(Date)
    item = Column(String)
    category = Column(String)
    store_id = Column(Integer, ForeignKey('stores.id'))
    unit_price = Column(Float)
    quantity = Column(Integer)
    total = Column(Float)
    notes = Column(Text)

    aquarium = relationship('Aquarium', back_populates='expenses')

    def __repr__(self):
        return f"<Expense(id={self.id}, item={self.item}, aquarium_id={self.aquarium_id})>"