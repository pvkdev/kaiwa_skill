$ErrorActionPreference = 'Stop'
$repoRoot = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path

foreach ($lesson in @(1, 39)) {
    $lessonCode = '{0:D2}' -f $lesson
    $jsonPath = Join-Path $repoRoot ("authored/lesson-{0}/listening.json" -f $lessonCode)
    $data = Get-Content -LiteralPath $jsonPath -Raw -Encoding UTF8 | ConvertFrom-Json -Depth 30
    $media = $data.sections[0].media
    $scriptJa = [string]$media.script_ja
    if ([string]::IsNullOrWhiteSpace($scriptJa)) { throw "No Japanese script in $jsonPath" }
    $mp3Path = Join-Path $repoRoot ([string]$media.local_asset)
    New-Item -ItemType Directory -Force -Path (Split-Path -Parent $mp3Path) | Out-Null
    $wavPath = Join-Path $env:TEMP ("minna-listening-{0}-{1}.wav" -f $lessonCode, [guid]::NewGuid().ToString('N'))

    $voice = New-Object -ComObject SAPI.SpVoice
    $haruka = @($voice.GetVoices() | Where-Object { $_.GetDescription() -eq 'Microsoft Haruka Desktop - Japanese' })
    if ($haruka.Count -ne 1) { throw 'Microsoft Haruka Desktop - Japanese voice is unavailable' }
    $voice.Voice = $haruka[0]
    $stream = New-Object -ComObject SAPI.SpFileStream
    $stream.Open($wavPath, 3, $false)
    try {
        $voice.AudioOutputStream = $stream
        [void]$voice.Speak($scriptJa, 0)
    }
    finally {
        $stream.Close()
    }

    & ffmpeg -hide_banner -loglevel error -y -i $wavPath -codec:a libmp3lame -b:a 64k -ac 1 -ar 22050 $mp3Path
    if ($LASTEXITCODE -ne 0) { throw "FFmpeg failed for lesson $lessonCode" }
    $sha = (Get-FileHash -LiteralPath $mp3Path -Algorithm SHA256).Hash.ToLowerInvariant()
    $duration = & ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 $mp3Path
    if ($LASTEXITCODE -ne 0) { throw "FFprobe failed for lesson $lessonCode" }
    Write-Output ("lesson={0} duration={1} sha256={2} file={3}" -f $lessonCode, $duration, $sha, $mp3Path)
}
