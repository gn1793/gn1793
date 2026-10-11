"""Fetch reproducible, public-account GitHub metrics only.

Never infer a contribution grade or pretend public counts cover private activity.
On API failure, exit without replacing the cache or README.
"""
import json
import os
import requests
from common import DATA

API = 'https://api.github.com'
USERNAME = 'gn1793'


def main():
    headers = {'Accept': 'application/vnd.github+json', 'X-GitHub-Api-Version': '2022-11-28'}
    if os.environ.get('GH_TOKEN'):
        headers['Authorization'] = f"Bearer {os.environ['GH_TOKEN']}"
    with requests.Session() as session:
        session.headers.update(headers)
        response = session.get(f'{API}/users/{USERNAME}', timeout=20)
        response.raise_for_status()
        user = response.json()
        stars = 0
        page = 1
        while True:
            response = session.get(f'{API}/users/{USERNAME}/repos',
                                   params={'per_page': 100, 'page': page, 'type': 'owner'}, timeout=20)
            response.raise_for_status()
            repos = response.json()
            stars += sum(r.get('stargazers_count', 0) for r in repos if not r.get('fork', False))
            if len(repos) < 100:
                break
            page += 1
    payload = dict(public_repos=int(user['public_repos']), stars_received=stars,
                   followers=int(user['followers']), following=int(user['following']))
    dest = DATA / 'github_stats.json'
    tmp = dest.with_suffix('.json.tmp')
    tmp.write_text(json.dumps(payload, indent=2) + '\n', encoding='utf-8')
    tmp.replace(dest)
    print('Public GitHub stats updated.')


if __name__ == '__main__':
    main()
