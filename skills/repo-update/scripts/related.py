#!/usr/bin/env python3
# Skill-Empfehlungen + "Verwandte MGD Projekte" in README einsetzen/aktualisieren
# Aufruf: python3 related.py <repo-ordner> [--repo NAME] [--write]   (ohne --write nur Vorschau)
import argparse, json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
S, E = '<!-- MGD-RELATED:START -->', '<!-- MGD-RELATED:END -->'


def build(fam, me):
    by = {r['repo']: r for r in fam['repos']}
    url = fam['url']
    line = lambda r: f"| [{r['repo']}]({url}{r['repo']}) | `{r['befehl']}` | {r['kurz']} |"
    out = [S, '## Skill-Empfehlungen', '']
    rec = [by[x] for x in by.get(me, {}).get('empfiehlt', []) if x in by and x != me]
    if rec:
        out += ['Passt gut dazu:', '', '| Skill | Befehl | Wofür |', '|---|---|---|'] + [line(r) for r in rec] + ['']
    out += ['## Verwandte MGD Projekte', '', '<details><summary>Alle MGD-Skills und Werkzeuge anzeigen</summary>', '', '| Projekt | Befehl | Wofür |', '|---|---|---|']
    out += [line(r) for r in fam['repos'] if r['repo'] != me]
    out += ['', '</details>', '', 'Mit `/skill-update` (im Todo-Skill) holst du alle lokal installierten MGD-Skills auf den neuesten Stand.', E]
    return '\n'.join(out) + '\n'


def apply(text, block):
    text = re.sub(re.escape(S) + r'.*?' + re.escape(E) + r'\n?', '', text, flags=re.S)
    # alte Abschnitte entfernen (bis zur nächsten ##-Überschrift)
    for h in ('Verwandte MGD Projekte', 'Skill-Empfehlungen', 'Skill-Empfehlung'):
        text = re.sub(r'^## ' + h + r'[^\n]*\n.*?(?=^## |^<!-- MGD-LEGAL|\Z)', '', text, flags=re.S | re.M)
    m = re.search(r'^(---\s*\n+)?(## Lizenz|<!-- MGD-LEGAL|## Impressum|## License)', text, flags=re.M)
    if m:
        i = m.start()
        return text[:i].rstrip('\n') + '\n\n' + block + '\n' + text[i:]
    return text.rstrip('\n') + '\n\n' + block


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('folder')
    ap.add_argument('--repo')
    ap.add_argument('--write', action='store_true')
    a = ap.parse_args()
    fam = json.load(open(os.path.join(HERE, '..', 'family.json'), encoding='utf-8'))
    me = a.repo or os.path.basename(os.path.abspath(a.folder))
    p = os.path.join(a.folder, 'README.md')
    old = open(p, encoding='utf-8').read()
    new = apply(old, build(fam, me))
    print(('geändert' if new != old else 'unverändert'), me)
    if a.write and new != old:
        open(p, 'w', encoding='utf-8').write(new)


if __name__ == '__main__':
    main()
