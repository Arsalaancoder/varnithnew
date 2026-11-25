import glob
import re

def verify_all():
    print("=== VERIFYING VARNITH GLOBAL LATEST CORRECTIONS ===\n")
    all_ok = True

    # 1. ANNOUNCEMENT BAR #f6aa1c
    with open("css/style.css", "r", encoding="utf-8") as f:
        css = f.read()
    
    if "#f6aa1c" in css and ".announcement-bar" in css:
        print("PASS [1]: Announcement bar background color #f6aa1c configured in css/style.css")
    else:
        print("FAIL [1]: #f6aa1c missing from .announcement-bar in css/style.css")
        all_ok = False

    # 2. HERO GREEN LABEL STRIP FIX
    if "inner-hero-label" in css and "width: fit-content !important" in css:
        print("PASS [2a]: .inner-hero-label styled as compact fit-content pill in css/style.css")
    else:
        print("FAIL [2a]: .inner-hero-label missing fit-content styling in css/style.css")
        all_ok = False

    service_files = glob.glob("services/hr-consulting/**/*.html", recursive=True) + glob.glob("course-*.html")
    full_width_found = []
    for sf in service_files:
        with open(sf, "r", encoding="utf-8") as f:
            c = f.read()
        # Ensure that inner-hero-label does not have an inline style stretching it full width
        if re.search(r'<span[^>]*class=[\'"][^\'"]*inner-hero-label[^\'"]*[\'"][^>]*style=[\'"][^\'"]*width:\s*100%', c):
            full_width_found.append(sf)
    if full_width_found:
        print(f"FAIL [2b]: Full-width label styles found in: {full_width_found}")
        all_ok = False
    else:
        print(f"PASS [2b]: No full-width inline strips in hero labels across {len(service_files)} service/course files")

    # 3. CONTACT PAGE RESTORATION
    with open("contact.html", "r", encoding="utf-8") as f:
        contact_html = f.read()

    # Must NOT have address card in body
    body_content = contact_html.split("<footer")[0]
    if "footer-address-card" in body_content or "varnith-address-card" in body_content:
        print("FAIL [3a]: Address card found in contact.html body")
        all_ok = False
    else:
        print("PASS [3a]: Corporate address card removed from contact.html body")

    # Must have the 3 original pastel cards
    if "card-tint-blue" in contact_html and "card-tint-green" in contact_html and "card-tint-purple" in contact_html:
        print("PASS [3b]: Original 3 contact info cards (Phone, Email, Office Address) restored")
    else:
        print("FAIL [3b]: Original contact info cards missing in contact.html")
        all_ok = False

    # Must have contact form and map
    if "form" in contact_html and "iframe" in contact_html:
        print("PASS [3c]: Original contact form and Google map iframe restored in contact.html")
    else:
        print("FAIL [3c]: Contact form or map iframe missing in contact.html")
        all_ok = False

    # 4. FOOTER ADDRESS CARD
    core_pages = [
        "index.html",
        "about.html",
        "contact.html",
        "services.html",
        "courses.html",
        "privacy-policy.html",
        "terms.html",
        "404.html",
        "talent-acquisition.html",
        "rpo.html",
        "executive-hiring.html",
        "dei-hiring.html",
        "talent-intelligence.html",
        "technology-transformation.html"
    ] + glob.glob("course-*.html")

    missing_footer_card = []
    for page in core_pages:
        with open(page, "r", encoding="utf-8") as f:
            c = f.read()
        if "footer-address-card" not in c:
            missing_footer_card.append(page)

    if missing_footer_card:
        print(f"FAIL [4a]: footer-address-card missing in: {missing_footer_card}")
        all_ok = False
    else:
        print(f"PASS [4a]: footer-address-card present across all {len(core_pages)} core pages and courses")

    # Check footer address card contents in index.html
    with open("index.html", "r", encoding="utf-8") as f:
        idx = f.read()
    
    footer_checks = [
        ("Company Name", lambda t: "VARNITH TECHNOLOGIES PRIVATE LIMITED" in t),
        ("Headquarters Label", lambda t: "CORPORATE HEADQUARTERS" in t),
        ("Office Address", lambda t: "1st Floor, Vikash Nagar, Dilshuknagar" in t and ("4-36" in t or "4–36" in t)),
        ("Direct Phone", lambda t: "tel:+919391816116" in t),
        ("Corporate Email", lambda t: "mailto:info@varnithglobal.com" in t),
        ("Official Website", lambda t: "www.varnithglobal.com" in t)
    ]
    for label, check_fn in footer_checks:
        if check_fn(idx):
            print(f"PASS [4b]: Footer Card has valid {label}")
        else:
            print(f"FAIL [4b]: Footer Card check failed for {label}")
            all_ok = False

    # 5. ZERO AL YAMIN BRANDING
    all_html = glob.glob("**/*.html", recursive=True)
    alyamin = []
    for h in all_html:
        with open(h, "r", encoding="utf-8") as f:
            if "yamin" in f.read().lower():
                alyamin.append(h)
    if alyamin:
        print(f"FAIL [5]: Al Yamin references found in: {alyamin}")
        all_ok = False
    else:
        print("PASS [5]: Zero references to Al Yamin across entire project")

    print("\n-------------------------------------------")
    if all_ok:
        print("ALL VERIFICATION CHECKS PASSED SUCCESSFULLY!")
    else:
        print("SOME VERIFICATION CHECKS FAILED.")
    print("-------------------------------------------")

if __name__ == "__main__":
    verify_all()
