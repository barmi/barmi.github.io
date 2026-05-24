# barmi.github.io

개인 홈페이지 — <https://barmi.github.io>

[Sphinx](https://www.sphinx-doc.org) + [Furo](https://pradyunsg.me/furo/) 테마 + [MyST](https://myst-parser.readthedocs.io/)(Markdown)로 작성하고, GitHub Actions로 자동 배포합니다.

## 디렉터리 구조

```
.
├── docs/                 # Sphinx 소스
│   ├── conf.py           # Sphinx 설정
│   ├── index.md          # 홈
│   ├── about.md          # 소개
│   ├── posts/            # 글 목록
│   ├── _static/          # 정적 파일 (custom.css 등)
│   └── _build/           # 빌드 산출물 (gitignored)
├── .github/workflows/
│   └── deploy.yml        # GitHub Pages 자동 배포
├── pyproject.toml        # uv 의존성
└── Makefile              # 자주 쓰는 명령
```

## 로컬에서 실행

```sh
# 의존성 설치 (최초 1회)
make install   # 또는: uv sync

# 정적 HTML 빌드 → docs/_build/html
make html

# 로컬 미리보기 (자동 새로고침; sphinx-autobuild 필요)
uv add --dev sphinx-autobuild   # 최초 1회
make serve
```

## 글 추가하기

1. `docs/posts/` 안에 `slug.md` 파일을 만든다.
2. 상단에 메타데이터를 적는다.

   ```markdown
   ---
   date: 2026-05-24
   ---

   # 제목

   본문...
   ```

3. `docs/posts/index.md`의 `toctree`에 파일 이름(확장자 제외)을 추가한다.

## GitHub Pages 배포

`main` 브랜치에 푸시하면 `.github/workflows/deploy.yml`이 자동으로 Sphinx 사이트를 빌드해 GitHub Pages에 배포합니다.

**최초 한 번**, 저장소 설정에서 Pages 소스를 바꿔야 합니다.

1. <https://github.com/barmi/barmi.github.io/settings/pages>
2. **Source**: `GitHub Actions` 선택

이후로는 푸시 → 자동 배포가 됩니다. 배포 진행 상황은 [Actions 탭](https://github.com/barmi/barmi.github.io/actions)에서 확인할 수 있습니다.

## 커스텀 도메인 (선택)

`docs/_static/CNAME` 파일에 도메인을 한 줄로 적으면 빌드 시 자동으로 사이트 루트에 포함됩니다. 도메인 DNS에서 CNAME → `barmi.github.io`을 설정하면 됩니다.
