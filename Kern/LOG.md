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
- 2026-08-23 — **Prüfung der Version 1.0.0**, Gegenstand Harness, in
  frischer Session: die vier neuen Regeln, die geretteten Regeln gegen
  die drei archivierten Arbeitsdateien und ein Durchgang quer über den
  Bestand ergaben **vierzehn Befunde** in `_HARNESS_PRUEFUNG_1_0_0.md`
  (acht muss · vier lohnt sich · einer bei Bedarf · einer ein Beleg ohne
  Auftrag), behoben wurde nichts. Der Beleg ist die Übergabe selbst: Die Session fand
  ihren Auftrag allein über die Leseordnung, ohne Zuruf — der Fall aus
  Befund A34 tritt nicht mehr auf. Die dichteste Stelle war das
  `GLOSSARY.md` mit drei falschen Zeilen aus zwei Bautagen; es ist ein
  von Hand gepflegtes Verzeichnis und steht in keiner Doku-Pflicht.
- 2026-08-23 — **Die vierzehn Befunde behoben und `pruefen.py` gebaut.**
  Alle Befunde der Prüfung sind erledigt; beim Beheben kamen zwei
  weitere Anzahl-Verstöße ans Licht, aus sechs gemeldeten Stellen wurden
  acht behobene. Das neue Werkzeug `Kern/Werkzeuge/pruefen.py` prüft
  Verweise, Chronik-Format, Befehle gegen ihre Arbeitskopie, Zahlwörter
  und das Glossar; es läuft bei jedem `/harness:sichern` und beim
  Session-Start, **meldet nur und ändert nichts**. Der erste Lauf ergab
  **45 Funde, davon rund 40 Fehlalarme** — geplante Dateien, Verweise auf
  fremde Bäume, ein Gegenbeispiel im Regeltext, Zeitangaben statt
  Listenanzahlen. Nach zwei Runden Schärfung: 4 Funde, davon einer echt
  — das Glossar führte „V-Nummer", `VERSIONIERUNG.md` nannte dieselbe
  Sache „Commit-Nummer". Daraus die Bauregel für jeden weiteren Prüfer:
  Ein Fund, den niemand nachprüfen kann, ist Rauschen, und Rauschen macht
  den Prüfer wertlos.
  Dazu aus Isors Einwürfen: Der **Session-Titel trägt jetzt den laufenden
  Abschnitt** in der Klammer, samt der Ruhezustände `zu` und
  `aufgehoben`; `WORKFLOW.md` hat einen Abschnitt **Die Prüfebenen**
  bekommen, weil sieben Stellen ohne Übersicht nicht mehr zu behalten
  waren. Die **Bestandsaufnahme der acht Altbestand-Artifacts** aus einer
  Parallel-Session wurde aus deren Scratchpad ins Repo gerettet — 540
  Zeilen, die an einem Temp-Ordner hingen. Drei Störungen festgehalten,
  darunter zwei eigene Fehlurteile.
  Zum Schluss die Ordnerstruktur zum ersten Mal ganz durchgesehen:
  `Assets\` des Harness-Repos enthält **14 Dateien, alle aus der
  Unity-Vorlage**. Daraus der Bauplan `_HARNESS_UMBAU_STRUKTUR.md` —
  der Harness wird sein eigenes Repo, null Weiterleitungen, der Notkern
  entfällt. Alle betroffenen Zeiger sind darin gesucht und aufgelistet,
  zwei davon liegen in **anderen Repos**.
  Geprüft: `pruefen.py` über 47 Dateien, 0 Funde · INDEX neu erzeugt,
  alle mit Ownership-Zeile · die ROADMAP von 224 auf 132 Zeilen zurück
  auf ihr eigenes Format gebracht.
- 2026-08-23 — **Harness 2.0.0: der Harness ist sein eigenes Repo.**
  Baustein 1 des Bauplans ausgeführt. Wurzel ist jetzt
  `C:\Repos Isor\Harness Project\`; der Inhalt von `Claude\` ist eine
  Ebene hochgezogen, `.git` mit ihm. Der Unity-Anteil ist archiviert —
  `Assets\`, `Library\`, `Logs\`, `Packages\`, `ProjectSettings\`,
  `UserSettings\`, die beiden `.csproj`, `.slnx`, `.vsconfig` und
  `.gitattributes`, dazu die beiden Weiterleitungs-`CLAUDE.md`. Getrackt
  waren vorher 123 Dateien, davon 57 Harness und 66 Ballast; jetzt sind
  es 58. Von der Platte gingen 1.843 MB `Library\`. Nichts gelöscht:
  alles liegt in
  `C:\IsorBackup\99_Archiv\_Zu_Loeschen\2026-08-23_Harness_Umbau_Struktur\`.
  Weggefallen sind der Notkern, die INDEX-Kategorie Wegweiser und zwei
  der drei `CLAUDE.md`. Nachgezogen wurden die zehn Befehlsdateien
  (Original und Arbeitskopie), beide Werkzeuge, `WORKFLOW.md` an zwei
  Stellen, `GLOSSARY.md` und die zwei READMEs in den **anderen beiden
  Repos**. Beim Ausführen kamen vier Dinge dazu, die der Bauplan nicht
  vorhergesehen hatte: `.claude\` lag schon auf der Zielebene, der
  Memory-Umzug entfiel ganz (der geöffnete Ordner blieb derselbe), die
  mitgetrackte PDF war ein bitgleiches Duplikat einer Datei im
  Datenbaum, und beide Skripte hätten `.claude\` und `.git\` künftig
  mitdurchsucht.
  Geprüft nach `DOC_RULES.md` 11.3 — 52 `.md`-Dateien und 8.634
  nicht-leere Zeilen vorher wie nachher · `pruefen.py` danach 0 Funde in
  allen fünf Prüfungen · INDEX neu erzeugt, 47 Dateien, alle mit
  Ownership-Zeile · die zehn Befehlsdateien von Hand gegengelesen, weil
  ihre absoluten Pfade außerhalb des Baums liegen und Prüfung 1 sie
  nicht sieht.
- 2026-08-23 — **Baustein 2: der erste Hook. Erzwingen statt erinnern.**
  `.claude\settings.json` trägt jetzt einen `SessionStart`-Hook, der
  `Kern/Werkzeuge/pruefen.py` beim Session-Start ausführt — Auslöser
  `startup|resume|clear|compact`. Damit hängt die erste der drei
  Skript-Prüfebenen nicht mehr an Claudes Erinnerung. Vor dem Bauen
  wurden die vier offenen Fragen des Bauplans gegen die Hook-Referenz
  geklärt: `SessionStart` kann eine Session **nicht** blockieren (Exit-Code
  und Fehler werden dort ignoriert), einfacher stdout wird **von selbst**
  als Kontext eingelesen, ein Fehlschlag kostet nur eine Meldung, und die
  Auslieferung erfasste den Hook bisher gar nicht.
  Daraus vier Dinge gebaut: die Vorlage `Kern/Vorlagen/settings.json` samt
  `README.md` und viertem Einrichtungs-Handgriff in `VERSIONIERUNG.md` ·
  **Prüfung 6** in `pruefen.py`, die Vorlage gegen Arbeitskopie hält ·
  der Schalter `--hook`, der die Herkunft der Ausgabe kennzeichnet ·
  `Kern/Bilder/` als Ort für Erklärskizzen, mit der ersten darin.
  Nachgezogen: `CLAUDE.md` Punkt 5 (melden statt ausführen, mit
  Rückfallebene), `WORKFLOW.md` an zwei Stellen, `GLOSSARY.md` um **Hook**
  und **Vorlage**.
  Zwei eigene Fehler beim Bauen gefunden und behoben: Die erste Fassung
  benutzte `$CLAUDE_PROJECT_DIR` in der Kommandozeile, was Git Bash
  voraussetzt — ohne Git Bash weicht Claude Code auf PowerShell aus, und
  der Hook wäre stumm kaputt gewesen; jetzt steht `${CLAUDE_PROJECT_DIR}`
  in der `args`-Form, die Claude Code selbst ersetzt. Und die Marker-Zeile
  sagte pauschal „ein zweiter Lauf ist unnötig", was die Läufe bei
  `/harness:sichern` stillgelegt hätte (Isors Einwand).
  Geprüft: `pruefen.py` 0 Funde in allen sechs Prüfungen · Prüfung 6 gegen
  vier nachgestellte Schäden gehalten und jedes Mal angeschlagen (Vorlage
  fehlt, `hooks`-Block entfernt, Matcher gekürzt, `settings.json` kein
  gültiges JSON) · INDEX neu erzeugt, 49 Dateien, alle mit
  Ownership-Zeile · die Kommandozeile in Git Bash gelaufen, Exit 0.
  **Nicht geprüft: ob der Hook wirklich feuert.** Das zeigt erst der
  nächste Session-Start; Erkennungszeichen ist die Zeile
  `[SessionStart-Hook]` **ohne** sichtbaren Werkzeugaufruf.
  Ins Knowledge gingen zwei Seiten: die Hook-Mechanik samt Matcher-Falle
  und Shell-Falle (`Werkzeuge/`) und das Prinzip dahinter,
  „Stille ist mehrdeutig" (`Patterns/`) — eigenes Repo, eigener Commit.
