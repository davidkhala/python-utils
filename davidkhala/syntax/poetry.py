import os
from configparser import ConfigParser, UNNAMED_SECTION
from typing import cast

from davidkhala.syntax import is_windows, is_linux, is_mac
from davidkhala.syntax.env import python_paths, APPDATA
from davidkhala.syntax.path import home_resolve, resolve


def pyvenv_cfg_path():
    remains = ['pypoetry', 'venv', 'pyvenv.cfg']
    if is_windows():
        return resolve(APPDATA['Roaming'], *remains)
    elif is_linux():
        return home_resolve('.config', *remains)
    elif is_mac():
        return home_resolve('Library', 'Application Support', *remains)


def reconfigure_python(sem_ver: str):
    """
    Added from 3.13.
    For poetry 2.0.1
    :param sem_ver:
    :return:
    """
    major, minor, micro = sem_ver.split('.')
    _pyvenv_cfg_path = pyvenv_cfg_path()
    if not os.path.exists(_pyvenv_cfg_path):
        raise FileNotFoundError(f"{_pyvenv_cfg_path} not found")

    config = ConfigParser(
        allow_unnamed_section=True
    )

    config.read(_pyvenv_cfg_path)

    # Update the home and version fields
    _home, executable = python_paths(major, minor)
    _UNNAMED_SECTION = cast(str, UNNAMED_SECTION)  # type erasing TODO might not be needed in future
    config.set(_UNNAMED_SECTION, "home", _home)
    config.set(_UNNAMED_SECTION, "executable", executable)
    config.set(_UNNAMED_SECTION, "version", sem_ver)
    _command = f"{executable} -m venv --clear --without-scm-ignore-files {resolve(APPDATA['Roaming'], 'pypoetry', 'venv')}"
    config.set(_UNNAMED_SECTION, "command", _command)

    with open(_pyvenv_cfg_path, "w") as f:
        config.write(f)
