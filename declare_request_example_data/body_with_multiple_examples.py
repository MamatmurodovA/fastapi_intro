from typing import Union

import uvicorn
from fastapi import FastAPI
from fastapi.params import Body, Query, Param, Path
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


@app.put("/items/{item_id}")
async def update_item(
        *,
        item_id: int = Path(
            examples={
                "available_item": {
                    "summary": "it's `item_id` path example",
                    "description": "Item with `item_id` id exists.",
                    "value": 5
                },
                "not_available_item": {
                    "summary": "it's `item_id` path example",
                    "description": "Item with `item_id` id does not exist.",
                    "value": -1
                }
            }
        ),
        item: Item = Body(
            examples={
                "normal": {
                    "summary": "A normal example",
                    "description": "A **normal** item works correctly.",
                    "value": {
                        "name": "Foo",
                        "description": "A very nice Item",
                        "price": 35.4,
                        "tax": 3.2,
                    },
                },
                "converted": {
                    "summary": "An example with converted data",
                    "description": "FastAPI can convert price `strings` to actual `numbers` automatically",
                    "value": {
                        "name": "Bar",
                        "price": "35.4",
                    },
                },
                "invalid": {
                    "summary": "Invalid data is rejected with an error",
                    "value": {
                        "name": "Baz",
                        "price": "thirty five point four",
                    },
                },
            }
        ),
        q: str = Query(examples={
            "positive": {
                "summary": "it's example of positive number",
                "description": "It's description of query `q` for positive number",
                "value": 123
            },
            "negative": {
                "summary": "it's example of negative number",
                "description": "It's description of query `q` for negative number",
                "value": -44
            }
        })
):
    results = {"item_id": item_id, "item": item, "q": q}
    return results


if __name__ == "__main__":
    uvicorn.run("{}:app".format(__name__), reload=True)
