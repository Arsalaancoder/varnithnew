import glob

files = glob.glob('**/*.html', recursive=True)
without_card = [f for f in files if 'footer-address-card' not in open(f, encoding='utf-8').read()]
print('Files without footer card:', len(without_card))
for f in without_card:
    print('  ', f)

