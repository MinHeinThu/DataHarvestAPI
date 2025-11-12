from pydantic import BaseModel
from crud_database import Base

# --- Models ---

class TaskCreate(BaseModel):
    title: str
    completed: bool = False

class Task(BaseModel):
    id: int
    title: str
    completed: bool = False
