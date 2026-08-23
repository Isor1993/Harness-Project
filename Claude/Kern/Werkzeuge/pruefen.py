# -*- coding: utf-8 -*-
"""Prüft die Harness-Dateien gegen die Regeln, die sich mechanisch prüfen lassen.

Wird bei jedem `/harness:sichern` aufgerufen (Kern/WORKFLOW.md). Das Skript
**meldet nur** — es ändert nichts. Was behoben wird, entscheiden Isor und
Claude; ein Fund ist ein Befund, kein Auftrag.

Die fünf Prüfungen, jede aus einem belegten Fehler entstanden:
  1 Verweise      tote Pfade in Backticks            (Abnahme 2026-08-22)
  2 Chroniken     Datumsfolge und Pflichtfelder      (Abnahme 2026-08-22, A28)
  3 Befehle       Original gegen Arbeitskopie        (A39)
  4 Zahlwörter    Anzahl in Überschrift oder Fettung (P4, 2026-08-23)
  5 Glossar       Kurzform gegen ihre Besitzerdatei  (P13, 2026-08-23)

Aufruf:
    python pruefen.py               alle Prüfungen
    python pruefen.py 1 4           nur die genannten
    python pruefen.py --glossar-ok  Kurzformen sind gegengelesen, Hinweis weg

Was das Skript NICHT sieht: ob eine Aussage stimmt. Es prüft Form und
Bestand, nicht Inhalt — dafür braucht es weiterhin eine Prüf-Session
(Kern/WORKFLOW.md, Typ „Prüfung").
"""
import io
import os
import re
import sys

HIER = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.abspath(os.path.join(HIER, "..", ".."))          # ...\Claude
BEFEHLE = os.path.join(BASE, "Kern", "Befehle")
ARBEITSKOPIE = os.path.abspath(
    os.path.join(BASE, "..", "..", ".claude", "commands", "harness"))

# Chroniken werden nie geändert; ein Verweis darin beschreibt den Stand von
# damals und ist kein Fund (Kern/DOC_RULES.md, Abschnitte 4 und 6). Dasselbe
# gilt für Archive und Zeugnisse.
CHRONIK_NAMEN = ("LOG.md", "STOERUNGEN.md", "_ARCHIV.md", "DECISIONS.md")
CHRONIK_ORDNER = ("Zeugnisse", "DECISIONS")

# Schichten dieses Baums. Nur was so anfängt, kann das Skript überhaupt
# nachschlagen — ein Verweis auf den Knowledge-Ordner oder das Tower-Repo
# liegt außerhalb seiner Zuständigkeit und ist deshalb kein Fund.
EIGENE_PFADE = ("Kern/", "Uni/", "Projekte/", "IsorBackup/")
EIGENE_DATEIEN = ("CLAUDE.md", "INDEX.md", "PLAN.md")

# Pflichtfelder je Chronik-Art (Kern/DOC_RULES.md, Abschnitt 3: Format-Zeile).
PFLICHTFELDER = {
    "DECISIONS.md": (u"Was", u"Warum"),
    "STOERUNGEN.md": (u"Was", u"Ursache", u"Regel", u"Stand"),
}

ZAHLWORT = (u"zwei|drei|vier|fünf|sechs|sieben|acht|neun|zehn|"
            u"elf|zwölf|beide")

# Temporäre Befundlisten beschreiben einen abgeschlossenen Durchgang — dort
# trägt eine Anzahl Information statt eines Verfallsdatums.
ZAHLWORT_FREI = ("_HARNESS_",)


def ist_chronik(rel):
    name = os.path.basename(rel)
    if name in CHRONIK_NAMEN:
        return True
    teile = rel.replace("\\", "/").split("/")
    return any(o in teile for o in CHRONIK_ORDNER)


def md_dateien():
    """Alle .md des Harness, relativ zu Claude\\, ohne Werkzeuge und Befehle."""
    treffer = []
    for wurzel, ordner, dateien in os.walk(BASE):
        ordner[:] = [o for o in ordner
                     if o not in ("Werkzeuge", "Befehle", "__pycache__")]
        for d in sorted(dateien):
            if d.endswith(".md"):
                voll = os.path.join(wurzel, d)
                treffer.append(os.path.relpath(voll, BASE).replace("\\", "/"))
    return sorted(treffer)


def lies(rel):
    with io.open(os.path.join(BASE, rel), encoding="utf-8") as fh:
        return fh.read()


def zeilen_von(text):
    return text.split("\n")


# ---------------------------------------------------------------- Prüfung 1

