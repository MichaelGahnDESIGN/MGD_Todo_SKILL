"""Prüft echte Pfadauswahl und Projektgrenzen ohne Browser oder Fremdpakete."""
from pathlib import Path
import runpy
import tempfile
import unittest

REPO = Path(__file__).resolve().parents[1]
find = runpy.run_path(str(REPO / 'skills/wissen-ansehen/scripts/find_documentation.py'))['find_documentation']


class DocumentationFinderTest(unittest.TestCase):
    def setUp(self):
        # Testdaten liegen nur unter dem vom Aufrufer festgelegten TMPDIR.
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.base = Path(self.directory.name)
        self.root = self.base / 'projekt'
        self.root.mkdir()

    def write(self, name, text='Dokumentation'):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text)
        return path.resolve()

    def test_html_is_preferred_and_project_is_not_changed(self):
        target = self.write('docs/index.html')
        self.write('docs/LIVING_DOCUMENTATION.md')
        before = {str(p.relative_to(self.root)): p.read_bytes() for p in self.root.rglob('*') if p.is_file()}
        result = find(self.root)
        self.assertEqual(result['target'], str(target))
        self.assertEqual(result['kind'], 'html')
        after = {str(p.relative_to(self.root)): p.read_bytes() for p in self.root.rglob('*') if p.is_file()}
        self.assertEqual(before, after)

    def test_markdown_fallback(self):
        target = self.write('docs/LIVING_DOCUMENTATION.md')
        self.assertEqual(find(self.root)['target'], str(target))
        self.assertEqual(find(self.root)['kind'], 'markdown')

    def test_readme_documents_custom_entry_with_spaces(self):
        target = self.write('Unser Wissen/start.html')
        self.write('README.md', '[Dokumentation](Unser%20Wissen/start.html)')
        self.assertEqual(find(self.root)['target'], str(target))

    def test_explicit_entry_wins(self):
        self.write('docs/index.html')
        target = self.write('WIKI/Home.md')
        self.assertEqual(find(self.root, 'WIKI/Home.md')['target'], str(target))

    def test_missing_documentation_creates_nothing(self):
        self.assertEqual(find(self.root)['status'], 'missing')
        self.assertEqual(list(self.root.iterdir()), [])

    def test_missing_project_is_not_created(self):
        target = self.base / 'fehlt'
        self.assertEqual(find(target)['status'], 'missing')
        self.assertFalse(target.exists())

    def test_external_and_parent_links_are_not_selected(self):
        (self.base / 'extern.md').write_text('Außerhalb')
        self.write('README.md', '[Dokumentation](https://example.invalid/docs)\n[Wiki](../extern.md)')
        self.assertEqual(find(self.root)['status'], 'missing')
        self.assertEqual(find(self.root, '../extern.md')['status'], 'missing')

    def test_symlink_outside_project_is_not_selected(self):
        outside = self.base / 'extern.html'
        outside.write_text('Außerhalb')
        (self.root / 'docs').mkdir()
        (self.root / 'docs/index.html').symlink_to(outside)
        self.assertEqual(find(self.root)['status'], 'missing')

    def test_no_project_program_is_executed(self):
        marker = self.root / 'ausgefuehrt'
        self.write('build.py', "from pathlib import Path; Path('ausgefuehrt').touch()")
        self.write('package.json', '{"scripts":{"docs":"python3 build.py"}}')
        self.write('README.md', '[Dokumentation](build.py)')
        self.assertEqual(find(self.root)['status'], 'missing')
        self.assertFalse(marker.exists())


if __name__ == '__main__':
    unittest.main()
