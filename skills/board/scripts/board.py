#!/usr/bin/env python3
# MGD Board - liest chat.jsonl + dashboard-status.json > dashboard.html (nur lesen, offline)
# Aufruf: python3 board.py [--chat chat.jsonl] [--status dashboard-status.json] [--out dashboard.html]
import argparse, collections, datetime, hashlib, html, json, os, re, sys

e = html.escape
JS = r'''<script>
var $=function(s,r){return Array.prototype.slice.call((r||document).querySelectorAll(s))};
function ls(k,v){try{if(v===undefined)return localStorage.getItem('mgdb_'+k);if(v===null)localStorage.removeItem('mgdb_'+k);else localStorage.setItem('mgdb_'+k,v)}catch(x){return null}}
function copy(txt,el){var done=function(){var o=el.parentNode.querySelector('.ok');if(o){o.textContent='✅ kopiert';setTimeout(function(){o.textContent=''},2000)}};
 if(navigator.clipboard&&window.isSecureContext){navigator.clipboard.writeText(txt).then(done,function(){fb()})}else fb();
 function fb(){var a=document.createElement('textarea');a.value=txt;document.body.appendChild(a);a.select();try{document.execCommand('copy');done()}catch(x){}document.body.removeChild(a)}}
function qtxt(d){var v=d.dataset.von;return (v?'Frage aus Thread "'+v+'": ':'Frage: ')+d.dataset.t}
$('details[data-k]').forEach(function(d){if(ls('open_'+d.dataset.k)==='1')d.open=true;d.addEventListener('toggle',function(){ls('open_'+d.dataset.k,d.open?'1':null)})});
$('.ans').forEach(function(a){var s=ls('ans_'+a.dataset.k);if(s)a.value=s;a.addEventListener('input',function(){ls('ans_'+a.dataset.k,a.value||null)})});
document.addEventListener('click',function(ev){var b=ev.target.closest('button[data-act]');if(!b)return;var act=b.dataset.act,d=b.closest('.it');
 if(act==='cq')copy(qtxt(d),b);
 if(act==='ca'){var a=d.querySelector('.ans').value.trim();copy(qtxt(d)+'\nMeine Antwort: '+(a||'(noch keine)'),b)}
 if(act==='all'){var out=[];$('.it.q').forEach(function(x){var a=x.querySelector('.ans').value.trim();if(a)out.push(qtxt(x)+'\nMeine Antwort: '+a)});copy(out.length?out.join('\n\n'):'(noch keine Antworten)',b)}});
document.getElementById('ex').onclick=function(){$('details').forEach(function(d){d.open=true})};
document.getElementById('co').onclick=function(){$('details').forEach(function(d){d.open=false})};
var q=document.getElementById('q');q.addEventListener('input',function(){var v=q.value.toLowerCase();$('#g .card').forEach(function(c){c.classList.toggle('hide',c.dataset.s.indexOf(v)<0)})});
setTimeout(function re(){var f=document.activeElement;if(f&&(f.tagName==='TEXTAREA'||f.tagName==='INPUT')){setTimeout(re,30000);return}location.reload()},300000);
</script>'''
ICO = {'fertig': '✅', 'arbeitet': '🔧', 'wartet': '⏳', 'blockiert': '🚫', 'offen': '☑️'}


def link(s):
    # URLs im Text klickbar machen (erst escapen, dann verlinken)
    return re.sub(r'(https?://[^\s<]+)', r'<a href="\1" target="_blank" rel="noopener">\1</a>', e(s))


