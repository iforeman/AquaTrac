from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Resource(Base):
    __tablename__ = 'resources'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    name = Column(String, nullable=False)
    type = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)
    unit_price = Column(Float, nullable=False)
    total_price = Column(Float, nullable=False)
    supplier_id = Column(Integer, ForeignKey('suppliers.id'), nullable=False, index=True)  # Changed from supplier_id to supplier_id
    aquarium_id = Column(Integer, ForeignKey('aquariums.id'), nullable=False)
    content = Column(String, nullable=True)

    supplier = relationship('Supplier', back_populates='resources')  # Changed from store to supplier
    aquarium = relationship('Aquarium', back_populates='resources')

    def __init__(self, title, name, type, quantity, unit_price, total_price, supplier_id, aquarium_id, content=None):
        self.title = title
        self.name = name
        self.type = type
        self.quantity = quantity
        self.unit_price = unit_price
        self.total_price = total_price
        self.supplier_id = supplier_id  # Changed from supplier_id to supplier_id
        self.aquarium_id = aquarium_id
        self.content = content

    def __repr__(self):
        return f"<Resource(id={self.id}, title='{self.title}', type='{self.type}', aquarium_id={self.aquarium_id})>"
