from typing import Union
from model import Item
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.post("/create")
async def createItem(item: Item):
    item_dict = item.dict()
    item.price = item.price + 100
    #item_dict.update({"price_update":price_update})
    return item

