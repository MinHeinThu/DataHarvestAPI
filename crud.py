from fastapi import FastAPI, HTTPException
from typing import List, Union, Annotated
from crud_models import TaskCreate, Task

app = FastAPI()

# --- In-Memory Database ---
# We'll store our Task objects in this list
db: List[Task] = []
current_id = 0 # This will help us generate unique IDs

# Create Post
@app.post("/tasks")
async def create_task(task_create: TaskCreate):
    global current_id # We need change to global variable 
    current_id += 1

    # 2. Create a new Task object (the "database" model)
    #    .model_dump() gets a dict of the data from task_create
    new_task = Task(id = current_id, **task_create.model_dump())
    db.append(new_task)
    return new_task

# Show all tasks
@app.get("/tasks")
async def task_list():
    return db

# Get the specific id 
@app.get("/tasks/{id}")
async def maching_task(id: int): # path parameter
    for task in db:
        if task.id == id:
            return {"title": task.title}
    raise HTTPException(status_code=404, detail="Item not found")

@app.put("/tasks/{id}")
async def update_task(id: int, task_update: TaskCreate): # path parameter and request body
    # request body = sending data from client to your server not like request
    # for task in db:
    #     if task.id == id:
    #         task.title = task_update.title
    #         task.completed = task_update.completed
    #         return task
    
    # Using enumerate we get both index and task
    for i, task in enumerate(db):
        if task.id == id:
            update_data = task_update.model_dump()

            updated_task = task.model_copy(update=update_data)
            # Replace with the index
            db[i] = updated_task
            return updated_task
    
    return HTTPException(status_code=404, detail="Item not found")

@app.delete("/tasks/{id}")
async def delete_task(id: int):
    for task in db:
        if task.id == id:
            db.remove(task)
        return {"messsage": "Task deleted successfully"}
    return HTTPException(status_code=404, detail="Item not found")
