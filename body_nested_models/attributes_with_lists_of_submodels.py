from typing import Union, Set, List

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl

app = FastAPI()


class Image(BaseModel):
    url: HttpUrl
    name: str


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    tags: Set[str] = set()
    images: Union[List[Image], None] = None


@app.put('/items/{item_id}')
async def update_item(item_id: int, item: Item):
    results = {}
    print(item)
    results.update(item.dict())
    return results


if __name__ == "__main__":
    uvicorn.run("{}:app".format(__name__), reload=True)
