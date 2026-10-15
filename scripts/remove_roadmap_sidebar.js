const fs = require('fs');

const guidePath = 'd:/TV 유럽영업/15. AX Task/2026 AX 실행과제/00. TV Europe Sales Management Portal/docs/AXIS_System_Architecture_Guide.html';
let guideHtml = fs.readFileSync(guidePath, 'utf8');

// Target button in sidebar to remove
const targetSnippet = `            <button class="nav-item w-full flex items-center gap-3 px-3.5 py-2.5 rounded-lg text-left text-white/80 hover:text-white hover:bg-white/5 transition-all text-xs" onclick="showTab('tab-roadmap', this)">
                <span class="material-symbols-outlined text-base">trending_up</span>
                <span>7. FAQ, 도입효과 & 로드맵</span>
            </button>`;

if (guideHtml.includes(targetSnippet)) {
    guideHtml = guideHtml.replace(targetSnippet, '');
    fs.writeFileSync(guidePath, guideHtml, 'utf8');
    console.log('Successfully removed 7. FAQ, 도입효과 & 로드맵 from sidebar navigation!');
} else {
    // Check regex fallback with whitespace tolerance
    const regex = /\s*<button class="nav-item[^"]*" onclick="showTab\('tab-roadmap'[^>]*>[\s\S]*?<\/button>/;
    if (regex.test(guideHtml)) {
        guideHtml = guideHtml.replace(regex, '');
        fs.writeFileSync(guidePath, guideHtml, 'utf8');
        console.log('Successfully removed using regex fallback!');
    } else {
        console.log('Error: Target button not found in guide html.');
    }
}
