from sqlalchemy import Column, Integer, String, ForeignKey, Date, Boolean
from sqlalchemy.orm import relationship
from .base import Base

class Task(Base):
    __tablename__ = 'tasks'
    
    id = Column(Integer, primary_key=True)
    aquarium_id = Column(Integer, ForeignKey('aquariums.id'), nullable=False)
    description = Column(String)
    due_date = Column(Date)
    completed = Column(Boolean, default=False)
    type = Column(String)
    interval = Column(Integer)
    week_day = Column(Integer)

    aquarium = relationship('Aquarium', back_populates='tasks')

    def __repr__(self):
        return f"<Task(id={self.id}, description={self.description}, aquarium_id={self.aquarium_id})>"