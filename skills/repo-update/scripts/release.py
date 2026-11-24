#!/usr/bin/env python3
# Neue Release-Version veröffentlichen: Version aus CHANGELOG.md, Tag, GitHub-Release, ZIP-Paket
# Aufruf: python3 release.py [--version X.Y.Z] [--package] [--push]   (ohne --push nur Plan zeigen)
# Voraussetzung: sauberer Git-Stand auf main, gh angemeldet. Löscht nie Tags oder Releases.
import argparse, re, subprocess, sys


def sh(*c, check=True):
    r = subprocess.run(c, capture_output=True, text=True)
    if check and r.returncode:
        sys.exit(f"Fehler bei {' '.join(c)}: {r.stderr.strip()}")
    return r.stdout.strip()


ap = argparse.ArgumentParser()
ap.add_argument('--version')
ap.add_argument('--package', action='store_true', help='ZIP aus git archive anhängen')
ap.add_argument('--push', action='store_true')
a = ap.parse_args()

log = open('CHANGELOG.md', encoding='utf-8').read()
m = re.search(r'^## \[?v?(\d+\.\d+\.\d+)\]?[^\n]*\n(.*?)(?=^## |\Z)', log, flags=re.S | re.M)
if not m:
    sys.exit('Keine Version im CHANGELOG.md gefunden (Format: "## 1.2.3 — Datum")')
ver = a.version or m.group(1)
notes = m.group(2).strip() or f'Version {ver}'
tag = 'v' + ver
if sh('git', 'status', '--porcelain'):
    sys.exit('Arbeitsordner nicht sauber: erst committen.')
if sh('git', 'tag', '--list', tag):
    sys.exit(f'Tag {tag} gibt es schon. Version im CHANGELOG erhöhen.')
print(f'Plan: Tag {tag}, Release-Notizen {len(notes)} Zeichen, Paket: {"ja" if a.package else "nein"}')
if not a.push:
    print('Vorschau. Mit --push ausführen.'); sys.exit(0)
sh('git', 'push', 'origin', 'HEAD')
sh('git', 'tag', '-a', tag, '-m', f'Version {ver}')
sh('git', 'push', 'origin', tag)
cmd = ['gh', 'release', 'create', tag, '--title', f'{tag}', '--notes', notes]
if a.package:
    name = re.sub(r'[^A-Za-z0-9._-]', '-', sh('git', 'rev-parse', '--show-toplevel').split('/')[-1]) + f'-{ver}.zip'
    sh('git', 'archive', '--format=zip', '-o', f'/tmp/{name}', tag)
    cmd.append(f'/tmp/{name}')
print(sh(*cmd))
