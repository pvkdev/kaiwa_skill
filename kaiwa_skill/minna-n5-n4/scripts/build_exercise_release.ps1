#requires -Version 7.0
# Rebuild the preview from reviewed, local authoring files.
$ErrorActionPreference = 'Stop'
$root = Split-Path -Parent $PSScriptRoot
function Invoke-LessonTool {
    param([string]$Script, [string[]]$ToolArgs)
    & py -B -X utf8 (Join-Path $PSScriptRoot $Script) @ToolArgs
    if ($LASTEXITCODE -ne 0) { throw "Failed: $Script $ToolArgs" }
}
Push-Location -LiteralPath $root
try {
    Invoke-LessonTool 'quick_checks.py'
    Invoke-LessonTool 'grammar_practice_order.py'
    foreach ($bank in @('quick-checks', 'renshuu', 'renshuu-drills')) {
        $option = if ($bank -eq 'quick-checks') { '--quick-check' } else { '--renshuu' }
        foreach ($file in Get-ChildItem -LiteralPath "authored/$bank" -File -Filter 'lesson-*.json') {
            $dest = Join-Path "exports/curriculum-exercises/$bank" $file.BaseName
            Invoke-LessonTool 'curriculum_templates.py' @($option, $file.FullName, '--out', $dest)
        }
    }
    Invoke-LessonTool 'curriculum_templates.py' @('authored/lesson-39/templates/sections.json')
    Invoke-LessonTool 'lesson39_reading.py'
    Invoke-LessonTool 'curriculum_templates.py' @('authored/lesson-39/reading.json','--out','exports/curriculum-exercises/reading/lesson-39')
    foreach ($family in @('listening','assessment')) {
        foreach ($file in Get-ChildItem -Path "authored/lesson-*/$family.json" -File) {
            $dest = Join-Path "exports/curriculum-exercises/$family" $file.Directory.Name
            Invoke-LessonTool 'curriculum_templates.py' @($file.FullName,'--out',$dest)
        }
    }
    Invoke-LessonTool 'curriculum_preview.py'
} finally {
    Pop-Location
}
