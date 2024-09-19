
from sqlalchemy import Column, Integer, String, Float, Enum, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    password_hash = Column(String, nullable=True)  # Added password_hash

    # Relationship to Aquarium
    aquariums = relationship('Aquarium', back_populates='user')

    def __init__(self, username, email, password, password_hash=None):
        self.username = username
        self.email = email
        self.password = password
        self.password_hash = password_hash  # Store password_hash
