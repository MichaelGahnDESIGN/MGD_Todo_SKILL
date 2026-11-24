---
name: todo-update
description: TODO-Datei aktualisieren: Erledigtes schließen, Neues aus Board und Doku eintragen. Für /todo-update.
metadata:
  version: 1.0.0
---

# /todo-update

Bringt die `TODO.html` auf den aktuellen Stand, ohne etwas zu löschen.

## Ablauf
1. Offene Fragen und Hinweise aus `dashboard-status.json` als Aufgaben vorschlagen (nicht doppelt).
2. Nachweislich Erledigtes mit `/todo done` schließen (Beleg: Commit, Test, Release).
3. Links zur Living Documentation mit `/todo-link` prüfen.
4. Bericht: neu, geschlossen, offen.

Regeln: nie löschen, nur `done` setzen; keine Secrets in Einträgen.
