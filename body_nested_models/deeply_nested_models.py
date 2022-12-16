from typing import Union, Set, List

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
    images: Union[List[Image], None] = None


class Offer(BaseModel):
    name: str
    description: Union[str, None] = None
    items: Union[List[Item], None] = None


@app.post('/items/')
def create_offer(offer: Offer):
    results = {}
    return results


if __name__ == "__main__":
    uvicorn.run("{}:app".format(__name__), reload=True)
