# LERNLOG.md — Isors Lernverlauf

Ownership: Nur das Lern-Log — die laufende Aufzeichnung, was Isor selbst geschafft hat,
wo Gerüste oder Hilfe nötig waren und welche Fehlerbilder auftraten —
das Rohmaterial, aus dem die Zeugnisse lesen (`ASSESSMENT_RULES.md`).
Keine Bewertung und keine Muster-Deutung: Die passiert im Zeugnis, nicht
hier. Kein Projektfortschritt: Das ist das LOG der Schicht.
Format: `- JJJJ-MM-TT · <Kontext> — ` dann bis zu drei benannte
Halbsätze: **Selbst:** … · **Hilfe:** … · **Fehlerbild:** … — nur
belegte Felder, eine bis drei Zeilen. **Älteste oben**, wie in einer
Chronik.

**Wer schreibt:** Claude, laufend während der Arbeit — sobald etwas
selbst gelang, ein Gerüst oder eine Erklärung nötig war oder ein
Fehlerbild auftrat. Die Doku-Pflicht (`WORKFLOW.md`) fragt bei jedem
Sichern nach, ob die Zeilen des Abschnitts geschrieben sind — das Netz
gegen das Einschlafen, nicht der Auslöser.

**Reist nicht mit:** Diese Datei beschreibt eine Person, nicht den
Harness. Die Packliste (`VERSIONIERUNG.md`) und `ausliefern.py` lassen
sie bei jeder Auslieferung weg — wie `Kern/Zeugnisse/`.

---

*Erstbefüllung rückwirkend am 2026-09-04, aus Session-Verlauf, LOG und
Knowledge-Notizen — lückenhaft, weil vor diesem Datum nur festgehalten
wurde, was die Chroniken ohnehin trugen. Ab hier wird laufend geführt.*

- 2026-08-28 · Baustein A, Dienst und Menüwege — **Selbst:**
  `ISessionService` und `RelaySessionService` kleinschrittig selbst
  getippt (Entwurf vor Gerüst). **Fehlerbild:** vier Verdrahtungsfehler
  in der Szene, gefunden per Skript-Audit, nicht beim Bauen. *(aus
  `Projekte/Isor_Tower/LOG.md`)*
- 2026-08-30 · Rückweg-Feld des Menüs — **Fehlerbild:** Zuweisung
  dreimal seitenverkehrt (`_menuPanel = _lobbyBackTarget`) — der
  Inspector-Verweis wäre mit null überschrieben worden; im Review vor dem
  ersten Test gefunden. **Hilfe:** Merksatz „links steht der Empfänger".
  *(aus `Knowledge/CSharp/zuweisung-links-empfaengt.md`)*
- 2026-09-01 · `HostOptionsPanel` getippt — **Selbst:** die ganze Klasse
  nach Gerüst selbst geschrieben; `ChangePlayerLimit` (Clamp plus
  Anzeige) auf Anhieb richtig; Konstanten-Konvention richtig angewandt.
  **Fehlerbild:** vier Review-Runden — Dateiname ≠ Klassenname;
  `GetString` ohne Zuweisung (Rückgabewert verfiel); `SetString` mit der
  Konstante statt des Feldinhalts — dieselbe Quelle-Ziel-Verwechslung,
  einmal je Richtung; `blocksRaycasts` statt `interactable`, und der
  else-Zweig setzte nichts zurück. **Hilfe:** Kontrollfrage „Wer soll
  den Wert am Ende haben?" — saß danach.
- 2026-09-01 · Lobby-Design — **Selbst:** die eigene Scrollbar-Verwerfung
  mit einem neuen Argument widerrufen (Bewertung statt Vorführung) und
  den Spieler-Deckel 6 anhand gerechneter Tafelhöhen entschieden — beides
  Entscheidungen an Zahlen statt am Gefühl.
- 2026-09-02 · Verdrahtung im Menü-Controller — **Selbst:** die Trennung
  GameObject gegen Komponente („Frontend/Backend") ohne Anleitung
  gefunden; `_isPlayingAlone` als nötigen Merker erkannt; gegen doppelten
  Code selbst eine Hilfsmethode gezogen (Instinkt richtig, Zeitpunkt zu
  früh). **Fehlerbild:** `[SerializeField]` fehlte, das Feld stand im
  Laufzeit-Block; Umbenennung ohne die Geschwister, obwohl die eigene
  Regel dazu bereitstand.
- 2026-09-04 · Umzug der Dienst-Aufrufe und Tafelbau — **Selbst:** den
  Umzug in die Bestätigungs-Methode fast vollständig allein entworfen
  (nur das `Create`-Rohr für die Spielergrenze fehlte im Entwurf); die
  Tafel nach Bauplan in die Szene gebaut; `0.4f` selbst als Magic Number
  erkannt und zur Konstante gemacht; den Prefab-Bedarf (Button, Tafel,
  InputRow) selbst vorgeschlagen. **Fehlerbild:** dreimal
  „Editor-Wahrheit gegen Platten-Wahrheit" (VS-Puffer, Nur-aktive-Datei
  gespeichert, ungespeicherte Szene); `playerlimit` statt `playerLimit` —
  Signatur abgetippt statt kopiert. **Hilfe:** Klickpfad-Anleitung für
  die sieben Bauschritte; die Inspector-oder-Code-Regel beim Abfragen im
  Kern richtig, nur mit „Netzwerk" statt „später" begründet.
- 2026-09-05 · Design-Runde UI-Prefabs — **Selbst:** die Stempel-Form
  (Vorlage reinziehen und entpacken) als eigene dritte Option
  eingebracht, die in Claudes Zwei-Wege-Bewertung fehlte; das Ziel
  „einmal richtig aufbauen statt Flickwerk" selbst gesetzt und dabei
  benannt, Kriterien statt Rezepte lernen zu wollen. **Hilfe:** die
  Abgrenzung verbunden · Stempel · kein Prefab kam als Merk-Tabelle von
  Claude, samt Laufzeit-Argument für die `LobbyPlayerRow`.
