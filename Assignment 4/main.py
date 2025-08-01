from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
        name: str
        price: float
        is_offer: Union[bool, None] = None

#reading root
@app.get("/")
def read_root():
        return {"Hello": "World"}

#reading the item
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
        return {"item_id": item_id, "q": q}

#updating the items
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
        return {"item_name": item.name, "item_id": item_id}