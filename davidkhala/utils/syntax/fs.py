from os import PathLike
from pathlib import Path

from davidkhala.utils.syntax.format import JSONReadable
from davidkhala.utils.syntax.interface import Serializable


def read(path: int | str | bytes | PathLike) -> str:
    with open(path, encoding="utf-8") as file:
        return file.read()


def write(path: int | str | bytes | PathLike, data):
    if not isinstance(path, int):
        resolved = path.decode() if isinstance(path, bytes) else path
        Path(resolved).parent.mkdir(parents=True, exist_ok=True)

    with open(path, 'w') as file:
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
