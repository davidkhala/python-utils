from os import PathLike
from pathlib import Path
from typing import Literal

from davidkhala.utils.syntax.format import JSONReadable
from davidkhala.utils.syntax.interface import Serializable


def read(path: int | str | bytes | PathLike, *,
         mode: Literal['r', 'rb'] = 'r',
         encoding: str | None = None
         ) -> str | bytes:
    match mode:
        case 'r':
            if not encoding:
                encoding = 'utf-8'
        case 'rb':
            encoding = None

    with open(path, mode, encoding=encoding) as file:
        return file.read()


def write(path: int | str | bytes | PathLike, data: str | bytes,
          *,
          mode: Literal['w', 'wb'] = 'w',
          encoding: str | None = None
          ):
    match mode:
        case 'w':
            assert type(data) == str
            if not encoding:
                encoding = 'utf-8'
        case 'wb':
            assert type(data) == bytes
    if not isinstance(path, int):
        resolved = path.decode() if isinstance(path, bytes) else path
        Path(resolved).parent.mkdir(parents=True, exist_ok=True)

    with open(path, mode, encoding=encoding) as file:
        return file.write(data)


def write_json(data, name=None):
    if not name:
        name = str(data)
    if isinstance(data, Serializable):
        data = data.as_dict()
    write(f"{name}.json", JSONReadable(data))


def append(path: str, data):
    with open(path, mode='a') as file:
        return file.write(data)


from shutil import rmtree


def rm(path):
    rmtree(path, ignore_errors=True)
