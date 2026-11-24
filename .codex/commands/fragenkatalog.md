# fragenkatalog (ChatGPT Codex Command)

Codex-Pendant zum Claude-Code-Slash-Command `/fragenkatalog`. Nutzt dieselbe kanonische
Spezifikation aus `skills/fragenkatalog/SKILL.md`.

## Aufruf-Konvention

Da Codex keine native Slash-Command-Argument-Syntax wie Claude Code hat, wird der Unterbefehl als
erstes Wort im Prompt erwartet:

```
fragenkatalog setup
fragenkatalog generate 50
fragenkatalog add-category "Monetarisierung"
fragenkatalog add-question "UI/UX" "Wie sieht das Onboarding für Erstnutzer aus?"
fragenkatalog answer 17
fragenkatalog export
fragenkatalog import pfad/zu/alte-liste.json
fragenkatalog stats
fragenkatalog pfad docs/Fragenkatalog.html
fragenkatalog perspektive "Naughty Dog Narrative Director"
```

## Ablauf für den Agenten

1. **Immer zuerst** `SKILL.md` im Skill-Root vollständig lesen — das ist die einzige Quelle der
   Wahrheit für Verhalten, Datenmodell und HTML-Struktur. Diese Datei hier ist nur ein dünner
   Einstiegspunkt und dupliziert keine Logik.
2. Ermittele den Unterbefehl aus dem ersten Wort des Prompts. Ohne erkennbaren Unterbefehl oder
   falls `.fragenkatalog-config` im Projekt-Root fehlt: `setup`-Ablauf starten.
3. Führe exakt den in `SKILL.md` beschriebenen Abschnitt `/fragenkatalog-<unterbefehl>` aus.
4. Arbeite mit denselben Dateien wie die Claude-Code-Variante:
   - `.fragenkatalog-config` (Projektkonfiguration, JSON)
   - `fragenkatalog.json` (kanonisches Fragen-Datenmodell)
   - `templates/Fragenkatalog.template.html` (Basis für den Export)
   - Ziel-HTML unter dem in `.fragenkatalog-config` hinterlegten `outputPath`
5. Codex hat typischerweise keinen direkten Browser-Zugriff — beim Export reicht es, die Datei zu
   schreiben und dem Nutzer den Pfad zu nennen; er öffnet sie selbst lokal.
6. Antworten in der konfigurierten Sprache (Default Deutsch), kurze Bestätigung nach jeder
   Aktion.

## Kompatibilitätshinweis

Beide Umgebungen (Claude Code über `.claude/commands/fragenkatalog.md` und Codex über diese
Datei) greifen auf **dieselbe** `SKILL.md` und dasselbe Template zurück. Änderungen an der
Kernlogik gehören ausschließlich in `SKILL.md` bzw. `templates/Fragenkatalog.template.html` —
nicht in diese Wrapper-Dateien, damit beide Umgebungen synchron bleiben.
