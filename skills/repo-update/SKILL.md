---
name: repo-update
description: GitHub-Repo aktualisieren: README, Wiki, Skill-Empfehlungen, neue Release-Version, bei Bedarf Paket. Für /repo-update.
metadata:
  version: 1.0.0
---

# /repo-update

Bringt ein Repo vollständig auf GitHub auf den neuesten Stand. Alias: `/github-update`.

## Ablauf
1. **Prüfen:** `python3 skills/repo-update/scripts/repo_check.py .` (README, LICENSE, Impressum, Lizenz/Impressum am Ende, Links, CHANGELOG).
2. **Empfehlungen:** `python3 skills/repo-update/scripts/related.py . --write` setzt „Skill-Empfehlungen" und „Verwandte MGD Projekte" ein (Liste: `family.json`).
3. **README und Wiki:** verständlich für Einsteiger, Lizenz und Impressum **ganz am Ende**. Wiki-Seiten aus `wiki/` ins GitHub-Wiki (`<repo>.wiki.git`) übertragen.
4. **Version:** `CHANGELOG.md` oben um neue Version ergänzen (`## X.Y.Z — Datum`).
5. **Release:** `python3 skills/repo-update/scripts/release.py` zeigt den Plan. Mit `--push` wird getaggt und das GitHub-Release erstellt. Mit `--package` hängt ein ZIP dran. Bei Bedarf (Plugin, Tool zum Herunterladen) Paket mitliefern.
6. Bericht mit Link zum Release.

Regeln: Tags und Releases werden nie gelöscht oder überschrieben. Vor `--push` Zustimmung einholen, wenn der Nutzer nicht schon „veröffentlichen" gesagt hat. Keine Zugangsdaten in Repo, README oder Release.
