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
