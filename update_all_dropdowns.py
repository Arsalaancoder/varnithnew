import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

replacements = [
    ('href="talent-acquisition.html"', 'href="/services/hr-consulting/talent-acquisition"'),
    ('href="rpo.html"', 'href="/services/hr-consulting/recruitment-process-outsourcing"'),
    ('href="executive-hiring.html"', 'href="/services/hr-consulting/executive-search-hiring"'),
    ('href="dei-hiring.html"', 'href="/services/hr-consulting/dei-hiring"'),
    ('href="talent-intelligence.html"', 'href="/services/hr-consulting/talent-intelligence"'),
    ('href="it-services.html" class="dropdown-link"', 'href="/services/technology-transformation" class="dropdown-link"'),
    ('href="it-services.html" class="mobile-submenu-link"', 'href="/services/technology-transformation" class="mobile-submenu-link"'),
    # Also handle single-quoted or root-relative versions if any
    ('href="/talent-acquisition.html"', 'href="/services/hr-consulting/talent-acquisition"'),
    ('href="/rpo.html"', 'href="/services/hr-consulting/recruitment-process-outsourcing"'),
    ('href="/executive-hiring.html"', 'href="/services/hr-consulting/executive-search-hiring"'),
    ('href="/dei-hiring.html"', 'href="/services/hr-consulting/dei-hiring"'),
    ('href="/talent-intelligence.html"', 'href="/services/hr-consulting/talent-intelligence"'),
    ('href="/it-services.html" class="dropdown-link"', 'href="/services/technology-transformation" class="dropdown-link"'),
    ('href="/it-services.html" class="mobile-submenu-link"', 'href="/services/technology-transformation" class="mobile-submenu-link"'),
]

updated_count = 0
for f in html_files:
    # Skip the service files themselves if already pointing to correct routes
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    modified = False
    for old, new in replacements:
        if old in content:
            content = content.replace(old, new)
            modified = True
            
    if modified:
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Updated dropdown links in: {f}")
        updated_count += 1

print(f"Total files updated: {updated_count}")

