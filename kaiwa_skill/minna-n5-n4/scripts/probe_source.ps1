#requires -Version 7.0
param([ValidateRange(1,50)][int]$Lesson = 39)
$ErrorActionPreference = 'Stop'
$ProgressPreference = 'SilentlyContinue'
$root = Split-Path -Parent $PSScriptRoot
$catalog = Get-Content (Join-Path $root 'catalog/sources.json') -Raw | ConvertFrom-Json -AsHashtable
$pages = $catalog.lessons[('{0:D2}' -f $Lesson)].pages
$rows = foreach ($family in @('lesson','grammar','shadowing','conversation','listening','short_reading','long_reading','assessment')) {
    $url = $pages[$family].candidate_url
    if ([uri]::new($url).Authority -ne 'www.vnjpclub.com') {throw "Unexpected catalog host: $url"}
    $row = [ordered]@{family=$family; url=$url; fetched_at=[datetime]::UtcNow.ToString('o'); http_status=$null; final_url=$null; status='network_error'}
    try {
        $response = Invoke-WebRequest -Uri $url -TimeoutSec 20 -SkipHttpErrorCheck
        $row.http_status = [int]$response.StatusCode
        $row.final_url = $response.BaseResponse.RequestMessage.RequestUri.AbsoluteUri
        $title = [regex]::Match([string]$response.Content,'(?is)<title[^>]*>(.*?)</title>').Groups[1].Value
        $row.title = [Net.WebUtility]::HtmlDecode($title)
        $row.status = if ($row.http_status -eq 429) {'rate_limited'}
            elseif ($row.http_status -in 401,403 -or $title -match 'xác minh|One moment|Just a moment') {'access_blocked'}
            elseif ($row.http_status -ne 200) {'http_error'}
            elseif ($row.final_url -ne $url) {'redirect_review'}
            elseif ($response.Content -match '<div[^>]+class="[^"]*ykhp-protected-content') {'requires_render'}
            else {'inspect_dom'}
    } catch { $row.error_type = $_.Exception.GetType().Name }
    [pscustomobject]$row
    if ($row.status -in 'rate_limited','access_blocked') { break }
    if ($family -ne 'assessment') {Start-Sleep -Seconds 2}
}
$report = [ordered]@{lesson=$Lesson; planned_pages=$pages.Count; attempted_pages=@($rows).Count; pages=@($rows)}
$dir = New-Item -ItemType Directory -Force -Path (Join-Path $root 'reports')
$file = Join-Path $dir ("http-{0:D2}.json" -f $Lesson)
$report | ConvertTo-Json -Depth 5 | Set-Content -LiteralPath $file -Encoding utf8NoBOM
Write-Output $file
