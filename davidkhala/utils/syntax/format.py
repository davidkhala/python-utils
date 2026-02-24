import base64
import json
from pathlib import Path
from mimetypes import guess_type


def mime_of(file: Path | str) -> str:
    """
    :param file: Path or url
    """
    mime, encoding = guess_type(file)
    assert encoding in ['gzip', 'compress', 'bzip2', 'xz', 'br', 'zstd', None]
    return mime


def JSONReadable(data):
    return json.dumps(data, indent=4, sort_keys=True)


class Package:
    def __init__(self, name: str):
        import re
        assert re.match('^([A-Z0-9]|[A-Z0-9][A-Z0-9._-]*[A-Z0-9])$', name, re.IGNORECASE)


class Base64:
    @staticmethod
    def encode_file(file: Path):
        with open(file, "rb") as f:
            return Base64.encode(f.read())

    @staticmethod
    def encode(data: bytes):
        return base64.b64encode(data).decode('utf-8')
