<!-- Generated file. Edit README.template.md and data/*.yaml instead. -->
<p align="center"><img src="assets/hero.png" width="100%" alt="Molecular discovery scientific hero" /></p>

<h1 align="center">{{ profile.headline | e }}</h1>
<p align="center"><strong>{{ profile.tagline | e }}</strong></p>
<p align="center">Building AI models to understand molecular interactions and predict molecular properties.</p>
<p align="center">{% for interest in profile.interests %}<code>{{ interest.title | e }}</code>{% if not loop.last %} &nbsp;·&nbsp; {% endif %}{% endfor %}</p>

---

## Featured Research

{% for project in projects %}> **{{ '%02d' | format(loop.index) }} / {{ project.title | md_text }}**
>
> {{ project.description | md_text }}
>
> {% for keyword in project.keywords %}`{{ keyword | md_code }}`{% if not loop.last %} · {% endif %}{% endfor %}{% if project.repository %}
>
> [View repository →](https://github.com/{{ project.repository }}){% endif %}

{% endfor %}---

## The Build Lab

*Ideas → Working Software*

<table width="100%">
{% if latest_build %}  <tr><td width="100%">
    <p><strong>● LATEST BUILD</strong></p>
    <h3><a href="https://github.com/{{ latest_build.repository | e }}">{{ latest_build.title | e }} ↗</a></h3>
    <p>{{ latest_build.description | e }}</p>
    <p>{% for tech in latest_build.technologies %}<code>{{ tech | e }}</code>{% if not loop.last %} &nbsp; {% endif %}{% endfor %}</p>
    <p><a href="https://github.com/{{ latest_build.repository | e }}"><strong>View Latest Build ↗</strong></a></p>
  </td></tr>
{% endif %}{% if previous_build %}  <tr><td width="100%">
    <p><strong>PREVIOUS BUILD</strong></p>
    <h3><a href="https://github.com/{{ previous_build.repository | e }}">{{ previous_build.title | e }} ↗</a></h3>
    <p>{{ previous_build.description | e }}</p>
    <p>{% for tech in previous_build.technologies %}<code>{{ tech | e }}</code>{% if not loop.last %} &nbsp; {% endif %}{% endfor %}</p>
  </td></tr>
{% endif %}  <tr><td width="100%">
    <h3><a href="{{ build_collection_url | e }}">Build Collection →</a></h3>
    <p>Explore experiments, applications, and developer tools.</p>
    <p><a href="{{ build_collection_url | e }}">View all builds ↗</a></p>
  </td></tr>
</table>

---

## Tools & Technologies

| Category | Technologies |
| :--- | :--- |
{% for group in badge_stack %}| **{{ group.name | md_cell }}** | {% for badge in group.badges %}![{{ badge.label | md_text }}]({{ badge.url }}){% if not loop.last %} {% endif %}{% endfor %} |
{% endfor %}
---

## GitHub Stats

| Metric | Public GitHub data |
| :--- | ---: |
| ⭐ Public repositories | **{{ stats.public_repos if stats else '—' }}** |
| ⭐ Stars received | **{{ stats.stars_received if stats else '—' }}** |
| Followers | **{{ stats.followers if stats else '—' }}** |
| Following | **{{ stats.following if stats else '—' }}** |
{% if not stats %}<sub>Stats pending: run the GitHub Actions “Update Profile README” workflow or `python3 scripts/fetch_stats.py` to populate verified public counts.</sub>
{% else %}<sub>Public GitHub API data · refreshed by GitHub Actions. Private activity is not included.</sub>
{% endif %}

---

## Recent Activity

{% if activity %}{% for event in activity %}- **[{{ event.repo.split('/')[-1] | md_text }}](https://github.com/{{ event.repo }})** · [{{ event.message | md_text }}]({{ event.url }}) <sub>({{ event.date | md_text }})</sub>
{% endfor %}{% else %}Recent public development updates will appear after the next successful sync.
{% endif %}
{% if publications %}
---

## Publications

{% for paper in publications %}- **{{ paper.title | md_text }}** ({{ paper.year }}) — {{ paper.venue | md_text }}{% if paper.doi %} · [DOI](https://doi.org/{{ paper.doi }}){% endif %}{% if paper.arxiv %} · [arXiv](https://arxiv.org/abs/{{ paper.arxiv }}){% endif %}
{% endfor %}{% endif %}
