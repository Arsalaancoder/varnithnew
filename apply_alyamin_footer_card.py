import glob
import re

new_card_inner = """<div class="footer-address-frame">
                        <div class="footer-card-top-accent"></div>
                        <div class="footer-address-inner">
                            <div class="footer-card-logo-box">
                                <img src="{prefix}assets/images/varnith-website-logo.svg" alt="Varnith Technologies Private Limited" class="footer-card-logo">
                            </div>
                            <h4 class="footer-card-company">VARNITH TECHNOLOGIES PRIVATE LIMITED</h4>
                            <p class="footer-card-address">
                                4–36, 1st Floor, Vikash Nagar, Dilshuknagar,<br>
                                Hyderabad, Telangana – 500060, India
                            </p>
                            <div class="footer-card-line">
                                <span class="label">Tel :</span> <a href="tel:+919391816116" class="contact-link">+91 9391816116</a>
                            </div>
                            <div class="footer-card-line">
                                <span class="label">Email :</span> <a href="mailto:info@varnithglobal.com" class="contact-link">info@varnithglobal.com</a>
                            </div>
                            <div class="footer-card-web">
                                <a href="https://www.varnithglobal.com" target="_blank" rel="noopener noreferrer" class="web-link">www.varnithglobal.com</a>
                            </div>
                            <div class="footer-card-socials">
                                <a href="https://www.facebook.com/varnithglobal" target="_blank" rel="noopener noreferrer" class="social-circle" aria-label="Facebook">
                                    <svg width="15" height="15" viewBox="0 0 24 24" fill="currentColor"><path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/></svg>
                                </a>
                                <a href="https://www.instagram.com/varnithglobal" target="_blank" rel="noopener noreferrer" class="social-circle" aria-label="Instagram">
                                    <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line></svg>
                                </a>
                                <a href="https://www.linkedin.com/company/varnith-global" target="_blank" rel="noopener noreferrer" class="social-circle" aria-label="LinkedIn">
                                    <svg width="15" height="15" viewBox="0 0 24 24" fill="currentColor"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"></path><rect x="2" y="9" width="4" height="12"></rect><circle cx="4" cy="4" r="2"></circle></svg>
                                </a>
                                <a href="https://wa.me/919391816116?text=Hello%20Varnith%20Global%2C%20I%20would%20like%20to%20know%20more%20about%20your%20services." target="_blank" rel="noopener noreferrer" class="social-circle" aria-label="WhatsApp">
                                    <svg width="15" height="15" viewBox="0 0 24 24" fill="currentColor"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 0 1-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 0 1-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 0 1 2.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0 0 12.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 0 0 5.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 0 0-3.48-8.413Z"/></svg>
                                </a>
                            </div>
                        </div>
                    </div>"""

pattern = re.compile(r'<div class="footer-address-card">.*?</div>\s*</div>\s*(?=</div>|\s*<!-- Footer Bottom)', re.DOTALL)

target_files = [
    "index.html",
    "about.html",
    "contact.html",
    "courses.html",
    "services.html",
    "privacy-policy.html",
    "terms.html",
    "404.html"
] + glob.glob("course-*.html")

updated_count = 0
for fpath in target_files:
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    if '<div class="footer-address-card">' in content:
        prefix = ""
        card_html = new_card_inner.format(prefix=prefix)
        # We replace the whole <div class="footer-address-card">...</div>
        # Let's find exactly the matching block
        new_content = re.sub(r'<div class="footer-address-card">.*?</div>\s*</div>\s*(?=\s*</div>\s*(?:<!-- Footer Bottom|</div>))', card_html + "\n                </div>", content, flags=re.DOTALL)
        if new_content != content:
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"Updated: {fpath}")
            updated_count += 1
        else:
            print(f"Regex no replace: {fpath}")
    else:
        print(f"Skipping (no footer-address-card): {fpath}")

print(f"\nTotal files updated with Al Yamin footer address card: {updated_count}")

