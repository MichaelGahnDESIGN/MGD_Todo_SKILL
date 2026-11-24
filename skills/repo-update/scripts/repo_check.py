#!/usr/bin/env python3
# Prüft ein Repo: README-Pflichtteile, Lizenz/Impressum am Ende, Links auf lokale Dateien
# Aufruf: python3 repo_check.py <repo-ordner>     Ausgabe: ✅/⚠️ je Punkt, Exit 1 bei Fehlern
import os, re, sys

d = sys.argv[1] if len(sys.argv) > 1 else '.'
bad = 0


def say(ok, msg):
    global bad
    print(('✅ ' if ok else '⚠️ ') + msg)
    bad += 0 if ok else 1


p = os.path.join(d, 'README.md')
if not os.path.exists(p):
    say(False, 'README.md fehlt'); sys.exit(1)
t = open(p, encoding='utf-8').read()
say(os.path.exists(os.path.join(d, 'LICENSE')), 'LICENSE vorhanden')
say(os.path.exists(os.path.join(d, 'IMPRESSUM.md')) or 'Impressum' in t, 'Impressum vorhanden')
say('MGD-RELATED:START' in t, 'Skill-Empfehlungen + Verwandte MGD Projekte')
heads = [m.group(0) for m in re.finditer(r'^## .*$', t, flags=re.M)]
tail = [h for h in heads[-3:]]
say(any('Lizenz' in h or 'License' in h for h in tail) and any('Impressum' in h for h in tail), 'Lizenz und Impressum am Ende')
miss = []
for m in re.finditer(r'\]\((?!https?:|#|mailto:)([^)\s#]+)', t):
    if not os.path.exists(os.path.join(d, m.group(1))):
        miss.append(m.group(1))
say(not miss, 'Lokale Links ok' + (': fehlt ' + ', '.join(sorted(set(miss))[:6]) if miss else ''))
say(os.path.exists(os.path.join(d, 'CHANGELOG.md')), 'CHANGELOG.md vorhanden')
sys.exit(1 if bad else 0)
