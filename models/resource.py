from sqlalchemy import Column, Integer, String, Text, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Resource(Base):
    __tablename__ = 'resources'
    
    id = Column(Integer, primary_key=True)
    date = Column(Date)
    title = Column(String)
    content = Column(Text)
    category = Column(String)
    author = Column(String)
    publish_date = Column(Date)

    def __repr__(self):
        return f"<Resource(id={self.id}, title={self.title})>"