<!-- Generated from README.template.md and data/*.yaml. Edit the sources, not README.md. -->
<p align="center">
  <img src="assets/hero.png" alt="Scientific molecular discovery banner" width="100%" />
</p>

<h1 align="center">{{ profile.headline | e }}</h1>
<p align="center"><strong>{{ profile.tagline | e }}</strong></p>

---

## Research Interests

| Research area | Focus |
| :--- | :--- |
{% for interest in profile.interests %}| **{{ interest.title | md_cell }}** | {{ interest.detail | md_cell }} |
{% endfor %}

## Featured Research

| {% for project in projects %}{{ project.title | md_cell }}{% if not loop.last %} | {% endif %}{% endfor %} |
| {% for project in projects %}:---{% if not loop.last %} | {% endif %}{% endfor %} |
| {% for project in projects %}**{{ project.status | md_cell }}**<br>{{ project.description | md_cell }}<br><br>{% for keyword in project.keywords %}`{{ keyword | md_cell }}` {% endfor %}{% if project.repository %}<br>[View research repository →](https://github.com/{{ project.repository }}){% endif %}{% if not loop.last %} | {% endif %}{% endfor %} |

## The Build Lab

*Turning ideas into working software, one project at a time.*

{% if latest_build %}
### Latest Build · {{ latest_build.title | md_text }}

{{ latest_build.description | md_text }}

**Built with:** {{ latest_build.technologies | join(' · ') | md_text }}

**[View project on GitHub →](https://github.com/{{ latest_build.repository }})**
{% endif %}

{% if archive_builds %}
<details open>
<summary><strong>Build Archive ({{ archive_builds | length }})</strong></summary>

| Project | Description | Technologies |
| :--- | :--- | :--- |
{% for build in archive_builds %}| **[{{ build.title | md_cell }}](https://github.com/{{ build.repository }})** | {{ build.description | md_cell }} | {{ build.technologies | join(' · ') | md_cell }} |
{% endfor %}
</details>
{% endif %}

## Technical Stack

| Category | Technologies & Methods |
| :--- | :--- |
{% for group in stack.groups %}| **{{ group.name | md_cell }}** | {{ group.technologies | join(' · ') | md_cell }} |
{% endfor %}

## Publications

{% if publications %}
{% for paper in publications %}- **{{ paper.title | md_text }}** ({{ paper.year }}) — {{ paper.venue | md_text }}{% if paper.doi %} · [DOI](https://doi.org/{{ paper.doi }}){% endif %}{% if paper.arxiv %} · [arXiv](https://arxiv.org/abs/{{ paper.arxiv }}){% endif %}
{% endfor %}
{% else %}
Research outputs and publications will be listed here as they become publicly available.
{% endif %}

## Recent Development Activity

{% if activity %}
| Repository | Latest update | Date |
| :--- | :--- | :--- |
{% for event in activity %}| [{{ event.repo | md_cell }}](https://github.com/{{ event.repo }}) | [{{ event.message | md_cell }}]({{ event.url }}) | {{ event.date | md_cell }} |
{% endfor %}
{% else %}
Public development updates will appear after GitHub Actions syncs recent commits.
{% endif %}
