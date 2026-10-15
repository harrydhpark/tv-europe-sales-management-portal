const fs = require('fs');
const path = 'd:/TV 유럽영업/15. AX Task/2026 AX 실행과제/00. TV Europe Sales Management Portal/docs/AXIS_System_Architecture_Guide.html';
const html = fs.readFileSync(path, 'utf8');

const sIdx = html.indexOf('id="tab-scenarios"');
console.log('Section index:', sIdx);
if (sIdx !== -1) {
    console.log(html.substring(sIdx, sIdx + 5000));
}