def pruefe_verweise(dateien):
    """Jeder Verweis auf eine Datei *dieses* Baums muss es geben.

    Geprüft wird nur, was eindeutig hierher zeigt — ein Pfad, der mit einer
    Schicht beginnt, oder eine der drei Dateien oben. Alles andere kann das
    Skript nicht nachschlagen: `validate.py` liegt im Uni-Ordner, `_Quelle.txt`
    im Datenbaum, `README.md` im Knowledge. Ein Fund, den niemand prüfen kann,
    ist Rauschen — und Rauschen killt den Prüfer (belegt: erster Lauf am
    2026-08-23, 34 Verweis-Funde, davon 3 echt).

    Ebenfalls kein Fund: geplante Dateien aus index_geplant.txt. Der INDEX
    führt sie bewusst, sie existieren nur noch nicht.
    """
    funde = []
    uebersprungen = 0
    plan = geplante_pfade()
    muster = re.compile(r"`([^`\n]+?\.(?:md|py|ps1|txt))`")
    for rel in dateien:
        if ist_chronik(rel):
            uebersprungen += 1
            continue
        for nr, zeile in enumerate(zeilen_von(lies(rel)), 1):
            for treffer in muster.findall(zeile):
                pfad = treffer.strip().replace("\\", "/")
                if "<" in pfad or "*" in pfad:
                    continue
                if not zeigt_hierher(pfad):
                    continue
                if pfad in plan:
                    continue
                if os.path.exists(os.path.join(BASE, pfad)):
                    continue
                funde.append((rel, nr, u"toter Verweis: `%s`" % pfad))
    return funde, u"%d Chronik-Dateien übersprungen" % uebersprungen


def zeigt_hierher(pfad):
    return pfad.startswith(EIGENE_PFADE) or pfad in EIGENE_DATEIEN


def geplante_pfade():
    """Die noch nicht gebauten Dateien aus index_geplant.txt."""
    quelle = os.path.join(HIER, "index_geplant.txt")
    if not os.path.exists(quelle):
        return set()
    pfade = set()
    with io.open(quelle, encoding="utf-8") as fh:
        for z in fh:
            z = z.strip()
            if z and not z.startswith("#") and "|" in z:
                pfade.add(z.split("|", 1)[0].strip().replace("\\", "/"))
    return pfade


# ---------------------------------------------------------------- Prüfung 2

def pruefe_chroniken(dateien):
    """Älteste oben, und jeder Eintrag trägt seine Pflichtfelder.

    Der Fund, aus dem die Regel stammt: Nachgetragene Einträge landeten
    hinten statt an ihrem Datum, und die Chronik behauptete eine Zeitfolge,
    die sie nicht hatte (A28).
    """
    funde = []
    geprueft = 0
    datum = re.compile(r"^#{2,3}\s*(\d{4})-(\d{2})-(\d{2})|^-\s+(\d{4})-(\d{2})-(\d{2})")
    for rel in dateien:
        if not ist_chronik(rel):
            continue
        geprueft += 1
        text = lies(rel)
        eintraege = []
        for nr, zeile in enumerate(zeilen_von(text), 1):
            m = datum.match(zeile)
            if not m:
                continue
            teile = [t for t in m.groups() if t]
            eintraege.append((nr, "-".join(teile[:3])))
        # Ein Archiv sortiert nach dem Tag der Ablösung; der zitierte Alttext
        # darunter trägt sein eigenes, älteres Datum. Das ist keine verdrehte
        # Reihenfolge, sondern der Zweck der Datei.
        if os.path.basename(rel) != "_ARCHIV.md":
            vorheriges = None
            for nr, wert in eintraege:
                if vorheriges and wert < vorheriges:
                    funde.append((rel, nr,
                                  u"Datum %s steht nach %s" % (wert, vorheriges)))
                vorheriges = wert
        funde.extend(fehlende_felder(rel, text))
    return funde, u"%d Chroniken geprüft" % geprueft


def fehlende_felder(rel, text):
    """Pflichtfelder je Eintrag, sofern die Datei welche zugesagt hat."""
    felder = PFLICHTFELDER.get(os.path.basename(rel))
    if not felder:
        return []
    funde = []
    bloecke = re.split(r"\n(?=#{2,3}\s*\d{4}-)", text)
    for block in bloecke[1:]:
        kopf = block.split("\n", 1)[0].strip("# ")
        for feld in felder:
            # „Warum (Isor, 2026-08-22):" ist dasselbe Feld wie „Warum:"
            if not re.search(r"^\**%s\b" % feld, block, re.M):
                funde.append((rel, 0, u"Eintrag `%s` ohne Feld %s"
                              % (kopf[:40], feld)))
    return funde


# ---------------------------------------------------------------- Prüfung 3

