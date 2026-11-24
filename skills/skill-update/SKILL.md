---
name: skill-update
description: Alle lokalen MGD-Skills mit der neuesten GitHub-Version vergleichen und aktualisieren. Für /skill-update.
metadata:
  version: 1.0.0
---

# /skill-update

Prüft `~/.claude/skills` und `~/.codex/skills` gegen GitHub.

## Ablauf
1. Prüfen (nur lesen): `python3 skills/skill-update/scripts/skill_update.py`
   - ✅ aktuell, ☑️ Update verfügbar, ⚠️ lokale Anpassung oder GitHub nicht erreichbar.
2. Dem Nutzer zeigen, was sich ändert. Bei lokalen Anpassungen **fragen**.
3. Aktualisieren: `... skill_update.py --apply`. Vorher sichert das Skript jede Kopie nach `.backup-skill-update/<zeit>/`.
4. Ordner mit lokaler Anpassung (`INSTALLATION.json` mit `local_overlay`) nur mit `--force` und nach Zustimmung.

Welche Skills gehören dazu? Die Liste steht in `skills/repo-update/family.json` (Feld `lokal`).
