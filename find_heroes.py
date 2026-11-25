import glob
import re

for f in glob.glob('**/*.html', recursive=True):
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    match = re.search(r'<section[^>]*class=[\'"][^\'"]*(?:inner-hero|hero-section)[^\'"]*[\'"][^>]*style=[\'"][^\'"]*url\([^\'"]*[\'"]', content)
    if match:
        print(f, "-->", match.group(0)[:120])

