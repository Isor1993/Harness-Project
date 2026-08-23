# README.md — Vorlagen des Kerns

Ownership: Nur die Originale, die beim Einrichten eines neuen Projekts
nach `.claude\` kopiert werden. Was eine Vorlage bewirkt, steht in der
Regeldatei, zu der sie gehört; wann kopiert wird, in
`Kern/VERSIONIERUNG.md` unter „Die Kern-Auslieferung".

Dieser Ordner steht neben `Kern/Befehle/` und folgt derselben
Arbeitsteilung: **Hier liegt das Original, unter `.claude\` die
Arbeitskopie.** Geändert wird das Original, danach wird kopiert — nie
umgekehrt.

Grund für die Doppelung: `.claude\` ist Konfiguration des Programms
Claude Code und geht nicht in die Auslieferung ein; die packt `Kern/`.
Läge das Original dort, wäre es in einem neuen Projekt weg.

## Was hier liegt

| Vorlage | Ziel | wofür |
|---|---|---|
| `settings.json` | `.claude\settings.json` | der `SessionStart`-Hook, der `Kern/Werkzeuge/pruefen.py` bei jedem Session-Start ausführt |

Zwei Einzelheiten daran sind Absicht und sollen beim Ändern erhalten
bleiben:

- **`${CLAUDE_PROJECT_DIR}` in der `args`-Form**, nicht als Text in der
  Kommandozeile. Claude Code ersetzt den Platzhalter selbst, bevor
  überhaupt eine Shell startet. Die Kommandozeilen-Fassung
  (`"python \"$CLAUDE_PROJECT_DIR/…\""`) setzt dagegen Bash voraus; wo
  Git Bash fehlt, weicht Claude Code auf PowerShell aus, und dort heißt
  die Variable anders — der Hook wäre **stumm kaputt**.
- **Der Schalter `--hook`.** Er lässt das Skript eine Herkunftszeile
  `[SessionStart-Hook]` voranstellen. Ohne sie ist der Ausgabe nicht
  anzusehen, ob der Harness sie erzeugt hat oder Claude das Skript von
  Hand gestartet hat — und dieser Unterschied ist der ganze Zweck des
  Hooks. Dieselbe Zeile verhindert einen zweiten Lauf (`CLAUDE.md`,
  Punkt 5).

**Die Vorlage enthält bewusst nur den `hooks`-Block**, keine
Berechtigungen und keine freigegebenen Ordner. Beides ist rechner- und
personenabhängig; eine Auslieferung ist eine Vorlage, keine Kopie
(`Kern/VERSIONIERUNG.md`). Existiert im Zielprojekt schon eine
`settings.json`, wird nur der `hooks`-Block hineinübernommen.

## Wie der Abgleich geprüft wird

`Kern/Werkzeuge/pruefen.py` fährt ihn als **Prüfung 6**, gebaut am
2026-08-23 nach dem Muster von Prüfung 3 (Befehle gegen Arbeitskopie).

Verglichen wird **je Hook-Eintrag, nicht die ganze Datei**: Eigene Hooks
dürfen in `.claude\settings.json` dazukommen, ohne einen Fund auszulösen;
fehlen oder abweichen darf keiner aus der Vorlage. Berechtigungen und
freigegebene Ordner bleiben außen vor.

Der Grund für diese Prüfung: Der Hook ist das einzige Stück des Harness,
das **seinen eigenen Ausfall nicht melden kann**. Verschwindet er aus der
Arbeitskopie, läuft `pruefen.py` beim Session-Start nicht mehr — und
niemand sagt etwas. Deshalb prüft das Skript, ob es selbst noch gerufen
wird.

Abgedeckte Fälle, alle am 2026-08-23 nachgestellt und bestanden: Vorlage
fehlt · `settings.json` fehlt · `hooks`-Block entfernt · Matcher geändert
· `settings.json` ist kein gültiges JSON mehr.
