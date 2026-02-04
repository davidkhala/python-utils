import requests
from typing import Generator, Callable
import json

from requests import Session

from davidkhala.utils.http_request import Request as SessionRequest


def sse_default_filter(line: bytes) -> bool:
    return line and line != b'event: ping'


def as_sse(
        response: requests.Response,
        _filter: Callable[[bytes], bool] = sse_default_filter
) -> Generator[dict, None, None]:
    for line in response.iter_lines():
        if _filter(line):
            yield json.loads(line[5:].decode())


class Request:
    def __init__(self, borrow: SessionRequest):
        self.options: dict = borrow.options
        self.session: Session = borrow.session

    def request(self, url, method: str, params=None, data=None, json=None) -> requests.Response:
        return self.session.request(method, url, stream=True, params=params, data=data, json=json, **self.options)
