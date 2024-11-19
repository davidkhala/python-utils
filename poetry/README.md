# poetry

[wiki](https://github.com/davidkhala/python-utils/wiki/Package-Management-Tools#poetry)
## Install
> Poetry should always be installed in a dedicated virtual environment to isolate it from the rest of your system.
> It should in no case be installed in the environment of the project that is to be managed by Poetry. 
> This ensures that Poetry’s own dependencies will not be accidentally upgraded or uninstalled. 

> In addition, the isolated virtual environment in which poetry is installed should not be activated for running poetry commands.

- Generic linux install `curl https://raw.githubusercontent.com/davidkhala/python-utils/refs/heads/main/poetry/poetry.sh | bash -s install`
  - It does not include path import natively. You need to handle it yourself.
- On Ubuntu: `curl https://raw.githubusercontent.com/davidkhala/ubuntu-utils/refs/heads/master/language/python.sh | bash -s poetry`




## setup
`poetry init` to initialise a pre-existing project

`poetry update --sync` to install/update dependencies
- If not found, this command will create another venv

`poetry install` compared to `poetry update` 
- Beyond dependencies, it can install current python module into context for reuse (e.g. use in tests)
- It will respect lock file

`poetry add <packagename>` adds required packages to your pyproject.toml and installs them.

## publish
- `poetry publish --build` will prompt for confirm
  - For no-interaction publish. You need `poetry build` in advanced 
- [configure credential](https://python-poetry.org/docs/repositories/#configuring-credentials)
  - for pypi: `poetry config http-basic.pypi __token__ <PYPI_TOKEN>`

## clean up
- clean up venv: `poetry env remove python` 
  - It will not cleanup cache/dependencies in interpreter 

