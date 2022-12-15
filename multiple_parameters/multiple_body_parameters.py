from typing import Union

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


class User(BaseModel):
    username: str
    full_name: Union[str, None] = None


@app.put('/items/{item_id}')
async def update_item(item_id: int, item: Item, user: User):
    result = {
        "item_id": item_id,
        "item": item,
        "user": user
    }
    return result


if __name__ == "__main__":
    uvicorn.run("{}:app".format(__name__), reload=True)

