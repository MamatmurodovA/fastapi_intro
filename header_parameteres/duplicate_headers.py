from typing import Union, List

import uvicorn
from fastapi import FastAPI
from fastapi.params import Header

app = FastAPI()


@app.get('/items/')
async def read_items(x_token: Union[List[str], None] = Header(default=None)):
    return {"X-Token values": x_token}


if __name__ == "__main__":
    uvicorn.run("{}:app".format(__name__), reload=True)
