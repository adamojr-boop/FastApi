from fastapi import FastAPI, Query, Path
from typing import Annotated
from pydantic import BaseModel, Field

app = FastAPI()

#@app.get("/items/")
#async def read_items(q: Annotated[str | None, Query(min_length=3, max_length=50, pattern = "^fixedquery$")] = None):
#    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#    if q:
#        results.update({"q": q})
#    return results

@app.get("/items/{item_id}")
async def read_items(item_id: Annotated[int, Path(title ="The ID of the item", gt = 1, le = 1000)]):
    return {"item_id": item_id}

class FilterParams(BaseModel):
    model_config = {"extra": "forbid"}
    limit: int = Field(100, gt=0, le=100)
    offset: int = Field(0, ge=0)
    order_by: str = "Created_at"
    tags: list[str] = []

@app.get("/items/")
async def read_items(filter_query: Annotated[FilterParams, Query()]): 
    return filter_query