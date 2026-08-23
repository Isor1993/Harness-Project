# -*- coding: utf-8 -*-
"""Erzeugt INDEX.md aus den Ownership-Zeilen der Harness-Dateien.

Arbeitsteilung (Kern/DOC_RULES.md, Abschnitt 5):
  Das Skript besitzt die *Liste* — welche Dateien es gibt und was ihre
  Ownership-Zeile sagt. Der Mensch besitzt die *geplanten* Einträge; die
  stehen in index_geplant.txt daneben, weil es die Dateien noch nicht gibt.

Aufruf:
    python index_bauen.py            Probelauf, schreibt nichts
    python index_bauen.py --write    schreibt INDEX.md

Meldungen:
    ! ohne Ownership-Zeile   -> Datei erscheint im INDEX als Warnung
    ! geplant, existiert     -> Eintrag in index_geplant.txt ist erledigt
"""
import io
import os
import re
import sys

HIER = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.abspath(os.path.join(HIER, "..", ".."))   # Repo-Wurzel
ZIEL = os.path.join(BASE, "INDEX.md")
GEPLANT = os.path.join(HIER, "index_geplant.txt")
BEFEHLE = os.path.join(BASE, "Kern", "Befehle")

# Seit 2.0.0 liegen .claude\ und .git\ INNERHALB der Wurzel. Beide sind
# Programmordner, kein Bestand — ohne diese Zeile stuenden die fuenf
# Arbeitskopien der Befehle als Dateien ohne Ownership-Zeile im INDEX.
NICHT_DURCHSUCHEN = (".claude", ".git", "__pycache__")

SCHICHTEN = [
    ("Oben", "Oben — schichtübergreifend"),
    ("Kern", "Kern — generisch, wandert in jedes Projekt mit"),
    ("Uni", "Uni — studienspezifisch, herausnehmbar"),
    ("IsorBackup", "IsorBackup — Regeln für den externen Datenbaum"),
    ("Projekte", "Projekte"),
    ("Temporär", "Temporär — eine Datei je Durchgang, danach ins Archiv"),
]

KOPF = u"""# INDEX.md — Landkarte

Ownership: Nur die Landkarte — welche Dokumente existieren und wofür jedes
zuständig ist. Eine Zeile pro Dokument, keine Inhalte.

**Diese Datei wird erzeugt.** Sie kommt aus der `Ownership:`-Zeile jeder
Datei; von Hand geändert wird sie nicht, sondern über
`Kern/Werkzeuge/index_bauen.py`. Geplante, noch nicht gebaute Dokumente
stehen daneben in `index_geplant.txt`.

Der INDEX bleibt bewusst **oben** und wird nicht in eine Schicht
einsortiert: Er ist ein Register über alle Schichten, und ein Register
muss vollständig sein (`Kern/DOC_RULES.md`, Abschnitt 8).

Eine Datei ohne `Ownership:`-Zeile erscheint hier als ⚠ — so setzt sich
die Regel „keine neue Datei ohne INDEX-Eintrag" von selbst durch, statt
erinnert werden zu müssen.

Eine Gruppe führt der Index abweichend, unten mit eigener Tabelle: die
**Befehle**. Sie tragen keine Ownership-Zeile — ihre `description` ist
die Zuständigkeit. Sie stehen hier, weil ein Register vollständig sein
muss (`Kern/DOC_RULES.md`, Abschnitt 8).
"""


def schicht_von(rel):
    teile = rel.replace("\\", "/").split("/")
    if os.path.basename(rel).startswith("_HARNESS_"):
        return "Temporär"
    if len(teile) == 1:
        return "Oben"
    if teile[0] in ("Kern", "Uni", "IsorBackup", "Projekte"):
        return teile[0]
    return "Oben"


def ownership_satz(pfad):
    """Erste Aussage der Ownership-Zeile, ohne Zeilenumbrüche."""
    with io.open(pfad, encoding="utf-8") as fh:
        text = fh.read()
    m = re.search(r"^Ownership:\s*(.+?)(?:\n\n|\Z)", text, re.S | re.M)
    if not m:
        return None
    satz = " ".join(m.group(1).split())
    # erster Satz, aber Abkürzungen wie „z. B." nicht als Ende werten
    stelle = re.search(r"\.(?=\s+[A-ZÄÖÜ**])", satz)
    if stelle and stelle.start() > 25:
        satz = satz[:stelle.start() + 1]
    return satz


def werkzeuge():
    """Skripte in den Werkzeuge-Ordnern, mit ihrer ersten Beschreibungszeile."""
    treffer = []
    for wurzel, ordner, dateien in os.walk(BASE):
        if os.path.basename(wurzel) != "Werkzeuge":
            continue
        for d in sorted(dateien):
            if not d.endswith((".py", ".ps1")):
                continue
            voll = os.path.join(wurzel, d)
            rel = os.path.relpath(voll, BASE).replace("\\", "/")
            with io.open(voll, encoding="utf-8-sig") as fh:
                text = fh.read()
            m = re.search(r'"""(.+?)$|^\s{4}(\S.+?)$', text, re.M)
            satz = (m.group(1) or m.group(2)).strip() if m else u"—"
            treffer.append((rel, satz))
    return treffer


