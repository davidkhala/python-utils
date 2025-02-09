import os

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
    major, minor, micro = sem_ver.split('.')
    _pyvenv_cfg_path = pyvenv_cfg_path()
    if not os.path.exists(_pyvenv_cfg_path):
        raise FileNotFoundError(f"{_pyvenv_cfg_path} not found")

    _paths = python_paths(major, minor)
    _command = f"{_paths['executable']} -m venv --clear --without-scm-ignore-files {resolve(APPDATA['Roaming'], 'pypoetry', 'venv')}"
    target = {
        **_paths,
        "version": sem_ver,
        "command": _command,
    }

    from dotenv import dotenv_values, set_key
    dotenv_values(_pyvenv_cfg_path)  # format validate purpose

    for key, value in target.items():
        set_key(_pyvenv_cfg_path, key, value, quote_mode="never")
