function Install-Poetry
{
    Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Force
    pip install certifi
    (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
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
    Remove-Item $env:LOCALAPPDATA\pypoetry -Recurse -Force
    (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py - --uninstall
}
function Find-Poetry
{
    Get-Command poetry
}
function Configure
{
    # TODO issue #7
    Invoke-Item $env:APPDATA/pypoetry/venv/pyvenv.cfg
}