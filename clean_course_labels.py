import glob

for f in glob.glob('course-*.html'):
    with open(f, 'r', encoding='utf-8') as file:
        c = file.read()
    c = c.replace(' style="background: rgba(140, 198, 63, 0.2); color: var(--color-accent); border: 1px solid rgba(140, 198, 63, 0.4);"', '')
    with open(f, 'w', encoding='utf-8') as file:
        file.write(c)

print('Cleaned course labels')

