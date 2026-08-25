# -*- coding: utf-8 -*-
"""Erzeugt eine .docx-Abgabefassung aus einem Markdown-Manuskript.

Vollgenerierung (Kern/DECISIONS.md, 2026-08-25): Jeder Lauf baut die
Zieldatei komplett neu — Quelle ist das Markdown, die Styles kommen aus
einer Referenz-.docx (Formatvorlage). Layout-Feinschliff von Hand wird
dabei überschrieben und gehört deshalb ans Ende, unmittelbar vor die
Abgabe (Uni/DOCX_RULES.md).

Selbstschutz, in dieser Reihenfolge:
  1. Sperr-Check — liegt neben dem Ziel eine ~$-Datei, ist es in Word
     geöffnet: Abbruch, nichts wird geschrieben.
  2. Sicherung — besteht das Ziel schon, wandert es vorher nach
     Sicherung\\<Name>_<JJJJ-MM-TT_HHMM>_vor-neubau.docx.
  3. Bauen — pandoc <quelle> --reference-doc=<vorlage> -o <ziel>.
  4. Nachzählen — Absätze, Medien und Content-Types des Pakets werden
     geprüft und gemeldet. Der Sichttest bleibt Pflicht: in Word
     öffnen, Strg+A und F9, Seiten ansehen (Uni/DOCX_RULES.md).

Beschriftungen: Der Nachlauf `beschriftungen_verfelden` macht aus
`Tabelle <Name>`- und `Abbildung <Name>`-Absätzen echte Beschriftungen
(Style plus SEQ-Feld samt Sprungmarke) — Abbildungs- und
Tabellenverzeichnis füllen sich damit bei F9. Querverweise im Fließtext
(„Tabelle 1") werden REF-Felder auf diese Marken: Sie springen wieder
und aktualisieren ihre Nummer bei F9 mit.

Titelteil-Modus (`--titelteil=<datei.docx>`): Layout-Seiten — Titelblatt,
Erklärungen, Verzeichnis-Felder — überleben die Markdown-Schleife nicht
(belegt am 2026-08-25: Tabulatoren, Zentrierung und Felder gingen
verloren). Sie leben deshalb als fixe Titelteil-Datei; das Werkzeug
setzt sie unverändert vor den gebauten Fließtext und beginnt dahinter
einen neuen Abschnitt mit arabischer Zählung ab 1. Dieser Modus braucht
Word und pywin32 auf dem Rechner — dieselbe Voraussetzung wie das
F9-Füllen der Felder danach.

Aufruf:
    python abgabe_bauen.py <quelle.md> <vorlage.docx> <ziel.docx>
        [<bildordner>] [--titelteil=<datei.docx>]

<bildordner> ist der Ordner, gegen den relative Bildpfade der Quelle
aufgelöst werden (pandoc --resource-path); ohne Angabe der Ordner der
Quelle.
"""
import datetime
import io
import os
import shutil
import subprocess
import sys
import tempfile
import zipfile

MEDIEN_ENDUNGEN = {".png", ".jpg", ".jpeg", ".gif", ".emf", ".wmf", ".bmp", ".tiff"}


def abbruch(text):
    sys.exit("Abbruch: %s" % text)


def sperr_check(ziel):
    """Word-Sperrdatei neben dem Ziel? Dann ist es geöffnet."""
    ordner, name = os.path.split(ziel)
    sperre = os.path.join(ordner, "~$" + name[2:] if len(name) > 2 else "~$" + name)
    if os.path.exists(sperre):
        abbruch("%s ist in Word geöffnet (Sperrdatei %s). Erst speichern "
                "und schließen." % (name, os.path.basename(sperre)))


def sichern(ziel):
    """Bestehendes Ziel mit Zeitstempel in den Sicherung-Ordner kopieren."""
    if not os.path.exists(ziel):
        return None
    ordner, name = os.path.split(ziel)
    stamm, endung = os.path.splitext(name)
    sicherung_ordner = os.path.join(ordner, "Sicherung")
    if not os.path.isdir(sicherung_ordner):
        os.makedirs(sicherung_ordner)
    stempel = datetime.datetime.now().strftime("%Y-%m-%d_%H%M")
    kopie = os.path.join(sicherung_ordner,
                         "%s_%s_vor-neubau%s" % (stamm, stempel, endung))
    shutil.copy2(ziel, kopie)
    return kopie


