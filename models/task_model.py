from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from .base import Base


class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, autoincrement=True)
    aquarium_id = Column(Integer, ForeignKey('aquariums.id'), nullable=False)
    description = Column(String)
    due_date = Column(String)  # Changed from Date to String
    completed = Column(Boolean, default=False)
    type = Column(String)
    interval = Column(Integer)
    week_day = Column(Integer)

    aquarium = relationship('Aquarium', back_populates='tasks')  # Added this line

    def __init__(self, aquarium_id, description=None, due_date=None, completed=False, type=None,
                 interval=None, week_day=None):
        self.aquarium_id = aquarium_id
        self.description = description
        self.due_date = due_date
        self.completed = completed
        self.type = type
        self.interval = interval
        self.week_day = week_day