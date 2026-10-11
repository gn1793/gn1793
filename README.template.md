<!-- Generated file. Edit README.template.md and data/*.yaml instead. -->
<p align="center"><img src="assets/hero.png" width="100%" alt="Molecular discovery scientific hero" /></p>
<h1 align="center">{{ profile.headline | e }}</h1>
<p align="center"><strong>{{ profile.tagline | e }}</strong></p>
<p align="center">Building AI models to understand molecular interactions and predict molecular properties.</p>
<p align="center">{% for interest in profile.interests %}<code>{{ interest.title | e }}</code>{% if not loop.last %} &nbsp;·&nbsp; {% endif %}{% endfor %}</p>

---
## Featured Research

<p><em>Exploring computational methods for drug discovery and molecular understanding</em></p>

<table width="100%">
<tr>
{% for project in projects[:2] %}
<td width="50%" valign="top">
<sub>{{ '%02d' | format(loop.index) }} / {% if loop.first %}RESEARCH PROJECT{% else %}RESEARCH PROJECT{% endif %}</sub>
<h3>{% if project.repository %}<a href="https://github.com/{{ project.repository | e }}">{{ project.title | e }}</a>{% else %}{{ project.title | e }}{% endif %}</h3>
<p>{{ project.description | e }}</p>
{% if loop.first %}<br>{% endif %}
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

<table width="100%">
<tr>
{% if latest_build %}
<td width="50%" valign="top">
<sub>01 / FEATURED PROJECT</sub>
<h3><a href="https://github.com/{{ latest_build.repository | e }}">{{ latest_build.title | e }}</a></h3>
<p>{{ latest_build.description | e }}</p>
<br>
<p>{% for tech in latest_build.technologies %}<code>{{ tech | e }}</code> {% endfor %}</p>
<p><a href="https://github.com/{{ latest_build.repository | e }}">View repository ↗</a></p>
</td>
{% endif %}
{% if previous_build %}
<td width="50%" valign="top">
<sub>02 / DEVELOPER UTILITY</sub>
<h3><a href="https://github.com/{{ previous_build.repository | e }}">{{ previous_build.title | e }}</a></h3>
<p>{{ previous_build.description | e }}</p>
<br>
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
<tr>
<td width="50%" valign="top">
<sub>01 / TOOLKIT</sub>
<h3>Languages</h3>
<p><em>Core languages for research workflows and application development.</em></p>
<p><code>Python</code> <code>Swift</code></p>
</td>
<td width="50%" valign="top">
<sub>02 / TOOLKIT</sub>
<h3>Deep Learning</h3>
<p><em>Frameworks for geometric learning and model development.</em></p>
<p><code>PyTorch</code> <code>PyTorch Geometric</code></p>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<sub>03 / TOOLKIT</sub>
<h3>Molecular</h3>
<p><em>Libraries for cheminformatics and molecular structure handling.</em></p>
<p><code>RDKit</code> <code>Biopython</code> <code>Cheminformatics</code></p>
</td>
<td width="50%" valign="top">
<sub>04 / TOOLKIT</sub>
<h3>Engineering</h3>
<p><em>Infrastructure and tooling for reproducible development.</em></p>
<p><code>GitHub</code> <code>Linux</code></p>
</td>
</tr>
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
<td width="50%" valign="top">
<sub>{{ '%02d' | format(loop.index) }} / {% if loop.first %}LATEST UPDATE{% else %}RECENT UPDATE{% endif %} &nbsp;·&nbsp; {{ event.date | e }}</sub>
<h3><a href="https://github.com/{{ event.repo | e }}">{{ event.repo.split('/')[-1] | e }}</a></h3>
<p>{{ event.message | e }}</p>
<br>
<br>
<p><a href="{{ event.url | e }}">View commit ↗</a></p>
<br>
</td>
{% endfor %}
{% if activity[:2] | length == 1 %}<td width="50%"></td>{% endif %}
</tr>
</table>
{% else %}No verified public commits available yet.
{% endif %}
{% if publications %}
---
## Publications

{% for paper in publications %}- **{{ paper.title | md_text }}** ({{ paper.year }}) — {{ paper.venue | md_text }}{% if paper.doi %} · [DOI](https://doi.org/{{ paper.doi }}){% endif %}{% if paper.arxiv %} · [arXiv](https://arxiv.org/abs/{{ paper.arxiv }}){% endif %}
{% endfor %}{% endif %}