def bauen(quelle, vorlage, ziel, bildordner):
    kommando = [
        "pandoc", quelle,
        "--reference-doc=" + vorlage,
        "--resource-path=" + bildordner,
        "-o", ziel,
    ]
    lauf = subprocess.run(kommando, capture_output=True, text=True,
                          encoding="utf-8", errors="replace")
    if lauf.returncode != 0:
        abbruch("pandoc meldete:\n%s" % lauf.stderr.strip())
    if lauf.stderr.strip():
        print("pandoc-Hinweise:")
        print("  " + lauf.stderr.strip().replace("\n", "\n  "))


def xml_escape(text):
    return (text.replace("&", "&amp;").replace("<", "&lt;")
            .replace(">", "&gt;"))


def beschriftungen_verfelden(pfad):
    """Macht aus den Beschriftungs-Absätzen echte Word-Beschriftungen:
    Style `Beschriftung` plus SEQ-Feld — dieselben Bezeichner (`Tabelle`,
    `Abbildung`), die die Verzeichnis-Felder des Titelteils einsammeln.
    Erkannt wird am Textmuster `Tabelle <Name>` / `Abbildung <Name>`
    ohne Ziffer (die Ziffer war das verlorene Feld); Tabellen-
    Beschriftungen wandern unter ihre Tabelle, wie im Original."""
    import re
    with zipfile.ZipFile(pfad) as z:
        doc = z.read("word/document.xml").decode("utf-8")

    tabellen = []

    def merken(m):
        tabellen.append(m.group(0))
        return "\x00%d\x00" % (len(tabellen) - 1)

    doc = re.sub(r"<w:tbl>.*?</w:tbl>", merken, doc, flags=re.S)

    gezaehlt = {"Tabelle": 0, "Abbildung": 0}

    def absatz_text(p):
        return "".join(re.findall(r"<w:t[^>]*>([^<]*)</w:t>", p))

    def verfelden(m):
        p = m.group(0)
        text = absatz_text(p)
        art = re.match(r"^(Tabelle|Abbildung)\s+(\S.*)$", text)
        if not art or len(text) > 150 or art.group(2)[0].isdigit():
            return p
        label, rest = art.group(1), art.group(2)
        gezaehlt[label] += 1
        nr = gezaehlt[label]
        # Die pandoc-Sprungmarken des Absatzes bleiben erhalten (alte
        # Anker-Links zeigen weiter hierher); dazu kommt eine eigene
        # Marke um Label und Nummer als Ziel der REF-Felder.
        alte_marken = "".join(
            re.findall(r"<w:bookmark(?:Start|End)\b[^>]*/>", p))
        marke = "Ref%s%d" % (label, nr)
        mid = 9000 + gezaehlt["Tabelle"] + gezaehlt["Abbildung"]
        neu = (
            '<w:p><w:pPr><w:pStyle w:val="Beschriftung"/></w:pPr>%s'
            '<w:bookmarkStart w:id="%d" w:name="%s"/>'
            '<w:r><w:t xml:space="preserve">%s </w:t></w:r>'
            '<w:r><w:fldChar w:fldCharType="begin"/></w:r>'
            '<w:r><w:instrText xml:space="preserve"> SEQ %s \\* ARABIC '
            '</w:instrText></w:r>'
            '<w:r><w:fldChar w:fldCharType="separate"/></w:r>'
            '<w:r><w:t>0</w:t></w:r>'
            '<w:r><w:fldChar w:fldCharType="end"/></w:r>'
            '<w:bookmarkEnd w:id="%d"/>'
            '<w:r><w:t xml:space="preserve"> %s</w:t></w:r></w:p>'
            % (alte_marken, mid, marke, label, label, mid,
               xml_escape(rest))
        )
        return neu

    doc = re.sub(r"<w:p(?: [^>]*)?>.*?</w:p>", verfelden, doc, flags=re.S)

    # Tabellen-Beschriftungen unter ihre Tabelle schieben (Original-
    # Konvention): erzeugter Beschriftungs-Absatz direkt vor einem
    # Tabellen-Platzhalter tauscht mit ihm den Platz.
    doc, verschoben = re.subn(
        r'(<w:p><w:pPr><w:pStyle w:val="Beschriftung"/></w:pPr>'
        r'(?:<w:bookmark[^>]*/>)*'
        r'<w:r><w:t xml:space="preserve">Tabelle .*?</w:p>)'
        r'(\s*\x00\d+\x00)',
        r"\2\1", doc, flags=re.S)
    print("Tabellen-Beschriftungen unter die Tabelle verschoben:",
          verschoben)

    doc = re.sub(r"\x00(\d+)\x00", lambda m: tabellen[int(m.group(1))], doc)

    # Querverweise: „Tabelle N"/„Abbildung N"-Links zeigten auf Anker,
    # die es nach dem Neubau nicht mehr gibt — sie werden zu REF-Feldern
    # auf die eigenen Marken. Damit springen sie wieder, und die Nummern
    # aktualisieren sich bei F9 mit. Läuft nach dem Demaskieren, damit
    # auch Verweise in Tabellenzellen erfasst werden.
    verweise = {"umgebaut": 0}

    def verlinken(m):
        inner = m.group(1)
        text = "".join(re.findall(r"<w:t[^>]*>([^<]*)</w:t>", inner))
        ziel = re.match(r"^(Tabelle|Abbildung)\s+(\d+)$", text.strip())
        if not ziel or int(ziel.group(2)) > gezaehlt[ziel.group(1)]:
            return m.group(0)
        verweise["umgebaut"] += 1
        marke = "Ref%s%s" % (ziel.group(1), ziel.group(2))
        return (
            '<w:r><w:fldChar w:fldCharType="begin"/></w:r>'
            '<w:r><w:instrText xml:space="preserve"> REF %s \\h '
            '</w:instrText></w:r>'
            '<w:r><w:fldChar w:fldCharType="separate"/></w:r>'
            '<w:r><w:t xml:space="preserve">%s</w:t></w:r>'
            '<w:r><w:fldChar w:fldCharType="end"/></w:r>'
            % (marke, xml_escape(text.strip()))
        )

    doc = re.sub(r'<w:hyperlink\b[^>]*w:anchor="[^"]*"[^>]*>(.*?)'
                 r"</w:hyperlink>", verlinken, doc, flags=re.S)
    print("Querverweise auf REF-Felder umgebaut:", verweise["umgebaut"])

    with zipfile.ZipFile(pfad) as alt, \
         zipfile.ZipFile(pfad + ".neu", "w", zipfile.ZIP_DEFLATED) as ziel:
        for eintrag in alt.infolist():
            daten = alt.read(eintrag.filename)
            if eintrag.filename == "word/document.xml":
                daten = doc.encode("utf-8")
            ziel.writestr(eintrag, daten)
    os.replace(pfad + ".neu", pfad)
    print("Beschriftungen verfeldert: %d Tabellen, %d Abbildungen"
          % (gezaehlt["Tabelle"], gezaehlt["Abbildung"]))


