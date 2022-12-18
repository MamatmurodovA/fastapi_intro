from typing import Union

import uvicorn
from fastapi import FastAPI
from fastapi.params import Header

app = FastAPI()


@app.get('/items/')
async def read_items(user_agent: Union[str, None] = Header()):
    return {"User-agent": user_agent}


if __name__ == "__main__":
    uvicorn.run("{}:app".format(__name__), reload=True)
