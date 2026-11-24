---
name: messageboard-update
description: Message-Board abgleichen: neue Meldungen lesen, Status-Datei nachziehen, Dashboard erneuern. Für /messageboard-update.
metadata:
  version: 1.0.0
---

# /messageboard-update

Hält Chat-Protokoll, Status-Datei und Dashboard in Übereinstimmung.

## Ablauf
1. Neue Nachrichten lesen (`chat.py neu <name>` oder `THREAD-CHAT/chat.jsonl`).
2. `dashboard-status.json` nur mit **belegten** Aussagen aus dem Chat anpassen: Thread-Stand, Phasen, offene Fragen, Hinweise.
3. Dashboard neu erzeugen (`/dashboard-update`).
4. Kurzer Bericht mit ✅ erledigt, ❓ Fragen an Michael, ⚠️ Wichtiges, ☑️ offen.

Regeln: nichts erfinden, keine Zugangsdaten übernehmen, kein Thread-Status ohne Chat-Beleg ändern.
Optional: mit `--abfrage` zuerst allen Threads eine Statusfrage in den Chat schreiben.
