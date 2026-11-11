$ErrorActionPreference = 'Stop'
Push-Location -LiteralPath $PSScriptRoot
try {
    New-Item -ItemType Directory -Force -Path 'build' | Out-Null
    foreach ($taskCompilePass in 1..2) {
        & xelatex -interaction=nonstopmode -halt-on-error -output-directory=build handout04_slides.tex > "build/compile-pass-$taskCompilePass.txt"
        if ($LASTEXITCODE -ne 0) {
            throw "XeLaTeX failed. See build/compile-pass-$taskCompilePass.txt"
        }
    }
    Copy-Item -LiteralPath 'build/handout04_slides.pdf' -Destination 'handout04_slides.pdf' -Force
    Write-Output 'Created handout04_slides.pdf'
} finally {
    Pop-Location
}
