function Install-Poetry {
  (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
}
