function Install-Poetry
{
    (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
    Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Force
    (Invoke-WebRequest -Uri https://raw.githubusercontent.com/davidkhala/windows-utils/master/powershell.ps1 -UseBasicParsing).Content | Invoke-Expression
    Add-Path $env:APPDATA\Python\Scripts
    Add-Path $env:APPDATA\Python\Scripts User # need admin to configure `Machine` as replacement of `User`
        
    poetry --version

}
function Clear-venv{
    # keep the folder
    Get-ChildItem $env:LOCALAPPDATA\pypoetry\Cache\virtualenvs | Remove-Item -Recurse -Force
}
function Uninstall-Poetry
{
    Clear-venv

    (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py - --uninstall
}
function Find-Poetry
{
    Get-Command poetry
}
function Configure
{
    # TODO issue #7
    code $env:APPDATA/pypoetry/venv/pyvenv.cfg
}