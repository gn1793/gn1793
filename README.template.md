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
> [View repository →](https://github.com/{{ project.repository }}){% endif %}{{ '\n\n' }}
{% endfor %}
---

## The Build Lab

*Ideas → Working Software*

<table width="100%">
{% if latest_build %}<tr><td width="100%" align="left">
<strong>01 / LATEST BUILD</strong>
<br/><br/>
<strong><a href="https://github.com/{{ latest_build.repository }}">{{ latest_build.title | e }}</a></strong>
<br/>
{{ latest_build.description | e }}
<br/><br/>
{% for tech in latest_build.technologies %}<code>{{ tech | e }}</code>{% if not loop.last %} &nbsp;·&nbsp; {% endif %}{% endfor %}
<br/><br/>
<a href="https://github.com/{{ latest_build.repository }}">View repository ↗</a>
</td></tr>
{% endif %}{% if previous_build %}<tr><td width="100%" align="left">
<strong>02 / PREVIOUS BUILD</strong>
<br/><br/>
<strong><a href="https://github.com/{{ previous_build.repository }}">{{ previous_build.title | e }}</a></strong>
<br/>
{{ previous_build.description | e }}
<br/><br/>
{% for tech in previous_build.technologies %}<code>{{ tech | e }}</code>{% if not loop.last %} &nbsp;·&nbsp; {% endif %}{% endfor %}
<br/><br/>
<a href="https://github.com/{{ previous_build.repository }}">View repository ↗</a>
</td></tr>
{% endif %}<tr><td width="100%" align="left">
<strong>03 / <a href="{{ build_collection_url }}">Build Collection ↗</a></strong>
<br/><br/>
Explore experiments, applications, and developer tools.
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

<p align="center">
  <img src="assets/github-stats.svg" alt="GitHub contribution stats for gn1793, automatically refreshed" width="760" />
</p>


---

## Recent Activity

*Latest public updates across tracked projects*

{% if activity %}{% for event in activity %}> **{{ '%02d' | format(loop.index) }} / [{{ event.repo.split('/')[-1] | md_text }}](https://github.com/{{ event.repo }})**
>
> {{ event.message | md_text }}
>
> `{{ event.date | md_code }}` &nbsp;·&nbsp; [View commit ↗]({{ event.url }})

{% endfor %}{% else %}No verified public commits available yet.

{% endif %}
{% if publications %}
---

## Publications

{% for paper in publications %}- **{{ paper.title | md_text }}** ({{ paper.year }}) — {{ paper.venue | md_text }}{% if paper.doi %} · [DOI](https://doi.org/{{ paper.doi }}){% endif %}{% if paper.arxiv %} · [arXiv](https://arxiv.org/abs/{{ paper.arxiv }}){% endif %}
{% endfor %}{% endif %}
