from typing import Set, Union

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl

app = FastAPI()


class Image(BaseModel):
    name: str
    url: HttpUrl


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    tags: Set[str] = set()
    image: Union[Image, None] = None


@app.put('/items/{item_id}')
async def update_item(item_id: int, item: Item):
    results = {}
    results.update({
        'item_id': item_id,
        'item': item
    })
    return results


if __name__ == "__main__":
    uvicorn.run("{}:app".format(__name__), reload=True)
