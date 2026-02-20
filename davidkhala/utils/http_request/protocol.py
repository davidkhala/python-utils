from typing import Protocol, Any


class RequestProtocol(Protocol):
    def request(self, url, method: str, params: dict = None, data: dict = None, json: dict = None,
                files: dict[str, tuple[str, ...]] = None
                ) -> Any:...
