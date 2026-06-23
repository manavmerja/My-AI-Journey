from typing import Annotated
from enum import Enum
from fastapi import FastAPI, Query, HTTPException, Header
from pydantic import BaseModel, Field
import uvicorn

app = FastAPI()

SECRET_TOKEN = "supersecret123"


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


class Item(BaseModel):
    name: str = Field(examples=["Foo"])
    description: str | None = Field(default=None, max_length=300)
    price: float = Field(gt=0, description="The price must be greater than zero")
    tax: float | None = None
    tags: list[str] = []  # Added a list of strings


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the things"}

    return {"model_name": model_name, "message": "Have some residuals"}


@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int, item_id: str, q: str | None = None, short: bool = False
):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item


@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict


@app.get("/items/")
async def read_items(q: Annotated[str | None, Query(max_length=50)] = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


@app.get("/items_multiple/")
async def read_multiple_items(q: Annotated[list[str] | None, Query()] = None):
    # This allows URLs like: /items_multiple/?q=foo&q=bar
    query_items = {"q": q}
    return query_items


    return {"User-Agent": user_agent}


@app.get("/protected/")
async def read_protected_data(x_token: Annotated[str | None, Header()] = None):
    if x_token != SECRET_TOKEN:
        raise HTTPException(status_code=403, detail="Invalid or missing X-Token")
    return {"message": "You are authorized!", "secret_data": "FastAPI is awesome!"}


@app.put("/items/{item_id}")
async def update_item(item_id: str, item: Item):
    results = {"item_name": item.name, "item_id": item_id}
    if item.price:
        results.update({"price": item.price, "tax": item.tax})
    return results


@app.get("/items/{item_id}")
async def read_item(item_id: str, q: str | None = None):
    if item_id == "foo":
        return {"item_id": "foo", "q": q}
    else:
        raise HTTPException(status_code=404, detail="Item not found")


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
