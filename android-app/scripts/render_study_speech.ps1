param(
    [Parameter(Mandatory=$true)][string] $Plan,
    [Parameter(Mandatory=$true)][string] $Output
)
$ErrorActionPreference = 'Stop'
Add-Type -AssemblyName System.Speech
$synth = New-Object System.Speech.Synthesis.SpeechSynthesizer
$format = [System.Speech.AudioFormat.SpeechAudioFormatInfo]::new(
    44100, [System.Speech.AudioFormat.AudioBitsPerSample]::Sixteen, [System.Speech.AudioFormat.AudioChannel]::Mono
)
$voices = @{ M = 'Microsoft David Desktop'; W = 'Microsoft Zira Desktop' }
try {
    $synth.Rate = -1
    $clips = Get-Content -LiteralPath $Plan -Raw -Encoding utf8 | ConvertFrom-Json
    foreach ($clip in $clips) {
        if ($clip.id -notmatch '^P[1-4]-(G)?[0-9]+$') { throw 'Invalid audio clip ID' }
        for ($index = 0; $index -lt $clip.turns.Count; $index++) {
            $turn = $clip.turns[$index]
            $synth.SelectVoice($voices[$turn[0]])
            $synth.SetOutputToWaveFile((Join-Path $Output "$($clip.id)-$index.wav"), $format)
            $synth.Speak([string] $turn[1])
            $synth.SetOutputToNull()
        }
    }
} finally {
    $synth.Dispose()
}
