---
name: todo-doku
description: >-
  Aktualisiert TODO.html, Living Documentation und den lokalen Graphify-Stand
  konsistent, ohne Fakten zu erfinden oder Schutzgrenzen zu überschreiten.
---

# /todo-doku — TODO und Living Documentation abgleichen

Verwende `/todo-doku [Thema]`, wenn eine Produktentscheidung, Änderung oder
Prüfung zugleich in der Living Documentation und der TODO-Liste nachvollziehbar
bleiben soll. Der Befehl pflegt die vorhandenen Projektdateien und aktualisiert
den lokal konfigurierten Graphify-Index. Er implementiert keine Produktfunktion
und veröffentlicht nichts.

## Ablauf

1. **Projektregeln und Ausgangslage lesen.** Lies `AGENTS.md` oder die geltenden
   Projektregeln, das Dokumentations-README, die passende Fachseite und die
   relevante `TODO.html`. Prüfe `git status --short`, damit bestehende lokale
   Änderungen sichtbar und erhalten bleiben. Wenn Graphify eingerichtet ist,
   nutze zuerst `graphify query` und bei Bedarf `graphify path` oder
   `graphify explain`, um betroffene Bereiche gezielt zu finden.
2. **Wissensquelle bestimmen.** Verwende die bereits vorhandene kanonische
   Living Documentation, zum Beispiel `DOKUMENTATION/`, `docs/` oder `WIKI/`.
   Lege keine zweite Dokumentationsstruktur an. Trenne bestätigte Tatsachen,
   Nutzerentscheidungen, Vorschläge, offene Fragen und Risiken. Alte Aussagen,
   die ersetzt wurden, als historisch oder überholt kennzeichnen, nicht still
   als aktuelle Wahrheit stehen lassen.
3. **Fachseite aktualisieren.** Schreibe die dauerhafte Entscheidung oder den
   geprüften Befund zuerst an die inhaltlich zuständige Stelle. Aktualisiere
   Einstiegsseiten nur mit einer kurzen Zusammenfassung und einem Verweis; halte
   keine konkurrierenden Kopien desselben Sachverhalts.
4. **TODO synchronisieren.** Suche die passende bestehende Todo-ID. Aktualisiere
   Titel, Status oder Notizen gezielt und verknüpfe sie mit der Fachseite, wenn
   das dem nächsten Arbeitsschritt hilft. Erstelle nur dann ein neues Todo,
   wenn eine konkrete, noch offene Aufgabe bleibt. Eine Dokumentationsänderung
   allein macht ein Todo nicht erledigt. Setze `done` nur bei nachweislich
   abgeschlossener Aufgabe; lösche keine offenen Todos und erfinde keine IDs.
5. **Graphify neu aufbauen.** Verwende den vom Projekt vorgegebenen lokalen
   Befehl, zum Beispiel `npm run graph:update` oder `graphify update .`. Ändere
   generierte Graphdateien nicht von Hand. Beachte Projektregeln zu
   Ausschlusslisten, privaten Dateien und externen Diensten. Keine semantische
   Extraktion, Cloud-Uploads oder LLM-Beschriftungen starten, wenn das Projekt
   dies nicht erlaubt oder der Nutzer es nicht beauftragt hat.
6. **Änderungen prüfen.** Führe `git diff --check` aus. Prüfe geänderte Links,
   Todo-IDs und Statuswerte sowie, sofern vorhanden, den Projektbefehl zur
   Todo-Validierung. Berichte Grenzen offen, etwa wenn Graphify Inhalte zwar
   nicht indiziert oder eine Live-Prüfung nicht beauftragt wurde.

## Schutzregeln

- Niemals Secrets, Zugangsdaten, personenbezogene Daten, private Backups oder
  ausgeschlossene Projektordner in Todo, Graph, Dokumentation oder Git übernehmen.
- Vorhandene Änderungen anderer Arbeitsschritte erhalten; kein pauschales
  Zurücksetzen oder Aufräumen.
- Keine Commits, Pushes, Wikiveröffentlichungen, Deployments oder Live-Änderungen
  allein durch diesen Befehl. Dafür ist eine ausdrückliche Nutzeranweisung nötig.
- Bei einem echten Widerspruch, einer rechtlich relevanten Frage oder einer
  sicherheitskritischen offenen Entscheidung die betroffene Arbeit nicht als
  geklärt dokumentieren. Unabhängige, sichere Dokumentation kann fortgesetzt
  werden.

## Rückmeldung

Nenne die geänderten Living-Documentation- und Todo-Dateien, den
Graphify-Status, die tatsächlich ausgeführten Prüfungen und verbleibende offene
Punkte. Trenne lokale Änderungen klar von Commit, Push, Veröffentlichung und
Deployment.
