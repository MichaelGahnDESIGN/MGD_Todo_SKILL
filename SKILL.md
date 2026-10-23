---
name: todo
description: Verwalte Projekt-Aufgaben in einer Datei — alle an einem Ort, sortierbar, immer aktuell.
---

# /todo — Deine Aufgabenliste

Alle deine Projekt-Aufgaben in einer Datei, die sich selbst organisiert. Nicht vergessen, nicht doppelt, immer aktuell.

## Erste Schritte

**Erstellen:**
```
/todo
```

Claude fragt: "Wo soll die Datei sein?" Du sagst z.B. `TODO/TODO.html` — fertig.

Die Datei wird angelegt, und du kannst sofort Aufgaben hinzufügen.

## Was du tun kannst

| Befehl | Macht |
|---|---|
| `/todo add "Aufgabe schreiben"` | Neue Aufgabe hinzufügen |
| `/todo done 5` | Aufgabe #5 als fertig markieren |
| `/todo list` | Alle Aufgaben anzeigen |
| `/todo search "Login"` | Aufgaben durchsuchen |
| `/todo category "Bug" "Login funktioniert nicht"` | In Kategorie "Bug" ablegen |

## Beispiel

```
/todo add "Datenbankverbindung prüfen"
→ Aufgabe #1 hinzugefügt

/todo add "Benutzer-Login schreiben"
→ Aufgabe #2 hinzugefügt

/todo add "Tests für Login"
→ Aufgabe #3 hinzugefügt

Nach einer Stunde:
/todo done 1
→ Aufgabe #1 ✓ fertig

/todo list
→ 2 offen, 1 fertig
   [ ] #2 Benutzer-Login schreiben
   [ ] #3 Tests für Login
   [✓] #1 Datenbankverbindung prüfen
```

## Kategorien

Ordne Aufgaben nach Typ:

- **Feature** — neue Funktion
- **Bug** — Fehler
- **Doku** — Dokumentation
- Eigene Kategorien? Kein Problem

```
/todo category "Bug" "Startseite lädt langsam"
```

## Häufig gefragt

**F: Wo landen die Aufgaben?**  
A: In einer HTML-Datei, die du einmal festlegst. Lokal, nicht in der Cloud.

**F: Kann ich die bearbeiten ohne `/todo`?**  
A: Ja. Die Datei ist normales HTML. Aber `/todo` ist schneller.

**F: Was passiert mit erledigten Aufgaben?**  
A: Sie bleiben in der Liste, sind aber markiert. Du kannst sie ausblenden oder löschen.

## Antwort- und Dokumentations-Stil (verbindlich)

- **Einfach schreiben:** so verständlich wie möglich, kurze Sätze, keine unerklärten Fachwörter.
- **Marker benutzen:**
  - ❓ Frage an den Nutzer
  - ⚠️ wichtiger Hinweis
  - ✅ erledigt
  - ☑️ noch offen
  - weitere erlaubt: 🔎 geprüft, 🚫 geht nicht, ➕ neu
- **READMEs und Wikis für den DAU** (dümmster anzunehmender User) schreiben: Schritt für Schritt, mit Beispiel, ohne Abkürzungen ohne Erklärung.
- Diese Regeln gelten für alle Texte, die der Skill erzeugt (Doku, TODO, Berichte, Übergaben).
