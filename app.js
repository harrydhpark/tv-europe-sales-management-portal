// Global Sales Insight Portal - Application Logic (Left Sidebar Version)

// Authentication & Security Configuration (SHA-256 Hashed Credentials)
const AUTH_CONFIG = {
  // SHA-256 Hash of 'LGE135' (case-sensitive)
  ID_HASH: '4ed89d4c95cd896421176fe47e4c9ee9a0baad02dae39f57ce32eef58ec8e942',
  // SHA-256 Hash of 'LGE777' (case-sensitive)
  PW_HASH: '7e48a3df9992868561fed23f3f2137a2315a02981f23207a5af46b4374bbf5bb',
  SESSION_KEY: 'lge_portal_authenticated_user',
  TIMESTAMP_KEY: 'lge_portal_auth_timestamp',
  TIMEOUT_MS: 30 * 60 * 1000, // 30 minutes session timeout
  SECRET: 'LGE_TV_EU_PORTAL_SECRET_2026'
};

/**
 * SHA-256 Hashing helper using Web Crypto API
 * @param {string} message 
 * @returns {Promise<string>} Hex string of SHA-256 hash
 */
async function sha256(message) {
  const msgBuffer = new TextEncoder().encode(message);
  const hashBuffer = await crypto.subtle.digest('SHA-256', msgBuffer);
  const hashArray = Array.from(new Uint8Array(hashBuffer));
  return hashArray.map(b => b.toString(16).padStart(2, '0')).join('');
}

