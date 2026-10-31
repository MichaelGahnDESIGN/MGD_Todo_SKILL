---
name: wissen-ansehen
description: >-
  Findet und öffnet die vorhandene Projektdokumentation. Für /wissen-ansehen,
  Doku anzeigen oder Living Documentation öffnen; verändert keine Inhalte.
metadata:
  version: 1.0.0
---

# /wissen-ansehen – Projektdokumentation öffnen

Zeige die vorhandene Dokumentation des aktuellen Projekts. Dieser Befehl
liest und öffnet; `/wissen` aktualisiert. Keine Dokumentation erzeugen,
Builds starten, Graphen ändern, Pakete installieren oder Inhalte veröffentlichen.

## Vorhandenen Einstieg finden

1. Bestimme die tatsächliche Projektwurzel anhand des aktuellen Auftrags und
   der Projektregeln. Nutze keinen Sammelordner als vermeintliches Projekt.
2. Ermittle den vorhandenen Einstieg mit dem mitgelieferten, nur lesenden
   Helfer. Den Scriptpfad relativ zu diesem Skill auflösen:

   ```sh
   python3 scripts/find_documentation.py --project "<Projektwurzel>"
   ```

   Ein ausdrücklich genannter lokaler Einstieg kann mit
   `--entry "<Pfad relativ zur Projektwurzel>"` gewählt werden.
   Der Helfer bevorzugt dokumentierte HTML-Einstiege aus der README und
   bekannte Dokumentationspfade; Markdown bleibt der Rückfall. Er öffnet
   selbst nichts und führt keinen Projektcode aus.
3. Prüfe das JSON-Ergebnis. Bei `status: found` den tatsächlichen absoluten
   Zielpfad verwenden, nicht einen Beispielpfad aus einem anderen Projekt.
   Fehlt Python, dieselben vorhandenen Pfade lesend prüfen; nichts installieren.

## Anzeigen

- HTML über ein vorhandenes Browser-/Vorschauwerkzeug oder den Betriebssystem-
  Öffner anzeigen. Auf macOS ist zum Beispiel `open "<absoluter Dateipfad>"`
  möglich. Pfade sicher als einzelne Argumente übergeben. Kein Webserver nötig.
- Markdown mit einem vorhandenen Vorschauwerkzeug anzeigen oder einen
  anklickbaren Dateilink anbieten. Keine ungefragte HTML-Konvertierung.
- Zusätzlich einen Dateilink mit absolutem Pfad ausgeben. Ohne Vorschaufunktion
  ehrlich nur den Link anbieten; einen erfolgreichen Browserstart nicht erfinden.
- Eine externe Wiki-/BookStack-Instanz nur öffnen, wenn sie für das Projekt
  bereits dokumentiert oder ausdrücklich angegeben ist. Keine Instanz anlegen,
  Zugangsdaten eintragen oder Inhalte synchronisieren.

## Wenn keine Dokumentation vorhanden ist

Kurz melden: „Für dieses Projekt habe ich noch keinen Dokumentationseinstieg
gefunden.“ `/wissen` als nächsten Schritt nennen. Bei mehreren tatsächlichen
Projekten die Projektwahl klären, statt eine fremde Doku zu öffnen. Keine
fehlenden Dateien oder Verzeichnisse anlegen.

## Abschluss

Knapp den Namen der geöffneten Dokumentation und ihren Dateilink nennen.
Öffnen ist keine Bestätigung, dass Inhalt, Tests oder Live-Stand aktuell sind.
