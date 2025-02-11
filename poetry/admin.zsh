set -e
install() {
  pip3 install certifi
  curl -sSL https://install.python-poetry.org | python3 -
  # https://python-poetry.org/docs/main/#enable-tab-completion-for-bash-fish-or-zsh
  echo "fpath+=~/.zfunc" > ~/.zshrc
  echo "autoload -Uz compinit && compinit" >/.zshrc
  mkdir  ~/.zfunc/
  poetry completions zsh > ~/.zfunc/_poetry

}
"$@"

