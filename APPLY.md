# v4 Profile Patch

Only updated README/template/renderer/tests are included. Extract these files **into the existing Git clone** so `.git` stays intact.

```bash
cd ~/Downloads/gn1793-profile
unzip -o ~/Downloads/gn1793-profile-v4-update.zip -d .
python3 scripts/build_readme.py
python3 -m unittest discover -s tests -v
git add README.md README.template.md scripts/build_readme.py tests/test_profile.py
git commit -m "style: streamline profile layout v4"
git push origin main
```

No SVG cards are generated. The original `assets/hero.png`, YAML, and GitHub Actions stay unchanged.
