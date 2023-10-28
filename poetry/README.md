# poetry

[wiki](https://github.com/davidkhala/python-utils/wiki/Package-Management-Tools#poetry)

## setup
`poetry init` to initialise a pre-existing project

`poetry update` to install/update dependencies
- `poetry add <packagename>[ <other-packagename> ...]` adds required packages to your pyproject.toml and installs them.
- If not found, this command will create another venv

## project structure
- [official: issue closed without resolution](https://github.com/python-poetry/poetry/issues/2252)


## publish
`poetry publish --build`
- [configure credential](https://python-poetry.org/docs/repositories/#configuring-credentials)
  - for pypi: `poetry config http-basic.pypi <username> <password>`

## clean up
1. find your environment by `poetry env list`
2. remove the environment by `poetry env remove <env-name>`