// 15 Dashboard Definitions with Custom Preview Graphics (No numerical values)
const DASHBOARDS = [
  // 1. 매출/손익 관리 (6 Cards)
  {
    id: "daily-sales-progress",
    category: "매출/손익 관리",
    categoryKey: "sales",
    period: "daily",
    title: "Daily Sales Progress",
    desc: "유럽 권역 및 법인별 일간 실시간 매출 진척률, 월 목표 대비 일일 출하 모니터링",
    updated: "Live Today 14:20",
    agentUrl: "https://eucisdailysales.apps.hedej.lge.com/",
    icon: "ri-pulse-line",
    previewSvg: `
      <svg viewBox="0 0 300 110" fill="none" xmlns="http://www.w3.org/2000/svg">
        <rect width="300" height="110" fill="#F8FAFC"/>
        <rect x="25" y="25" width="250" height="16" rx="8" fill="#E2E8F0"/>
        <rect x="25" y="25" width="185" height="16" rx="8" fill="url(#dailyGrad)"/>
        <line x1="210" y1="18" x2="210" y2="48" stroke="#EF4444" stroke-width="3" stroke-dasharray="3 3"/>
        <text x="215" y="22" fill="#EF4444" font-family="Inter, sans-serif" font-size="9" font-weight="700">TARGET (85%)</text>
        <defs>
          <linearGradient id="dailyGrad" x1="0" y1="0" x2="1" y2="0">
            <stop offset="0%" stop-color="#0D9488"/>
            <stop offset="100%" stop-color="#10B981"/>
          </linearGradient>
        </defs>
        <path d="M 25 85 L 65 75 L 105 80 L 145 60 L 185 65 L 225 48 L 275 42" stroke="#0D9488" stroke-width="3" stroke-linecap="round"/>
        <circle cx="275" cy="42" r="4" fill="#10B981"/>
        <rect x="25" y="52" width="90" height="20" rx="3" fill="#D1FAE5"/>
        <text x="32" y="66" fill="#065F46" font-family="Inter, sans-serif" font-size="9" font-weight="700">RUN RATE: 104%</text>
      </svg>
    `
  },
  {
    id: "kpi-sheet",
    category: "매출/손익 관리",
    categoryKey: "sales",
    period: "weekly",
    title: "KPI Sheet",
    desc: "권역 및 법인별 매출 실적, 출하 및 재고 주수(WOS) 등 핵심 영업 KPI 종합 모니터링",
    updated: "Today 09:30",
    agentUrl: "https://kpi-sheet-europe-2026.web.app",
    icon: "ri-file-list-3-line",
    previewSvg: `
      <svg viewBox="0 0 300 110" fill="none" xmlns="http://www.w3.org/2000/svg">
        <rect width="300" height="110" fill="#F8FAFC"/>
        <rect x="20" y="55" width="22" height="35" rx="3" fill="#94A3B8" opacity="0.4"/>
        <rect x="52" y="42" width="22" height="48" rx="3" fill="#0F172A" opacity="0.85"/>
        <rect x="84" y="32" width="22" height="58" rx="3" fill="#0D9488"/>
        <rect x="116" y="22" width="22" height="68" rx="3" fill="#0D9488"/>
        <path d="M20 50 L52 38 L84 28 L116 18 L150 14" stroke="#F59E0B" stroke-width="3" stroke-linecap="round"/>
        <circle cx="150" cy="14" r="4" fill="#F59E0B"/>
        <rect x="180" y="24" width="100" height="28" rx="4" fill="#0F172A"/>
        <text x="190" y="42" fill="#0D9488" font-family="Inter, sans-serif" font-size="11" font-weight="700">YoY GROWTH</text>
        <rect x="180" y="60" width="100" height="24" rx="4" fill="#E2E8F0"/>
        <text x="190" y="76" fill="#475569" font-family="Inter, sans-serif" font-size="10" font-weight="600">WOS TARGET</text>
      </svg>
    `
  },
  {
    id: "pnl-analysis",
    category: "매출/손익 관리",
    categoryKey: "sales",
    period: "monthly",
    title: "TV P&L Analysis",
    desc: "TV 사업부 매출원가, 판촉비, 손익구조 심층 분석 및 영업이익률 트렌드",
    updated: "Today 08:15",
    agentUrl: "https://lge-tv-pnl-2026.web.app",
    icon: "ri-funds-box-line",
    previewSvg: `
      <svg viewBox="0 0 300 110" fill="none" xmlns="http://www.w3.org/2000/svg">
        <rect width="300" height="110" fill="#F8FAFC"/>
        <path d="M20 80 Q 70 30, 140 65 T 280 20 L 280 90 L 20 90 Z" fill="url(#pnlGrad)" opacity="0.25"/>
        <path d="M20 80 Q 70 30, 140 65 T 280 20" stroke="#0D9488" stroke-width="3" stroke-linecap="round"/>
        <defs>
          <linearGradient id="pnlGrad" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stop-color="#0D9488"/>
            <stop offset="100%" stop-color="#0D9488" stop-opacity="0"/>
          </linearGradient>
        </defs>
        <rect x="25" y="20" width="110" height="26" rx="4" fill="#0F172A"/>
        <text x="35" y="37" fill="#10B981" font-family="Inter, sans-serif" font-size="11" font-weight="700">NET MARGIN</text>
        <circle cx="280" cy="20" r="4" fill="#0D9488"/>
      </svg>
    `
  },
  {
    id: "gdmi-weekly",
    category: "매출/손익 관리",
    categoryKey: "sales",
    period: "weekly",
    title: "GDMI Weekly Sellout Analysis",
    desc: "주차별 유럽 15개국 법인/유통 주간 Sellout 실적 및 재고 분석 리포트",
    updated: "2026-07-22",
    agentUrl: "https://gdmi-weekly-dashboard.web.app",
    icon: "ri-calendar-check-line",
    previewSvg: `
      <svg viewBox="0 0 300 110" fill="none" xmlns="http://www.w3.org/2000/svg">
        <rect width="300" height="110" fill="#F8FAFC"/>
        <text x="20" y="25" fill="#64748B" font-family="Inter, sans-serif" font-size="10" font-weight="700">WEEKLY SELLOUT TREND</text>
        <rect x="20" y="55" width="36" height="35" rx="3" fill="#CBD5E1"/>
        <text x="26" y="80" fill="#475569" font-family="Inter, sans-serif" font-size="9">Wk</text>
        <rect x="66" y="45" width="36" height="45" rx="3" fill="#CBD5E1"/>
        <text x="72" y="80" fill="#475569" font-family="Inter, sans-serif" font-size="9">Wk</text>
        <rect x="112" y="38" width="36" height="52" rx="3" fill="#0F172A"/>
        <text x="118" y="80" fill="#FFF" font-family="Inter, sans-serif" font-size="9">Wk</text>
        <rect x="158" y="30" width="36" height="60" rx="3" fill="#0D9488"/>
        <text x="164" y="80" fill="#FFF" font-family="Inter, sans-serif" font-size="9">Wk</text>
        <rect x="204" y="20" width="36" height="70" rx="3" fill="#0D9488"/>
        <text x="210" y="80" fill="#FFF" font-family="Inter, sans-serif" font-size="9">Wk</text>
        <rect x="245" y="20" width="50" height="24" rx="3" fill="#10B981"/>
        <text x="250" y="36" fill="#FFF" font-family="Inter, sans-serif" font-size="9" font-weight="700">SELLOUT</text>
      </svg>
    `
  },
  {
    id: "pre-profitability",
    category: "매출/손익 관리",
    categoryKey: "sales",
    period: "monthly",
    title: "선행 수익성 분석",
    desc: "신규 수주 및 출하 전 시나리오별 선행 이익률 예측 및 시뮬레이션 타당성 검증",
    updated: "Today 11:00",
    agentUrl: "https://lge-advance-profitability-2026.web.app",
    icon: "ri-calculator-line",
    previewSvg: `
      <svg viewBox="0 0 300 110" fill="none" xmlns="http://www.w3.org/2000/svg">
        <rect width="300" height="110" fill="#F8FAFC"/>
        <circle cx="80" cy="55" r="35" stroke="#E2E8F0" stroke-width="8"/>
        <path d="M 80 20 A 35 35 0 1 1 50 78" stroke="#0D9488" stroke-width="8" stroke-linecap="round"/>
        <text x="62" y="60" fill="#0F172A" font-family="Inter, sans-serif" font-size="11" font-weight="700">MARGIN</text>
        <text x="140" y="42" fill="#0F172A" font-family="Inter, sans-serif" font-size="12" font-weight="700">PRE-MARGIN TARGET</text>
        <text x="140" y="60" fill="#64748B" font-family="Inter, sans-serif" font-size="11">Pre-order Validation OK</text>
        <rect x="140" y="70" width="130" height="20" rx="3" fill="#FEE2E2"/>
        <text x="148" y="84" fill="#991B1B" font-family="Inter, sans-serif" font-size="10" font-weight="600">Risk Items Check</text>
      </svg>
    `
  },
  {
    id: "profit-simulator",
    category: "매출/손익 관리",
    categoryKey: "sales",
    period: "monthly",
    title: "수익성 Simulator",
    desc: "환율, 원가, 유통 장려금 변동 민감도 시뮬레이션 및 손익 시나리오 분석 도구",
    updated: "2026-07-21",
    agentUrl: "https://lge-profitability-simulator-2026.web.app",
    icon: "ri-dashboard-2-line",
    previewSvg: `
      <svg viewBox="0 0 300 110" fill="none" xmlns="http://www.w3.org/2000/svg">
        <rect width="300" height="110" fill="#F8FAFC"/>
        <line x1="30" y1="35" x2="270" y2="35" stroke="#CBD5E1" stroke-width="4" stroke-linecap="round"/>
        <circle cx="120" cy="35" r="8" fill="#0D9488"/>
        <line x1="30" y1="75" x2="270" y2="75" stroke="#CBD5E1" stroke-width="4" stroke-linecap="round"/>
        <circle cx="190" cy="75" r="8" fill="#3B82F6"/>
        <text x="30" y="24" fill="#475569" font-family="Inter, sans-serif" font-size="10" font-weight="700">FX Sensitivity Slider</text>
        <text x="30" y="64" fill="#475569" font-family="Inter, sans-serif" font-size="10" font-weight="700">Rebate Cost Slider</text>
      </svg>
    `
  },

  // 2. 제품 정보 (4 Cards)
  {
    id: "tv-prm",
    category: "제품 정보",
    categoryKey: "product",
    period: "monthly",
    title: "TV PRM",
    desc: "TV Product Roadmap / 연간 모델 라인업 출시 일정 및 세그먼트 스펙",
    updated: "2026-07-20",
    agentUrl: "https://lge-product-showcase-2026.web.app",
    icon: "ri-tv-2-line",
    previewSvg: `
      <svg viewBox="0 0 300 110" fill="none" xmlns="http://www.w3.org/2000/svg">
        <rect width="300" height="110" fill="#F8FAFC"/>
        <!-- TV Frame Silhouette -->
        <rect x="25" y="20" width="110" height="65" rx="4" fill="#0F172A"/>
        <rect x="29" y="24" width="102" height="57" fill="#1E293B"/>
        <path d="M 60 85 L 100 85 L 105 95 L 55 95 Z" fill="#475569"/>
        <text x="45" y="58" fill="#0D9488" font-family="IBM Plex Sans, sans-serif" font-size="14" font-weight="700">OLED TV</text>
        <!-- Timeline -->
        <line x1="155" y1="35" x2="280" y2="35" stroke="#0D9488" stroke-width="2"/>
        <circle cx="170" cy="35" r="4" fill="#0D9488"/>
        <text x="162" y="52" fill="#0F172A" font-family="Inter, sans-serif" font-size="10" font-weight="700">Q1</text>
        <circle cx="220" cy="35" r="4" fill="#0D9488"/>
        <text x="212" y="52" fill="#0F172A" font-family="Inter, sans-serif" font-size="10" font-weight="700">Q3</text>
        <circle cx="270" cy="35" r="4" fill="#3B82F6"/>
        <text x="256" y="52" fill="#0F172A" font-family="Inter, sans-serif" font-size="10" font-weight="700">NEXT</text>
        <rect x="155" y="65" width="125" height="24" rx="4" fill="#E2E8F0"/>
        <text x="165" y="81" fill="#0F172A" font-family="Inter, sans-serif" font-size="10" font-weight="600">Active Lineups</text>
      </svg>
    `
  },
  {
    id: "spec-sheet",
    category: "제품 정보",
    categoryKey: "product",
    period: "monthly",
    title: "Spec Sheet",
    desc: "OLED/QNED/NanoCell 모델별 세부 사양 비교, 패널 정보 및 기술 사양서 조회",
    updated: "2026-07-19",
    agentUrl: "https://lge-product-showcase-2026.web.app",
    icon: "ri-article-line",
    previewSvg: `
      <svg viewBox="0 0 300 110" fill="none" xmlns="http://www.w3.org/2000/svg">
        <rect width="300" height="110" fill="#F8FAFC"/>
        <rect x="25" y="18" width="250" height="74" rx="4" fill="#FFF" stroke="#CBD5E1"/>
        <rect x="25" y="18" width="250" height="20" fill="#0F172A"/>
        <text x="35" y="32" fill="#FFF" font-family="Inter, sans-serif" font-size="10" font-weight="700">MODEL SPEC MATRIX (OLED vs QNED)</text>
        <line x1="25" y1="56" x2="275" y2="56" stroke="#E2E8F0"/>
        <line x1="25" y1="74" x2="275" y2="74" stroke="#E2E8F0"/>
        <line x1="110" y1="38" x2="110" y2="92" stroke="#E2E8F0"/>
        <text x="35" y="50" fill="#475569" font-family="Inter, sans-serif" font-size="9">OLED evo</text>
        <text x="120" y="50" fill="#0D9488" font-family="Inter, sans-serif" font-size="9" font-weight="700">evo Display / High-Hz</text>
        <text x="35" y="68" fill="#475569" font-family="Inter, sans-serif" font-size="9">QNED Mini</text>
        <text x="120" y="68" fill="#3B82F6" font-family="Inter, sans-serif" font-size="9" font-weight="700">MiniLED / High-Hz</text>
      </svg>
    `
  },
  {
    id: "tv-profile",
    category: "제품 정보",
    categoryKey: "product",
    period: "monthly",
    title: "TV Product profile",
    desc: "전략 모델 및 시리즈별 USP, 셀링 포인트, 주요 유통 타깃 사양 프로파일",
    updated: "2026-07-18",
    agentUrl: "https://lge-product-showcase-2026.web.app",
    icon: "ri-presentation-line",
    previewSvg: `
      <svg viewBox="0 0 300 110" fill="none" xmlns="http://www.w3.org/2000/svg">
        <rect width="300" height="110" fill="#F8FAFC"/>
        <rect x="30" y="20" width="130" height="70" rx="4" fill="#0F172A"/>
        <rect x="34" y="24" width="122" height="62" fill="#1E293B"/>
        <text x="45" y="52" fill="#FFF" font-family="IBM Plex Sans, sans-serif" font-size="13" font-weight="700">HERO OLED</text>
        <text x="45" y="68" fill="#0D9488" font-family="Inter, sans-serif" font-size="9">Gallery Flush Fit</text>
        <rect x="175" y="25" width="95" height="24" rx="12" fill="#0D9488"/>
        <text x="184" y="41" fill="#FFF" font-family="Inter, sans-serif" font-size="10" font-weight="700">Product Profile</text>
        <rect x="175" y="60" width="95" height="24" rx="4" fill="#E2E8F0"/>
        <text x="185" y="76" fill="#475569" font-family="Inter, sans-serif" font-size="10" font-weight="600">USP Highlight</text>
      </svg>
    `
  },
  {
    id: "dealer-trip-calendar",
    category: "제품 정보",
    categoryKey: "product",
    period: "monthly",
    title: "거래선 방한 상담 일정 캘린더",
    desc: "유럽/CIS 주요 거래선 방한 일정, 본사 미팅 스케줄 및 상담 내역 통합 관리 캘린더",
    updated: "Live Today",
    agentUrl: "https://dealertrip.apps.hedej.lge.com/",
    icon: "ri-calendar-event-line",
    previewSvg: `
      <svg viewBox="0 0 300 110" fill="none" xmlns="http://www.w3.org/2000/svg">
        <rect width="300" height="110" fill="#F8FAFC"/>
        <!-- Calendar Window Frame -->
        <rect x="25" y="16" width="250" height="78" rx="6" fill="#FFF" stroke="#CBD5E1" stroke-width="1.5"/>
        <!-- Calendar Header Bar -->
        <rect x="25" y="16" width="250" height="22" rx="6" fill="#0F172A"/>
        <rect x="25" y="32" width="250" height="6" fill="#0F172A"/>
        <text x="36" y="31" fill="#FFF" font-family="Inter, sans-serif" font-size="10" font-weight="700">DEALER VISIT CALENDAR</text>
        <rect x="215" y="21" width="52" height="12" rx="3" fill="#0D9488"/>
        <text x="220" y="30" fill="#FFF" font-family="Inter, sans-serif" font-size="8" font-weight="700">2026 VISIT</text>
        <!-- Grid Lines -->
        <line x1="25" y1="56" x2="275" y2="56" stroke="#F1F5F9" stroke-width="1"/>
        <line x1="25" y1="74" x2="275" y2="74" stroke="#F1F5F9" stroke-width="1"/>
        <line x1="87" y1="38" x2="87" y2="94" stroke="#F1F5F9" stroke-width="1"/>
        <line x1="150" y1="38" x2="150" y2="94" stroke="#F1F5F9" stroke-width="1"/>
        <line x1="212" y1="38" x2="212" y2="94" stroke="#F1F5F9" stroke-width="1"/>
        <!-- Event Pills -->
        <rect x="30" y="42" width="52" height="11" rx="2" fill="#0D9488"/>
        <text x="33" y="50" fill="#FFF" font-family="Inter, sans-serif" font-size="7" font-weight="700">EU HQ Visit</text>
        <rect x="92" y="60" width="53" height="11" rx="2" fill="#3B82F6"/>
        <text x="95" y="68" fill="#FFF" font-family="Inter, sans-serif" font-size="7" font-weight="700">Retail Conf</text>
        <rect x="155" y="42" width="52" height="11" rx="2" fill="#10B981"/>
        <text x="158" y="50" fill="#FFF" font-family="Inter, sans-serif" font-size="7" font-weight="700">Lineup Tour</text>
        <rect x="217" y="78" width="53" height="11" rx="2" fill="#F59E0B"/>
        <text x="220" y="86" fill="#FFF" font-family="Inter, sans-serif" font-size="7" font-weight="700">Biz Meeting</text>
      </svg>
    `
  },

  // 3. 가격 관리 (2 Cards)
  {
    id: "price-tracker",
    category: "가격 관리",
    categoryKey: "pricing",
    period: "daily",
    title: "Price Tracker",
    desc: "국가별/유통별 실시간 매장 및 온라인 판매 가격(ASP) 추적 및 Price Gap 분석",
    updated: "Today 10:45",
    agentUrl: "https://eu-price-tracker-lge.web.app",
    icon: "ri-price-tag-3-line",
    previewSvg: `
      <svg viewBox="0 0 300 110" fill="none" xmlns="http://www.w3.org/2000/svg">
        <rect width="300" height="110" fill="#F8FAFC"/>
        <path d="M25 75 L80 45 L140 60 L210 25 L275 35" stroke="#B45309" stroke-width="3" stroke-linecap="round"/>
        <circle cx="210" cy="25" r="5" fill="#B45309"/>
        <rect x="155" y="12" width="115" height="22" rx="3" fill="#B45309"/>
        <text x="162" y="27" fill="#FFF" font-family="Inter, sans-serif" font-size="10" font-weight="700">EU ASP TRACKER</text>
        <rect x="25" y="20" width="80" height="20" rx="3" fill="#FEF3C7"/>
        <text x="32" y="34" fill="#92400E" font-family="Inter, sans-serif" font-size="9" font-weight="700">Gap Alert</text>
      </svg>
    `
  },
  {
    id: "ata-guide",
    category: "가격 관리",
    categoryKey: "pricing",
    period: "monthly",
    title: "ATA Guide",
    desc: "Authorization To Act / 권역별 최저 승인 판매 가격 가이드라인 및 승인 현황",
    updated: "Today 07:50",
    agentUrl: "https://lge-product-showcase-2026.web.app/docs/ata-guide/",
    icon: "ri-shield-check-line",
    previewSvg: `
      <svg viewBox="0 0 300 110" fill="none" xmlns="http://www.w3.org/2000/svg">
        <rect width="300" height="110" fill="#F8FAFC"/>
        <path d="M 60 25 L 100 25 C 100 65 60 85 60 85 C 60 85 20 65 20 25 Z" fill="#0F172A"/>
        <path d="M 45 52 L 55 62 L 78 38" stroke="#0D9488" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
        <text x="115" y="42" fill="#0F172A" font-family="Inter, sans-serif" font-size="13" font-weight="700">ATA APPROVED</text>
        <text x="115" y="60" fill="#64748B" font-family="Inter, sans-serif" font-size="11">Floor Price Policy Active</text>
        <rect x="115" y="70" width="140" height="20" rx="3" fill="#D1FAE5"/>
        <text x="123" y="84" fill="#065F46" font-family="Inter, sans-serif" font-size="10" font-weight="700">Pending Authorization</text>
      </svg>
    `
  },

  // 4. 시장 정보 (3 Cards)
  {
    id: "gfk-monthly",
    category: "시장 정보",
    categoryKey: "market",
    period: "monthly",
    title: "GfK Monthly Report",
    desc: "유럽 주요 12개국 GfK 월간 시장 수량/금액 수집 데이터 보고서 및 세그먼트 분석",
    updated: "2026-07-15",
    agentUrl: "https://gfk-report-monthly-lge.web.app",
    icon: "ri-pie-chart-2-line",
    previewSvg: `
      <svg viewBox="0 0 300 110" fill="none" xmlns="http://www.w3.org/2000/svg">
        <rect width="300" height="110" fill="#F8FAFC"/>
        <!-- Donut Chart -->
        <circle cx="75" cy="55" r="32" fill="#7E22CE"/>
        <path d="M 75 55 L 75 23 A 32 32 0 0 1 107 55 Z" fill="#0D9488"/>
        <path d="M 75 55 L 107 55 A 32 32 0 0 1 75 87 Z" fill="#3B82F6"/>
        <circle cx="75" cy="55" r="16" fill="#F8FAFC"/>
        <text x="130" y="42" fill="#0F172A" font-family="Inter, sans-serif" font-size="12" font-weight="700">GfK MARKET SIZE</text>
        <text x="130" y="60" fill="#64748B" font-family="Inter, sans-serif" font-size="11">Data Month: Latest</text>
        <rect x="130" y="70" width="130" height="20" rx="3" fill="#F3E8FF"/>
        <text x="138" y="84" fill="#6B21A8" font-family="Inter, sans-serif" font-size="10" font-weight="700">EU Countries Sync</text>
      </svg>
    `
  },
  {
    id: "ms-trend",
    category: "시장 정보",
    categoryKey: "market",
    period: "weekly",
    title: "M/S Trend",
    desc: "경쟁사(Samsung, Sony, Hisense) 대비 브랜드별/인치별 Market Share 트렌드",
    updated: "2026-07-15",
    agentUrl: "https://tv-ms-trend-dashboard.web.app",
    icon: "ri-bar-chart-grouped-line",
    previewSvg: `
      <svg viewBox="0 0 300 110" fill="none" xmlns="http://www.w3.org/2000/svg">
        <rect width="300" height="110" fill="#F8FAFC"/>
        <text x="25" y="24" fill="#475569" font-family="Inter, sans-serif" font-size="10" font-weight="700">BRAND M/S RANKING</text>
        <rect x="25" y="35" width="170" height="16" rx="3" fill="#7E22CE"/>
        <text x="202" y="47" fill="#7E22CE" font-family="Inter, sans-serif" font-size="10" font-weight="700">OLED SHARE</text>
        <rect x="25" y="58" width="120" height="16" rx="3" fill="#0F172A"/>
        <text x="152" y="70" fill="#0F172A" font-family="Inter, sans-serif" font-size="10" font-weight="700">Total TV SHARE</text>
        <rect x="25" y="81" width="80" height="16" rx="3" fill="#CBD5E1"/>
        <text x="112" y="93" fill="#64748B" font-family="Inter, sans-serif" font-size="10">Competitor A</text>
      </svg>
    `
  },
  {
    id: "fx-monitor",
    category: "시장 정보",
    categoryKey: "market",
    period: "daily",
    title: "FX-Monitor",
    desc: "글로벌 주요 통화(EUR, USD, GBP, PLN 등) 환율 변동 추이 및 실적 리스크 분석",
    updated: "Live Auto",
    agentUrl: "https://ac-fx-monitor-test.apps.hedej.lge.com/",
    icon: "ri-money-dollar-circle-line",
    previewSvg: `
      <svg viewBox="0 0 300 110" fill="none" xmlns="http://www.w3.org/2000/svg">
        <rect width="300" height="110" fill="#F8FAFC"/>
        <path d="M20 70 L60 50 L100 65 L150 35 L200 45 L260 20" stroke="#0D9488" stroke-width="3" stroke-linecap="round"/>
        <circle cx="260" cy="20" r="4" fill="#0D9488"/>
        <rect x="20" y="15" width="90" height="22" rx="3" fill="#0F172A"/>
        <text x="28" y="30" fill="#FFF" font-family="Inter, sans-serif" font-size="10" font-weight="700">EUR / USD</text>
        <rect x="120" y="15" width="120" height="22" rx="3" fill="#D1FAE5"/>
        <text x="128" y="30" fill="#065F46" font-family="Inter, sans-serif" font-size="10" font-weight="700">FX Impact Status</text>
      </svg>
    `
  }
];

