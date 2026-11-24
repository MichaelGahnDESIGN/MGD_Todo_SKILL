---
name: dashboard-update
description: Dashboard (Message-Board) neu erzeugen und öffnen. Für /dashboard-update.
metadata:
  version: 1.0.0
---

# /dashboard-update

Erzeugt das Dashboard neu und öffnet es. Kurzform von `/board neu` plus Öffnen.

## Ablauf
1. `python3 skills/board/scripts/board.py` ausführen (Ordner `THREAD-CHAT/` wird gesucht).
2. Ergebnis `THREAD-CHAT/dashboard.html` im Standardbrowser öffnen.
3. Eine Zeile Bericht: Anzahl Threads, offene Fragen, neue Nachrichten seit dem letzten Mal.

Nur lesen. Keine Zugangsdaten anzeigen.
