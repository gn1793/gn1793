<!-- Generated automatically. Update README.template.md and data/*.yaml. -->
<p align="center"><img src="assets/hero.png" width="100%" alt="Original scientific molecular discovery banner" /></p>

<h1 align="center">{{ profile.headline | e }}</h1>
<p align="center"><strong>{{ profile.tagline | e }}</strong></p>

## Research Interests
<table><tr>
{% for interest in profile.interests %}<td width="25%" align="center"><img src="assets/generated/interest-{{ loop.index }}.svg" width="100%" alt="{{ interest.title | e }}" /></td>{% endfor %}
</tr></table>

## Featured Research
<table><tr>
{% for project in projects %}<td width="50%" valign="top"><img src="assets/generated/research-{{ project.id }}.svg" width="100%" alt="{{ project.title | e }}" />{% if project.repository %}<br/><a href="https://github.com/{{ project.repository | e }}">Research repository ↗</a>{% endif %}</td>{% endfor %}
</tr></table>

## The Build Lab
*Turning ideas into working software, one project at a time.*

{% if latest_build %}
<a href="https://github.com/{{ latest_build.repository | e }}"><img src="assets/generated/latest-build.svg" width="100%" alt="Latest build: {{ latest_build.title | e }}" /></a>
{% endif %}

{% if archive_builds %}
<details open><summary><strong>Build Archive · {{ archive_builds | length }} released projects</strong></summary>

{% for build in archive_builds %}
<a href="https://github.com/{{ build.repository | e }}"><img src="assets/generated/archive-{{ build.id }}.svg" width="100%" alt="{{ build.title | e }} — repository" /></a>
{% endfor %}
</details>
{% endif %}

## Technical Stack
<table><tr>
{% for group in stack.groups %}<td width="20%" valign="top" align="center"><img src="assets/generated/stack-{{ loop.index }}.svg" width="100%" alt="{{ group.name | e }}: {{ group.technologies | join(', ') | e }}" /></td>{% endfor %}
</tr></table>

## Publications
{% if publications %}
{% for paper in publications %}
- **{{ paper.title | md_text }}** ({{ paper.year }}) — {{ paper.venue | md_text }}{% if paper.doi %} · [DOI](https://doi.org/{{ paper.doi }}){% endif %}{% if paper.arxiv %} · [arXiv](https://arxiv.org/abs/{{ paper.arxiv }}){% endif %}
{% endfor %}
{% else %}
> Research outputs and publications will be listed here as they become publicly available.
{% endif %}

## Recent Development Activity
{% if activity %}
{% for event in activity %}
- **[{{ event.repo | md_text }}](https://github.com/{{ event.repo }})** — [{{ event.message | md_text }}]({{ event.url }}) · {{ event.date }}
{% endfor %}
{% else %}
Recent public repository updates will appear after the first successful GitHub Actions synchronization.
{% endif %}
