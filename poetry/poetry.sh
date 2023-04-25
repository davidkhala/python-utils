install() {
    curl -sSL https://install.python-poetry.org | python3 -
}
uninstall() {
    curl -sSL https://install.python-poetry.org | python3 - --uninstall
}
update() {
    poetry self update
}
install() {
    poetry add $1
    poetry install --no-root

}
login(){
    local username=$1
    local password=$2
    poetry config http-basic.pypi $username $password
}
$@