// Dual Persistence Storage Helpers (LocalStorage + Cookie Fallback)
function loadStoredCustomUrls() {
  try {
    const fromStorage = localStorage.getItem("portal_custom_urls");
    if (fromStorage) return JSON.parse(fromStorage);
  } catch (e) {}

  try {
    const match = document.cookie.match(/(?:^|; )portal_custom_urls=([^;]*)/);
    if (match && match[1]) return JSON.parse(decodeURIComponent(match[1]));
  } catch (e) {}

  return {};
}

function saveStoredCustomUrls(data) {
  const jsonStr = JSON.stringify(data);
  try {
    localStorage.setItem("portal_custom_urls", jsonStr);
  } catch (e) {}

  try {
    document.cookie = "portal_custom_urls=" + encodeURIComponent(jsonStr) + "; path=/; max-age=31536000";
  } catch (e) {}
}

const DEFAULT_AGENT_URLS = {
  "daily-sales-progress": "https://eucisdailysales.apps.hedej.lge.com/",
  "kpi-sheet": "https://kpi-sheet-europe-2026.web.app",
  "pnl-analysis": "https://lge-tv-pnl-2026.web.app",
  "gdmi-weekly": "https://gdmi-weekly-dashboard.web.app",
  "pre-profitability": "https://lge-advance-profitability-2026.web.app",
  "profit-simulator": "https://lge-profitability-simulator-2026.web.app",
  "tv-prm": "https://lge-product-showcase-2026.web.app",
  "spec-sheet": "https://lge-product-showcase-2026.web.app",
  "tv-profile": "https://lge-product-showcase-2026.web.app",
  "price-tracker": "https://eu-price-tracker-lge.web.app",
  "ata-guide": "https://lge-product-showcase-2026.web.app/docs/ata-guide/",
  "gfk-monthly": "https://gfk-report-monthly-lge.web.app",
  "ms-trend": "https://tv-ms-trend-dashboard.web.app",
  "fx-monitor": "https://ac-fx-monitor-test.apps.hedej.lge.com/"
};

