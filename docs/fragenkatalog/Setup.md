# Setup

## Claude Code

1. Repo klonen oder als Referenz herunterladen:

   ```bash
   git clone https://github.com/MichaelGahnDESIGN/Fragenkatalog-Skill.git
   ```

2. Im Zielprojekt die Skill-Dateien ablegen:

   ```bash
   mkdir -p <projekt>/.claude/skills/fragenkatalog
   cp Fragenkatalog-Skill/SKILL.md <projekt>/.claude/skills/fragenkatalog/SKILL.md
   cp -r Fragenkatalog-Skill/templates <projekt>/.claude/skills/fragenkatalog/templates

   mkdir -p <projekt>/.claude/commands
   cp Fragenkatalog-Skill/.claude/commands/fragenkatalog.md <projekt>/.claude/commands/fragenkatalog.md
   ```

3. In Claude Code im Zielprojekt:

   ```
   /fragenkatalog setup
   ```

4. Claude Code liest daraufhin `SKILL.md` und führt den interaktiven Ersteinrichtungs-Assistenten
   aus (Projektname/-typ, Plattform, Experten-Perspektive, Speicherpfad, Sprache, Rechts-
   Kategorie).

## ChatGPT Codex

1. Repo klonen (siehe oben).
2. Im Zielprojekt:

   ```bash
   mkdir -p <projekt>/.codex/skills/fragenkatalog
   cp Fragenkatalog-Skill/SKILL.md <projekt>/.codex/skills/fragenkatalog/SKILL.md
   cp -r Fragenkatalog-Skill/templates <projekt>/.codex/skills/fragenkatalog/templates

   mkdir -p <projekt>/.codex/commands
   cp Fragenkatalog-Skill/.codex/commands/fragenkatalog.md <projekt>/.codex/commands/fragenkatalog.md
   ```

3. Im Codex-Prompt:

   ```
   fragenkatalog setup
   ```

   Codex hat keine native Slash-Command-Argumentsyntax — der Unterbefehl wird als erstes Wort im
   Prompt übergeben (siehe `.codex/commands/fragenkatalog.md`).

## Beide Umgebungen parallel nutzen

Da beide Wrapper (`​.claude/commands/fragenkatalog.md` und `.codex/commands/fragenkatalog.md`) auf
dieselbe `SKILL.md` verweisen, lässt sich ein Projekt problemlos mit beiden Tools bearbeiten — die
Daten (`.fragenkatalog-config`, `fragenkatalog.json`, die exportierte HTML) sind toolagnostisch
und liegen als normale Dateien im Projekt-Repo.

## Verzeichnisstruktur nach Installation

```
<projekt>/
├── .claude/
│   ├── commands/fragenkatalog.md
│   └── skills/fragenkatalog/
│       ├── SKILL.md
│       └── templates/Fragenkatalog.template.html
├── .codex/
│   ├── commands/fragenkatalog.md
│   └── skills/fragenkatalog/
│       ├── SKILL.md
│       └── templates/Fragenkatalog.template.html
├── .fragenkatalog-config     ← nach /fragenkatalog setup
├── fragenkatalog.json        ← nach /fragenkatalog setup
└── docs/Fragenkatalog.html   ← nach /fragenkatalog export
```
