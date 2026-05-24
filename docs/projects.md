---
myst:
  html_meta:
    description: barmi가 작성/관리하는 프로젝트와 학습 노트의 분류 목록
---

# 프로젝트

지금까지 만들었거나 유지하고 있는 작업을 분야별로 정리합니다. 각 항목은 [GitHub @barmi](https://github.com/barmi) 저장소로 연결됩니다.

> 공개 저장소 약 135개(직접 작성 ~69 / fork ~66). 가장 오래된 직접 저장소는 2012년, 가장 최근은 2026-05.

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

---

## A. 활발한 2026 작업 (지난 6개월)

| Repo | 언어 | 생성 → 최근 | 비고 |
|---|---|---|---|
| [barmi.github.io](https://github.com/barmi/barmi.github.io) | Makefile | 2026-05-24 → 진행중 | 이 사이트 (Sphinx + Furo + MyST) |
| [cve-patch-auditor](https://github.com/barmi/cve-patch-auditor) | Go | 2026-05-16 → 2026-05-22 | Featured · 3⭐ · fork 2 |
| [js-billiards-3d](https://github.com/barmi/js-billiards-3d) | JavaScript | 2026-05-14 → 2026-05-15 | Featured |
| [js-tetris-3d](https://github.com/barmi/js-tetris-3d) | JavaScript | 2026-05-09 → 2026-05-10 | Featured |
| [orbitarium](https://github.com/barmi/orbitarium) | TypeScript | 2026-05-05 → 2026-05-06 | Featured |
| [js-tower-defense](https://github.com/barmi/js-tower-defense) | JavaScript | 2026-02-20 → 2026-05-05 | 그리드 TD. 3종 타워 · 5종 적 · 업그레이드/매각 |
| [bxos](https://github.com/barmi/bxos) | C | 2012-09-11 → 2026-05-04 | Featured · 13년차 |
| [grace_keychain_3d_model_for_jlc3dp](https://github.com/barmi/grace_keychain_3d_model_for_jlc3dp) | Python | 2026-03-24 | grace keychain STL → JLC3DP 변환 절차 |
| [lv_esp32s3_pc](https://github.com/barmi/lv_esp32s3_pc) | C | 2026-03-16 | LVGL + ESP32-S3 + PC SDL 시뮬레이터 |

## B. 게임 & 3D 시뮬레이션

| Repo | 언어 | 최근 | 비고 |
|---|---|---|---|
| [orbitarium](https://github.com/barmi/orbitarium) | TypeScript | 2026-05-06 | 태양계 시뮬레이터 |
| [js-billiards-3d](https://github.com/barmi/js-billiards-3d) | JavaScript | 2026-05-15 | 3D 8볼 풀 |
| [js-tetris-3d](https://github.com/barmi/js-tetris-3d) | JavaScript | 2026-05-10 | 3D 테트리스 (PWA) |
| [js-tower-defense](https://github.com/barmi/js-tower-defense) | JavaScript | 2026-05-05 | 타워 디펜스 |
| [nemo_solver](https://github.com/barmi/nemo_solver) | Python | 2024-08-25 | 네모로직(노노그램) 솔버 |
| [SimpleNemonemo](https://github.com/barmi/SimpleNemonemo) | Java | 2021-10-07 | 자바 노노그램 |
| [c_console_game](https://github.com/barmi/c_console_game) | C | 2021-01-05 | C 콘솔 게임 |
| [NumberBaseball](https://github.com/barmi/NumberBaseball) | C++ | 2018-10-30 | 숫자야구 |
| [PygameCross](https://github.com/barmi/PygameCross) | Python | 2018-06-25 | pygame picross |
| [skill-server-numbaseball](https://github.com/barmi/skill-server-numbaseball) | JavaScript | 2019-04-23 | 카카오톡 챗봇용 숫자야구 스킬 서버 |

## C. 모바일 / 크로스플랫폼

| Repo | 언어 | 최근 | 비고 |
|---|---|---|---|
| [flutter_nonogram](https://github.com/barmi/flutter_nonogram) | Dart | 2024-09-14 | Flutter 노노그램 |
| [flutter_todo_app](https://github.com/barmi/flutter_todo_app) | Dart | 2024-09-08 | Flutter Todo |
| [flutter_barcode](https://github.com/barmi/flutter_barcode) | Dart | 2024-10-06 | Flutter 바코드 |
| [MyPrinterA](https://github.com/barmi/MyPrinterA) | Java | 2019-05-23 | Android POS 프린터 |
| [SingleDiaryApp](https://github.com/barmi/SingleDiaryApp) | Java | 2019-04-17 | Android 일기 앱 |

## D. 임베디드 / 하드웨어 / IoT

| Repo | 언어 | 최근 | 비고 |
|---|---|---|---|
| [lv_esp32s3_pc](https://github.com/barmi/lv_esp32s3_pc) | C | 2026-03-16 | LVGL + ESP32-S3 + PC SDL 시뮬레이터 |
| [can_python](https://github.com/barmi/can_python) | Python | 2025-06-14 | CAN bus + Python |
| [grace_keychain_3d_model_for_jlc3dp](https://github.com/barmi/grace_keychain_3d_model_for_jlc3dp) | Python | 2026-03-24 | 3D 프린팅 STL 변환 |
| [esp8266_pms7003_dht11_ssd1306](https://github.com/barmi/esp8266_pms7003_dht11_ssd1306) | PHP/C | 2018-08-09 | 서울고 IoT 소모임 — 미세먼지 측정기 (ESP8266 + PMS7003 + DHT11 + SSD1306) |
| [get_instance_id](https://github.com/barmi/get_instance_id) | C | 2022-01-27 | GCP/AWS 인스턴스 ID 취득 |

## E. 시스템 / OS

| Repo | 언어 | 최근 | 비고 |
|---|---|---|---|
| [bxos](https://github.com/barmi/bxos) | C | 2026-05-04 | 한신대 OS 강의용. 13년차 |
| [OS_Scheduler_Simulator](https://github.com/barmi/OS_Scheduler_Simulator) | C++ | 2014-09-01 | OS 스케줄러 시뮬레이터 |
| [acmipc](https://github.com/barmi/acmipc) | C++ | 2025-12-19 | (README 미비) |

## F. 보안

본인 작업과, 학습/분석을 위해 fork한 저장소를 함께 모았습니다.

### 본인 작업

| Repo | 언어 | 최근 | 비고 |
|---|---|---|---|
| [cve-patch-auditor](https://github.com/barmi/cve-patch-auditor) | Go | 2026-05-22 | **3⭐ · fork 2**. 시스템별 CVE 감사·임시조치 자동화 CLI. 단일 Go 바이너리. 지원 CVE: |
|  |  |  | • CVE-2026-31431 (Copy Fail, CISA KEV) — `algif_aead` 로더블/built-in 분기 |
|  |  |  | • CVE-2026-43284 (Dirty Frag #1) — `esp4`/`esp6` 차단 |
|  |  |  | • CVE-2026-43500 (Dirty Frag #2) — `rxrpc`/`afs` 차단 |
|  |  |  | • CVE-2026-46300 (Fragnesia) — XFRM ESP-in-TCP 모듈 차단 |
|  |  |  | • CVE-2026-23918 (Apache HTTP/2 double-free) — `Protocols http/1.1` 드롭인 + graceful reload |
|  |  |  | • CVE-2026-46333 (ptrace LPE) — Yama LSM sysctl 즉시+영속 적용 |
|  |  |  | 정책: 도구가 자동 실행하는 것은 임시조치뿐, 패키지 매니저 호출 안 함. CVE별 분리 conf로 rollback 안전성 확보. |

### 학습·분석 fork

| Repo | 영역 | 시점 | 비고 |
|---|---|---|---|
| [copy-fail-c](https://github.com/barmi/copy-fail-c) | LPE 분석 | 2026-05 | CVE-2026-31431 Cross-platform C port. Theori/Xint 공개 (2026-04-29) |
| [copyfail-go](https://github.com/barmi/copyfail-go) | LPE 분석 | 2026-05 | 같은 CVE의 Go(+ Assembly) 구현 |
| [tls-cryptography](https://github.com/barmi/tls-cryptography) | 암호학 | 2021-09 | 『TLS 구현으로 배우는 암호학 — C++로 만드는 HTTPS 서비스』 학습 |
| [wolfssl](https://github.com/barmi/wolfssl) | TLS/SSL | 2021-10 | 임베디드용 TLS 1.3 라이브러리 |
| [ariago](https://github.com/barmi/ariago) | 대칭키 암호 | 2021-08 | 국산 표준 블록암호 ARIA의 Go 구현 |
| [libdssl](https://github.com/barmi/libdssl) | SSL 복호화 | 2016-09 | 네트워크 캡처 & SSL 복호화 toolkit |
| [libpsl](https://github.com/barmi/libpsl) | 도메인 검증 | 2024-05 | Public Suffix List C 라이브러리 (쿠키/도메인 정책) |
| [bpf-developer-tutorial](https://github.com/barmi/bpf-developer-tutorial) | eBPF | 2024-12 | 보안 모니터링/관찰성 학습 |

## G. VoIP / 네트워크

| Repo | 언어 | 최근 | 비고 |
|---|---|---|---|
| [qSIP](https://github.com/barmi/qSIP) (fork) | C | 2025-05-19 | VoIP/SIP 클라이언트(소프트폰) |
| [cppsipstack](https://github.com/barmi/cppsipstack) (fork) | C/C++ | 2023-12-13 | C++ SIP 스택 |
| [ponvif](https://github.com/barmi/ponvif) (fork) | PHP | 2019-12-04 | ONVIF + WS-Discovery PHP 구현 |
| [rpos](https://github.com/barmi/rpos) (fork) | JavaScript | 2019-03-28 | Raspberry Pi ONVIF 서버 |
| [2019-mdOnvif](https://github.com/barmi/2019-mdOnvif) | PHP | 2019-08-17 | ONVIF 관련 작업 |

## H. 백엔드 / 웹 서비스

| Repo | 언어 | 최근 | 비고 |
|---|---|---|---|
| [docker-fastapi-mongo-crud](https://github.com/barmi/docker-fastapi-mongo-crud) | Python | 2025-03-20 | FastAPI + MongoDB + Docker CRUD 보일러플레이트 |
| [grid_diary_php](https://github.com/barmi/grid_diary_php) | PHP | 2025-11-28 | 그리드 다이어리. 2시간 토큰, CSRF, 달력, MySQL upsert |
| [sellerkorea](https://github.com/barmi/sellerkorea) | CSS/PHP | 2020-10-28 | 셀러 사이트 |
| [ginnskin](https://github.com/barmi/ginnskin) | PHP | 2020-05-01 | PHP 스킨 |
| [dmshop](https://github.com/barmi/dmshop) | PHP | 2020-04-23 | PHP 쇼핑몰 |
| [work_timesheet](https://github.com/barmi/work_timesheet) | PHP | 2020-03-28 | 근무 시간 기록 |
| [github_code_review](https://github.com/barmi/github_code_review) | Python | 2019-06-05 | GitHub 코드리뷰 실습 |

## I. 강의 / 교육 자료

| Repo | 분야 | 시점 | 비고 |
|---|---|---|---|
| [bxos](https://github.com/barmi/bxos) | 운영체제 | 2012– | 한신대 OS 강의용 OS |
| [webprogramming2018](https://github.com/barmi/webprogramming2018) | 웹프로그래밍 | 2018-2학기 | 한신대 강의 |
| [WindowsProgramming2016](https://github.com/barmi/WindowsProgramming2016) | 윈도우 프로그래밍 | 2016 | 한신대 강의 |
| [PythonLogicGame](https://github.com/barmi/PythonLogicGame) | Python | 2018-2학기 | 경기꿈의대학 — 숫자야구·몬티홀·스도쿠·아인슈타인 문제 |
| [CodingClub_python](https://github.com/barmi/CodingClub_python) | Python | 2017-11 | 한빛 「코딩클럽」 책 예제 |
| [OS_Scheduler_Simulator](https://github.com/barmi/OS_Scheduler_Simulator) | OS | 2014-09 | OS 스케줄러 시뮬레이터 |

## J. 개인 라이브러리 / 도구

| Repo | 언어 | 최근 | 비고 |
|---|---|---|---|
| [htmlcxx](https://github.com/barmi/htmlcxx) | C++ | 2018-10-01 | **17⭐ · fork 5** — 최다 star 자산. HTML/CSS 파서 |
| [nemo_solver](https://github.com/barmi/nemo_solver) | Python | 2024-08-25 | 노노그램 솔버 |
| [get_instance_id](https://github.com/barmi/get_instance_id) | C | 2022-01-27 | GCP/AWS 인스턴스 ID |

## K. 학습 노트 (fork — 관심사 단서)

홈페이지에 「공부 노트」 섹션으로 별도 노출 가능.

| Fork | 영역 | 시점 |
|---|---|---|
| [RustTraining-MS](https://github.com/barmi/RustTraining-MS) | Rust (Microsoft 자료) | 2026-03 |
| [bpf-developer-tutorial](https://github.com/barmi/bpf-developer-tutorial) | eBPF | 2024-12 |
| [KiwiTalk](https://github.com/barmi/KiwiTalk) | Rust/Tauri 카카오톡 비공식 클라이언트 | 2023-11 |
| [doomgeneric](https://github.com/barmi/doomgeneric) + [DOOM_wads](https://github.com/barmi/DOOM_wads) | Doom 포팅·WAD | 2024-07 / 2019-06 |
| [glslViewer](https://github.com/barmi/glslViewer) | GLSL 셰이더 | 2025-01 |
| [CANgaroo](https://github.com/barmi/CANgaroo) / [CANable-MKS](https://github.com/barmi/CANable-MKS) | CAN bus 도구 | 2024–25 |
| [nimble-commander](https://github.com/barmi/nimble-commander) | Mac 듀얼 페인 파일 매니저 | 2024-08 |
| [iOS-Open-GPX-Tracker](https://github.com/barmi/iOS-Open-GPX-Tracker) | iOS/WatchOS GPX 트래커 | 2024-12 |
| [tensorflowbook](https://github.com/barmi/tensorflowbook) + [TensorFlow-Tutorials](https://github.com/barmi/TensorFlow-Tutorials) + [first-steps-with-tensorflow](https://github.com/barmi/first-steps-with-tensorflow) | TensorFlow 학습 (2017) | 2017 |
| [cs231n](https://github.com/barmi/cs231n) | Stanford CS231n (딥러닝) | 2018–22 |
| [pysc2-examples](https://github.com/barmi/pysc2-examples) + [commandcenter](https://github.com/barmi/commandcenter) + [MinervaSc2](https://github.com/barmi/MinervaSc2) | StarCraft II AI/RL | 2017-09 |