def befehle():
    """Ausloeser in Kern/Befehle/, mit ihrer description aus dem Frontmatter.

    Sie tragen keine Ownership-Zeile, weil sie keine Dokumente sind, sondern
    acht Zeilen Zeiger auf ihre Regeldatei (Kern/WORKFLOW.md, Die Befehle).
    Die description ist zugleich der Text, den das /-Menue anzeigt.
    """
    if not os.path.isdir(BEFEHLE):
        return []
    treffer = []
    for d in sorted(os.listdir(BEFEHLE)):
        if not d.endswith(".md"):
            continue
        with io.open(os.path.join(BEFEHLE, d), encoding="utf-8") as fh:
            text = fh.read()
        m = re.search(r"^description:\s*(.+?)$", text, re.M)
        satz = m.group(1).strip() if m else u"⚠ **keine `description:`** — bitte ergänzen"
        treffer.append((u"/harness:" + d[:-3], satz))
    return treffer


def sammeln():
    gefunden = {}
    for wurzel, ordner, dateien in os.walk(BASE):
        ordner[:] = [o for o in ordner
                     if o not in ("Werkzeuge", "Befehle") + NICHT_DURCHSUCHEN]
        for d in sorted(dateien):
            if not d.endswith(".md"):
                continue
            voll = os.path.join(wurzel, d)
            rel = os.path.relpath(voll, BASE)
            gefunden[rel.replace("\\", "/")] = ownership_satz(voll)
    return gefunden


def geplante():
    if not os.path.exists(GEPLANT):
        return []
    zeilen = []
    with io.open(GEPLANT, encoding="utf-8") as fh:
        for z in fh:
            z = z.strip()
            if not z or z.startswith("#"):
                continue
            if "|" not in z:
                print("  ! Zeile ohne | in index_geplant.txt:", z[:50])
                continue
            pfad, text = z.split("|", 1)
            zeilen.append((pfad.strip(), text.strip()))
    return zeilen


def main():
    gefunden = sammeln()
    plan = geplante()
    warnungen = []

    tabellen = {name: [] for name, _ in SCHICHTEN}

    for rel in sorted(gefunden):
        satz = gefunden[rel]
        s = schicht_von(rel)
        if satz is None:
            warnungen.append(rel)
            satz = u"⚠ **keine `Ownership:`-Zeile** — bitte ergänzen"
        tabellen[s].append((rel, satz))

    for pfad, text in plan:
        if pfad.replace("\\", "/") in gefunden:
            print("  ! geplant, existiert aber schon:", pfad)
            continue
        tabellen[schicht_von(pfad)].append((pfad, u"(geplant) " + text))

    zeilen = [KOPF]
    gesamt = 0
    for name, ueberschrift in SCHICHTEN:
        eintraege = sorted(tabellen[name])
        if not eintraege:
            continue
        zeilen.append(u"\n## " + ueberschrift + u"\n\n")
        zeilen.append(u"| Dokument | Zuständigkeit |\n|---|---|\n")
        for rel, satz in eintraege:
            zeilen.append(u"| `%s` | %s |\n" % (rel, satz))
        gesamt += len(eintraege)

    wz = werkzeuge()
    if wz:
        zeilen.append(u"\n## Werkzeuge — erzeugen und pflegen die Dateien oben\n\n")
        zeilen.append(u"| Skript | Zweck |\n|---|---|\n")
        for rel, satz in sorted(wz):
            zeilen.append(u"| `%s` | %s |\n" % (rel, satz))

    bf = befehle()
    if bf:
        zeilen.append(u"\n## Befehle — Auslöser, Ablauf in `Kern/WORKFLOW.md`\n\n")
        zeilen.append(u"Original in `Kern/Befehle/`, Arbeitskopie in "
                      u"`.claude\\commands\\harness\\` — geändert wird das "
                      u"Original, dann kopiert.\n\n")
        zeilen.append(u"| Befehl | Tut |\n|---|---|\n")
        for name, satz in sorted(bf):
            zeilen.append(u"| `%s` | %s |\n" % (name, satz))

    print("Dateien: %d, geplant: %d, Werkzeuge: %d, Befehle: %d, Zeilen: %d"
          % (len(gefunden), len(plan), len(wz), len(bf), gesamt))
    if warnungen:
        print("OHNE Ownership-Zeile (%d):" % len(warnungen))
        for w in warnungen:
            print("   !", w)
    else:
        print("Alle Dateien haben eine Ownership-Zeile.")

    if "--write" in sys.argv:
        with io.open(ZIEL, "w", encoding="utf-8") as fh:
            fh.write("".join(zeilen))
        print("geschrieben:", ZIEL)
    else:
        print("\n(Probelauf. Mit --write wird geschrieben.)")


if __name__ == "__main__":
    main()