def mit_titelteil_mergen(titelteil, hauptteil, ziel):
    """Titelteil unverändert übernehmen, Fließtext in neuem Abschnitt
    (arabisch ab 1) anhängen. Läuft über Word — die einzige Instanz,
    die Abschnitte, Medien und Felder verlässlich zusammenführt."""
    try:
        import win32com.client
    except ImportError:
        abbruch("Titelteil-Modus braucht pywin32 (pip install pywin32).")
    word = win32com.client.Dispatch("Word.Application")
    word.Visible = False
    word.DisplayAlerts = 0
    try:
        doc = word.Documents.Open(os.path.abspath(titelteil),
                                  False, True)  # ReadOnly
        doc.SaveAs2(os.path.abspath(ziel))
        titel_sections = doc.Sections.Count
        rng = doc.Content
        rng.Collapse(0)                      # ans Ende
        rng.InsertBreak(2)                   # Abschnittswechsel, neue Seite
        rng = doc.Content
        rng.Collapse(0)
        rng.InsertFile(os.path.abspath(hauptteil))
        # Seitenzählung: durchgehend ab der ersten Seite, Anzeige überall
        # arabisch (Formatvorgabe, Variante „durchgehend"; Isor,
        # 2026-08-25). Dazu darf keine Section neu zählen, und die
        # PAGE-Felder der Fußzeilen verlieren ihren römischen
        # Feldschalter — der übersteuert sonst jedes Abschnittsformat.
        for s in range(1, doc.Sections.Count + 1):
            sektion = doc.Sections(s)
            nummern = sektion.Footers(1).PageNumbers
            nummern.NumberStyle = 0          # arabisch
            if s > 1:
                nummern.RestartNumberingAtSection = False
            for typ in (1, 2, 3):            # Standard, erste Seite, gerade
                fuss = sektion.Footers(typ)
                if not fuss.Exists:
                    continue
                if s > 1 and fuss.LinkToPrevious:
                    continue                 # erbt die normalisierte Fassung
                for feld in fuss.Range.Fields:
                    if feld.Type == 33:      # wdFieldPage
                        feld.Code.Text = " PAGE "
                        feld.Update()
        doc.Save()
        doc.Close(0)
    finally:
        word.Quit()


