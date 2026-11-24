# /board — Message-Board und Dashboard (einfach erklärt)

**Kurz:** `/board` zeigt dir auf einer Seite, was alle deine KI-Threads gerade machen.

## Wofür?
Wenn mehrere KI-Threads gleichzeitig arbeiten, schreiben sie in **ein gemeinsames Protokoll** (das Message-Board). Du musst nicht in jedem Thread nachfragen. Das Dashboard macht aus dem Protokoll eine Übersicht mit Ampeln.

## Schritt für Schritt
1. Ordner `THREAD-CHAT/` anlegen. Darin die Datei `chat.jsonl` (eine Zeile = eine Nachricht).
2. Daneben `dashboard-status.json` (Vorlage steht in `skills/board/SKILL.md`).
3. `/board` eingeben. Die Seite `THREAD-CHAT/dashboard.html` entsteht und öffnet sich im Browser.
4. Für automatisches Aktualisieren alle 5 Minuten: `/board live`. Das kostet keine Tokens.

## Was du siehst
- **Kacheln:** wie viele Threads fertig, am Arbeiten, wartend oder blockiert sind.
- **Phasen:** der große Plan mit Fortschrittsbalken.
- **Threads:** eine Karte pro Thread mit Ampel und letzter Meldung. Mit Suchfeld.
- **Offene Fragen an dich** (❓) und **wichtige Hinweise** (⚠️).
- **Letzte Nachrichten:** anklicken zum Aufklappen.

## Sicherheit
Das Skript liest nur. Keine Zugangsdaten in Chat oder Status schreiben. Die Seite braucht kein Internet.

## Zusammenspiel
- `/todo`: offene Fragen als Aufgaben festhalten.
- `/wissen`: beim Wissens-Update die Status-Datei mit nachziehen.
