param(
    [string]$Root = (Split-Path -Parent $PSScriptRoot),
    [string]$FeedUrl,
    [string]$RssFile,
    [switch]$UseSavedFeed,
    [switch]$ReplaceEpisode,
    [string]$PreviewPath
)
$ErrorActionPreference = 'Stop'
$Root = (Resolve-Path -LiteralPath $Root).Path
$excel = Join-Path $Root 'JLPT_AUDIO.xlsx'
$runtime = $env:JLPT_WORKSPACE_DEPENDENCIES
if (-not $runtime) {
    $app = Get-AppxPackage -Name 'OpenAI.CodexPrimaryRuntime*' | Sort-Object Version -Descending | Select-Object -First 1
    if (-not $app) { throw 'Đặt JLPT_WORKSPACE_DEPENDENCIES bằng đường dẫn dependencies của Codex Workspace.' }
    $runtime = Join-Path $app.InstallLocation 'dependencies'
}
$node = Join-Path $runtime 'node/bin/node.exe'
$modules = Join-Path $runtime 'node/node_modules'
if (-not (Test-Path -LiteralPath (Join-Path $modules '@oai/artifact-tool'))) { throw 'Thiếu @oai/artifact-tool trong workspace dependencies.' }
$scratch = New-Item -ItemType Directory -Path (Join-Path ([IO.Path]::GetTempPath()) ("jlpt-rss-" + [guid]::NewGuid()))
$link = Join-Path $scratch.FullName 'node_modules'
$stage = Join-Path $Root ('.rss-' + [guid]::NewGuid() + '.xlsx')
$lock = $null
try {
    $lock = [IO.FileStream]::new((Join-Path $Root '.audio-rss.lock'), 'OpenOrCreate', 'ReadWrite', 'None', 1024, 'DeleteOnClose')
    if (Test-Path -LiteralPath $excel) {
        $probe = [IO.File]::Open($excel, 'Open', 'ReadWrite', 'None')
        $probe.Dispose()
    }
    New-Item -ItemType Junction -Path $link -Target $modules | Out-Null
    $builder = Join-Path $scratch.FullName 'workbook.mjs'
    $rows = Join-Path $scratch.FullName 'rows.json'
    Copy-Item -LiteralPath (Join-Path $PSScriptRoot 'write_audio_workbook.mjs') -Destination $builder
    $opts = @('--root', $Root, '--output', $rows)
    if ($FeedUrl) { $opts += @('--feed-url', $FeedUrl) }
    if ($RssFile) { $opts += @('--rss-file', (Resolve-Path -LiteralPath $RssFile).Path) }
    if ($UseSavedFeed) { $opts += '--use-saved-feed' }
    if ($ReplaceEpisode) { $opts += '--replace-episode' }
    $env:PYTHONUTF8 = '1'
    & py -3 (Join-Path $PSScriptRoot 'sync_exam_audio.py') @opts
    if ($LASTEXITCODE) { throw 'Đồng bộ RSS thất bại. Workbook cũ vẫn còn trên đĩa.' }
    & $node $builder $rows $stage $PreviewPath
    if ($LASTEXITCODE) { throw 'Xuất Excel thất bại. Chạy lại sau khi đã đóng workbook.' }
    if ([IO.File]::Exists($excel)) {
        $backup = $stage + '.bak'
        [IO.File]::Replace($stage, $excel, $backup)
        [IO.File]::Delete($backup)
    } else { [IO.File]::Move($stage, $excel) }
    $result = Get-Content -Raw -Encoding utf8 -LiteralPath $rows | ConvertFrom-Json
    Write-Output "$excel ($($result.rows.Count))"
    if ($result.issues.Count) { throw 'Đã xuất Excel. Xem các gói cần kiểm tra trong cột F và thông báo phía trên.' }
} finally {
    if ($lock) { $lock.Dispose() }
    if (Test-Path -LiteralPath $stage) { [IO.File]::Delete($stage) }
    [IO.File]::Delete($stage + '.inspect.ndjson')
    if (Test-Path -LiteralPath $link) { [IO.Directory]::Delete($link) }
    foreach ($name in @('workbook.mjs', 'rows.json')) { [IO.File]::Delete((Join-Path $scratch.FullName $name)) }
    [IO.Directory]::Delete($scratch.FullName)
}