function getEffectiveUrl(dash) {
  if (customUrls && customUrls[dash.id] !== undefined && customUrls[dash.id].trim() !== "") {
    return customUrls[dash.id];
  }
  return dash.agentUrl || DEFAULT_AGENT_URLS[dash.id] || "";
}

// Application State
let currentCategory = "ALL";
let currentPeriod = "ALL";
let searchQuery = "";
let customUrls = loadStoredCustomUrls();
let favorites = JSON.parse(localStorage.getItem("portal_favorites") || "[]");

// DOM Elements
const cardsGrid = document.getElementById("cardsGrid");
const searchInput = document.getElementById("searchInput");
const clearSearchBtn = document.getElementById("clearSearchBtn");
const currentCategoryTitle = document.getElementById("currentCategoryTitle");
const currentCategoryDesc = document.getElementById("currentCategoryDesc");
const visibleCardCount = document.getElementById("visibleCardCount");

const countAllEl = document.getElementById("countAll");
const countDailyEl = document.getElementById("countDaily");
const countWeeklyEl = document.getElementById("countWeekly");
const countMonthlyEl = document.getElementById("countMonthly");

// Sidebar Nav Elements
const navHome = document.getElementById("navHome");
const navDaily = document.getElementById("navDaily");
const navWeekly = document.getElementById("navWeekly");
const navMonthly = document.getElementById("navMonthly");
const accordions = document.querySelectorAll(".category-accordion");

