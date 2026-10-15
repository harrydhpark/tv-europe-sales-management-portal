const fs = require('fs');
const path = 'd:/TV 유럽영업/15. AX Task/2026 AX 실행과제/00. TV Europe Sales Management Portal/docs/AXIS_System_Architecture_Guide.html';
const html = fs.readFileSync(path, 'utf8');

const regex = /tab-roadmap/g;
let m;
while ((m = regex.exec(html)) !== null) {
    console.log('Match tab-roadmap at', m.index);
    console.log(html.substring(Math.max(0, m.index - 50), Math.min(html.length, m.index + 80)));
    console.log('---');
}
