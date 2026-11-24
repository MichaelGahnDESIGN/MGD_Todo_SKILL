import json, os, subprocess, sys, tempfile, unittest

BASE = os.path.join(os.path.dirname(__file__), '..', 'skills', 'repo-update')
REL = os.path.join(BASE, 'scripts', 'related.py')
CHK = os.path.join(BASE, 'scripts', 'repo_check.py')


class RelatedTest(unittest.TestCase):
    def test_family_json_valid(self):
        fam = json.load(open(os.path.join(BASE, 'family.json'), encoding='utf-8'))
        names = {r['repo'] for r in fam['repos']}
        for r in fam['repos']:
            self.assertTrue(set(r['empfiehlt']) <= names, r['repo'])

    def test_block_before_legal_and_idempotent(self):
        with tempfile.TemporaryDirectory() as d:
            p = os.path.join(d, 'README.md')
            open(p, 'w', encoding='utf-8').write('# X\n\n## Verwandte MGD Projekte\nalt\n\n## Lizenz\nMIT\n\n## Impressum\nI\n')
            for _ in range(2):
                subprocess.run([sys.executable, REL, d, '--repo', 'MGD_Todo_SKILL', '--write'], check=True, capture_output=True)
            t = open(p, encoding='utf-8').read()
            self.assertEqual(t.count('MGD-RELATED:START'), 1)
            self.assertNotIn('\nalt\n', t)
            self.assertLess(t.index('Skill-Empfehlungen'), t.index('## Lizenz'))
            self.assertTrue(t.rstrip().endswith('I'))

    def test_check_flags_missing_files(self):
        with tempfile.TemporaryDirectory() as d:
            open(os.path.join(d, 'README.md'), 'w').write('# X\n')
            r = subprocess.run([sys.executable, CHK, d], capture_output=True, text=True)
            self.assertEqual(r.returncode, 1)
            self.assertIn('LICENSE', r.stdout)


if __name__ == '__main__':
    unittest.main()
