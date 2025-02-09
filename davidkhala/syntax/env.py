import os
import platform
from packaging import version
from davidkhala.syntax import is_windows, is_linux, is_mac
from davidkhala.syntax.path import resolve

APPDATA = {
    'Roaming': os.environ.get('APPDATA'),
    'Local': os.environ.get('LOCALAPPDATA')
}


def python_paths(major: int | str, minor: int | str) -> dict | None:
    _ = f"Python{major}{minor}"

    if is_windows():
        home = resolve(APPDATA['Local'], 'Programs', 'Python', _)

        return {
            'home': home,
            'executable': resolve(home, 'python.exe'),
        }
    elif is_linux():
        pass
    elif is_mac():
        pass


class Version:
    """
    Python version
    """

    def __init__(self):
        self.major, self.minor, self.patch = platform.python_version_tuple()

    @staticmethod
    def sem_ver() -> str:
        return platform.python_version()

    @property
    def micro(self) -> str:
        return self.patch

    @staticmethod
    def is_older_than(target_version):
        """
        Check if the current Python version is older than the specified target version.

        :param target_version: A string representing the target version (e.g., "3.8.0").
        """
        current_version = Version.sem_ver()

        return version.parse(current_version) < version.parse(target_version)
