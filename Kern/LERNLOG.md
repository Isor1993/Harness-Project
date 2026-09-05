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
