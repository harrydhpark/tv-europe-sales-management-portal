# -*- coding: utf-8 -*-
with open("d:/TV 유럽영업/15. AX Task/2026 AX 실행과제/00. TV Europe Sales Management Portal/styles.css", "r", encoding="utf-8") as f:
    text = f.read()

import re
matches = [m.start() for m in re.finditer(r'(category-tag|bento-card|\.sales|\.product|\.pricing|\.market|btn-open)', text)]
print('Matches in styles.css:', len(matches))
for pos in matches[:25]:
    print('--- MATCH ---')
    print(text[max(0, pos-40):min(len(text), pos+160)].replace('\n', ' '))
