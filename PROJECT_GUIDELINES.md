# TV Europe Sales Management Portal - 프로젝트 지침 및 개발 가이드

이 문서는 **TV Europe Sales Management Portal** (해외영업 대시보드 통합 메뉴 포털 사이트)의 유지보수, 기능 확장 및 운영을 위한 지침서입니다.

---

## 1. 프로젝트 구조 (Project Directory Structure)

```
00. TV Europe Sales Management Portal/
├── index.html            # 좌측 사이드바 및 포탈 메인 구조, 에이전트 뷰어 오버레이
├── styles.css            # Stitch Strategic Insight System 기반 CSS (토큰, 사이드바, 뷰어 스타일)
├── app.js                # 13개 대시보드 데이터 정의, 사이드바 아코디언, 뷰어 전환 및 URL 매핑 로직
└── PROJECT_GUIDELINES.md # 프로젝트 관리 지침 문서 (본 파일)
```

---

## 2. 디자인 규격 (Design & Tone Manner)

- **디자인 시스템**: Stitch Project `Global Sales Insight Portal` (Strategic Insight System)
- **참조 프로젝트**: `GDMI_Weekly_Sellout_Analysis-main` (C-PSI Executive Portal)
- **컬러 스킴**:
  - Main Slate: `#0F172A`
  - Accent Teal: `#0D9488`
  - Blue: `#3B82F6`
  - Background: `#F8FAFC`
- **폰트 패밀리**:
  - `IBM Plex Sans` (타이틀 및 헤딩)
  - `Inter` (UI 및 본문)
  - `JetBrains Mono` (수치, KPI 및 타임스탬프)

---

## 3. 주요 기능 명세 (Core Features)

1. **280px 좌측 고정 사이드바 Navigation**:
   - `대시보드 포탈 홈` & `★ 즐겨찾기` 메인 메뉴
   - 4개 업무 카테고리 아코디언 (매출/손익 관리, 제품 정보, 가격 관리, 시장 정보)
   - 서브메뉴 클릭 시 해당 대시보드 뷰어 즉시 열기
2. **에이전트 네비게이션 뷰어 (Agent Navigation Viewer)**:
   - 카드 또는 사이드바 클릭 시 상단에 `← 포탈로 돌아가기` 헤더가 포함된 뷰어 오픈
   - 닫기 클릭 시 포탈 홈으로 즉시 복귀
3. **에이전트 URL 동적 매핑**:
   - 메인 콘텐츠 영역 우측 상단의 `에이전트 URL 관리` 버튼을 통해 카드별 외부 에이전트 URL 설정 지원
   - 미설정 시 내장 인터랙티브 시연 리포트 자동 렌더링

---

## 4. 운영 및 추가 가이드 (Maintenance Guide)

- **신규 대시보드 카드 추가 시**:
  - `app.js` 내 `DASHBOARDS` 배열에 새로운 대시보드 객체 등록.
  - `index.html` 내 사이드바 해당 카테고리 아래 `<button class="sub-nav-item" data-id="...">` 버튼 추가.
- **새 카테고리 추가 시**:
  - `index.html` 사이드바 및 `app.js` 카테고리 필터링 로직 확장.

---

## 5. 서브 대시보드 SSO & Auth Guard 연동 규격 (Unified Auth Guard Standard)

신규 서브 대시보드 웹사이트를 제작/배포할 때 아래 보안 및 SSO 규격을 적용해야 합니다.

1. **`auth-guard.js` 파일 포함**:
   - 서브 대시보드 루트 또는 public 디렉터리에 `auth-guard.js`를 배포합니다.
2. **`index.html` <head> 연동**:
   - 대시보드의 `index.html` `<head>` 태그 최상단에 아래 스크립트를 삽입합니다:
     ```html
     <script src="auth-guard.js"></script>
     ```
3. **인증 및 세션 작동 방식**:
   - **포털 경유 (SSO)**: 포털에서 이동 시 부착된 `auth_token`, `auth_ts`, `auth_user` 토큰을 자율 검증하여 **로그인 폼 입력 없이 바로 접속**되며, URL 파라미터는 `history.replaceState`로 깨끗하게 자동 삭제됩니다.
   - **독립 주소 직접 접근 (Direct)**: 브라우저에 대시보드 URL을 직접 입력해 진입하면 풀스크린 로그인 가드가 발동합니다 (ID: `LGE135` / PW: `LGE246`).
   - **세션 연장**: 30분 활동 없는 상태 유지 시 자동 로그아웃되며, 사용자 활동(마우스, 키보드) 시 30분 자동 연장됩니다.

