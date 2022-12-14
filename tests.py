import requests


def test_main():
    req = requests.get('http://127.0.0.1:8000/')
    assert req.status_code == 200
    assert req.json() == {"message": "Hello World"}


