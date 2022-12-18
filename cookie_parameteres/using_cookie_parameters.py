from typing import Union

import uvicorn
from fastapi import FastAPI, Cookie

app = FastAPI()


@app.get('/items/')
async def read_items(ads_id: Union[str, None] = Cookie(default=None)):
    return {"ads_id": ads_id}


if __name__ == "__main__":
    uvicorn.run("{}:app".format(__name__), reload=True)
