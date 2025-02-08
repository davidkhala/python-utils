import os
from enum import Enum
from typing import Callable, Iterable
import platform


class Package:
    def __init__(self, name: str):
        import re
        assert re.match('^([A-Z0-9]|[A-Z0-9][A-Z0-9._-]*[A-Z0-9])$', name, re.IGNORECASE)


class NameEnum(Enum):
    @staticmethod
    def _generate_next_value_(name, *args):
        return name


def for_each(content: Iterable, on_each: Callable[[int, str], None]):
    for index, value in enumerate(content):
        on_each(index, value)


class Version:
    def __init__(self):
        self.major, self.minor, self.patch = platform.python_version_tuple()

    @staticmethod
    def sem_ver() -> str:
        return platform.python_version()

    @property
    def micro(self) -> str:
        return self.patch


def is_windows() -> bool:
    return os.name == 'nt' or platform.system() == 'Windows'


def is_linux() -> bool:
    return platform.system() == 'Linux'


def is_mac() -> bool:
    return platform.system() == 'Darwin'
