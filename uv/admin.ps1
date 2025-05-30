$ErrorActionPreference = "Stop"
function Install
{
    powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
}
function WinGet-Install
{
    winget install --id=astral-sh.uv  -e
}
function Uninstall
{
    uv cache clean
    $python_dir = uv python dir
    if (Test-Path $python_dir)
    {
        Remove-Item $python_dir -Recurse -Force
    }

    $tool_dir = uv tool dir
    if (Test-Path $tool_dir)
    {
        Remove-Item $tool_dir -Recurse -Force
    }

    rm $HOME\.local\bin\uv.exe
    rm $HOME\.local\bin\uvx.exe
}

if ($args.Count -gt 0)
{
    Invoke-Expression ($args -join " ")
}