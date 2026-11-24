#!/usr/bin/env python3
# Lokale Skills mit der neuesten GitHub-Version vergleichen und (mit --apply) aktualisieren
# Aufruf: python3 skill_update.py [--apply] [--force] [--dir ~/.claude/skills]
# Vorher wird jede Skill-Kopie nach <dir>/.backup-skill-update/<zeit>/ gesichert. Nur lesen ohne --apply.
import argparse, datetime, hashlib, json, os, shutil, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
FAM = os.path.join(HERE, '..', '..', 'repo-update', 'family.json')


def sha(p):
    return hashlib.sha256(open(p, 'rb').read()).hexdigest() if os.path.exists(p) else None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--apply', action='store_true')
    ap.add_argument('--force', action='store_true', help='auch Ordner mit lokalem Overlay überschreiben')
    ap.add_argument('--dir', action='append')
    a = ap.parse_args()
    dirs = [os.path.expanduser(x) for x in (a.dir or ['~/.claude/skills', '~/.codex/skills'])]
    fam = json.load(open(FAM, encoding='utf-8'))
    ts = datetime.datetime.now().strftime('%Y%m%d-%H%M%S')
    for base in dirs:
        if not os.path.isdir(base):
            continue
        print(f'== {base}')
        for r in fam['repos']:
            for name in r['lokal']:
                loc = os.path.join(base, name)
                if not os.path.isdir(loc):
                    continue
                tmp = tempfile.mkdtemp()
                try:
                    c = subprocess.run(['gh', 'repo', 'clone', f"{fam['owner']}/{r['repo']}", tmp, '--', '-q', '--depth', '1'], capture_output=True, text=True)
                    if c.returncode:
                        print(f"⚠️ {name}: GitHub nicht erreichbar ({r['repo']})"); continue
                    same = sha(os.path.join(tmp, 'SKILL.md')) == sha(os.path.join(loc, 'SKILL.md'))
                    new_rev = subprocess.run(['git', '-C', tmp, 'rev-parse', '--short', 'HEAD'], capture_output=True, text=True).stdout.strip()
                    overlay = os.path.exists(os.path.join(loc, 'INSTALLATION.json')) and 'local_overlay' in open(os.path.join(loc, 'INSTALLATION.json')).read()
                    if same:
                        print(f'✅ {name}: aktuell ({new_rev})'); continue
                    if overlay and not a.force:
                        print(f'⚠️ {name}: Update da ({new_rev}), aber lokale Anpassung. Mit --force überschreiben'); continue
                    if not a.apply:
                        print(f'☑️ {name}: Update verfügbar ({new_rev})'); continue
                    bk = os.path.join(base, '.backup-skill-update', ts, name)
                    shutil.copytree(loc, bk)
                    subprocess.run(['rsync', '-a', '--exclude', '.git', '--exclude', '.DS_Store', tmp + '/', loc + '/'], check=True)
                    print(f'✅ {name}: aktualisiert auf {new_rev} (Sicherung: {bk})')
                finally:
                    shutil.rmtree(tmp, ignore_errors=True)


if __name__ == '__main__':
    main()
