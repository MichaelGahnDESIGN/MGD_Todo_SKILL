# Beispielprojekt: "Sternenfänger"

Fiktives Mini-Beispiel: ein kleines Mobile-Sammelspiel namens **Sternenfänger** (iOS/Android),
Perspektive: **💙 Blizzard Entertainment Lead Game Designer**. Zeigt, wie ein fertiger,
kompakter Katalog aussehen kann (Auszug, 15 von z. B. 50 generierten Fragen).

## `.fragenkatalog-config` (Auszug)

```json
{
  "projectName": "Sternenfänger",
  "projectType": "Mobile Game",
  "platforms": ["iOS", "Android"],
  "perspective": "Blizzard Entertainment Lead Game Designer",
  "perspectivePrefix": "💙",
  "outputPath": "docs/Fragenkatalog.html",
  "dataPath": "docs/fragenkatalog.json",
  "language": "de",
  "includeLegalCategory": true,
  "createdAt": "2026-09-23"
}
```

## Kern-Loop

**Frage:** Was ist die zentrale Spielhandlung, die der Spieler alle 30–60 Sekunden wiederholt?
**💙 Antwort:** Der Spieler fängt fallende Sterne mit einer Wisch-Geste, kombiniert gleichfarbige
Sterne zu stärkeren Formen und sammelt so Energie für die nächste Levelrunde. Der Loop sollte in
unter 5 Sekunden verständlich sein und pro Session mehrere kleine Belohnungsmomente liefern.

**Frage:** Wie wird Frustration bei knapp verpassten Kombos vermieden?
**💙 Antwort:** Ein kurzes Toleranzfenster (Coyote-Time von ca. 150–200 ms) nach der Wisch-Geste
sowie ein visuelles "Fast geschafft"-Feedback reduzieren das Gefühl von Unfairness, ohne die
Mechanik zu verwässern.

## Progression

**Frage:** Wie schaltet der Spieler neue Stern-Typen frei?
**💙 Antwort:** Über ein Level-basiertes Freischaltsystem kombiniert mit seltenen Drops aus
täglichen Herausforderungen — das erzeugt sowohl verlässlichen als auch überraschenden
Fortschritt.

**Frage:** Wie wird verhindert, dass sich das Spiel nach Stunde 3 leer anfühlt?
**💙 Antwort:** Ein zweites, langsameres Progressionssystem (z. B. Sternbild-Sammlung mit
saisonalen Zielen) hält auch erfahrene Spieler bei der Stange, ohne den Kern-Loop zu verändern.

## Wirtschaft/Balance

**Frage:** Soll es eine Premium-Währung geben, und wofür?
**💙 Antwort:** Ja, primär für kosmetische Sternenspuren und Zeitersparnis (Energie-Auffüllung) —
nie für spielentscheidende Stärke, um Pay-to-Win-Kritik zu vermeiden.

## UI/UX/HUD

**Frage:** Wie viele HUD-Elemente sind während des Kern-Loops gleichzeitig sichtbar?
**💙 Antwort:** Maximal 3 (Punktzahl, Energie-Leiste, aktueller Combo-Multiplikator) — alles
Weitere gehört in Zwischenbildschirme, um die Spielfläche auf kleinen Mobile-Screens frei zu
halten.

## Recht

**Frage:** Welche Altersfreigabe ist für Sternenfänger in der EU zu erwarten?
**⚖️ Antwort:** Ohne Gewaltdarstellung und ohne Zufallskäufe mit Sekundärmarktwert ist eine
niedrige PEGI-Einstufung (PEGI 3–7) realistisch; sobald Lootbox-ähnliche Mechaniken mit Echtgeld
eingeführt werden, kann sich das ändern und zusätzliche Hinweispflichten auslösen. Dies ist keine
Rechtsberatung, sondern eine allgemeine Orientierung zur Recherche. Für verbindliche Aussagen
einen Anwalt/Fachberater für Jugendschutzrecht, EU konsultieren.

**Frage:** Welche DSGVO-Pflichten entstehen durch ein optionales Nutzerkonto mit Highscore-Liste?
**⚖️ Antwort:** In der Regel eine Datenschutzerklärung mit Angaben zu Zweck, Speicherdauer und
Empfängern (z. B. Backend-Hoster), eine Rechtsgrundlage für die Verarbeitung sowie ggf. ein
Auftragsverarbeitungsvertrag mit dem Backend-Anbieter. Dies ist keine Rechtsberatung, sondern
eine allgemeine Orientierung zur Recherche. Für verbindliche Aussagen einen Anwalt/Fachberater
für Datenschutzrecht konsultieren.

**Frage:** Muss der Spieltitel "Sternenfänger" vor Veröffentlichung geprüft werden?
**⚖️ Antwort:** Eine einfache Vorabrecherche in Markenregistern (DPMA für Deutschland, EUIPO für
die EU) sowie eine Store-Namenssuche auf App Store/Google Play wird empfohlen, um
Verwechslungsgefahr oder Namenskollisionen frühzeitig auszuschließen. Dies ist keine
Rechtsberatung, sondern eine allgemeine Orientierung zur Recherche. Für verbindliche Aussagen
einen Anwalt/Fachberater für Markenrecht konsultieren.

## `userAnswer`-Feld

Alle `userAnswer`-Felder bleiben nach der Generierung leer — der Projektinhaber trägt seine
tatsächliche Entscheidung direkt in der exportierten HTML (Edit-Modus) oder über
`/fragenkatalog-answer` im Chat ein. `/fragenkatalog-stats` zeigt danach z. B.:

```
📊 Fragenkatalog-Statistik
   Gesamt: 15 Fragen in 5 Kategorien
   Eigene Antworten vorhanden: 0 (0 %)
   Noch offen: 15
```

Nach einer ersten Bearbeitungsrunde könnte derselbe Stand z. B. so aussehen:

```
📊 Fragenkatalog-Statistik
   Gesamt: 15 Fragen in 5 Kategorien
   Eigene Antworten vorhanden: 9 (60 %)
   Noch offen: 6
```
