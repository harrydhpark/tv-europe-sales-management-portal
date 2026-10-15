# -*- coding: utf-8 -*-
import os

GUIDE_PATH = r"D:\TV 유럽영업\15. AX Task\2026 AX 실행과제\00. TV Europe Sales Management Portal\docs\AXIS_System_Architecture_Guide.html"

with open(GUIDE_PATH, "r", encoding="utf-8") as f:
    content = f.read()

s3_start = content.find("<!-- Scenario 3:")
s4_start = content.find("<!-- Scenario 4:")

if s3_start == -1 or s4_start == -1:
    print(f"Error: Markers not found. s3_start={s3_start}, s4_start={s4_start}")
    exit(1)

new_s3 = """<!-- Scenario 3: 법인별 OLED TV 내 W / G / C / B 시리즈 매출 비중 및 영업이익율·한계이익율 분석 -->
                    <div class="bg-white rounded-xl border border-slate-200 shadow-sm p-6 space-y-4 clean-card">
                        <div class="flex items-center justify-between border-b border-slate-100 pb-3">
                            <div class="flex items-center gap-3">
                                <span class="w-8 h-8 rounded-lg bg-blue-50 text-blue-700 flex items-center justify-center font-bold text-sm font-mono-num">03</span>
                                <h3 class="text-base font-bold text-slate-800">법인별 OLED TV 내 W / G / C / B 시리즈 매출 비중 및 영업이익율·한계이익율 분석</h3>
                            </div>
                            <span class="px-2.5 py-0.5 rounded bg-blue-50 text-blue-700 font-medium text-xs">OLED 시리즈 손익 분석</span>
                        </div>
                        
                        <!-- Before vs After -->
                        <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs">
                            <div class="p-4 rounded-lg bg-rose-50/50 border border-rose-100 space-y-1.5">
                                <div class="font-bold text-rose-800 flex items-center gap-1.5">
                                    <span class="material-symbols-outlined text-sm">history</span>
                                    <span>기존 수작업 방식 (Before)</span>
                                </div>
                                <p class="text-slate-600 leading-relaxed">
                                    17개 판매법인별 수백 MB에 달하는 NERP P&L Analysis 엑셀/XLSB 파일을 일일이 열고, 수십만 행의 원천 데이터에서 OLED 및 시리즈(W/G/C/B)를 필터링하여 매출액, COI, 한계이익, 수량을 각각 수작업으로 계산하고 통합하는 데 꼬박 수일(2~3일) 소요.
                                </p>
                            </div>
                            <div class="p-4 rounded-lg bg-emerald-50/50 border border-emerald-100 space-y-1.5">
                                <div class="font-bold text-emerald-800 flex items-center gap-1.5">
                                    <span class="material-symbols-outlined text-sm">check_circle</span>
                                    <span>AXIS 활용 방식 (After)</span>
                                </div>
                                <p class="text-slate-600 leading-relaxed">
                                    마스터 에이전트에게 <em>"법인별로 OLED TV 내 W / G / C 시리즈 매출 비중과 영업이익율, 한계이익율을 정리해줘"</em> 라고 질의 시, <strong>05. TV P&L Analysis</strong> 시스템과 즉시 연계하여 16개 전 법인 및 CIS의 W/G/C/B 매출 비중 100% 검증표, 영업이익율, 한계이익율 종합 매트릭스 및 전략 제언을 10초 만에 완벽 산출 (소요시간: 10초).
                                </p>
                            </div>
                        </div>

                        <!-- Live Actionable Prompt Chip -->
                        <div class="bg-slate-50 p-3.5 rounded-lg border border-slate-200">
                            <div class="text-[11px] font-bold text-slate-600 mb-1.5 flex items-center justify-between">
                                <span>마스터 에이전트 실전 질의 프롬프트 (클릭 시 복사)</span>
                                <span class="text-[10px] text-teal-600 font-semibold">One-Click Copy</span>
                            </div>
                            <div class="prompt-chip p-2.5 rounded bg-white border border-slate-200 text-xs font-mono text-slate-800 flex items-center justify-between shadow-sm" onclick="copyPrompt('법인별로 OLED TV 내 W / G / C 시리즈 매출 비중과 영업이익율, 한계이익율을 정리해줘')">
                                <span>"법인별로 OLED TV 내 W / G / C 시리즈 매출 비중과 영업이익율, 한계이익율을 정리해줘"</span>
                                <span class="material-symbols-outlined text-sm text-slate-400">content_copy</span>
                            </div>
                        </div>

                        <!-- Open Dedicated Standalone Result Viewer -->
                        <div class="mt-3.5 pt-3.5 border-t border-slate-200/80 flex flex-wrap items-center justify-between gap-3">
                            <a href="scenario_03_result_viewer.html" 
                               target="_blank" 
                               rel="noopener noreferrer"
                               class="py-2.5 px-4 rounded-lg bg-blue-600 hover:bg-blue-500 text-white text-xs font-bold flex items-center gap-2 shadow-sm transition-all hover:scale-105 active:scale-95 group">
                                <span class="material-symbols-outlined text-sm group-hover:rotate-12 transition-transform">open_in_new</span>
                                <span class="font-headline text-sm font-bold">마스터 에이전트 실전 답변 및 데이터 결과 보기</span>
                            </a>
                        </div>
                    </div>

                    """

updated_content = content[:s3_start] + new_s3 + content[s4_start:]

with open(GUIDE_PATH, "w", encoding="utf-8") as f:
    f.write(updated_content)

print("Successfully replaced Scenario 03 in AXIS_System_Architecture_Guide.html!")
