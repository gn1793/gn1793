<!-- Generated file. Edit README.template.md and data/*.yaml instead. -->
<p align="center"><img src="assets/hero.png" width="100%" alt="Molecular discovery scientific hero" /></p>
<h1 align="center">{{ profile.headline | e }}</h1>
<p align="center"><strong>{{ profile.tagline | e }}</strong></p>
<p align="center">Building AI models to understand molecular interactions and predict molecular properties.</p>
<p align="center">{% for interest in profile.interests %}<code>{{ interest.title | e }}</code>{% if not loop.last %} &nbsp;·&nbsp; {% endif %}{% endfor %}</p>

---
## Research

<p><em>Exploring computational methods for drug discovery and molecular understanding</em></p>

<table width="100%">
<tr>
{% for project in projects[:2] %}
<td width="450" valign="top">
<sub>{{ '%02d' | format(loop.index) }} / {% if loop.first %}RESEARCH PROJECT{% else %}RESEARCH PROJECT{% endif %}</sub>
<h3>{% if project.repository %}<a href="https://github.com/{{ project.repository | e }}">{{ project.title | e }}</a>{% else %}{{ project.title | e }}{% endif %}</h3>
<p>{{ project.description | e }}</p>
<p>{% for keyword in project.keywords %}<code>{{ keyword | e }}</code> {% endfor %}</p>
<p><sub>Status: {{ project.status | e }}</sub></p>
{% if project.repository %}<p><a href="https://github.com/{{ project.repository | e }}">View repository ↗</a></p>{% endif %}
</td>
{% endfor %}
</tr>
</table>

---
## The Build Lab

*Ideas → Working Software*

{% set builds = [latest_build, previous_build] %}
<table width="100%">
<tr>
{% for build in builds %}
<td width="450" valign="top">
{% if build %}
<sub>{{ '%02d' | format(loop.index) }} / {% if loop.first %}FEATURED PROJECT{% else %}DEVELOPER UTILITY{% endif %}</sub>
<h3><a href="https://github.com/{{ build.repository | e }}">{{ build.title | e }}</a></h3>
<p>{{ build.description | e }}</p>
{% endif %}
</td>
{% endfor %}
</tr>
<tr>
{% for build in builds %}
<td width="450" valign="bottom">
{% if build %}
<p>{% for tech in build.technologies %}<code>{{ tech | e }}</code> {% endfor %}</p>
<p><a href="https://github.com/{{ build.repository | e }}">View repository ↗</a></p>
{% endif %}
</td>
{% endfor %}
</tr>
</table>
<p align="right"><a href="{{ build_collection_url | e }}">Explore All Projects →</a></p>

---
## Tools & Technologies

<table width="100%">
{% for pair in badge_stack | batch(2) %}
<tr>
{% for group in pair %}
<td width="450" valign="top">
<strong>{{ group.name | e }}</strong><br>
{% for badge in group.badges %}<code>{{ badge.label | e }}</code> {% endfor %}
</td>
{% endfor %}
{% if pair | length == 1 %}<td width="450"></td>{% endif %}
</tr>
{% endfor %}
</table>

---
## GitHub Stats

<p align="center">
  <img src="assets/github-stats.svg" alt="GitHub contribution stats for gn1793, automatically refreshed" width="760" />
</p>

---
## Recent Activity

*Latest public updates across tracked projects*

{% if activity %}<table width="100%">
<tr>
{% for event in activity[:2] %}
<td width="450" valign="top">
<sub>{{ '%02d' | format(loop.index) }} / {% if loop.first %}LATEST UPDATE{% else %}RECENT UPDATE{% endif %} &nbsp;·&nbsp; {{ event.date | e }}</sub>
<h3><a href="https://github.com/{{ event.repo | e }}">{{ event.repo.split('/')[-1] | e }}</a></h3>
<p>{{ event.message | e }}</p>
</td>
{% endfor %}
{% if activity[:2] | length == 1 %}<td width="450"></td>{% endif %}
</tr>
<tr>
{% for event in activity[:2] %}
<td width="450" valign="bottom">
<p><a href="{{ event.url | e }}">View commit ↗</a></p>
</td>
{% endfor %}
{% if activity[:2] | length == 1 %}<td width="450"></td>{% endif %}
</tr>
</table>
{% else %}No verified public commits available yet.
{% endif %}
{% if publications %}
---
## Publications

{% for paper in publications %}- **{{ paper.title | md_text }}** ({{ paper.year }}) — {{ paper.venue | md_text }}{% if paper.doi %} · [DOI](https://doi.org/{{ paper.doi }}){% endif %}{% if paper.arxiv %} · [arXiv](https://arxiv.org/abs/{{ paper.arxiv }}){% endif %}
{% endfor %}{% endif %}
