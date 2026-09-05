# -*- coding: utf-8 -*-
"""Packt eine Auslieferung des Kerns nach der Packliste in Kern/VERSIONIERUNG.md.

Warum als Skript und nicht von Hand: Die Packliste sagt ausdrücklich, dass
sie **nicht je Auslieferung neu entschieden** wird (Isor, 2026-08-24). Von
Hand gepackt wurde sie beide bisherigen Male verschieden ausgelegt. Dieses
Skript ist die Durchsetzung derselben Regel — dieselbe Bauart wie
index_bauen.py: erzeugen statt pflegen (Kern/DOC_RULES.md, Abschnitt 5).

Was es tut:
  * Regeldateien, Werkzeuge, Befehle, Vorlagen, Bilder  -> unverändert
  * Chroniken und Bestandslisten -> Kopf plus genau ein Muster-Eintrag
  * index_geplant.txt            -> nur der Kommentarkopf
  * PFADE.md                     -> Pfad-Spalte auf (nicht eingerichtet)
  * Kern/Zeugnisse/              -> gar nicht
  * Kern/LERNLOG.md              -> gar nicht (beschreibt eine Person)

Aufruf:
    python ausliefern.py              Trockenlauf — meldet nur, schreibt nichts
    python ausliefern.py --schreiben  legt die Auslieferung wirklich an

Ein Handgriff bleibt und ist keiner, den das Skript nehmen kann: Die
Kopf-Abschnitte einiger Dateien erzählen, warum **dieses** Projekt sie
angelegt hat. Nach dem Packen wird das Ergebnis einmal durchgesehen und
projektfremde Kopf-Absätze werden entfernt (Kern/VERSIONIERUNG.md,
Packliste). Das Skript listet am Ende auf, welche Dateien das betrifft.
"""
import io
import os
import re
import shutil
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

HIER = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.abspath(os.path.join(HIER, "..", ".."))

# Zeile, an der in dieser Datei ein Eintrag beginnt. Je Datei eine eigene:
# Die Formate sind bewusst verschieden (eine Chronik zählt Ereignisse, eine
# ROADMAP Aufgaben), und ein gemeinsamer Ausdruck träfe entweder zu viel
# oder zu wenig. Was hier fehlt, geht unverändert mit.
EINTRAG_BEGINNT = {
    u"ARTIFACT_INDEX.md": u"^## ",
    u"DECISIONS.md":      u"^## \\d{4}-",
    u"LOG.md":            u"^- \\d{4}-",
    u"ROADMAP.md":        u"^- \\[",
    u"STOERUNGEN.md":     u"^### \\d{4}-",
    u"_ARCHIV.md":        u"^## \\d{4}-",
}

MUSTER_VERMERK = (
    u"<!-- Auslieferung: Ab hier steht genau EIN echter Eintrag als Muster.\n"
    u"     Er zeigt Länge, Belegtiefe und Tonfall, die die Format-Zeile oben\n"
    u"     nicht ausdrücken kann. Beim ersten eigenen Eintrag darf er weg. -->\n")

# Woran ein Kopf-Absatz erkennbar ist, der die Geschichte dieses Projekts
# erzählt statt einer Regel: an einem **konkreten Datum**. Der Name „Isor"
# taugt dafür nicht — er steht in jeder Regeldatei als Rolle („Isor baut und
# entscheidet") und wäre ein Fehlalarm in fast jeder Zeile.
PROJEKTFREMD = re.compile(u"\\d{4}-\\d{2}-\\d{2}")

# Ein Absatz, der nur dieses Projekt betrifft, wird in der Quelle eingeklammert
# und beim Packen entfernt. So bleibt die Auslieferung reproduzierbar: Sie
# entsteht in einem Lauf, ohne Nachbearbeitung von Hand — und wer die Quelle
# liest, sieht sofort, was ein fremdes Projekt davon nicht bekommt.
NICHT_AUSLIEFERN = re.compile(
    u"\\n?<!-- nicht ausliefern -->.*?<!-- /nicht ausliefern -->\\n?",
    re.S)


