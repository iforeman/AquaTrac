from sqlalchemy import Column, Integer, String, Float, ForeignKey, Date, Text
from sqlalchemy.orm import relationship
from .base import Base

class Income(Base):
    __tablename__ = 'incomes'
    
    id = Column(Integer, primary_key=True)
    aquarium_id = Column(Integer, ForeignKey('aquariums.id'), nullable=False)
    date = Column(Date)
    designation = Column(String)
    amount = Column(Float)
    notes = Column(Text)

    aquarium = relationship('Aquarium', back_populates='incomes')

    def __repr__(self):
        return f"<Income(id={self.id}, designation={self.designation}, aquarium_id={self.aquarium_id})>"