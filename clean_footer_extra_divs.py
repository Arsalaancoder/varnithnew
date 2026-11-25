import glob
import re

all_html = glob.glob("**/*.html", recursive=True)

for f in all_html:
    if f.startswith(('ai-solutions', 'industries', 'solutions', 'training')):
        continue
    with open(f, "r", encoding="utf-8") as fp:
        c = fp.read()
    
    if "<footer" not in c:
        continue
    
    # Check if there is </div>\s*</div>\s*</div> right before bottom bar
    # We want: 
    # </div> (closes column 4)
    # </div> (closes footer-grid)
    # followed by bottom bar
    
    # Replace any triple closing </div>\s*</div>\s*</div> before bottom bar
    new_c = re.sub(
        r'(</div>\s*</div>)\s*</div>\s*(?=(?:\s*<!-- Footer Bottom|\s*<!-- Bottom Legal Bar|\s*<div\s*style=[\'"][^\'"]*padding:\s*1\.5rem))',
        r'\1',
        c
    )
    if new_c != c:
        with open(f, "w", encoding="utf-8") as fp:
            fp.write(new_c)
        print(f"Removed extra closing div in: {f}")


