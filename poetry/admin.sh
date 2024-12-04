set -e
install() {
  curl -sSL https://install.python-poetry.org | python3 -
  # https://python-poetry.org/docs/main/#enable-tab-completion-for-bash-fish-or-zsh
  poetry completions bash >>~/.bash_completion
}
uninstall() {
  curl -sSL https://install.python-poetry.org | python3 - --uninstall
}
upgrade() {
  poetry self update
}
"$@"
