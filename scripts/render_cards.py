"""Rounded, script-free SVG cards for GitHub's CSS-sanitized README."""
from html import escape
import textwrap
from common import ROOT

OUT = ROOT / 'assets' / 'cards'


def lines(value, width):
    return textwrap.wrap(str(value), width=width, break_long_words=True) or []


def layout(card):
    title = lines(card['title'], 29)
    body = lines(card.get('body', ''), 43)
    tags = lines(' · '.join(card.get('tags', [])), 40)
    header = 30 if card.get('label') else 0
    content_end = 30 + header + len(title) * 25 + (14 if body else 0) + len(body) * 21
    footer_height = len(tags) * 20 + (30 if card.get('footer') else 0)
    height = max(98, content_end + footer_height + 40)
    if not body and not header and not card.get('footer'):
        height = 40 + len(title) * 25 + len(tags) * 20
    return title, body, tags, header, height


def render_group(name, cards):
    OUT.mkdir(parents=True, exist_ok=True)
    result = []
    for offset in range(0, len(cards), 2):
        pair = cards[offset:offset + 2]
        height = max(layout(card)[-1] for card in pair)
        for i, card in enumerate(pair, offset):
            title, body, tags, header, _ = layout(card)
            alt = '. '.join(filter(None, [card.get('label'), card['title'], card.get('body'), ', '.join(card.get('tags', [])), card.get('footer')]))
            parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="400" height="{height}" viewBox="0 0 400 {height}" role="img" aria-labelledby="title desc">',
                     f'<title id="title">{escape(card["title"])}</title><desc id="desc">{escape(alt)}</desc>',
                     f'<rect x="4" y="1" width="392" height="{height - 2}" rx="16" fill="#0D1520" stroke="#354252"/>',
                     '<g font-family="-apple-system,BlinkMacSystemFont,Segoe UI,sans-serif">']
            def text(value, y, size=14, color='#BDC9D8', weight=400):
                parts.append(f'<text x="24" y="{y}" font-size="{size}" font-weight="{weight}" fill="{color}">{escape(value)}</text>')
            if card.get('label'):
                text(card['label'], 30, 11, '#879CAF')
            y = 30 + header
            for line in title:
                text(line, y, 20, '#F3F6FA', 600)
                y += 25
            y += 10
            for line in body:
                text(line, y)
                y += 21
            y = height - 24 - (30 if card.get('footer') else 0) - max(0, len(tags) - 1) * 20
            for line in tags:
                text(line, y, 13, '#A8B9CD')
                y += 20
            if card.get('footer'):
                text(card['footer'], height - 24, 14, '#75DEC8')
            parts.append('</g></svg>')
            path = OUT / f'{name}-{i + 1}.svg'
            path.write_text('\n'.join(parts) + '\n', encoding='utf-8')
            result.append({'src': str(path.relative_to(ROOT)), 'alt': alt, 'url': card.get('url')})
    return result


def render_cards(projects, builds, groups, activity):
    return {
        'research': render_group('research', [dict(title=p['title'], body=p['description'], tags=p['keywords'], label=f'{i + 1:02d} / RESEARCH PROJECT', footer='Status: ' + p['status'], url='https://github.com/' + p['repository'] if p.get('repository') else None) for i, p in enumerate(projects[:2])]),
        'builds': render_group('build', [dict(title=b['title'], body=b['description'], tags=b['technologies'], label=f'{i + 1:02d} / ' + ('FEATURED PROJECT' if i == 0 else 'DEVELOPER UTILITY'), footer='View repository ↗', url='https://github.com/' + b['repository']) for i, b in enumerate(builds) if b]),
        'tools': render_group('tools', [dict(title=g['name'], tags=[b['label'] for b in g['badges']]) for g in groups]),
        'activity': render_group('activity', [dict(title=e['repo'].split('/')[-1], body=e['message'], label=f'{i + 1:02d} / ' + e['date'], footer='View commit ↗', url=e['url']) for i, e in enumerate(activity[:2])]),
    }