// Agent Viewer Overlay Elements
const agentViewerOverlay = document.getElementById("agentViewerOverlay");
const closeViewerBtn = document.getElementById("closeViewerBtn");
const closeViewerXBtn = document.getElementById("closeViewerXBtn");
const viewerCategory = document.getElementById("viewerCategory");
const viewerTitle = document.getElementById("viewerTitle");
const viewerExternalLink = document.getElementById("viewerExternalLink");
const agentIframe = document.getElementById("agentIframe");
const mockDashboardContainer = document.getElementById("mockDashboardContainer");

// Modal Elements
const configUrlBtn = document.getElementById("configUrlBtn");
const configModalOverlay = document.getElementById("configModalOverlay");
const closeConfigModalBtn = document.getElementById("closeConfigModalBtn");
const urlConfigList = document.getElementById("urlConfigList");
const saveUrlsBtn = document.getElementById("saveUrlsBtn");
const resetUrlsBtn = document.getElementById("resetUrlsBtn");

// Authentication Handlers & Activity Monitoring
function updateAuthActivity() {
  const authUser = sessionStorage.getItem(AUTH_CONFIG.SESSION_KEY);
  if (authUser) {
    sessionStorage.setItem(AUTH_CONFIG.TIMESTAMP_KEY, Date.now().toString());
  }
}

function clearAuthSession() {
  sessionStorage.removeItem(AUTH_CONFIG.SESSION_KEY);
  sessionStorage.removeItem(AUTH_CONFIG.TIMESTAMP_KEY);
}

function checkAuthStatus() {
  const loginOverlay = document.getElementById("loginOverlay");
  const authUser = sessionStorage.getItem(AUTH_CONFIG.SESSION_KEY);
  const lastActivity = sessionStorage.getItem(AUTH_CONFIG.TIMESTAMP_KEY);
  const now = Date.now();
  
  const isValidSession = authUser && lastActivity && (now - parseInt(lastActivity, 10) < AUTH_CONFIG.TIMEOUT_MS);
  
  if (isValidSession) {
    updateAuthActivity();
    if (loginOverlay) loginOverlay.classList.add("hidden");
    const sidebarUserName = document.getElementById("sidebarUserName");
    const sidebarAvatar = document.getElementById("sidebarAvatar");
    if (sidebarUserName) sidebarUserName.textContent = authUser;
    if (sidebarAvatar) sidebarAvatar.textContent = authUser.substring(0, 3).toUpperCase();
  } else {
    clearAuthSession();
    if (loginOverlay) loginOverlay.classList.remove("hidden");
    const usernameInput = document.getElementById("usernameInput");
    if (usernameInput) setTimeout(() => usernameInput.focus(), 100);
  }
}

async function handleLoginSubmit(e) {
  if (e) e.preventDefault();
  const usernameInput = document.getElementById("usernameInput");
  const passwordInput = document.getElementById("passwordInput");
  const errorMessage = document.getElementById("loginErrorMessage");
  const errorText = document.getElementById("loginErrorText");
  const submitBtn = document.getElementById("loginSubmitBtn");
  
  if (!usernameInput || !passwordInput) return;
  
  const enteredId = usernameInput.value.trim();
  const enteredPw = passwordInput.value.trim();
  
  if (!enteredId || !enteredPw) {
    if (errorText) errorText.textContent = "아이디와 비밀번호를 모두 입력해 주세요.";
    if (errorMessage) errorMessage.style.display = "flex";
    return;
  }
  
  if (submitBtn) submitBtn.disabled = true;
  
  try {
    const idHash = await sha256(enteredId);
    const pwHash = await sha256(enteredPw);
    
    if (idHash === AUTH_CONFIG.ID_HASH && pwHash === AUTH_CONFIG.PW_HASH) {
      sessionStorage.setItem(AUTH_CONFIG.SESSION_KEY, enteredId);
      sessionStorage.setItem(AUTH_CONFIG.TIMESTAMP_KEY, Date.now().toString());
      if (errorMessage) errorMessage.style.display = "none";
      usernameInput.value = "";
      passwordInput.value = "";
      checkAuthStatus();
    } else {
      if (errorText) errorText.textContent = "아이디 또는 비밀번호가 일치하지 않습니다. (대소문자 구별)";
      if (errorMessage) {
        errorMessage.style.display = "flex";
        errorMessage.style.animation = 'none';
        errorMessage.offsetHeight; // trigger reflow
        errorMessage.style.animation = 'shake 0.4s ease-in-out';
      }
      passwordInput.value = "";
      passwordInput.focus();
    }
  } catch (err) {
    console.error("Authentication Error:", err);
    if (errorText) errorText.textContent = "인증 중 오류가 발생했습니다.";
    if (errorMessage) errorMessage.style.display = "flex";
  } finally {
    if (submitBtn) submitBtn.disabled = false;
  }
}

function handleLogout() {
  if (confirm("로그아웃 하시겠습니까?")) {
    clearAuthSession();
    checkAuthStatus();
  }
}

let activityThrottleTimer = null;
function setupActivityListeners() {
  const events = ['mousemove', 'keydown', 'click', 'scroll', 'touchstart'];
  events.forEach(evt => {
    window.addEventListener(evt, () => {
      if (!activityThrottleTimer) {
        updateAuthActivity();
        activityThrottleTimer = setTimeout(() => {
          activityThrottleTimer = null;
        }, 10000); // Throttle activity updates to once every 10 seconds
      }
    }, { passive: true });
  });

  // Periodically check session expiration every 1 minute
  setInterval(checkAuthStatus, 60000);
}

function setupAuthEventListeners() {
  const loginForm = document.getElementById("loginForm");
  const logoutBtn = document.getElementById("logoutBtn");
  const togglePasswordBtn = document.getElementById("togglePasswordBtn");
  const passwordInput = document.getElementById("passwordInput");
  const usernameInput = document.getElementById("usernameInput");
  const capsLockWarning = document.getElementById("capsLockWarning");
  const togglePasswordIcon = document.getElementById("togglePasswordIcon");

  if (loginForm) {
    loginForm.addEventListener("submit", handleLoginSubmit);
  }

  if (logoutBtn) {
    logoutBtn.addEventListener("click", handleLogout);
  }

  if (togglePasswordBtn && passwordInput && togglePasswordIcon) {
    togglePasswordBtn.addEventListener("click", () => {
      const isPassword = passwordInput.type === "password";
      passwordInput.type = isPassword ? "text" : "password";
      togglePasswordIcon.className = isPassword ? "ri-eye-line" : "ri-eye-off-line";
    });
  }

  const checkCapsLock = (e) => {
    if (e && e.getModifierState) {
      const isCapsLock = e.getModifierState("CapsLock");
      if (capsLockWarning) {
        capsLockWarning.style.display = isCapsLock ? "flex" : "none";
      }
    }
  };

  if (passwordInput) {
    passwordInput.addEventListener("keyup", checkCapsLock);
    passwordInput.addEventListener("keydown", checkCapsLock);
  }
  if (usernameInput) {
    usernameInput.addEventListener("keyup", checkCapsLock);
    usernameInput.addEventListener("keydown", checkCapsLock);
  }
}

