"""Static QA for the bilingual single-scroll portfolio. Run after npm run build."""
import json
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / 'dist'

class Inspector(HTMLParser):
    def __init__(self, source):
        super().__init__()
        self.tags = []
        self.ids = []
        self.feed(source)
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self.tags.append((tag, attrs))
        if 'id' in attrs:
            self.ids.append(attrs['id'])

checks = 0

def check(condition, message):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(message)

projects = [json.loads(p.read_text(encoding='utf-8')) for p in (ROOT / 'src/content/projects').glob('*.json')]
published = [p for p in projects if p['visibility'] == 'published']
for locale in ('ar', 'en'):
    path = DIST / locale / 'index.html'
    check(path.exists(), f'{locale}: home output exists')
    source = path.read_text(encoding='utf-8')
    page = Inspector(source)
    html = next(attrs for tag, attrs in page.tags if tag == 'html')
    check(html.get('lang') == locale, f'{locale}: language')
    check(html.get('dir') == ('rtl' if locale == 'ar' else 'ltr'), f'{locale}: text direction')
    check(len(page.ids) == len(set(page.ids)), f'{locale}: unique element IDs')
    check(sum(tag == 'h1' for tag, _ in page.tags) == 1, f'{locale}: exactly one H1')
    check(any(tag == 'meta' and attrs.get('name') == 'description' for tag, attrs in page.tags), f'{locale}: description')
    check(any(tag == 'link' and attrs.get('rel') == 'canonical' for tag, attrs in page.tags), f'{locale}: canonical')
    for anchor in ('top', 'work', 'expertise', 'about', 'contact'):
        check(anchor in page.ids, f'{locale}: section {anchor}')
    for tag, attrs in page.tags:
        if tag == 'a' and attrs.get('href', '').startswith('#'):
            check(attrs['href'][1:] in page.ids, f'{locale}: section link {attrs["href"]}')
        if tag == 'img' and not attrs.get('src', '').startswith('data:'):
            image = DIST / unquote(urlsplit(attrs['src']).path.lstrip('/'))
            check(image.is_file(), f'{locale}: image {image}')
            check('alt' in attrs, f'{locale}: image alternative text')
        if tag == 'a' and attrs.get('target') == '_blank':
            check('noopener' in attrs.get('rel', ''), f'{locale}: safe new tab')
    for project in published:
        check('project-' + project['slug'] in page.ids, f'{locale}: published project {project["slug"]}')
        legacy = DIST / locale / 'projects' / project['slug'] / 'index.html'
        check(legacy.is_file(), f'{locale}: legacy project route')
        check(f'/{locale}/#project-{project["slug"]}' in legacy.read_text(encoding='utf-8'), f'{locale}: correct project redirect')
    for project in projects:
        if project['visibility'] != 'published':
            check(('project-' + project['slug']) not in page.ids, f'{locale}: non-public project excluded')
    for old, target in [('about', 'about'), ('contact', 'contact'), ('expertise', 'expertise'), ('projects', 'work')]:
        legacy = (DIST / locale / old / 'index.html').read_text(encoding='utf-8')
        check(f'/{locale}/#{target}' in legacy, f'{locale}: legacy {old} redirect')
    check(not any(tag == 'form' for tag, _ in page.tags), f'{locale}: no non-working contact form')
    check('users.noreply.github.com' not in source, f'{locale}: no placeholder email')

sitemap = (DIST / 'sitemap.xml').read_text(encoding='utf-8')
check(sitemap.count('<loc>') == 2, 'Sitemap has exactly two language views')
check('/projects/' not in sitemap, 'Legacy routes excluded from sitemap')
print(f'PASS: {checks} static checks. Visual layout, live deployment, and external links require separate browser checks.')
