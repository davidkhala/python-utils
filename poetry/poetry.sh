install() {
  curl -sSL https://install.python-poetry.org | python3 -
}
uninstall() {
  curl -sSL https://install.python-poetry.org | python3 - --uninstall
}
update() {
  poetry self update
}
update-lock() {
  poetry update
}
install-package() {
  poetry add $1
  poetry install --no-root
}
clean-venv() {
  poetry env remove --all
}
login() {
  local username=$1
  local password=$2
  poetry config http-basic.pypi $username $password
}
publish() {
  poetry publish --build
}
$@
