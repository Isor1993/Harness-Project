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

*(geschrieben 2026-08-25 abends — fünf Kern-Punkte geschlossen: E56,
Pflegetag, Revier-Regel, E14, E61b samt Abnahme)*

Als Nächstes: die **Repo/Git-Design-Session** (`Kern/ROADMAP.md`,
letzter Baupunkt — fürs Wochenende) oder die Testphase auf Zuruf. Beim
TDD führt jetzt das **Markdown** — Text nur noch in
`Projekte/Isor_Tower/TDD.md`, Bau per `abgabe_bauen.py`
(`Uni/DOCX_RULES.md`). Sonntags erste Ein-Seiten-Prüfung des
Pflegetags: dran ist `💡 EditorWindow & MVP`. Typ und Modus fragt die
Session selbst.

---

### Testphase — erst auf Isors Zuruf

Sie beginnt **nicht** nach der Prüfung und nicht nach Kalender, sondern
wenn Isor den Harness für so weit erklärt. Bis dahin wird am Harness
selbst gearbeitet: prüfen, was noch nicht trägt, und es verbessern.
Claude meldet die Testphase nicht als fällig. *(Isor, 2026-08-23;
Begründung in `Kern/DECISIONS.md`.)*

- [ ] Den Datenbaum aufräumen, in Viererpaketen — Punkte in
      `IsorBackup/ROADMAP.md`. Zugleich die erste Belastungsprobe des
      Harness im Betrieb; was nicht trägt, kommt in `STOERUNGEN.md`.
- [ ] Danach zurück ins Projekt Isor's Tower, Basiszustand nach der
      Abgabe (`Projekte/Isor_Tower/ROADMAP.md`).
