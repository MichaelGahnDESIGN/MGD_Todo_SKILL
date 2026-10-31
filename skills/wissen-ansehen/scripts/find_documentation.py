"""Findet vorhandene Projektdokumentation, ohne zu schreiben oder Code zu starten."""
import argparse
import json
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit


KNOWN = (
    'docs/index.html', 'DOKUMENTATION/index.html', 'WIKI/index.html',
    'docs/LIVING_DOCUMENTATION.html', 'LIVING_DOCUMENTATION.html',
    'docs/LIVING_DOCUMENTATION.md', 'LIVING_DOCUMENTATION.md',
    'DOKUMENTATION/README.md', 'docs/README.md', 'wiki/Home.md', 'WIKI/Home.md',
)


def find_documentation(project, entry=None):
    root = Path(project).expanduser().resolve()
    if not root.is_dir():
        return {'status': 'missing', 'reason': 'project_not_found', 'project': str(root)}

    def candidate(value):
        parts = urlsplit(value)
        if parts.scheme or parts.netloc or not parts.path:
            return None
        path = (root / unquote(parts.path)).resolve()
        # Auch Symlinks dürfen nicht in andere Projekte oder private Ablagen führen.
        if not path.is_relative_to(root) or not path.is_file():
            return None
        if path.suffix.lower() not in ('.html', '.htm', '.md'):
            return None
        return path

    if entry is not None:
        target = candidate(entry)
        if target is None:
            return {'status': 'missing', 'reason': 'entry_not_found_or_outside_project', 'project': str(root)}
        paths = [target]
    else:
        linked = []
        for name in ('README.md', 'readme.md'):
            readme = root / name
            if not readme.is_file() or readme.stat().st_size > 262144:
                continue
            text = readme.read_text(encoding='utf-8', errors='replace')
            for label, href in re.findall(r'\[([^]]+)\]\(([^)]+)\)', text):
                if re.search(r'dokumentation|documentation|\bwiki\b|handbuch', label, re.I):
                    path = candidate(href.strip('<>'))
                    if path is not None:
                        linked.append(path)
        linked.sort(key=lambda p: p.suffix.lower() == '.md')
        paths = list(dict.fromkeys(linked + [p for name in KNOWN if (p := candidate(name)) is not None]))
    if not paths:
        return {'status': 'missing', 'reason': 'no_documentation_entry', 'project': str(root)}
    target = paths[0]
    return {'status': 'found', 'project': str(root), 'target': str(target),
            'kind': 'markdown' if target.suffix.lower() == '.md' else 'html',
            'alternatives': [str(path) for path in paths[1:]]}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--project', required=True)
    parser.add_argument('--entry')
    args = parser.parse_args()
    result = find_documentation(args.project, args.entry)
    print(json.dumps(result, ensure_ascii=False))
    return 0 if result['status'] == 'found' else 2


if __name__ == '__main__':
    raise SystemExit(main())
