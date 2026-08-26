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

*(geschrieben 2026-08-26 — dritte Session des Tages: die offenen
Harness-Punkte abgearbeitet, danach zwei Prüfdurchgänge)*

**Fünfzehn Befunde warten auf Behebung** — neun in
`_HARNESS_CODE_GUIDELINES.md`, sechs in `_HARNESS_UNI_SCHICHT.md`.
Das muss eine **frische** Session tun (`Kern/WORKFLOW.md`: Prüfer und
Ausführender nicht dieselbe). Zwei Entscheidungen gehören davor, beide
in `Kern/ROADMAP.md` benannt; für die Uni-Hälfte fehlt die
Revier-Freigabe. Sonst unverändert offen: **Phase 0 des Koop-Prototyps**
(`Projekte/Isor_Tower/ROADMAP.md`, zwei Wochen, vor dem Semesterstart).
Sonntags die Ein-Seiten-Prüfung: dran ist `💡 EditorWindow & MVP`.

---

### Testphase — erst auf Isors Zuruf

Sie beginnt **nicht** nach der Prüfung und nicht nach Kalender, sondern
wenn Isor den Harness für so weit erklärt. Bis dahin wird am Harness
selbst gearbeitet: prüfen, was noch nicht trägt, und es verbessern.
Claude meldet die Testphase nicht als fällig. *(Isor, 2026-08-23;
Begründung in `Kern/DECISIONS.md`.)*

**Gegen den Stand vom 2026-08-26 gehalten:** Beide Punkte unten gelten
unverändert. Der Vorbehalt oben ist an diesem Tag zum ersten Mal
eingelöst worden — die Arbeit ging in „prüfen, was noch nicht trägt":
zwei Prüfdurchgänge, fünfzehn Befunde, vier neue Regeln. Die Testphase
selbst bleibt ungefragt liegen.

- [ ] Den Datenbaum aufräumen, in Viererpaketen — Punkte in
      `IsorBackup/ROADMAP.md`. Zugleich die erste Belastungsprobe des
      Harness im Betrieb; was nicht trägt, kommt in `STOERUNGEN.md`.
- [ ] Danach zurück ins Projekt Isor's Tower
      (`Projekte/Isor_Tower/ROADMAP.md`).
      **Gegen den Stand vom 2026-08-26 gehalten:** Der Abschnitt
      „Basiszustand nach der Abgabe", auf den dieser Punkt zeigte, gibt
      es nicht mehr — die Projekt-ROADMAP wurde für Semester 3 neu
      geschrieben. Offen und von Isor zu entscheiden ist außerdem die
      Reihenfolge: Der Koop-Prototyp hat jetzt einen Semestertermin, der
      Datenbaum keinen.
