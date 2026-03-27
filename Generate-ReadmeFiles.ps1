#Requires -Version 5.1
<#
.SYNOPSIS
    Generates README.md files from cheats.yaml files in the CheatArchiver repository.
.DESCRIPTION
    Walks the consoles/ directory tree, parses each cheats.yaml (no external modules
    required), and writes the corresponding README.md files.  Also regenerates the
    index pages at the region, console, and consoles/ levels.
.PARAMETER Root
    Root of the repository.  Defaults to the directory that contains this script.
#>
[CmdletBinding()]
param(
    [string]$Root = $PSScriptRoot
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

# ---------------------------------------------------------------------------
# YAML parser (hand-rolled – no powershell-yaml module required)
# ---------------------------------------------------------------------------

function ConvertFrom-CheatsYaml {
    param([string]$Path)

    $lines = Get-Content -LiteralPath $Path -Encoding UTF8

    $data = [PSCustomObject]@{
        game        = ''
        console     = ''
        region      = ''
        serial      = ''
        cheat_type  = ''
        source      = ''
        patch       = ''
        base_serial = ''
        cheats      = [System.Collections.Generic.List[object]]::new()
    }

    $currentCheat   = $null
    $currentPointer = $null
    $currentOffset  = $null
    $context        = 'top'

    foreach ($rawLine in $lines) {
        # Skip comment lines and blank lines
        if ($rawLine -match '^\s*#' -or $rawLine -match '^\s*$') { continue }

        $indent  = $rawLine.Length - $rawLine.TrimStart().Length
        $trimmed = $rawLine.TrimStart()

        # Try to extract a key/value pair from the current line.
        # Handles:  key: "quoted value"   key: unquoted value   - key: "quoted"
        $key = $null
        $val = $null
        if ($trimmed -match '^-?\s*([A-Za-z_][A-Za-z_0-9]*):\s*"([^"]*)"') {
            $key = $Matches[1]; $val = $Matches[2]
        } elseif ($trimmed -match '^-?\s*([A-Za-z_][A-Za-z_0-9]*):\s+(\S.*)') {
            $key = $Matches[1]; $val = $Matches[2].TrimEnd()
        }

        switch ($indent) {
            0 {
                if ($trimmed -eq 'cheats:') {
                    $context = 'cheats'
                } elseif ($key -and $data.PSObject.Properties[$key]) {
                    $data.$key = $val
                }
            }
            2 {
                # Start of a new cheat item — flush whatever was being built
                if ($currentOffset  -ne $null) {
                    $currentPointer.offsets.Add($currentOffset)
                    $currentOffset = $null
                }
                if ($currentPointer -ne $null) {
                    $currentCheat.pointers.Add($currentPointer)
                    $currentPointer = $null
                }
                if ($currentCheat -ne $null) { $data.cheats.Add($currentCheat) }

                $currentCheat = [PSCustomObject]@{
                    name     = if ($key -eq 'name') { $val } else { '' }
                    author   = ''
                    notes    = ''
                    codes    = [System.Collections.Generic.List[string]]::new()
                    pointers = [System.Collections.Generic.List[object]]::new()
                }
                $context = 'cheat'
            }
            4 {
                if ($trimmed -eq 'codes:') {
                    $context = 'codes'
                } elseif ($trimmed -eq 'pointers:') {
                    $context = 'pointers'
                } elseif ($key -and $currentCheat -ne $null) {
                    switch ($key) {
                        'name'   { $currentCheat.name   = $val }
                        'author' { $currentCheat.author = $val }
                        'notes'  { $currentCheat.notes  = $val }
                    }
                }
            }
            6 {
                if ($context -eq 'codes') {
                    if ($trimmed -match '^-\s+"([^"]+)"') {
                        $currentCheat.codes.Add($Matches[1])
                    }
                } elseif ($context -eq 'pointers') {
                    # Start of a new pointer item — flush the previous one
                    if ($currentOffset -ne $null) {
                        $currentPointer.offsets.Add($currentOffset)
                        $currentOffset = $null
                    }
                    if ($currentPointer -ne $null) {
                        $currentCheat.pointers.Add($currentPointer)
                    }
                    $currentPointer = [PSCustomObject]@{
                        base        = if ($key -eq 'base') { $val } else { '' }
                        base_label  = ''
                        offsets     = [System.Collections.Generic.List[object]]::new()
                        final_code  = ''
                        final_label = ''
                    }
                }
            }
            8 {
                if ($trimmed -ne 'offsets:' -and $key -and $currentPointer -ne $null) {
                    switch ($key) {
                        'base_label'  { $currentPointer.base_label  = $val }
                        'final_code'  { $currentPointer.final_code  = $val }
                        'final_label' { $currentPointer.final_label = $val }
                    }
                }
            }
            10 {
                # Start of a new offset item — flush the previous one
                if ($currentOffset -ne $null) {
                    $currentPointer.offsets.Add($currentOffset)
                }
                $currentOffset = [PSCustomObject]@{
                    offset = if ($key -eq 'offset') { $val } else { '' }
                    label  = ''
                }
            }
            12 {
                if ($key -eq 'label' -and $currentOffset -ne $null) {
                    $currentOffset.label = $val
                }
            }
        }
    }

    # Flush any remaining objects at end-of-file
    if ($currentOffset  -ne $null) { $currentPointer.offsets.Add($currentOffset) }
    if ($currentPointer -ne $null) { $currentCheat.pointers.Add($currentPointer) }
    if ($currentCheat   -ne $null) { $data.cheats.Add($currentCheat) }

    return $data
}

# ---------------------------------------------------------------------------
# README section builders
# ---------------------------------------------------------------------------

function Format-PointerChain {
    param($pointer)
    $sb = [System.Text.StringBuilder]::new()

    $baseLabel  = if ($pointer.base_label)  { " [$($pointer.base_label)]" }  else { '' }
    $finalLabel = if ($pointer.final_label) { " [$($pointer.final_label)]" } else { '' }

    $null = $sb.AppendLine("Base${baseLabel}:   $($pointer.base)")
    foreach ($off in $pointer.offsets) {
        $offLabel = if ($off.label) { "  [$($off.label)]" } else { '' }
        $null = $sb.AppendLine("  -> +$($off.offset)$offLabel")
    }
    $null = $sb.Append("Final${finalLabel}:   $($pointer.final_code)")
    return $sb.ToString()
}

function Build-CheatSection {
    param($cheat)
    $sb = [System.Text.StringBuilder]::new()

    $null = $sb.AppendLine("### $($cheat.name)")
    $null = $sb.Append("**Author:** $($cheat.author)")

    if ($cheat.notes) {
        $null = $sb.AppendLine("  ")
        $null = $sb.Append("**Notes:** $($cheat.notes)")
    }
    $null = $sb.AppendLine("")
    $null = $sb.AppendLine("")

    if ($cheat.codes.Count -gt 0) {
        $null = $sb.AppendLine('```')
        foreach ($code in $cheat.codes) { $null = $sb.AppendLine($code) }
        $null = $sb.AppendLine('```')
        $null = $sb.AppendLine("")
    }

    if ($cheat.pointers.Count -gt 0) {
        $null = $sb.AppendLine("**Pointer chain:**")
        $null = $sb.AppendLine('```')
        foreach ($ptr in $cheat.pointers) {
            $null = $sb.AppendLine((Format-PointerChain $ptr))
        }
        $null = $sb.AppendLine('```')
        $null = $sb.AppendLine("")
    }

    $null = $sb.AppendLine("---")
    $null = $sb.AppendLine("")
    return $sb.ToString()
}

# ---------------------------------------------------------------------------
# Game-level README
# ---------------------------------------------------------------------------

function Build-GameReadme {
    param($data, [string]$gameDir)
    $sb = [System.Text.StringBuilder]::new()

    $null = $sb.AppendLine("# $($data.game)")
    $null = $sb.AppendLine("")
    $null = $sb.AppendLine("**Console:** $($data.console)  ")
    $null = $sb.AppendLine("**Region:** $($data.region)  ")
    if ($data.serial) {
        $null = $sb.AppendLine("**Serial:** $($data.serial)  ")
    }
    if ($data.cheat_type) {
        $null = $sb.AppendLine("**Cheat Type:** $($data.cheat_type)  ")
    }
    if ($data.source) {
        $srcText = if ($data.source -match 'https?://([^/]+)') { $Matches[1] } else { $data.source }
        $null = $sb.AppendLine("**Source:** [$srcText]($($data.source))  ")
    }
    $null = $sb.AppendLine("")
    $null = $sb.AppendLine("---")
    $null = $sb.AppendLine("")
    $null = $sb.AppendLine("## Cheats")
    $null = $sb.AppendLine("")

    foreach ($cheat in $data.cheats) {
        $null = $sb.Append((Build-CheatSection $cheat))
    }

    # Patches section — list any patch sub-folders
    $patchesDir = Join-Path $gameDir 'patches'
    if (Test-Path -LiteralPath $patchesDir) {
        $patches = @(Get-ChildItem -LiteralPath $patchesDir -Directory | Sort-Object Name)
        if ($patches.Count -gt 0) {
            $null = $sb.AppendLine("## Patches")
            $null = $sb.AppendLine("")
            $null = $sb.AppendLine("| Patch |")
            $null = $sb.AppendLine("|---|")
            foreach ($p in $patches) {
                $urlName = [Uri]::EscapeDataString($p.Name)
                $null = $sb.AppendLine("| [$($p.Name)](./patches/$urlName/) |")
            }
            $null = $sb.AppendLine("")
        }
    }

    return $sb.ToString().TrimEnd() + "`n"
}

# ---------------------------------------------------------------------------
# Patch-level README
# ---------------------------------------------------------------------------

function Build-PatchReadme {
    param($data)
    $sb = [System.Text.StringBuilder]::new()

    $null = $sb.AppendLine("# $($data.game) — $($data.patch)")
    $null = $sb.AppendLine("")
    $null = $sb.AppendLine("**Console:** $($data.console)  ")
    $null = $sb.AppendLine("**Region:** $($data.region)  ")
    $null = $sb.AppendLine("**Base Game:** [$($data.game)](../../)  ")
    $null = $sb.AppendLine("**Patch:** $($data.patch)  ")
    if ($data.cheat_type) {
        $null = $sb.AppendLine("**Cheat Type:** $($data.cheat_type)  ")
    }
    $null = $sb.AppendLine("")
    $null = $sb.AppendLine("---")
    $null = $sb.AppendLine("")
    $null = $sb.AppendLine("## Cheats")
    $null = $sb.AppendLine("")

    foreach ($cheat in $data.cheats) {
        $null = $sb.Append((Build-CheatSection $cheat))
    }

    return $sb.ToString().TrimEnd() + "`n"
}

# ---------------------------------------------------------------------------
# Index-page builders
# ---------------------------------------------------------------------------

function Build-RegionReadme {
    param([string]$console, [string]$region, [object[]]$games)
    $sb = [System.Text.StringBuilder]::new()

    $null = $sb.AppendLine("# $console — $region")
    $null = $sb.AppendLine("")
    $null = $sb.AppendLine("## Games (A-Z)")
    $null = $sb.AppendLine("")
    $null = $sb.AppendLine("| Game | Cheats |")
    $null = $sb.AppendLine("|---|---|")
    foreach ($g in $games | Sort-Object Name) {
        $urlName = [Uri]::EscapeDataString($g.Name)
        $null = $sb.AppendLine("| [$($g.Name)](./$urlName/) | $($g.CheatCount) |")
    }
    $null = $sb.AppendLine("")
    $null = $sb.AppendLine("---")
    $null = $sb.AppendLine("")
    $null = $sb.Append("*Add more games by following the [contributing guide](../../../README.md#contributing).*")

    return $sb.ToString().TrimEnd() + "`n"
}

function Build-ConsoleReadme {
    param([string]$console, [string[]]$regions)
    $regionDesc = @{
        'NTSC-U' = 'North America'
        'NTSC-J' = 'Japan'
        'PAL'    = 'Europe / Australia'
        'World'  = 'Region-free'
    }
    $sb = [System.Text.StringBuilder]::new()

    $null = $sb.AppendLine("# $console")
    $null = $sb.AppendLine("")
    $null = $sb.AppendLine("## Regions")
    $null = $sb.AppendLine("")
    $null = $sb.AppendLine("| Region | Description |")
    $null = $sb.AppendLine("|---|---|")
    foreach ($r in $regions | Sort-Object) {
        $desc = if ($regionDesc.ContainsKey($r)) { $regionDesc[$r] } else { '' }
        $urlR = [Uri]::EscapeDataString($r)
        $null = $sb.AppendLine("| [$r](./$urlR/) | $desc |")
    }
    $null = $sb.AppendLine("")
    $null = $sb.Append("---")

    return $sb.ToString().TrimEnd() + "`n"
}

function Build-ConsolesReadme {
    param([object[]]$consoles)
    $sb = [System.Text.StringBuilder]::new()

    $null = $sb.AppendLine("# Consoles")
    $null = $sb.AppendLine("")
    $null = $sb.AppendLine("Browse cheats by hardware platform. Each console folder contains one sub-folder per region.")
    $null = $sb.AppendLine("")
    $null = $sb.AppendLine("| Console | Regions Available |")
    $null = $sb.AppendLine("|---|---|")
    foreach ($c in $consoles | Sort-Object Name) {
        $urlName = [Uri]::EscapeDataString($c.Name)
        $regions = $c.Regions -join ', '
        $null = $sb.AppendLine("| [$($c.Name)](./$urlName/) | $regions |")
    }
    $null = $sb.AppendLine("")
    $null = $sb.AppendLine("---")
    $null = $sb.AppendLine("")
    $null = $sb.Append("*New consoles are added as data is scraped and contributed. See the [contributing guide](../README.md#contributing) to add more.*")

    return $sb.ToString().TrimEnd() + "`n"
}

# ---------------------------------------------------------------------------
# File writer — skips the write if content is identical
# ---------------------------------------------------------------------------

function Write-ReadmeIfChanged {
    param([string]$Path, [string]$Content)

    # Normalize to LF for comparison and storage
    $normalised = $Content -replace '\r\n', "`n" -replace '\r', "`n"

    if (Test-Path -LiteralPath $Path) {
        $existing = (Get-Content -LiteralPath $Path -Raw -Encoding UTF8) -replace '\r\n', "`n" -replace '\r', "`n"
        if ($existing -eq $normalised) { return $false }
    }

    $utf8NoBom = New-Object System.Text.UTF8Encoding $false
    [System.IO.File]::WriteAllText($Path, $normalised, $utf8NoBom)
    Write-Host "  Updated: $Path"
    return $true
}

# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

$consolesDir = Join-Path $Root 'consoles'
if (-not (Test-Path $consolesDir)) {
    Write-Error "consoles/ directory not found at: $consolesDir"
    exit 1
}

$consolesData = [System.Collections.Generic.List[object]]::new()
$updated      = 0

foreach ($consoleDir in Get-ChildItem -LiteralPath $consolesDir -Directory | Sort-Object Name) {
    $regionsInConsole = [System.Collections.Generic.List[string]]::new()

    foreach ($regionDir in Get-ChildItem -LiteralPath $consoleDir.FullName -Directory | Sort-Object Name) {
        $gamesInRegion = [System.Collections.Generic.List[object]]::new()

        foreach ($gameDir in Get-ChildItem -LiteralPath $regionDir.FullName -Directory | Sort-Object Name) {
            $gameYaml = Join-Path $gameDir.FullName 'cheats.yaml'
            if (-not (Test-Path -LiteralPath $gameYaml)) { continue }

            Write-Host "Processing: $($consoleDir.Name) / $($regionDir.Name) / $($gameDir.Name)"

            $data   = ConvertFrom-CheatsYaml -Path $gameYaml
            $readme = Build-GameReadme -data $data -gameDir $gameDir.FullName
            if (Write-ReadmeIfChanged -Path (Join-Path $gameDir.FullName 'README.md') -Content $readme) {
                $updated++
            }

            # Patch READMEs
            $patchesDir = Join-Path $gameDir.FullName 'patches'
            if (Test-Path -LiteralPath $patchesDir) {
                foreach ($patchDir in Get-ChildItem -LiteralPath $patchesDir -Directory | Sort-Object Name) {
                    $patchYaml = Join-Path $patchDir.FullName 'cheats.yaml'
                    if (-not (Test-Path -LiteralPath $patchYaml)) { continue }

                    Write-Host "  Processing patch: $($patchDir.Name)"
                    $pdata   = ConvertFrom-CheatsYaml -Path $patchYaml
                    $preadme = Build-PatchReadme -data $pdata
                    if (Write-ReadmeIfChanged -Path (Join-Path $patchDir.FullName 'README.md') -Content $preadme) {
                        $updated++
                    }
                }
            }

            $gamesInRegion.Add([PSCustomObject]@{
                Name       = $gameDir.Name
                CheatCount = $data.cheats.Count
            })
        }

        # Region-level index README
        if ($gamesInRegion.Count -gt 0) {
            $regionReadme = Build-RegionReadme -console $consoleDir.Name -region $regionDir.Name -games $gamesInRegion
            if (Write-ReadmeIfChanged -Path (Join-Path $regionDir.FullName 'README.md') -Content $regionReadme) {
                $updated++
            }
            $regionsInConsole.Add($regionDir.Name)
        }
    }

    # Console-level index README
    if ($regionsInConsole.Count -gt 0) {
        $consoleReadme = Build-ConsoleReadme -console $consoleDir.Name -regions $regionsInConsole
        if (Write-ReadmeIfChanged -Path (Join-Path $consoleDir.FullName 'README.md') -Content $consoleReadme) {
            $updated++
        }
        $consolesData.Add([PSCustomObject]@{
            Name    = $consoleDir.Name
            Regions = $regionsInConsole.ToArray()
        })
    }
}

# Root consoles/ index README
if ($consolesData.Count -gt 0) {
    $consolesReadme = Build-ConsolesReadme -consoles $consolesData
    if (Write-ReadmeIfChanged -Path (Join-Path $consolesDir 'README.md') -Content $consolesReadme) {
        $updated++
    }
}

Write-Host ""
Write-Host "Done. $updated README file(s) updated."
