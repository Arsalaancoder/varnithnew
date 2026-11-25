import glob
import re
import urllib.request

def run_tests():
    all_passed = True
    print("=== FINAL TESTING: VARNITH GLOBAL DESIGN CORRECTIONS ===\n")

    # 1. Check index.html hero logo pill
    with open("index.html", "r", encoding="utf-8") as f:
        index_html = f.read()
    if "hero-brand-pill" in index_html:
        print("FAILED: index.html still contains hero-brand-pill")
        all_passed = False
    else:
        print("PASS: Logo removed from hero in index.html")

    # 2. Check hero background images in HR consulting & course pages
    target_pages = [
        "services.html",
        "courses.html",
        "services/hr-consulting/talent-acquisition/index.html",
        "services/hr-consulting/recruitment-process-outsourcing/index.html",
        "services/hr-consulting/executive-search-hiring/index.html",
        "services/hr-consulting/dei-hiring/index.html",
        "services/hr-consulting/talent-intelligence/index.html",
        "services/technology-transformation/index.html"
    ] + glob.glob("course-*.html")

    hero_img_failures = []
    for page in target_pages:
        with open(page, "r", encoding="utf-8") as f:
            content = f.read()
        match = re.search(r'<section[^>]*class=[\'"][^\'"]*inner-hero[^\'"]*[\'"][^>]*style=[\'"][^\'"]*url\([^\'"]*[\'"]', content)
        if match:
            hero_img_failures.append(page)
    
    if hero_img_failures:
        print(f"FAILED: Found hero background images in: {hero_img_failures}")
        all_passed = False
    else:
        print(f"PASS: Zero unwanted hero background images found across {len(target_pages)} HR Consulting & Course pages")

    # 3. Check WhatsApp floating button across ALL HTML files
    all_html_files = glob.glob("**/*.html", recursive=True)
    wa_missing = []
    for page in all_html_files:
        with open(page, "r", encoding="utf-8") as f:
            content = f.read()
        if "whatsapp-floating-btn" not in content:
            wa_missing.append(page)
        if "wa.me/919391816116" not in content:
            wa_missing.append(f"{page} (bad link)")

    if wa_missing:
        print(f"FAILED: WhatsApp button missing/invalid in: {wa_missing}")
        all_passed = False
    else:
        print(f"PASS: WhatsApp floating button verified across all {len(all_html_files)} HTML pages with verified link")

    # 4. Check contact.html redesigned address card
    with open("contact.html", "r", encoding="utf-8") as f:
        contact_html = f.read()

    contact_checks = [
        ("Varnith address card class", "varnith-address-card"),
        ("Official Varnith logo in card", "/assets/images/varnith-website-logo.svg"),
        ("Company name", "VARNITH TECHNOLOGIES PRIVATE LIMITED"),
        ("Clickable tel", 'href="tel:+919391816116"'),
        ("Clickable email", 'href="mailto:info@varnithglobal.com"'),
        ("Official website", 'href="https://varnithglobal.com"'),
        ("LinkedIn link", 'https://www.linkedin.com/company/varnith-global'),
        ("Two-column layout (grid-2)", "grid-2"),
        ("Enquiry form present", 'id="varnith-contact-form"')
    ]

    for label, snippet in contact_checks:
        if snippet in contact_html:
            print(f"PASS: Contact page - {label} present")
        else:
            print(f"FAILED: Contact page - {label} missing snippet \"{snippet}\"")
            all_passed = False

    # Check for no Al Yamin branding anywhere in whole workspace
    al_yamin_found = []
    for page in all_html_files:
        with open(page, "r", encoding="utf-8") as f:
            c = f.read().lower()
        if "yamin" in c:
            al_yamin_found.append(page)
    if al_yamin_found:
        print(f"FAILED: Al Yamin reference found in {al_yamin_found}")
        all_passed = False
    else:
        print("PASS: Verified zero references to Al Yamin across entire website")

    # 5. Check HTTP 200 on local server
    test_urls = [
        "/",
        "/contact.html",
        "/services.html",
        "/courses.html",
        "/services/hr-consulting/talent-acquisition",
        "/services/hr-consulting/recruitment-process-outsourcing",
        "/services/hr-consulting/executive-search-hiring",
        "/services/hr-consulting/dei-hiring",
        "/services/hr-consulting/talent-intelligence",
        "/services/technology-transformation"
    ]
    print("\n--- Testing HTTP status codes on local server (port 3000) ---")
    server_ok = True
    for u in test_urls:
        try:
            req = urllib.request.urlopen("http://localhost:3000" + u)
            status = req.getcode()
            print(f"  {u} -> {status} OK")
        except Exception as e:
            print(f"  {u} -> Error: {e}")
            server_ok = False
            all_passed = False

    print("\nOVERALL TEST RESULT:", "SUCCESS - ALL TESTS PASSED!" if all_passed else "FAILURES DETECTED")
    return all_passed

if __name__ == "__main__":
    passed = run_tests()
    exit(0 if passed else 1)

