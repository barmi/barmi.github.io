---
myst:
  html_meta:
    description: barmi가 작성/관리하는 프로젝트와 학습 노트의 분류 목록
---

# 프로젝트

지금까지 만들었거나 유지하고 있는 작업을 분야별로 정리합니다. 각 항목은 [GitHub @barmi](https://github.com/barmi) 저장소로 연결됩니다.

> 공개 저장소 약 135개(직접 작성 ~69 / fork ~66). 가장 오래된 직접 저장소는 2012년, 가장 최근은 2026-05.

```{toctree}
:maxdepth: 1
:hidden:

active
games
mobile
embedded
system
security
network
backend
teaching
library
notes
```

## Featured

::::{grid} 1 2 3 3
:gutter: 3

:::{grid-item-card} 🛡️ cve-patch-auditor
:link: https://github.com/barmi/cve-patch-auditor

**Go · 2026-05 · 3⭐**

시스템별 CVE 영향도·패치 상태·조치 진행·결과 검증을 **단일 Go 바이너리**로 자동화하는 CLI 감사 도구. 6개 CVE(커널 LPE 4 + Apache HTTP/2 + ptrace LPE) 임시조치 자동화.
:::

:::{grid-item-card} 🪐 orbitarium
:link: https://github.com/barmi/orbitarium

**TypeScript · 2026-05**

JPL Horizons + SPICE/DE440 ephemeris 기반 정밀 태양계 시뮬레이터. React 19 + r3f + three.js + Playwright.
:::

:::{grid-item-card} 🧠 bxos
:link: https://github.com/barmi/bxos

**C · 2012–2026 (13년)**

한신대 운영체제 강의용 OS. 가장 오래되고 지금도 유지되는 자산.
:::

:::{grid-item-card} 📦 htmlcxx
:link: https://github.com/barmi/htmlcxx

**C++ · 17⭐ · fork 5**

C++ HTML/CSS 파서. barmi 계정 최다 star/fork 라이브러리. htmlcxx.sourceforge.net 클론·미러.
:::

:::{grid-item-card} 🧩 js-tetris-3d
:link: https://github.com/barmi/js-tetris-3d

**JavaScript · 2026-05**

3D 테트리스(Blockout 클론). PWA 오프라인, AI 자동 플레이(AP), OrbitControls, 4테마, 색맹 친화 팔레트. 빌드 도구 없는 ES Modules.
:::

:::{grid-item-card} 🎱 js-billiards-3d
:link: https://github.com/barmi/js-billiards-3d

**JavaScript · 2026-05**

three.js + cannon-es 기반 3D 8볼 풀. 스핀 위젯, ball-in-hand, 표준 8볼 룰 풀구현.
:::

::::

## 분류

좌측 사이드바 또는 아래에서 분야를 선택하세요.

::::{grid} 1 2 3 3
:gutter: 2

:::{grid-item-card} 활발한 2026 작업
:link: active
:link-type: doc

지난 6개월간 푸시한 직접 작성 저장소
:::

:::{grid-item-card} 게임 & 3D 시뮬레이션
:link: games
:link-type: doc

브라우저 3D 게임, 노노그램, 콘솔 게임 등
:::

:::{grid-item-card} 모바일 / 크로스플랫폼
:link: mobile
:link-type: doc

Flutter, Android (Java)
:::

:::{grid-item-card} 임베디드 / 하드웨어 / IoT
:link: embedded
:link-type: doc

ESP32·LVGL, CAN bus, 측정기, 클라우드
:::

:::{grid-item-card} 시스템 / OS
:link: system
:link-type: doc

운영체제, 스케줄러 시뮬레이터
:::

:::{grid-item-card} 보안
:link: security
:link-type: doc

CVE 감사 도구 · TLS/암호학 학습 fork
:::

:::{grid-item-card} VoIP / 네트워크
:link: network
:link-type: doc

SIP/MCPTT, ONVIF
:::

:::{grid-item-card} 백엔드 / 웹 서비스
:link: backend
:link-type: doc

FastAPI, PHP, MySQL 서비스
:::

:::{grid-item-card} 강의 / 교육 자료
:link: teaching
:link-type: doc

한신대 강의, 경기꿈의대학, 한빛 코딩클럽
:::

:::{grid-item-card} 개인 라이브러리 / 도구
:link: library
:link-type: doc

htmlcxx 등 외부 인용 가치 있는 라이브러리
:::

:::{grid-item-card} 학습 노트 (fork)
:link: notes
:link-type: doc

Rust, eBPF, TensorFlow 등 관심사 fork
:::

::::