def pruefe_befehle(_dateien):
    """Original in Kern/Befehle/ und Arbeitskopie in .claude\\ müssen gleich sein.

    Nur von der Arbeitskopie aus findet Claude Code die Befehle; geändert wird
    aber das Original (Kern/WORKFLOW.md, „Wo die Auslöser liegen"). Ohne
    Abgleich laufen beide auseinander, ohne dass es jemand merkt (A39).
    """
    if not os.path.isdir(ARBEITSKOPIE):
        return [(u"(Arbeitskopie)", 0,
                 u"Ordner fehlt: %s" % ARBEITSKOPIE)], u"nicht vergleichbar"
    funde = []
    originale = sorted(d for d in os.listdir(BEFEHLE) if d.endswith(".md"))
    kopien = sorted(d for d in os.listdir(ARBEITSKOPIE) if d.endswith(".md"))
    for d in originale:
        if d not in kopien:
            funde.append((u"Kern/Befehle/" + d, 0, u"fehlt in der Arbeitskopie"))
            continue
        with io.open(os.path.join(BEFEHLE, d), encoding="utf-8") as fh:
            a = fh.read()
        with io.open(os.path.join(ARBEITSKOPIE, d), encoding="utf-8") as fh:
            b = fh.read()
        if a != b:
            funde.append((u"Kern/Befehle/" + d, 0,
                          u"weicht von der Arbeitskopie ab — Original gilt"))
    for d in kopien:
        if d not in originale:
            funde.append((u".claude/commands/harness/" + d, 0,
                          u"ohne Original in Kern/Befehle/"))
    return funde, u"%d Befehle verglichen" % len(originale)


# ---------------------------------------------------------------- Prüfung 4

def pruefe_zahlwoerter(dateien):
    """Keine Anzahl in Überschrift oder Einleitung, wenn die Liste wachsen kann.

    Erlaubt bleibt sie, wenn die Aufzählung abgeschlossen ist und der Text
    sagt, warum (Kern/DOC_RULES.md, Abschnitt 7). Das kann das Skript nicht
    beurteilen — es meldet die Stelle, das Urteil bleibt beim Leser.
    """
    funde = []
    ueberschrift = re.compile(r"^#{1,6}\s+.*\b(%s)\b" % ZAHLWORT, re.I)
    fettung = re.compile(r"^\*\*[^*\n]*\b(%s)\b[^*\n]*\*\*" % ZAHLWORT, re.I)
    # „in rund zwei Wochen" zählt keine Liste, sondern Zeit.
    zeitangabe = re.compile(r"\b(%s)\s+(Sekunden?|Minuten?|Stunden?|Tage?n?|"
                            u"Wochen?|Monate?n?|Jahre?n?|Semester)" % ZAHLWORT, re.I)
    for rel in dateien:
        if ist_chronik(rel):
            continue
        if any(m in os.path.basename(rel) for m in ZAHLWORT_FREI):
            continue
        for nr, zeile in enumerate(zeilen_von(lies(rel)), 1):
            if zeitangabe.search(zeile):
                continue
            m = ueberschrift.match(zeile) or fettung.match(zeile)
            if m:
                funde.append((rel, nr, u"Anzahl `%s` in: %s"
                              % (m.group(1), zeile.strip()[:60])))
    return funde, u""


# ---------------------------------------------------------------- Prüfung 5

