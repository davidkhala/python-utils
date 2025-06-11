

# Install

```shell
curl -LsSf https://astral.sh/uv/install.sh | sh
```

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Prebuilt in container image `ghcr.io/astral-sh/uv:latest`
# usage
`uv publish --token $pypi_token`
- uv does not have equivalent to option [`--skip-existing`](https://github.com/astral-sh/uv/issues/7917)
# migrate
`uvx migrate-to-uv` support from `pip`, `poetry`, `pipenv`, `pip-tools`

# Limit
- `uv publish` cannot smartly know current version in `pyproject.toml` as the target release version. 
  - You need to make sure `/dist` only has one version  
