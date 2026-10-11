"""Fetch confirmed commits by gn1793 in the public build repositories.

Fail closed: on API errors exit nonzero before replacing cached data/README.
"""
import json
import os
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import quote
import requests
from common import DATA, visible_items

USERNAME = 'gn1793'
API = 'https://api.github.com'


def main():
    token = os.environ.get('GH_TOKEN')
    headers = {'Accept': 'application/vnd.github+json', 'X-GitHub-Api-Version': '2022-11-28'}
    if token:
        headers['Authorization'] = f'Bearer {token}'
    repos = sorted({b['repository'] for b in visible_items('builds.yaml', 'builds') if b.get('repository')})
    commits = []
    with requests.Session() as session:
        session.headers.update(headers)
        for repo in repos:
            response = session.get(f'{API}/repos/{repo}/commits',
                                   params={'per_page': 30}, timeout=20)
            response.raise_for_status()
            for item in response.json():
                author = item.get('author') or {}
                # Require authenticated GitHub author match; don't ascribe others' commits.
                if author.get('login', '').lower() != USERNAME:
                    continue
                details = item.get('commit') or {}
                date_value = ((details.get('author') or {}).get('date'))
                message = (details.get('message') or '').splitlines()[0].strip()
                url = item.get('html_url') or ''
                if not date_value or not message or not url.startswith(f'https://github.com/{repo}/commit/'):
                    continue
                if '[skip ci]' in message.lower() or '[ci skip]' in message.lower():
                    continue
                dt = datetime.fromisoformat(date_value.replace('Z', '+00:00'))
                commits.append({'repo': repo, 'date': dt.date().isoformat(),
                                'timestamp': dt.timestamp(), 'message': message[:115], 'url': url})
    commits.sort(key=lambda event: event['timestamp'], reverse=True)
    # An empty successful response is valid and distinct from an API failure.
    sanitized = [{k: c[k] for k in ('repo', 'date', 'message', 'url')} for c in commits[:5]]
    dest = DATA / 'activity.json'
    tmp = dest.with_suffix('.json.tmp')
    tmp.write_text(json.dumps(sanitized, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    tmp.replace(dest)
    print(f'Fetched {len(sanitized)} verified public commits across {len(repos)} repositories.')


if __name__ == '__main__':
    main()