// Initialize Portal
function init() {
  setupAuthEventListeners();
  checkAuthStatus();
  setupActivityListeners();
  updateCounts();
  renderCards();
  setupEventListeners();

  // Open first accordion by default
  const firstAccordion = document.querySelector(".category-accordion");
  if (firstAccordion) firstAccordion.classList.add("open");
}

// Update Counts
function updateCounts() {
  countAllEl.textContent = DASHBOARDS.length;
  if (countDailyEl) countDailyEl.textContent = DASHBOARDS.filter(d => d.period.toLowerCase() === "daily").length;
  if (countWeeklyEl) countWeeklyEl.textContent = DASHBOARDS.filter(d => d.period.toLowerCase() === "weekly").length;
  if (countMonthlyEl) countMonthlyEl.textContent = DASHBOARDS.filter(d => d.period.toLowerCase() === "monthly").length;
}

/**
 * Helper to resolve the effective URL for a dashboard.
 * Explicitly respects user's custom URL configuration (including empty string "").
 */
function getEffectiveUrl(dash) {
  if (Object.prototype.hasOwnProperty.call(customUrls, dash.id)) {
    return customUrls[dash.id];
  }
  return dash.agentUrl || "";
}

// Render Bento Cards
function renderCards() {
  cardsGrid.innerHTML = "";
  updateSidebarIndicators();

  // Sync category chip UI active state
  const categoryChipsContainer = document.getElementById("categoryChips");
  if (categoryChipsContainer) {
    categoryChipsContainer.querySelectorAll(".chip-btn").forEach(btn => {
      const cat = btn.getAttribute("data-category");
      if (cat === currentCategory) btn.classList.add("active");
      else btn.classList.remove("active");
    });
  }

  const filtered = DASHBOARDS.filter(dash => {
    // Period filter
    let matchPeriod = true;
    if (currentPeriod !== "ALL") {
      matchPeriod = dash.period.toUpperCase() === currentPeriod;
    }

    // Category filter
    let matchCat = true;
    if (currentCategory !== "ALL") {
      matchCat = dash.category === currentCategory;
    }

    // Search filter
    let matchSearch = true;
    if (searchQuery.trim() !== "") {
      const q = searchQuery.toLowerCase();
      matchSearch = dash.title.toLowerCase().includes(q) ||
                    dash.category.toLowerCase().includes(q) ||
                    dash.desc.toLowerCase().includes(q) ||
                    dash.period.toLowerCase().includes(q);
    }

    return matchPeriod && matchCat && matchSearch;
  });

  visibleCardCount.textContent = filtered.length;

  if (filtered.length === 0) {
    cardsGrid.innerHTML = `
      <div style="grid-column: 1/-1; text-align: center; padding: 60px 20px; background: #ffffff; border-radius: 8px; border: 1px dashed #cbd5e1;">
        <i class="ri-search-eye-line" style="font-size: 42px; color: #94a3b8; margin-bottom: 12px; display: block;"></i>
        <h3 style="font-size: 16px; color: #0f172a; margin-bottom: 6px;">검색 조건과 일치하는 대시보드가 없습니다</h3>
        <p style="font-size: 13px; color: #64748b;">키워드를 변경하거나 다른 카테고리/주기 탭을 선택해 보세요.</p>
      </div>
    `;
    return;
  }

  filtered.forEach(dash => {
    const configuredUrl = getEffectiveUrl(dash);
    const hasUrl = Boolean(configuredUrl && configuredUrl.trim() !== "");

    // Use custom imageSrc if provided, otherwise render custom previewSvg
    const previewGraphic = dash.imageSrc 
      ? `<img src="${dash.imageSrc}" alt="${dash.title} Preview">`
      : dash.previewSvg;

    const periodUpper = dash.period.toUpperCase();

    const card = document.createElement("div");
    card.className = "bento-card";
    card.innerHTML = `
      <div>
        <div class="card-top">
          <span class="category-tag ${dash.categoryKey}">${dash.category}</span>
          <span class="period-badge ${dash.period.toLowerCase()}">${periodUpper}</span>
        </div>
        <div class="card-body">
          <h3 class="card-title">
            <i class="${dash.icon}" style="color: ${hasUrl ? 'var(--color-secondary)' : '#64748b'};"></i>
            ${dash.title}
          </h3>
          <p class="card-desc">${dash.desc}</p>
          <div class="card-preview-image" title="${dash.title} Dashboard Preview">
            ${previewGraphic}
          </div>
        </div>
      </div>
      <div class="card-footer">
        <span class="last-updated"><i class="ri-time-line"></i> ${dash.updated}</span>
        <button class="open-dashboard-btn ${hasUrl ? 'linked' : 'unlinked'}" data-id="${dash.id}" title="${hasUrl ? '연결된 외부 에이전트 대시보드 열기' : '미연결 (시연 대시보드열기)'}">
          <span>${hasUrl ? '대시보드열기' : '대시보드열기'}</span>
          <i class="${hasUrl ? 'ri-external-link-line' : 'ri-arrow-right-line'}"></i>
        </button>
      </div>
    `;

    cardsGrid.appendChild(card);
  });
}

// Update Sidebar Menu URL Status Indicators
function updateSidebarIndicators() {
  document.querySelectorAll(".sub-nav-item").forEach(btn => {
    const id = btn.getAttribute("data-id");
    const dash = DASHBOARDS.find(d => d.id === id);
    if (!dash) return;

    const configuredUrl = getEffectiveUrl(dash);
    const hasUrl = Boolean(configuredUrl && configuredUrl.trim() !== "");

    let dot = btn.querySelector(".url-indicator-dot");
    if (!dot) {
      dot = document.createElement("span");
      dot.className = "url-indicator-dot";
      btn.appendChild(dot);
    }

    if (hasUrl) {
      dot.className = "url-indicator-dot linked";
      dot.title = "URL 연결됨 (Live Connected)";
    } else {
      dot.className = "url-indicator-dot unlinked";
      dot.title = "URL 미설정 (Demo View)";
    }
  });
}

// Toggle Favorite Pin
function toggleFavorite(id) {
  if (favorites.includes(id)) {
    favorites = favorites.filter(item => item !== id);
  } else {
    favorites.push(id);
  }
  localStorage.setItem("portal_favorites", JSON.stringify(favorites));
  updateCounts();
  renderCards();
}

// Generate SSO Token for Sub-Dashboard Navigation
async function generateSsoUrl(baseUrl) {
  const authUser = sessionStorage.getItem(AUTH_CONFIG.SESSION_KEY) || 'LGE135';
  const ts = Date.now();
  const sig = await sha256(authUser + ":" + ts + ":" + AUTH_CONFIG.SECRET);
  const delimiter = baseUrl.includes("?") ? "&" : "?";
  return `${baseUrl}${delimiter}auth_token=${sig}&auth_ts=${ts}&auth_user=${encodeURIComponent(authUser)}`;
}

