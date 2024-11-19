set -e
install() {
  curl -sSL https://install.python-poetry.org | python3 -
}
uninstall() {
  curl -sSL https://install.python-poetry.org | python3 - --uninstall
}
upgrade() {
  poetry self update
}
"$@"