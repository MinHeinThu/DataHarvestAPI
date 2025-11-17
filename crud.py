from fastapi import FastAPI, Depends, HTTPException
from typing import List
import crud_models
from crud_schemas import TaskCreate, TaskResponse
from crud_database import engine, SessionLocal
from sqlalchemy.orm import Session

crud_models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal() # Open new a window 
    try:
        yield db # Let endpoint use this window
    finally:
        db.close() # Close window 

@app.post("/tasks", response_model=TaskResponse) 
async def create_task(task: TaskCreate, db: Session = Depends(get_db)):

    # Sqlalchemy model instance(copy of object)
    db_task = crud_models.Task(**task.model_dump())

    # add to the session (the staging area)
    db.add(db_task)

    # commit to the database (save permanently)
    db.commit()

    # Refresh the instance
    #    This fetches the new ID and any default values (like 'completed=False')
    #    from the database back into our 'db_task' object.
    db.refresh(db_task)

    # Return the complete object (FastAPI converts to it to Json)
    return db_task

@app.get("/tasks", response_model=List[TaskResponse])
async def tasks_list(db: Session = Depends(get_db)):

    # query all data from database
    # 1. This is the SQLAlchemy query.
    #    It means: "Query the Task model (table) and get .all() results."
    
    tasks = db.query(crud_models.Task).all()

    # 2. FastAPI automatically converts each item in the 'tasks' list
    #    into JSON using your TaskResponse model (because of 'from_attributes = True').
    return tasks

@app.get("/tasks/{task_id}", response_model=List[TaskResponse])
async def ge_task(task_id: int, db: Session = Depends(get_db)):
    # 2. This is the efficient query:
    #    - .query(): Start a query
    #    - .filter(): Ask the DB to find where the Task.id column == task_id
    #    - .first(): Stop as soon as you find one and return it.
    task = db.query(crud_models.Task).filter(crud_models.Task.id == task_id).first()

    # If the database returns None (it wasn't found), raise a 404
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    
    # If we found it, return the task object.
    # FastAPI will handle the conversion.
    return task

@app.put("/tasks/{task_id}", response_model=TaskResponse)
async def update_task(task_id: int, task_update: TaskCreate, db: Session = Depends(get_db)):
    
    task_in_db = db.query(crud_models.Task).filter(crud_models.Task.id == task_id).first()
    if task_in_db is None:
        return HTTPException(status_code=404, detail="Task not found")
    
    # task_in_db.title = task_update.title
    # task_in_db.description = task_update.description
    # task_in_db.reminder_time = task_update.reminder_time
    # task_in_db.completed = task_update.completed
    update_data = task_update.model_dump()

    for key, value in update_data.items():
        setattr (task_in_db, key, value)

    db.commit() # Change in database

    # REFRESH the object to get the updated data from the DB
    db.refresh(task_in_db)

    return task_in_db

@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int, db: Session = Depends(get_db)):
    task_in_db = db.query(crud_models.Task).filter(crud_models.Task.id == task_id).first()
    if task_in_db is None:
        raise HTTPException(status_code=404, detail="Task not found")
    
    db.delete(task_in_db)

    db.commit()

    return {"message": "Task deleted successfully"}