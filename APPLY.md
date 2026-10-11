# v5 update patch

Keep your existing Git repository and `assets/hero.png`. Extract these files into the existing clone; do not replace the `.git` directory.

```bash
cd ~
# If not already cloned:
# git clone https://github.com/gn1793/gn1793.git ~/gn1793-profile
cd ~/gn1793-profile
unzip -o ~/Downloads/gn1793-profile-v5-patch.zip -d .
python3 scripts/build_readme.py
python3 -m unittest discover -s tests -v
git add -A
git commit -m "feat: build lab, technology badges and public stats"
git push origin main
```

Then run `Update Profile README` in GitHub Actions to fetch public stats and activity. API failure leaves existing README intact. The GitHub interface cannot render exact custom rounded cards or a non-image circular grade using Markdown/HTML alone.
