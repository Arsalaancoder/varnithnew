import os
import glob
import re

FOOTER_CARD = '''                <!-- Corporate Address Card Column -->
                <div>
                    <div class="footer-address-card">
                        <div class="footer-address-card-header">
                            <div class="footer-address-capsule">
                                <img src="/assets/images/varnith-website-logo.svg" alt="Varnith Global Logo" class="footer-address-logo">
                            </div>
                        </div>
                        <div class="footer-address-lime-sep"></div>
                        <div class="footer-address-card-body">
                            <h4 class="footer-address-company">VARNITH TECHNOLOGIES PRIVATE LIMITED</h4>
                            <span class="footer-address-hq-label">CORPORATE HEADQUARTERS</span>
                            <div class="footer-address-divider"></div>
                            <div class="footer-address-item">
                                <span class="footer-address-subheading">OFFICE ADDRESS</span>
                                <p class="footer-address-text">
                                    4-36, 1st Floor, Vikash Nagar, Dilshuknagar,<br>
                                    Hyderabad, Telangana – 500060, India
                                </p>
                            </div>
                            <div class="footer-address-item">
                                <span class="footer-address-subheading">DIRECT TELEPHONE</span>
                                <a href="tel:+919391816116" class="footer-address-phone">+91 9391816116</a>
                            </div>
                            <div class="footer-address-item">
                                <span class="footer-address-subheading">CORPORATE EMAIL</span>
                                <a href="mailto:info@varnithglobal.com" class="footer-address-email">info@varnithglobal.com</a>
                            </div>
                            <div class="footer-address-item" style="margin-bottom: 0;">
                                <span class="footer-address-subheading">OFFICIAL WEBSITE</span>
                                <a href="https://varnithglobal.com" target="_blank" rel="noopener noreferrer" class="footer-address-web">www.varnithglobal.com</a>
                            </div>
                        </div>
                    </div>
                </div>'''

files = glob.glob('*.html')
updated = 0

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()

    if 'footer-address-card' in content:
        continue

    # Regex pattern to replace the 4th column inside <footer ...>
    # Pattern 1: <div>\s*<h4[^>]*>Contact Info</h4>\s*<p[^>]*>.*?</div>\s*</div>\s*<div[^>]*padding: 1.5rem
    # Pattern 2: <div>\s*<h4[^>]*>Contact</h4>\s*<ul[^>]*>.*?</ul>\s*</div>\s*</div>\s*<div[^>]*padding: 1.5rem
    # Pattern 3: <!-- Contact -->.*?</div>\s*</div>\s*<!-- Footer Bottom -->

    p1 = re.compile(r'<div>\s*<h4[^>]*>Contact Info</h4>\s*<p[^>]*>.*?info@varnithglobal\.com</p>\s*</div>', re.DOTALL)
    p2 = re.compile(r'<div>\s*<h4[^>]*>Contact</h4>\s*<ul[^>]*>.*?Telangana.*?</ul>\s*</div>', re.DOTALL)
    p3 = re.compile(r'<!-- Contact -->\s*<div>\s*<h4[^>]*>Contact</h4>.*?</ul>\s*</div>', re.DOTALL)

    matched = False
    if p1.search(content):
        content = p1.sub(FOOTER_CARD, content)
        matched = True
    elif p2.search(content):
        content = p2.sub(FOOTER_CARD, content)
        matched = True
    elif p3.search(content):
        content = p3.sub(FOOTER_CARD, content)
        matched = True

    if matched:
        # Also ensure grid columns are balanced
        content = re.sub(
            r'grid-template-columns:\s*2fr\s+1fr\s+1fr\s+1\.5fr;',
            'grid-template-columns: 1.8fr 1fr 1fr 1.8fr; align-items: start;',
            content
        )
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Updated footer card in: {f}")
        updated += 1
    else:
        print(f"No match for footer card in: {f}")

print(f"Total updated: {updated}")

