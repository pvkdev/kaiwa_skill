#requires -Version 7.0
param([ValidateRange(1,50)][int]$Start = 1, [ValidateRange(1,50)][int]$End = 50)
$ErrorActionPreference = 'Stop'
$ProgressPreference = 'SilentlyContinue'
if ($End -lt $Start) { throw 'End precedes Start' }
$root = Split-Path -Parent $PSScriptRoot
$ledger = Get-Content -LiteralPath (Join-Path $root 'reports/crawl-coverage.json') -Raw | ConvertFrom-Json -AsHashtable
foreach ($n in $Start..$End) {
    $entry = $ledger[[string]$n].grammar
    if ($entry.state -ne 'captured') { throw "Capture the grammar page for lesson $n first" }
    $file = Join-Path $root $entry.snapshot
    $snapshot = Get-Content -LiteralPath $file -Raw | ConvertFrom-Json -AsHashtable
    $ids = @($snapshot.drill_ids)
    if ($snapshot.lesson -ne $n -or $ids.Count -ne $entry.drill_count) { throw "Snapshot mismatch: $n" }
    $path = Join-Path (Split-Path -Parent $file) (([IO.Path]::GetFileNameWithoutExtension($file)) + '.answers.json')
    $results = if (Test-Path -LiteralPath $path) { Get-Content -LiteralPath $path -Raw | ConvertFrom-Json -AsHashtable } else { [ordered]@{} }
    $missing = @($ids | Where-Object { !$results.Contains($_) })
    if (!$missing.Count) { Write-Output "Lesson $n : $($ids.Count) answers accounted for"; continue }
    $url = $entry.url
    if ($url -ne "https://www.vnjpclub.com/minna-no-nihongo/bai-$n-ngu-phap.html") { throw "Review source for lesson $n" }
    Start-Sleep -Seconds 2
    $page = Invoke-WebRequest -Uri $url -SessionVariable answerSession -TimeoutSec 30
    $match = [regex]::Match($page.Content,'<script id="vnjp-answer-check-js-before" src="data:text/javascript;base64,([^"]+)"')
    if (!$match.Success) { throw "Review the current public reveal controls on lesson $n" }
    $js = [Text.Encoding]::UTF8.GetString([Convert]::FromBase64String($match.Groups[1].Value))
    $config = [regex]::Match($js,'(?s)\{.*\}').Value | ConvertFrom-Json
    if ($config.ajaxUrl -ne 'https://www.vnjpclub.com/wp-admin/admin-ajax.php') { throw 'Unexpected answer service URL' }
    for ($i=0; $i -lt $missing.Count; $i+=4) {
        $chunk = @($missing[$i..([Math]::Min($i+3,$missing.Count-1))])
        Start-Sleep -Seconds 2
        $params = @{action='vnjp_answer_check'; op='reveal'; source='minna-grammar-drill'; lesson="$n"
            items=(ConvertTo-Json -InputObject $chunk -Compress); locale='vi'; nonce=$config.nonce }
        $raw = Invoke-WebRequest -Method Post -Uri $config.ajaxUrl -WebSession $answerSession -Headers @{Referer=$url} -Body $params -TimeoutSec 30
        $response = $raw.Content | ConvertFrom-Json -AsHashtable
        foreach ($id in $chunk) {
            $item = $response.items[$id]
            if (!$item -or $item.error -or $item.extra.error -or [string]::IsNullOrWhiteSpace($item.answer)) {
                throw "No verified source answer for lesson $n / $id"
            }
            $results[$id] = [ordered]@{answer=$item.answer; reveal_html=$item.reveal_html; explanation_html=$item.explanation_html}
        }
        $results | ConvertTo-Json -Depth 12 | Set-Content -LiteralPath ($path+'.tmp') -Encoding utf8NoBOM
        [IO.File]::Move(($path+'.tmp'),$path,$true)
    }
    Write-Output "Lesson $n : $($results.Count)/$($ids.Count) answers"
}
