<#
    sichern.ps1 — wöchentliche Sicherung auf die externe Platte.

    Verfahren (Kern/DECISIONS.md, 2026-08-22): Spiegeln mit Papierkorb.
    Die Platte zeigt den aktuellen Stand; alles, was dort wegfiele, wandert
    vorher nach _Geloescht\<Datum>\ statt gelöscht zu werden. Geleert wird
    nur von Isor — dieselbe Regel wie 99_Archiv\_Zu_Loeschen.

    Ausdrücklich KEIN robocopy /MIR ohne Papierkorb: Ein versehentliches
    Löschen wäre nach dem nächsten Lauf endgültig, und genau dann reißt
    das Sicherheitsnetz, wenn man es braucht.

    Aufruf:
        .\sichern.ps1 -Ziel E:\            Probelauf, ändert nichts
        .\sichern.ps1 -Ziel E:\ -Ausfuehren

    Voraussetzung: Auf der Platte muss die Datei _ISOR_BACKUP.txt liegen.
    Ohne sie bricht das Skript ab — so kann kein falscher Laufwerksbuchstabe
    vollgeschrieben werden.
#>

param(
    [Parameter(Mandatory = $true)][string]$Ziel,
    [switch]$Ausfuehren
)

$ErrorActionPreference = 'Stop'

$Quellen = @(
    'C:\IsorBackup',
    'C:\Repos Isor'
)

$Marker = Join-Path $Ziel '_ISOR_BACKUP.txt'
$Papierkorb = Join-Path $Ziel ('_Geloescht\' + (Get-Date -Format 'yyyy-MM-dd'))

# --- Sicherheitsprüfungen ---------------------------------------------------
if (-not (Test-Path $Ziel)) {
    throw "Ziel nicht erreichbar: $Ziel — Platte angesteckt?"
}
if (-not (Test-Path $Marker)) {
    throw @"
Erkennungsdatei fehlt: $Marker

Das ist die Sicherung gegen einen falschen Laufwerksbuchstaben. Wenn das
wirklich die Backup-Platte ist, lege die Datei einmalig an:
    New-Item -ItemType File '$Marker'
"@
}

Write-Output "Ziel:      $Ziel"
Write-Output "Papierkorb: $Papierkorb"
Write-Output ("Modus:     " + $(if ($Ausfuehren) { 'AUSFUEHREN' } else { 'Probelauf (nichts wird geschrieben)' }))
Write-Output ''

$GesamtNeu = 0
$GesamtWeg = 0

foreach ($Quelle in $Quellen) {
    if (-not (Test-Path $Quelle)) {
        Write-Output "uebersprungen (nicht vorhanden): $Quelle"
        continue
    }
    $Name = Split-Path $Quelle -Leaf
    $ZielOrdner = Join-Path $Ziel $Name
    Write-Output "--- $Name ---"

    # 1) Was liegt auf der Platte, aber nicht mehr in der Quelle?
    $Weg = @()
    if (Test-Path $ZielOrdner) {
        $QuellSet = New-Object 'System.Collections.Generic.HashSet[string]'
        Get-ChildItem $Quelle -Recurse -File -Force -ErrorAction SilentlyContinue |
            ForEach-Object { $null = $QuellSet.Add($_.FullName.Substring($Quelle.Length)) }

        Get-ChildItem $ZielOrdner -Recurse -File -Force -ErrorAction SilentlyContinue |
            ForEach-Object {
                $Rel = $_.FullName.Substring($ZielOrdner.Length)
                if (-not $QuellSet.Contains($Rel)) { $Weg += $_ }
            }
    }

    Write-Output ("  faellt auf der Platte weg: " + $Weg.Count + " Datei(en)")
    $GesamtWeg += $Weg.Count

    if ($Ausfuehren -and $Weg.Count -gt 0) {
        foreach ($Datei in $Weg) {
            $Rel = $Datei.FullName.Substring($ZielOrdner.Length).TrimStart('\')
            $NeuerPfad = Join-Path (Join-Path $Papierkorb $Name) $Rel
            $NeuerOrdner = Split-Path $NeuerPfad -Parent
            if (-not (Test-Path $NeuerOrdner)) {
                $null = New-Item -ItemType Directory -Path $NeuerOrdner -Force
            }
            Move-Item -LiteralPath $Datei.FullName -Destination $NeuerPfad -Force
        }
        Write-Output "  -> in den Papierkorb verschoben, nicht geloescht"
    }

    # 2) Neues und Geaendertes kopieren. Kein /MIR — geloescht wird oben.
    # Ausgeschlossen wird nur, was Unity beim naechsten Oeffnen neu baut.
    # .git bleibt ausdruecklich DRIN: ohne Historie waere die Kopie kein
    # Repo mehr, sondern nur ein Haufen Dateien.
    $RoboArgs = @($Quelle, $ZielOrdner, '/E', '/R:1', '/W:1', '/NFL', '/NDL', '/NJH', '/NP',
                  '/XD', '_Geloescht', 'Library', 'Temp', 'obj', 'Logs')
    if (-not $Ausfuehren) { $RoboArgs += '/L' }

    $Ausgabe = & robocopy @RoboArgs
    $Code = $LASTEXITCODE
    $Ausgabe | Where-Object { $_ -match '\S' } | Select-Object -Last 6 | ForEach-Object { "  $_" }

    if ($Code -ge 8) { throw "robocopy meldet Fehler (Code $Code) fuer $Name" }
    Write-Output ''
}

Write-Output '=========================================='
Write-Output ("Wegfallende Dateien insgesamt: " + $GesamtWeg)
if (-not $Ausfuehren) {
    Write-Output 'Probelauf — es wurde nichts geschrieben.'
    Write-Output 'Zum wirklichen Lauf: -Ausfuehren anhaengen.'
} else {
    Write-Output "Fertig. Papierkorb dieses Laufs: $Papierkorb"
    Write-Output 'Der Papierkorb wird nur von Isor geleert.'
}

# robocopy meldet mit Code 1 "Dateien kopiert" — das ist Erfolg, kein Fehler.
exit 0