// Open Agent Viewer Overlay or External Site
async function openDashboardViewer(id) {
  const dash = DASHBOARDS.find(d => d.id === id);
  if (!dash) return;

  const configuredUrl = getEffectiveUrl(dash);

  viewerCategory.textContent = dash.category;
  viewerTitle.textContent = dash.title;

  if (configuredUrl && configuredUrl.trim() !== "") {
    // 외부 배포 URL이 등록되어 있는 경우 SSO 인증 토큰 생성 후 포털 내 포함(iframe) 뷰어로 열기
    const ssoUrl = await generateSsoUrl(configuredUrl);
    viewerExternalLink.href = ssoUrl;
    if (viewerStatusTag) {
      viewerStatusTag.innerHTML = `<i class="ri-robot-line"></i> Agent Live Connected`;
      viewerStatusTag.style.background = "rgba(13, 148, 136, 0.15)";
      viewerStatusTag.style.color = "#0D9488";
    }

    mockDashboardContainer.style.display = "none";
    agentIframe.style.display = "block";
    agentIframe.src = ssoUrl;
  } else {
    // 배포 URL이 미설정된 경우 내장 포털 시연 오버레이 뷰어 렌더링
    viewerExternalLink.href = "#";
    if (viewerStatusTag) {
      viewerStatusTag.innerHTML = `<i class="ri-slideshow-line"></i> Demo Mode`;
      viewerStatusTag.style.background = "rgba(100, 116, 139, 0.15)";
      viewerStatusTag.style.color = "#64748B";
    }

    agentIframe.style.display = "none";
    agentIframe.src = "";
    mockDashboardContainer.style.display = "block";
    renderMockDashboardContent(dash);
  }

  agentViewerOverlay.classList.add("active");
  document.body.style.overflow = "hidden";
}

// Close Agent Viewer (Return to Portal)
function closeDashboardViewer() {
  agentViewerOverlay.classList.remove("active");
  document.body.style.overflow = "auto";
  agentIframe.src = "";
}

// Render Mock Interactive Dashboard Content
function renderMockDashboardContent(dash) {
  mockDashboardContainer.innerHTML = `
    <div class="mock-dashboard-card">
      <div class="mock-dash-header">
        <div>
          <span style="font-family: var(--font-mono); font-size: 11px; color: var(--color-secondary); font-weight: 600;">AGENT DASHBOARD VIEW</span>
          <h1 class="mock-dash-title">${dash.title}</h1>
          <p style="font-size: 13px; color: var(--color-text-muted); margin-top: 4px;">${dash.desc}</p>
        </div>
        <div class="mock-dash-controls">
          <select class="mock-filter-select">
            <option>2026 YTD (Jan-Jul)</option>
            <option>2026 Q3 Forecast</option>
            <option>2025 Full Year</option>
          </select>
          <select class="mock-filter-select">
            <option>All Product Series (OLED/QNED)</option>
            <option>OLED TV Only</option>
            <option>QNED / Premium UHD</option>
          </select>
        </div>
      </div>

      <!-- KPI Summary Cards -->
      <div class="mock-kpi-row">
        <div class="mock-kpi-card">
          <div class="mock-kpi-title">주요 실적 지표</div>
          <div class="mock-kpi-num">${dash.metrics[0] ? dash.metrics[0].value : '100%'}</div>
          <div class="mock-kpi-trend up"><i class="ri-arrow-up-line"></i> +5.4% vs Last Month</div>
        </div>
        <div class="mock-kpi-card">
          <div class="mock-kpi-title">목표 달성률</div>
          <div class="mock-kpi-num">${dash.metrics[1] ? dash.metrics[1].value : '102%'}</div>
          <div class="mock-kpi-trend up"><i class="ri-arrow-up-line"></i> Target Achieved</div>
        </div>
        <div class="mock-kpi-card">
          <div class="mock-kpi-title">유럽 권역 MS / 지표</div>
          <div class="mock-kpi-num">34.2%</div>
          <div class="mock-kpi-trend up"><i class="ri-arrow-up-line"></i> Market Leader</div>
        </div>
        <div class="mock-kpi-card">
          <div class="mock-kpi-title">최근 데이터 동기화</div>
          <div class="mock-kpi-num" style="font-size: 16px;">${dash.updated}</div>
          <div class="mock-kpi-trend" style="color: var(--color-text-muted);">Agent Sync Complete</div>
        </div>
      </div>

      <!-- Interactive Mock Visualization -->
      <div class="mock-chart-placeholder">
        <i class="${dash.icon}" style="font-size: 48px; color: var(--color-secondary);"></i>
        <div style="font-family: var(--font-headline); font-size: 16px; font-weight: 600; color: var(--color-primary);">
          [${dash.title}] 에이전트 생성 심층 분석 리포트 및 그래프 시연 화면
        </div>
        <p style="font-size: 12px; max-width: 500px; text-align: center; color: var(--color-text-muted);">
          이 화면은 해당 대시보드의 에이전트 생성 뷰어입니다. 상단 우측 '에이전트 URL 관리'에서 실제 에이전트 사이트 URL을 등록하시면 해당 실소유 Web 애플리케이션으로 바로 전환됩니다.
        </p>
      </div>

      <!-- Sample Table -->
      <table class="mock-table">
        <thead>
          <tr>
            <th>구분 (Sub-segment)</th>
            <th>월간 목표 (Target)</th>
            <th>실적 (Actual)</th>
            <th>달성률 (%)</th>
            <th>YoY (%)</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>OLED TV (77"+ Large)</strong></td>
            <td class="num">12,500</td>
            <td class="num">13,240</td>
            <td class="num" style="color: var(--color-success); font-weight: 600;">105.9%</td>
            <td class="num" style="color: var(--color-success);">+18.4%</td>
          </tr>
          <tr>
            <td><strong>OLED TV (55"/65" Main)</strong></td>
            <td class="num">45,000</td>
            <td class="num">46,120</td>
            <td class="num" style="color: var(--color-success); font-weight: 600;">102.5%</td>
            <td class="num" style="color: var(--color-success);">+12.1%</td>
          </tr>
          <tr>
            <td><strong>QNED 8K / MiniLED</strong></td>
            <td class="num">8,400</td>
            <td class="num">7,980</td>
            <td class="num" style="color: var(--color-warning); font-weight: 600;">95.0%</td>
            <td class="num" style="color: var(--color-danger);">-2.4%</td>
          </tr>
        </tbody>
      </table>
    </div>
  `;
}

// Config Modal Handlers
function openConfigModal() {
  urlConfigList.innerHTML = "";
  DASHBOARDS.forEach(dash => {
    const currentUrl = getEffectiveUrl(dash);
    const isLinked = Boolean(currentUrl && currentUrl.trim() !== "");
    const item = document.createElement("div");
    item.className = "url-config-item";
    item.innerHTML = `
      <div class="url-config-label">
        <span>${dash.title} <small style="color: var(--color-text-muted);">(${dash.category})</small></span>
        <span class="url-status-badge ${isLinked ? 'linked' : 'unlinked'}">${isLinked ? '연결됨 (Live)' : '미연결 (시연 뷰어)'}</span>
      </div>
      <div class="url-input-row">
        <input type="text" class="url-config-input" data-id="${dash.id}" placeholder="URL 미설정 (외부 에이전트 URL 입력)" value="${currentUrl}" autocomplete="off" spellcheck="false">
        <button type="button" class="url-clear-btn" data-id="${dash.id}" title="URL 삭제 (시연 모드로 전환)"><i class="ri-delete-bin-line"></i> 삭제</button>
      </div>
    `;
    urlConfigList.appendChild(item);
  });

  // Attach inline clear button click listeners
  urlConfigList.querySelectorAll(".url-clear-btn").forEach(btn => {
    btn.addEventListener("click", e => {
      const id = e.currentTarget.getAttribute("data-id");
      const input = urlConfigList.querySelector(`input[data-id="${id}"]`);
      if (input) {
        input.value = "";
        const badge = input.closest(".url-config-item").querySelector(".url-status-badge");
        if (badge) {
          badge.textContent = "미연결 (시연 뷰어)";
          badge.className = "url-status-badge unlinked";
        }
      }
    });
  });

  configModalOverlay.classList.add("active");
}