def nachzaehlen(ziel):
    """Paket öffnen und die Kennzahlen melden — kein Urteil, nur Zahlen."""
    with zipfile.ZipFile(ziel) as z:
        namen = z.namelist()
        inhalt = z.read("word/document.xml").decode("utf-8")
        typen = z.read("[Content_Types].xml").decode("utf-8")
    medien = [n for n in namen if n.startswith("word/media/")]
    ohne_typ = [m for m in medien
                if 'PartName="/%s"' % m not in typen
                and 'Extension="%s"' % m.rsplit(".", 1)[-1].lower() not in typen]
    print("Absätze: %d · Medien: %d · Größe: %.1f MB"
          % (inhalt.count("<w:p>") + inhalt.count("<w:p "), len(medien),
             os.path.getsize(ziel) / 1024.0 / 1024.0))
    if ohne_typ:
        print("  ! Medien ohne Content-Type (Word wird meckern): %d — %s"
              % (len(ohne_typ), ", ".join(ohne_typ[:3])))
    else:
        print("Alle Medien im Content-Type-Verzeichnis erfasst.")


def main():
    argumente = [a for a in sys.argv[1:] if not a.startswith("--")]
    titelteil = None
    for a in sys.argv[1:]:
        if a.startswith("--titelteil="):
            titelteil = a.split("=", 1)[1]
    if len(argumente) not in (3, 4):
        abbruch("Aufruf: python abgabe_bauen.py <quelle.md> <vorlage.docx> "
                "<ziel.docx> [<bildordner>] [--titelteil=<datei.docx>]")
    quelle, vorlage, ziel = argumente[:3]
    bildordner = argumente[3] if len(argumente) == 4 \
        else os.path.dirname(os.path.abspath(quelle)) or "."

    pruefpfade = [(quelle, "Quelle"), (vorlage, "Formatvorlage")]
    if titelteil:
        pruefpfade.append((titelteil, "Titelteil"))
    for pfad, rolle in pruefpfade:
        if not os.path.exists(pfad):
            abbruch("%s nicht gefunden: %s" % (rolle, pfad))
    if not os.path.isdir(bildordner):
        abbruch("Bildordner nicht gefunden: %s" % bildordner)

    sperr_check(ziel)
    kopie = sichern(ziel)
    if kopie:
        print("Sicherung:", kopie)
    if titelteil:
        zwischen = os.path.join(tempfile.gettempdir(),
                                "abgabe_hauptteil.docx")
        bauen(quelle, vorlage, zwischen, bildordner)
        beschriftungen_verfelden(zwischen)
        mit_titelteil_mergen(titelteil, zwischen, ziel)
        os.remove(zwischen)
    else:
        bauen(quelle, vorlage, ziel, bildordner)
        beschriftungen_verfelden(ziel)
    print("geschrieben:", ziel)
    nachzaehlen(ziel)
    print("Sichttest bleibt Pflicht: in Word öffnen, Strg+A und F9, "
          "Seiten ansehen.")


if __name__ == "__main__":
    main()
