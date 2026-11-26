#requires -Version 7.0
# Audit the groups actually observed in lesson 39. Keep one bilingual example.
$ErrorActionPreference = 'Stop'
$ProgressPreference = 'SilentlyContinue'
$root = Split-Path -Parent $PSScriptRoot
$plan = Get-Content (Join-Path $root 'pilot/lesson-39.plan.json') -Raw | ConvertFrom-Json
$pageUrl = 'https://www.vnjpclub.com/minna-no-nihongo/bai-39-ngu-phap.html'
$page = Invoke-WebRequest $pageUrl -SessionVariable publicSession -TimeoutSec 20
$tag = [regex]::Match($page.Content,'<script id="vnjp-answer-check-js-before" src="data:text/javascript;base64,([^"]+)"')
if (!$tag.Success) {throw 'Missing public answer client config. Inspect the current lesson layout.'}
$js = [Text.Encoding]::UTF8.GetString([Convert]::FromBase64String($tag.Groups[1].Value))
$config = [regex]::Match($js,'(?s)\{.*\}').Value | ConvertFrom-Json
if ($config.ajaxUrl -ne 'https://www.vnjpclub.com/wp-admin/admin-ajax.php') {throw 'Unexpected answer service URL.'}
$rows = [Collections.Generic.List[object]]::new()
$sample = $null
foreach ($group in $plan.renshuu_b) {
    Start-Sleep -Seconds 2
    $params = @{
        action='vnjp_answer_check'; op='reveal'; source='minna-grammar-drill'
        lesson='39'; items=(ConvertTo-Json -InputObject @($group.item_ids) -Compress)
        locale='vi'; nonce=$config.nonce
    }
    $result = Invoke-WebRequest -Method Post -Uri $config.ajaxUrl -WebSession $publicSession -TimeoutSec 20 -Headers @{Accept='application/json';Referer=$pageUrl} -Body $params
    $body = $result.Content | ConvertFrom-Json -AsHashtable
    if ($body.items -isnot [Collections.IDictionary]) {throw "Missing item map for $($group.source_group_id)"}
    foreach ($id in $group.item_ids) {
        $item = $body.items[$id]
        if ($null -eq $item -or $item.error -or $item.extra.error) {throw "Missing or failed reveal for $id"}
        $html = [string]$item.reveal_html
        $vi = [regex]::Match($html,'(?s)<div class="mg-vi">(.*?)</div>').Groups[1].Value
        $vi = [Net.WebUtility]::HtmlDecode(($vi -replace '<[^>]+>', '')).Trim()
        $track = [regex]::Match($html,'data-track="([^"]+)"').Groups[1].Value
        $time = [regex]::Match($html,'data-t="([0-9.]+),([0-9.]+)"')
        $clip = $null
        if ($time.Success -and $track) {
            $start = [decimal]::Parse($time.Groups[1].Value,[cultureinfo]::InvariantCulture)
            $end = [decimal]::Parse($time.Groups[2].Value,[cultureinfo]::InvariantCulture)
            if ($start -lt 0 -or $end -le $start) {throw "Invalid clip in $id"}
            $clip = @{track=$track;start_ms=[int]($start*1000);end_ms=[int]($end*1000)}
        }
        $rows.Add([ordered]@{
            item_id=$id; answer_present=![string]::IsNullOrWhiteSpace($item.answer)
            translation_present=[bool]$vi; explanation_html_present=![string]::IsNullOrWhiteSpace($item.explanation_html)
            clip=$clip
        })
        if ($id -eq 'b1-1') {
            if (!$vi -or !$clip -or !$item.answer) {throw 'B1-1 sample changed. Review before updating the baseline.'}
            $sample = [ordered]@{
                source_item_id=$id; origin='source'; answer_ja=$item.answer; translation_vi=$vi
                explanation_html=$item.explanation_html; clip=$clip
            }
        }
    }
}
$report = [ordered]@{
    lesson_number=39; source_url=$pageUrl; verified_at=[datetime]::UtcNow.ToString('o')
    method='public_reveal_by_observed_item_id'; item_count=$rows.Count; items=$rows; sample=$sample
}
$dir = New-Item -ItemType Directory -Force -Path (Join-Path $root 'reports')
$path = Join-Path $dir 'lesson-39-renshuu-b.json'
$report | ConvertTo-Json -Depth 7 | Set-Content -LiteralPath ($path+'.tmp') -Encoding utf8NoBOM
Move-Item -LiteralPath ($path+'.tmp') -Destination $path -Force
Write-Output $path