function closeConfigModal() {
  configModalOverlay.classList.remove("active");
}

function saveCustomUrls() {
  try {
    const inputs = urlConfigList.querySelectorAll(".url-config-input");
    inputs.forEach(input => {
      const id = input.getAttribute("data-id");
      let val = input.value.trim();

      // Automatically prepend https:// if user entered a domain/hostname without http(s)://
      if (val && !/^https?:\/\//i.test(val)) {
        val = "https://" + val;
      }

      customUrls[id] = val; // Store explicit user value (including empty string "")
    });

    saveStoredCustomUrls(customUrls);
    closeConfigModal();
    renderCards();
    alert("에이전트 대시보드 URL 설정이 성공적으로 저장되었습니다.");
  } catch (err) {
    console.error("Save custom URLs error:", err);
    alert("URL 저장 중 오류가 발생했습니다: " + err.message);
  }
}

function resetCustomUrls() {
  if (confirm("모든 설정된 에이전트 URL을 초기화하시겠습니까?")) {
    customUrls = {};
    saveStoredCustomUrls(customUrls);
    closeConfigModal();
    renderCards();
    alert("에이전트 대시보드 URL 설정이 초기화되었습니다.");
  }
}

// Setup Event Listeners
function setupEventListeners() {
  // Home & Period Buttons
  navHome.addEventListener("click", () => {
    document.querySelectorAll(".nav-item, .sub-nav-item").forEach(el => el.classList.remove("active"));
    navHome.classList.add("active");
    currentPeriod = "ALL";
    currentCategory = "ALL";
    currentCategoryTitle.textContent = "TV 해외영업 업무지원 에이전트 리스트";
    currentCategoryDesc.textContent = "해외영업 실적, 제품 로드맵, 가격 가이드 및 GfK 시장 데이터를 통합 조회할 수 있는 에이전트 포털입니다.";
    renderCards();
  });

  if (navDaily) {
    navDaily.addEventListener("click", () => {
      document.querySelectorAll(".nav-item, .sub-nav-item").forEach(el => el.classList.remove("active"));
      navDaily.classList.add("active");
      currentPeriod = "DAILY";
      currentCategoryTitle.textContent = "Daily 업데이트 대시보드";
      currentCategoryDesc.textContent = "매일 실시간으로 업데이트되는 주요 모니터링 대시보드 모음입니다.";
      renderCards();
    });
  }

  if (navWeekly) {
    navWeekly.addEventListener("click", () => {
      document.querySelectorAll(".nav-item, .sub-nav-item").forEach(el => el.classList.remove("active"));
      navWeekly.classList.add("active");
      currentPeriod = "WEEKLY";
      currentCategoryTitle.textContent = "Weekly 주간 대시보드";
      currentCategoryDesc.textContent = "주차별 실적 및 주간 단위 분석 리포트 모음입니다.";
      renderCards();
    });
  }

  if (navMonthly) {
    navMonthly.addEventListener("click", () => {
      document.querySelectorAll(".nav-item, .sub-nav-item").forEach(el => el.classList.remove("active"));
      navMonthly.classList.add("active");
      currentPeriod = "MONTHLY";
      currentCategoryTitle.textContent = "Monthly 월간 대시보드";
      currentCategoryDesc.textContent = "월간 GfK 시장 데이터 및 월별 손익/라인업 분석 보고서 모음입니다.";
      renderCards();
    });
  }

  // Accordions Header Click (Filter Category)
  accordions.forEach(acc => {
    const header = acc.querySelector(".accordion-header");
    header.addEventListener("click", () => {
      // Toggle accordion open state
      acc.classList.toggle("open");

      const catName = header.getAttribute("data-category");
      currentCategory = catName;

      document.querySelectorAll(".nav-item, .sub-nav-item").forEach(el => el.classList.remove("active"));

      currentCategoryTitle.textContent = `${currentCategory} 대시보드`;
      currentCategoryDesc.textContent = `'${currentCategory}' 관련 핵심 분석 리포트 및 에이전트 대시보드 모음입니다.`;

      renderCards();
    });
  });

  // Sub Navigation Item Click (Open Dashboard Viewer directly)
  document.querySelectorAll(".sub-nav-item").forEach(btn => {
    btn.addEventListener("click", e => {
      e.stopPropagation();
      document.querySelectorAll(".sub-nav-item").forEach(el => el.classList.remove("active"));
      btn.classList.add("active");

      const id = btn.getAttribute("data-id");
      openDashboardViewer(id);
    });
  });

  // Executive Toolbar Category Chips Click
  const categoryChipsContainer = document.getElementById("categoryChips");
  if (categoryChipsContainer) {
    categoryChipsContainer.addEventListener("click", e => {
      const chipBtn = e.target.closest(".chip-btn");
      if (!chipBtn) return;
      const cat = chipBtn.getAttribute("data-category");
      currentCategory = cat;

      document.querySelectorAll(".nav-item, .sub-nav-item").forEach(el => el.classList.remove("active"));
      if (cat === "ALL") {
        navHome.classList.add("active");
        currentCategoryTitle.textContent = "TV 해외영업 업무지원 포털";
        currentCategoryDesc.textContent = "해외영업 실적, 제품 로드맵, 가격 가이드 및 GfK 시장 데이터를 통합 조회할 수 있는 에이전트 포털입니다.";
      } else {
        currentCategoryTitle.textContent = `${cat} 대시보드`;
        currentCategoryDesc.textContent = `'${cat}' 카테고리의 분석 리포트 및 업무 지원 에이전트 모음입니다.`;
      }
      renderCards();
    });
  }

  // Search Input
  if (searchInput) {
    searchInput.addEventListener("input", e => {
      searchQuery = e.target.value;
      if (clearSearchBtn) clearSearchBtn.style.display = searchQuery ? "block" : "none";
      renderCards();
    });
  }

  if (clearSearchBtn) {
    clearSearchBtn.addEventListener("click", () => {
      if (searchInput) searchInput.value = "";
      searchQuery = "";
      clearSearchBtn.style.display = "none";
      renderCards();
    });
  }

  // Cards Grid Pin & Open Buttons
  cardsGrid.addEventListener("click", e => {
    const pinBtn = e.target.closest(".pin-btn");
    if (pinBtn) {
      e.stopPropagation();
      const id = pinBtn.getAttribute("data-id");
      toggleFavorite(id);
      return;
    }

    const openBtn = e.target.closest(".open-dashboard-btn");
    const bentoCard = e.target.closest(".bento-card");
    
    if (openBtn) {
      openDashboardViewer(openBtn.getAttribute("data-id"));
    } else if (bentoCard) {
      const btn = bentoCard.querySelector(".open-dashboard-btn");
      if (btn) openDashboardViewer(btn.getAttribute("data-id"));
    }
  });

  // Viewer Close Actions
  closeViewerBtn.addEventListener("click", closeDashboardViewer);
  closeViewerXBtn.addEventListener("click", closeDashboardViewer);

  // Config Modal Events
  configUrlBtn.addEventListener("click", openConfigModal);
  closeConfigModalBtn.addEventListener("click", closeConfigModal);
  saveUrlsBtn.addEventListener("click", saveCustomUrls);
  resetUrlsBtn.addEventListener("click", resetCustomUrls);

  // ESC key to close Viewer or Modal
  document.addEventListener("keydown", e => {
    if (e.key === "Escape") {
      if (agentViewerOverlay.classList.contains("active")) closeDashboardViewer();
      else if (configModalOverlay.classList.contains("active")) closeConfigModal();
    }
  });
}

// Run App
document.addEventListener("DOMContentLoaded", init);

