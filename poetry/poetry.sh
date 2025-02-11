set -e
update() {
  poetry update --sync
}
install() {
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
current-venv(){
   poetry env info --path
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