def hid(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()[:8]


def item(x):
    # Frage/Hinweis: String oder {text, von, detail, link}
    return x if isinstance(x, dict) else {'text': x}


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
        f"<details class='step {e(p.get('status',''))}' data-k='ph{e(str(p.get('nr','')))}'><summary><span class='nr'>{e(str(p.get('nr','')))}</span>"
        f"<b>{e(p.get('name',''))}</b><small>{ICO.get(p.get('status'),'')} {e(p.get('status',''))}</small></summary>"
        f"<em>{link(p.get('info',''))}</em>"
        + (f"<p>{link(p['detail'])}</p>" if p.get('detail') else '') + "</details>" for p in ph)

    # Threads
    cards, tally = '', collections.Counter()
    by_thread = collections.defaultdict(list)
    for m in msgs:
        by_thread[m.get('von')].append(m)
    for n, v in st.get('threads', {}).items():
        d = v if isinstance(v, dict) else {'text': v}
        txt = d.get('text', '')
        stat = d.get('status') or guess(txt)
        tally[stat] += 1
        m = last.get(n)
        sess = d.get('session')
        open_link = (f"<a class='btn' href='claude://claude.ai/epitaxy/{e(sess)}'>Thread öffnen ↗</a>" if sess else
                     (f"<a class='btn' href='{e(d['link'])}' target='_blank' rel='noopener'>Öffnen ↗</a>" if d.get('link') else ''))
        recent_t = ''.join(
            f"<div class='tm'><small>{e(str(x.get('zeit',''))[5:16].replace('T',' '))} → {e(str(x.get('an')))}</small><br>{link(str(x.get('text',''))[:500])}</div>"
            for x in by_thread.get(n, [])[-3:][::-1]) or '<div class="tm"><small>Noch keine Nachricht</small></div>'
        cards += (f"<details class='card t {stat}' data-k='th{e(n)}' data-s='{e(n.lower())} {e(txt.lower())}'>"
                  f"<summary><span class='dot'></span><b>{e(n)}</b><small>{ago(m['zeit']) if m else '-'}</small></summary>"
                  f"<p>{link(txt)}</p><div class='f'>{ICO.get(stat,'')} {e(stat)} · {cnt.get(n,0)} Nachr. {open_link}</div>"
                  f"<div class='tms'>{recent_t}</div></details>")

    tiles = ''.join(
        f"<div class='tile {k}'><b>{tally.get(k,0)}</b><span>{ICO[k]} {k}</span></div>"
        for k in ('fertig', 'arbeitet', 'wartet', 'blockiert'))
    def entry(x, kind):
        d = item(x)
        k = kind + hid(d['text'])
        von = d.get('von', '')
        src = f"<span class='von'>aus: {e(von)}</span>" if von else ''
        det = f"<div class='det'>{link(d['detail'])}</div>" if d.get('detail') else ''
        lk = f" <a href='{e(d['link'])}' target='_blank' rel='noopener'>Link ↗</a>" if d.get('link') else ''
        icon = '❓' if kind == 'q' else '⚠️'
        ans = (f"<textarea class='ans' data-k='{k}' rows='2' placeholder='Deine Antwort…'></textarea>"
               f"<div class='row'><button data-act='cq' data-k='{k}'>Frage kopieren</button>"
               f"<button data-act='ca' data-k='{k}'>Antwort kopieren</button><span class='ok'></span></div>") if kind == 'q' else \
              f"<div class='row'><button data-act='cq' data-k='{k}'>Kopieren</button><span class='ok'></span></div>"
        return (f"<details class='it {kind}' data-k='{k}' data-von='{e(von)}' data-t='{e(d['text'])}'>"
                f"<summary>{icon} {link(d['text'])}{lk} {src}</summary>{det}{ans}</details>")

    fr = ''.join(entry(x, 'q') for x in st.get('fragen', [])) or '<p>Keine offenen Fragen ✅</p>'
    hi = ''.join(entry(x, 'h') for x in st.get('hinweise', [])) or '<p>Keine Hinweise</p>'
    recent = ''.join(
        f"<details class='m'><summary><small>{e(str(m.get('zeit',''))[5:16].replace('T',' '))}</small> "
        f"<b>{e(str(m.get('von')))}</b> → {e(str(m.get('an')))} "
        f"<span>{e(str(m.get('text',''))[:90])}</span></summary><p>{link(str(m.get('text','')))}</p></details>"
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
.hide{display:none}
details>summary{cursor:pointer;list-style:none}details>summary::-webkit-details-marker{display:none}
details>summary::before{content:'▸';display:inline-block;width:1em;color:var(--mut)}details[open]>summary::before{content:'▾'}
.t summary{display:flex;align-items:center;gap:8px}.t summary small{margin-left:auto;color:var(--mut);font-size:12px}
.tms{border-top:1px dashed var(--line);margin-top:8px;padding-top:6px}.tm{font-size:12.5px;margin:6px 0;word-break:break-word}
.btn{display:inline-block;margin-left:8px;padding:2px 8px;border:1px solid var(--line);border-radius:8px;text-decoration:none;color:var(--acc)}
a{color:var(--acc)}.step summary{padding-right:18px}.step em{display:block}
.it{border-bottom:1px solid var(--line);padding:8px 0}.it:last-child{border:0}.von{display:inline-block;background:var(--bg);border:1px solid var(--line);border-radius:8px;padding:0 8px;font-size:12px;color:var(--mut);margin-left:6px}
.det{margin:6px 0 4px 18px;font-size:13.5px;color:var(--mut)}.ans{width:100%;margin-top:8px;padding:8px;border:1px solid var(--line);border-radius:8px;background:var(--bg);color:var(--fg);font:inherit}
.row{display:flex;gap:8px;align-items:center;margin-top:6px;flex-wrap:wrap}button{border:1px solid var(--line);background:var(--card);color:var(--fg);border-radius:8px;padding:5px 10px;cursor:pointer;font:inherit;font-size:13px}button:hover{border-color:var(--acc)}
.ok{color:var(--g);font-size:12.5px}.bar2{display:flex;gap:8px;margin:14px 0 0;flex-wrap:wrap}footer{margin:30px 0 8px;color:var(--mut);font-size:12px}
@media(max-width:600px){body{padding:12px}h1{font-size:21px}}
""".replace('PCT', str(pct))

    page = f"""<!doctype html><html lang="de"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>MGD Message-Board</title><style>{css}</style></head><body>
<header><div><h1>MGD Message-Board</h1><div class="sub">Stand {e(str(st.get('stand','-')))} · erzeugt {now} · {len(msgs)} Nachrichten · lädt alle 5 Min neu (nicht beim Tippen)</div></div>
<div class="sub">Phasen: {done} von {len(ph)} fertig ({pct} %)</div></header>
<div class="bar"><i></i></div>
<div class="bar2"><button id="ex">Alles aufklappen</button><button id="co">Alles zuklappen</button></div>
<div class="tiles">{tiles}</div>
<h2>Phasen</h2><div class="steps">{steps}</div>
<h2>Threads</h2><input class="search" id="q" placeholder="Thread suchen (Name oder Stichwort)…" aria-label="Threads suchen">
<div class="grid" id="g">{cards}</div>
<div class="two"><div><h2>Offene Fragen an dich</h2><div class="card">{fr}<div class='row'><button data-act='all'>Alle beantworteten kopieren</button><span class='ok'></span></div></div></div>
<div><h2>Wichtige Hinweise</h2><div class="card">{hi}</div></div></div>
<h2>Letzte Chat-Nachrichten</h2><div class="card">{recent}</div>
<footer>MGD Board · nur lesen · keine Zugangsdaten · neu erzeugen: <code>python3 board.py</code></footer>
{JS}
</body></html>"""
    open(a.out, 'w', encoding='utf-8').write(page)
    print('Board fertig:', a.out)


if __name__ == '__main__':
    main()
