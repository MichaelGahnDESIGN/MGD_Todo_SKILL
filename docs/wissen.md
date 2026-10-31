# `/wissen` – Aufgaben, Karte und Erklärung zusammenhalten

`/wissen` ist der kurze Abschluss nach einem Arbeitsblock. Er sorgt dafür,
dass eine erledigte Aufgabe nicht als offen stehen bleibt und dass eine wichtige
Entscheidung dort erklärt ist, wo später Menschen und Agenten sie finden.

## Die drei Orte

| Ort | Einfache Frage |
| --- | --- |
| TODO | Was ist der nächste konkrete Schritt? |
| Graphify | Welche Dateien und Bereiche hängen zusammen? |
| Living Documentation | Was gilt, warum und wodurch ist es belegt? |

Das sind keine drei Kopien derselben Liste. Jeder Ort hat eine andere Aufgabe.

## So verwendest du den Skill

```text
/wissen
```

Der Agent liest zuerst Regeln, Git-Stand und die bestehende Dokumentation.
Danach aktualisiert er nur die tatsächlich betroffenen Punkte. Ist Graphify im
Projekt eingerichtet, wird die Karte inkrementell aktualisiert; andernfalls
bleibt das als offener, sichtbarer Hinweis stehen. Anschließend werden Diff und
Links geprüft.

## Wichtige Grenzen

- `/wissen` veröffentlicht, deployt und löscht nichts automatisch.
- Ein lokaler Test, ein Commit, ein Push und ein Live-Stand sind getrennte
  Nachweise.
- Passwörter, Tokens, personenbezogene Daten, Backups und private
  Infrastrukturdetails gehören niemals in diese Dateien.

Die vollständige Arbeitsanweisung liegt in
[`skills/wissen/SKILL.md`](../skills/wissen/SKILL.md). Der gleiche Skill wird
auch in [MGD Living Documentation](https://github.com/MichaelGahnDESIGN/MGD_Living-Documentation)
gepflegt, damit Aufgaben und dauerhafte Projektklärung dieselbe Sprache nutzen.

## Dokumentation ansehen

```text
/wissen-ansehen
```

Der Befehl öffnet die **vorhandene Dokumentation des aktuellen Projekts**.
Er bevorzugt einen dokumentierten HTML-Einstieg und bietet vorhandene
Markdown-Dokumentation als Rückfall an. Es werden keine Inhalte geändert,
keine Builds gestartet und keine Daten veröffentlicht. Wenn noch keine
Dokumentation existiert, meldet der Agent das und nennt `/wissen` als
möglichen nächsten Schritt. Er erstellt nichts automatisch.

### Installieren

Den Ordner `skills/wissen-ansehen` vollständig in das Skill-Verzeichnis
deines Werkzeugs kopieren, zum Beispiel nach
`~/.codex/skills/wissen-ansehen/` oder `~/.claude/skills/wissen-ansehen/`.
Für projektlokale Nutzung entsprechend `.agents/skills/` beziehungsweise
`.claude/skills/` verwenden. Die jeweilige Befehlsdatei
`.codex/commands/wissen-ansehen.md` oder `.claude/commands/wissen-ansehen.md`
kann zusätzlich in das entsprechende Befehlsverzeichnis kopiert werden.
Ein Wrapper allein ersetzt nicht den installierten Skill. Falls die neue
Auswahl noch nicht erscheint, die Skill-Liste neu laden oder eine neue
Sitzung öffnen.

Der nur lesende Suchhelfer benötigt Python 3.9 oder neuer. Fehlt Python,
prüft der Agent die vorhandenen Dokumentationspfade direkt; es wird nichts
installiert. Der Skill liegt unter
[`skills/wissen-ansehen/SKILL.md`](../skills/wissen-ansehen/SKILL.md).
