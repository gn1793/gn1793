"""Generate a deterministic, accessible SVG from verified GitHub metric cache."""
import json
import math
from html import escape
from common import ROOT, DATA

OUT = ROOT / 'assets' / 'github-stats.svg'


def fmt(value):
    return f'{int(value):,}' if isinstance(value, int) and not isinstance(value, bool) else 'N/A'


def main():
    path = DATA / 'github_stats.json'
    metrics = json.loads(path.read_text(encoding='utf-8')) if path.exists() else {}
    fields = [
        ('Total Stars', metrics.get('stars_received')),
        ('Commits', metrics.get('commit_contributions_12m')),
        ('PRs', metrics.get('pr_contributions_12m')),
        ('Issues', metrics.get('issue_contributions_12m')),
        ('Contributions', metrics.get('total_contributions_12m')),
    ]
    total = metrics.get('total_contributions_12m')
    valid = isinstance(total, int) and total >= 0
    ratio = min(total / 100, 1) if valid else 0
    circumference = 2 * math.pi * 69
    dashboard_rows = []
    for i, (label, value) in enumerate(fields):
        y = 124 + i * 59
        dashboard_rows.append(f'<text x="47" y="{y}" font-size="18" fill="#BDC9D8">{escape(label)}</text>'
                              f'<text x="463" y="{y}" font-size="20" font-weight="600" text-anchor="end" fill="#75DEC8">{fmt(value)}</text>')
    label = f'{min(total,100)}%' if valid else 'N/A'
    progress = f'{total:,} / 100' if valid else 'Awaiting data'
    # The ring indicates an explicitly defined personal 100-contribution milestone,
    # not a GitHub rank or percentile. Clamp above 100 at full circle.
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="800" height="460" viewBox="0 0 800 460" role="img" aria-labelledby="t d">
<title id="t">GitHub Stats for gn1793</title>
<desc id="d">Public stars and GitHub contributions for the last 12 months. The ring shows progress toward a reference milestone of 100 contributions, not a GitHub rating.</desc>
<rect x="4" y="1" width="792" height="458" rx="16" fill="#0D1520" stroke="#354252" stroke-width="1"/>
<text x="42" y="58" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, sans-serif" font-size="30" font-weight="700" fill="#F3F6FA">GitHub Stats</text>
<path d="M43 77 H757" stroke="#273748"/>
<g font-family="-apple-system, BlinkMacSystemFont, Segoe UI, sans-serif">{''.join(dashboard_rows)}
<circle cx="634" cy="215" r="69" stroke="#303B4A" stroke-width="13" fill="none"/>
<circle cx="634" cy="215" r="69" stroke="#72D9CB" stroke-width="13" fill="none" stroke-linecap="round" stroke-dasharray="{ratio*circumference:.2f} {circumference:.2f}" transform="rotate(-90 634 215)"/>
<text x="634" y="211" font-size="27" font-weight="700" text-anchor="middle" fill="#F3F6FA">{escape(label)}</text>
<text x="634" y="239" font-size="14" text-anchor="middle" fill="#A8B9CD">of milestone</text>
<text x="634" y="332" font-size="16" text-anchor="middle" fill="#B7CAD6">{escape(progress)} contributions</text>
<text x="634" y="356" font-size="13" text-anchor="middle" fill="#879CAF">100-contribution reference</text>

</g></svg>'''
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(svg + '\n', encoding='utf-8')
    print('Stats SVG rendered.')


if __name__ == '__main__':
    main()
