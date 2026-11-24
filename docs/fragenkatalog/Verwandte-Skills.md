# Verwandte MGD-Skills

Der Fragenkatalog-Skill ist Teil einer Familie von vier zusammengehörigen KI-Agenten-Skills für
**Claude Code** und **ChatGPT Codex**, die im selben Projekt oft gemeinsam sinnvoll sind:

1. **MGD_DEV_SKILL** — Release/Sync/Backup/Cleanup/Tests/Wissensdokumentation.
2. **Fragenkatalog-Skill** (dieser Skill) — interaktiver Design-Fragenkatalog mit KI-Antworten aus
   wählbarer Experten-Perspektive, inkl. Rechts-Kategorie.
3. **MGD_Todo_SKILL** — selbst-gehostete `TODO.html` mit Bearbeiten-Funktion und
   Dokument-Verknüpfung.
4. **MGD_Living-Documentation** — lebendige Projektdokumentation (Entscheidungen, offene Punkte,
   Risiken, Testnachweise) als HTML+Markdown.

## Warum diese Kombination

Der Fragenkatalog klärt *was* entschieden werden muss und *was* die KI dazu vorschlägt. Die drei
anderen Skills schließen daran an, sobald aus einer geklärten Frage eine Aufgabe, ein Projektstand
oder ein dokumentierter Punkt wird:

| Skill | Repo | Nutzen im Zusammenspiel mit dem Fragenkatalog |
|---|---|---|
| MGD_DEV_SKILL | [MichaelGahnDESIGN/MGD_DEV_SKILL](https://github.com/MichaelGahnDESIGN/MGD_DEV_SKILL) | Der Fragenkatalog-Stand (Anzahl offener/beantworteter Fragen) wird vor einem Release Teil der Projekt-Wissensdokumentation. |
| MGD_Todo_SKILL | [MichaelGahnDESIGN/MGD_Todo_SKILL](https://github.com/MichaelGahnDESIGN/MGD_Todo_SKILL) | Unbeantwortete Fragen (leeres `userAnswer`) lassen sich als Todos exportieren, um sie gezielt abzuarbeiten. |
| MGD_Living-Documentation | [MichaelGahnDESIGN/MGD_Living-Documentation](https://github.com/MichaelGahnDESIGN/MGD_Living-Documentation) | Unbeantwortete Fragen lassen sich als offene Punkte in die Living Documentation übernehmen. |

## Automatischer Begleit-Skills-Check

`/fragenkatalog-setup` (der Erstinstallations-Assistent, siehe [Befehle](Befehle.md) und
[Setup](Setup.md)) prüft bei der Ersteinrichtung aktiv anhand konkreter Datei-/Ordnerpfade — nicht
nur per Hinweistext —, ob die drei Begleit-Skills bereits im Projekt oder global installiert sind:

- **MGD_DEV_SKILL**: `.claude/commands/dev.md` bzw. `.claude/skills/dev/SKILL.md` (projekt-lokal)
  oder `~/.claude/skills/dev/SKILL.md` (global) — jeweils mit Codex-Pendant unter `.codex/...` bzw.
  `~/.codex/...`.
- **MGD_Todo_SKILL**: `.claude/commands/todo.md` bzw. `PROJEKT/TODO/.todo-config` (projekt-lokal)
  oder `~/.claude/skills/todo/SKILL.md` (global), Codex analog.
- **MGD_Living-Documentation**: `.claude/skills/living-documentation/SKILL.md` (projekt-lokal) oder
  `~/.claude/skills/living-documentation/SKILL.md` (global), Codex analog.

Fehlt einer der drei Skills, fragt der Agent aktiv nach, ob er ihn per `git clone` und Kopieren in
die jeweils dokumentierte Zielstruktur mitinstallieren soll. Ohne Netzzugriff beschreibt er die
Schritte stattdessen nur als Anleitung. Die vollständige Logik inkl. Prüfpfad-Tabelle und
Installationsbefehlen steht in `SKILL.md` (Abschnitt "Begleit-Skills-Check" unter
`/fragenkatalog-setup`). Der Check läuft ausschließlich einmalig beim Erstlauf von
`/fragenkatalog-setup`.

## Weiterführend

- [Home](Home.md) — Einstieg und Konzept-Übersicht
- [Befehle](Befehle.md) — alle Slash-Befehle im Detail
- [Setup](Setup.md) — Installationsanleitung für Claude Code und Codex
