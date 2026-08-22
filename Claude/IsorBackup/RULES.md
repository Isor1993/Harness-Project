# RULES.md — Regeln für den Datenbaum

Ownership: Baum, Ablageregeln, Benennung und Asset-Library für
`C:\IsorBackup\`. Keine Aufgaben (das ist `ROADMAP.md` dieser Schicht),
keine Begründungen (`DECISIONS.md`), keine Regeln für die Repos — die
stehen in `Kern/CODE_GUIDELINES.md`.

Warum die Regeln hier und nicht im Datenbaum selbst liegen:
`C:\IsorBackup` ist kein Git-Repo. Ein Regeltext ohne
Versionsgeschichte lässt sich nicht mehr nachvollziehen, sobald ihn
jemand ändert. Im Datenbaum steht deshalb nur ein Wegweiser hierher.

## Was hier liegt und was nicht

`C:\IsorBackup\` nimmt **alles auf, was nicht Code in einem Git-Repo
ist.** Angelegt am 2026-08-06. Die Repos liegen daneben auf `C:\`; das
externe Backup umfasst deshalb **drei** Ordner, nicht einen — der Umfang
steht im Skript, siehe „Werkzeug" unten.

## Baum

Nur die oberste Ebene und wofür jeder Ordner da ist. Was darunter liegt,
zeigt der Ordner selbst — eine vollständige Auflistung wäre nach einer
Woche falsch.

```
00_Eingang\        alles Neue landet hier — wird geleert, nicht bewohnt
01_Uni\            je Semester ein Ordner, aufgebaut nach _Vorlagen\Semester_Vorlage
02_Projekte\       Projektdaten, die nicht ins Repo gehören (Builds, Messungen, Media)
03_AssetLibrary\   Eigene\ · Extern_Gekauft\ · Extern_Frei\ · KI_Generiert\ · _Lizenzen\
04_Lernen\         Tutorials, Kurse, gespeicherte Artikel
05_Werkzeuge\      Installer, Layouts, Vorlagen, Presets, Harness-Auslieferungen
99_Archiv\         erledigt, aber nicht wegwerfen  (+ _Zu_Loeschen\)
```

## Ablageregeln

1. **Desktop bleibt leer.** Er ist eine Ablagefläche, kein Ordner.
2. **Downloads ist Durchgang.** Behalten → `00_Eingang` oder direkt an
   seinen Platz.
3. **`00_Eingang` wird geleert**, einmal die Woche. Was dort liegt, gilt
   als unsortiert.
4. **Eine Sache, ein Ort.** Keine „Kopie von". Alte Stände nur in
   `_Archiv\`, mit Datum vorn: `2026-07-12_TDD.odt`.
5. **Unterstriche statt Leerzeichen, keine Umlaute.**
6. **`_` vorn = kein Arbeitsmaterial** (Archiv, Vorlagen, Lizenzen).
   **Zahlen vorn** halten die Reihenfolge stabil.
7. **Gelöscht wird nur von Isor.** „Weg" heißt `99_Archiv\_Zu_Loeschen\`.
   Diese Regel gilt auch für Claude und für jedes Skript.

## Benennung

Schema `<Thema>_<Objekt>_<Variante>_<Map>.<ext>` — keine laufenden
Nummern außer als echte Variante. Textur-Maps nach den Unity-Slots:
`_Color`, `_Normal`, `_AO`, `_Roughness`, `_Height`, `_Mask`.

**Die Original-ID des Herstellers** (`Moon_002`, `Ground096B`) darf nicht
verloren gehen — sie ist der Lizenznachweis. Deshalb **pro Fremd-Paket
eine `_Quelle.txt`** mit Quelle, URL, Original-ID, Lizenz und Ladedatum.

## Asset-Library

Unity-Assets gehören als **`.unitypackage`** in die Library, nicht als
lose Datei: Rechtsklick im Projekt → *Export Package* mit „Include
dependencies". Eine einzeln herauskopierte `.shadergraph` oder `.vfx`
verliert ihre Texturen, Materialien und Subgraphs, weil die Verweise über
GUIDs in den `.meta`-Dateien laufen.

Bei Fremd-Packs mit mehreren Formaten braucht Unity nur **FBX +
Texturen**. `glTF`, `OBJ`, `.usdc`, `.mtlx` und `.tres` (Godot) sind
Beigaben für andere Pipelines. Bei Normal-Maps `NormalGL` behalten —
Unity folgt der OpenGL-Konvention, `NormalDX` ist für Unreal. Unity will
Smoothness = 1 − Roughness.

## Werkzeug

`IsorBackup/Werkzeuge/sichern.ps1` spiegelt den Baum auf die externe
Platte. Probelauf ist die Voreinstellung; Wegfallendes wandert nach
`_Geloescht\<Datum>\` statt gelöscht zu werden (Regel 7, angewandt auf
die Platte). Ausgelöst wird es am Pflegetag, siehe `Kern/WORKFLOW.md`.
