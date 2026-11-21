[CmdletBinding()]
param(
    [string]$KotlinHome = $env:KOTLIN_HOME,
    [string]$JavaHome = $env:JAVA_HOME
)

$ErrorActionPreference = 'Stop'
$projectRoot = Split-Path -Parent $PSScriptRoot
Set-Location $projectRoot

$kotlinc = if ($KotlinHome) {
    Join-Path $KotlinHome 'bin\kotlinc.bat'
} else {
    $command = Get-Command kotlinc.bat -ErrorAction SilentlyContinue
    if ($command) { $command.Source } else { $null }
}
if (-not $kotlinc -or -not (Test-Path -LiteralPath $kotlinc)) {
    throw 'Missing kotlinc.bat. Set KOTLIN_HOME or pass -KotlinHome to a Kotlin compiler distribution.'
}

$java = if ($JavaHome) {
    Join-Path $JavaHome 'bin\java.exe'
} else {
    $command = Get-Command java.exe -ErrorAction SilentlyContinue
    if ($command) { $command.Source } else { $null }
}
if (-not $java -or -not (Test-Path -LiteralPath $java)) {
    throw 'Missing java.exe. Set JAVA_HOME or pass -JavaHome to a JDK 17+ installation.'
}

$outputDirectory = Join-Path ([System.IO.Path]::GetTempPath()) "toeic-alpha-pure-kotlin-$PID"
$jar = Join-Path $outputDirectory 'alpha-pure-core.jar'
New-Item -ItemType Directory -Path $outputDirectory | Out-Null

try {
    & $kotlinc `
        'app/src/main/java/vn/toeiclearning/alpha/domain/AlphaModels.kt' `
        'app/src/main/java/vn/toeiclearning/alpha/domain/SyntheticCatalogue.kt' `
        'tests/pure-kotlin/AlphaCoreSmokeTest.kt' `
        '-include-runtime' '-d' $jar
    if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

    & $java '-jar' $jar
    exit $LASTEXITCODE
} finally {
    if (Test-Path -LiteralPath $outputDirectory) {
        Remove-Item -LiteralPath $outputDirectory -Recurse -Force
    }
}
