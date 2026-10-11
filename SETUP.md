# gn1793 GitHub Profile — Text-first README

This profile uses a single original scientific hero image; **all other sections are selectable Markdown/HTML text**, not rendered SVG cards.

## Initial setup

1. Create the public GitHub repository `gn1793/gn1793` (if not already present).
2. Edit `data/profile.yaml`, `data/projects.yaml`, `data/builds.yaml`, `data/tech_stack.yaml`, and `data/publications.yaml`.
3. Install requirements and rebuild:

```bash
python3 -m pip install -r requirements.txt
python3 scripts/validate_data.py
python3 scripts/build_readme.py
python3 -m unittest discover -s tests -v
```

4. Review the generated `README.md`, then commit and push the changes in your **existing git clone**.

## Adding a Build Lab release

Add an item to `data/builds.yaml` with `id`, `title`, `description`, `repository`, `technologies`, `published_at` and `visible: true`. Set exactly one build as `featured: true`; older builds are archived automatically.

## Automatic activity

The workflow `.github/workflows/update-profile.yml` validates the data, tests the renderer, fetches recent **public** activity, updates `README.md`, and commits it only if changed. API collection errors should abort without replacing your README with stale or fabricated updates.

## From the SVG-based v2 repository

This v3 replaces `scripts/render_cards.py` and `assets/generated/*.svg` with plain text. Delete those obsolete files as part of the update. Do not delete `assets/hero.png`.

To install an archive into an existing clone, **preserve its `.git` folder** and copy the extracted contents over it. Then run `git status` and commit the changes.
