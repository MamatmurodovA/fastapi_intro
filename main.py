from typing import Union

from fastapi import FastAPI

my_awesome_api = FastAPI()


@my_awesome_api.get("/")
async def root():
    return {"message": "Hello World"}


@my_awesome_api.get('/items/{country}')
async def foo_view(country, name: str = 'Michael'):
    """
    Hi, there!
    It's foo page, and we'll return dummy text.
    :return:
    """
    print(country)
    return "Hello, {}! Are you from {}".format(name, country)


