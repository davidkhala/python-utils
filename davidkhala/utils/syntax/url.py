import os
from urllib.parse import urlparse


def filename_from(url: str):
    return os.path.basename(urlparse(url).path)
