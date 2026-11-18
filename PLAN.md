# PLAN.md — Arbeitsplan

Ownership: Was in den nächsten ein bis drei Wochen dran ist,
schichtübergreifend — und der Auftrag an die nächste Session. Was
irgendwann kommt, steht in der ROADMAP der jeweiligen Schicht; was
passiert ist, im LOG.
Format: `### <Zeitraum oder Baustein>` mit Aufzählungspunkten, je Punkt
ein Satz. Erledigtes wird abgehakt, nicht gelöscht. Der Abschnitt „Für
die nächste Session" steht oben und hat sein eigenes Format.

**Höchstens ~100 Zeilen.** Ist ein Zeitraum durch, wandert er als
Ereignis ins LOG, erledigte Punkte werden in der ROADMAP abgehakt, und
diese Datei wird **geleert** — nicht archiviert. Die Geschichte steht
im LOG.

---

## Für die nächste Session

Steht **oben**, weil es das Erste ist, was zählt. Wird bei jedem
`/harness:ende` **überschrieben**, nie ergänzt — „gerade nichts offen"
ist ein gültiger Inhalt. Höchstens fünf Zeilen; Ausführliches steht in
der Datei, auf die hier verwiesen wird.

*(überschrieben 2026-11-17 beim `/harness:ende` der Session
„Pathmakers TD · P-B7 Dorfschütze". P-B7 ist fertig und abgehakt —
der Core-Loop ist erstmals geschlossen, Solo-Tests grün, Artifacts
nachgezogen, Zeiten samt P-B5-Nachtrag gebucht.)*

**Erst Build, dann die große Design-Runde (Isors Entscheid, 17.11.):**
1. **V 0.0.005 bauen** — Player Settings auf `0.0.005`, Ablage im
   Datenbaum unter `02_Projekte\PathmakersTD\Builds\
   PathmakersTD_0.0.005_2026-11-18\` (`Kern/PFADE.md` → `DATENBAUM`).
   Die Marke „erster geschlossener Core-Loop".
2. **Große Design-Runde als Erstes** (Typ Brainstorm/Design): Isor
   legt fest, wie das Spiel am Ende sein soll — liefert zugleich das
   GDD/Pitch-Material der Pufferwoche und das Zielbild für den
   Alpha-Refactor. Die Wächter-Runde (Basisklasse/Strategy, Isors
   Naht-Skizze am M4-Eintrag) wird mit verhandelt. Begründung und
   Termin: ROADMAP → P-R.
3. Danach **P-B8** (Mine + Arbeiter, ~7–8 h), soweit das Fenster bis
   zum Feature-Stopp **Fr 20.11.** trägt — Streichrecht greift sonst.
4. Hilfe-Level bleibt erhöht bis Prototyp-Stand; Rückeroberung in der
   Refactor-Runde (DECISIONS → „Fertig bauen vor Refactoring").

---

### Die Testphase läuft — seit 2026-08-27

Sie hat auf Isors Zuruf begonnen, wie es seit dem 2026-08-23 vorgesehen
war (`Kern/DECISIONS.md`). Ab jetzt gilt: **Der Harness wird benutzt,
nicht gebaut.** Claude schlägt von sich aus keine Umbauten mehr vor.

Was im Betrieb nicht trägt, wird als Störung notiert
(`Kern/STOERUNGEN.md`) und über die Doku-Pflicht zu einem ROADMAP-Punkt —
nicht sofort behoben. Ein Befund ist ein Zustand, kein Auftrag.

- [x] **Phase 0 · Netz-Prüfstand** — **erledigt am 2026-08-28**, in fünf
      Tagen statt zwei Wochen. Der Vergleichstest ist bestanden (AMD gegen
      Intel, identische Prüfsummen), die Zeitrechnung des Semesters bleibt
      also wie geplant. Zusätzlich belegt: Relay trägt über zwei Netze,
      getestet bis auf die Philippinen.
- [ ] **Der Datenbaum wartet** (`IsorBackup/ROADMAP.md`, vier Punkte).
      **Kein Termin** — bewusst hinter Phase 0 gestellt, weil nur der
      Prototyp einen Semestertermin hat (Isor, 2026-08-27). Er bleibt
      die geplante Belastungsprobe des Harness im Betrieb.
- [x] **Abgabe-Struktur anlegen**, sobald die Semester-Aufgaben da sind
      (`Uni/ROADMAP.md`) — der Punkt, an dem im zweiten Semester Zeit
      verloren ging. Die Aufgaben sind seit dem 2026-09-07 bestätigt.
      **Erledigt am 2026-09-08** — Beleg: `Uni/ROADMAP.md` →
      „Abgabe-Struktur beim Semesterstart kopieren".

