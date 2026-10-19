from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

@app.get("/")
async def root():
    return {"Hello": "World"}

class Item(BaseModel):
    name: str
    description: str | None = Field(None, title = "The description of the item", max_length = 300)
    price: float = Field(..., title = "The price of the item, greater than 0", gt = 0)
    tax: float | None = None

#@app.post("/items/")
#async def create_item(item: Item):
#    return item

@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.model_dump()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})

    return item_dict

##@app.put("/items/{item_id}")
#async def update_item(item_id: int, item: Item):
#    return {"item_name": item.name, **item.model_dump()}

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item, q: str | None = None):
    result = {"item_id": item_id, **item.model_dump()}
    if q:
        result.update({"q": q})

    return result