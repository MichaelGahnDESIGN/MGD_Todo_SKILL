---
name: board
description: Zeigt das Message-Board und Projekt-Dashboard: alle Threads, Phasen, offene Fragen und die letzten Chat-Nachrichten auf einer Seite. Für /board, "Dashboard anzeigen", Überblick über Threads und Fortschritt.
metadata:
  version: 1.1.0
  integration:
    - todo
    - wissen
---

# /board — Message-Board und Dashboard

Eine Seite, auf der du alles im Blick hast: **Phasen**, **Threads** (mit Ampel),
**offene Fragen an dich**, **Hinweise** und die **letzten Chat-Nachrichten**.

## Was ist das Message-Board?

Mehrere KI-Threads arbeiten parallel an einem Projekt. Damit sie nicht aneinander
vorbei arbeiten, schreiben sie in **ein gemeinsames Protokoll** (`THREAD-CHAT/chat.jsonl`,
eine Zeile pro Nachricht). Das ist das Message-Board. Das Dashboard liest dieses
Protokoll und macht eine übersichtliche Seite daraus.

## Befehle

| Befehl | Macht |
|---|---|
| `/board` | Dashboard neu erzeugen und im Browser öffnen |
| `/board neu` | nur neu erzeugen |
| `/board live` | alle 5 Minuten im Hintergrund neu erzeugen (kostet keine Tokens) |
| `/board status` | Status-Datei (Phasen, Fragen, Hinweise) zeigen und mit dem Chat abgleichen |

## So geht es (Schritt für Schritt)

1. Lege den Ordner `THREAD-CHAT/` an. Darin liegt `chat.jsonl` (das Protokoll).
   Jede Zeile ist JSON: `{"zeit":"2026-11-24T01:00:00Z","von":"plattform","an":"koordination","text":"..."}`.
2. Lege daneben `dashboard-status.json` an (Vorlage unten). Die pflegst du oder der Koordinations-Thread.
3. Starte: `python3 skills/board/scripts/board.py`
4. Ergebnis: `THREAD-CHAT/dashboard.html`. Doppelklick, fertig. Die Seite lädt alle 5 Minuten neu.

Andere Orte: `board.py --chat <chat.jsonl> --status <status.json> --out <datei.html>`.

## Vorlage dashboard-status.json

```json
{
  "stand": "24.11.2026",
  "phasen": [{"nr": 1, "name": "Baukasten", "status": "fertig", "info": "Kit 1.12.0"}],
  "threads": {"share": "Pilot fertig, wartet", "plattform": {"text": "baut 1.12.1", "status": "arbeitet"}},
  "fragen": ["Preise und Tarife?"],
  "hinweise": ["Release-Stopp bis 2.1.1"]
}
```

Status-Wörter: `fertig` (grün), `arbeitet` (blau), `wartet` (gelb), `blockiert` (rot), `offen` (grau).
Ohne Angabe rät das Skript aus dem Text ("blockiert", "wartet", "fertig"/"live").

## Interaktiv (ab 1.1.0)

- Phasen, Threads, Fragen und Hinweise lassen sich **aufklappen**. Oben: „Alles aufklappen/zuklappen".
- Jede Frage zeigt, **aus welchem Thread** sie kommt (`von`). Mit „Frage kopieren" kopierst du sie, im Feld schreibst du deine Antwort (bleibt im Browser gespeichert), „Antwort kopieren" erzeugt einen Text zum Einfügen in den Chat. „Alle beantworteten kopieren" sammelt alle.
- Links im Text sind klickbar. Thread-Karten haben „Thread öffnen" (Feld `session`) und zeigen die letzten Nachrichten.
- Felder für Fragen/Hinweise: `{"text":"…","von":"thread","detail":"…","link":"https://…"}` (ein reiner Text geht weiterhin).

## Regeln

- Nur lesen: Das Skript ändert weder Chat noch Status.
- Keine Zugangsdaten, keine Kundendaten in Chat, Status oder Seite.
- Die Seite läuft ohne Internet und ohne Fremdbibliothek.
- Mit `/todo`: offene Fragen und Hinweise gehören auch als Aufgaben in die TODO-Datei.
- Mit `/wissen`: Beim Wissens-Update die Status-Datei mit nachziehen.
