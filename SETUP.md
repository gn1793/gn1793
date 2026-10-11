# Setup / 운영 가이드

## 최초 적용
1. GitHub에서 공개 저장소 **gn1793/gn1793**를 만들고 기본 branch를 `main`으로 설정합니다.
2. 이 폴더의 파일들을 저장소 루트에 업로드합니다. (`README.md`, 숨김 폴더 `.github/` 포함)
3. GitHub → Repository Settings → Actions → General → Workflow permissions에서 **Read and write permissions**를 허용합니다. 조직/저장소 정책이 더 엄격하면 관리자 설정이 필요합니다.
4. Actions → **Update Profile README** → **Run workflow** 를 한번 실행합니다.
5. `https://github.com/gn1793` Overview에서 렌더링을 확인합니다.

## 로컬 테스트
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python scripts/validate_data.py
python -m unittest discover -s tests -v
python scripts/build_readme.py
# 선택: 인터넷 연결 및 GitHub public API 사용
python scripts/fetch_activity.py
python scripts/build_readme.py
```

## 새 개발작 추가
- `data/builds.yaml`에 새 항목을 등록합니다. `published_at`에 실제 공개 날짜(YYYY-MM-DD)를 기록합니다.
- 최신 프로젝트에만 `featured: true`를 지정하고 이전 항목은 `featured: false`로 변경합니다.
- `featured`를 모두 false로 설정하면 공개 날짜순으로 최신 항목이 자동 선정됩니다.
- 개발 기록은 공개된 저장소만 대상으로 수집합니다. README 자체 생성 커밋은 수집하지 않습니다.

## 연구·논문 업데이트
- 연구 정보는 `data/projects.yaml`, 연구 관심사는 `data/profile.yaml`을 편집합니다.
- 논문은 `data/publications.yaml`의 빈 배열을 아래 예시로 교체합니다.
```yaml
publications:
  - title: Example paper title
    year: 2026
    venue: Example journal
    doi: "10.xxxx/example"
    arxiv: null
    visible: true
```
- 비공개 연구의 링크나 지표는 공개 승인 전까지 넣지 마세요.

## 운영 주의사항
- Actions의 schedule은 항상 정시 실행을 보장하지 않습니다.
- GitHub API 응답 실패 시 workflow가 실패하며 기존 README는 유지됩니다.
- 공개 repository의 commit author가 GitHub 계정으로 확인된 경우만 활동 항목에 기록됩니다.
- GitHub README의 HTML은 일부 제한됩니다. CSS/JS를 사용하지 않으며 GitHub 기본 HTML table과 Markdown만 사용합니다.
- SVG/배너는 향후 실제 연구 구조 데이터로 대체 가능합니다. 현재 Hero는 직접 생성한 이미지입니다.

## v2 visual cards

`python scripts/build_readme.py` now also generates self-contained SVG cards in
`assets/generated/`. Commit these cards together with `README.md`; they are
needed for GitHub to display the visual profile. The scheduled GitHub Action
commits both automatically. The files are deterministic and do not require
external image hosts or remote icon resources.

To change text, update `data/*.yaml`, then run the generator. To change
appearance, edit `scripts/render_cards.py`. Custom layout is limited by
GitHub's Markdown renderer; this is a static SVG approximation of the design
mockup, not a fully interactive HTML/CSS page.

### Upgrade existing profile repository

Copy the contents of this v2 folder over your existing checkout (do not copy
or replace `.git`). From the existing checkout, run:

```bash
python3 -m pip install -r requirements.txt
python3 scripts/validate_data.py
python3 scripts/build_readme.py
python3 -m unittest discover -s tests -v
git add README.md README.template.md scripts/ tests/ assets/generated/ .github/workflows/ SETUP.md
git commit -m "feat: add scientific SVG profile cards"
git push origin main
```
