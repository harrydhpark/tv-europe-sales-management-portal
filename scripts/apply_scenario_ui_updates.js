const fs = require('fs');

// 1. Update AXIS_System_Architecture_Guide.html
const guidePath = 'd:/TV 유럽영업/15. AX Task/2026 AX 실행과제/00. TV Europe Sales Management Portal/docs/AXIS_System_Architecture_Guide.html';
let guideHtml = fs.readFileSync(guidePath, 'utf8');

// Request 1: 제목 변경
const oldTitle = '<h3 class="text-base font-bold text-slate-800">주간 권역/법인별 출하 진척률 및 유통 재고 주수(WOS) 점검</h3>';
const newTitle = '<h3 class="text-base font-bold text-slate-800">주간 지점/법인별 실판매 진척률 및 유통 재고(WOS) 점검</h3>';

console.log('guideHtml has oldTitle:', guideHtml.includes(oldTitle));
guideHtml = guideHtml.replace(oldTitle, newTitle);

// Update comment above it
guideHtml = guideHtml.replace(
    '<!-- Scenario 1: 주간 출하 및 유통재고 점검 -->',
    '<!-- Scenario 1: 주간 지점/법인별 실판매 진척률 및 유통 재고(WOS) 점검 -->'
);

// Request 2: 우측 뱃지 태그 변경 ('매주 월/화 주간회의' -> '주간 실판매 점검')
const oldBadge = '<span class="px-2.5 py-0.5 rounded bg-teal-50 text-teal-700 font-medium text-xs">매주 월/화 주간회의</span>';
const newBadge = '<span class="px-2.5 py-0.5 rounded bg-teal-50 text-teal-700 font-medium text-xs">주간 실판매 점검</span>';

console.log('guideHtml has oldBadge:', guideHtml.includes(oldBadge));
guideHtml = guideHtml.replace(oldBadge, newBadge);

// Request 3: 상황 설명은 모든 예시에서 삭제 (Scenario 1, 2, 3, 4)
// Find and remove all <p class="text-xs text-slate-600 leading-relaxed">\s*<strong>상황:</strong>[\s\S]*?</p>
const situationRegex = /\s*<p class="text-xs text-slate-600 leading-relaxed">\s*<strong>상황:<\/strong>[\s\S]*?<\/p>/g;
const matchCount = (guideHtml.match(situationRegex) || []).length;
console.log('Total situation paragraphs found to remove:', matchCount);
guideHtml = guideHtml.replace(situationRegex, '');

// Request 4: 네 번째 이미지(버튼 옆 안내 문구) 삭제
const oldGuideNoteRegex = /\s*<span class="text-\[11px\] text-slate-500 flex items-center gap-1">[\s\S]*?<span>독립 전용 창에서 무편집 원문 답변 및 16개국 엑셀 매트릭스를 쾌적하게 확인·복귀<\/span>\s*<\/span>/;
console.log('guideHtml has guide note:', oldGuideNoteRegex.test(guideHtml));
guideHtml = guideHtml.replace(oldGuideNoteRegex, '');

fs.writeFileSync(guidePath, guideHtml, 'utf8');
console.log('Successfully updated AXIS_System_Architecture_Guide.html!');

// 2. Update scenario_01_result_viewer.html
const viewerPath = 'd:/TV 유럽영업/15. AX Task/2026 AX 실행과제/00. TV Europe Sales Management Portal/docs/scenario_01_result_viewer.html';
let viewerHtml = fs.readFileSync(viewerPath, 'utf8');

const oldViewerTitle = '주간 권역/법인별 출하 진척률 및 유통 재고 주수(WOS) 점검 실전 결과';
const newViewerTitle = '주간 지점/법인별 실판매 진척률 및 유통 재고(WOS) 점검 실전 결과';

console.log('viewerHtml has oldViewerTitle:', viewerHtml.includes(oldViewerTitle));
viewerHtml = viewerHtml.replace(oldViewerTitle, newViewerTitle);

fs.writeFileSync(viewerPath, viewerHtml, 'utf8');
console.log('Successfully updated scenario_01_result_viewer.html!');
