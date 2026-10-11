import json
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
    # Compact display: keep every tool, but avoid five large repeated tables.
    display_stack = [
        {'name': 'AI / Data', 'technologies': list(dict.fromkeys(
            tool for group in stack_groups if group['name'] in ('Deep Learning', 'Data Science')
            for tool in group['technologies']))},
        {'name': 'Molecular', 'technologies': list(dict.fromkeys(
            tool for group in stack_groups if group['name'] in ('Molecular Modeling', 'Molecular Property Prediction')
            for tool in group['technologies']))},
        {'name': 'Engineering', 'technologies': next(
            g['technologies'] for g in stack_groups if g['name'] == 'Engineering')},
    ]
    output = env.get_template('README.template.md').render(
        profile=load_data('profile.yaml'), projects=projects,
        latest_build=featured, archive_builds=archive,
        display_stack=display_stack,
        publications=[p for p in load_data('publications.yaml')['publications'] if p.get('visible', False)],
        activity=activity)
    (ROOT / 'README.md').write_text(output.rstrip() + '\n', encoding='utf-8')
    print('README.md rendered.')


if __name__ == '__main__':
    main()
