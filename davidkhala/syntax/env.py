import os

from davidkhala.syntax import is_windows, is_linux, is_mac
from davidkhala.syntax.path import resolve

APPDATA ={
    'Roaming':os.environ.get('APPDATA'),
    'Local': os.environ.get('LOCALAPPDATA')
}


def python_paths(major: int | str, minor: int | str) -> (str | None, str | None):
    _ = f"Python{major}{minor}"

    if is_windows():
        home = resolve(APPDATA['Local'], 'Programs', 'Python', _)

        return home, resolve(home, 'python.exe')
    elif is_linux():
        pass
    elif is_mac():
        pass
