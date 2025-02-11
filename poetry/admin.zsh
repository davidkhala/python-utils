set -e
install() {
  curl -sSL https://install.python-poetry.org | python3 -
  # https://python-poetry.org/docs/main/#enable-tab-completion-for-bash-fish-or-zsh
  poetry completions zsh > ~/.zfunc/_poetry
  # TODO
  # You must then add the following lines in your ~/.zshrc, if they do not already exist:
  #   fpath+=~/.zfunc
  #   autoload -Uz compinit && compinit
}
"$@"

