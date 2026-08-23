# LOG.md — Chronik Harness

Ownership: Nur was wann passiert ist — datierte Ereignisse, älteste oben.
Eine **Chronik**: Einträge werden nie geändert oder gekürzt, nur ergänzt.
Sie kann daher nicht falsch werden und braucht kein Archiv.
Was als Nächstes kommt, steht in `ROADMAP.md`; warum es so entschieden
wurde, in den DECISIONS dieser Schicht.
Format: `- JJJJ-MM-TT — Ereignis (1–3 Sätze: was, und woran es geprüft
wurde)`. Bei einem Umbau, der viele Dateien auf einmal betrifft, darf
ein Eintrag bis zu einem Absatz lang werden.
Ein Eintrag darf einen Ablageort nennen — er beschreibt den Stand von
damals, nicht den von heute.

- 2026-07-14 — Kern des Harness angelegt: `INDEX.md`, `ROADMAP.md` und
  eine minimale `CLAUDE.md`. Geprüft per Übergabetest — eine frische
  Session sollte allein aus den Dateien arbeitsfähig werden.
- 2026-07-17 — `WORKFLOW.md` gebaut: Grundregeln und alle vier
  Session-Typen (Brainstorm/Design, Development, Art, später Zeugnis).
- 2026-07-17 — Knowledge-System eingeführt: externer Ordner
  `C:\Repos Isor\Knowledge\` mit Themen-Unterordnern, dazu
  `KNOWLEDGE_RULES.md`. Extern, weil Wissen das Projekt überlebt.
- 2026-07-17 — `FEATURE_LOG.md` und `DECISIONS.md` angelegt — Gebautes
  und Begründungen bekommen getrennte Dateien.
- 2026-07-17 — `CODE_GUIDELINES.md` als Rohmaterial: Uni-Conventions und
  gefilterte Dozenten-Regeln in der Zwei-Block-Struktur.
- 2026-08-05 bis 2026-08-08 — Artifact-Seiten nach den drei Typen
  sortiert: zehn Seiten mit Symbol, Kind-Badge und Favicon; Regeln in
  `ARTIFACT_RULES.md`, Bestand in `ARTIFACT_INDEX.md`.
- 2026-08-08 — Diagramm-Werkzeug hält jetzt die gesamte Handarbeit über
  Neuerzeugungen hinweg: Kastenpositionen (über den Klassennamen statt der Id),
  Linien-Wegpunkte, Andockpunkte und die Lage der Multiplizitäts-Beschriftungen.
  Andockpunkte an Member-Zeilen werden auf den Kasten umgerechnet (pixelgleich).
  Neu `linienstaerke_setzen.py` für handgezeichnete Diagramme. Geprüft: zweiter
  Lauf erzeugt alle sieben Dateien byte-identisch.
- 2026-08-09 — Ablaufplan-Formen im Diagramm-Werkzeug (`uml_drawio.py`, +95
  Zeilen): sechs Sinnbilder nach DIN 66001 (`start`, `ende`, `prozess`,
  `entscheidung`, `unterprogramm`, `ein_aus`) über `knoten()`, Ablauflinien mit
  Zweigbeschriftung über `pfeil()`, `ablauf_lesen()` liest Lage **und** Größe
  zurück. Sinnbilder laufen über ihre Id statt über den Text — „Ende" kommt
  mehrfach vor. Klassendiagramme bleiben unberührt (nachgewiesen: kein
  Klassendiagramm hat einen Nicht-Swimlane-Kasten auf oberster Ebene, alle
  sieben Dateien nach dem Umbau byte-identisch).
- 2026-08-11 — Zwei Fehler im Diagramm-Werkzeug behoben, beide fielen erst an
  einem von Hand angeordneten Diagramm auf: (1) `knoten()` schrieb die Geometrie
  als Ganzzahl und verschob Kästen, die auf halben Pixeln sitzen — jetzt `%g`
  über `_zahl()`. (2) Ein bewusst frei gelassenes Linienende wurde von der
  Skript-Vorgabe überschrieben; Gegenmittel ist, die Vorgabe für diese Kante zu
  entfernen (jetzt Bedienregel 5 in DIAGRAM_RULES). Neu außerdem `SPRUNG =
  jumpStyle=arc` als zentrale Vorgabe: Bogensprung an jeder Kreuzung.
  Geprüft: 13 Kästen und 31 Kanten der Handanordnung unverändert, zweiter Lauf
  byte-identisch.
- 2026-08-11 — Session-Typ „Zeugnis" gebaut: vierter Typ in WORKFLOW.md,
  eigene Regeln in ASSESSMENT_RULES.md, Auslöser `/zeugnis`. Erstes
  Zeugnis am selben Tag geschrieben.
- 2026-08-22 — Harness auf die Schichten-Struktur umgebaut (Phasen 1–5 der
  Überholung). Neu: DOC_RULES, GDD_RULES, VERSIONIERUNG, PLAN, STOERUNGEN.
  Vier Schicht-Ordner angelegt, 17 Dateien einsortiert. Fünf Bestände
  aufgeteilt und jeder vor dem Archivieren geprüft: Zeugnisse (2 Dateien),
  FEATURE_LOG (3 Chroniken), ROADMAP (708 → 204 Zeilen Planung + 521
  Archiv), TDD_NOTES (10 Themenblöcke), DECISIONS (133 Einträge → 9
  Dateien). Vierzehn Regeldateien nachgezogen, alle toten Verweise
  repariert. Drei Skripte gebaut: INDEX und PREFAB_STATUS werden ab jetzt
  erzeugt, dazu die Sicherung auf die externe Platte.
  Leseordnung je Session-Start damit von 847 auf rund 250 Zeilen.
- 2026-08-22 — Phase 6 der Überholung: die Befehle gebaut. `/harness:sichern`,
  `:wechsel`, `:ende`, `:sonntag` und `:zeugnis` liegen als Auslöser in
  `.claude\commands\harness\`, ihr Ablauf in `Kern/WORKFLOW.md`; der
  Unterordner erzeugt den Namensraum, an dem die eigenen Befehle im
  `/`-Menü erkennbar sind. Der globale Skill `~\.claude\skills\zeugnis`
  ist damit archiviert. Berechtigungen von 314 Allow-Einträgen auf 51
  Muster plus 8 `ask` und 4 `deny`; die alte Fassung liegt im Archiv.
  Prüfung P1 gemessen: Von drei `CLAUDE.md` lädt nur die im Projektstamm
  von selbst, weshalb sie jetzt einen benannten Notkern trägt.
  Geprüft: `/harness:sichern` im selben Zug erstmals gelaufen — die
  Leseordnung führte ohne Zuruf zur Doku-Pflicht.
- 2026-08-22 — Phase 7 der Überholung: der Kern ist vollständig. Die Schicht
  `IsorBackup/` gebaut (RULES, ROADMAP, DECISIONS) und `C:\IsorBackup\README.md`
  von 93 auf 30 Zeilen als Wegweiser gekürzt; der Regeltext hat damit
  Versionsgeschichte. `Kern/GLOSSARY.md` mit 26 Begriffen eingesammelt, jeder
  mit Zeiger auf seinen Besitzer. Beim Aufteilen der acht „Offenen Punkte"
  gehörten drei in andere Schichten, einer war überholt, und einer war gar
  keine Aufgabe, sondern die Regel „beim draw.io-Export *Include a copy of my
  diagram* angehakt lassen" — sie steht jetzt in `Kern/DIAGRAM_RULES.md`.
  Geprüft: INDEX neu erzeugt, 46 Dateien, alle mit Ownership-Zeile.
- 2026-08-22 — Phase 8 der Überholung: die Abnahme. Schlussdurchgang über
  50 Dateien und rund 9.400 Zeilen in sechs Durchgängen, Ergebnis **33
  Befunde** in `_HARNESS_ABNAHME.md` (15 muss · 14 lohnt sich · 4 bei
  Bedarf). Nach Ursache sortiert liegt die größte Gruppe nicht bei den
  Regeln und nicht beim Altbestand, sondern mit 14 Befunden an den
  **Nahtstellen des Umbaus** vom 21./22.08. Drei Haken der Baulisten
  waren nicht gedeckt (Auslieferungs-Ordner, vier Aufgabentexte,
  ARTIFACT_INDEX-Eintrag). **30 der 33 Befunde im selben Zug behoben**;
  die drei übrigen hängen am Archivieren bzw. am ersten Pflegetag.
  Die Befehle haben ein Zuhause im Repo bekommen (`Kern/Befehle/`,
  Arbeitskopie in `.claude\`), das INDEX-Skript führt sie und die beiden
  Wegweiser-`CLAUDE.md` in eigenen Abschnitten. `CODE_GUIDELINES.md`
  beschrieb noch die Ordnerstruktur vor dem 2026-08-20 — neu geschrieben
  gegen den tatsächlichen Assets-Baum. Fünf Regeln geschärft, der Begriff
  „Befund" hat einen Besitzer.
  Geprüft mit zwei eigens gebauten Skripten: alle Datei-Verweise gegen
  den Bestand, Datumsreihenfolge und Pflichtfelder von drei Chroniken und
  zehn Entscheidungsdateien — am Ende null Beanstandungen. Sie fanden 6
  der 33 Befunde allein und stehen deshalb als Aufgabe in
  `Kern/ROADMAP.md`. Nebenbei einen aktiven Datenverlust abgewendet:
  `prefab_status.py` las 34 Prefabs als 33 Einträge, weil `Torch` und
  `Torch ` auf denselben Schlüssel fielen.
- 2026-08-23 — **Version 1.0.0 steht.** Der Tag begann mit einem
  Gegenlese-Durchgang aus eigener Session: Von den 30 als erledigt
  geführten Befunden der Abnahme waren **28 gedeckt, zwei nicht** — bei
  einem hing die Korrektur am falschen DECISIONS-Eintrag, beim anderen
  war nur die Regel geändert, nicht das, was sie vorschrieb. Dazu fünf
  neue Befunde (A34–A40), darunter der Auftrag an die nächste Session,
  der in keiner Leseordnung stand. Alle acht wurden im selben Zug
  entschieden und gebaut: **fünfter Session-Typ „Prüfung"**, die
  **Übergabe in `PLAN.md`** samt Schritt „Plan nachziehen" in `/ende`,
  die Chronik-Ausnahme zur Verweisregel und die Umzugsregeln als
  Abschnitt 11 der `DOC_RULES.md`. Vor dem Archivieren wurden sieben
  Regeln aus den Arbeitsdateien gerettet, die nur dort lebten — darunter
  der Prüfbogen und Isors fünf Grenzen für den Harness. Der erste
  Pflegetag lief (drei Artifact-Funde), die Seiten `⚙️ System · Harness`
  und `📍 Status` wurden gebaut bzw. neu gebaut, und die Artifact-Seiten
  haben eine verbindliche Farbwelt bekommen. Das Backup fällt auf Isors
  Wunsch aus dem Pflegetag heraus. Ausgeliefert nach
  `C:\IsorBackup\05_Werkzeuge\Harness_Auslieferungen\Harness_1.0.0\`,
  als **Vorlage statt Kopie** — 24 Dateien, 3.028 Zeilen.
  Geprüft: INDEX neu erzeugt (44 Dateien, alle mit Ownership-Zeile) ·
  das INDEX-Skript läuft in der Auslieferung eigenständig · nach dem
  Archivieren zeigt kein lebender Verweis mehr auf die drei
  Arbeitsdateien. Nicht geprüft: die rund zwanzig Dateien, die an diesem
  Tag geschrieben wurden — das gehört einer frischen Session.
