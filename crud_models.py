from crud_database import Base
from sqlalchemy import Column, Integer, String, DateTime, Boolean

# Blueprint of database
class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key = True, index = True) # index is faster for queries that filter or sort
    title = Column(String, index=True, nullable=False)
    description = Column(String, nullable= True)
    reminder_time = Column(DateTime(timezone=True), nullable=True, index=True)
    completed = Column(Boolean, default=False, nullable=False, index=True)
