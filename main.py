from typing import Union

from fastapi import FastAPI

my_awesome_api = FastAPI()


@my_awesome_api.get("/")
async def root():
    return {"message": "Hello World"}


@my_awesome_api.get('/items/foo')
async def foo_view(name: str = 'Michael'):
    """
    Hi, there!
    It's foo page, and we'll return dummy text.
    :return:
    """
    return "Hello, {}! It's our foo page".format(name)


