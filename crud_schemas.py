from pydantic import BaseModel
from datetime import datetime 

# Data validation from user (Input)
class TaskCreate(BaseModel):
    title: str
    description: str | None = None
    reminder_time: datetime | None = None
    completed: bool = False

# ORM model to Json (Output)
class TaskResponse(BaseModel):
    id: int
    title: str
    description: str | None = None
    reminder_time: datetime | None = None
    completed: bool = False

    class Config: # permession to read from that database objects
        from_attributes = True