#!/usr/bin/env python3
# MGD Board - liest chat.jsonl + dashboard-status.json > dashboard.html (nur lesen, offline)
# Aufruf: python3 board.py [--chat chat.jsonl] [--status dashboard-status.json] [--out dashboard.html]
import argparse, collections, datetime, html, json, os, sys

e = html.escape
ICO = {'fertig': '✅', 'arbeitet': '🔧', 'wartet': '⏳', 'blockiert': '🚫', 'offen': '☑️'}


def find_dir():
    # THREAD-CHAT im aktuellen Ordner oder darüber suchen
    p = os.getcwd()
    for _ in range(5):
        c = os.path.join(p, 'THREAD-CHAT')
        if os.path.isdir(c):
            return c
        p = os.path.dirname(p)
    return os.getcwd()


def guess(text):
    t = text.lower()
    if any(w in t for w in ('blockiert', 'fehlgeschlagen', 'abgebrochen')):
        return 'blockiert'
    if 'wartet' in t or 'warte' in t:
        return 'wartet'
    if any(w in t for w in ('fertig', 'live', 'veröffentlicht')):
        return 'fertig'
    return 'arbeitet'


def ago(z):
    try:
        t = datetime.datetime.strptime(z, '%Y-%m-%dT%H:%M:%SZ').replace(tzinfo=datetime.timezone.utc)
        s = int((datetime.datetime.now(datetime.timezone.utc) - t).total_seconds())
    except Exception:
        return z or '-'
    if s >= 86400:
        return f'vor {s // 86400} Tg'
    if s >= 3600:
        return f'vor {s // 3600} Std'
    return f'vor {max(s // 60, 0)} Min'


