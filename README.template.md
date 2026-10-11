<!-- This README is generated. Edit README.template.md or data/*.yaml instead. -->
<p align="center">
  <img src="assets/hero.png" width="100%" alt="Original scientific illustration of molecular interactions and structure-based drug discovery" />
</p>

<h1 align="center">{{ profile.headline | e }}</h1>
<p align="center"><strong>{{ profile.tagline | e }}</strong></p>

## Research Interests

<table>
<tr>
{% for interest in profile.interests[:2] %}<td width="50%"><strong>{{ interest.title | e }}</strong><br/>{{ interest.detail | e }}</td>{% endfor %}
</tr>
<tr>
{% for interest in profile.interests[2:4] %}<td width="50%"><strong>{{ interest.title | e }}</strong><br/>{{ interest.detail | e }}</td>{% endfor %}
</tr>
</table>

## Featured Research

<table>
<tr>
{% for project in projects %}<td width="50%" valign="top">
<h3>{{ project.title | e }}</h3>
<strong>{{ project.status | e }}</strong>
<p>{{ project.description | e }}</p>
<p><small>{{ project.keywords | join(' · ') | e }}</small></p>
{% if project.repository %}<a href="https://github.com/{{ project.repository | e }}">Source code →</a>{% endif %}
</td>{% endfor %}
</tr>
</table>

## The Build Lab

*Turning ideas into working software, one project at a time.*

{% if latest_build %}
### Latest Build · {{ latest_build.title | e }}

{{ latest_build.description | e }}

**Tech:** {{ latest_build.technologies | join(' · ') | e }}  
[View repository →](https://github.com/{{ latest_build.repository }})
{% endif %}

{% if archive_builds %}
<details>
<summary><strong>Build Archive ({{ archive_builds | length }})</strong></summary>

{% for build in archive_builds %}
- **[{{ build.title | md_text }}](https://github.com/{{ build.repository }})** — {{ build.description | md_text }} ({{ build.technologies | join(', ') | md_text }})
{% endfor %}
</details>
{% endif %}

## Technical Stack

<table>
{% for group in stack.groups %}
<tr><td><strong>{{ group.name | e }}</strong></td><td>{{ group.technologies | join(' · ') | e }}</td></tr>
{% endfor %}
</table>

## Publications

{% if publications %}
{% for paper in publications %}
- **{{ paper.title | md_text }}** ({{ paper.year }}) — {{ paper.venue | md_text }}{% if paper.doi %} · [DOI](https://doi.org/{{ paper.doi }}){% endif %}{% if paper.arxiv %} · [arXiv](https://arxiv.org/abs/{{ paper.arxiv }}){% endif %}
{% endfor %}
{% else %}
Research outputs and publications will be listed here as they become publicly available.
{% endif %}

## Recent Development Activity

{% if activity %}
{% for event in activity %}
- **[{{ event.repo | md_text }}](https://github.com/{{ event.repo }})** — [{{ event.message | md_text }}]({{ event.url }}) · {{ event.date }}
{% endfor %}
{% else %}
Recent public repository updates will appear here after the first successful scheduled synchronization.
{% endif %}
