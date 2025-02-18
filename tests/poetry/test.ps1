Describe "poetry.exe" {
    BeforeAll {
        $cliPath = Resolve-Path "./dist/poetry.exe"
        Write-Host $cliPath
    }
    It "exist" {
        Test-Path -Path $cliPath | Should -Be $true
    }
    It "reconfigure" {
        & $cliPath reconfigure "3.12.7" | Write-Host # Write-Host to redirect content in Python print(...)
    }
}

