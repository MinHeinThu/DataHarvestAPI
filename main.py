from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get("/") # api route
async def read_root():
    home  = {'home': "Welcome Home"}
    return home

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q" : q}