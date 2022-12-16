from typing import Union

import uvicorn
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel, Field

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Union[str, None] = Field(
        default=None,
        title="The description of item",
        max_length=300
    )
    price: float = Field(
        gt=0,
        description="The price must be greater than zero"
    )
    tax: Union[float, None] = None


@app.put('/items/{item_id}')
async def update_item(item_id: int, item: Item = Body(embed=True)):
    results = {}
    results.update({
        'item_id': item_id,
        'item': item
    })
    return results


if __name__ == "__main__":
    uvicorn.run("{}:app".format(__name__), reload=True)
