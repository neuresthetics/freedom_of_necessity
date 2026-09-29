#!/usr/bin/env python3
"""Convert The Latin Library Ethica HTML (raw/spinoza.ethica[1-5].html) to plain UTF-8 text.
Rules (documented in MANIFEST.md):
 - Legacy stray bytes: 0x83 -> U+00B0 DEGREE SIGN (ordinal marker, e.g. 'I°'; part 2 uses &#176; for the same),
   0x99 -> U+0153 LATIN SMALL LIGATURE OE ('pœnitentia'; part 4 uses &oelig;). No other non-ASCII bytes exist.
 - HTML entities decoded (&aelig; &AElig; &oelig; &#176;).
 - Tags removed; <p>, <br>, <div>, <hr>, table cells become line breaks; whitespace inside a paragraph
   collapsed to single spaces (as a browser renders it); paragraphs separated by one blank line.
 - Site navigation (Neo-Latin / The Latin Library / The Classics Page links) removed.
 - The five parts are concatenated in order, separated by blank lines. No text is added or altered otherwise.
"""
import html, re, sys
from html.parser import HTMLParser

BLOCK = {'p','br','div','hr','tr','td','table','center','h1','h2','h3'}
class P(HTMLParser):
    def __init__(s):
        super().__init__(convert_charrefs=True); s.out=[]; s.skip=0
    def handle_starttag(s,t,a):
        if t in ('head','title','style','script'): s.skip+=1
        if t in BLOCK: s.out.append('\n\n' if t!='br' else '\n')
    def handle_endtag(s,t):
        if t in ('head','title','style','script'): s.skip=max(0,s.skip-1)
        if t in BLOCK and t!='br': s.out.append('\n\n')
    def handle_data(s,d):
        if not s.skip: s.out.append(d)

NAV = {'Neo-Latin','The Latin Library','The Classics Page','The Classics Homepage'}
def convert(path):
    b=open(path,'rb').read().replace(b'\x83','\u00b0'.encode()).replace(b'\x99','\u0153'.encode())
    t=b.decode('utf-8')
    p=P(); p.feed(t); p.close()
    txt=''.join(p.out)
    paras=[]
    for block in re.split(r'\n\s*\n',txt):
        lines=[re.sub(r'[ \t\r\f\v]+',' ',l).strip() for l in block.split('\n')]
        lines=[l for l in lines if l]
        if not lines or all(l in NAV for l in lines): continue
        paras.append('\n'.join(lines))
    return '\n\n'.join(paras)

parts=[convert(f'raw/spinoza.ethica{i}.html') for i in range(1,6)]
sys.stdout.write('\n\n\n'.join(parts)+'\n')
