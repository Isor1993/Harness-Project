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

*(geschrieben 2026-08-28 beim `/harness:ende`)*

**Phase 0 ist abgeschlossen** — alle fünf Abnahmepunkte, der Seed-Weg ist
gemessen und trägt (`Projekte/Isor_Tower/LOG.md`, 2026-08-28). Als Nächstes
**Phase 1 · Spielernaht und Einstieg** (3 Wochen,
`Projekte/Isor_Tower/ROADMAP.md`): Input nach Reichweite teilen,
Spieler-Prefab zum Netzobjekt, Einstieg über das bestehende Hauptmenü, und
`ISessionService` als Naht für einen späteren Steam-Transport. Sonntags die
Ein-Seiten-Prüfung: dran ist `💡 EditorWindow & MVP`.

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
- [ ] **Abgabe-Struktur anlegen**, sobald die Semester-Aufgaben da sind
      (`Uni/ROADMAP.md`) — der Punkt, an dem im zweiten Semester Zeit
      verloren ging.
