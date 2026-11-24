import json, os, subprocess, sys, tempfile, unittest

SCRIPT = os.path.join(os.path.dirname(__file__), '..', 'skills', 'board', 'scripts', 'board.py')


class BoardTest(unittest.TestCase):
    def run_board(self, chat_lines, status):
        with tempfile.TemporaryDirectory() as d:
            c, s, o = (os.path.join(d, n) for n in ('chat.jsonl', 'status.json', 'out.html'))
            open(c, 'w', encoding='utf-8').write('\n'.join(chat_lines))
            open(s, 'w', encoding='utf-8').write(json.dumps(status))
            r = subprocess.run([sys.executable, SCRIPT, '--chat', c, '--status', s, '--out', o], capture_output=True, text=True)
            self.assertEqual(r.returncode, 0, r.stderr)
            return open(o, encoding='utf-8').read()

    def test_renders_threads_and_phases(self):
        chat = [json.dumps({'zeit': '2026-01-01T00:00:00Z', 'von': 'a', 'an': 'b', 'text': 'hallo'})]
        page = self.run_board(chat, {'stand': 'x', 'phasen': [{'nr': 1, 'name': 'P', 'status': 'fertig', 'info': 'i'}],
                                     'threads': {'a': 'wartet auf 2.1.1', 'b': {'text': 'läuft', 'status': 'blockiert'}},
                                     'fragen': ['F?'], 'hinweise': []})
        self.assertIn("class='card t wartet'", page)
        self.assertIn("class='card t blockiert'", page)
        self.assertIn('F?', page)

    def test_escapes_html(self):
        chat = [json.dumps({'zeit': '2026-01-01T00:00:00Z', 'von': 'a', 'an': 'b', 'text': '<script>x</script>'})]
        page = self.run_board(chat, {'threads': {}})
        self.assertNotIn('<script>x</script>', page)

    def test_questions_interactive_with_source(self):
        page = self.run_board([], {'threads': {}, 'fragen': [{'text': 'Frage 1?', 'von': 'plattform', 'detail': 'Details https://x.de'}]})
        self.assertIn("data-von='plattform'", page)
        self.assertIn("data-act='ca'", page)
        self.assertIn('<a href="https://x.de"', page)

    def test_broken_chat_line_ignored(self):
        page = self.run_board(['kaputt', ''], {'threads': {}})
        self.assertIn('0 Nachrichten', page)


if __name__ == '__main__':
    unittest.main()
