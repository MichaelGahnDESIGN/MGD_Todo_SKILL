---
name: related-update
description: Skill-Empfehlungen und Verwandte MGD Projekte in allen MGD-Repos aktualisieren. Für /related-update.
metadata:
  version: 1.0.0
---

# /related-update

Hält den Block „Skill-Empfehlungen" und „Verwandte MGD Projekte" in allen öffentlichen MGD-Skill-Repos gleich.

## Ablauf
1. Liste aus `skills/repo-update/family.json` lesen.
2. Je Repo klonen, `related.py <ordner> --write`, bei Änderung committen (`docs: Skill-Empfehlungen aktualisiert`) und pushen.
3. Bericht: geändert / unverändert / Fehler.

Nur öffentliche Repos. Private Repos nie anfassen. Neue Skills zuerst in `family.json` eintragen.