def lies(pfad):
    with io.open(pfad, encoding="utf-8") as fh:
        return fh.read()


def schreibe(pfad, text):
    ordner = os.path.dirname(pfad)
    if not os.path.isdir(ordner):
        os.makedirs(ordner)
    with io.open(pfad, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)


def version():
    """Die Harness-Version aus CLAUDE.md — sie besitzt die Nummer."""
    treffer = re.search(u"Harness-Version:\\s*([0-9]+\\.[0-9]+\\.[0-9]+)",
                        lies(os.path.join(BASE, "CLAUDE.md")))
    if not treffer:
        raise SystemExit(u"CLAUDE.md trägt keine Zeile „Harness-Version: X.Y.Z\".")
    return treffer.group(1)


def marke_pfad(marke):
    """Der Pfad hinter einer Marke aus Kern/PFADE.md, sonst None."""
    for zeile in lies(os.path.join(BASE, "Kern", "PFADE.md")).split("\n"):
        if not zeile.startswith("|") or (u"`%s`" % marke) not in zeile:
            continue
        spalten = [s.strip() for s in zeile.strip().strip("|").split("|")]
        if len(spalten) >= 2:
            treffer = re.search(u"`([^`]+)`", spalten[1])
            if treffer:
                return treffer.group(1)
    return None


def auf_ein_muster(text, ausdruck):
    """Kopf plus den ersten Eintrag; alles Weitere fällt weg."""
    zeilen = text.split("\n")
    muster = re.compile(ausdruck)
    treffer = [i for i, z in enumerate(zeilen) if muster.match(z)]
    if not treffer:
        return text, 0
    erster = treffer[0]
    zweiter = treffer[1] if len(treffer) > 1 else len(zeilen)
    kopf = u"\n".join(zeilen[:erster]).rstrip() + u"\n\n"
    eintrag = u"\n".join(zeilen[erster:zweiter]).rstrip() + u"\n"
    return kopf + MUSTER_VERMERK + eintrag, len(treffer) - 1


def pfade_leeren(text):
    """Marken und Zweck bleiben, die Pfad-Spalte wird zurückgesetzt."""
    neu = []
    for zeile in text.split("\n"):
        spalten = [s.strip() for s in zeile.strip().strip("|").split("|")]
        if (zeile.startswith("|") and len(spalten) >= 3
                and re.match(u"^`[A-ZÄÖÜ][A-ZÄÖÜ_]*`$", spalten[0])):
            neu.append(u"| %s | (nicht eingerichtet) | %s |"
                       % (spalten[0], spalten[2]))
        else:
            neu.append(zeile)
    return u"\n".join(neu)


def nur_kommentarkopf(text):
    """Alles ab der ersten Zeile, die kein Kommentar und nicht leer ist."""
    zeilen = text.split("\n")
    behalten = []
    for zeile in zeilen:
        if zeile.strip() and not zeile.lstrip().startswith("#"):
            break
        behalten.append(zeile)
    return u"\n".join(behalten).rstrip() + u"\n"


def quellen():
    """Was überhaupt mitgeht: CLAUDE.md und Kern/, ohne Zeugnisse, Lern-Log und Cache."""
    treffer = [u"CLAUDE.md"]
    for wurzel, ordner, dateien in os.walk(os.path.join(BASE, "Kern")):
        ordner[:] = [o for o in ordner
                     if o not in ("Zeugnisse", "__pycache__")]
        for d in sorted(dateien):
            if d.endswith(".pyc"):
                continue
            # Beschreibt eine Person, nicht den Harness (VERSIONIERUNG.md).
            if d == "LERNLOG.md":
                continue
            voll = os.path.join(wurzel, d)
            treffer.append(os.path.relpath(voll, BASE).replace("\\", "/"))
    return sorted(treffer)


