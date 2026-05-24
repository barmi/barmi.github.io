# 보안

본인 작업과, 학습/분석을 위해 fork한 저장소를 함께 모았습니다.

## 본인 작업

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

## 학습·분석 fork

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
