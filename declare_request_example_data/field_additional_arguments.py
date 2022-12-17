from typing import Union

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


class Item(BaseModel):
    name: str = Field(example="Some title info")
    description: Union[str, None] = Field(example="Some description info")
    price: float = Field(example="10.4")
    tax: Union[float, None] = Field(example=0.55)


@app.post("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results


if __name__ == "__main__":
    uvicorn.run("{}:app".format(__name__), reload=True)
