<!-- Generated from README.template.md and data/*.yaml. Edit the sources, not README.md. -->
<p align="center">
  <img src="assets/hero.png" alt="Scientific molecular discovery banner" width="100%" />
</p>

<h1 align="center">{{ profile.headline | e }}</h1>
<p align="center"><strong>{{ profile.tagline | e }}</strong></p>
<p align="center">Building AI models to understand molecular interactions and predict molecular properties.</p>

<p align="center">
{% for interest in profile.interests %}<code>{{ interest.title | e }}</code>{% if not loop.last %} &nbsp;·&nbsp; {% endif %}{% endfor %}
</p>

---

## Featured Research

{% for project in projects %}> ### {{ '%02d' | format(loop.index) }} / {{ project.title | md_text }}
>
> {{ project.description | md_text }}
>
> {% for keyword in project.keywords %}`{{ keyword | md_code }}`{% if not loop.last %} · {% endif %}{% endfor %}{% if project.repository %}
>
> [View research repository →](https://github.com/{{ project.repository }}){% endif %}

{% if not loop.last %}{{ "\n" }}{% endif %}{% endfor %}{{ "\n" }}---

## The Build Lab

*Ideas → Working Software*

{% if latest_build %}**LATEST BUILD**

### [{{ latest_build.title | md_text }}](https://github.com/{{ latest_build.repository }}) ↗

{{ latest_build.description | md_text }}

{% for technology in latest_build.technologies %}`{{ technology | md_code }}`{% if not loop.last %} · {% endif %}{% endfor %}

[Explore repository →](https://github.com/{{ latest_build.repository }})
{{ "\n" }}{% endif %}
{% if archive_builds %}
**Previous builds**

{% for build in archive_builds %}- **[{{ build.title | md_text }}](https://github.com/{{ build.repository }})** — {{ build.description | md_text }}
{% endfor %}{{ "\n" }}{% endif %}
---

## Tools & Technologies

{% for group in display_stack %}**{{ group.name | md_text }}** · {{ group.technologies | join(', ') | md_text }}

{% endfor %}{{ "\n" }}---

## Recent Activity

{% if activity %}{% for event in activity %}- **[{{ event.repo.split('/')[-1] | md_text }}](https://github.com/{{ event.repo }})** · [{{ event.message | md_text }}]({{ event.url }}) <sub>({{ event.date | md_text }})</sub>
{% endfor %}{% else %}Recent public development updates will appear here after the next successful sync.
{% endif %}
{% if publications %}
---

## Publications

{% for paper in publications %}- **{{ paper.title | md_text }}** ({{ paper.year }}) — {{ paper.venue | md_text }}{% if paper.doi %} · [DOI](https://doi.org/{{ paper.doi }}){% endif %}{% if paper.arxiv %} · [arXiv](https://arxiv.org/abs/{{ paper.arxiv }}){% endif %}
{% endfor %}{% endif %}
