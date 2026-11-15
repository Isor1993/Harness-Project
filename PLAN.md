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

*(überschrieben 2026-11-15 beim `/harness:ende` der Session
„Code-Durchgang P-B6". Design-Runde P-B7 ist entschieden — vier
DECISIONS-Einträge vom 15.11. —, der Code-Durchgang ist komplett, der
14.11.-Code gilt als Isors. Neu: Refactor-Merkliste P-R in der
ROADMAP, Hilfe-Level erhöht bis Prototyp-Stand, Lageplan-Tafel.)*

**P-B7 bauen — der Dorfschütze (~8–10 h, eher unterer Rand):**
1. Optionaler Fünf-Minuten-Blitzcheck zum Einstieg: Distanzfeld und
   RestorePath-Mengenlogik — die zwei müden Stellen aus Station 3
   (Lern-Log, 2026-11-15).
2. Erste Entwurfsfrage: der **Skript-Zuschnitt** — Brief-Paar fürs
   Turm-Setzen (eigenes Netz-Skript oder Anbau an PathGridNet),
   Wächter-Skript, Panel als drittes InfoPanelUI-Kind. Die sechs
   Andock-Nähte stehen auf der Lageplan-Tafel (ARTIFACT_INDEX →
   „⚙️ System · Code-Lageplan").
3. Zuschnitt: **nur die Grundfigur** — platzieren über die Figur bei
   gültigem Weg (`IsPathValid`), `CellContent.Tower`, schießen,
   Kopfgeld Normal 5, Preis 50 (DECISIONS vom 2026-11-15).
4. Feature-Stopp 18.–20.11., danach P-B8 mit Streichrecht.
   Hilfe-Level: Claude greift stärker unter die Arme; Rückeroberung
   in der Refactor-Runde (DECISIONS → „Fertig bauen vor Refactoring").

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

