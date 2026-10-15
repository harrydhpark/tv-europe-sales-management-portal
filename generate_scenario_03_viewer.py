# -*- coding: utf-8 -*-
"""
Generates docs/scenario_03_result_viewer.html for Scenario 03
"""
import os
import base64

DOCS_DIR = r"D:\TV 유럽영업\15. AX Task\2026 AX 실행과제\00. TV Europe Sales Management Portal\docs"
CSV_PATH = os.path.join(DOCS_DIR, "scratch_oled_pnl_summary.csv")
OUTPUT_HTML = os.path.join(DOCS_DIR, "scenario_03_result_viewer.html")

with open(CSV_PATH, "rb") as f:
    csv_b64 = base64.b64encode(f.read()).decode("utf-8")

html_content = f'''<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>시나리오 03 실전 답변 및 데이터 결과 - AXIS Master AI Agent</title>
    
    <!-- Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600;700&family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600;700&family=Noto+Sans+KR:wght@300;400;500;700&family=Noto+Serif+KR:wght@400;600;700&family=Source+Serif+4:ital,opsz,wght@0,8..60,400..700;1,8..60,400..700&display=swap" rel="stylesheet">
    
    <!-- Icons -->
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200" />
    <link href="https://cdn.jsdelivr.net/npm/remixicon@4.3.0/fonts/remixicon.css" rel="stylesheet" />

    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {{
            theme: {{
                extend: {{
                    fontFamily: {{
                        sans: ['Inter', 'Noto Sans KR', 'sans-serif'],
                        headline: ['Source Serif 4', 'Noto Serif KR', 'serif'],
                        mono: ['JetBrains Mono', 'monospace'],
                    }},
                    colors: {{
                        primary: '#1B365D',
                        secondary: '#008080',
                    }}
                }}
            }}
        }}
    </script>

    <style>
        body {{
            background-color: #F8FAFC;
            color: #1E293B;
            font-family: 'Inter', 'Noto Sans KR', sans-serif;
            -webkit-font-smoothing: antialiased;
        }}
        .font-mono-num {{
            font-family: 'JetBrains Mono', monospace;
            font-variant-numeric: tabular-nums;
        }}
        table.custom-matrix-table th {{
            background-color: #1B365D !important;
            color: #FFFFFF !important;
            font-size: 0.72rem !important;
            font-weight: 700 !important;
            text-transform: none !important;
            letter-spacing: normal !important;
            border-bottom: 2px solid #0F2027 !important;
            line-height: 1.35 !important;
        }}
        table.custom-matrix-table th.th-highlight {{
            background-color: #244677 !important;
            color: #FFFFFF !important;
        }}
        table.custom-matrix-table td {{
            font-size: 0.72rem !important;
            border-color: #E2E8F0 !important;
        }}
    </style>
</head>
<body class="bg-slate-50 min-h-screen pb-16">

    <!-- Top Fixed Navigation Bar -->
    <header class="sticky top-0 z-50 bg-[#051c2c] text-white border-b border-slate-700/80 shadow-md">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 h-14 flex items-center justify-between gap-4">
            
            <!-- Left: Back Button & Context Info -->
            <div class="flex items-center gap-3">
                <button type="button" 
                        onclick="returnToGuide()"
                        class="px-3 py-1.5 rounded-lg bg-teal-600 hover:bg-teal-500 text-white text-xs font-bold flex items-center gap-1.5 transition-all shadow-xs hover:scale-105 active:scale-95 group">
                    <span class="material-symbols-outlined text-base group-hover:-translate-x-0.5 transition-transform">arrow_back</span>
                    <span>가이드로 돌아가기</span>
                </button>
                <div class="h-4 w-px bg-slate-700 hidden sm:block"></div>
                <div class="flex items-center gap-2">
                    <span class="px-2 py-0.5 rounded bg-blue-900/80 text-blue-300 text-[10px] font-bold border border-blue-700/60 hidden md:inline">실전 질의 시나리오 03</span>
                    <h1 class="text-sm font-bold text-white tracking-tight truncate">법인별 OLED TV 내 W / G / C / B 시리즈 매출 비중 및 영업이익율·한계이익율 분석 실전 결과</h1>
                </div>
            </div>

            <!-- Right: Actions -->
            <div class="flex items-center gap-2">
                <button type="button" 
                        onclick="downloadScenarioCsv()"
                        class="px-3 py-1.5 rounded-lg bg-blue-600 hover:bg-blue-500 text-white text-xs font-bold flex items-center gap-1.5 shadow-sm transition-all hover:scale-105 active:scale-95">
                    <span class="material-symbols-outlined text-sm">download</span>
                    <span class="hidden sm:inline">CSV 데이터 다운로드 (scratch_oled_pnl_summary.csv)</span>
                    <span class="sm:hidden">CSV 다운로드</span>
                </button>
                <button type="button" 
                        onclick="window.print()"
                        class="px-2.5 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 hover:text-white text-xs font-medium flex items-center gap-1 transition-all border border-slate-700">
                    <span class="material-symbols-outlined text-sm">print</span>
                    <span class="hidden md:inline">인쇄 / PDF</span>
                </button>
            </div>
        </div>
    </header>

    <!-- Main Content Container -->
    <main class="max-w-7xl mx-auto px-4 sm:px-6 pt-6 space-y-6">
        
        <!-- Breadcrumb & Title Banner -->
        <div class="bg-white rounded-xl border border-slate-200 shadow-xs p-6 space-y-3">
            <div class="flex items-center gap-2 text-xs text-slate-500">
                <span>AXIS 시스템 가이드</span>
                <span class="material-symbols-outlined text-xs">chevron_right</span>
                <span>6. 실무 활용 예시</span>
                <span class="material-symbols-outlined text-xs">chevron_right</span>
                <span class="font-bold text-blue-700">시나리오 03 실전 답변 상세 결과</span>
            </div>
            <div class="flex flex-wrap items-center justify-between gap-3">
                <div>
                    <h2 class="text-xl font-headline font-bold text-slate-900">법인별 OLED TV 내 W / G / C / B 시리즈 매출 비중 및 영업이익율·한계이익율 분석 실전 결과</h2>
                    <p class="text-xs text-slate-600 mt-1">LGE 유럽영업본부 공식 NERP 관리회계 시스템(05. TV P&L Analysis)의 2026년 1~8월 누적 실적 원천 데이터베이스를 기반으로 전수 산출된 마스터 에이전트 실전 답변 원문입니다.</p>
                </div>
                <div class="flex items-center gap-2 text-xs bg-slate-50 px-3 py-1.5 rounded-lg border border-slate-200">
                    <span class="w-2.5 h-2.5 rounded-full bg-emerald-500 animate-pulse"></span>
                    <span class="text-slate-600">소요 시간: <strong class="text-blue-700 font-mono">10초</strong></span>
                    <span class="text-slate-300">|</span>
                    <span class="text-slate-600">분석 범위: <strong class="text-slate-800">유럽 16개국 판매법인 및 CIS(러시아) NERP 원천 DB 전수</strong></span>
                </div>
            </div>

            <!-- Original Query Chip -->
            <div class="p-3 rounded-lg bg-blue-50/50 border border-blue-100 flex items-center justify-between text-xs font-mono text-slate-800 gap-2">
                <div class="flex items-center gap-2 truncate">
                    <span class="px-2 py-0.5 rounded bg-blue-600 text-white text-[10px] font-bold font-sans">실전 질의</span>
                    <span class="truncate">"법인별로 OLED TV 내 W / G / C 시리즈 매출 비중과 영업이익율, 한계이익율을 정리해줘"</span>
                </div>
                <span class="px-2 py-0.5 rounded bg-slate-200/80 text-slate-700 text-[10px] font-sans font-medium whitespace-nowrap">원천 CSV 파일 동봉</span>
            </div>
        </div>

        <!-- Download Banner Card -->
        <div class="bg-gradient-to-r from-blue-900 to-slate-900 text-white rounded-xl p-5 shadow-sm flex flex-col md:flex-row items-center justify-between gap-4">
            <div class="flex items-center gap-3.5">
                <div class="w-12 h-12 rounded-xl bg-blue-500/20 border border-blue-400/30 flex items-center justify-center shrink-0">
                    <span class="material-symbols-outlined text-blue-300 text-2xl">table_chart</span>
                </div>
                <div>
                    <div class="flex items-center gap-2">
                        <span class="text-sm font-bold text-white">첨부 파일: scratch_oled_pnl_summary.csv</span>
                        <span class="text-[10px] bg-blue-500/30 text-blue-200 px-2 py-0.5 rounded font-mono border border-blue-400/30">16.9 KB</span>
                    </div>
                    <p class="text-xs text-slate-300 mt-0.5">유럽 16개 판매법인/지점 및 CIS 전체 OLED 시리즈별 순매출, 비중, 영업이익, COI%, 한계이익, MP%, 수량, ASP 전수 원천 집계 데이터</p>
                </div>
            </div>
            <button type="button" 
                    onclick="downloadScenarioCsv()"
                    class="w-full md:w-auto px-5 py-2.5 rounded-lg bg-blue-500 hover:bg-blue-400 text-white text-xs font-bold flex items-center justify-center gap-2 transition-all shadow-md shrink-0 hover:scale-105 active:scale-95">
                <span class="material-symbols-outlined text-base">download</span>
                <span>scratch_oled_pnl_summary.csv 다운로드</span>
            </button>
        </div>

        <!-- Master Agent Response Card -->
        <div class="bg-white rounded-xl border border-slate-200 shadow-sm p-6 sm:p-8 space-y-8">
            
            <!-- Agent Header -->
            <div class="flex items-center justify-between border-b border-slate-200 pb-4">
                <div class="flex items-center gap-3">
                    <div class="w-9 h-9 rounded-xl bg-primary text-white flex items-center justify-center font-bold text-sm shadow-xs">
                        <span class="material-symbols-outlined text-lg">smart_toy</span>
                    </div>
                    <div>
                        <div class="flex items-center gap-2">
                            <h3 class="text-sm font-bold text-slate-900">Master AI Agent 실전 응답</h3>
                            <span class="px-2 py-0.5 rounded-full bg-emerald-100 text-emerald-800 text-[10px] font-bold">검증 완료 (Verified)</span>
                        </div>
                        <p class="text-[11px] text-slate-500">연계 에이전트: TV P&L Analysis Agent, Financial Analyst | 데이터 기준: 2026년 1~8월 누적 실적 (USD)</p>
                    </div>
                </div>
                <span class="text-xs font-mono text-slate-400">2026-10-07 09:22:10 KST</span>
            </div>

            <!-- Content Area: Exactly starting from '1. 유럽 16개국 통합 요약 (Pan-European Aggregate)' -->
            <div class="space-y-8 text-slate-800 text-xs sm:text-sm leading-relaxed">
                
                <!-- Section 1 -->
                <section class="space-y-4">
                    <div class="border-b border-slate-200 pb-2">
                        <h4 class="text-base sm:text-lg font-bold text-slate-900 flex items-center gap-2">
                            <span class="w-6 h-6 rounded-md bg-blue-100 text-blue-700 flex items-center justify-center text-xs font-bold font-mono">1</span>
                            <span>유럽 16개국 통합 요약 (Pan-European Aggregate)</span>
                        </h4>
                    </div>
                    <p class="text-xs sm:text-sm text-slate-600 leading-relaxed">
                        2026년 1~8월 누적 유럽 16개 판매법인/지점의 OLED TV 총 순매출은 <strong>$706.8M (755,380대, ASP $936)</strong>이며, <strong>영업이익 $33.48M (COI% +4.7%)</strong>, <strong>한계이익 $181.80M (MP% +25.7%)</strong>을 달성하였습니다.
                    </p>

                    <div class="overflow-x-auto rounded-lg border border-slate-200 shadow-2xs">
                        <table class="w-full text-left border-collapse custom-matrix-table">
                            <thead>
                                <tr>
                                    <th class="p-2.5 text-center">시리즈 구분</th>
                                    <th class="p-2.5 text-right">순매출액 (USD)</th>
                                    <th class="p-2.5 text-right th-highlight">OLED 내 매출비중</th>
                                    <th class="p-2.5 text-right">영업이익 (COI)</th>
                                    <th class="p-2.5 text-right th-highlight">영업이익율 (COI%)</th>
                                    <th class="p-2.5 text-right">한계이익 (MP)</th>
                                    <th class="p-2.5 text-right th-highlight">한계이익율 (MP%)</th>
                                    <th class="p-2.5 text-right">판매수량 (대)</th>
                                    <th class="p-2.5 text-right">평균 ASP</th>
                                </tr>
                            </thead>
                            <tbody class="divide-y divide-slate-200 font-mono-num text-xs">
                                <tr class="hover:bg-slate-50 transition-colors">
                                    <td class="p-2.5 font-bold text-slate-900 font-sans">W 시리즈 (Wireless)</td>
                                    <td class="p-2.5 text-right">$3,867,728</td>
                                    <td class="p-2.5 text-right font-bold text-blue-700 bg-blue-50/30">0.5%</td>
                                    <td class="p-2.5 text-right text-emerald-700 font-bold">+$649,862</td>
                                    <td class="p-2.5 text-right font-bold text-emerald-700 bg-emerald-50/30">+16.8%</td>
                                    <td class="p-2.5 text-right">$1,431,188</td>
                                    <td class="p-2.5 text-right font-bold text-emerald-700 bg-emerald-50/30">+37.0%</td>
                                    <td class="p-2.5 text-right">1,533</td>
                                    <td class="p-2.5 text-right font-bold">$2,523</td>
                                </tr>
                                <tr class="hover:bg-slate-50 transition-colors bg-amber-50/15">
                                    <td class="p-2.5 font-bold text-slate-900 font-sans flex items-center gap-1.5">
                                        <span class="w-2 h-2 rounded-full bg-amber-500"></span>
                                        <span>G 시리즈 (Gallery)</span>
                                    </td>
                                    <td class="p-2.5 text-right font-bold">$207,614,449</td>
                                    <td class="p-2.5 text-right font-bold text-amber-700 bg-amber-50/30">29.4%</td>
                                    <td class="p-2.5 text-right text-emerald-700 font-bold">+$25,867,618</td>
                                    <td class="p-2.5 text-right font-bold text-emerald-700 bg-emerald-50/30">+12.5%</td>
                                    <td class="p-2.5 text-right">$67,354,324</td>
                                    <td class="p-2.5 text-right font-bold text-emerald-700 bg-emerald-50/30">+32.4%</td>
                                    <td class="p-2.5 text-right">155,929</td>
                                    <td class="p-2.5 text-right font-bold">$1,331</td>
                                </tr>
                                <tr class="hover:bg-slate-50 transition-colors bg-blue-50/15">
                                    <td class="p-2.5 font-bold text-slate-900 font-sans flex items-center gap-1.5">
                                        <span class="w-2 h-2 rounded-full bg-blue-500"></span>
                                        <span>C 시리즈 (Core Main)</span>
                                    </td>
                                    <td class="p-2.5 text-right font-bold">$378,774,320</td>
                                    <td class="p-2.5 text-right font-bold text-blue-700 bg-blue-50/30">53.6%</td>
                                    <td class="p-2.5 text-right text-emerald-700 font-bold">+$8,659,211</td>
                                    <td class="p-2.5 text-right font-bold text-emerald-700 bg-emerald-50/30">+2.3%</td>
                                    <td class="p-2.5 text-right">$89,776,957</td>
                                    <td class="p-2.5 text-right font-bold text-emerald-700 bg-emerald-50/30">+23.7%</td>
                                    <td class="p-2.5 text-right">435,970</td>
                                    <td class="p-2.5 text-right font-bold">$869</td>
                                </tr>
                                <tr class="hover:bg-slate-50 transition-colors">
                                    <td class="p-2.5 font-bold text-slate-900 font-sans">B 시리즈 (Entry)</td>
                                    <td class="p-2.5 text-right">$115,107,383</td>
                                    <td class="p-2.5 text-right font-bold text-slate-700 bg-slate-50/50">16.3%</td>
                                    <td class="p-2.5 text-right text-rose-600 font-bold">-$2,183,234</td>
                                    <td class="p-2.5 text-right font-bold text-rose-600 bg-rose-50/30">-1.9%</td>
                                    <td class="p-2.5 text-right">$22,513,978</td>
                                    <td class="p-2.5 text-right font-bold text-emerald-700 bg-emerald-50/30">+19.6%</td>
                                    <td class="p-2.5 text-right">161,576</td>
                                    <td class="p-2.5 text-right font-bold">$712</td>
                                </tr>
                                <tr class="hover:bg-slate-50 transition-colors">
                                    <td class="p-2.5 font-medium text-slate-600 font-sans">기타 (M/T/A/Z)</td>
                                    <td class="p-2.5 text-right">$1,461,802</td>
                                    <td class="p-2.5 text-right text-slate-500">0.2%</td>
                                    <td class="p-2.5 text-right text-emerald-700 font-bold">+$485,192</td>
                                    <td class="p-2.5 text-right font-bold text-emerald-700">+33.2%</td>
                                    <td class="p-2.5 text-right">$722,232</td>
                                    <td class="p-2.5 text-right font-bold text-emerald-700">+49.4%</td>
                                    <td class="p-2.5 text-right">372</td>
                                    <td class="p-2.5 text-right font-bold">$3,930</td>
                                </tr>
                                <tr class="bg-slate-100 font-bold text-slate-900 border-t-2 border-slate-300">
                                    <td class="p-2.5 font-sans">유럽 16개국 합계</td>
                                    <td class="p-2.5 text-right font-bold text-primary">$706,825,682</td>
                                    <td class="p-2.5 text-right font-bold text-primary">100.0%</td>
                                    <td class="p-2.5 text-right font-bold text-emerald-700">+$33,478,649</td>
                                    <td class="p-2.5 text-right font-bold text-emerald-700">+4.7%</td>
                                    <td class="p-2.5 text-right font-bold text-primary">$181,798,679</td>
                                    <td class="p-2.5 text-right font-bold text-emerald-700">+25.7%</td>
                                    <td class="p-2.5 text-right font-bold">755,380</td>
                                    <td class="p-2.5 text-right font-bold">$936</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </section>

                <!-- Section 2 -->
                <section class="space-y-4">
                    <div class="border-b border-slate-200 pb-2">
                        <h4 class="text-base sm:text-lg font-bold text-slate-900 flex items-center gap-2">
                            <span class="w-6 h-6 rounded-md bg-blue-100 text-blue-700 flex items-center justify-center text-xs font-bold font-mono">2</span>
                            <span>핵심 3대 전략 진단</span>
                        </h4>
                    </div>

                    <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                        <div class="p-4 rounded-xl bg-amber-50/40 border border-amber-200/80 space-y-2">
                            <div class="flex items-center gap-2 text-amber-800 font-bold text-sm">
                                <span class="material-symbols-outlined text-base">monetization_on</span>
                                <span>1) G 시리즈의 압도적 영업이익 기여 (전체의 77.3% 창출)</span>
                            </div>
                            <p class="text-xs text-slate-700 leading-relaxed">
                                G 시리즈는 전체 OLED 매출의 29.4%($207.6M)를 차지하지만, 유럽 OLED 전체 영업이익($33.48M) 중 <strong>77.3%($25.87M)</strong>를 창출하는 절대적 캐시카우입니다. 영국(+17.9%), 독일(+15.8%), 이탈리아(+15.7%), 스위스(+16.6%), 라트비아(+22.8%), 폴란드(+21.0%) 등 대다수 법인에서 두 자릿수 영업이익율을 안정적으로 수성하고 있습니다.
                            </p>
                        </div>

                        <div class="p-4 rounded-xl bg-blue-50/40 border border-blue-200/80 space-y-2">
                            <div class="flex items-center gap-2 text-blue-800 font-bold text-sm">
                                <span class="material-symbols-outlined text-base">donut_large</span>
                                <span>2) C 시리즈의 볼륨 지배력 및 유통별 손익 차별화</span>
                            </div>
                            <p class="text-xs text-slate-700 leading-relaxed">
                                매출의 53.6%($378.8M), 수량의 57.7%(43.6만대)를 견인하는 주력 엔진으로, 한계이익율 +23.7%($89.8M)를 통해 고정비 회수에 결정적 기여를 하고 있습니다. 단, 영국(+6.8%), 스위스(+6.3%), 독일(+5.3%), 폴란드(+5.7%) 등 흑자 법인과 프랑스(-10.6%), 이탈리아(-6.1%), 그리스(-4.0%) 등 가격 격전지 법인 간의 손익 양극화가 뚜렷합니다.
                            </p>
                        </div>

                        <div class="p-4 rounded-xl bg-rose-50/40 border border-rose-200/80 space-y-2">
                            <div class="flex items-center gap-2 text-rose-800 font-bold text-sm">
                                <span class="material-symbols-outlined text-base">trending_down</span>
                                <span>3) B 시리즈의 가격 압박 및 업셀링(Up-selling) 과제</span>
                            </div>
                            <p class="text-xs text-slate-700 leading-relaxed">
                                B 시리즈는 매출 비중 16.3%($115.1M)에 영업이익 -1.9%(-$2.18M)로 손실을 기록하고 있으나, 한계이익율은 +19.6%($22.5M)로 양호합니다. B 시리즈 공급 물량을 타이트하게 캡핑(Capping)하고, 매장에서 C/G 시리즈로 상향 구매를 유도하는 가격 사다리 전략이 필수적입니다.
                            </p>
                        </div>

                        <div class="p-4 rounded-xl bg-emerald-50/40 border border-emerald-200/80 space-y-2">
                            <div class="flex items-center gap-2 text-emerald-800 font-bold text-sm">
                                <span class="material-symbols-outlined text-base">workspace_premium</span>
                                <span>4) W 시리즈의 초고수익 프리미엄 상징성</span>
                            </div>
                            <p class="text-xs text-slate-700 leading-relaxed">
                                매출 비중은 0.5%($3.87M)이나, 영업이익율 <strong>+16.8%</strong>, 한계이익율 <strong>+37.0%</strong>, ASP <strong>$2,523</strong>을 기록하며 무선 OLED의 초프리미엄 수익성을 입증하였습니다.
                            </p>
                        </div>
                    </div>
                </section>

                <!-- Section 3 -->
                <section class="space-y-6">
                    <div class="border-b border-slate-200 pb-2">
                        <h4 class="text-base sm:text-lg font-bold text-slate-900 flex items-center gap-2">
                            <span class="w-6 h-6 rounded-md bg-blue-100 text-blue-700 flex items-center justify-center text-xs font-bold font-mono">3</span>
                            <span>법인/지점별 OLED 시리즈 손익 상세 비교 매트릭스</span>
                        </h4>
                    </div>

                    <!-- 3.1 Sales Mix Table -->
                    <div class="space-y-2">
                        <div class="flex items-center justify-between">
                            <h5 class="text-xs sm:text-sm font-bold text-slate-800">📊 3.1 매출 비중 (Sales Mix %) 비교표</h5>
                            <span class="text-[11px] text-slate-500">*각 법인의 OLED 전체 순매출 100% 대비 시리즈별 비중</span>
                        </div>
                        <div class="overflow-x-auto rounded-lg border border-slate-200 shadow-2xs">
                            <table class="w-full text-left border-collapse custom-matrix-table">
                                <thead>
                                    <tr>
                                        <th class="p-2 text-center">법인/지점</th>
                                        <th class="p-2">국가명</th>
                                        <th class="p-2 text-right">W 시리즈</th>
                                        <th class="p-2 text-right th-highlight">G 시리즈</th>
                                        <th class="p-2 text-right th-highlight">C 시리즈</th>
                                        <th class="p-2 text-right">B 시리즈</th>
                                        <th class="p-2 text-right">기타 OLED</th>
                                        <th class="p-2 text-right">전체 합계</th>
                                    </tr>
                                </thead>
                                <tbody class="divide-y divide-slate-200 font-mono-num text-xs">
                                    <tr class="hover:bg-slate-50"><td class="p-2 text-center font-bold text-primary">UK</td><td class="p-2 font-sans font-medium">영국 (United Kingdom)</td><td class="p-2 text-right">0.5%</td><td class="p-2 text-right font-bold text-amber-700 bg-amber-50/20">32.2%</td><td class="p-2 text-right font-bold text-blue-700 bg-blue-50/20">51.6%</td><td class="p-2 text-right">15.2%</td><td class="p-2 text-right">0.5%</td><td class="p-2 text-right font-bold">100.0%</td></tr>
                                    <tr class="hover:bg-slate-50"><td class="p-2 text-center font-bold text-primary">FS</td><td class="p-2 font-sans font-medium">프랑스 (France)</td><td class="p-2 text-right">1.0%</td><td class="p-2 text-right font-bold text-amber-700 bg-amber-50/20">33.1%</td><td class="p-2 text-right font-bold text-blue-700 bg-blue-50/20">51.4%</td><td class="p-2 text-right">14.3%</td><td class="p-2 text-right">0.2%</td><td class="p-2 text-right font-bold">100.0%</td></tr>
                                    <tr class="hover:bg-slate-50"><td class="p-2 text-center font-bold text-primary">IS</td><td class="p-2 font-sans font-medium">이탈리아 (Italy)</td><td class="p-2 text-right">0.6%</td><td class="p-2 text-right font-bold text-amber-700 bg-amber-50/20">31.7%</td><td class="p-2 text-right font-bold text-blue-700 bg-blue-50/20">41.1%</td><td class="p-2 text-right font-bold text-rose-700">26.6%</td><td class="p-2 text-right">-0.0%</td><td class="p-2 text-right font-bold">100.0%</td></tr>
                                    <tr class="hover:bg-slate-50"><td class="p-2 text-center font-bold text-primary">ES</td><td class="p-2 font-sans font-medium">스페인 (Spain)</td><td class="p-2 text-right">0.0%</td><td class="p-2 text-right font-bold text-amber-700 bg-amber-50/20">26.2%</td><td class="p-2 text-right font-bold text-blue-700 bg-blue-50/20">57.8%</td><td class="p-2 text-right">15.4%</td><td class="p-2 text-right">0.6%</td><td class="p-2 text-right font-bold">100.0%</td></tr>
                                    <tr class="hover:bg-slate-50"><td class="p-2 text-center font-bold text-primary">SW</td><td class="p-2 font-sans font-medium">스웨덴/노르딕 (Sweden)</td><td class="p-2 text-right">0.4%</td><td class="p-2 text-right font-bold text-amber-700 bg-amber-50/20">26.1%</td><td class="p-2 text-right font-bold text-blue-700 bg-blue-50/20">56.8%</td><td class="p-2 text-right">16.7%</td><td class="p-2 text-right">-0.0%</td><td class="p-2 text-right font-bold">100.0%</td></tr>
                                    <tr class="hover:bg-slate-50"><td class="p-2 text-center font-bold text-primary">DG</td><td class="p-2 font-sans font-medium">독일 (Germany)</td><td class="p-2 text-right">0.0%</td><td class="p-2 text-right font-bold text-amber-700 bg-amber-50/20">27.3%</td><td class="p-2 text-right font-bold text-blue-700 bg-blue-50/20">60.8%</td><td class="p-2 text-right">11.9%</td><td class="p-2 text-right">0.0%</td><td class="p-2 text-right font-bold">100.0%</td></tr>
                                    <tr class="hover:bg-slate-50"><td class="p-2 text-center font-bold text-primary">BN</td><td class="p-2 font-sans font-medium">베네룩스 (Benelux)</td><td class="p-2 text-right">0.9%</td><td class="p-2 text-right font-bold text-amber-700 bg-amber-50/20">40.3%</td><td class="p-2 text-right font-bold text-blue-700 bg-blue-50/20">45.5%</td><td class="p-2 text-right">13.4%</td><td class="p-2 text-right">-0.1%</td><td class="p-2 text-right font-bold">100.0%</td></tr>
                                    <tr class="hover:bg-slate-50"><td class="p-2 text-center font-bold text-primary">PL</td><td class="p-2 font-sans font-medium">폴란드 (Poland)</td><td class="p-2 text-right">0.3%</td><td class="p-2 text-right font-bold text-amber-700 bg-amber-50/20">14.6%</td><td class="p-2 text-right font-bold text-blue-700 bg-blue-50/20">61.4%</td><td class="p-2 text-right font-bold text-rose-700">23.7%</td><td class="p-2 text-right">0.0%</td><td class="p-2 text-right font-bold">100.0%</td></tr>
                                    <tr class="hover:bg-slate-50"><td class="p-2 text-center font-bold text-primary">MK</td><td class="p-2 font-sans font-medium">헝가리 (Hungary)</td><td class="p-2 text-right">0.7%</td><td class="p-2 text-right font-bold text-amber-700 bg-amber-50/20">20.4%</td><td class="p-2 text-right font-bold text-blue-700 bg-blue-50/20">65.3%</td><td class="p-2 text-right">13.6%</td><td class="p-2 text-right">-0.0%</td><td class="p-2 text-right font-bold">100.0%</td></tr>
                                    <tr class="hover:bg-slate-50"><td class="p-2 text-center font-bold text-primary">Swiss</td><td class="p-2 font-sans font-medium">스위스 (Switzerland)</td><td class="p-2 text-right font-bold text-blue-600">1.3%</td><td class="p-2 text-right font-bold text-amber-700 bg-amber-50/20">25.2%</td><td class="p-2 text-right font-bold text-blue-700 bg-blue-50/20">58.9%</td><td class="p-2 text-right">14.3%</td><td class="p-2 text-right">0.3%</td><td class="p-2 text-right font-bold">100.0%</td></tr>
                                    <tr class="hover:bg-slate-50"><td class="p-2 text-center font-bold text-primary">LA</td><td class="p-2 font-sans font-medium">라트비아/발틱 (Latvia)</td><td class="p-2 text-right">0.2%</td><td class="p-2 text-right font-bold text-amber-700 bg-amber-50/20">38.4%</td><td class="p-2 text-right font-bold text-blue-700 bg-blue-50/20">61.1%</td><td class="p-2 text-right">0.4%</td><td class="p-2 text-right">0.0%</td><td class="p-2 text-right font-bold">100.0%</td></tr>
                                    <tr class="hover:bg-slate-50"><td class="p-2 text-center font-bold text-primary">AG</td><td class="p-2 font-sans font-medium">오스트리아 (Austria)</td><td class="p-2 text-right">0.6%</td><td class="p-2 text-right font-bold text-amber-700 bg-amber-50/20">28.5%</td><td class="p-2 text-right font-bold text-blue-700 bg-blue-50/20">57.7%</td><td class="p-2 text-right">13.2%</td><td class="p-2 text-right">0.0%</td><td class="p-2 text-right font-bold">100.0%</td></tr>
                                    <tr class="hover:bg-slate-50"><td class="p-2 text-center font-bold text-primary">PT</td><td class="p-2 font-sans font-medium">포르투갈 (Portugal)</td><td class="p-2 text-right">0.7%</td><td class="p-2 text-right font-bold text-amber-700 bg-amber-50/20">27.1%</td><td class="p-2 text-right font-bold text-blue-700 bg-blue-50/20">45.8%</td><td class="p-2 text-right font-bold text-rose-700">25.7%</td><td class="p-2 text-right">0.7%</td><td class="p-2 text-right font-bold">100.0%</td></tr>
                                    <tr class="hover:bg-slate-50"><td class="p-2 text-center font-bold text-primary">CK</td><td class="p-2 font-sans font-medium">체코 (Czech)</td><td class="p-2 text-right">0.3%</td><td class="p-2 text-right font-bold text-amber-700 bg-amber-50/20">13.5%</td><td class="p-2 text-right font-bold text-blue-700 bg-blue-50/20">61.7%</td><td class="p-2 text-right font-bold text-rose-700">24.3%</td><td class="p-2 text-right">0.2%</td><td class="p-2 text-right font-bold">100.0%</td></tr>
                                    <tr class="hover:bg-slate-50"><td class="p-2 text-center font-bold text-primary">RO</td><td class="p-2 font-sans font-medium">루마니아 (Romania)</td><td class="p-2 text-right font-bold text-blue-600">1.1%</td><td class="p-2 text-right font-bold text-amber-700 bg-amber-50/20">26.7%</td><td class="p-2 text-right font-bold text-blue-700 bg-blue-50/20">54.4%</td><td class="p-2 text-right">17.8%</td><td class="p-2 text-right">0.0%</td><td class="p-2 text-right font-bold">100.0%</td></tr>
                                    <tr class="hover:bg-slate-50"><td class="p-2 text-center font-bold text-primary">HS</td><td class="p-2 font-sans font-medium">그리스 (Greece)</td><td class="p-2 text-right">0.6%</td><td class="p-2 text-right font-bold text-amber-700 bg-amber-50/20">32.7%</td><td class="p-2 text-right font-bold text-blue-700 bg-blue-50/20">47.1%</td><td class="p-2 text-right">19.1%</td><td class="p-2 text-right">0.4%</td><td class="p-2 text-right font-bold">100.0%</td></tr>
                                    <tr class="bg-slate-100 font-bold text-slate-900 border-t-2 border-slate-300"><td class="p-2 text-center font-sans">EU16</td><td class="p-2 font-sans">유럽 16개국 평균/합계</td><td class="p-2 text-right">0.5%</td><td class="p-2 text-right text-amber-800">29.4%</td><td class="p-2 text-right text-blue-800">53.6%</td><td class="p-2 text-right">16.3%</td><td class="p-2 text-right">0.2%</td><td class="p-2 text-right font-bold">100.0%</td></tr>
                                    <tr class="text-slate-500 italic bg-slate-50/60"><td class="p-2 text-center font-sans">RA</td><td class="p-2 font-sans">러시아 (Russia, 참고)</td><td class="p-2 text-right">-0.0%</td><td class="p-2 text-right">31.4%</td><td class="p-2 text-right">57.0%</td><td class="p-2 text-right">11.6%</td><td class="p-2 text-right">-0.0%</td><td class="p-2 text-right">100.0%</td></tr>
                                </tbody>
                            </table>
                        </div>
                    </div>

                    <!-- 3.2 COI% & MP% Table -->
                    <div class="space-y-2 pt-4">
                        <div class="flex items-center justify-between">
                            <h5 class="text-xs sm:text-sm font-bold text-slate-800">📈 3.2 영업이익율 (COI %) 및 한계이익율 (MP %) 비교표</h5>
                            <span class="text-[11px] text-slate-500">*각 시리즈별 순매출 대비 마진율 (COI% / MP%)</span>
                        </div>
                        <div class="overflow-x-auto rounded-lg border border-slate-200 shadow-2xs">
                            <table class="w-full text-left border-collapse custom-matrix-table">
                                <thead>
                                    <tr>
                                        <th class="p-2 text-center">법인/지점</th>
                                        <th class="p-2">국가명</th>
                                        <th class="p-2 text-center">W 시리즈 (COI% / MP%)</th>
                                        <th class="p-2 text-center th-highlight">G 시리즈 (COI% / MP%)</th>
                                        <th class="p-2 text-center th-highlight">C 시리즈 (COI% / MP%)</th>
                                        <th class="p-2 text-center">B 시리즈 (COI% / MP%)</th>
                                        <th class="p-2 text-center th-highlight">OLED 전체 (COI% / MP%)</th>
                                    </tr>
                                </thead>
                                <tbody class="divide-y divide-slate-200 font-mono-num text-xs">
                                    <tr class="hover:bg-slate-50"><td class="p-2 text-center font-bold text-primary">UK</td><td class="p-2 font-sans font-medium">영국 (United Kingdom)</td><td class="p-2 text-center text-emerald-700 font-bold">+34.3% / 51.2%</td><td class="p-2 text-center font-bold text-emerald-700 bg-amber-50/20">+17.9% / 37.2%</td><td class="p-2 text-center font-bold text-emerald-700 bg-blue-50/20">+6.8% / 27.7%</td><td class="p-2 text-center text-emerald-700 font-bold">+9.6% / 29.0%</td><td class="p-2 text-center font-bold text-emerald-700 bg-slate-100">+11.2% / 31.3%</td></tr>
                                    <tr class="hover:bg-slate-50"><td class="p-2 text-center font-bold text-primary">FS</td><td class="p-2 font-sans font-medium">프랑스 (France)</td><td class="p-2 text-center text-emerald-700 font-bold">+9.6% / 32.0%</td><td class="p-2 text-center font-bold text-emerald-700 bg-amber-50/20">+2.5% / 27.8%</td><td class="p-2 text-center font-bold text-rose-600 bg-blue-50/20">-10.6% / 16.4%</td><td class="p-2 text-center text-rose-600 font-bold">-2.2% / 23.8%</td><td class="p-2 text-center font-bold text-rose-600 bg-slate-100">-4.8% / 21.4%</td></tr>
                                    <tr class="hover:bg-slate-50"><td class="p-2 text-center font-bold text-primary">IS</td><td class="p-2 font-sans font-medium">이탈리아 (Italy)</td><td class="p-2 text-center text-emerald-700 font-bold">+24.9% / 42.0%</td><td class="p-2 text-center font-bold text-emerald-700 bg-amber-50/20">+15.7% / 34.1%</td><td class="p-2 text-center font-bold text-rose-600 bg-blue-50/20">-6.1% / 16.6%</td><td class="p-2 text-center text-rose-600 font-bold">-8.8% / 12.1%</td><td class="p-2 text-center font-bold text-emerald-700 bg-slate-100">+0.3% / 21.1%</td></tr>
                                    <tr class="hover:bg-slate-50"><td class="p-2 text-center font-bold text-primary">ES</td><td class="p-2 font-sans font-medium">스페인 (Spain)</td><td class="p-2 text-center text-slate-400">- / -</td><td class="p-2 text-center font-bold text-rose-600 bg-amber-50/20">-4.5% / 16.5%</td><td class="p-2 text-center font-bold text-emerald-700 bg-blue-50/20">+2.1% / 23.3%</td><td class="p-2 text-center text-emerald-700 font-bold">+1.6% / 22.5%</td><td class="p-2 text-center font-bold text-emerald-700 bg-slate-100">+0.3% / 21.4%</td></tr>
                                    <tr class="hover:bg-slate-50"><td class="p-2 text-center font-bold text-primary">SW</td><td class="p-2 font-sans font-medium">스웨덴/노르딕 (Sweden)</td><td class="p-2 text-center text-emerald-700 font-bold">+8.1% / 24.8%</td><td class="p-2 text-center font-bold text-emerald-700 bg-amber-50/20">+19.6% / 33.8%</td><td class="p-2 text-center font-bold text-emerald-700 bg-blue-50/20">+5.1% / 21.6%</td><td class="p-2 text-center text-emerald-700 font-bold">+3.1% / 18.6%</td><td class="p-2 text-center font-bold text-emerald-700 bg-slate-100">+8.6% / 24.3%</td></tr>
                                    <tr class="hover:bg-slate-50"><td class="p-2 text-center font-bold text-primary">DG</td><td class="p-2 font-sans font-medium">독일 (Germany)</td><td class="p-2 text-center text-slate-400">-</td><td class="p-2 text-center font-bold text-emerald-700 bg-amber-50/20">+15.8% / 35.1%</td><td class="p-2 text-center font-bold text-emerald-700 bg-blue-50/20">+5.3% / 24.7%</td><td class="p-2 text-center text-rose-600 font-bold">-5.3% / 16.0%</td><td class="p-2 text-center font-bold text-emerald-700 bg-slate-100">+6.9% / 26.5%</td></tr>
                                    <tr class="hover:bg-slate-50"><td class="p-2 text-center font-bold text-primary">BN</td><td class="p-2 font-sans font-medium">베네룩스 (Benelux)</td><td class="p-2 text-center text-rose-600 font-bold">-1.0% / 22.1%</td><td class="p-2 text-center font-bold text-emerald-700 bg-amber-50/20">+8.7% / 29.3%</td><td class="p-2 text-center font-bold text-emerald-700 bg-blue-50/20">+0.5% / 22.5%</td><td class="p-2 text-center text-rose-600 font-bold">-16.1% / 8.8%</td><td class="p-2 text-center font-bold text-emerald-700 bg-slate-100">+1.5% / 23.4%</td></tr>
                                    <tr class="hover:bg-slate-50"><td class="p-2 text-center font-bold text-primary">PL</td><td class="p-2 font-sans font-medium">폴란드 (Poland)</td><td class="p-2 text-center text-emerald-700 font-bold">+33.2% / 52.8%</td><td class="p-2 text-center font-bold text-emerald-700 bg-amber-50/20">+21.0% / 39.8%</td><td class="p-2 text-center font-bold text-emerald-700 bg-blue-50/20">+5.7% / 26.0%</td><td class="p-2 text-center text-rose-600 font-bold">-13.6% / 10.8%</td><td class="p-2 text-center font-bold text-emerald-700 bg-slate-100">+3.4% / 24.5%</td></tr>
                                    <tr class="hover:bg-slate-50"><td class="p-2 text-center font-bold text-primary">MK</td><td class="p-2 font-sans font-medium">헝가리 (Hungary)</td><td class="p-2 text-center text-emerald-700 font-bold">+23.2% / 38.0%</td><td class="p-2 text-center font-bold text-emerald-700 bg-amber-50/20">+13.6% / 31.8%</td><td class="p-2 text-center font-bold text-emerald-700 bg-blue-50/20">+7.2% / 26.3%</td><td class="p-2 text-center text-emerald-700 font-bold">+3.0% / 22.3%</td><td class="p-2 text-center font-bold text-emerald-700 bg-slate-100">+8.0% / 26.9%</td></tr>
                                    <tr class="hover:bg-slate-50"><td class="p-2 text-center font-bold text-primary">Swiss</td><td class="p-2 font-sans font-medium">스위스 (Switzerland)</td><td class="p-2 text-center text-emerald-700 font-bold">+17.8% / 42.9%</td><td class="p-2 text-center font-bold text-emerald-700 bg-amber-50/20">+16.6% / 41.3%</td><td class="p-2 text-center font-bold text-emerald-700 bg-blue-50/20">+6.3% / 34.4%</td><td class="p-2 text-center text-emerald-700 font-bold">+8.5% / 35.6%</td><td class="p-2 text-center font-bold text-emerald-700 bg-slate-100">+9.4% / 36.5%</td></tr>
                                    <tr class="hover:bg-slate-50"><td class="p-2 text-center font-bold text-primary">LA</td><td class="p-2 font-sans font-medium">라트비아/발틱 (Latvia)</td><td class="p-2 text-center text-emerald-700 font-bold">+25.3% / 41.1%</td><td class="p-2 text-center font-bold text-emerald-700 bg-amber-50/20">+22.8% / 38.7%</td><td class="p-2 text-center font-bold text-emerald-700 bg-blue-50/20">+9.4% / 28.0%</td><td class="p-2 text-center text-emerald-700 font-bold">+6.1% / 20.7%</td><td class="p-2 text-center font-bold text-emerald-700 bg-slate-100">+14.5% / 32.1%</td></tr>
                                    <tr class="hover:bg-slate-50"><td class="p-2 text-center font-bold text-primary">AG</td><td class="p-2 font-sans font-medium">오스트리아 (Austria)</td><td class="p-2 text-center text-emerald-700 font-bold">+28.9% / 47.3%</td><td class="p-2 text-center font-bold text-emerald-700 bg-amber-50/20">+12.5% / 32.8%</td><td class="p-2 text-center font-bold text-rose-600 bg-blue-50/20">-0.4% / 21.1%</td><td class="p-2 text-center text-rose-600 font-bold">-4.4% / 16.5%</td><td class="p-2 text-center font-bold text-emerald-700 bg-slate-100">+2.8% / 24.0%</td></tr>
                                    <tr class="hover:bg-slate-50"><td class="p-2 text-center font-bold text-primary">PT</td><td class="p-2 font-sans font-medium">포르투갈 (Portugal)</td><td class="p-2 text-center text-emerald-700 font-bold">+7.5% / 28.1%</td><td class="p-2 text-center font-bold text-emerald-700 bg-amber-50/20">+9.6% / 29.1%</td><td class="p-2 text-center font-bold text-rose-600 bg-blue-50/20">-1.4% / 19.4%</td><td class="p-2 text-center text-rose-600 font-bold">-0.8% / 20.4%</td><td class="p-2 text-center font-bold text-emerald-700 bg-slate-100">+2.2% / 22.7%</td></tr>
                                    <tr class="hover:bg-slate-50"><td class="p-2 text-center font-bold text-primary">CK</td><td class="p-2 font-sans font-medium">체코 (Czech)</td><td class="p-2 text-center text-emerald-700 font-bold">+24.5% / 43.1%</td><td class="p-2 text-center font-bold text-emerald-700 bg-amber-50/20">+16.6% / 36.2%</td><td class="p-2 text-center font-bold text-emerald-700 bg-blue-50/20">+1.6% / 22.8%</td><td class="p-2 text-center text-rose-600 font-bold">-1.5% / 19.0%</td><td class="p-2 text-center font-bold text-emerald-700 bg-slate-100">+3.0% / 23.8%</td></tr>
                                    <tr class="hover:bg-slate-50"><td class="p-2 text-center font-bold text-primary">RO</td><td class="p-2 font-sans font-medium">루마니아 (Romania)</td><td class="p-2 text-center text-emerald-700 font-bold">+9.2% / 35.6%</td><td class="p-2 text-center font-bold text-rose-600 bg-amber-50/20">-2.2% / 28.1%</td><td class="p-2 text-center font-bold text-rose-600 bg-blue-50/20">-1.6% / 25.3%</td><td class="p-2 text-center text-rose-600 font-bold">-3.4% / 23.7%</td><td class="p-2 text-center font-bold text-rose-600 bg-slate-100">-2.0% / 25.9%</td></tr>
                                    <tr class="hover:bg-slate-50"><td class="p-2 text-center font-bold text-primary">HS</td><td class="p-2 font-sans font-medium">그리스 (Greece)</td><td class="p-2 text-center text-emerald-700 font-bold">+20.9% / 42.4%</td><td class="p-2 text-center font-bold text-emerald-700 bg-amber-50/20">+11.1% / 33.3%</td><td class="p-2 text-center font-bold text-rose-600 bg-blue-50/20">-4.0% / 20.6%</td><td class="p-2 text-center text-rose-600 font-bold">-8.7% / 16.7%</td><td class="p-2 text-center font-bold text-emerald-700 bg-slate-100">+0.1% / 24.1%</td></tr>
                                    <tr class="bg-slate-100 font-bold text-slate-900 border-t-2 border-slate-300"><td class="p-2 text-center font-sans">EU16</td><td class="p-2 font-sans">유럽 16개국 평균/합계</td><td class="p-2 text-center font-bold text-emerald-700">+16.8% / 37.0%</td><td class="p-2 text-center font-bold text-emerald-700 bg-amber-100/30">+12.5% / 32.4%</td><td class="p-2 text-center font-bold text-emerald-700 bg-blue-100/30">+2.3% / 23.7%</td><td class="p-2 text-center font-bold text-rose-600">-1.9% / 19.6%</td><td class="p-2 text-center font-bold text-emerald-700 bg-slate-200/80">+4.7% / 25.7%</td></tr>
                                    <tr class="text-slate-500 italic bg-slate-50/60"><td class="p-2 text-center font-sans">RA</td><td class="p-2 font-sans">러시아 (Russia, 참고)</td><td class="p-2 text-center">0.0% / 0.0%</td><td class="p-2 text-center font-bold text-emerald-700">+29.1% / 45.0%</td><td class="p-2 text-center font-bold text-emerald-700">+24.8% / 41.1%</td><td class="p-2 text-center font-bold text-emerald-700">+23.6% / 40.7%</td><td class="p-2 text-center font-bold text-emerald-700">+26.0% / 42.3%</td></tr>
                                </tbody>
                            </table>
                        </div>
                    </div>
                </section>

                <!-- Section 4 -->
                <section class="space-y-4">
                    <div class="border-b border-slate-200 pb-2">
                        <h4 class="text-base sm:text-lg font-bold text-slate-900 flex items-center gap-2">
                            <span class="w-6 h-6 rounded-md bg-blue-100 text-blue-700 flex items-center justify-center text-xs font-bold font-mono">4</span>
                            <span>핵심 전략 제언 및 액션 아이템</span>
                        </h4>
                    </div>

                    <div class="space-y-3">
                        <div class="p-4 rounded-xl bg-slate-50 border border-slate-200 space-y-1.5">
                            <div class="font-bold text-slate-900 text-sm flex items-center gap-2">
                                <span class="w-2 h-2 rounded-full bg-amber-500"></span>
                                <span>1. G 시리즈 비중 확대를 통한 이익 극대화 (Mix Elevation Campaign)</span>
                            </div>
                            <p class="text-xs text-slate-600 leading-relaxed">
                                G 시리즈의 높은 수익성(COI% 12.5%, MP% 32.4%)을 극대화하기 위해, 베네룩스(40.3%), 라트비아(38.4%), 프랑스(33.1%), 영국(32.2%) 수준으로 동유럽 법인(체코 13.5%, 폴란드 14.6%, 헝가리 20.4%)의 G시리즈 판매 비중을 25% 이상으로 상향시키는 프리미엄 전환 마케팅 집중.
                            </p>
                        </div>

                        <div class="p-4 rounded-xl bg-slate-50 border border-slate-200 space-y-1.5">
                            <div class="font-bold text-slate-900 text-sm flex items-center gap-2">
                                <span class="w-2 h-2 rounded-full bg-blue-500"></span>
                                <span>2. C 시리즈 유통 사후 차감(S/D) 및 가격 가이드라인 통제</span>
                            </div>
                            <p class="text-xs text-slate-600 leading-relaxed">
                                프랑스(-10.6%), 이탈리아(-6.1%), 그리스(-4.0%) 등 C시리즈 적자 법인의 경우, 온라인/오프라인 최저 승인가격(ATA/MAP) 가이드라인을 엄격히 준수하고 비효율적 Sell-out 인센티브를 즉각 구조조정해야 함.
                            </p>
                        </div>

                        <div class="p-4 rounded-xl bg-slate-50 border border-slate-200 space-y-1.5">
                            <div class="font-bold text-slate-900 text-sm flex items-center gap-2">
                                <span class="w-2 h-2 rounded-full bg-rose-500"></span>
                                <span>3. B 시리즈 수량 캡핑 및 C시리즈 유도 매장 연출</span>
                            </div>
                            <p class="text-xs text-slate-600 leading-relaxed">
                                B 시리즈의 영업손실(-1.9%)을 감안하여 유통 공급 물량을 철저히 조절하고, 매장 진열 시 C/G 시리즈와의 프로세서 화질, 사운드, 디자인 차별성을 부각하여 상향 구매(Up-selling)를 유도.
                            </p>
                        </div>
                    </div>
                </section>

                <!-- Section 5 -->
                <section class="space-y-4 pt-4 border-t border-slate-200">
                    <div class="flex items-center justify-between">
                        <div class="flex items-center gap-2">
                            <span class="material-symbols-outlined text-blue-600">attach_file</span>
                            <span class="font-bold text-slate-900 text-sm">생성된 산출물 및 첨부 파일</span>
                        </div>
                        <span class="text-xs text-slate-500">단일 클릭 즉시 다운로드 가능</span>
                    </div>

                    <div class="p-4 rounded-xl bg-slate-50 border border-slate-200 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-3">
                        <div class="flex items-center gap-3">
                            <div class="w-10 h-10 rounded-lg bg-blue-100 text-blue-700 flex items-center justify-center font-bold text-xs shrink-0">CSV</div>
                            <div>
                                <div class="text-xs font-bold text-slate-900 font-mono">scratch_oled_pnl_summary.csv</div>
                                <div class="text-[11px] text-slate-500">유럽 16개국 및 CIS 17개 판매법인/지점 OLED 시리즈별(W/G/C/B) 실적 전수 집계 원천 DB</div>
                            </div>
                        </div>
                        <button type="button" 
                                onclick="downloadScenarioCsv()"
                                class="px-4 py-2 rounded-lg bg-blue-600 hover:bg-blue-500 text-white text-xs font-bold flex items-center gap-1.5 transition-all shadow-xs hover:scale-105 active:scale-95 shrink-0">
                            <span class="material-symbols-outlined text-sm">download</span>
                            <span>scratch_oled_pnl_summary.csv 다운로드</span>
                        </button>
                    </div>
                </section>

            </div>
        </div>

    </main>

    <!-- Client-side Scripts -->
    <script>
        function returnToGuide() {{
            const guideUrl = 'AXIS_System_Architecture_Guide.html#tab-scenarios';
            if (window.opener && !window.opener.closed) {{
                try {{
                    window.opener.location.href = guideUrl;
                    window.close();
                    return;
                }} catch (e) {{}}
            }}
            window.location.href = guideUrl;
        }}

        const SCENARIO_CSV_B64 = "{csv_b64}";

        function downloadScenarioCsv() {{
            try {{
                const byteCharacters = atob(SCENARIO_CSV_B64);
                const byteNumbers = new Array(byteCharacters.length);
                for (let i = 0; i < byteCharacters.length; i++) {{
                    byteNumbers[i] = byteCharacters.charCodeAt(i);
                }}
                const byteArray = new Uint8Array(byteNumbers);
                const blob = new Blob([byteArray], {{ type: 'text/csv;charset=utf-8;' }});
                
                const link = document.createElement('a');
                link.href = URL.createObjectURL(blob);
                link.download = 'scratch_oled_pnl_summary.csv';
                document.body.appendChild(link);
                link.click();
                document.body.removeChild(link);
                URL.revokeObjectURL(link.href);
            }} catch (e) {{
                // fallback to direct link
                window.location.href = 'scratch_oled_pnl_summary.csv';
            }}
        }}
    </script>
</body>
</html>
'''

with open(OUTPUT_HTML, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Generated {OUTPUT_HTML} (Size: {os.path.getsize(OUTPUT_HTML)} bytes)")
