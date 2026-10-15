const fs = require('fs');

// 1. Update AXIS_System_Architecture_Guide.html
const guidePath = 'd:/TV 유럽영업/15. AX Task/2026 AX 실행과제/00. TV Europe Sales Management Portal/docs/AXIS_System_Architecture_Guide.html';
let guideHtml = fs.readFileSync(guidePath, 'utf8');

const g1 = '<span>6. 실무 활용 방안 & 시나리오</span>';
const g1_rep = '<span>6. 실무 활용 예시</span>';

const g2 = '<!-- TAB 6: 실무 활용 방안 & 시나리오 (Operational Scenarios Full Detail) -->';
const g2_rep = '<!-- TAB 6: 실무 활용 예시 (Operational Scenarios Full Detail) -->';

const g3 = '<h2 class="text-2xl font-bold text-primary tracking-tight font-headline">6. 실무 활용 방안 & 시나리오</h2>';
const g3_rep = '<h2 class="text-2xl font-bold text-primary tracking-tight font-headline">6. 실무 활용 예시</h2>';

console.log('Guide has g1:', guideHtml.includes(g1));
console.log('Guide has g2:', guideHtml.includes(g2));
console.log('Guide has g3:', guideHtml.includes(g3));

guideHtml = guideHtml.replace(g1, g1_rep).replace(g2, g2_rep).replace(g3, g3_rep);
fs.writeFileSync(guidePath, guideHtml, 'utf8');
console.log('Successfully updated AXIS_System_Architecture_Guide.html');

// 2. Update scenario_01_result_viewer.html
const viewerPath = 'd:/TV 유럽영업/15. AX Task/2026 AX 실행과제/00. TV Europe Sales Management Portal/docs/scenario_01_result_viewer.html';
let viewerHtml = fs.readFileSync(viewerPath, 'utf8');

console.log('Viewer has g1:', viewerHtml.includes(g1));
viewerHtml = viewerHtml.replace(g1, g1_rep);
fs.writeFileSync(viewerPath, viewerHtml, 'utf8');
console.log('Successfully updated scenario_01_result_viewer.html');