def pruefe_glossar(_dateien):
    """Jede Kurzform nennt ihren Besitzer — der muss existieren und den
    Begriff auch führen.

    Zusätzlich der Hinweis, wenn eine Besitzerdatei jünger ist als das
    Glossar: Dann wurde die Definition womöglich geändert, ohne dass die
    Kurzform nachgezogen wurde. Genau so sammelte GLOSSARY.md in zwei Tagen
    drei falsche Zeilen (P10 bis P13). Der Zeitstempel ist ein Hinweis, kein
    Beweis — nach einem frischen Klon sind alle Dateien gleich alt.
    """
    rel = "Kern/GLOSSARY.md"
    voll = os.path.join(BASE, rel)
    if not os.path.exists(voll):
        return [], u"kein Glossar vorhanden"
    funde = []
    nachziehen = {}
    stand_glossar = os.path.getmtime(voll)
    geprueft = 0
    for nr, zeile in enumerate(zeilen_von(lies(rel)), 1):
        if not zeile.startswith("|") or "**" not in zeile:
            continue
        spalten = [s.strip() for s in zeile.strip().strip("|").split("|")]
        if len(spalten) < 3:
            continue
        begriff = spalten[0].strip("* ")
        besitzer = spalten[-1]
        # „`WORKFLOW.md`, Begriffe" — der Dateiname steht in den Backticks
        m = re.search(r"`([^`]+)`", besitzer)
        datei = (m.group(1) if m else besitzer.split(",")[0]).strip()
        geprueft += 1
        ziele = finde(datei)
        if not ziele:
            funde.append((rel, nr, u"Besitzer nicht gefunden: %s" % datei))
            continue
        texte = []
        for z in ziele:
            with io.open(z, encoding="utf-8") as fh:
                texte.append(fh.read().lower())
        if not any(begriff.lower() in t for t in texte):
            funde.append((rel, nr, u"`%s` kommt in %s nicht vor"
                          % (begriff, datei)))
        elif any(os.path.getmtime(z) > stand_glossar for z in ziele):
            nachziehen.setdefault(datei, []).append(begriff)

    # Ein Sammel-Hinweis je Besitzerdatei statt einer Zeile je Begriff: Wer
    # WORKFLOW.md anfasst, löst sonst elf gleichlautende Meldungen aus.
    for datei in sorted(nachziehen):
        begriffe = nachziehen[datei]
        funde.append((rel, 0, u"Hinweis: %s ist jünger als das Glossar — "
                      u"%d Kurzform%s gegenlesen (%s)"
                      % (datei, len(begriffe), u"" if len(begriffe) == 1 else u"en",
                         u", ".join(begriffe))))
    if nachziehen:
        funde.append((rel, 0, u"    → nach dem Gegenlesen: "
                      u"python pruefen.py --glossar-ok"))
    return funde, u"%d Kurzformen geprüft" % geprueft


def finde(name):
    """Alle Dateien dieses Namens — `CLAUDE.md` gibt es dreimal, und der
    Begriff kann in jeder von ihnen stehen (Notkern: in der obersten)."""
    name = name.replace("\\", "/").lstrip("./")
    treffer = []
    kandidat = os.path.join(BASE, name)
    if os.path.exists(kandidat):
        treffer.append(kandidat)
    kurz = os.path.basename(name)
    for wurzel, ordner, dateien in os.walk(BASE):
        if kurz in dateien:
            voll = os.path.join(wurzel, kurz)
            if voll not in treffer:
                treffer.append(voll)
    for hoch in ("..", os.path.join("..", "..")):
        voll = os.path.abspath(os.path.join(BASE, hoch, kurz))
        if os.path.exists(voll) and voll not in treffer:
            treffer.append(voll)
    return treffer


# ------------------------------------------------------------------- Ablauf

PRUEFUNGEN = [
    (u"Verweise", pruefe_verweise),
    (u"Chroniken", pruefe_chroniken),
    (u"Befehle", pruefe_befehle),
    (u"Zahlwörter", pruefe_zahlwoerter),
    (u"Glossar", pruefe_glossar),
]


def glossar_abgeglichen():
    """Vermerkt, dass die Kurzformen gegengelesen wurden.

    Ohne diesen Griff bliebe der Hinweis stehen, bis jemand das Glossar
    zufällig ändert — und ein Fund, der immer dasteht, wird nach dem dritten
    Mal überlesen. Er setzt nur den Zeitstempel, kein Zeichen im Text.
    """
    ziel = os.path.join(BASE, "Kern", "GLOSSARY.md")
    os.utime(ziel, None)
    print(u"GLOSSARY.md als abgeglichen vermerkt (Zeitstempel auf jetzt).")
    print(u"Der Vermerk hält, bis eine Besitzerdatei erneut geändert wird.")


def main():
    if "--glossar-ok" in sys.argv:
        glossar_abgeglichen()
        return
    gewuenscht = [int(a) for a in sys.argv[1:] if a.isdigit()]
    dateien = md_dateien()
    print(u"pruefen.py — %d Dateien im Bestand\n" % len(dateien))

    gesamt = 0
    for i, (name, funktion) in enumerate(PRUEFUNGEN, 1):
        if gewuenscht and i not in gewuenscht:
            continue
        funde, notiz = funktion(dateien)
        gesamt += len(funde)
        kopf = u"[%d] %-12s %d Fund%s" % (i, name, len(funde),
                                          u"" if len(funde) == 1 else u"e")
        if notiz:
            kopf += u"   (%s)" % notiz
        print(kopf)
        for rel, nr, text in funde:
            ort = u"%s:%d" % (rel, nr) if nr else rel
            print(u"    ! %s — %s" % (ort, text))

    print(u"\nErgebnis: %d Fund%s. Nichts wurde geändert."
          % (gesamt, u"" if gesamt == 1 else u"e"))


if __name__ == "__main__":
    main()
