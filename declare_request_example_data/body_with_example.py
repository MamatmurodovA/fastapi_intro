from typing import Union

import uvicorn
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


@app.put("/items/{item_id}")
async def update_item(
        item_id,
        item: Item = Body(
            example={
                "name": "Foo",
                "description": "A very nice item",
                "price": 35.4,
                "tax": 3.2
            }
        )):
    results = {"item_id": item_id, "item": item}
    return results


if __name__ == "__main__":
    uvicorn.run("{}:app".format(__name__), reload=True)