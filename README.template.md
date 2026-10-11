{% macro card_rows(items) -%}
{% for pair in items | batch(2) %}
<p>{% for card in pair %}{% if card.url %}<a href="{{ card.url | e }}">{% endif %}<img src="{{ card.src | e }}" width="50%" alt="{{ card.alt | e }}" />{% if card.url %}</a>{% endif %}{% endfor %}</p>
{% endfor %}
{%- endmacro %}
<!-- Generated file. Edit README.template.md and data/*.yaml instead. -->
<p align="center"><img src="assets/hero.png" width="100%" alt="Molecular discovery scientific hero" /></p>
<h1 align="center">{{ profile.headline | e }}</h1>
<p align="center"><strong>{{ profile.tagline | e }}</strong></p>
<p align="center">Building AI models to understand molecular interactions and predict molecular properties.</p>
<p align="center">{% for interest in profile.interests %}<code>{{ interest.title | e }}</code>{% if not loop.last %} &nbsp;·&nbsp; {% endif %}{% endfor %}</p>

---
## Research

<p><em>Exploring computational methods for drug discovery and molecular understanding</em></p>

{{ card_rows(cards.research) }}

---
## The Build Lab

*Ideas → Working Software*

{{ card_rows(cards.builds) }}
<p align="right"><a href="{{ build_collection_url | e }}">Explore All Projects →</a></p>

---
## Tools & Technologies

{{ card_rows(cards.tools) }}

---
## GitHub Stats

<p align="center">
  <img src="assets/github-stats.svg" alt="GitHub contribution stats for gn1793, automatically refreshed" width="100%" />
</p>

---
## Recent Activity

*Latest public updates across tracked projects*

{% if activity %}{{ card_rows(cards.activity) }}
{% else %}No verified public commits available yet.
{% endif %}
{% if publications %}
---
## Publications

{% for paper in publications %}- **{{ paper.title | md_text }}** ({{ paper.year }}) — {{ paper.venue | md_text }}{% if paper.doi %} · [DOI](https://doi.org/{{ paper.doi }}){% endif %}{% if paper.arxiv %} · [arXiv](https://arxiv.org/abs/{{ paper.arxiv }}){% endif %}
{% endfor %}{% endif %}
