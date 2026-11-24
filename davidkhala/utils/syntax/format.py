import base64
import json
from pathlib import Path
from mimetypes import guess_type
from typing import Literal


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


def sniff_image_format(data: bytes) -> Literal["png", "jpeg", "gif", "webp", None]:
    """Detect image format from magic bytes."""
    if data.startswith(b"\x89PNG\r\n\x1a\n"):
        return "png"
    if data.startswith(b"\xff\xd8\xff"):
        return "jpeg"
    if data.startswith((b"GIF87a", b"GIF89a")):
        return "gif"
    if data[:4] == b"RIFF" and data[8:12] == b"WEBP":
        return "webp"
    return None

def data_url_of(path: Path):
    """
    :return: base64 encoded file in a data URL (aka. Data URI). RFC 2397 standard format
    """
    return f"data:{mime_of(path)};base64,{Base64.encode_file(path)}"
