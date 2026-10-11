<!-- Generated file. Edit README.template.md and data/*.yaml instead. -->
<p align="center"><img src="assets/hero.png" width="100%" alt="Molecular discovery scientific hero" /></p>
<h1 align="center">{{ profile.headline | e }}</h1>
<p align="center"><strong>{{ profile.tagline | e }}</strong></p>
<p align="center">Building AI models to understand molecular interactions and predict molecular properties.</p>
<p align="center">{% for interest in profile.interests %}<code>{{ interest.title | e }}</code>{% if not loop.last %} &nbsp;·&nbsp; {% endif %}{% endfor %}</p>

---
## Featured Research

<table width="100%">
{% for pair in projects | batch(2) %}
{% set pair_index = loop.index0 %}
<tr>
{% for project in pair %}
<td width="50%" valign="top">
<sub>{{ '%02d' | format(pair_index * 2 + loop.index) }} / {% if pair_index * 2 + loop.index == 1 %}STRUCTURE-BASED DRUG DISCOVERY{% else %}MOLECULAR PROPERTY PREDICTION{% endif %}</sub>
<h3>{{ project.title | e }}</h3>
<p>{{ project.description | e }}</p>
</td>
{% endfor %}
</tr>
<tr>
{% for project in pair %}
<td width="50%" valign="bottom">
<p>{% for keyword in project.keywords %}<code>{{ keyword | e }}</code> {% endfor %}</p>
<p><sub>Status: {{ project.status | e }}</sub></p>
{% if project.repository %}<p><a href="https://github.com/{{ project.repository | e }}">View repository ↗</a></p>{% endif %}
</td>
{% endfor %}
</tr>
{% endfor %}
</table>

---
## The Build Lab

*Ideas → Working Software*

<table width="100%">
<tr>
{% if latest_build %}
<td width="50%" valign="top">
<sub>01 / FEATURED PROJECT</sub>
<h3><a href="https://github.com/{{ latest_build.repository | e }}">{{ latest_build.title | e }}</a></h3>
<p>{{ latest_build.description | e }}</p>
<p>{% for tech in latest_build.technologies %}<code>{{ tech | e }}</code> {% endfor %}</p>
<p><a href="https://github.com/{{ latest_build.repository | e }}">View repository ↗</a></p>
</td>
{% endif %}
{% if previous_build %}
<td width="50%" valign="top">
<sub>02 / DEVELOPER UTILITY</sub>
<h3><a href="https://github.com/{{ previous_build.repository | e }}">{{ previous_build.title | e }}</a></h3>
<p>{{ previous_build.description | e }}</p>
<p>{% for tech in previous_build.technologies %}<code>{{ tech | e }}</code> {% endfor %}</p>
<p><a href="https://github.com/{{ previous_build.repository | e }}">View repository ↗</a></p>
</td>
{% endif %}
</tr>
</table>
<p align="right"><a href="{{ build_collection_url | e }}">Explore All Projects →</a></p>

---
## Tools & Technologies

<table width="100%">
{% for pair in badge_stack | batch(2) %}
{% set row_number = loop.index %}
<tr>
{% for group in pair %}
<td width="50%" valign="top">
<br>
<sub>{{ '%02d' | format((row_number - 1) * 2 + loop.index) }} / TOOLKIT</sub>
<h3>{{ group.name | e }}</h3>
<p>{% for badge in group.badges %}<code>{{ badge.label | e }}</code> {% endfor %}</p>
<br>
</td>
{% endfor %}
{% if pair | length == 1 %}<td width="50%"></td>{% endif %}
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
{% for event in activity %}<tr>
<td width="100%" valign="top">
<br>
<sub>{{ '%02d' | format(loop.index) }} / {% if loop.first %}LATEST UPDATE{% else %}RECENT UPDATE{% endif %} &nbsp;·&nbsp; {{ event.date | e }}</sub>
<h3><a href="https://github.com/{{ event.repo | e }}">{{ event.repo.split('/')[-1] | e }}</a></h3>
<p>{{ event.message | e }}</p>
<p><a href="{{ event.url | e }}">View commit ↗</a></p>
<br>
</td>
</tr>
{% endfor %}</table>
{% else %}No verified public commits available yet.
{% endif %}
{% if publications %}
---
## Publications

{% for paper in publications %}- **{{ paper.title | md_text }}** ({{ paper.year }}) — {{ paper.venue | md_text }}{% if paper.doi %} · [DOI](https://doi.org/{{ paper.doi }}){% endif %}{% if paper.arxiv %} · [arXiv](https://arxiv.org/abs/{{ paper.arxiv }}){% endif %}
{% endfor %}{% endif %}