def main():
    base = find_dir()
    ap = argparse.ArgumentParser()
    ap.add_argument('--chat', default=os.path.join(base, 'chat.jsonl'))
    ap.add_argument('--status', default=os.path.join(base, 'dashboard-status.json'))
    ap.add_argument('--out', default=os.path.join(base, 'dashboard.html'))
    a = ap.parse_args()

    try:
        st = json.load(open(a.status, encoding='utf-8'))
    except Exception as ex:
        print('Status-Datei fehlt oder kaputt:', a.status, ex, file=sys.stderr)
        st = {'stand': '-', 'phasen': [], 'threads': {}, 'fragen': [], 'hinweise': []}
    msgs = []
    try:
        for l in open(a.chat, encoding='utf-8'):
            try:
                msgs.append(json.loads(l))
            except Exception:
                pass
    except Exception as ex:
        print('Chat fehlt:', a.chat, ex, file=sys.stderr)

    cnt = collections.Counter(m.get('von') for m in msgs)
    last = {m.get('von'): m for m in msgs}

    # Phasen
    ph = st.get('phasen', [])
    done = sum(1 for p in ph if p.get('status') == 'fertig')
    pct = int(100 * done / len(ph)) if ph else 0
    steps = ''.join(
        f"<div class='step {e(p.get('status',''))}'><span class='nr'>{e(str(p.get('nr','')))}</span>"
        f"<b>{e(p.get('name',''))}</b><small>{ICO.get(p.get('status'),'')} {e(p.get('status',''))}</small>"
        f"<em>{e(p.get('info',''))}</em></div>" for p in ph)

    # Threads
    cards, tally = '', collections.Counter()
    for n, v in st.get('threads', {}).items():
        txt, stat = (v.get('text', ''), v.get('status')) if isinstance(v, dict) else (v, None)
        stat = stat or guess(txt)
        tally[stat] += 1
        m = last.get(n)
        cards += (f"<div class='card t {stat}' data-s='{e(n.lower())} {e(txt.lower())}'>"
                  f"<div class='h'><span class='dot'></span><b>{e(n)}</b><small>{ago(m['zeit']) if m else '-'}</small></div>"
                  f"<p>{e(txt)}</p><div class='f'>{ICO.get(stat,'')} {e(stat)} · {cnt.get(n,0)} Nachr.</div></div>")

    tiles = ''.join(
        f"<div class='tile {k}'><b>{tally.get(k,0)}</b><span>{ICO[k]} {k}</span></div>"
        for k in ('fertig', 'arbeitet', 'wartet', 'blockiert'))
    fr = ''.join(f'<li>❓ {e(x)}</li>' for x in st.get('fragen', [])) or '<li>Keine offenen Fragen ✅</li>'
    hi = ''.join(f'<li>⚠️ {e(x)}</li>' for x in st.get('hinweise', [])) or '<li>Keine Hinweise</li>'
    recent = ''.join(
        f"<details class='m'><summary><small>{e(str(m.get('zeit',''))[5:16].replace('T',' '))}</small> "
        f"<b>{e(str(m.get('von')))}</b> → {e(str(m.get('an')))} "
        f"<span>{e(str(m.get('text',''))[:90])}</span></summary><p>{e(str(m.get('text','')))}</p></details>"
        for m in msgs[-15:][::-1])
    now = datetime.datetime.now().strftime('%d.%m.%Y %H:%M')

    css = """
:root{--bg:#f6f5f0;--fg:#1d2723;--card:#fff;--line:#dedbd0;--acc:#2f5d4a;--mut:#6b756f;--g:#2a9d5c;--b:#2f7bd0;--y:#c98a00;--r:#d04a3f;--o:#9aa39e}
@media(prefers-color-scheme:dark){:root{--bg:#121516;--fg:#e8e8e2;--card:#1c2123;--line:#333a3c;--acc:#7fc4a4;--mut:#98a39d;--g:#4cc380;--b:#6aa8f0;--y:#e0a82e;--r:#f0766b;--o:#6d7873}}
*{box-sizing:border-box}body{background:var(--bg);color:var(--fg);font:15px/1.5 -apple-system,system-ui,sans-serif;margin:0;padding:20px;max-width:1180px;margin:auto}
header{display:flex;flex-wrap:wrap;gap:12px;align-items:end;justify-content:space-between}h1{margin:0;font-size:26px}h2{margin:28px 0 10px;font-size:17px;color:var(--acc);letter-spacing:.3px}
.sub{color:var(--mut);font-size:12.5px}.bar{height:10px;background:var(--line);border-radius:9px;overflow:hidden;margin:10px 0 6px}.bar i{display:block;height:100%;background:var(--g);width:PCT%}
.tiles{display:grid;grid-template-columns:repeat(auto-fit,minmax(130px,1fr));gap:10px;margin-top:14px}.tile{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:12px;border-top:4px solid var(--o)}
.tile b{font-size:28px;display:block}.tile span{color:var(--mut);font-size:13px}.tile.fertig{border-top-color:var(--g)}.tile.arbeitet{border-top-color:var(--b)}.tile.wartet{border-top-color:var(--y)}.tile.blockiert{border-top-color:var(--r)}
.steps{display:grid;grid-template-columns:repeat(auto-fit,minmax(170px,1fr));gap:10px}.step{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:10px 12px;position:relative}
.step .nr{position:absolute;top:8px;right:10px;color:var(--mut);font-size:12px}.step b{display:block;font-size:14px;padding-right:18px}.step small{color:var(--mut)}.step em{display:block;font-style:normal;font-size:12.5px;color:var(--mut);margin-top:4px}
.step.fertig{border-left:4px solid var(--g)}.step.wartet,.step.arbeitet{border-left:4px solid var(--y)}.step.offen{border-left:4px solid var(--o);opacity:.85}
.search{width:100%;padding:10px 12px;border:1px solid var(--line);border-radius:10px;background:var(--card);color:var(--fg);font:inherit;margin-bottom:10px}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(250px,1fr));gap:10px}.card{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:12px}
.t .h{display:flex;align-items:center;gap:8px}.t .h small{margin-left:auto;color:var(--mut);font-size:12px}.dot{width:11px;height:11px;border-radius:50%;background:var(--o)}
.t.fertig .dot{background:var(--g)}.t.arbeitet .dot{background:var(--b)}.t.wartet .dot{background:var(--y)}.t.blockiert .dot{background:var(--r)}.t p{margin:8px 0;font-size:13.5px}.t .f{font-size:12px;color:var(--mut)}
.two{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:12px}ul{margin:0;padding-left:18px}li{margin:5px 0}
.m{border-bottom:1px solid var(--line);padding:6px 0;font-size:13px}.m summary{cursor:pointer;list-style:none}.m span{color:var(--mut)}.m p{white-space:pre-wrap;margin:6px 0 4px 6px}
.hide{display:none}footer{margin:30px 0 8px;color:var(--mut);font-size:12px}
@media(max-width:600px){body{padding:12px}h1{font-size:21px}}
""".replace('PCT', str(pct))

    page = f"""<!doctype html><html lang="de"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta http-equiv="refresh" content="300"><title>MGD Message-Board</title><style>{css}</style></head><body>
<header><div><h1>MGD Message-Board</h1><div class="sub">Stand {e(str(st.get('stand','-')))} · erzeugt {now} · {len(msgs)} Nachrichten · lädt alle 5 Min neu</div></div>
<div class="sub">Phasen: {done} von {len(ph)} fertig ({pct} %)</div></header>
<div class="bar"><i></i></div>
<div class="tiles">{tiles}</div>
<h2>Phasen</h2><div class="steps">{steps}</div>
<h2>Threads</h2><input class="search" id="q" placeholder="Thread suchen (Name oder Stichwort)…" aria-label="Threads suchen">
<div class="grid" id="g">{cards}</div>
<div class="two"><div><h2>Offene Fragen an dich</h2><div class="card"><ul>{fr}</ul></div></div>
<div><h2>Wichtige Hinweise</h2><div class="card"><ul>{hi}</ul></div></div></div>
<h2>Letzte Chat-Nachrichten</h2><div class="card">{recent}</div>
<footer>MGD Board · nur lesen · keine Zugangsdaten · neu erzeugen: <code>python3 board.py</code></footer>
<script>var q=document.getElementById('q');q.addEventListener('input',function(){{var v=q.value.toLowerCase();document.querySelectorAll('#g .card').forEach(function(c){{c.classList.toggle('hide',c.dataset.s.indexOf(v)<0)}})}})</script>
</body></html>"""
    open(a.out, 'w', encoding='utf-8').write(page)
    print('Board fertig:', a.out)


if __name__ == '__main__':
    main()
