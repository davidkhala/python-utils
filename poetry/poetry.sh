set -e
update() {
  poetry update --sync
}
install-all() {
  poetry install --all-extras
}
add() {
  #  adds required packages to your pyproject.toml and installs them.
  poetry add "$@"
}
add-dev() {
  poetry add -G dev "$@"
}
clean-venv() {
  poetry env remove --all
}
login() {
  local PYPI_TOKEN=$1
  poetry config http-basic.pypi __token__ "$PYPI_TOKEN"
}
publish() {
  poetry build
  poetry publish
}
"$@"
