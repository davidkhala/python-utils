install() {
    curl -sSL https://raw.githubusercontent.com/pdm-project/pdm/main/install-pdm.py | python3 -
}
uninstall() {
    curl -sSL https://raw.githubusercontent.com/pdm-project/pdm/main/install-pdm.py | python3 - --remove
}
$@
