from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Supplier(Base):  # Changed from Store to Supplier
    __tablename__ = 'suppliers'  # Changed from stores to suppliers

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    address = Column(String)
    address2 = Column(String)
    postal_code = Column(String)
    city = Column(String)
    country = Column(String)
    phone = Column(String)
    email = Column(String)
    website = Column(String)
    contact1 = Column(String)
    contact2 = Column(String)
    notes = Column(String)
    visibility = Column(Boolean, default=True)

    # Relationships
    aquariums = relationship('Aquarium', back_populates='supplier')
    resources = relationship('Resource', back_populates='supplier')
    invertebrates = relationship('Invertebrate', back_populates='supplier')
    equipment = relationship('Equipment', back_populates='supplier')
    fish = relationship('Fish', back_populates='supplier')
    plants = relationship('Plant', back_populates='supplier')
    expenses = relationship('Expense', back_populates='supplier')
    incomes = relationship('Income', back_populates='supplier')

    def __init__(self, name, address=None, address2=None, postal_code=None, city=None,
                 country=None, phone=None, email=None, website=None, contact1=None,
                 contact2=None, notes=None, visibility=True):
        self.name = name
        self.address = address
        self.address2 = address2
        self.postal_code = postal_code
        self.city = city
        self.country = country
        self.phone = phone
        self.email = email
        self.website = website
        self.contact1 = contact1
        self.contact2 = contact2
        self.notes = notes
        self.visibility = visibility
