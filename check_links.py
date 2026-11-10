#!/usr/bin/env python3
"""Controlla dist/: link interni e immagini esistono, HTML ben formato, title/description, hreflang."""
import os, sys
from html.parser import HTMLParser
from urllib.parse import urlparse

DIST = os.path.join(os.path.dirname(os.path.abspath(__file__)), "dist")
VOID = {"area","base","br","col","embed","hr","img","input","link","meta","source","track","wbr"}

class P(HTMLParser):
    def __init__(s):
        super().__init__(); s.refs=[]; s.stack=[]; s.err=[]; s.title=None; s.desc=None; s._t=False; s.ids=set()
    def handle_starttag(s, tag, a):
        a=dict(a)
        if a.get("id"): s.ids.add(a["id"])
        for k in ("href","src"):
            if a.get(k): s.refs.append(a[k])
        if tag=="meta" and a.get("name")=="description": s.desc=a.get("content")
        if tag=="title": s._t=True
        if tag not in VOID: s.stack.append(tag)
    def handle_endtag(s, tag):
        if tag in VOID: return
        if not s.stack or s.stack[-1]!=tag: s.err.append(f"chiusura </{tag}> inattesa (aperto: {s.stack[-1:] })"); 
        else: s.stack.pop()
        if tag=="title": s._t=False
    def handle_data(s, d):
        if s._t: s.title=(s.title or "")+d

def target_exists(path):
    p=os.path.join(DIST, path.lstrip("/"))
    return os.path.isfile(p) or os.path.isfile(os.path.join(p,"index.html"))

errors=[]
for dp,_,fs in os.walk(DIST):
    for f in fs:
        if not f.endswith(".html"): continue
        fp=os.path.join(dp,f); rel=os.path.relpath(fp,DIST)
        p=P(); p.feed(open(fp,encoding="utf-8").read())
        if p.stack: errors.append(f"{rel}: tag non chiusi {p.stack}")
        errors += [f"{rel}: {x}" for x in p.err]
        is_redirect = 'http-equiv="refresh"' in open(fp,encoding="utf-8").read()
        if not is_redirect and f!="404.html":
            if not p.title or len(p.title)>65: errors.append(f"{rel}: title assente o lungo ({len(p.title or '')})")
            if not p.desc or not (110<=len(p.desc)<=160): errors.append(f"{rel}: description {len(p.desc or '')} caratteri")
        for r in p.refs:
            u=urlparse(r)
            if u.scheme in ("http","https","mailto","tel") and u.netloc!="trullo-rosy.it": continue
            path=u.path if u.netloc else r.split("#")[0].split("?")[0]
            if not path: continue
            if not target_exists(path): errors.append(f"{rel}: link rotto {r}")
for e in errors: print("ERRORE", e)
print(f"Controllo finito: {len(errors)} errori")
sys.exit(1 if errors else 0)
