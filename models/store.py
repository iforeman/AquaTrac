from sqlalchemy import Column, Integer, String, Text, Boolean
from .base import Base


class Store(Base):
    __tablename__ = 'stores'

    id = Column(Integer, primary_key=True)
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
    notes = Column(Text)
    visibility = Column(Boolean, default=True)

    def __repr__(self):
        return f"<Store(id={self.id}, name={self.name})>"