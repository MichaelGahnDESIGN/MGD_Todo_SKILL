---
name: mgd-update
description: Alles aktualisieren, in beide Richtungen: lokale Skills von GitHub holen, Projektstand und Repos nach GitHub bringen. Für /MGD-update.
metadata:
  version: 1.0.0
---

# /MGD-update

Gesamtlauf für den MGD-Werkzeugkasten.

## Richtung 1: GitHub → lokal
1. `/skill-update` (Prüfung, dann mit Zustimmung `--apply`).

## Richtung 2: lokal → GitHub
2. `/wissen-update` (Wissen, Graph, Living Documentation, Dashboard).
3. `/todo-update`.
4. `/related-update` und `/repo-update` für Repos mit Änderungen. Release nur nach Zustimmung.

## Ende
5. Kurzbericht: ✅ erledigt, ☑️ offen, ⚠️ braucht Entscheidung, ❓ Fragen.

Nichts wird gelöscht. Lokale Anpassungen und private Repos bleiben tabu, Zugangsdaten nie anfassen.
