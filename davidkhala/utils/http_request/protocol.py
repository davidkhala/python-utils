from typing import Protocol


class RequestProtocol(Protocol):
    def request(self, url, method: str, params=None, data=None, json=None) -> Any: ...
