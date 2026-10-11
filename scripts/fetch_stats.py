"""Refresh public profile metrics; GraphQL contributions need GH_TOKEN.

Errors to the contribution endpoint leave those metrics unreported, never faked.
A failure of the essential REST endpoints aborts without overwriting the cache.
"""
import json
import os
import requests
from common import DATA

API = 'https://api.github.com'
USERNAME = 'gn1793'
QUERY = '''query($login:String!) {
 user(login:$login) {
  contributionsCollection {
   totalCommitContributions
   totalPullRequestContributions
   totalIssueContributions
   contributionCalendar { totalContributions }
  }
 }
}'''


def main():
    token = os.environ.get('GH_TOKEN')
    headers = {'Accept': 'application/vnd.github+json', 'X-GitHub-Api-Version': '2022-11-28'}
    if token:
        headers['Authorization'] = f'Bearer {token}'
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
        payload = dict(public_repos=int(user['public_repos']), stars_received=int(stars),
                       followers=int(user['followers']), following=int(user['following']))
        if token:
            try:
                gql = session.post(f'{API}/graphql', json={'query': QUERY, 'variables': {'login': USERNAME}}, timeout=20)
                gql.raise_for_status()
                body = gql.json()
                if body.get('errors'):
                    raise ValueError(body['errors'])
                coll = body['data']['user']['contributionsCollection']
                payload.update({
                    'commit_contributions_12m': int(coll['totalCommitContributions']),
                    'pr_contributions_12m': int(coll['totalPullRequestContributions']),
                    'issue_contributions_12m': int(coll['totalIssueContributions']),
                    'total_contributions_12m': int(coll['contributionCalendar']['totalContributions']),
                })
            except (requests.RequestException, KeyError, TypeError, ValueError) as exc:
                print(f'Contribution counts unavailable; showing N/A: {exc}')
        else:
            print('GH_TOKEN absent: contribution metrics will show N/A.')
    dest = DATA / 'github_stats.json'
    temp = dest.with_suffix('.json.tmp')
    temp.write_text(json.dumps(payload, indent=2) + '\n', encoding='utf-8')
    temp.replace(dest)
    print(f'Public GitHub stats updated: {payload}')


if __name__ == '__main__':
    main()
