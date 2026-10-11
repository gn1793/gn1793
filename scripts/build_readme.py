import json
from urllib.parse import quote
import re
from html import escape
from jinja2 import Environment, FileSystemLoader, StrictUndefined
from common import ROOT, DATA, load_data, visible_items


def md_text(value):
    # Treat remote strings as text, not as Markdown or HTML.
    value = re.sub(r'[\\`*_{}\[\]()#+.!|<>]', lambda m: '\\' + m.group(), str(value))
    return value.replace('\n', ' ').replace('\r', ' ')


def main():
    projects = sorted((p for p in visible_items('projects.yaml', 'projects') if p.get('featured')),
                      key=lambda p: p.get('order', 999))
    builds = visible_items('builds.yaml', 'builds')
    featured = next((b for b in builds if b['featured']), None)
    # Once dates are supplied, newest dated build is selected automatically unless pinned.
    if featured is None and builds:
        featured = max(builds, key=lambda b: (str(b.get('published_at') or ''), b['id']))
    archive = sorted((b for b in builds if b is not featured),
                     key=lambda b: (str(b.get('published_at') or ''), b['id']), reverse=True)
    activity_path = DATA / 'activity.json'
    activity = json.loads(activity_path.read_text(encoding='utf-8')) if activity_path.exists() else []
    env = Environment(loader=FileSystemLoader(ROOT), autoescape=False,
                      undefined=StrictUndefined, keep_trailing_newline=True,
                      trim_blocks=True, lstrip_blocks=True)
    env.filters['e'] = lambda value: escape(str(value), quote=True)
    env.filters['md_text'] = md_text
    env.filters['md_cell'] = lambda value: md_text(value).replace('\\|', '&#124;').replace('|', '&#124;')
    env.filters['md_code'] = lambda value: str(value).replace('`', '').replace('\n', ' ').replace('\r', ' ')
    # Keep each repository represented by only its latest verified commit.
    latest_by_repo = {}
    for event in activity:
        latest_by_repo.setdefault(event['repo'], event)
    activity = list(latest_by_repo.values())
    stack_groups = load_data('tech_stack.yaml')['groups']
    indexed = {g['name']: g['technologies'] for g in stack_groups}
    badge_definitions = [
        ('Languages', [('Python', '3776AB', 'python'), ('Swift', 'F05138', 'swift')]),
        ('Deep Learning', [('PyTorch', 'EE4C2C', 'pytorch'), ('PyTorch Geometric', '654C9B', None)]),
        ('Molecular', [('RDKit', '127D80', None), ('Biopython', '31866C', None), ('Cheminformatics', '32689E', None)]),
        ('Data Science', [('NumPy', '326A93', 'numpy'), ('Pandas', '574B8C', 'pandas'), ('scikit-learn', 'DB8A24', 'scikitlearn')]),
        ('Engineering', [('GitHub', '30343B', 'github'), ('Linux', '8F7422', 'linux')]),
    ]
    badge_stack = []
    allowed = {t for group in indexed.values() for t in group}
    for category, items in badge_definitions:
        badges = []
        for label, color, logo in items:
            if label not in allowed:
                continue
            url = f'https://img.shields.io/badge/{quote(label, safe="")}-{color}?style=for-the-badge'
            if logo:
                url += f'&logo={logo}&logoColor=white'
            badges.append({'label': label, 'url': url})
        badge_stack.append({'name': category, 'badges': badges})
    stats_path = DATA / 'github_stats.json'
    stats = json.loads(stats_path.read_text(encoding='utf-8')) if stats_path.exists() else None
    output = env.get_template('README.template.md').render(
        profile=load_data('profile.yaml'), projects=projects,
        latest_build=featured, archive_builds=archive,
        badge_stack=badge_stack,
        previous_build=archive[0] if archive else None,
        build_collection_url="https://github.com/gn1793?tab=repositories",
        stats=stats,
        publications=[p for p in load_data('publications.yaml')['publications'] if p.get('visible', False)],
        activity=activity)
    (ROOT / 'README.md').write_text(output.rstrip() + '\n', encoding='utf-8')
    print('README.md rendered.')


if __name__ == '__main__':
    main()
