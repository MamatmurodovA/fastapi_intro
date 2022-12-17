from typing import List

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl

app = FastAPI()


class Image(BaseModel):
    url: HttpUrl
    name: str


@app.post('/images/multiple/')
async def create_multiple_images(images: List[Image]):
    for image in images:
        print("{} - {}".format(image.name, image.url))
    return images


if __name__ == "__main__":
    uvicorn.run("{}:app".format(__name__), reload=True)
