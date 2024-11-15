# poetry

[wiki](https://github.com/davidkhala/python-utils/wiki/Package-Management-Tools#poetry)
## Install
> Poetry should always be installed in a dedicated virtual environment to isolate it from the rest of your system.
> It should in no case be installed in the environment of the project that is to be managed by Poetry. 
> This ensures that Poetry’s own dependencies will not be accidentally upgraded or uninstalled. 

> In addition, the isolated virtual environment in which poetry is installed should not be activated for running poetry commands.


## setup
`poetry init` to initialise a pre-existing project

`poetry update` to install/update dependencies
- `poetry add <packagename>[ <other-packagename> ...]` adds required packages to your pyproject.toml and installs them.
- If not found, this command will create another venv

## project structure
- [official: issue closed without resolution](https://github.com/python-poetry/poetry/issues/2252)


## publish
- `poetry publish --build` will prompt for confirm
  - For no-interaction publish. You need `poetry build` in advanced 
- [configure credential](https://python-poetry.org/docs/repositories/#configuring-credentials)
  - for pypi: `poetry config http-basic.pypi __token__ <PYPI_TOKEN>`

## clean up
1. find your environment by `poetry env list`
2. remove the environment by `poetry env remove <env-name>`