- 2026-09-06 · Prefab-Umzug des Hauptmenüs — **Selbst:** die vier
  HostOptions-Knöpfe gegen Claudes Positions-Ansage richtig als
  Layout-Fall erkannt und mit LayoutElement gebaut („wie es davor war")
  — die angesagten Koordinaten waren nur das gespeicherte Ergebnis der
  HorizontalLayoutGroup; dazu den Join-Code-Winzling eigenständig auf
  200×50 vergrößert. **Fehlerbild:** an Back- und Confirm-Knopf die
  OnClick-Verdrahtung vergessen — vom Skript-Abgleich gefunden, nicht
  beim Bauen. **Hilfe:** Verdrahtungs-Ansagen je Knopf aus dem
  Vorher-Protokoll.
- 2026-09-06 · Schritt 5, Panel und Zeilen-View — **Selbst:**
  Spawner-Handler samt `SpawnWithOwnership` allein; `OnReadyClicked`
  auf Anhieb fehlerfrei; `TryGetValue` nach einem Hinweis sauber
  übernommen; eigene Funde: fehlendes LayoutElement am neuen
  Start-Knopf, das MPPM-Namens-Wettrennen korrekt auf geteilte
  PlayerPrefs getippt, den Bereit-Haken zur Sichtbarkeits- statt
  Farbfrage umentschieden, MaxPlayers-Doppelpflege als Wartungsfalle
  erkannt (führte zur Service-Property); beim API-Streit dreimal auf
  dem Editor-Befund beharrt — Auflösung durchs Lesen der
  Obsolete-Meldung, beide lagen halb daneben. **Fehlerbild:** zweimal
  Objekt statt Komponente erzeugt (Roster — Merksatz:
  Hierarchy-Rechtsklick baut Objekte, Add Component baut Fähigkeiten);
  Fallthrough nach if zweimal; im Dictionary gesucht statt
  nachgeschlagen (`row == player` über zwei Typen); Ping-Kette Quelle
  vor Ziel plus vertauschte Farbstufen. **Hilfe:**
  Existenz-gegen-Zustand als Antwort auf die eigene
  Awake/Start-Regel-Frage; `.Values`/`.gameObject`-Griffe; Gerüste mit
  vordeklarierter NGO-Syntax.
- 2026-09-06 · Erste Netz-Klasse (`LobbyPlayer`) — **Selbst:** Entwurf zu
  drei Vierteln richtig (Werte, Lebenszyklus, ein-Objekt-je-Spieler);
  beide RPC-Rümpfe und `OnNetworkSpawn` auf Anhieb, PlayerPrefs-Key
  eigenständig zur Konstante gezogen; den Spawner-Handler samt
  `SpawnWithOwnership` gefüllt, erster Live-Test erfolgreich.
  **Fehlerbild:** im Ping-Takt zuerst Schreiben vor Messen — dieselbe
  Quelle-Ziel-Verwechslung wie am 01.09., über die eigene Kontrollfrage
  („Wer soll den Wert am Ende haben?") selbst aufgelöst; beim Entwurf
  Owner-Schreibrecht statt Host-Schreibrecht angesetzt (am Ping-Argument
  verstanden). **Hilfe:** NetworkVariable-Deklarationssyntax und
  RPC-Attribute als Gerüst, Cast-Hinweis ulong→int, Sortier-Fragen statt
  Lösung.
  Claudes Datei-Befund dreimal auf dem eigenen Inspector-Blick bestanden
  („da ist nichts drin") und recht behalten — der Parser las verwaiste
  Listen-Overrides als wirksam, obwohl `Array.size = 0` sie aufhebt;
  dazu zweimal die Stil-Ansage mit bestandskonformeren Werten
  überstimmt (Zähler in LiberationSans nach der Value-Konvention,
  Caption im Feld-Label-Stil). **Fehlerbild:** Objektname „Roaster",
  drei leere Rest-Images im Roster, ein Speicherstand-Versatz
  (Stern-Regel). **Hilfe:** Klickpfade je Runde, Häkchen-Sprite von
  Claude generiert, Maß-Nachträge aus dem Audit.
- 2026-09-06 · Lobby-Chat, Abendabschnitt (Regler: Claude schreibt) —
  **Selbst:** die Chat-UI nach Schrittliste in der Szene gebaut und
  dabei vorgegriffen (ScrollRect samt Clamped und Verdrahtung, Rich
  Text aus, Character Limit 100 — vor der jeweiligen Ansage); beim
  Font-Zwischenfall das Muster „kommt wieder, egal was ich tippe"
  präzise gemeldet — der Schlüssel zur Diagnose; Polishing-Befunde
  eigenständig gesammelt (Scroll zu flott, Feldgrößen,
  Fullscreen-Frage, Namensgrenze) und die Semester-Reihenfolge aus dem
  Kopf richtig rekonstruiert (deckte sich mit der ROADMAP).
  **Fehlerbild:** im Debug-Inspector einen leeren Persistent-Call
  angelegt (Rohansicht nicht als solche erkannt); das Eingabefeld
  zunächst als Kind in den Scroll-Verlauf gehängt (Umhäng-Versatz
  Pos Y 131 blieb stehen). **Hilfe:** Hierarchie-Soll als Diagramm,
  nachgerechnete Anker-Werte, onSubmit-Abo in den Code verlegt. Das
  Gegenlesen der RPC-Kette ist bewusst auf morgen vertagt.
- 2026-09-06 · Abend-Abfrage, sechs Fragen auf Isors Wunsch —
  **Selbst:** Host-Stempel-Begründung vollständig richtig (Manipulation,
  Name aus dem Netzobjekt); Event-Abo-Muster samt Ansammlungs-Argument;
  die Chat-Kette ohne Code-Lektüre zu gut der Hälfte hergeleitet
  (Objekt je Spieler, Weg über den Host); Unsicherheiten präzise selbst
  markiert — die Markierungen deckten sich mit den echten Lücken.
  **Fehlerbild:** Kernmuster Zustand-gegen-Ereignis nicht abrufbar (auf
  die Wann-Frage kam Syntax statt Kriterium; Späteinsteiger- und
  Rundreise-Teilfragen blieben unbeantwortet); `IsOwner`/Besitz nicht
  als Werkzeug genannt, obwohl selbst verbaut; die Zerlege-Aufgabe als
  „Aufgabe unklar" blockiert, während das Konzept (Kamera lokal, nur
  Positionen reisen) im selben Diktat richtig kam — die eigene
  Diagnose „Zerlegen ist die Baustelle" damit doppelt bestätigt.
  **Hilfe:** Schneide-Schablone nachgereicht (Normalfall → Weiche →
  Aufräumen → Beweis) plus Drei-Gewohnheiten-Plan für wenig Zeit
  (eigene Schrittliste vor jeder Claude-Liste, eine
  Wiederhol-Frage je Session-Start, Fragerunde je Baustein-Ende —
  Ritualisierung offen, Isor entscheidet bei der nächsten Sicherung).
- 2026-09-06 · Design-Session Gras-Assets (Blender) —
  **Selbst:** Die Design-Session geführt und ihre Grenze verteidigt —
  den Bau zweimal gestoppt, als Claude vor der Entscheidung zu
  modellieren begann. Formfehler am Bild eigenständig erkannt und
  benannt („zu arg geknickt"), was auf eine echte Konstruktionsursache
  führte (Krümmung auf zwei Segmente gedrängt). Nach dreimaligem
  Danebenliegen die entscheidende Abhilfe selbst geliefert:
  Referenzbilder, aus denen sich Proportionen messen ließen. Alle
  Design-Entscheidungen selbst getroffen, darunter der Umschwenk vom
  großen Büschel auf viele kleine.
  **Hilfe:** Übersetzung des Vorbilds in Zahlen (Seitenverhältnisse,
  Biegewinkel, Halmzahl), die Messverfahren für Deckung und Pixelgröße.
- 2026-09-07 · Noten-Auswertung und Stack-Entscheidung — **Selbst:** die
  D004-Lücke eigenständig diagnostiziert (zu wenig Spielmechaniken, weil
  einzelne Systeme zu komplex — Tiefe fraß das Breite-Budget) und die
  Berufslogik C++ → C# selbst hergeleitet; die Engine-Entscheidung trotz
  benannter Angst getroffen und den Anker samt Notausgang selbst
  eingefordert; eigene Ängste präzise benannt (C++, KI-Abhängigkeit,
  Veränderung). **Fehlerbild:** Entscheidungs-Schleife — jedes „Aber"
  lud das nächste nach, zwei abgebrochene Auswahlfelder, bis die Punkte
  einzeln beantwortet waren. **Hilfe:** Fakten-Gegenlese je Angst
  (Modul verlangt C++ ohnehin, Kommentar-Zitate, Beispiel-Spiele) und
  der DECISIONS-Eintrag mit Kontrollpunkt als Anker gegen die
  Grübelschleife.
- 2026-09-08 · Werkzeug-Setup C++/Unreal — **Selbst:** beide neuen Repos
  über GitHub Desktop committet und veröffentlicht (Lane-Defender samt
  Push, Isor-Tower-Unreal privat) und Unreal 5.6.1 samt Bridge- und
  Fab-Plugin-Warteschlange installiert — alles ohne Klickanleitung.
  **Hilfe:** Einordnung des hängenden „Überprüfen 99 %"
  (Task-Manager-Datenträger statt Launcher-Anzeige prüfen) und der
  Toolchain-Frage VS 2026 gegen UE 5.6.
- 2026-09-08 · C++-Unterricht Chapter 1 (Stoff nur gehört, nicht
  getippt — alle Code-Screenshots stammen vom Beamer) — **Selbst:**
  `argc` als Elementzahl und `return 0` als Exit-Code ans
  Betriebssystem richtig eingeordnet, die Literale-Regel des Dozenten
  sinngemäß wiedergegeben (nicht nur Zahlen, auch Strings), die
  Vorinitialisierungs-Pflicht behalten. Stärkster eigener Beitrag: der
  Einwand, der 3D-Model-Viewer sei doch ebenfalls ein Konsolenprojekt —
  daraus wurde eine echte Lücke in `Kern/CODE_GUIDELINES.md` und ein
  ROADMAP-Punkt. **Fehlerbild:** drei Übertragungsfehler aus C#, alle
  vom selben Muster — bekannte Wörter auf neue Bedeutung gelesen:
  `a_` als „Member" gedeutet statt als Parameter (Member ist `m_`,
  lokale Variablen tragen gar kein Rollenpräfix); C → C++ → C# als
  Versionsreihe gelesen statt als drei eigenständige Sprachen; „Vector"
  aus `argv` auf `std::vector` übertragen, obwohl das eine ein festes
  Array und das andere der Listen-Container ist. **Hilfe:** der
  Adress-gegen-Inhalt-Vergleich in Zahlen aufgeschrieben, die
  Präfix-Tabelle aus den CODE_GUIDELINES gegen seine Deutung gehalten.
  Dazu ein Hemmnis abgeräumt, das kein Wissenslücken-Problem war: Die
  Lesbarkeit der Systems-Hungarian-Notation hatte die Lust am
  Konsolenprojekt spürbar gedrückt („ich mag es nicht") und drohte auf
  den Stack überzugehen. Getrennt wurde beides über die belegte Zahl
  aus `Projekte/Lane_Defender/ZEITPLAN.md` — 36 h, danach gilt die
  Notation nirgends mehr — und den Vergleich mit dem Epic-Standard, der
  bis auf `b` für bool ohne Typkürzel auskommt. Die Stack-Entscheidung
  wurde dabei nicht neu aufgemacht (Anker vom 2026-09-07,
  Kontrollpunkt Ende November).
- 2026-09-09 · L1, erstes eigenes C++-Projekt — **Selbst:** VS-Projekt
  nach Anleitung angelegt, kompiliert und den Debugger bedient
  (Breakpoint, F5, Locals gelesen); die SAE-Konvention unaufgefordert
  selbst eingefordert („wir sind doch im Konsolenprojekt") — einen Tag
  nach „ich mag es nicht"; Commit V 0.0002 mit sauberem Inhalt selbst
  gebaut. **Fehlerbild:** Wiederholung vom 2026-09-08, andere Richtung:
  `a_ILive` für eine lokale Variable — das Rollenpräfix `a_` (Parameter)
  diesmal auf eine Lokale gesetzt statt auf einen Member gedeutet, dazu
  Typkürzel `I` groß statt klein. Das Rollenpräfix-System ist als System
  noch nicht verankert. **Hilfe:** Präfix-Tabelle erneut, Strg+R,R als
  Umbenennen-Werkzeug, Einordnung des Locals-Werts 0 (frisch genullter
  Stack, keine Garantie — der gelebte Grund für SAE-Regel 7).
- 2026-09-09 · L2 Ü1, Typen nach SAE — **Selbst:** den eigenen Lernraum
  verteidigt („keine Lösung zeigen, will es selber erst machen"), dann
  alle vier Variablennamen beim ersten Selbstversuch SAE-korrekt
  (`iLives`, `fSpeed`, `bIsRoundRunning`, `sPlayerName`) — das
  Rollenpräfix-Fehlerbild vom Vormittag trat nicht wieder auf; das
  Float-Suffix `f` aus C# richtig übertragen; die bool-Überraschung
  (Ausgabe 1 statt true) selbst gefunden und präzise gemeldet.
  **Fehlerbild:** `#include <string>` weggelassen, obwohl vorab
  angesagt — kompilierte nur, weil MSVCs iostream den Header transitiv
  mitliefert. **Hilfe:** Auflösung bool = kleine Zahl samt
  `std::boolalpha` als Werkzeug; Datei-Header und Ausgabetext-Korrekturen
  übernahm Claude nach Arbeitsteilung.
- 2026-09-09 · L2 Ü2, Kontrollfluss — **Selbst:** die drei Pflichtstücke
  (for, if/else, while) eigenständig zu einer verschachtelten
  Runden-Spielschleife komponiert statt sie einzeln abzuliefern; Literale
  von sich aus in benannte Werte gezogen (vor Behandlung von SAE-Regel
  11); alle Folge-Fixes selbst gebaut — Lane-Offset samt treffender
  Umbenennung, Rundenzähler durch Verschieben des Inkrements, Guard
  Clause mit `break` am Schleifenkopf und dabei defensiv `<=` statt `==`
  gewählt; beim Konstanten-Umbau Regel gegen Zustand sauber getrennt und
  MACRO_CASE samt großem Typkürzel fehlerfrei angewandt; testet
  Änderungen jetzt selbst, bevor er sie abgibt. C#-Transfer der
  Trainingsfrage 2/3: beide Compiler-Reaktionen auf `if (iLives)`
  korrekt vorhergesagt. **Fehlerbild:** die Zahl-als-Wahrheit-Regel
  falsch gedeutet („solange es 3 ist" statt „0 ist die einzige falsche
  Zahl"); das while als Dauer-Wächter verstanden statt als Prüfung nur
  am Kopf — deshalb am Vergleich (`>=`) experimentiert statt am
  Zeitpunkt; Lane-Ausgabe 0-basiert (Off-by-one); in der Verlust-Meldung
  den Reststand statt des Verlusts ausgegeben (bekanntes
  Quelle-Ziel-Muster); Game Over eine Runde zu hoch gezählt.
  **Hilfe:** Zahlen-Trace der Runde 2 plus Ablauf-Diagramm der
  Prüf-Zeitpunkte (Türsteher gegen blinde Zone); Zielbild mit
  Erfolgskriterium (bekannte Eingabe 5 → „Game Over in Round 2", nie
  −1); Konstanten-Aufgabe als Regel-gegen-Zustand-Frage gestellt.
- 2026-09-10 · C++-Unterricht UE 1, Praxisübung Formelrechner (45-min-
  Zeitbox, erste selbst getippte Übung im Unterricht) — **Selbst:**
  `GetInput()` samt Eingabe-Validierung nach Gerüst gebaut — deckt die
  offenen L2-Themen Funktionen und Validierung vorweg; erster Lauf mit
  den Kontrollzahlen exakt richtig (31.4159 / 78.5398). Für den
  vorgewarnten ignore-Hänger eine **eigene** Lösung gebaut (Aufräumen
  ans Schleifenende verlegt statt Claudes if-Vorschlag) — robuster als
  der Vorschlag, weil sie auch Restzeichen wie `.7` mit ausräumt;
  `numeric_limits<streamsize>::max()` statt Literal verbaut; SAE-Namen
  durchgängig korrekt (`bInputHasFailed`, `iRadius`, `dArea`).
  Verständnisfrage selbst gestellt (warum `int32_t` statt `int`).
  **Fehlerbild:** die Linker-Stufe war unbekannt — LNK2005 (doppelte
  `main`) nicht einordnen können und die Error List nicht als Stand des
  letzten Builds erkannt (Datei gelöscht, Fehler „blieb");
  Wiederholung vom 2026-09-09: benutzter Header nicht selbst included
  (`<limits>`, damals `<string>`) — kompilierte nur über MSVCs
  transitive Includes; `system("cls")` direkt nach der Ausgabe wischte
  das Ergebnis weg. **Hilfe:** Compiler-gegen-Linker-Zweistufigkeit
  samt Lese-Regel (LNK- vs. C-Präfix); Vorwarnung, dass `ignore()` vor
  der ersten Eingabe blockiert; Typbreiten-Erklärung (int ohne
  Größengarantie, `_t`-Familie, Brücke zu Unreals `int32`).
- 2026-09-11 · Lane Defender Ü3 Funktionen (L2, erste Funktions-Übung
  ohne Gerüst) — **Selbst:** PrintMessage-Überladungsfamilie und
  LoseLives entworfen; die Signatur-Lücke (aktueller Lebensstand fehlt)
  nach sokratischer Rückfrage selbst geschlossen; `int32_t` gegen die
  SAE-Beispiel-Praxis selbst begründet (explizite Breite) und
  konsequent durchgezogen; statt der empfohlenen float-Umstellung
  eigenständig getrennte int32/float-Überladungen gebaut — die bessere
  Lösung; `I_ADD_ROUND` ungefragt zur Konstante gemacht; C2084 über
  Semikolon-Prototypen behoben, Default-Werte korrekt nur in die
  Prototypen gesetzt; Überladungswahl („billigster Weg") danach in
  eigenen Worten richtig erklärt. **Fehlerbild:** „kompiliert" mit
  „fertig" verwechselt — Regressionslauf ausgelassen (Unterbrechung im
  Alltag) und Warnungen in der Error List ausgeblendet, dadurch
  float→int32-Abschneiden (C4244) und bool→1 unbemerkt;
  `iLives -= LoseLives(...)` — Abzug doppelt gerechnet, Spiel endete
  nie; Prototypen zunächst als Leer-Definitionen `{}` getippt (C2084
  als Schwester des LNK2005 aus UE 1); boolalpha zunächst als
  Umwandlungs-Zwang gedeutet statt als Anzeige-Schalter. **Hilfe:**
  Überladungsauflösung (Anzahl, dann billigste Umwandlung) als
  Diagramm; Deklaration gegen Definition am Semikolon erklärt; Regel
  für Default-Argumente (nur im Prototyp); cout-eigener bool-Weg.
- 2026-09-12 · Lane Defender Ü4 Eingabe-Validierung (L2, letzter
  Übungspunkt vor L3) — **Selbst:** die ganze Übung ohne Gerüst gebaut —
  eigene Funktion `ReadValueInput` mit Warteschleife, `fail`/`clear`/
  `ignore` in der richtigen Reihenfolge, Bereichsprüfung als zweite
  Ebene, `<limits>` wie beauftragt selbst included (das
  Include-Fehlerbild vom 09./10.09. trat nicht auf); das
  Nur-Enter-Verhalten eigenständig entdeckt und präzise gemeldet
  („fail merkt es nicht, wenn leer"); nach der Parameter-Erklärung den
  Umbau (Signatur auf `a_iMinLives` geschrumpft, Arbeitsvariablen in die
  Funktion, `continue` gegen die Doppel-Meldung) komplett selbst
  getippt; die leere Eingabe bewusst als Standardverhalten belassen
  (stilles Warten, kein Umbau). Testreihe `abc`/`-3`/`0`/`5` bestanden —
  je Fehleingabe genau eine Meldung, 5 startet das Spiel; belegt durch
  Claudes Gegenlauf, kompiliert warnungsfrei unter /W4.
  **Fehlerbild:** Parameter als Zugriffsweg gedeutet („die Funktion kommt
  nicht an mains Variablen, also gebe ich sie mit") — Arbeitsvariablen
  durch die Parameterliste gereicht statt lokal angelegt; beim Umzug in
  die Funktion beide Lokale erneut mit `a_`-Präfix (`a_iInput`,
  `a_bValidInput`) — dritte Auflage des Rollenpräfix-Fehlerbilds vom
  2026-09-08/09, das System ist weiter nicht verankert; Doppel-Meldung
  bei `abc` übersehen (Fallthrough nach dem if, bekanntes Muster vom
  2026-09-06). **Hilfe:** Whitespace-Regel von `>>` erklärt (Enter ist
  Whitespace — Warten, kein Fehlerzustand; peek/getline als Wege
  gezeigt); Merksatz „Parameter ist eine Tür für Wissen des Aufrufers,
  eine lokale Variable ist Werkzeug der Funktion" samt Diagramm;
  `continue` als Schnitt gegen den Fallthrough.
- 2026-09-12 · Lane Defender L3 Ü1, Adressen im Debugger — **Selbst:**
  die Übung nach Zettel durchgeführt (Breakpoint, Watch mit `&`,
  Frame-Wechsel über den Call Stack) und die Abnahme-Erklärung im Kern
  richtig: zwei Variablen, zwei Container, darum zwei Adressen
  (`0x…ee6fefa0` gegen `0x…ee6ff0a4`); dazu den Müllwert eines noch
  nicht zugewiesenen `iLives` eigenständig entdeckt und präzise
  gemeldet. **Fehlerbild:** Breakpoint zunächst am return der falschen
  Funktion (ReadValueInput statt LoseLives); die Frame-Bindung des
  Watch-Fensters unbekannt — „identifier is undefined" als Defekt statt
  als „wohnt hier nicht" gelesen; in der Erklärung den Parameter „nur
  eine lokale Variable" genannt (Karton-Verhalten richtig, der
  Tür-Begriff vom Vormittag noch nicht angewandt). **Hilfe:** Klickpfad
  samt Ebenen-Diagramm (der Watch fragt die markierte
  Call-Stack-Ebene); Einordnung des Müllwerts als gelebter Grund der
  Vorinitialisierungs-Regel.
- 2026-09-12 · Lane Defender L3 Ü2, erster Pointer — **Selbst:** das
  Snippet komplett ohne Gerüst gebaut (nullptr-Start, `&`-Verbindung,
  Wächter mit Fehler-Rückgabe, Schreiben über `*`), eigenständig
  getestet (beide Ausgaben 1) und daraus die richtige Kernregel selbst
  formuliert: „überschreibt nicht die Adresse, sondern schreibt in die
  Adresse rein"; SAE-`p`-Präfix auf Anhieb; die Sinnfrage („warum nicht
  direkt in die Variable?") selbst gestellt — und das Urteil dahinter
  stimmt: Neben dem sichtbaren Namen ist ein Pointer ein Umweg.
  **Fehlerbild:** in der Trainingsfrage das Umhängen übersehen —
  `p = &iRounds` nicht als Zustandswechsel des Pointers gelesen und
  die 7 gedanklich ans alte Ziel geschrieben; die Ebene „wohin zeigt
  er" war als Einmal-Setup verbucht, während die Ebene „was liegt
  dort" sicher saß. Dazu die Sprach-Unschärfe „der Pointer hat 7" (ein
  Pointer hat nie den Wert, nur die Hausnummer). Vorab die Rückmeldung
  „zu wenig visuell, ich habe noch nie einen Pointer gesehen" —
  berechtigt, der Theorie-Happen vor dem Entwurf war übersprungen.
  **Hilfe:** interaktives Karton-Modell (Zeigen/Lesen/Schreiben/nullptr
  samt Wächter-Toggle), der Skill-Slot aus den eigenen DECISIONS als
  Antwort auf die Sinnfrage, Zahlen-Trace und ein zweites Modell mit
  zwei Zielkartons zum Umhängen.
- 2026-09-12 · Lane Defender L3 Ü3, const-Referenzen an PrintMessage —
  **Selbst:** zwei der drei string-Überladungen im ersten Anlauf an
  beiden Orten (Prototyp und Definition) korrekt umgestellt, die dritte
  nach Claudes Befund selbst nachgezogen; Regressionslauf eigenständig
  gefahren und im Gegenlauf bestätigt (Eingabe 5 → „Game Over in
  Round 2", /W4 warnungsfrei); am Hover die richtige Detektiv-Frage
  gestellt (const char[36] vorher wie nachher — gemessen an der einen
  Station, die sich nie ändert) und die Wortfragen (Adressoperator,
  Referenz, Literal) aktiv eingefordert. **Fehlerbild:** das const
  zunächst weggelassen (non-const-Referenz hätte an den
  Literal-Aufrufen den Build gebrochen); die Referenz hartnäckig als
  Speichern-Vorgang modelliert („schreibt die Zeichen in die Adresse
  rein, immer die gleiche") — dass die Zeichen schon am Ziel liegen und
  nur gelesen wird, brauchte zwei Anläufe; zwischenzeitlich Frust
  („weiß nicht, ob ich doof bin") — Auslöser war Claudes
  Stapel-Erklärung (Temporär, Literal, Lebensdauer in einem Zug statt
  einer einzigen Unterscheidung). **Hilfe:** der Vergleich „zwei
  Adressen gegen eine Adresse — kopieren oder Hausnummer durchreichen"
  als Auflösung; Referenz als „Pointer im Autopilot" an das
  Ü2-Wissen gehängt; Vokabeltafel zu `*`/`&` nach Ort und die
  Literal-Definition an seinen eigenen Codebeispielen.
- 2026-09-12 · Lane Defender M1, Design-Auftakt — **Selbst:** den
  Programmablauf eigenständig als Szenen-Modell entworfen (Hauptmenü →
  Namenseingabe → Spiel → Endszene, hergeleitet aus der
  Unity-Szenen-Analogie) samt Bedienkonzept (Pfeile/W+S,
  Auswahlmarker) — trägt direkt den Zustandsautomaten des M1-Gerüsts;
  dazu die Highscore-Idee, die sich mit Ausbau A2 der ROADMAP deckt;
  beim Gegenlesen des Ablaufs die fehlende Steuerungs-Anzeige selbst
  bemerkt und als Zwischenszene nachgezogen.
- 2026-09-12 · Lane Defender M1, Abnahme Console-Baustein — **Selbst:**
  den Header ohne Anleitung als „Versprechen, Definition in der .cpp"
  gedeutet (Transfer aus den Ü3-Prototypen), `&lConsoleMode` als
  Schreiben über die Adresse gelesen (L3-Transfer),
  `INVALID_HANDLE_VALUE` korrekt als −1 getippt, Guard-Struktur und
  die Scan-Code-Übersetzung erkannt; Includes selbst mit C#-usings
  verknüpft. **Fehlerbild:** „if-Schleife" als Wort; die Prefix-Codes
  224/0 zunächst als „nicht legitime" Tasten gedeutet statt als
  Ankündigung des zweiten Codes; `#define`, Header-Rolle und `flush`
  unbekannt — neuer Stoff, kein Verwechsler. **Hilfe:**
  Compiler/Linker-Diagramm (C- gegen LNK-Fehler an den eigenen Fällen
  C2084/LNK2005), define = Textersetzung, flush = Sammelmappe leeren,
  Out-Parameter als Tür für die Antwort. Transferfrage danach: .h/.cpp-
  Zuordnung sicher; die fehlende Einlösung aber als Compiler- statt
  Linker-Fehler getippt (LNK2005 aus UE 1 nicht mehr abrufbar). Dazu
  offen benannter Motivationsknick: der WinAPI-Teil wirkt „kryptisch,
  in C# würde ich das verstehen" — Auslöser ist die
  Betriebssystem-Schicht des gelieferten Bausteins, nicht der eigene
  C++-Code (dieselbe Quelle wie das SAE-Hemmnis vom 2026-09-08).
- 2026-09-12 · Lane Defender M1, Vertiefung InitConsole (interaktive
  Stationen-Maschine) — **Selbst:** den Out-Parameter präzise erklärt
  („Adresse ist der Ort, an den GetConsoleMode schreiben soll, keine
  Kopie") und dazu eigenständig das richtige API-Schnittstellen-Bild
  gebildet; den Zweck des VT-Bits in eigenen Worten („Befehle bleiben
  unsichtbar und wirken"); die Fail-Pfade der Guards korrekt gelesen.
  **Fehlerbild:** Bit-Wert mit Bit-Position verwechselt („Bit 4" als
  viertes Bit gelesen); die Codepage als weiteres Modus-Bit
  einsortiert, obwohl sie ein eigener Schalter ist; den bool-Rückgabewert
  an „alle Bits gesetzt" geknüpft statt an „alle Handgriffe geklappt";
  führende Null in 0111 unklar. Teils von Claudes Lampen-Beschriftung
  und einer verunglückten Rechenfrage mitverursacht. **Hilfe:**
  Stellenwert-Tafel 8/4/2/1 samt 007-Vergleich für die führende Null,
  Trennung der zwei Ebenen (Handgriff-Erfolg gegen Schalter-Inhalt),
  Bytes-Brille für die Codepage (226/148/140 als Ôöî gegen ┌).
- 2026-09-12 · Lane Defender M1, Bit-Oder an InitConsole — **Selbst:**
  2 | 4 = 6 samt richtigen Lampen; nach der Spalten-Erklärung offen
  gesagt „ich verstehe | nicht" — präzises Selbst-Markieren der Lücke.
  **Fehlerbild:** | zunächst als + gedeutet (ging bei getrennten Bits
  zufällig auf); 4 binär als 0011 geschrieben (das wäre 3); die
  Folge-Antwort „bzw 0110" blieb mehrdeutig (Korrektur der eigenen
  Binärdarstellung oder 7|4-Versuch mit verrutschter 1er-Spalte).
  **Hilfe:** Spaltentafel mit Stellenwerten 8/4/2/1, Merksatz „an oder
  an = an", und das Plus-lügt-Beispiel 7+4 = 1011 (Übertrag verstellt
  Schalter, die niemand angefasst hat). Auflösung danach: die
  Kern-Einsicht „7 | 4 bleibt 7" selbst gezogen; hartnäckig blieb nur
  die Binär-Schreibweise — 7 zweimal als 0110 notiert, die 1er-Spalte
  fällt wiederholt weg. Gegenmittel: Merksatz „ungerade Zahl = letzte
  Stelle 1".
- 2026-09-12 · Lane Defender M1, SetConsoleMode-Zeile selbst zerlegt —
  **Selbst:** `ENABLE_VIRTUAL_TERMINAL_PROCESSING` = 0x0004 eigenständig
  in VS nachgeschlagen und richtig als „da kommt immer 4 raus" gedeutet;
  die Kette „SetConsoleMode gibt bool, darf nicht FALSE sein, sonst
  Abbruch" korrekt nacherzählt; die eigene Unsicherheit präzise benannt
  („was gerade im Modus drinsteht, weiß ich ja nicht") — genau die
  Lücke, die das Lesen-Oder-Zurückschreiben-Muster schließt.
  **Fehlerbild:** Rollen kurz vertauscht (Handle als „das Ausgelesene"
  statt als Ansprechpartner); `SetConsoleOutputCP` als „.cpp" gehört
  (Diktat); der Dreifachschritt der return-Zeile (Aufruf, Vergleich,
  return in einem) unklar. **Hilfe:** Wer/Was-Trennung
  (Handle = welche Konsole, Mode = was eingestellt ist),
  Hex-Kurzerklärung zu 0x, Get/Set-Anker an C#-Properties, die
  return-Zeile in Langform, BOOL als Zahl-Wahrheit an Ü2 angebunden.
  Fortsetzung nach eigener Gesamt-Nacherzählung: Ablauf Ausweis → Guard
  → Karton füllen sowie „dritte Stelle dazu, von 3 auf 7" jetzt korrekt
  wiedergegeben, „0 heißt automatisch false zurück" selbst gefolgert,
  und das eigene Nicht-Sitzen ehrlich markiert. Hartnäckig zwei
  Lese-Fehler mit derselben Wurzel (mehrere Schritte in einer Zeile):
  das `|` im if als Vergleich gelesen und `return X != FALSE` als
  bedingtes return („sonst gebe ich gar nichts zurück"); der Handle
  blieb „irgendwas von Windows". Gegenmittel: Zeitlupen-Langform beider
  Zeilen, Garderoben-Marke als Handle-Bild, Umleitung `> log.txt` als
  echter Fall, in dem die Guards greifen.
- 2026-09-12 · Lane Defender M1, ClearScreen und ReadKey — **Selbst:**
  das Tempo selbst gedrosselt („Halt, stopp, du bist zu schnell") —
  wie am 09.09. den eigenen Lernraum verteidigt; ClearScreen-Zweck
  (leeren plus Cursor setzen) und den ReadKey-Grundablauf samt
  Guard-Rückgabe und Neu-Mapping korrekt erklärt. **Fehlerbild:**
  `flush` mit dem Bildschirm-Löschen vermengt („sammelt und cleart
  dann alles") — das Wort „leeren" war doppelt belegt (Bildschirm
  gegen Mappe); der Zweck der Prefix-Werte 224/0 unklar („für was habe
  ich die?"). **Hilfe:** WhatsApp-Bild (cout tippt den Entwurf, flush
  drückt Senden, endl ist Enter mit Auto-Senden), 224/0 als „Achtung,
  Durchsage"-Ankündigung samt Pflicht zum zweiten _getch gegen
  liegengebliebene Geistertasten (Anker: das liegengebliebene \n bei
  cin). Nachgang: die Geistertasten-Folge im Kern selbst formuliert
  („der nächste Lesevorgang bekäme den falschen Wert in iKey") — die
  Ursache dabei an der Variablen-Adresse verortet statt in der
  Tastatur-Warteschlange; Auflösung über das Bild der Warteschlange,
  aus der jedes _getch nur den vordersten Wert nimmt. Zur
  flush-Kontrollfrage kam „der Befehl würde gelöscht, aber die Message
  kommt noch" (Diktat, mehrdeutig) — die Hälfte „kommt später noch an"
  stimmt; klargestellt, dass dabei nichts verloren geht: Der Entwurf
  wartet und reist mit dem nächsten Auto-Senden mit. Nach einer Pause
  das Ansammeln-Modell selbst sauber formuliert (Container füllt sich,
  gesendet erst bei endl oder flush) und die Restlücke präzise benannt:
  Unterschied endl gegen flush — Vermutung „flush macht mehr", richtig
  ist das Gegenteil. Auflösung: endl = "\n" + flush, flush sendet nur;
  ClearScreen darf gerade keinen Umbruch anhängen, weil der den frisch
  gesetzten Cursor eine Zeile nach unten schöbe.
- 2026-09-12 · Lane Defender M1, Abschluss-Siegel Console-Baustein
  (je ein Satz je Funktion, frei formuliert) — **Selbst:** ClearScreen
  fehlerfrei (leeren, Cursor an den Start, mit flush senden); das
  ReadKey-Konzept richtig (normale gegen Spezialtasten, Scan-Codes auf
  eigene Konstanten ummappen, Unbekanntes als I_KEY_UNKNOWN);
  eigenständig beschlossen, die M1-Arbeitszeit ab jetzt mit Grindstone
  zu tracken — deckt genau die Ist-Spalte des ZEITPLANs.
  **Fehlerbild:** InitConsole als „stoppt mein Programm automatisch"
  erklärt — Melden mit Entscheiden verwechselt (die Funktion gibt nur
  bool zurück, der Aufrufer entscheidet; derselbe Ebenen-Mix wie bei
  bool gegen Bits), dazu „guckt, ob die Konsole ausgeben kann" statt
  „stellt sie um"; im ReadKey-Satz iKey und iScanCode einmal verdreht
  (Konzept dahinter stimmte). **Hilfe:** Merksatz „Funktionen melden,
  Aufrufer entscheiden"; Dreizeiler-Ablauf zum Geradeziehen der
  Variablenrollen. Console.h/.cpp hatte er zu diesem Zeitpunkt bereits
  eigenständig in VS eingebunden und gebaut, ohne den Klickpfad zu
  brauchen.
- 2026-09-12 · Lane Defender M1, Entwurf Zeichentest-Szene (Entwurf
  vor Gerüst) — **Selbst:** über die Vorgabe hinaus einen eigenen,
  zweiten Test erfunden: ein Symbol läuft Tick für Tick eine Mini-Lane
  mit Wänden hinab, um die Stabilität beim Neuzeichnen zu prüfen —
  nimmt exakt die M2-Rendering-Situation vorweg; die Lane-Breite mit
  zwei Plätzen deckt sich ungeplant mit der beschlossenen
  Doppelzellbreite; C#-Brücke Console.SetCursorPosition selbst
  gezogen. **Fehlerbild:** das Symbol einzeln per Cursor setzen wollen
  statt des beschlossenen Ein-Puffer-Renderings (ganzer Frame als ein
  String, Cursor-Home, einmal senden); ein Feld-Array angesetzt, wo
  als Zustand eine einzige Zahl reicht. **Hilfe:** Merksatz „der
  Zustand ist die Zahl, das Bild wird jeden Tick frisch daraus
  gebaut"; Home-statt-Löschen als Flacker-Schutz aus den DECISIONS.
- 2026-09-13 · Lane Defender M1, Output-Umzug (erster eigener Header) —
  **Selbst:** die Datei-Trennung selbst eingefordert und mit der
  eigenen C#-Regel begründet (eine Zuständigkeit je Klasse → in C++ je
  .h/.cpp-Paar); die Kontrollfrage zu LoseLives richtig beantwortet
  (Spiellogik, keine Ausgabe) und es konsequent ganz entfernt statt es
  herrenlos liegen zu lassen; beide Dateien über VS angelegt
  (Projekteintrag automatisch); Default-Argumente beim Umzug korrekt
  nur im Header belassen. **Fehlerbild:** beim Ausschneiden
  Nachbarzeilen mitgerissen — das Console-Include und die
  LoseLives-Definition verschwanden still, und der Build blieb grün,
  weil die leere main nichts ruft („kompiliert ist nicht fertig" in
  neuer Form: Der Linker sucht nur Gerufenes); Includes zunächst
  weiter über die Console.h-Textkopie geliehen. **Hilfe:** Erklärung
  der stillen Grün-Falle; SAE-Köpfe und Summaries übernahm Claude —
  nach Isors berechtigter Rüge, sie standen fälschlich in seiner
  Aufgabenliste (Arbeitsteilung aus CODE_GUIDELINES).
- 2026-09-13 · Lane Defender M1, Zeichentest gebaut und gemessen —
  **Selbst:** Init-Guard mit Meldung und Fehler-Rückgabe allein, dazu
  unaufgefordert die Design-Frage nach benannten Exit-Codes (eigene
  Fehlerliste ab 1000) — nach Bewertung selbst auf eine lokale
  Konstante mit Wert 1 entschieden; die Array-Klammer-Position über
  den Compiler-Fehler gefunden; die Doppelschleifen-Struktur (Wände
  außen, zehnmal innen) stand im ersten Entwurf; das foreach nach der
  Zerlegung korrekt eingebaut; am laufenden Test die Schach-Doppelbreite
  selbst vermessen („braucht 2 Zellen") und daraus live ein
  Lane-Layout entworfen (Wand + vier Leerzellen, Figur mittig, Schuss
  zwei Zellen breit — als M2-Merker in der ROADMAP). **Fehlerbild:**
  `S_SYMBOL_CANDIDATES->length()` — das Array zerfiel still zum
  Pointer aufs erste Element, gemessen wurde die Textlänge von „A",
  die Schleife endete nach zwei Zeilen; die Bewerberliste zunächst als
  „je Rolle ein String" gebündelt und die Kommentar-Aufzählung als
  Unicode-Bauteile gedeutet; PrintMessage ohne zweites Argument — der
  Default machte je Symbol einen Umbruch; Überforderungs-Frust, als
  Meta-Umbauten und neuer Stoff sich stapelten („bin komplett
  draußen") — Auslöser war die Menge zugleich, nicht der Stoff.
  **Hilfe:** die foreach-Zeile zerlegt mit C#-Spiegel (foreach/in ↔
  for/Doppelpunkt); die Bewerberliste als Tabelle (drei Kandidaten je
  Rolle, einer gewinnt); Rest-Feinschliff (Lineal, Literal-Wände,
  ReadKey) übernahm Claude auf Zuruf; Step-für-Step-Modus mit
  Einzelvorlage je Schritt eingeführt.
- 2026-09-13 · Lane Defender M1, SymbolTest-Auslagerung (unaufgefordert,
  am Abschnittsende) — **Selbst:** die Test-Szene komplett
  selbstständig in ein eigenes Paar `SymbolTest.h`/`SymbolTest.cpp`
  ausgelagert — die Dateipaar-Regel vom Vormittag aus eigenem Antrieb
  angewandt und damit die Szenen-Struktur von M2 vorweggenommen; alle
  vier Includes der neuen .cpp selbst getragen (das Include-Fehlerbild
  trat nicht wieder auf); Prototyp samt Summary korrekt mitgezogen.
  **Fehlerbild:** die Exit-Konstante von main im SymbolTest-Header
  geparkt (fremde Zuständigkeit — die Utils-Falle im Kleinen), dadurch
  lieh sich der Header int32_t über die Include-Kette; der eigene
  Header fehlte als erster Include der .cpp (Signatur-Abgleich
  entfällt). **Hilfe:** beide Funde über Isors eigene Dateipaar-Regel
  erklärt, Rückverlegung und Köpfe im Kommentar-Pass durch Claude.
- 2026-09-13 · Lane Defender M1, Szenen-Zustandsautomat (Abend) —
  **Selbst:** enum class, switch und alle Szenen-Stubs eigenständig
  aufgesetzt (mündlicher Entwurf vorab korrekt); die
  Architektur-Anforderung selbst formuliert („main clean, Szenen
  gehören später zu eigenen Controllern") und damit das Melde-Muster
  begründet; beim Umbau in acht Einzel-Steps jede Bewegung selbst
  vollzogen, die Namenseingabe-Station nach Muster allein ergänzt und
  den Symbol-Test eigenständig konsistenter gelöst als vorgeschlagen
  (Szene meldet selbst „danach Menü" statt Sonderweg im case); die
  Pointer-Konzeptfrage präzise gestellt („immer neuer Inhalt — warum
  kein Pointer?"). **Fehlerbild:** Zustandsvariable im Header
  definiert (Include-Textkopie → Doppel-Definition beim Linken); das
  Shadowing ein zweites Mal (lokale Neu-Deklaration in main neben der
  globalen); im Exit-case Rückgabewert verfallen lassen und ohne break
  in default durchgefallen (beide bekannten Muster in einer Zeile);
  ChangeScene setzte anfangs die Hausnummer der Parameter-Kopie
  (toter Zettel nach Funktionsende); „Wert wechselt im Karton" mit
  „Ziel wechselt zwischen Kartons" verwechselt. **Hilfe:**
  Header-Regel („Zusagen, keine Kartons") und return-Regel („nur main
  beendet main") je an seinem Code; Muster A gegen B als Klickfrage
  mit Codebildern; Acht-Step-Führung auf seinen Wunsch („Step für
  Step, sonst komme ich nicht sauber weiter"); Widget zur
  Variable-gegen-Pointer-Unterscheidung.
- 2026-09-13 · Abend-Reflexion (Isors eigene Einschätzungen) —
  **Selbst:** die Acht-Step-Führung als „sehr leicht" bewertet und
  den eigenen Arbeitsmodus präzise formuliert (Korrekturen
  kleinschrittig; beim Neu-Bauen erst Aufbau-Gespräch, dann eigenes
  Gerüst, dann Einigung, Hilfe erst beim Festhängen); die eigenen
  Lücken exakt benannt — foreach „noch nicht drin, sieht abstrakt
  aus", Klassen-Syntax fehlt komplett (Hinterkopf-Bild von
  class/public:/private: vorhanden), Stern und Und-Zeichen „strengt
  extrem an" („wann existiert was, wann hole ich die Adresse, wann
  den Wert"); die Zeitlage selbst gemessen und offen angesprochen
  (10:22 h auf M1 gegen 6 h Schätzung, Grindstone) samt eigener
  Hypothese, dass spätere Meilensteine schneller laufen. **Hilfe:**
  Einordnung der Zeit (Einmal-Lernkosten in M1, Budget-Polster,
  Schnittlinien als Vorsorge — entschieden wird am M2-Trend); Rüge an
  Claude angenommen: beim Zeichentest die Wunsch-Symbole nicht zuerst
  getestet — als Arbeitsregel in Claudes Gedächtnis übernommen.
- 2026-09-14 · Lane Defender M1, Aufbau-Gespräch Hauptmenü — **Selbst:**
  die Menü-Architektur eigenständig entworfen: Output als reiner
  Zeichner („bekommt Was und Wo, holt sich nichts"), Trennung von
  Logik und Darstellung, je Szene eine eigene Einheit — knüpft an den
  eigenen „main clean"-Satz vom 13.09. an; Ein-Puffer fürs Menü selbst
  bestätigt und den Zeichenweg der übrigen Szenen bewusst offen
  gelassen („entscheiden wir je Szene"); die Titelwahl pragmatisch an
  der Terminalbreite entschieden (Blockschrift 128 Zeichen verworfen,
  Linien-Fassung ~72 gewählt — Linien-Schrift-Beschluss bleibt gültig).
  **Fehlerbild:** „Klasse" als Default-Baustein aus der C#-Gewohnheit
  (Klassen-Syntax laut eigener Reflexion vom 13.09. noch nicht da; V1
  bleibt beim Dateipaar-Muster des Bestands); den Auswahl-Marker per
  SetCursor setzen wollen — zweite Auflage des Einzel-Cursor-Musters
  vom Zeichentest-Entwurf (12.09.), der Merksatz „Zustand ist die
  Zahl, das Bild wird frisch daraus gebaut" ist noch nicht verankert.
  **Hilfe:** Vergleichs-Diagramm Entwurf gegen Bestand (main / MainMenu
  / Output / Console); SetCursor-Vorschau als Escape-Text-Erklärung;
  Marker-im-Frame statt Cursor-Sprung eingeordnet.
- 2026-09-14 · C++-Unterricht Chapter 1.4–2.1 (Stoff nur gehört, Folien
  als Screenshots nachgereicht: true/false, Systems Hungarian, Strings,
  abstrakte Datentypen, Initialisierung, Von-Neumann) — **Selbst:** den
  Großteil als bereits vorgearbeitet eingeordnet (.h/.cpp, Klassen,
  struct); die eigenen Lücken präzise markiert (typedef offen, union
  halb, Initialisierungsformen nicht auswendig); für typedef die
  richtige Brücke selbst gebildet („wichtig über mehrere
  Betriebssysteme"); Architektur-Theorie bewusst niedrig priorisiert,
  Fokus auf Lane Defender gesetzt. **Fehlerbild:** union als „enum, bei
  dem ich die Datentypen verändern kann" gedeutet — zwei unverwandte
  Bausteine über das ähnliche Stichwort verknüpft (Muster vom
  2026-09-08: bekanntes Wort auf neue Bedeutung gelesen); dazu
  Entmutigung, weil die Viewer-Bibliothek in C geschrieben ist („noch
  eine Sprache"). **Hilfe:** Speicher-Widget struct (nebeneinander)
  gegen union (dieselben 4 Bytes, zwei Lesarten; f = 1.0f → i liest
  1065353216) samt Abgrenzung zu enum; typedef/using an Unreals int32
  angebunden; Initialisierung auf zwei Regeln verkürzt (`int k = 1337;`
  schreiben, uninitialisiert = Müll) statt Liste lernen; zwei
  Folienfehler benannt (`INT_MAX == true` ist false — ungleich 0 zählt
  nur als Bedingung wahr; sz-Präfix gehört zu `const char*`, nicht
  `std::string`); C als aus C++ direkt aufrufbar eingeordnet, GLSL als
  einzige echte Zusatzsprache.
- 2026-09-18 · Lane Defender M1, Menü-Frame allein gebaut (zwischen den
  Sessions, 14.–18.09.) — **Selbst:** `MainMenu.h`/`.cpp` eigenständig
  angelegt und den Ein-Puffer-Frame über Get-Funktionen komponiert
  (Titel, Start- und Exit-Button als Bausteine, GetMainMenuScene setzt
  zusammen); Raw-String-Literale selbst gefunden und damit das
  angekündigte Backslash-Problem des ASCII-Titels gelöst, bevor Claudes
  escaped Array nötig war; Start/Exit ungefragt gleich als
  Linien-Schrift-Blöcke; `BuildEmptyNextline` als eigener Helfer; den
  Rechts-Versatz des Titels selbst entdeckt, eingegrenzt
  (LaneDefender.cpp geprüft, ClearScreen als Verdacht benannt) und zur
  Diskussion gestellt statt drüberzubauen. **Fehlerbild:**
  VS-Auto-Einrückung im Raw-String übernommen (Tabs — der Raw-String
  nimmt sie wörtlich, Ursache des Versatzes), Verdacht stattdessen bei
  der Konsolen-Technik; Off-by-one in `BuildEmptyNextline` (`i <= n`
  liefert n+1 Zeilen); `PrintMainMenu` in Output gebaut — der Zeichner
  kennt damit eine konkrete Szene, gegen den eigenen Satz „Output ist
  nur der Zeichner"; eigener Header erneut nicht erster Include; das
  Flacker-Modell „ganze Page neu = flackert" (dritter Anlauf zum
  Einzel-Cursor — Home-statt-Löschen ist als Flacker-Lösung noch nicht
  verankert). **Hilfe:** Tab-Sprung am Spaltenraster samt
  View-White-Space-Handgriff; Clear-gegen-Überschreiben als
  Frame-Folge visualisiert; Block-Zentrierung als Padding-Rechnung auf
  die 120er-Breite statt SetCursor; Umbau-Pfad benannt (Szene zieht
  nach MainMenu, Output wird wieder generisch).
- 2026-09-18 · Lane Defender M1, Rückfragen zum Feinschliff —
  **Selbst:** die Grenze der Literal-Regel eigenständig hinterfragt
  („ist die 1 im Schleifenkopf eine Magic Number?") und den
  Off-by-one-Fix davor allein gezogen (Schleifenstart auf 1); die
  Zuständigkeit des Automaten aktiv geklärt („gehört RunMainMenuScene
  nicht zur State Machine in LaneDefender.cpp?") statt den
  vorgeschlagenen Umzug blind auszuführen. **Hilfe:** Faustregel „eine
  Zahl braucht einen Namen, wenn der Name mehr sagt als die Zahl";
  Schalter-gegen-Station-Trennung, belegt am eigenen
  SymbolTest-Präzedenzfall vom 13.09.
- 2026-09-18 · Lane Defender M1, Szenen-Umzug und Include-Detektiv —
  **Selbst:** `RunMainMenuScene` eigenständig nach MainMenu verschoben
  und dafür `LaneDefender.h` in MainMenu.h selbst als nötig erkannt
  (das Enum im Prototyp); die ReadKey-Herkunftsfrage allein aufgelöst —
  Hypothese gebildet (Console), Console.h included, Build bestätigt:
  erste eigene Include-Ketten-Analyse, das Leih-Fehlerbild vom 13.09.
  trat nicht wieder auf; nebenbei das Szenen-Enum eigenständig auf
  `uint8_t` umgestellt. **Fehlerbild:** der alte Stub-Prototyp blieb
  doppelt in LaneDefender.h stehen, und LaneDefender.cpp rief die
  Szene weiter über diesen Alt-Prototyp, statt MainMenu.h zu includen —
  das Leih-Muster eine Ebene höher (Prototyp statt Include); der
  PrintMainMenu-Rückbau war nicht zu Ende gezogen. **Hilfe:** Regel
  „jede Datei includet selbst, was sie benutzt"; Restaufräumen durch
  Claude (Prototyp-Doppel raus, PrintMainMenu entfernt, Include-Gruppen
  geordnet, Summaries nachgezogen), /W4-Build grün.
- 2026-09-18 · Lane Defender M1, Einstieg Auswahl-Schleife —
  **Selbst:** die eigene Render-Idee (nur den geänderten Bereich
  löschen und neu zeichnen) klar formuliert und aktiv zur Prüfung
  gestellt („oder liege ich da falsch?") statt sie still einzubauen;
  den Transfer zur späteren Spielersteuerung selbst gezogen — der
  Instinkt trifft eine echte Technik (dirty rectangles, ncurses).
  **Fehlerbild:** das Flacker-Modell „alles neu zeichnen = Flackern"
  hielt sich im vierten Anlauf (Löschen als eigentliche Flacker-Quelle
  noch nicht verankert); dazu die Annahme, Teil-Zeichnen mache
  Bewegung flüssiger — Konsolen-Bewegung ist aber zellweise, und der
  Voll-Frame liegt weit unter dem Refresh-Budget. **Hilfe:**
  Zell-Zeitachse Löschen-gegen-Überschreiben als Widget; Kernsatz
  „gleiches Zeichen erneut gezeichnet ist unsichtbar — sichtbar ändert
  sich nur die Diff-Zelle"; Kostenrechnung 3600 Zeichen ≪ 1 ms gegen
  16,7 ms Terminal-Takt; Einordnung, wann Diff-Senden wirklich lohnt
  (langsame Leitung, gemessene Ruckler).
- 2026-09-18 · Lane Defender M1, Gerüst der Auswahl-Schleife —
  **Selbst:** die case-Syntax nach dem Anker am eigenen Automaten
  allein repariert (feste Kandidaten statt Variable hinter case); die
  Controller-Schleife mit ReadKey, switch und Druck je Richtungstaste
  gebaut; den Umlauf eigenständig versucht (zweimal ↑ wird über die
  gemerkte Vorgängertaste zu ↓); die Sprite-Frage selbst erkannt und
  offen gestellt statt die Doppel-Sprite-Lösung still zu bauen.
  **Fehlerbild:** der Zustand ist der Tastencode statt der
  Auswahl-Zahl (Parameter heißen …KeyValue, gedruckt wird je Taste,
  der Umlauf braucht darum die Tastengeschichte); `GetMainMenuScene`
  in drei Fassungen — Header ein Parameter, Definition zwei, Aufruf
  ein Argument: die Versprechen-gegen-Lieferung-Familie vom 11.09.,
  diesmal als Linker-Fehler; „theoretisch geht es" ohne Build
  gemeldet. **Hilfe:** die drei Indizien auf die fehlende Auswahl-Zahl
  zurückgeführt; Platzhalter-Verfahren als Marker-Option neben
  Doppel-Sprite und Index-Konstante vorgelegt, Entscheidung bei Isor.
- 2026-09-19 · Lane Defender M1, Marker-Optik entschieden —
  **Selbst:** die Darstellungsfrage selbst aufgeworfen, bevor gebaut
  wurde („erst entscheiden, wie wir es darstellen — sonst sind die
  Funktionen komplett anders"), mit eigenen Vorschlägen (Balken,
  großer Pfeil); Entscheidung: Balken unter dem gewählten Button plus
  gelbe Färbung — der eigene Balken-Vorschlag, kombiniert.
  **Fehlerbild:** der find-/Index-Baustein vom Vortag trug nur
  minimal — String als nummerierte Zellreihe samt npos war als Bild
  erklärt, blieb aber wackelig; durch die Marker-Entscheidung entfällt
  das Verfahren ohnehin. **Hilfe:** vier Optik-Kandidaten als
  Konsolen-Mockups mit Bau-Preis vorgelegt (Balken · Farbe · Pfeil ·
  Rahmen), Empfehlung auf Isors eigenem Balken-Vorschlag; Hinweis,
  dass die Wahl den `>`-Beschluss vom 12.09. legitim überholt
  (Linien-Schrift kam später) — DECISIONS-Eintrag folgt beim Sichern.
- 2026-09-19 · Lane Defender M1, Auswahl-Schleife läuft erstmals —
  **Selbst:** eigene Abstraktion `AddSelectedMarker(bool, string)`
  erfunden und in beide Getter eingebaut („später nur eine Methode");
  den kompletten Schleifen-Refactor umgesetzt und die Fälle ↓/Enter/
  ESC/T selbstständig gespiegelt; den VS-Encoding-Dialog nach
  Anleitung gemeistert (UTF-8 ohne Signatur); Balken-Konstanten selbst
  getippt (Zentrierung dann von Claude ausgezählt: 47+25, 51+18).
  **Fehlerbild:** Loch in der eigenen Abstraktion — die gemeinsame
  Methode hängt fest den Start-Balken an, was je Aufrufer verschieden
  ist, kam nicht als Parameter mit; beim Spiegeln des Umlaufs das
  Vergleichszeichen nicht mitgedreht (`<` statt `>` nach dem ++);
  kein Modell für Terminal-Scroll — Frame füllte mit dem
  PrintMessage-Extra-`\n` exakt die 30 Terminal-Zeilen, jeder Frame
  schob um eins und Home zielte daneben. **Hilfe:** Merksatz „was
  sich je Aufrufer unterscheidet, wird Parameter"; Zeilen-Budget als
  Tabelle vorgerechnet (29+1 gegen 30), Regel „nie über den unteren
  Rand schreiben" mit drei Handgriffen (bNextLine false, Luft 6→4,
  Cursor verstecken); Fenster-Wächter als Härtungspunkt vorgemerkt.
- 2026-09-19 · Lane Defender M1, klebender Balken und Zellen-Gedächtnis —
  **Selbst:** die drei Scroll-Handgriffe, den ↓-Umlauf und die
  Enter-Verzweigung eigenständig umgesetzt; das Fehlverhalten präzise
  beschrieben und eine eigene Hypothese samt Gegenrede formuliert
  („String wird doch jedes Mal neu gebaut") — die Gegenrede war
  richtig. **Fehlerbild:** Zustand im falschen Ort vermutet (String
  statt Terminal) — das Modell „nicht geschriebene Zellen behalten
  ihren Inhalt" fehlte als Kehrseite der Flacker-Lektion; die
  Leerzeile des else-Zweigs schreibt null Zellen, der alte Balken
  blieb stehen. **Hilfe:** Kehrseiten-Merksatz „der Bildschirm ist
  ein Zellen-Gedächtnis — stehen bleibt, was du nicht schreibst;
  Löschen ist Schreiben von Leerzeichen"; Putz-Zeile (72 Leerzeichen)
  als Konstante ausgezählt, Umbau auf den dritten Parameter samt
  else-Putz an Isor übergeben.
- 2026-09-19 · Lane Defender M1, Beeps und der Weg zum Sound-Paar —
  **Selbst:** den dritten Parameter samt beiden Aufrufen allein fertig
  gebaut (Falsch-Balken-Bug damit selbst erledigt); WinAPI-`Beep` auf
  eigene Faust gefunden und in die cases eingebaut; die eigenen
  Literale sofort als Magic Numbers erkannt (SAE-Regel griff von
  allein) und daraus selbstständig den richtigen Schnitt abgeleitet —
  eigenes Header/CPP-Paar mit Funktionen je Ton-Bedeutung, bewusst
  ohne Klasse („kein Zustand"): das Output-Muster vom 13.09. aus
  eigenem Antrieb wiedererkannt und übertragen. **Fehlerbild:**
  `windows.h` direkt in MainMenu.cpp gezogen (Schichten-Regel „WinAPI
  wohnt im .cpp der Technik-Schicht" noch nicht verankert — Console
  macht es vor); Ton-Dauern ohne Blockade-Bewusstsein gewählt (Beep
  blockiert 200–250 ms je Tastendruck). **Hilfe:** Benennung nach
  Bedeutung statt Ton (PlayMenuMoveSound statt BeepHigh) mit dem
  Ein-Datei-Argument; Zahlen-Rat 50–80 ms und 200–400 Hz;
  Datei-Namen und Konstanten-Muster vorgeschlagen, Isor tippt.
- 2026-09-19 · Lane Defender M1, Sound-Paar fertig und Include-Frage —
  **Selbst:** Sound.h/Sound.cpp komplett allein gebaut — Namen nach
  Bedeutung übernommen, alle acht Zahlen als Konstanten, Fehler-Sound
  als eigene zweistufige Idee („dü-dü", zwei fallende Beeps),
  `windows.h` selbst aus MainMenu.cpp entfernt, default-Fall
  eigenständig mit PlayErrorSound versorgt; die Include-Ordnung aus
  eigenem Antrieb hinterfragt, Vermutung fast richtig (eigene Header
  vor Standard — nur die Stufe „die EIGENE .h zuerst" fehlte).
  **Fehlerbild:** Begriff „zwei Klassen" für ein Datei-Paar mit
  freien Funktionen (Terminologie fürs Verteidigen); ein geliehenes
  Include (MainMenu.h nutzt int32_t über LaneDefender.h) — sonst
  war die Include-Lage entgegen seinem „Knoten"-Gefühl sauber.
  **Hilfe:** Drei-Gruppen-Regel mit Begründung „eigene .h zuerst als
  Selbstständigkeits-Test"; Unterscheidung Redundanz (harmlos) gegen
  Leihen (gefährlich); Review-Pass durch Claude (Datei-Köpfe,
  Summaries, Kosmetik, cstdint), Prüf-Build grün ohne Warnungen.
- 2026-09-19 · Lane Defender M1, Standortbestimmung an der Baustein-Grenze —
  **Selbst:** eigene Zwischenbilanz formuliert: Header/CPP-Modell
  sitzt („im Header steht das Versprochene, die Definition wohnt im
  CPP"), eigene Konstanten-Praxis (alles ins .cpp) selbst zur Prüfung
  gestellt — sie war richtig; offene Baustellen selbst benannt
  (Console.cpp-Innenleben nur grob → M7-Verstehens-Runde; Pointer/
  Referenzen werden mit den Klassen ernst) und vorausgedacht, dass
  der Name zum Player-Objekt gehört. **Fehlerbild:** Meilenstein-
  Modell „jedes M = eine Szene" (M1 ist das Gerüst samt aller
  Rahmen-Szenen, M2–M6 füllen die Game-Szene) — Überblick war weg;
  Unsicherheit global-gegen-const (Gefahr ist Veränderlichkeit, nicht
  Sichtbarkeit — eigenes 13.09.-Erlebnis als Beleg gezeigt).
  **Hilfe:** M1–M7-Tabelle; Schaufenster-Regel für Konstanten
  (Nutzerzahl entscheidet, const im .cpp ist datei-sichtbar);
  Merksatz „Werte dürfen global sein, Zustand wohnt lokal oder im
  Objekt"; Wechsel in den Design-Abschnitt Namenseingabe empfohlen.
- 2026-09-19 · Lane Defender M1, Design der Namenseingabe —
  **Selbst:** eigenen Screen-Entwurf als Paint-Skizze geliefert
  (Dialogfenster-Metapher, Regeln vor dem Fehler, Fehlerzeile am
  Feld, Button-Zeile unten) und die Implementierungsfrage bewusst
  hinter das Design gestellt; das Unbehagen am zweiphasigen Ablauf
  präzise artikuliert („man müsste wählen können, ob man im Feld
  ist") — das ist der Kern des beschlossenen Fokus-Modells; vor dem
  Kippen des getline-Beschlusses von sich aus die Sicherheitsfrage
  gestellt („machen wir gerade etwas kaputt?") — Beschluss-Hygiene
  aus eigenem Antrieb. **Fehlerbild:** Rot als Fehlerfarbe erneut
  vorgeschlagen, ohne die 12.09.-Verwerfung präsent zu haben —
  diesmal trug allerdings das neue Zwei-Signale-Argument, und der
  Vorschlag wurde mit Grund angenommen statt wiederholt abgelehnt;
  Unsicherheit, wie das Fenster in Code entsteht („Array oder
  Schleife?" — es ist derselbe statische Raw-String-Block wie beim
  Menü). **Hilfe:** getline-gegen-Selbst-Zeichnen als
  Tastatur-Besitz-Frage erklärt (modal: die Konsole hält die
  Tastatur, bis Enter fällt); Verlust-Bilanz als Tabelle (drei
  Schutzaufgaben von getline, drei benannte Nachfolger; Preis nur
  Backspace statt Zeilen-Editing); Fokus-Modell als Diagramm,
  Layout mit Zahlen (Fenster 62 Spalten, Zeilen-Budget der 30).
- 2026-09-19 · Lane Defender M1, Solo-Umbau vor der Namenseingabe —
  **Selbst:** parallel zur Doku-Runde allein umgebaut: `S_COLOR_RED`
  korrekt angelegt (samt hellem 91er-Code aus der Design-Runde),
  MainMenu aus eigenem Antrieb auf MainMenuScene umbenannt
  (Konsistenz-Naming) und die NameInput-Szene in ihr eigenes Paar
  gezogen — diesmal **ohne** das Leih-Fehlerbild vom 13./18.09.:
  alter Prototyp raus, Stub raus, alle Includes nachgezogen, eigene
  .h zuerst; die Baureihenfolge selbst richtig eingeschätzt
  (SetCursorPosition vor dem Szenen-Bau). **Fehlerbild:** beim
  Umbenennen die `File:`-Zeilen der Datei-Köpfe nicht nachgezogen
  und die neuen Dateien ohne Köpfe angelegt — der Kommentar-Pass
  fing es ab, wofür er da ist. **Hilfe:** Kommentar-Pass durch
  Claude (File-Zeilen, Köpfe, History, Include-Ordnung in main).
- 2026-09-19 · Lane Defender M1, SetCursorPosition und die Anatomie
  der Escape-Sequenzen — **Selbst:** die Funktion nach Vorlage allein
  gebaut und mit eigenem Testaufruf (5,10 + X) verifiziert; dann
  nicht weitergerannt, sondern aktiv um Tiefe gebeten („ich möchte
  den Code einen Tick besser verstehen") — Verstehen vor Tempo aus
  eigenem Antrieb; das Semikolon als Trenner selbst richtig
  gedeutet. **Fehlerbild:** `\x1b` als „Flush-Befehl" gelesen (es
  ist ein einzelnes Zeichen, Nummer 27 — dieselbe wie die eigene
  I_KEY_ESCAPE-Konstante), die Klammer als Zahlen-Lese-Helfer, das
  `H` als Abschlusszeichen — das Verb-Konzept fehlte (Argumente
  zuerst, Befehlsbuchstabe zuletzt, erster Buchstabe beendet die
  Sequenz); flush als Absender statt als Puffer-Leerung. **Hilfe:**
  Anatomie-Zerlegung als Bild, Decoder-Tabelle der eigenen
  Console.h-Konstanten (m/H/J/l als Verben), ESC-Taste-27-Anker.
  **Zweite Runde (Selbst):** die Anatomie korrekt in eigenen Worten
  rekonstruiert und die richtige Anschlussfrage gestellt („woher
  weiß die Konsole, dass m Farbe heißt?") samt eigener
  Mapping-Vermutung — der Verdacht, das hänge mit der noch unklaren
  Console.cpp zusammen, stimmte exakt. **Fehlerbild:** das
  Wörterbuch im eigenen Code vermutet statt im Terminal; die
  Konstanten für Definitionen gehalten (sie sind Vokabelkarten).
  **Hilfe:** Dolmetscher-Modell als Pipeline-Bild (Terminal führt
  intern einen switch über den Verb-Buchstaben — dasselbe Konstrukt
  wie der eigene Szenen-switch); VT100/ANSI-Standard von 1978 als
  Herkunft; InitConsole als Dolmetscher-Einschalter erkannt — die
  halbe Console.cpp ist damit verstanden, offen bleibt die
  Lese-Seite (ReadKey/_getch) für den M7-Termin.
- 2026-09-19 · Lane Defender M1, Fenster-Rahmen per Schleife —
  **Selbst:** nach zwei Anläufen die Zerlegung in drei Zeilen-Typen
  übernommen und sauber umgesetzt (drei kleine Get-Bauer plus ein
  Stapler, FRAME_OFFSET bei der Höhe richtig eingesetzt); das
  Versatz-Problem präzise beschrieben und Hilfe geholt, statt zu
  raten. **Fehlerbild:** erster Rahmen-Wurf in Einzelzell-Logik
  (Doppel-Inkrement im Schleifenrumpf, unerreichbare
  x==Ende-Bedingung bei <-Schleife — Zaunpfahl, Ecken/Kanten-Rollen
  vermischt); SetCursorPosition als Fenster-Platzierer gedacht —
  die Regel „\n springt auf Spalte 1, nur die erste Zeile beginnt
  am Cursor" fehlte; die (5,10)-Testzeile blieb trotz Ansage
  liegen und wurde zur Versatz-Ursache. **Hilfe:** Drei-Zeilen-
  Typen-Rezept als Bild mit Zaunpfahl-Zahlen; Merksatz „was sich
  wiederholt, kommt in die Schleife — was einmal passiert, davor
  oder dahinter"; \n-Spalte-1-Regel mit Bild; Ein-Byte-Grenze von
  std::string(n, zeichen) erklärt (UTF-8-Striche brauchen die
  Schleife, Leerzeichen nicht); Positions- gegen Größen-Konstanten
  getrennt (Isors Inhalts-Konstanten bleiben, fenster-relativ
  empfohlen).
- 2026-09-19 · Lane Defender M1, Textzeilen-Bauer und Autopilot-Stopp —
  **Selbst:** den Fenster-Versatz sauber gemeldet statt zu raten;
  Angleichen/Polster/Naming bewusst delegiert („Naming ist nicht
  meine Stärke" — Selbsteinschätzung); den SetCursor-statt-Polster-
  Einwand vertreten und den Anker-Gegenbeleg akzeptiert; beim zu
  kompakten Dreifach-Ausdruck sofort Einspruch erhoben (eigener
  Ein-Schritt-je-Zeile-Stil eingefordert) und bei static_cast aktiv
  nachgefragt; GetMessageWindowTextRow danach fehlerfrei gebaut
  (Cast, Guard, Zusammenbau); am Ende den eigenen Autopilot bemerkt
  und benannt — Metakognition statt Weitertippen. **Fehlerbild:**
  SetCursorPosition erneut als Layout-Werkzeug gedacht (dritter
  Anlauf der Einzel-Cursor-Idee — der Ein-Puffer-Anker musste
  wieder gezeigt werden); „alles gebaut" gemeldet, als erst eines
  von drei Stücken stand; interne Helfer erneut in den Header
  gestellt (Schaufenster-Regel frisch, greift noch nicht von
  selbst). **Hilfe:** Anker-Zitat der Padding-Entscheidung vom
  18.09.; size_t/Unsigned-Kippen mit Zahlenbeispiel und
  static_cast als „suchbare Unterschrift"; Text-Konstanten
  ausgezählt geliefert; Verteiler-Gerüst mit einem vorgemachten
  Fall; Schnitt-Empfehlung beim Autopilot-Signal statt Durchziehen.
- 2026-09-19 · Lane Defender M1, statischer Namenseingabe-Screen steht —
  **Selbst:** nach dem Autopilot-Stopp bewusst „weiter" entschieden
  und gezielt um ein Bild gebeten; die Sinnfrage zum Textzeilen-Bauer
  gestellt und die richtige Lesart selbst formuliert („Text rein,
  Rest auffüllen"); den Verteiler halb gebaut, bevor Stück 1 stand,
  mit gutem DRY-Instinkt (TextRow auch für die Trennlinie — an der
  Byte-Falle gescheitert, Instinkt trotzdem richtig); Screen
  fertiggestellt, rechter Rand bündig; die überzählige Zwischenzeile
  selbst bemerkt und die Suche begonnen. **Fehlerbild:** vierter
  SetCursor-Reflex, diesmal als Welten-Vermischung erkannt
  („Bildschirm überschreiben" gegen „String anhängen" — Fließband-
  Bild); die Byte-Falle live erlebt (length() zählt Bytes: Striche
  wiegen 3 → Füllung 0 → Randloch), trotz ASCII-Kommentar über den
  Konstanten; im Verteiler unabhängige ifs plus bedingungslose
  Leerzeile (zwei Zeilen je Treffer-Runde — die gelobte Luftigkeit
  war der Bug) und Schleife 0-basiert gegen fensterzeilen-basierte
  Konstanten (alles zwei Zeilen tiefer). **Hilfe:**
  Vorher/Nachher-Bild mit Zeilenkarte; Runden-Tabelle; Drei-Sorten-
  Leerzeichen-Tabelle; Byte-Rechnung am Fall; Grundsatz „jede Runde
  hängt genau eine Zeile an — die Leerzeile ist der Sonst-Fall";
  Luftigkeit als Design-Regler statt Bug angeboten.
- 2026-09-19 · Lane Defender M1, Feinschliff-Runde zum Tagesende —
  **Selbst:** die überzählige Zwischenzeile am Bild selbst bemerkt;
  das Unbehagen an der Aufteilung geäußert und das Balance-Urteil
  nach Erklärung mitgetragen; die Zeilen-Umverteilung selbst
  eingetragen, bevor Claude sie anfasste; die Schreiblinien-Frage
  selbst aufgeworfen (blinkt der Cursor auf einem Slot überhaupt
  sichtbar?) — ein Laufzeit-Risiko im statischen Bau vorausgesehen,
  die robuste Formular-Lösung kam aus seinem Einwand; die restlichen
  Statik-Stücke bewusst delegiert und den Schnitt zum /harness:ende
  selbst gesetzt. **Fehlerbild:** eine ungenutzte Strich-Konstante
  angelegt, die durch den Textzeilen-Bauer gelaufen wäre
  (Byte-Falle im zweiten Anlauf — als Muster benannt);
  Unsicherheit, was die Rückgängig-Schaltfläche der App bedeutet
  (bot an, Claudes Fix zurückzunehmen). **Hilfe:** Kopflastigkeit
  als Benennung fürs Bauchgefühl (Zeilen-Bilanz 1 oben gegen 4
  unten); Umbau durch Claude auf Zuruf (Balance-Konstanten waren
  schon Isors, kurze Trennlinie mit Rand-Rechnung, Schreiblinie,
  Button-Zeile mit 103er-Füllung); Label-Empfehlung Confirm statt
  Start Game mit Begründung.
- 2026-09-19 · Lane Defender M1, Eigenversuch Steuerungs-Schleife der
  Namenseingabe — **Selbst:** die komplette Auswahl-Schleife ohne
  Gerüst nach dem Hauptmenü-Muster gebaut (while/ReadKey/switch,
  Auswahl-Konstanten 0–2, Sound je Fall, InputIsValid und
  ClearNameInput im Header versprochen); das Dreieck-Fokusmodell
  selbst erdacht (hoch/runter nur Feld↔Confirm, links/rechts nur
  Confirm↔Back); den Schnellweg Enter→Confirm aus den DECISIONS
  eingebaut; die WASD-Tipp-Kollision selbst entdeckt, bevor Claude
  sie nannte; Gelb als Fokusfarbe nach Zahlen- und Bildvergleich
  bestätigt (Grün verworfen — Rot-Grün-Paar mit der Fehlerfarbe).
  **Fehlerbild:** switch-Fallthrough unbekannt — zwei fehlende
  breaks (Rechts-Fall läuft in Enter weiter, Enter-Sonst-Zweig in
  default), die Warnung C26819 als „fehlendes default" gedeutet;
  das Dreieck als +1/−1 mit Klemmen auf der Zahlenlinie gebaut,
  wodurch links/rechts das Feld verlassen; fehlendes else lässt
  den Fehlerpfad auch bei gültiger Eingabe laufen; Funktionsname
  ohne Klammern in der Bedingung (prüft die Adresse, nicht die
  Antwort); Confirm zielt auf GS_GAME statt GS_TUTORIAL — die
  Zwischenszene des eigenen Automaten übersprungen; der
  Einmal-Druck vor der Schleife statt Home-Frame je Tastendruck.
  **Hilfe:** Fallthrough am eigenen Code erklärt (Korridor-Bild
  samt Spur „Taste → startet das Spiel"); Dreieck gegen
  Zahlenlinie als Bild; TODO-Marken an alle Fundstellen;
  Arrow-Tasten als kollisionsfreie Feld-Navigation benannt
  (eigene Codes ab 1000, nie tippbar).
- 2026-09-19 · Lane Defender M1, erste eigene C++-Klasse (CPlayer) —
  **Selbst:** die Ablage-Frage selbst aufgemacht und für die
  Mini-Klasse jetzt entschieden (gegen Claudes String-Empfehlung, mit
  eigener Begründung „einmal richtig angehen"); Player.h nach Gerüst
  fehlerfrei getippt; den .cpp-Versuch ungefragt gestartet, bevor die
  Erklärung da war; ein eigenes Steuerungs-Modell vorgeschlagen
  (Enter als einziger Ausgang aus dem Feld, ↑/W zurück) und
  Step-by-Step-Arbeit für sich eingefordert. **Fehlerbild:**
  C#-Reflex im .cpp — Klassenblock samt public: erneut aufgemacht
  statt freier Körper mit Nachnamen (dazu falscher Klassenname
  Player statt CPlayer); Rückgabetyp weggelassen; die Signaturen
  beider Methoden zu einer vermischt (GetName mit SetName-Parameter);
  Include-Tippfehler <strring> und unnötiges <cstdint>; der
  +1/−1-TODO blieb unverständlich, bis die Zahlenlinie gegen sein
  Fokus-Modell erklärt war. **Hilfe:** Versprechen-und-Bau-Muster als
  Bild an CExample (Nachname orange, wanderndes const blau);
  Brücke zu den freien Funktionen, die er schon trennt;
  Fehlermeldungs-Decoder für die drei typischen Compiler-Meldungen;
  Datei-Köpfe und Summaries von Claude nachgetragen. **Nachtrag im
  selben Zug:** zweiter Anlauf saß — beide Körper korrekt (freie
  Körper, Nachname, Signaturen, wanderndes const); die const-Frage
  („nach den Klammern — ist das ein Cast?") selbst präzise gestellt,
  Drei-Zuhause-Antwort samt const-Referenz-Nutzen nachvollzogen;
  Kuriosum CPlayer:: auch vor den Membern (legal, aber unnötig) als
  Stilpunkt erklärt und von Isor selbst bereinigt; VS-Editor-Puffer überschrieb Claudes Datei-Kopf
  in Player.h beim Speichern (Editor-gegen-Platte-Falle, erklärt).
- 2026-09-19 · Lane Defender M1, Schritt 2 — Verschachtelungs-Falle —
  **Selbst:** die Verwirrung sofort gemeldet und die eigene Idee klar
  beschrieben (switch im switch, „damit ich unten aussuchen kann"),
  statt still weiterzubauen. **Fehlerbild:** den ganzen Dialog-Fluss
  in einem einzigen Tastendruck behandeln wollen — innerer switch auf
  dieselbe Taste im Enter-Fall (sieht immer nur Enter, alle inneren
  cases toter Code); äußere Verzweigung wieder auf die Taste statt
  auf den Fokus; Kern-Lücke: dass die while-Schleife je Runde genau
  eine Taste verarbeitet und der Zustand das Wissen in die nächste
  Runde trägt. **Hilfe:** Karussell-Bild (Zeichnen → eine Taste lesen
  → Fokus → kleine Reaktion) plus Filmstreifen über drei Runden;
  Anker an seinen eigenen Szenen-Automaten in main (Szenen schachteln
  sich auch nicht ineinander); Gerüst zum Selbsttippen mit
  vorgemachtem Enter-Fall. **Nachtrag:** Gerüst gefüllt und alle
  Review-Funde in zwei Runden selbst gefixt; der Fallthrough entstand
  beim Füllen zweimal neu (Enter-Fall im Feld ohne break; im
  Button-Enter das falsche break gelöscht, nachdem der
  Kosmetik-Hinweis „break nach return ist tot" zu weit ausgelegt
  wurde) — Faustregel gesetzt: jeder case endet auf jedem Weg mit
  break oder return. Eigenständige Design-Überlegung: den Fehlerton
  im Feld-default bewusst gestrichen, weil Buchstaben dort später
  Tipp-Eingaben sind — Vorausdenken auf die Zeichen-Aufnahme; die
  Sound-Frage für die Button-Zeile selbst zur Entscheidung gestellt.
- 2026-09-19 · Lane Defender M1, Schritte 3 und 4 — **Selbst:**
  Schritt 4 (Referenz-Verdrahtung über drei Dateien: Signatur in
  Header und .cpp, Instanz und Aufruf in main) komplett selbst und
  fehlerfrei getippt, dazu ungefragt der Vorgriff `S_DEFAULT_NAME`
  für die kommende Zeichen-Aufnahme; Rundgang-Test selbst gefahren
  (Enter/Pfeile/ESC, Sounds als Beleg). **Fehlerbild:** keines —
  nur Kosmetik (fehlendes Leerzeichen im Include). **Hilfe:**
  Schritt 3 als reine Mechanik von Claude auf Zuruf (Umbenennung
  I_SELECTION_CONFIRM, Header entrümpelt, Datei-Köpfe); Hinweis auf
  die erwartete C4100, damit die Warnung nicht als Fehler erschrickt.
- 2026-09-20 · Lane Defender M1, Schritt 5 Button-Färbung (müder Tag,
  Umbau auf Zuruf durch Claude) — **Selbst:** trotz „nicht fit" einen
  eigenen Färbungs-Anlauf gebaut, und die Putz-Mechanik darin selbst
  konstruiert (beide Marker-Zeilen decken die volle Breite und putzen
  den je anderen Slot — die Terminal-Lektion angewendet); das eigene
  Unbehagen präzise gemeldet („nicht wunderschön, Konstanten nicht
  gut") und gezielt Korrekturhilfe statt Lösung light angefordert.
  **Fehlerbild:** beim Zerlegen der Button-Zeile den linken
  3-Spalten-Rand verloren; den Bauplan dreimal kopiert statt einmal
  gebaut (drei if-Blöcke); Feld-Fall ohne Marker-Zeile (alter Marker
  blieb kleben); Konstantennamen gegen MACRO_CASE und mit
  Tippfehlern; Kompensations-Offsets 107/110 statt Wiederverwendung
  des Zeilen-Skeletts. **Hilfe:** Skelett-Gedanke („Marker-Zeile =
  Button-Zeile mit anderen Slots"); Umbau komplett durch Claude auf
  Zuruf (AddFocusColor, GetButtonRow/GetMarkerRow, Konstanten);
  W4-Befund am Rande: Projekt stand seit je auf /W3 — Warnstufe auf
  Level4 gehoben, totes Doppel-return in InitConsole entdeckt und
  entfernt.
- 2026-09-20 · Lane Defender M1-Abschluss (Zeichen-Aufnahme bis
  Endszene, überwiegend Zuruf-Modus wegen Formtief) — **Selbst:**
  die Whitelist-Idee „Bereiche statt cases" mit eigenen Zahlen
  vorgedacht (Richtung und Operatoren kippten, Prinzip stimmte); die
  const-Frage und die Header-Inkonsistenz selbst aufgeworfen (Antwort
  war das Schaufenster-Prinzip — Richtung andersherum als vermutet);
  Figlet-Kerning der neuen Schriftzüge selbst gerichtet; den gesamten
  Szenen-Code gelesen und als eigenes Muster eingeordnet („eigentlich
  Copy & Paste, nicht schwer"); das Kommentar-Stil-Urteil gefällt
  (zu lang, wirkt KI-generiert → neue Zwei-Zeilen-Regel); Zeitdaten
  getrackt und selbst eingeordnet (20 h gegen 6 — bewusst besser
  ausdesignt, Gerüst für M2+ vorbereitet); Vorschau-vor-Code als
  Arbeitsweise eingefordert und die Einblendung als Zierrat selbst
  gestrichen. **Fehlerbild:** Blacklist mit unmöglichen &&-Paaren
  (De-Morgan-Kipper, still immer falsch); Rückerklärungs-Fragen
  (Leertaste, verschwundene C4100) blieben unbeantwortet — offen für
  eine wache Runde. **Hilfe:** Zeichen-Aufnahme, Färbungs-Umbau,
  Tutorial- und Endszene als erklärte Zuruf-Bauten in Happen; die
  drei Tür-Varianten (Kopie, const&, &) als Bild mit Anker an seine
  eigenen L3-Seiten.
- 2026-09-20 · Lane Defender M2-Design (Screen-Layout, Sprite,
  Symbole, Tastenabfrage) — **Selbst:** das M2-Screen-Layout als
  eigene Skizze mitgebracht (HUD oben, Shop unten, Korridore) und
  den Live-Shop als Vereinfachung erkannt (spart die Shop-Szene);
  das Sprung-Modell eigenständig hergeleitet samt Überdruck-Argument
  (Position = Lane-Index, nichts kann überprintet werden); die
  Lane-Progression selbst zugeschnitten (2/3/4 an den Boss-Siegen).
  **Hilfe:** Zellrechnung und Zeilenbudget (drei Design-Beispiele
  als Render), Zuschnitt des kbhit-Wächters samt Drain-Argument.
- 2026-09-20/21 · Lane Defender M2 B1 Lauf-Test (erste eigene
  Tick-Schleife, selbst getippt mit Schritt-Führung) — **Selbst:**
  GetLane mit Figur-Parameter und if/else eigenständig vorgebaut
  (Figur im String — den Kern des Ein-Puffer-Musters selbst
  umgesetzt); Spalten der drei Lane-Teile selbst nachgezählt;
  ++/Wrap eigenständig aus der Drain-Schleife gezogen, bevor der
  Schritt dran war; Wandbündigkeit empirisch selbst gefixt (ein
  Leerzeichen mehr in der Bauer-Zeile). **Fehlerbild:** break im
  switch als Schleifen-Ausgang gedacht (eigene Knowledge-Seite
  „break ist die Tür im switch" existierte schon); while-Bedingung
  ohne ! (Schleife lief nie); Erstwurf zeichnete per
  SetCursor-Overlay statt im Menü-Muster (Wiedererkennung des
  eigenen Beschlusses vom 18.09. fehlte); doppeltes row++ in
  for-Kopf und -Körper. **Hilfe:** Flag-Muster für den
  Drain-Ausgang, Home-ohne-Umbruch-Erklärung, Schritt-für-Schritt-
  Begleitung auf Zuruf (Formtief am Vorabend).
- 2026-09-23/25 · Lane Defender M2 B2 Spielfeld-Zeichner
  (BuildFrame im Schritt-Modus, Isor tippt) — **Selbst:** Ecken-
  und Symbol-Konstanten als eigene Idee ergänzt, die 118er-Breite
  selbst benannt; das Copy&Paste-Muster der Zeilen-Schleifen
  erkannt und übertragen (Kappe → Körper); den /2-Fix parallel zur
  Korrektur selbst gemacht; die Zaunpfahl-Lücke auf Anhieb richtig;
  nach der Abnahme selbst die DRY-Frage zur vierfachen
  Lane-Schleife gestellt samt der besseren Nachfrage, ob der Umbau
  warten sollte, weil B4/M3 die Zeilen-Logik ohnehin ändern.
  **Fehlerbild:** Rückgabewerte der Bauer verworfen statt
  eingesammelt (Korb-Muster fehlte); \n zweimal an der falschen
  Stelle (an der Lücke, am return) — Regel „jede Bildschirmzeile
  schließt sich selbst" erst im zweiten Anlauf; Einzelzeilen
  (Spieler) in 18er-Schleifen verpackt und Shop samt return in der
  Schleife (Klammer-Struktur); deutsches VERTIKAL im englischen
  Code. **Hilfe:** Schritt-Modus 3a–3d mit Zwischenlesen,
  Soll-Visuals (Zonen-Render, \n-Bild), Klammer-Entwirrung auf
  Zuruf.
- 2026-09-25 · Lane Defender M2 B3 Spieler (CPlayer-Ausbau, Isor
  tippt im Schritt-Modus) — **Selbst:** im Entwurf die Trennung
  „Methode beim Spieler" schon halb richtig vorgedacht;
  MoveLeft-Beispiel eigenständig zu MoveRight gespiegelt (nach
  Zaunpfahl-Korrektur); Fall-Stapel im Switch selbst platziert;
  das Referenz-Muster der Namenseingabe wiedererkannt.
  **Fehlerbild:** neue Methoden im private-Block angelegt
  (Schaufenster/Lager verwechselt); MoveRight-Wächter `>= Count`
  statt `>= Count-1` (T wäre aus dem Feld gesprungen — am
  Zahlenbeispiel gefunden); die Referenz-Reise nur an 1 von 3
  Stellen umgesetzt (Header), dabei die Überladungs-Falle erklärt
  bekommen (baut fehlerfrei, reist aber nie); IntelliSense-Kringel
  als Compiler-Urteil gelesen („er kennt CPlayer nicht" — Build
  war grün). Mentaler Knoten „String manipulieren" durch das
  Wegwerf-Frame-Bild gelöst (Bewegung = Zahl ändern + neu bauen —
  der eigene Bauer machte es längst vor). **Hilfe:** MoveLeft als
  vorgemachtes Beispiel, Wegwerf-Frame-Visual, Zeilen-Verortung
  des Eingabe-Switch.
- 2026-09-26 · Lane Defender M2 B4 Schießen (CShot + erster
  vector, Isor tippt im Schritt-Modus) — **Selbst:** im Entwurf
  mit der Dictionary-Idee den M4-Kollisionscheck vorweggedacht
  („gleiche Position → handeln") und selbst gespürt, dass es
  einfacher gehen muss; die kritische Nachfrage zum Range-for
  („muss ich nicht sagen, bis wohin?") — führte zur
  Klemmen-gegen-Sterben-Unterscheidung; Leertaste-Case und
  Beutel-Zustand selbst platziert; erster eigener Konstruktor.
  **Fehlerbild:** der Methoden-Nachname `CShot::` fehlte komplett
  (zweites Mal, dass die Antwort auf einer eigenen Knowledge-Seite
  stand); das IntelliSense-Echo im gesunden Header als
  Header-Fehler gelesen; die Drei-Stellen-Kette erneut
  unvollständig (Aufruf vergaß den Beutel — Wiederholung des
  B3-Musters Header/Definition/Aufruf); Update-Block zunächst
  hinter Zeichnen/Warten platziert (Tick-Ordnung). **Hilfe:**
  vector als C#-Übersetzungstabelle, Rückwärts-erase mit
  Zahlen-Trace, Konstruktor-Erklärung, CShot-Körper als Vorlage
  nach dem Parse-Chaos.
- 2026-09-27 · Lane Defender M3-Design (Gegner-Hierarchie,
  Spawn-Plan, Speicher, Figuren) — **Selbst:** den
  Hierarchie-Zuschnitt komplett selbst mitgebracht (Normal/Tank/Boss
  als Dreier-Modell; den Runner als globalen Level-Effekt erkannt
  statt als Klasse — eigene Vereinfachung); das Spawn-System als
  Level-Budget selbst entworfen (Max-Zahl je Level, Level-Ende,
  Boss-Ausnahme) und den Durchbruch bewusst einfach gehalten; im
  Verständnis-Check die delete-vor-erase-Regel selbst richtig
  begründet (Adresse weg = Objekt unerreichbar). **Hilfe:** den
  Spawn-Abstand als Lücke des Plans benannt bekommen; Tabelle statt
  Zufalls-Zuwachs, Rest-Wahrscheinlichkeit und Belegt-Wächter als
  Vereinfachungen; das Speicher-Thema nach ehrlichem „bin mir nicht
  sicher" komplett erklärt bekommen (C#-GC-Brücke, Slicing als
  Karton-Bild, die drei Lebensenden). **Fehlerbild:** keines —
  reine Design-Runde ohne Code.
- 2026-09-27 · Lane Defender M3 B1 Klassen (CEnemy + zwei Erben,
  Isor tippt im Schritt-Modus) — **Selbst:** das komplette
  CEnemy-Gerüst ungefragt selbst vorgebaut, SAE fehlerfrei
  (Präfixe, private unten, Erstinitialisierung, Dateipaar) — erste
  eigene Klasse ohne Vorlage; den Tank eigenständig als Spiegel
  gebaut; mitten im Umbau die SAE-Pointer-Regel selbst aufgerufen
  und den neuen Code dagegen gehalten (nullptr-Familie geklärt:
  Platzhalter nur, wenn der echte Wert später kommt); Kringel
  gemeldet statt weitergebaut. **Fehlerbild:** Startzeile blieb -1 —
  das eigene -1-Muster machte es sichtbar; Setter-Reflex aus C#
  (drei Hintertüren → Schaufenster-Bild); die Erbschafts-Zeile im
  Header vergessen und nur die Übergabe gebaut (Erben heißt zwei
  Stellen — diesmal hatte der Kringel recht: Meldung wörtlich
  lesen); das „mal zwei" in der Übergabe versteckt (Konstante trägt
  die Wahrheit); zweimal ungespeichert prüfen lassen (Claude liest
  nur die Platte). **Hilfe:** Erbschafts- und Übergabe-Zeile erklärt
  (private wirkt auch gegen Kinder), virtual als
  „Wer antwortet?"-Bild, erster new/delete-Lebenszyklus samt
  ESC-Aufräumzeile; der Doppel-Geburtsorte-Moment (ein Durchgang
  Turm, dann Bauer — derselbe Zeiger, zwei Objekte) als ungeplantes
  Polymorphie-Experiment gedeutet.
- 2026-09-27 · Lane Defender M3 B2 Liste und Spawner (Regler mitten
  im Baustein auf Zuruf gedreht: Claude tippt, Isor liest gegen —
  Abgabedruck) — **Selbst:** Beutel-Deklaration und
  Bewegungs-Schleife noch selbst getippt; die
  Compiler-Fehlerliste als Landkarte des Umbaus benutzt; die
  Abnahme über den Fünf-Punkte-Testbogen selbst gefahren (Turm
  wandert je Neustart — Saat-Prinzip erkannt); danach aktiv das
  gemeinsame Durchgehen des gelieferten Codes eingefordert („damit
  ich alles verstehe"). **Hilfe:** Rückwärts-Schleife mit
  delete-vor-erase, ESC-Aufräum-Schleife, BuildFrame-Zellsuche
  (pEnemyHere-nullptr-Muster), Schrittintervall am virtual-Hook
  und der komplette Spawner (Abstand-Zähler, Lane-Würfel mit
  Belegt-Wächter, Typ-Würfel als Rest-Wahrscheinlichkeit,
  srand/rand) geliefert und erklärt bekommen. **Fehlerbild:**
  Überforderung beim Listen-Umbau ehrlich gemeldet („ich komme
  nicht mehr mit") statt weiterzuwursteln — der Regler-Wechsel war
  die Antwort des Harness, kein Versagen.
- 2026-09-28 · Lane Defender M3, Vormittag (Pointer-Klärung +
  Tick-Aufräumen, Isor tippt wieder) — **Selbst:** den
  Lesbarkeits-Befund selbst erhoben („jeder Block sollte heißen,
  was er macht") und den kompletten Umbau in fünf benannte
  Funktionen selbst getippt, ab Runde 3 mit selbst gebildeten
  Köpfen; die SAE-Präfixfrage selbst gestellt (gibt es a_v für
  Vector? — Liste ist abgeschlossen, nein); F12-zur-Deklaration als
  Reflex übernommen und im Selbst-Check richtig gelesen.
  **Fehlerbild:** die gelernte Member-nullptr-Regel auf alle
  Pointer verallgemeinert („Pointer gehören in die Klasse") —
  aufgelöst über das Wohnungs-Bild (Lebensdauer wählt den Wohnort;
  die Regel gilt und kommt beim M5-Skill-Slot); beim Kopf-Bilden
  den Stern in die Schuss-Köpfe mitkopiert (Kopf erzählte
  Adressen, Körper Werte — Compiler als Schiedsrichter); Wurzel
  benannt: C# hat die Wert/Adresse-Wahl nie gezeigt, Klassen waren
  immer unsichtbar Referenzen. **Hilfe:** Wohnungs-Diagramm und
  Beutel-Beschriftungs-Bild, Kopie-Desaster-Beispiel für die
  int&-Zähler der Königsrunde (Spawner-Extraktion), Erinnerung,
  dass der Aufrufer kein & schreibt (anders als C#s ref).
- 2026-09-28 · Lane Defender M3 B3 Lebensenden (Isor tippt) —
  **Selbst:** den CPlayer-Ausbau komplett ungefragt vorgebaut —
  Handlungen statt Setter, Klemm-Gedanke, Konstanten, und AddLife
  als eigener Vorgriff auf den M4-Shop-Kauf; die Debugger-Abnahme
  selbst gefahren (Breakpoint fünfmal, Watch 20 → 15).
  **Fehlerbild:** Konstante „I_ZERO_LIVE = 1" — der Name log, und
  die Untergrenze 1 hätte den Spieler unsterblich gemacht
  (Design-Anker: Niederlage bei 0); Startwert 30 statt der
  beschlossenen 20; Live/Life-Wortfamilie verwechselt; Parameter
  erst ohne, dann mit halbem SAE-Präfix — samt Entdeckung, dass
  der Compiler Parameter-NAMEN zwischen Header und cpp nicht
  vergleicht (a_value gegen value, Build grün). **Hilfe:**
  Befundliste mit Begründung je Fund, Durchbruchs-Kosten als
  benannte Konstante, Debugger-Testplan.
- 2026-09-28 · Lane Defender M4-Design (Kollision, Feuerrate, Gold,
  Shop) — **Selbst:** den Kollisions-Aufschlag mit dem richtigen
  Kern-Instinkt gemacht (im Bewegungs-Moment prüfen — „der Schuss
  prüft seine nächste Position"); die eigene
  Schuss-Geschwindigkeits-Idee selbst angezweifelt und damit
  richtig gelegen (kein Schadens-Gewinn, nur Tunnel-Risiko); den
  Spielgefühl-Einwand gegen Cooldowns präzise formuliert und damit
  die Schlucken-Lösung provoziert; „immer kaufen, einfach Keys"
  deckungsgleich mit dem eigenen Live-Shop-Beschluss vom 20.09.
  erinnert. **Hilfe:** die zweite Tunnel-Richtung gezeigt (Gegner
  tritt auf wartenden Schuss) und zum Doppel-Prüfungs-Zuschnitt
  verallgemeinert; Arcade-Muster „geschluckt statt bestraft" samt
  Zahlenstaffel; Gold- und Schadens-Werte als Rechenbeispiel
  (130 G je Level gegen 100 G Erstpreis). **Fehlerbild:** keines —
  Design-Runde.
- 2026-09-28 · Lane Defender M4 B1 Spieler-Werte und HUD-Zeile
  (Isor tippt) — **Selbst:** im Entwurf mitten im Satz selbst
  korrigiert (void-Update verworfen, String-Bauer gewählt — das
  Build-Muster der Datei erkannt); die drei Shop-Stats samt
  Konstanten und Gettern exakt nach dem m_iLives-Muster gebaut;
  den BuildFrame-Umbau auf const CPlayer& allein durchgezogen
  (Signatur, beide Vergleiche, Aufrufstelle). **Fehlerbild:**
  „std::string += int" — die char-Überladung schluckt die Zahl als
  unsichtbares Steuerzeichen, und beide Versuche (direkt und
  to_string) blieben als Doppelzeilen stehen; die fertige Funktion
  nicht eingehängt — der Aufruf am Tick-Ende verwirft den
  Rückgabewert, die HUD-Zeile druckt weiter die Konstante (der
  void-Gedanke des ersten Entwurfs). **Hilfe:** Review-Runde mit
  der char-Überladung als Erklärstück (C# ruft ToString, C++
  deutet die Zahl als Zeichencode) und der Einhäng-Kette (Standort
  über BuildFrame, Zeile 113, toter Aufruf weg).
- 2026-09-28 · Lane Defender M4 B2 Kollision (Regler-Wechsel
  mittendrin: bis zur Schleifen-Hülle Isor, ab der Gegner-Suche
  Claude auf Zuruf — Energie am Abend aufgebraucht) — **Selbst:**
  Entwurf mit exakt richtiger Parameter-Wahl (Player, Gegner-,
  Schuss-Liste) samt Selbstkorrektur „Enemy, nicht Player"; die
  Vorarbeiten weitgehend allein (Reward-Feld und -Konstanten,
  TakeDamage mit ungefragter Null-Klemme nach dem eigenen
  RemoveLife-Muster, AddGold); Hülle und Rückwärts-Schleife aus dem
  eigenen RemoveFinishedShots-Muster abgeleitet. **Fehlerbild:**
  das vierte Startwert-Feld zweimal halb — erst Konstanten ohne
  Konstruktor-Weg (Feld blieb −1, Gold wäre gesunken), dann
  Parameter angenommen, aber nicht zugewiesen (C4100 als Beleg am
  Build vorgeführt); „Hülle steht" gemeldet, als die Schleife noch
  fehlte; einmal Ungespeichertes als fertig gemeldet (VS-Puffer).
  **Hilfe:** Zerlegung in Einzel-Handgriffe nach „zu viel auf
  einmal"; Gegner-Suche (Index statt Pointer, −1 statt nullptr),
  Treffer-Block (Schaden zur Trefferzeit, Gold vor delete, Schuss
  immer verbraucht) und Tick-Doppelruf von Claude getippt.
- 2026-09-29 · Lane Defender M4 B2-Abnahme (Erklär-Runde vor dem
  Test, Isor spielt selbst) — **Selbst:** im Verstehens-Check die
  Gold-Bedingung exakt begründet (Turm nach dem ersten Treffer
  nicht tot, die Health-Frage entscheidet) und die Zweistufigkeit
  des Turms erklärt; F5-Testbogen komplett bestanden — alle fünf
  Punkte, HUD-Soll 130 Gold erreicht. **Hilfe:** das Tick-für-Tick
  des Doppelschuss-Falls nachgezogen (zwei Drücke im selben Tick =
  deckungsgleiche Schüsse, ein HandleCollisions-Aufruf erledigt
  beide; vorwärts würde der zweite übersprungen und flöge für
  immer am Turm vorbei); davor die Erklär-Runde mit Tick-Bild,
  Treffer-Kette und Platztausch-Stepper samt Handy-Seite.
  **Fehlerbild:** keines — Abnahme-Runde.
- 2026-09-29 · Lane Defender M4 B3 Feuer-Sperre und Shop (Isor tippt
  die Sperre, ab den Shop-Cases Claude auf Zuruf) — **Selbst:** das
  Zwei-Werte-Modell im Entwurf benannt (Stat im Player, Zählen in
  der Szene), die Sperre komplett selbst getippt (stilles Schlucken,
  Neustart aus dem Stat, Zählstelle nach dem Drain); die Try-Idee
  selbst eingebracht — RemoveGold als bool, besser als der
  vorgeschlagene GetGold-Check in der Szene; zwei eigene
  Game-Design-Befunde am laufenden Spiel (Kauf ohne Sound,
  AtkSpeed-Anzeige läuft verkehrt herum). **Fehlerbild:** der
  unbewachte Runterzähler (lief ins Minus, „genau 0" nie wieder
  wahr — Fix nach Verweis aufs eigene Spawner-Muster);
  I_BASE_ADD_DAMAGE = 0 als stiller No-Op-Kauf; die VS-Puffer-Falle
  in Gegenrichtung (alter Puffer überschrieb den frischen Stand auf
  der Platte). **Hilfe:** Minus-Verlauf als Zahlen-Tabelle; die
  Try-Grenze erklärt (kein zweites Try nach dem Gold-Abzug —
  Rückbuchungs-Falle); Shop-Cases, Sounds und Stufen-Anzeige von
  Claude getippt, Builds über MSBuild geprüft.
- 2026-09-30 · Lane Defender M5-Design (Boss und Skill-Slot) —
  **Selbst:** den kompletten Boss-Zuschnitt vorgeschlagen (zufällige
  Lane, Durchbruch −5 Leben, Gold 500 mit Verdoppler — die eigene
  Reihe 500/1000/2000 war der Skalierer schon); den polymorphen
  Skill-Slot ohne Gerüst richtig entworfen: Zeiger wohnt im Spieler,
  startet auf null, eigene Basisklasse mit Multishot-Erben, die
  Leertaste prüft den Zeiger, das Objekt lebt auf dem Heap (Heap
  selbst richtig verortet); Multishot bewusst simpel geschnitten
  (rechte Nachbar-Lane, am Rand kein Zusatzschuss) und das
  JSON-Leaderboard selbst als zu teuer eingestuft; im Gegenhalten
  die Entweder-oder-Delegation selbst verteidigt (künftige Skills
  verändern den Schuss, statt nur zu ergänzen — Claudes
  Zusatz-Hook-Vorschlag verworfen, Isors Schnitt wurde der
  Beschluss). **Fehlerbild:**
  Begriffe vermischt — „Referenz im Pointer" (ein Zeiger speichert
  eine Adresse; die Referenz ist das andere, das Alias-Konstrukt aus
  L3) und „abstrakte Klasse" als Wort für jede eigene Klasse (der
  Fachbegriff meint nur Klassen mit rein-virtueller Methode, die
  sich nicht instanziieren lassen). **Hilfe:** Begriffs-Sortierung
  Pointer/Referenz/abstrakt mit Diagramm am eigenen Entwurf.
- 2026-09-30 · Lane Defender M5 B1 Boss (Development, Isor tippt) —
  **Selbst:** CBoss als Startwert-Erben ungefragt komplett allein
  vorgebaut (Muster und Werte exakt, eigener cstdint-Include
  sauberer als der Altbestand); den ersten Override des Projekts
  nach der Fallen-Erklärung fehlerfrei getippt (Signatur samt
  const, override-Schlüsselwort); Balance.h angelegt und den
  Include eigenständig in die .cpp statt in den Header gelegt —
  besser als Claudes Vorschlag; die Fünf-Parameter-Frage selbst
  aufgeworfen (Antwort: ok bei drei festen Aufrufern,
  Parameter-Objekt wartet nach YAGNI); die
  delete-Reihenfolge-Falle beim Durchbruch-Umbau erstmals **selbst**
  erkannt (Getter nach dem delete = Frage an ein gelöschtes Objekt)
  und die Zwischenspeicher-Lösung hergeleitet — Claudes Zusatz nur,
  dass die Effekt-vor-delete-Umstellung aus dem eigenen
  M4-Kollisionsblock dieselbe Falle eine Zeile billiger löst; einen
  Bool-Rückgabewert für RemoveLife erwogen und im Gespräch
  einsortiert (Try-Muster nur für Operationen, die scheitern
  können). **Fehlerbild:** die
  Tempo-Konstante erst definiert, aber nicht benutzt (Override
  fehlte, Boss fiel mit Basis-Tempo 3); beim fünften
  Konstruktor-Feld die zuvor angekündigte Vertauschungs-Falle in
  anderer Gestalt — Step-Interval-Konstanten (3/3/6) an die
  Durchbruch-Position gereicht statt 1/1/5, dazu zwei
  Doppel-Konstanten in Balance.h und den Getter vergessen; alles
  kompiliert grün, gefunden nur im Gegenlesen; beim Boss-Spawn den
  Würfelwurf per erneutem int32_t in eine Verschattung gelegt
  (zweite iBossLane nur im if-Block, die äußere bliebe −1) und den
  Boss-Spawn zunächst in den RunSpawner statt in die
  Levelbeginn-Vorbereitung gedacht — dort löste die Trennung
  „Tick-Maschine gegen Einmal-Vorbereitung" den Knoten; die
  Verschattung direkt danach ein zweites Mal gebaut (bool in beiden
  if/else-Zweigen des Sperr-Wächters — das äußere true hätte immer
  gewonnen, der Wächter wäre wirkungslos; im Gegenlesen gefunden,
  dazu die Kurzform gezeigt: ein Vergleich ist schon ein bool; auf
  die Nachfrage „nur eine andere Schreibweise?" den toten Wächter
  per Zeilen-Trace belegt — verdeckt hatte ihn der Zufall, denn der
  Boss blockiert Zeile 0 selbst und das Testlevel hat nur fünf
  Spawns). **Hilfe:**
  Override-Fallen-Tabelle; Geschwister-Includes auf Zuruf von
  Claude nachgezogen; MSBuild-Prüfläufe durch Claude.
