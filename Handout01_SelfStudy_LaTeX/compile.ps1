$ErrorActionPreference = 'Stop'
Push-Location -LiteralPath $PSScriptRoot
try {
    New-Item -ItemType Directory -Force -Path 'build' | Out-Null
    foreach ($taskCompilePass in 1..2) {
        & xelatex -interaction=nonstopmode -halt-on-error -output-directory=build handout01_slides.tex > "build/compile-pass-$taskCompilePass.txt"
        if ($LASTEXITCODE -ne 0) {
            throw "XeLaTeX failed. See build/compile-pass-$taskCompilePass.txt"
        }
    }
    Copy-Item -LiteralPath 'build/handout01_slides.pdf' -Destination 'handout01_slides.pdf' -Force
    Write-Output 'Created handout01_slides.pdf'
} finally {
    Pop-Location
}
