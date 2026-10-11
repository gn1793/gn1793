<!-- Generated file. Edit README.template.md and data/*.yaml instead. -->
<p align="center"><img src="assets/hero.png" width="100%" alt="Molecular discovery scientific hero" /></p>
<h1 align="center">{{ profile.headline | e }}</h1>
<p align="center"><strong>{{ profile.tagline | e }}</strong></p>
<p align="center">Building AI models to understand molecular interactions and predict molecular properties.</p>
<p align="center">{% for interest in profile.interests %}<code>{{ interest.title | e }}</code>{% if not loop.last %} &nbsp;·&nbsp; {% endif %}{% endfor %}</p>

---
## Featured Research

<table width="100%">
<tr>
{% for project in projects %}
<td width="50%" valign="top">
<sub>{{ '%02d' | format(loop.index) }} / {% if loop.index == 1 %}STRUCTURE-BASED DRUG DISCOVERY{% else %}MOLECULAR PROPERTY PREDICTION{% endif %}</sub>
<h3>{{ project.title | e }}</h3>
<p>{{ project.description | e }}</p>
<p>{% for keyword in project.keywords %}<code>{{ keyword | e }}</code> {% endfor %}</p>
<p><sub>Status: {{ project.status | e }}</sub></p>
{% if project.repository %}<p><a href="https://github.com/{{ project.repository | e }}">View repository ↗</a></p>{% endif %}
</td>
{% if loop.index is even and not loop.last %}</tr><tr>{% endif %}
{% endfor %}
</tr>
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

| Category | Technologies |
| :--- | :--- |
{% for group in badge_stack %}| **{{ group.name | md_cell }}** | {% for badge in group.badges %}`{{ badge.label | md_code }}`{% if not loop.last %} · {% endif %}{% endfor %} |
{% endfor %}

---
## GitHub Stats

<p align="center">
  <img src="assets/github-stats.svg" alt="GitHub contribution stats for gn1793, automatically refreshed" width="760" />
</p>

---
## Recent Activity

*Latest public updates across tracked projects*

{% if activity %}<table width="100%">
<tr><th align="left">Repository</th><th align="left">Update</th><th align="right">Date</th></tr>
{% for event in activity %}<tr><td><a href="https://github.com/{{ event.repo | e }}">{{ event.repo.split('/')[-1] | e }}</a></td><td><a href="{{ event.url | e }}">{{ event.message | e }} ↗</a></td><td align="right"><code>{{ event.date | e }}</code></td></tr>
{% endfor %}</table>
{% else %}No verified public commits available yet.
{% endif %}
{% if publications %}
---
## Publications

{% for paper in publications %}- **{{ paper.title | md_text }}** ({{ paper.year }}) — {{ paper.venue | md_text }}{% if paper.doi %} · [DOI](https://doi.org/{{ paper.doi }}){% endif %}{% if paper.arxiv %} · [arXiv](https://arxiv.org/abs/{{ paper.arxiv }}){% endif %}
{% endfor %}{% endif %}
