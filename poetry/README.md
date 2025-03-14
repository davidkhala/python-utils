# poetry

[wiki](https://github.com/davidkhala/python-utils/wiki/Package-Management-Tools#poetry)
## [Install](https://python-poetry.org/docs/master/#installing-with-the-official-installer)
> It should in no case be installed in the environment of the project that is to be managed by Poetry. 
> This ensures that Poetry’s own dependencies will not be accidentally upgraded or uninstalled. 
> The isolated virtual environment in which poetry is installed should not be activated for running poetry commands.


Linux: 
- It does not include path import natively. You need to handle it yourself.
```bash
curl https://raw.githubusercontent.com/davidkhala/python-utils/refs/heads/main/poetry/admin.sh | bash -s install
```
- Ubuntu
  ```bash
  curl https://raw.githubusercontent.com/davidkhala/ubuntu-utils/refs/heads/master/language/python.sh | bash -s poetry
  ```

## Rebase
To change a python version
1. `poetry self update`
2. for non-linux, see in `davidkhala.syntax.poetry.__init__.py#reconfigure_python`
3. Clear-venv

# Usage

## In GitHub workflow
- uses: snok/install-poetry@main
  - In Powershell(`poetry`), bin not in path: `& "$env:APPDATA\Python\Scripts\poetry"`
  - In shell=`bash`: use poetry  

## setup
`poetry init` to initialise a pre-existing project

`poetry update --sync` to install/update dependencies
- If not found, this command will create another venv
```bash
curl https://raw.githubusercontent.com/davidkhala/python-utils/refs/heads/main/poetry/poetry.sh | bash -s update
```

`poetry install --no-root` compared to `poetry update` 
- Beyond dependencies, it can install current python module into context for reuse (e.g. use in tests)
- It will respect lock file
### non package mode
by specify `package-mode = false` under section `[tool.poetry]`

You can
- skip requirements to specify mandatory `name`, `version`, `description` or `authors` value in section

While you cannot
- define scripts in the [tool.poetry.scripts] section
- reference and import you local python module


## publish
- `poetry publish --build` will prompt for confirm
  - For no-interaction publish. You need `poetry build` in advanced
- `poetry publish --skip-existing` can ignore error on existing version
- [configure credential](https://python-poetry.org/docs/repositories/#configuring-credentials)
  - for pypi: `poetry config http-basic.pypi __token__ <PYPI_TOKEN>`

## clean up
clean up venv: `poetry env remove --all`
- It will not clean up cache/dependencies in interpreter

