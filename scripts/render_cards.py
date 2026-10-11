"""Deterministic, dependency-free SVG card generator for GitHub Markdown.
No scripts, remote resources, or foreignObject: safe to embed with <img>.
"""
from html import escape
from pathlib import Path
import re
import textwrap
from common import ROOT, load_data, visible_items

OUT = ROOT / 'assets' / 'generated'
BG, PANEL, STROKE = '#0D1523', '#132337', '#294257'
TEAL, WHITE, MUTED, GOLD = '#72D9CB', '#EDF5FF', '#A8B9CD', '#E5BA79'
FONT = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, sans-serif"


def txt(x, y, value, size=20, color=WHITE, bold=False, anchor=None):
    attrs = f'font-size="{size}" fill="{color}" font-weight="{700 if bold else 400}"'
    if anchor: attrs += f' text-anchor="{anchor}"'
    return f'<text x="{x}" y="{y}" {attrs}>{escape(str(value))}</text>'


def lines(value, width=48, limit=3):
    result = textwrap.wrap(str(value), width=width, break_long_words=False, break_on_hyphens=False)
    if len(result) > limit:
        result = result[:limit]
        result[-1] = result[-1].rstrip(' .,') + '…'
    return result


def paragraph(x, y, value, width=48, limit=3, size=17, leading=26):
    return ''.join(txt(x, y + i * leading, line, size, MUTED) for i, line in enumerate(lines(value, width, limit)))


def chip(x, y, value, color=TEAL):
    w = max(64, min(270, 24 + len(str(value)) * 8.0))
    return (f'<rect x="{x}" y="{y}" width="{w}" height="30" rx="15" fill="#1D3547"/>'
            + txt(x + 12, y + 21, value, 13, color)), w


def icon(kind, x, y, scale=1):
    base = {
        'rna': '<path d="M4 0 C50 25 0 48 44 75 S6 123 44 145"/><path d="M44 0 C0 25 50 48 4 75 S42 123 4 145"/><path d="M9 21H39 M7 52H41 M7 92H41 M9 125H39"/>',
        'graph': '<path d="M6 120 L25 69 L66 90 L84 21"/><circle cx="6" cy="120" r="8"/><circle cx="25" cy="69" r="8"/><circle cx="66" cy="90" r="8"/><circle cx="84" cy="21" r="8"/>',
        'brain': '<path d="M45 9 C5 -5 -5 31 9 52 C-5 72 14 104 44 94 M45 9 C85 -5 96 31 80 52 C96 72 76 104 45 94 M45 9V96 M12 45L34 52 M78 45L55 52 M24 72L42 64 M65 72L47 64"/>',
        'flask': '<path d="M28 6H63 M37 6V50L10 96Q5 106 18 106H78Q89 106 82 96L55 50V6 M25 78H67"/>',
        'code': '<path d="M33 20L8 48L33 75 M65 20L90 48L65 75 M55 10L44 86"/>',
        'monitor': '<rect x="5" y="12" width="92" height="62" rx="7"/><path d="M51 74V97 M31 97H71 M19 57L33 38L47 46L64 28L81 42"/>',
    }
    return f'<g transform="translate({x} {y}) scale({scale})" fill="none" stroke="{TEAL}" stroke-width="3.1" stroke-linejoin="round" stroke-linecap="round">{base.get(kind, base["code"])}</g>'


def svg(w, h, content, title):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="{escape(title, quote=True)}">'
            f'<title>{escape(title)}</title><rect width="{w}" height="{h}" rx="18" fill="{PANEL}"/>'
            f'<rect x="1" y="1" width="{w-2}" height="{h-2}" rx="17" fill="none" stroke="{STROKE}" stroke-width="2"/>'
            f'{content}</svg>\n')


def save(name, w, h, body, title):
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / name).write_text(svg(w, h, body, title), encoding='utf-8')


def slug(value):
    return re.sub(r'[^a-z0-9-]+', '-', value.lower()).strip('-')


def render():
    interests = load_data('profile.yaml')['interests']
    kinds = ['rna', 'graph', 'brain', 'flask']
    for i, item in enumerate(interests):
        body = icon(kinds[i], 24, 25, .52)
        title = lines(item['title'], 23, 2)
        body += ''.join(txt(94, 54 + j*26, t, 20, WHITE, True) for j,t in enumerate(title))
        body += paragraph(24, 137, item['detail'], 34, 2, 16, 24)
        save(f'interest-{i+1}.svg', 345, 188, body, item['title'])

    projects = sorted((p for p in visible_items('projects.yaml','projects') if p['featured']), key=lambda p:p.get('order',999))
    for i,p in enumerate(projects):
        body = icon('rna' if i == 0 else 'graph', 35, 82, 1.25)
        body += f'<rect x="411" y="22" width="138" height="32" rx="16" fill="#174C48"/>' + txt(480, 44, p['status'], 15, TEAL, True, 'middle')
        body += txt(180, 84, p['title'], 21, WHITE, True)
        body += paragraph(180, 124, p['description'], 42, 4, 16, 26)
        x=180
        for tag in p['keywords'][:3]:
            part,w = chip(x, 237, tag)
            if x+w>560: break
            body += part; x += w+9
        save(f'research-{slug(p["id"])}.svg', 570, 285, body, p['title'])

    builds = visible_items('builds.yaml','builds')
    featured = next((b for b in builds if b.get('featured')), None)
    if featured is None and builds:
        featured = max(builds,key=lambda b:(str(b.get('published_at') or ''),b['id']))
    if featured:
        body = icon('monitor', 45, 76, 1.3)
        body += txt(210, 60, 'LATEST BUILD', 15, TEAL, True)
        body += txt(210, 103, featured['title'], 28, WHITE, True)
        body += paragraph(210, 143, featured['description'], 65, 2, 18, 27)
        x=210
        for tag in featured['technologies'][:4]:
            part,w=chip(x,223,tag,GOLD);body+=part;x+=w+10
        body+=txt(210,300,'VIEW REPOSITORY  ↗',17,TEAL,True)
        save('latest-build.svg',1135,340,body,featured['title'])
    for b in builds:
        if b is featured:continue
        body=icon('code',28,27,.64)
        body+=txt(117,58,b['title'],22,WHITE,True)
        body+=paragraph(117,90,b['description'],80,2,16,25)
        body+=txt(117,147,'  ·  '.join(b['technologies']),14,TEAL)
        save(f'archive-{slug(b["id"])}.svg',1135,175,body,b['title'])

    groups=load_data('tech_stack.yaml')['groups']
    for i,group in enumerate(groups):
        body=txt(22,43,group['name'],18,TEAL,True)
        y=74
        for tech in group['technologies']:
            body+=f'<rect x="18" y="{y}" width="235" height="34" rx="11" fill="#1D3547"/>'
            body+=txt(30,y+23,tech,15,WHITE)
            y+=46
        save(f'stack-{i+1}.svg',273,244,body,group['name'])
    print('SVG cards rendered in assets/generated/.')

if __name__ == '__main__':render()
