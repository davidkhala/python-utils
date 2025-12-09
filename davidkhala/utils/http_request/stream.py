import requests
from typing import Generator
import json
from davidkhala.utils.http_request import Request as SessionRequest



def as_sse(response: requests.Response) -> Generator[dict, None, None]:
    return (json.loads(line[5:].decode()) for line in response.iter_lines() if line)


class Request(SessionRequest):
    def __init__(self, auth: dict = None):
        super().__init__(auth)
        del self.on_response


    def request(self, url, method: str, params=None, data=None, json=None) -> requests.Response:
        return self.session.request(method, url, stream= True, params=params, data=data, json=json, **self.options)
