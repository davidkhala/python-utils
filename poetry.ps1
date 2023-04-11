function Install-Poetry {
  (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
  
  (Invoke-WebRequest https://raw.githubusercontent.com/davidkhala/windows-utils/master/powershell.ps1).Content | Add-Path ()
}
function Uninstall-Poetry {
  (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py - --uninstall
}
