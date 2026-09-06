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
