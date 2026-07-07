from typing import Any, Protocol

from requests import Session, Response, request
from requests.auth import HTTPBasicAuth

from davidkhala.utils.syntax.interface import ContextAware


def default_on_response(response: Response) -> dict | list | None:
    """
    :param response:
    :return: the input response
    :raise HTTPError: if not response.ok
    """
    if response.ok:
        if response.text: return response.json()
        return None
    else:
        response.raise_for_status()
        assert False  # dead code

class FileLike(Protocol):
    def read(self, n: int = -1) -> bytes: ...
class FileLikeWithName(FileLike):
    name: str

class Request(ContextAware):
    def __init__(self, auth: dict = None, on_response=default_on_response):
        super().__init__()
        self.options: dict = {"headers": {}}
        if auth is not None:
            bearer = auth.get("bearer")
            if bearer is not None:
                self.set_bearer(bearer)
                del auth["bearer"]
            else:
                self.options["auth"] = HTTPBasicAuth(auth["username"], auth["password"])
        self.session: Session | None = None
        self.on_response = on_response

    def set_bearer(self, token):
        self.options["headers"]["Authorization"] = f"Bearer {token}"

    def open(self) -> bool:
        self.session = Session()
        return True

    def close(self):
        if self.session:
            self.session.close()
            del self.session

    def request(self, url, method: str,
                params: dict | None = None,
                data: dict | None = None,  # for application/x-www-form-urlencoded
                json: dict | None = None,
                files: dict[str, tuple[str, FileLike]|FileLikeWithName] | None = None
                ) -> Any:
        if self.session:
            response = self.session.request(method, url,
                                            params=params, data=data, json=json, files=files,
                                            **self.options)
        else:
            response = request(
                method, url, params=params, data=data, json=json, files=files, **self.options
            )
        return self.on_response(response)
