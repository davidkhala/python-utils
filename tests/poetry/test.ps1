Describe "poetry.exe"{
    $cliPath = "./dist/poetry.exe"
    It "exist"{
        Test-Path -Path $cliPath | Should Be $true
    }
    It "reconfigure"{
        & $cliPath reconfigure "3.12.7" | Write-Host # Write-Host to redirect content in Python print(...)
    }
    It "clean"{

    }
}

