create() {
  python3 -m venv venv
  source venv/bin/activate
}
exit(){
  deactivate
}
"$@"
