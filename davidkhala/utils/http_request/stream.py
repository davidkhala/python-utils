from json import loads as json_loads
from typing import Generator, Callable, Any

import requests
from requests import Session

from davidkhala.utils.http_request import Request as SessionRequest, FileLike, FileLikeWithName


def sse_default_filter(line: bytes) -> bool:
    return bool(line) and line != b'event: ping'


def as_sse(
        response: requests.Response,
        _filter: Callable[[bytes], bool] = sse_default_filter
) -> Generator[dict, None, None]:
    for line in response.iter_lines():
        if _filter(line):
            yield json_loads(line[5:].decode())


class Request:
    def __init__(self, borrow: SessionRequest):
        super().__init__()
        self.options: dict = borrow.options
        assert borrow.session is not None
        self.session: Session = borrow.session

    def request(self, url, method: str,
                params: dict | None = None,
                data: dict | None = None,
                json: dict | None = None,
                files: dict[str, tuple[str, FileLike | Any] | FileLikeWithName | Any] | None = None
                ) -> requests.Response:
        return self.session.request(method, url,
                                    params=params, data=data, json=json, files=files,
                                    stream=True,
                                    **self.options)
