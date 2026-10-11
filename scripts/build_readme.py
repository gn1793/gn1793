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
    output = env.get_template('README.template.md').render(
        profile=load_data('profile.yaml'), projects=projects,
        latest_build=featured, archive_builds=archive,
        stack=load_data('tech_stack.yaml'),
        publications=[p for p in load_data('publications.yaml')['publications'] if p.get('visible', False)],
        activity=activity)
    (ROOT / 'README.md').write_text(output.rstrip() + '\n', encoding='utf-8')
    print('README.md rendered.')


if __name__ == '__main__':
    main()
