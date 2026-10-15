# -*- coding: utf-8 -*-
"""
generate_anonymized_scenario_04_viewer.py
AXIS Scenario 04 Result Viewer Generation Script
Subsidiary & Retailer Anonymization Applied:
- Subsidiary: 유럽 A 법인
- Country/Market: A국 시장
- Retailers: 거래선 A(1위 대형 가전체인), 거래선 B(2위 옴니채널 체인), 거래선 C(3위 IT/디지털 전문 체인)
- Embedded File: 유럽_A법인_2026년_8월_경영실적_보고서.docx (Base64 Inline Download)
"""

import os
import base64

DOCX_PATH = r"d:\TV 유럽영업\15. AX Task\2026 AX 실행과제\00. TV Europe Sales Management Portal\docs\유럽_A법인_2026년_8월_경영실적_보고서.docx"
OUTPUT_HTML = r"d:\TV 유럽영업\15. AX Task\2026 AX 실행과제\00. TV Europe Sales Management Portal\docs\scenario_04_result_viewer.html"

with open(DOCX_PATH, "rb") as f:
    docx_bytes = f.read()
    docx_b64 = base64.b64encode(docx_bytes).decode("ascii")

html_content = f"""<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>시나리오 04 실전 답변 및 경영진 보고서 결과 - AXIS Master AI Agent</title>
    
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
                    <span class="px-2 py-0.5 rounded bg-purple-900/80 text-purple-300 text-[10px] font-bold border border-purple-700/60 hidden md:inline">실전 질의 시나리오 04</span>
                    <h1 class="text-sm font-bold text-white tracking-tight truncate">월간 법인 경영실적 리뷰 및 진단 보고서(Word/Docx) 자동 생성 실전 결과</h1>
                </div>
            </div>

            <!-- Right: Actions -->
            <div class="flex items-center gap-2">
                <button type="button" 
                        onclick="downloadScenarioDocx()"
                        class="px-3 py-1.5 rounded-lg bg-purple-600 hover:bg-purple-500 text-white text-xs font-bold flex items-center gap-1.5 shadow-sm transition-all hover:scale-105 active:scale-95">
                    <span class="material-symbols-outlined text-sm">description</span>
                    <span class="hidden sm:inline">워드 보고서 다운로드 (.docx)</span>
                    <span class="sm:hidden">Word 다운로드</span>
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
                <span class="font-bold text-purple-700">시나리오 04 실전 답변 상세 결과</span>
            </div>
            <div class="flex flex-wrap items-center justify-between gap-3">
                <div>
                    <h2 class="text-xl font-headline font-bold text-slate-900">월간 법인 경영실적 리뷰 및 진단 보고서(Word/Docx) 자동 생성 실전 결과</h2>
                    <p class="text-xs text-slate-600 mt-1">유럽 A 법인의 2026년 8월 TV 사업 마감 실적(P&L, 셀아웃, 유통 재고, GfK 점유율, 3대 리테일러 전략)을 종합 분석하여 경영진 보고용 공식 워드 문서(.docx)를 생성한 마스터 에이전트 실전 답변 및 산출물입니다. (보안 가명화: 유럽 A 법인 / 거래선 A·B·C 적용)</p>
                </div>
                <div class="flex items-center gap-2 text-xs bg-slate-50 px-3 py-1.5 rounded-lg border border-slate-200">
                    <span class="w-2.5 h-2.5 rounded-full bg-emerald-500 animate-pulse"></span>
                    <span class="text-slate-600">소요 시간: <strong class="text-purple-700 font-mono">1분</strong></span>
                    <span class="text-slate-300">|</span>
                    <span class="text-slate-600">분석 범위: <strong class="text-slate-800">유럽 A 법인 NERP P&L, GDMI W36, GfK 7~8월 DB 종합</strong></span>
                </div>
            </div>

            <!-- Original Query Chip -->
            <div class="p-3 rounded-lg bg-purple-50/50 border border-purple-100 flex items-center justify-between text-xs font-mono text-slate-800 gap-2">
                <div class="flex items-center gap-2 truncate">
                    <span class="px-2 py-0.5 rounded bg-purple-600 text-white text-[10px] font-bold font-sans">실전 질의</span>
                    <span class="truncate">"유럽 A법인 8월 매출, 손익, 셀아웃, 시장점유율 등 최근 시장 동향 및 사업 성과를 경영진 리포트 형식으로 워드(.docx) 문서로 만들어줘"</span>
                </div>
                <span class="px-2 py-0.5 rounded bg-slate-200/80 text-slate-700 text-[10px] font-sans font-medium whitespace-nowrap">정식 워드 보고서 동봉</span>
            </div>
        </div>

        <!-- Download Banner Card -->
        <div class="bg-gradient-to-r from-purple-950 via-slate-900 to-blue-950 text-white rounded-xl p-5 shadow-sm flex flex-col md:flex-row items-center justify-between gap-4 border border-purple-800/40">
            <div class="flex items-center gap-3.5">
                <div class="w-12 h-12 rounded-xl bg-purple-500/20 border border-purple-400/30 flex items-center justify-center shrink-0">
                    <span class="material-symbols-outlined text-purple-300 text-2xl">description</span>
                </div>
                <div>
                    <div class="flex items-center gap-2">
                        <span class="text-sm font-bold text-white">생성 산출물: 유럽_A법인_2026년_8월_경영실적_보고서.docx</span>
                        <span class="text-[10px] bg-purple-500/30 text-purple-200 px-2 py-0.5 rounded font-mono border border-purple-400/30">43.8 KB</span>
                    </div>
                    <p class="text-xs text-slate-300 mt-0.5">경영진 보고용 정식 서식(표 8개, 4대 핵심 KPI 카드, 6개월 손익 추이, WOS 진단, GfK 점유율, 3대 액션플랜 수록 워드 문서)</p>
                </div>
            </div>
            <button type="button" 
                    onclick="downloadScenarioDocx()"
                    class="w-full md:w-auto px-5 py-2.5 rounded-lg bg-purple-600 hover:bg-purple-500 text-white text-xs font-bold flex items-center justify-center gap-2 transition-all shadow-md shrink-0 hover:scale-105 active:scale-95">
                <span class="material-symbols-outlined text-base">download</span>
                <span>워드 보고서(.docx) 즉시 다운로드</span>
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
                            <span class="px-2 py-0.5 rounded-full bg-emerald-100 text-emerald-800 text-[10px] font-bold">생성 완료 (Generated)</span>
                        </div>
                        <p class="text-[11px] text-slate-500">연계 에이전트: TV P&L Analysis, KPI Sheet, Price Tracker, MS Trend | 보고서 양식: LGE 경영진 보고용 표준 워드</p>
                    </div>
                </div>
                <span class="text-xs font-mono text-slate-400">2026-09-17 09:15:00 KST</span>
            </div>

            <!-- Content Area -->
            <div class="space-y-8 text-slate-800 text-xs sm:text-sm leading-relaxed">
                
                <!-- Section 0: Response Intro -->
                <div class="p-4 rounded-xl bg-slate-50 border border-slate-200 space-y-2">
                    <p class="font-medium text-slate-800">
                        요청하신 <strong>유럽 A 법인의 2026년 8월 TV 사업 경영실적 및 전략 진단 워드 경영진 보고서(<code>.docx</code>)</strong> 작성을 성공적으로 완료하였습니다.
                    </p>
                    <p class="text-xs text-slate-600">
                        보고서는 NERP 공식 P&L 관리회계 원천 DB, GDMI W36 주간 셀아웃/채널 재고 결산 데이터, GfK 7~8월 최신 시장 데이터 및 Price Tracker 채널 가격 정보를 융합 분석하여 작성되었습니다. 아래 요약 본문을 확인하시거나, 상단의 다운로드 버튼을 통해 정식 스타일이 적용된 워드 보고서를 즉시 다운로드하실 수 있습니다.
                    </p>
                </div>

                <!-- Section 1: Executive Summary -->
                <section class="space-y-4">
                    <div class="border-b border-slate-200 pb-2">
                        <h4 class="text-base sm:text-lg font-bold text-slate-900 flex items-center gap-2">
                            <span class="w-6 h-6 rounded-md bg-purple-100 text-purple-700 flex items-center justify-center text-xs font-bold font-mono">1</span>
                            <span>8월 핵심 경영 지표 총괄 요약 (Executive Summary)</span>
                        </h4>
                    </div>

                    <!-- 4 KPI Cards -->
                    <div class="grid grid-cols-2 md:grid-cols-4 gap-3">
                        <div class="p-3.5 rounded-xl bg-slate-50 border border-slate-200 space-y-1">
                            <div class="text-[11px] text-slate-500 font-medium">8월 Net Sales (순매출)</div>
                            <div class="text-base sm:text-lg font-bold text-slate-900 font-mono-num">$2.25M</div>
                            <div class="text-[11px] text-emerald-700 font-semibold flex items-center gap-1">
                                <span class="material-symbols-outlined text-xs">trending_up</span>
                                <span>YoY +5.6% (견조한 성장)</span>
                            </div>
                        </div>

                        <div class="p-3.5 rounded-xl bg-slate-50 border border-slate-200 space-y-1">
                            <div class="text-[11px] text-slate-500 font-medium">8월 영업이익 (COI)</div>
                            <div class="text-base sm:text-lg font-bold text-emerald-700 font-mono-num">+$5.7K</div>
                            <div class="text-[11px] text-emerald-700 font-semibold flex items-center gap-1">
                                <span class="material-symbols-outlined text-xs">check_circle</span>
                                <span>OPM +0.26% (흑자 전환)</span>
                            </div>
                        </div>

                        <div class="p-3.5 rounded-xl bg-slate-50 border border-slate-200 space-y-1">
                            <div class="text-[11px] text-slate-500 font-medium">평균 판매단가 (ASP)</div>
                            <div class="text-base sm:text-lg font-bold text-blue-700 font-mono-num">$420.0</div>
                            <div class="text-[11px] text-blue-700 font-semibold flex items-center gap-1">
                                <span class="material-symbols-outlined text-xs">trending_up</span>
                                <span>YoY +29.3% (프리미엄 믹스)</span>
                            </div>
                        </div>

                        <div class="p-3.5 rounded-xl bg-slate-50 border border-slate-200 space-y-1">
                            <div class="text-[11px] text-slate-500 font-medium">유통 재고 주수 (WOS)</div>
                            <div class="text-base sm:text-lg font-bold text-slate-900 font-mono-num">6.1주</div>
                            <div class="text-[11px] text-emerald-700 font-semibold flex items-center gap-1">
                                <span class="material-symbols-outlined text-xs">verified</span>
                                <span>Healthy (가이드라인 내 안착)</span>
                            </div>
                        </div>
                    </div>

                    <!-- Executive Summary Paragraph -->
                    <div class="p-4 rounded-xl bg-blue-50/40 border border-blue-100 text-xs sm:text-sm text-slate-700 leading-relaxed space-y-2">
                        <div class="font-bold text-blue-900 flex items-center gap-1.5 text-xs sm:text-sm">
                            <span class="material-symbols-outlined text-sm">assessment</span>
                            <span>경영진 총평</span>
                        </div>
                        <p>
                            2026년 8월 <strong>유럽 A 법인</strong>은 지난 7월의 일시적 영업적자(-$125.7K, OPM -5.29%)를 완벽히 극복하고 8월 단월 <strong>순매출 $2,248.7K(YoY +5.6%)</strong>, <strong>영업이익 +$5.7K(OPM +0.26%, YoY +20.8%p 개선)</strong>로 흑자 전환(Turnaround)에 성공하였습니다.
                        </p>
                        <p>
                            특히 수익성이 낮은 보급형 물량을 의도적으로 축소(수량 5,037대, YoY -19.1%)하는 대신 <strong>OLED C5/G5 및 대형 QNED 중심의 믹스 영업</strong>을 강화하여, <strong>평균판매단가(ASP)가 전년 동월 대비 +29.3% 급등한 $419.97</strong>를 기록하였고, <strong>한계이익률(MP Rate) 또한 34.14%(YoY +18.2%p)</strong>로 사상 최고 수준에 도달했습니다. 아울러 판매장려금(SD)을 15.45%로 전월비 -7.1%p 대폭 건전화하고 전체 채널 재고 주수(WOS)를 6.1주(총 11,899대)의 적정 수준으로 관리하였습니다. 다만 QNED 세그먼트의 재고 주수가 8.3주(4,037대)로 다소 누적되어 있고, 중국계 TCL이 수량 M/S 17.3%로 진입함에 따라 Q4 성수기 대비 선제적 대응이 필요합니다.
                        </p>
                    </div>
                </section>

                <!-- Section 2: P&L Deep-Dive -->
                <section class="space-y-4">
                    <div class="border-b border-slate-200 pb-2">
                        <h4 class="text-base sm:text-lg font-bold text-slate-900 flex items-center gap-2">
                            <span class="w-6 h-6 rounded-md bg-purple-100 text-purple-700 flex items-center justify-center text-xs font-bold font-mono">2</span>
                            <span>월별 손익 추이 및 8월 마감 상세 (P&L Deep-Dive)</span>
                        </h4>
                    </div>

                    <!-- Table 2-1 -->
                    <div class="space-y-2">
                        <div class="flex items-center justify-between">
                            <h5 class="text-xs sm:text-sm font-bold text-slate-800">📊 &lt;표 2-1&gt; 최근 6개월(3월~8월) 월별 손익 및 수익성 지표 추이</h5>
                            <span class="text-[11px] text-slate-500">*NERP P&L 관리회계 원천 결산 기준 (단위: $K, %)</span>
                        </div>
                        <div class="overflow-x-auto rounded-lg border border-slate-200 shadow-2xs">
                            <table class="w-full text-left border-collapse custom-matrix-table">
                                <thead>
                                    <tr>
                                        <th class="p-2.5">손익 지표</th>
                                        <th class="p-2.5 text-right">3월</th>
                                        <th class="p-2.5 text-right">4월</th>
                                        <th class="p-2.5 text-right">5월</th>
                                        <th class="p-2.5 text-right">6월</th>
                                        <th class="p-2.5 text-right">7월</th>
                                        <th class="p-2.5 text-right th-highlight">8월 (당월)</th>
                                    </tr>
                                </thead>
                                <tbody class="divide-y divide-slate-200 font-mono-num text-xs">
                                    <tr class="hover:bg-slate-50 transition-colors">
                                        <td class="p-2.5 font-bold text-slate-900 font-sans">Net Sales (순매출)</td>
                                        <td class="p-2.5 text-right">$3,065.7K</td>
                                        <td class="p-2.5 text-right">$3,053.9K</td>
                                        <td class="p-2.5 text-right">$3,495.5K</td>
                                        <td class="p-2.5 text-right">$3,142.4K</td>
                                        <td class="p-2.5 text-right">$2,377.2K</td>
                                        <td class="p-2.5 text-right font-bold text-primary bg-blue-50/20">$2,248.7K</td>
                                    </tr>
                                    <tr class="hover:bg-slate-50 transition-colors">
                                        <td class="p-2.5 font-bold text-slate-900 font-sans">한계이익 (MP)</td>
                                        <td class="p-2.5 text-right">$797.3K</td>
                                        <td class="p-2.5 text-right">$816.7K</td>
                                        <td class="p-2.5 text-right">$906.9K</td>
                                        <td class="p-2.5 text-right">$1,029.5K</td>
                                        <td class="p-2.5 text-right">$648.4K</td>
                                        <td class="p-2.5 text-right font-bold text-emerald-700 bg-emerald-50/20">$767.7K</td>
                                    </tr>
                                    <tr class="hover:bg-slate-50 transition-colors bg-emerald-50/15">
                                        <td class="p-2.5 font-bold text-slate-900 font-sans">한계이익률 (MP Rate)</td>
                                        <td class="p-2.5 text-right">26.0%</td>
                                        <td class="p-2.5 text-right">26.7%</td>
                                        <td class="p-2.5 text-right">25.9%</td>
                                        <td class="p-2.5 text-right">32.8%</td>
                                        <td class="p-2.5 text-right">27.3%</td>
                                        <td class="p-2.5 text-right font-bold text-emerald-700 bg-emerald-50/30">34.1%</td>
                                    </tr>
                                    <tr class="hover:bg-slate-50 transition-colors">
                                        <td class="p-2.5 font-bold text-slate-900 font-sans">판매장려금률 (SD Rate)</td>
                                        <td class="p-2.5 text-right">15.2%</td>
                                        <td class="p-2.5 text-right">17.2%</td>
                                        <td class="p-2.5 text-right">19.2%</td>
                                        <td class="p-2.5 text-right">16.8%</td>
                                        <td class="p-2.5 text-right text-rose-600 font-bold">22.6%</td>
                                        <td class="p-2.5 text-right font-bold text-blue-700 bg-blue-50/20">15.4%</td>
                                    </tr>
                                    <tr class="hover:bg-slate-50 transition-colors">
                                        <td class="p-2.5 font-bold text-slate-900 font-sans">물류비율 (TT Rate)</td>
                                        <td class="p-2.5 text-right">3.2%</td>
                                        <td class="p-2.5 text-right">3.2%</td>
                                        <td class="p-2.5 text-right">2.6%</td>
                                        <td class="p-2.5 text-right">2.8%</td>
                                        <td class="p-2.5 text-right">3.1%</td>
                                        <td class="p-2.5 text-right">3.0%</td>
                                    </tr>
                                    <tr class="hover:bg-slate-50 transition-colors">
                                        <td class="p-2.5 font-bold text-slate-900 font-sans">영업이익 (COI)</td>
                                        <td class="p-2.5 text-right text-emerald-700">+$26.5K</td>
                                        <td class="p-2.5 text-right text-emerald-700">+$30.1K</td>
                                        <td class="p-2.5 text-right text-emerald-700">+$108.2K</td>
                                        <td class="p-2.5 text-right text-emerald-700">+$299.3K</td>
                                        <td class="p-2.5 text-right text-rose-600 font-bold">-$125.7K</td>
                                        <td class="p-2.5 text-right text-emerald-700 font-bold bg-emerald-50/20">+$5.7K</td>
                                    </tr>
                                    <tr class="hover:bg-slate-50 transition-colors bg-blue-50/15">
                                        <td class="p-2.5 font-bold text-slate-900 font-sans">영업이익률 (OPM)</td>
                                        <td class="p-2.5 text-right text-emerald-700">+0.86%</td>
                                        <td class="p-2.5 text-right text-emerald-700">+0.98%</td>
                                        <td class="p-2.5 text-right text-emerald-700">+3.10%</td>
                                        <td class="p-2.5 text-right text-emerald-700 font-bold">+9.52%</td>
                                        <td class="p-2.5 text-right text-rose-600 font-bold">-5.29%</td>
                                        <td class="p-2.5 text-right font-bold text-emerald-700 bg-emerald-50/30">+0.26%</td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                    </div>

                    <!-- Table 2-2 -->
                    <div class="space-y-2 pt-2">
                        <div class="flex items-center justify-between">
                            <h5 class="text-xs sm:text-sm font-bold text-slate-800">📊 &lt;표 2-2&gt; 8월 MTD 및 1~8월 YTD 누적 실적 및 전년 동기(YoY) 비교</h5>
                        </div>
                        <div class="overflow-x-auto rounded-lg border border-slate-200 shadow-2xs">
                            <table class="w-full text-left border-collapse custom-matrix-table">
                                <thead>
                                    <tr>
                                        <th class="p-2.5">핵심 경영 지표</th>
                                        <th class="p-2.5 text-right">2026년 8월 MTD</th>
                                        <th class="p-2.5 text-right th-highlight">8월 YoY 증감</th>
                                        <th class="p-2.5 text-right">2026년 YTD 누계</th>
                                        <th class="p-2.5 text-right th-highlight">YTD YoY 증감</th>
                                    </tr>
                                </thead>
                                <tbody class="divide-y divide-slate-200 font-mono-num text-xs">
                                    <tr class="hover:bg-slate-50 transition-colors">
                                        <td class="p-2.5 font-bold text-slate-900 font-sans">판매 수량 (Qty)</td>
                                        <td class="p-2.5 text-right">5,037대</td>
                                        <td class="p-2.5 text-right font-bold text-slate-600">-19.1% (디마케팅)</td>
                                        <td class="p-2.5 text-right">62,247대</td>
                                        <td class="p-2.5 text-right text-emerald-700 font-bold">+9.7%</td>
                                    </tr>
                                    <tr class="hover:bg-slate-50 transition-colors">
                                        <td class="p-2.5 font-bold text-slate-900 font-sans">순매출액 (Net Sales)</td>
                                        <td class="p-2.5 text-right font-bold">$2,248,728</td>
                                        <td class="p-2.5 text-right font-bold text-emerald-700">+5.6%</td>
                                        <td class="p-2.5 text-right font-bold">$25,545,255</td>
                                        <td class="p-2.5 text-right font-bold text-emerald-700">+11.5%</td>
                                    </tr>
                                    <tr class="hover:bg-slate-50 transition-colors">
                                        <td class="p-2.5 font-bold text-slate-900 font-sans">평균 판매단가 (ASP)</td>
                                        <td class="p-2.5 text-right font-bold text-blue-700">$419.97</td>
                                        <td class="p-2.5 text-right font-bold text-blue-700">+29.3% (+$95.0)</td>
                                        <td class="p-2.5 text-right">$392.01</td>
                                        <td class="p-2.5 text-right text-emerald-700">+1.8%</td>
                                    </tr>
                                    <tr class="hover:bg-slate-50 transition-colors">
                                        <td class="p-2.5 font-bold text-slate-900 font-sans">한계이익률 (MP Rate)</td>
                                        <td class="p-2.5 text-right font-bold text-emerald-700">34.14%</td>
                                        <td class="p-2.5 text-right font-bold text-emerald-700">+18.2%p</td>
                                        <td class="p-2.5 text-right font-bold text-emerald-700">27.15%</td>
                                        <td class="p-2.5 text-right font-bold text-emerald-700">+7.2%p</td>
                                    </tr>
                                    <tr class="hover:bg-slate-50 transition-colors">
                                        <td class="p-2.5 font-bold text-slate-900 font-sans">판매장려금률 (SD Rate)</td>
                                        <td class="p-2.5 text-right">15.45%</td>
                                        <td class="p-2.5 text-right font-bold text-emerald-700">-9.4%p (건전화)</td>
                                        <td class="p-2.5 text-right">18.65%</td>
                                        <td class="p-2.5 text-right text-emerald-700">-3.0%p</td>
                                    </tr>
                                    <tr class="hover:bg-slate-50 transition-colors bg-emerald-50/15">
                                        <td class="p-2.5 font-bold text-slate-900 font-sans">영업이익률 (OPM)</td>
                                        <td class="p-2.5 text-right font-bold text-emerald-700">+0.26%</td>
                                        <td class="p-2.5 text-right font-bold text-emerald-700">+20.8%p (흑자전환)</td>
                                        <td class="p-2.5 text-right font-bold text-emerald-700">+3.92%</td>
                                        <td class="p-2.5 text-right font-bold text-emerald-700">+10.3%p</td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                    </div>

                    <!-- Analysis Notes -->
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-3 pt-2">
                        <div class="p-3.5 rounded-lg bg-slate-50 border border-slate-200 space-y-1">
                            <div class="font-bold text-slate-900 text-xs flex items-center gap-1.5">
                                <span class="material-symbols-outlined text-sm text-emerald-600">published_with_changes</span>
                                <span>흑자 전환 턴어라운드 동인</span>
                            </div>
                            <p class="text-xs text-slate-600 leading-relaxed">
                                7월 -$125.7K(-5.29%)의 적자는 유통 여름 바겐세일 참여에 따른 판매장려금(SD 22.6%) 급증이 주원인이었습니다. 8월에는 무분별한 BTL 가격 할인을 즉각 중단하고 고마진 C5/G5 및 대형 QNED 중심으로 믹스를 재편하여 SD율을 15.5%로 -7.1%p 감축, 영업이익을 흑자로 즉각 전환시켰습니다.
                            </p>
                        </div>
                        <div class="p-3.5 rounded-lg bg-slate-50 border border-slate-200 space-y-1">
                            <div class="font-bold text-slate-900 text-xs flex items-center gap-1.5">
                                <span class="material-symbols-outlined text-sm text-blue-600">auto_graph</span>
                                <span>한계이익률(MP 34.1%) 및 ASP 구조 혁신</span>
                            </div>
                            <p class="text-xs text-slate-600 leading-relaxed">
                                단순 수량 확대(Volume Chase) 대신 가치 중심 영업(Value-Up)을 전개하여 판매 수량이 5,037대로 전년비 -19.1% 줄었음에도, 단가가 $420로 +29.3% 상승하면서 매출액은 오히려 +5.6% 신장하고 한계이익률은 34.1%로 전년 동기(15.9%) 대비 두 배 이상 폭등하였습니다.
                            </p>
                        </div>
                    </div>
                </section>

                <!-- Section 3: GDMI Sell-out & WOS -->
                <section class="space-y-4">
                    <div class="border-b border-slate-200 pb-2">
                        <h4 class="text-base sm:text-lg font-bold text-slate-900 flex items-center gap-2">
                            <span class="w-6 h-6 rounded-md bg-purple-100 text-purple-700 flex items-center justify-center text-xs font-bold font-mono">3</span>
                            <span>GDMI 주간 셀아웃 및 제품 세그먼트별 재고(WOS) 진단</span>
                        </h4>
                    </div>

                    <div class="space-y-2">
                        <div class="flex items-center justify-between">
                            <h5 class="text-xs sm:text-sm font-bold text-slate-800">📊 &lt;표 3-1&gt; GDMI W36(8월말 기준) 세그먼트별 Sell-out 및 채널 재고(WOS) 현황</h5>
                        </div>
                        <div class="overflow-x-auto rounded-lg border border-slate-200 shadow-2xs">
                            <table class="w-full text-left border-collapse custom-matrix-table">
                                <thead>
                                    <tr>
                                        <th class="p-2.5">제품 세그먼트</th>
                                        <th class="p-2.5 text-right">주간 Sell-out</th>
                                        <th class="p-2.5 text-right">전년비 (YoY)</th>
                                        <th class="p-2.5 text-right">채널재고 (대)</th>
                                        <th class="p-2.5 text-right th-highlight">재고주수 (WOS)</th>
                                        <th class="p-2.5 text-center">건전성 평가</th>
                                    </tr>
                                </thead>
                                <tbody class="divide-y divide-slate-200 font-mono-num text-xs">
                                    <tr class="hover:bg-slate-50 transition-colors">
                                        <td class="p-2.5 font-bold text-slate-900 font-sans">OLED (초프리미엄)</td>
                                        <td class="p-2.5 text-right">294대</td>
                                        <td class="p-2.5 text-right font-bold text-emerald-700">+55.6%</td>
                                        <td class="p-2.5 text-right">1,456대</td>
                                        <td class="p-2.5 text-right font-bold text-emerald-700 bg-emerald-50/20">5.7주</td>
                                        <td class="p-2.5 text-center font-bold text-emerald-700 font-sans">✓ Healthy</td>
                                    </tr>
                                    <tr class="hover:bg-slate-50 transition-colors bg-amber-50/20">
                                        <td class="p-2.5 font-bold text-slate-900 font-sans">QNED / MRGB (프리미엄)</td>
                                        <td class="p-2.5 text-right">497대</td>
                                        <td class="p-2.5 text-right font-bold text-emerald-700">+73.8%</td>
                                        <td class="p-2.5 text-right font-bold text-amber-900">4,037대</td>
                                        <td class="p-2.5 text-right font-bold text-amber-700 bg-amber-50/40">8.3주</td>
                                        <td class="p-2.5 text-center font-bold text-amber-700 font-sans">⚠ Warning</td>
                                    </tr>
                                    <tr class="hover:bg-slate-50 transition-colors">
                                        <td class="p-2.5 font-bold text-slate-900 font-sans">NANO (중고급형)</td>
                                        <td class="p-2.5 text-right">374대</td>
                                        <td class="p-2.5 text-right font-bold text-emerald-700">+129.4%</td>
                                        <td class="p-2.5 text-right">1,091대</td>
                                        <td class="p-2.5 text-right font-bold text-emerald-700 bg-emerald-50/20">3.4주</td>
                                        <td class="p-2.5 text-center font-bold text-emerald-700 font-sans">✓ Healthy</td>
                                    </tr>
                                    <tr class="hover:bg-slate-50 transition-colors">
                                        <td class="p-2.5 font-bold text-slate-900 font-sans">UHD (메인스트림)</td>
                                        <td class="p-2.5 text-right">756대</td>
                                        <td class="p-2.5 text-right text-slate-500">-18.3%</td>
                                        <td class="p-2.5 text-right">4,005대</td>
                                        <td class="p-2.5 text-right font-bold text-emerald-700 bg-emerald-50/20">5.8주</td>
                                        <td class="p-2.5 text-center font-bold text-emerald-700 font-sans">✓ Healthy</td>
                                    </tr>
                                    <tr class="hover:bg-slate-50 transition-colors">
                                        <td class="p-2.5 font-bold text-slate-900 font-sans">FHD / STV (보급형)</td>
                                        <td class="p-2.5 text-right">198대</td>
                                        <td class="p-2.5 text-right text-slate-500">-13.9%</td>
                                        <td class="p-2.5 text-right">1,310대</td>
                                        <td class="p-2.5 text-right font-bold text-emerald-700 bg-emerald-50/20">6.2주</td>
                                        <td class="p-2.5 text-center font-bold text-emerald-700 font-sans">✓ Healthy</td>
                                    </tr>
                                    <tr class="bg-slate-100 font-bold text-slate-900 border-t-2 border-slate-300">
                                        <td class="p-2.5 font-sans">A국 전체 (Total)</td>
                                        <td class="p-2.5 text-right font-bold text-primary">2,119대</td>
                                        <td class="p-2.5 text-right font-bold text-emerald-700">+18.2%</td>
                                        <td class="p-2.5 text-right font-bold">11,899대</td>
                                        <td class="p-2.5 text-right font-bold text-emerald-700">6.1주</td>
                                        <td class="p-2.5 text-center font-bold text-emerald-700 font-sans">✓ Healthy</td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                    </div>

                    <!-- Notes -->
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-3 pt-1">
                        <div class="p-3 rounded-lg bg-emerald-50/30 border border-emerald-100 space-y-1">
                            <div class="font-bold text-emerald-800 text-xs">✓ 셀아웃 초과 달성 및 OLED 폭발적 성장</div>
                            <p class="text-xs text-slate-600 leading-relaxed">
                                W36 주간 셀아웃은 2,119대로 사업계획 대비 199.2%를 기록하며 압도적 판매 모멘텀을 보였습니다. 특히 OLED 셀아웃은 전년비 +55.6% 급증하였고 WOS 5.7주로 공급망이 완벽히 안정화되었습니다.
                            </p>
                        </div>
                        <div class="p-3 rounded-lg bg-amber-50/40 border border-amber-200 space-y-1">
                            <div class="font-bold text-amber-800 text-xs">⚠️ QNED 재고 집중 관리 (Warning)</div>
                            <p class="text-xs text-slate-600 leading-relaxed">
                                QNED 셀아웃은 +73.8%로 빠르게 확대되고 있으나, 채널 재고가 4,037대(WOS 8.3주)로 전체 재고의 34%를 차지하고 있습니다. 4분기 블랙프라이데이 물량 입고 전 8주 이하로 압축하는 프로모션이 요구됩니다.
                            </p>
                        </div>
                    </div>
                </section>

                <!-- Section 4: GfK M/S & 3 Retailers -->
                <section class="space-y-4">
                    <div class="border-b border-slate-200 pb-2">
                        <h4 class="text-base sm:text-lg font-bold text-slate-900 flex items-center gap-2">
                            <span class="w-6 h-6 rounded-md bg-purple-100 text-purple-700 flex items-center justify-center text-xs font-bold font-mono">4</span>
                            <span>GfK 시장 점유율 및 3대 유통 채널 전략</span>
                        </h4>
                    </div>

                    <!-- Table 4-1 -->
                    <div class="space-y-2">
                        <div class="flex items-center justify-between">
                            <h5 class="text-xs sm:text-sm font-bold text-slate-800">📊 &lt;표 4-1&gt; A국 TV 시장 주요 브랜드별 점유율(M/S) 및 경쟁 구도 (GfK 기준)</h5>
                        </div>
                        <div class="overflow-x-auto rounded-lg border border-slate-200 shadow-2xs">
                            <table class="w-full text-left border-collapse custom-matrix-table">
                                <thead>
                                    <tr>
                                        <th class="p-2.5">제조사 (Brand)</th>
                                        <th class="p-2.5 text-right th-highlight">금액 M/S (Value)</th>
                                        <th class="p-2.5 text-right th-highlight">수량 M/S (Volume)</th>
                                        <th class="p-2.5">주력 라인업 및 가격 포지셔닝</th>
                                        <th class="p-2.5">경쟁 구도 진단</th>
                                    </tr>
                                </thead>
                                <tbody class="divide-y divide-slate-200 text-xs">
                                    <tr class="hover:bg-slate-50 transition-colors">
                                        <td class="p-2.5 font-bold text-slate-900">Samsung</td>
                                        <td class="p-2.5 text-right font-mono-num font-bold text-primary">35.0%</td>
                                        <td class="p-2.5 text-right font-mono-num font-bold">22.9%</td>
                                        <td class="p-2.5 text-slate-600">Neo QLED, QLED (€500~€1,800)</td>
                                        <td class="p-2.5 font-medium text-slate-800">전통적 종합 1위 수성</td>
                                    </tr>
                                    <tr class="hover:bg-slate-50 transition-colors bg-blue-50/20">
                                        <td class="p-2.5 font-bold text-blue-900">LG Electronics</td>
                                        <td class="p-2.5 text-right font-mono-num font-bold text-blue-700">24.5%</td>
                                        <td class="p-2.5 text-right font-mono-num font-bold text-blue-700">16.5%</td>
                                        <td class="p-2.5 text-slate-600">OLED C5/G5, QNED (€600~€2,500)</td>
                                        <td class="p-2.5 font-bold text-blue-800">프리미엄 가치 1위, 고수익 집중</td>
                                    </tr>
                                    <tr class="hover:bg-slate-50 transition-colors bg-amber-50/20">
                                        <td class="p-2.5 font-bold text-amber-900">TCL</td>
                                        <td class="p-2.5 text-right font-mono-num font-bold text-amber-700">10.3%</td>
                                        <td class="p-2.5 text-right font-mono-num font-bold text-rose-600">17.3%</td>
                                        <td class="p-2.5 text-slate-600">MiniLED 초저가, UHD (€250~€700)</td>
                                        <td class="p-2.5 font-bold text-rose-600">⚠️ 수량 2위 급부상 (LG 추월)</td>
                                    </tr>
                                    <tr class="hover:bg-slate-50 transition-colors">
                                        <td class="p-2.5 font-bold text-slate-900">Hisense</td>
                                        <td class="p-2.5 text-right font-mono-num">4.7%</td>
                                        <td class="p-2.5 text-right font-mono-num">8.8%</td>
                                        <td class="p-2.5 text-slate-600">보급형 LCD, UHD (€200~€500)</td>
                                        <td class="p-2.5 text-slate-600">중저가 세그먼트 가격 파괴</td>
                                    </tr>
                                    <tr class="hover:bg-slate-50 transition-colors">
                                        <td class="p-2.5 font-bold text-slate-900">Local PB / Others</td>
                                        <td class="p-2.5 text-right font-mono-num">4.5%</td>
                                        <td class="p-2.5 text-right font-mono-num">8.7%</td>
                                        <td class="p-2.5 text-slate-600">로컬 PB 및 초저가 소형 (€150~€300)</td>
                                        <td class="p-2.5 text-slate-600">로컬 양판 엔트리 시장 장악</td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                    </div>

                    <!-- 3 Key Retailers Detail Cards -->
                    <div class="space-y-3 pt-2">
                        <div class="font-bold text-slate-900 text-xs sm:text-sm flex items-center gap-1.5">
                            <span class="material-symbols-outlined text-sm text-purple-700">storefront</span>
                            <span>A국 3대 가전 체인(전체 시장 매출의 70.7% 장악)별 대응 현황</span>
                        </div>
                        
                        <div class="grid grid-cols-1 md:grid-cols-3 gap-3">
                            <div class="p-4 rounded-xl bg-slate-50 border border-slate-200 space-y-2">
                                <div class="flex items-center justify-between">
                                    <span class="font-bold text-slate-900 text-xs sm:text-sm">거래선 A</span>
                                    <span class="px-2 py-0.5 rounded bg-blue-100 text-blue-800 text-[10px] font-bold">시장 점유율 45% (1위)</span>
                                </div>
                                <div class="text-[11px] text-slate-500 font-medium">대형 양판 가전체인</div>
                                <p class="text-xs text-slate-600 leading-relaxed">
                                    독점 금융 프로그램인 <strong>'자체 장기 무이자 금융 플랜(36개월)'</strong>을 전면 활용하여 OLED C5 및 대형 QNED 하이엔드 업셀링 전개. 90개 핵심 매장에 상주하는 8명의 전담 프로모터를 고수익 라인업에 집중 배치 중.
                                </p>
                            </div>

                            <div class="p-4 rounded-xl bg-slate-50 border border-slate-200 space-y-2">
                                <div class="flex items-center justify-between">
                                    <span class="font-bold text-slate-900 text-xs sm:text-sm">거래선 B</span>
                                    <span class="px-2 py-0.5 rounded bg-purple-100 text-purple-800 text-[10px] font-bold">시장 점유율 20% (2위)</span>
                                </div>
                                <div class="text-[11px] text-slate-500 font-medium">옴니채널 리테일러 체인</div>
                                <p class="text-xs text-slate-600 leading-relaxed">
                                    젊은 소비층 타깃의 온·오프라인 옴니채널 강화에 맞춰 <strong>OLED + 사운드바 패키지 프로모션</strong> 및 온라인 전용 e-쿠폰 집행을 통해 번들링 시너지 극대화.
                                </p>
                            </div>

                            <div class="p-4 rounded-xl bg-slate-50 border border-slate-200 space-y-2">
                                <div class="flex items-center justify-between">
                                    <span class="font-bold text-slate-900 text-xs sm:text-sm">거래선 C</span>
                                    <span class="px-2 py-0.5 rounded bg-teal-100 text-teal-800 text-[10px] font-bold">시장 점유율 6% (3위)</span>
                                </div>
                                <div class="text-[11px] text-slate-500 font-medium">IT / 디지털 전문 체인</div>
                                <p class="text-xs text-slate-600 leading-relaxed">
                                    게이밍 PC 수요와 연계하여 <strong>OLED 42/48인치 게이밍 전용존</strong> 구축 및 얼리어답터·VIP 게이머 타깃 마케팅을 적극 추진하여 니치 마켓 장악.
                                </p>
                            </div>
                        </div>
                    </div>
                </section>

                <!-- Section 5: Risk & Action Plan -->
                <section class="space-y-4">
                    <div class="border-b border-slate-200 pb-2">
                        <h4 class="text-base sm:text-lg font-bold text-slate-900 flex items-center gap-2">
                            <span class="w-6 h-6 rounded-md bg-purple-100 text-purple-700 flex items-center justify-center text-xs font-bold font-mono">5</span>
                            <span>핵심 리스크 진단 및 경영진 3대 실행 과제 (Action Plan)</span>
                        </h4>
                    </div>

                    <!-- Risk Alert Callout Box -->
                    <div class="p-4 rounded-xl bg-rose-50/60 border border-rose-200 space-y-2">
                        <div class="flex items-center gap-2 text-rose-800 font-bold text-xs sm:text-sm">
                            <span class="material-symbols-outlined text-base">warning</span>
                            <span>경영 리스크 경보: QNED 재고(WOS 8.3주) 누적 및 중국계 TCL 수량 M/S 잠식</span>
                        </div>
                        <ul class="text-xs text-slate-700 space-y-1.5 list-disc list-inside leading-relaxed">
                            <li>
                                <strong>QNED 재고 리스크:</strong> 전체 재고(11,899대) 중 QNED가 4,037대(34%)에 달하며 재고주수 8.3주로 권역 가이드라인(6~8주)을 초과함. 4분기 블랙프라이데이 신규 물량 입고 전 8주 이하로 소진하지 못할 경우 연말 재고 감가손 위험 상존.
                            </li>
                            <li>
                                <strong>TCL 수량 잠식 위협:</strong> TCL이 공격적인 저가 MiniLED 및 보급형 판촉으로 수량 점유율 17.3%를 기록하며 당사(16.5%)를 추월함. 메인스트림(UHD) 시장에서의 최소 점유율 방어벽 구축 필수.
                            </li>
                        </ul>
                    </div>

                    <!-- Action Items Table -->
                    <div class="space-y-2 pt-2">
                        <div class="flex items-center justify-between">
                            <h5 class="text-xs sm:text-sm font-bold text-slate-800">📋 &lt;표 5-1&gt; 경영진 3대 즉각 실행 과제 매트릭스</h5>
                        </div>
                        <div class="overflow-x-auto rounded-lg border border-slate-200 shadow-2xs">
                            <table class="w-full text-left border-collapse custom-matrix-table">
                                <thead>
                                    <tr>
                                        <th class="p-2.5">과제 분류</th>
                                        <th class="p-2.5">세부 실행 계획 (Action Items)</th>
                                        <th class="p-2.5">추진 일정</th>
                                        <th class="p-2.5 th-highlight">목표 지표</th>
                                    </tr>
                                </thead>
                                <tbody class="divide-y divide-slate-200 text-xs">
                                    <tr class="hover:bg-slate-50 transition-colors">
                                        <td class="p-2.5 font-bold text-amber-800 font-sans">[재고 정상화]<br>QNED 클리어링</td>
                                        <td class="p-2.5 text-slate-700">거래선 A '자체 무이자 금융 플랜'과 연계하여 55/65QNED80/85 대상 사운드바 캐시백 번들링 집중 판촉 전개</td>
                                        <td class="p-2.5 text-slate-600 font-mono-num">9월 3주차 ~ 10월 2주차 (4주 집중)</td>
                                        <td class="p-2.5 font-bold text-emerald-700 bg-emerald-50/20">QNED WOS 8.3주 → 6.5주 이하</td>
                                    </tr>
                                    <tr class="hover:bg-slate-50 transition-colors">
                                        <td class="p-2.5 font-bold text-blue-800 font-sans">[점유율 방어]<br>TCL 공세 대응</td>
                                        <td class="p-2.5 text-slate-700">무차별적 가격 인하를 배제하고, 고효율 60Hz 55/65인치 UHD 기획 모델 한정 공급 및 OLED 초격차 화질 매장 시연(8인 프로모터)</td>
                                        <td class="p-2.5 text-slate-600 font-mono-num">즉시 가동 ~ 10월 말</td>
                                        <td class="p-2.5 font-bold text-blue-700 bg-blue-50/20">수량 M/S 16.5% → 18.0%<br>금액 M/S 25.0% 수성</td>
                                    </tr>
                                    <tr class="hover:bg-slate-50 transition-colors">
                                        <td class="p-2.5 font-bold text-purple-800 font-sans">[수익성 극대화]<br>Q4 피크시즌 대비</td>
                                        <td class="p-2.5 text-slate-700">8월 흑자 전환 모멘텀을 이어 블랙프라이데이/사이버먼데이 타깃 OLED C5/G5 프리미엄 비중 35% 이상 유지 및 SD율 16% 이하 엄격 통제</td>
                                        <td class="p-2.5 text-slate-600 font-mono-num">10월 ~ 12월 (연말 성수기)</td>
                                        <td class="p-2.5 font-bold text-purple-700 bg-purple-50/20">Q4 OPM +5.0% 이상<br>연간 COI 목표 100% 달성</td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                    </div>
                </section>

                <!-- Section 6: Artifacts Download Card -->
                <section class="space-y-4 pt-4 border-t border-slate-200">
                    <div class="flex items-center justify-between">
                        <div class="flex items-center gap-2">
                            <span class="material-symbols-outlined text-purple-600">attach_file</span>
                            <span class="font-bold text-slate-900 text-sm">생성된 산출물 및 첨부 파일</span>
                        </div>
                        <span class="text-xs text-slate-500">단일 클릭 즉시 다운로드 가능</span>
                    </div>

                    <div class="p-4 rounded-xl bg-slate-50 border border-slate-200 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-3">
                        <div class="flex items-center gap-3">
                            <div class="w-10 h-10 rounded-lg bg-purple-100 text-purple-700 flex items-center justify-center font-bold text-xs shrink-0">DOCX</div>
                            <div>
                                <div class="text-xs font-bold text-slate-900 font-mono">유럽_A법인_2026년_8월_경영실적_보고서.docx</div>
                                <div class="text-[11px] text-slate-500">경영진 보고용 정식 워드 문서 (유럽 A 법인 / 거래선 A·B·C 가명화 적용 완료, 43.8 KB)</div>
                            </div>
                        </div>
                        <button type="button" 
                                onclick="downloadScenarioDocx()"
                                class="px-4 py-2 rounded-lg bg-purple-600 hover:bg-purple-500 text-white text-xs font-bold flex items-center gap-1.5 transition-all shadow-xs hover:scale-105 active:scale-95 shrink-0">
                            <span class="material-symbols-outlined text-sm">download</span>
                            <span>워드 보고서(.docx) 다운로드</span>
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

        const SCENARIO_DOCX_B64 = "{docx_b64}";

        function downloadScenarioDocx() {{
            try {{
                const byteCharacters = atob(SCENARIO_DOCX_B64);
                const byteNumbers = new Array(byteCharacters.length);
                for (let i = 0; i < byteCharacters.length; i++) {{
                    byteNumbers[i] = byteCharacters.charCodeAt(i);
                }}
                const byteArray = new Uint8Array(byteNumbers);
                const blob = new Blob([byteArray], {{ type: 'application/vnd.openxmlformats-officedocument.wordprocessingml.document' }});
                
                const link = document.createElement('a');
                link.href = URL.createObjectURL(blob);
                link.download = '유럽_A법인_2026년_8월_경영실적_보고서.docx';
                document.body.appendChild(link);
                link.click();
                document.body.removeChild(link);
                URL.revokeObjectURL(link.href);
            }} catch (e) {{
                window.location.href = '유럽_A법인_2026년_8월_경영실적_보고서.docx';
            }}
        }}
    </script>
</body>
</html>
"""

with open(OUTPUT_HTML, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Generated {OUTPUT_HTML} (Size: {os.path.getsize(OUTPUT_HTML)} bytes)")
