# Fragenkatalog-Skill — Wiki

Willkommen im Wiki des Fragenkatalog-Skills. Dieser Skill erzeugt für ein beliebiges Projekt
(Spiel, App, Website, Buch, Business-Plan, ...) eine durchsuchbare, kategorisierte Sammlung aller
wichtigen Design- und Konzeptfragen — inklusive sofortiger KI-Antwort aus einer frei wählbaren
Experten-Perspektive und einem eigenen Feld für die endgültige Entscheidung des Projektinhabers.

## Konzept in 3 Sätzen

1. **Frage** (rot) — was geklärt werden muss.
2. **KI-Antwort** (blau, `💙`) — ein fundierter Vorschlag aus einer frei wählbaren Experten-
   Perspektive, sofort bei Erstellung der Frage generiert.
3. **Eigene Antwort** (normal) — die tatsächliche, endgültige Entscheidung des Projektinhabers,
   anfangs leer.

Eine Sonderrolle nimmt die Kategorie **"Recht"** ein: dort antwortet die KI nicht aus einer
Kreativ-Persona, sondern mit eigenem Präfix (`⚖️`) und einem Pflicht-Disclaimer — siehe
[Rechtliche Fragen](Rechtliche-Fragen.md).

## Schnellreferenz

```
/fragenkatalog setup                       # einmalig: Projekt, Perspektive, Pfad konfigurieren
/fragenkatalog generate 50                 # initiale Fragenliste erzeugen
/fragenkatalog add-category "Monetarisierung"
/fragenkatalog add-question "UI/UX" "Wie sieht das Onboarding aus?"
/fragenkatalog answer 17                   # Frage #17 (neu) beantworten
/fragenkatalog export                      # finale HTML schreiben/aktualisieren
/fragenkatalog import alte-liste.json      # bestehende Liste übernehmen
/fragenkatalog stats                       # Fortschritt anzeigen
/fragenkatalog pfad docs/Fragenkatalog.html
/fragenkatalog perspektive "Naughty Dog Narrative Director"
```

## Weiterführende Seiten

- [Befehle](Befehle.md) — jeder Befehl im Detail mit Beispielen
- [HTML-Format](HTML-Format.md) — technische Struktur der erzeugten Datei
- [Experten-Perspektiven](Experten-Perspektiven.md) — wie man gute Perspektiven formuliert
- [Rechtliche Fragen](Rechtliche-Fragen.md) — Disclaimer-Konzept und Beispiele
- [Setup](Setup.md) — Installationsanleitung Claude Code & Codex
- [Beispielprojekt](Beispielprojekt.md) — durchgespieltes Mini-Beispiel "Sternenfänger"
- [Verwandte MGD-Skills](Verwandte-Skills.md) — MGD_DEV_SKILL, MGD_Todo_SKILL und
  MGD_Living-Documentation als Begleit-Skills, inkl. automatischem Installations-Check bei
  `/fragenkatalog-setup`

Die verbindliche technische Spezifikation ist immer `SKILL.md` im Repo-Root — die Wiki-Seiten
erklären und illustrieren, ersetzen sie aber nicht.
