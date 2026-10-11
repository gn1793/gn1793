import re
from datetime import date
from common import load_data

REPO = re.compile(r'^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$')


def require(condition, message):
    if not condition:
        raise ValueError(message)


def validate_collection(filename, key, required):
    entries = load_data(filename)[key]
    require(isinstance(entries, list), f'{filename}: {key} must be a list')
    ids = set()
    for index, entry in enumerate(entries):
        label = f'{filename}[{index}]'
        require(isinstance(entry, dict), f'{label}: expected object')
        for field in required:
            require(field in entry and entry[field] not in (None, ''), f'{label}: missing {field}')
        require(entry['id'] not in ids, f'{label}: duplicate id {entry["id"]}')
        ids.add(entry['id'])
        repo = entry.get('repository')
        require(repo is None or (isinstance(repo, str) and REPO.fullmatch(repo)), f'{label}: invalid repository')
        for flag in ('visible', 'featured'):
            require(isinstance(entry.get(flag), bool), f'{label}: {flag} must be boolean')
        if entry.get('published_at'):
            date.fromisoformat(str(entry['published_at']))
    return entries


def validate():
    profile = load_data('profile.yaml')
    require(profile.get('username') == 'gn1793', 'profile username mismatch')
    require(len(profile.get('interests', [])) == 4, 'exactly four interests required for grid')
    research = validate_collection('projects.yaml', 'projects', ['id', 'title', 'status', 'description', 'keywords'])
    builds = validate_collection('builds.yaml', 'builds', ['id', 'title', 'description', 'technologies'])
    require(sum(bool(b['featured'] and b['visible']) for b in builds) <= 1, 'at most one featured visible build')
    for p in research:
        require(isinstance(p.get('keywords'), list), 'research keywords must be a list')
    for b in builds:
        require(isinstance(b.get('technologies'), list), 'technologies must be a list')
        require(not b['visible'] or b['repository'], 'visible build must have a repository')
    stack = load_data('tech_stack.yaml')['groups']
    require(isinstance(stack, list) and bool(stack), 'stack groups required')
    for group in stack:
        require(group.get('name') and isinstance(group.get('technologies'), list), 'invalid stack group')
    pubs = load_data('publications.yaml')['publications']
    require(isinstance(pubs, list), 'publications must be a list')
    for pub in pubs:
        if pub.get('visible', False):
            require(all(pub.get(k) for k in ('title', 'year', 'venue')), 'visible publication missing metadata')
    print('Metadata validated.')


if __name__ == '__main__':
    validate()
