from requests import Response

from davidkhala.utils.http_request import default_on_response


def debug(response: Response) -> dict | list | None:
    if not response.ok:
        print(response.text)
    return default_on_response(response)


def file(response: Response) -> bytes:
    if response.ok:
        return response.content
    else:
        response.raise_for_status()
        assert False  # dead code
