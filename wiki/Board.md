# Message-Board und Dashboard

**Idee:** Viele KI-Threads arbeiten gleichzeitig. Sie schreiben in ein gemeinsames Protokoll (`THREAD-CHAT/chat.jsonl`). Das ist das **Message-Board**.

Das **Dashboard** (`dashboard.html`) zeigt daraus: Phasen mit Fortschrittsbalken, Thread-Ampeln (fertig, arbeitet, wartet, blockiert), offene Fragen an dich und die letzten Nachrichten.

**Starten:** `/board`. **Automatisch alle 5 Minuten:** `/board live` (kostet keine Tokens).

Mehr: [docs/board.md](https://github.com/MichaelGahnDESIGN/MGD_Todo_SKILL/blob/main/docs/board.md)
