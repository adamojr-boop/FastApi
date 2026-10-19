from fastapi import FastAPI
from enum import Enum

app = FastAPI()

@app.get("/")
def root():
    return {"Hello": "World"}

#@app.get("/items/{item_id}")
#async def read_item(item_id: int):
#    return {"item_id": item_id}
#Parte fissa sempre prima di quella variabile
@app.get("/users/me")
async def read_user_me():
    return {"username": "me"}

@app.get("/users/{user_id}")
async def read_user(user_id: int):
    return {"user_id": user_id}

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    return {"model_name": model_name}

@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@app.get("/items/")
async def read_items(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]

##@app.get("/items/{item_id}")
#async def read_item(item_id: str, q: str | None = None):
#    if q:
#        return {"item_id": item_id, "q": q}
#    return {"item_id": item_id}

##@app.get("/items/{item_id}")
##async def read_item(item_id: str, q: str | None = None, short: bool = False):
#    item = {"item_id": item_id}
#    if q:
#        item.update({"q": q})
#    if not short:
#        item.update({"description": "This is a long description because short is False"})
#    return item

@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int, item_id: str, q: str | None = None, short: bool = False
):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update(
            {"q": q}
        )
    if not short:
        item.update(
            {"description": "This is a long description because short is False"}
        )
    return item

#@app.get("/items/{item_id}")
#async def read_user_item(item_id: str, needy: str):
#    item = {"item_id": item_id, "needy": needy}
#    return item

@app.get("/items/{item_id}")
async def read_user_item(
    item_id: str, needy: str, skip: int = 0, limit: int | None = None
):
    item = {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit}
    return item