def main():
    schreiben = "--schreiben" in sys.argv
    nummer = version()
    datenbaum = marke_pfad(u"DATENBAUM")
    if not datenbaum:
        raise SystemExit(u"Marke DATENBAUM ist in Kern/PFADE.md nicht gesetzt.")
    ziel = os.path.join(datenbaum, "05_Werkzeuge", "Harness_Auslieferungen",
                        "Harness_%s" % nummer)

    print(u"ausliefern.py — Harness %s" % nummer)
    print(u"Ziel: %s" % ziel)
    if os.path.isdir(ziel):
        raise SystemExit(
            u"\nDiese Auslieferung gibt es schon. Eine abgelegte Auslieferung\n"
            u"wird nie bearbeitet (Kern/VERSIONIERUNG.md) — für eine Änderung\n"
            u"wird der Harness geändert und eine neue Nummer vergeben.")
    print(u"Modus: %s\n" % (u"SCHREIBEN" if schreiben
                            else u"Trockenlauf, es wird nichts angelegt"))

    nachsehen = []
    bytes_gesamt = 0
    for rel in quellen():
        name = os.path.basename(rel)
        text = lies(os.path.join(BASE, rel))
        text, eingeklammert = NICHT_AUSLIEFERN.subn(u"\n", text)
        vermerk = u"unverändert"
        if name in EINTRAG_BEGINNT:
            text, weg = auf_ein_muster(text, EINTRAG_BEGINNT[name])
            vermerk = u"Kopf + 1 Muster (%d Einträge weg)" % weg
        elif name == u"PFADE.md":
            text = pfade_leeren(text)
            vermerk = u"Pfad-Spalte zurückgesetzt"
        elif name == u"index_geplant.txt":
            text = nur_kommentarkopf(text)
            vermerk = u"nur Kommentarkopf"
        elif name.endswith(".svg") or name.endswith(".json"):
            vermerk = u"unverändert (binärnah, 1:1)"
        if eingeklammert:
            vermerk += u" · %d eingeklammerter Absatz weg" % eingeklammert

        # Geprüft wird genau der Kopf — alles vor dem Muster-Vermerk. Ein
        # Aufteilen an der ersten „## "-Überschrift ginge daneben: LOG.md hat
        # keine, und dann stünde die ganze Datei als Kopf da.
        # Nur die geschnittenen Dateien. Eine Regeldatei nennt Daten und Namen
        # als **Beleg** für ihre Regeln — das soll so bleiben und ist kein
        # Altbestand. Bei einer Chronik dagegen ist der Kopf die einzige
        # Stelle, an der noch Projektgeschichte stehen kann.
        kopf = text.split(MUSTER_VERMERK)[0]
        if vermerk.startswith((u"Kopf", u"Pfad")) and PROJEKTFREMD.search(kopf):
            nachsehen.append(rel)

        bytes_gesamt += len(text.encode("utf-8"))
        print(u"  %-34s %s" % (rel, vermerk))
        if schreiben:
            zieldatei = os.path.join(ziel, rel.replace("/", os.sep))
            if name.endswith(".svg"):
                # 1:1, damit keine Zeilenendenwandlung eine Grafik anfasst.
                ordner = os.path.dirname(zieldatei)
                if not os.path.isdir(ordner):
                    os.makedirs(ordner)
                shutil.copy2(os.path.join(BASE, rel), zieldatei)
            else:
                schreibe(zieldatei, text)

    print(u"\n%d Dateien, %d Bytes." % (len(quellen()), bytes_gesamt))
    if nachsehen:
        print(u"\nVon Hand durchsehen — der Kopf nennt ein Datum oder einen "
              u"Namen\nund erzählt damit womöglich die Geschichte dieses "
              u"Projekts:")
        for rel in nachsehen:
            print(u"  ! %s" % rel)
    if not schreiben:
        print(u"\nNichts angelegt. Mit --schreiben wirklich packen.")


if __name__ == "__main__":
    main()
