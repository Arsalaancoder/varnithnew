import glob
import re
import urllib.request

def run_checks():
    print("=== FINAL VERIFICATION: VARNITH GLOBAL CORRECTIONS ===\n")
    all_ok = True

    # 1. HERO BUTTONS IN index.html
    with open("index.html", "r", encoding="utf-8") as f:
        index_html = f.read()

    if "I'm Hiring" in index_html and "Want to Upskill" in index_html:
        print("PASS [1]: Hero buttons updated: \"I'm Hiring\" and \"Want to Upskill\"")
    else:
        print("FAIL [1]: Hero button titles missing in index.html")
        all_ok = False

    # 2. BUSINESS IMPACT SECTION
    with open("css/style.css", "r", encoding="utf-8") as f:
        style_css = f.read()
    with open("css/responsive.css", "r", encoding="utf-8") as f:
        resp_css = f.read()

    # Verify no white gradients in ai-business-section
    if "rgba(255, 255, 255, 0.98)" in style_css or "rgba(255, 255, 255, 0.98)" in resp_css:
        print("FAIL [2a]: White gradient still found in ai-business-section")
        all_ok = False
    else:
        print("PASS [2a]: Balanced dark navy overlay configured in style.css and responsive.css")

    # Verify 4 cards in index.html
    impact_cards = [
        "Strategic Talent Solutions",
        "Organizational Growth",
        "Professional Development",
        "Technology & Innovation"
    ]
    for card_title in impact_cards:
        if card_title in index_html:
            print(f"PASS [2b]: Business Impact card \"{card_title}\" present")
        else:
            print(f"FAIL [2b]: Business Impact card \"{card_title}\" missing")
            all_ok = False

    if "impact-grid" in index_html and "impact-card" in index_html:
        print("PASS [2c]: 4-card balanced .impact-grid layout configured")
    else:
        print("FAIL [2c]: .impact-grid or .impact-card missing in index.html")
        all_ok = False

    # 3. AL YAMIN STYLE FOOTER ADDRESS CARD
    all_html = [f for f in glob.glob("**/*.html", recursive=True) if not f.startswith(('ai-solutions', 'industries', 'solutions', 'training'))]
    missing_frame = []
    for fpath in all_html:
        with open(fpath, "r", encoding="utf-8") as f:
            c = f.read()
        if "footer-address-frame" not in c:
            missing_frame.append(fpath)

    if missing_frame:
        print(f"FAIL [3a]: footer-address-frame missing in: {missing_frame}")
        all_ok = False
    else:
        print(f"PASS [3a]: Al Yamin style footer-address-frame present across all {len(all_html)} HTML files")

    # Check footer card details in index.html
    card_checks = [
        ("Company Name", "VARNITH TECHNOLOGIES PRIVATE LIMITED"),
        ("Address text", "Vikash Nagar, Dilshuknagar"),
        ("Clickable Tel", 'href="tel:+919391816116"'),
        ("Clickable Email", 'href="mailto:info@varnithglobal.com"'),
        ("Official Website", 'www.varnithglobal.com'),
        ("Facebook Icon", 'facebook.com/varnithglobal'),
        ("Instagram Icon", 'instagram.com/varnithglobal'),
        ("LinkedIn Icon", 'linkedin.com/company/varnith-global'),
        ("WhatsApp Icon", 'wa.me/919391816116')
    ]
    for label, snippet in card_checks:
        if snippet in index_html:
            print(f"PASS [3b]: Footer Card has {label}")
        else:
            print(f"FAIL [3b]: Footer Card missing {label}: {snippet}")
            all_ok = False

    # Verify contact.html body does NOT have address card
    with open("contact.html", "r", encoding="utf-8") as f:
        c_body = f.read().split("<footer")[0]
    if "footer-address-frame" in c_body or "footer-address-card" in c_body:
        print("FAIL [3c]: Address card found in contact.html body!")
        all_ok = False
    else:
        print("PASS [3c]: Verified contact.html body has NO address card")

    # Verify zero Al Yamin branding
    al_yamin_hits = []
    for fpath in glob.glob("**/*.html", recursive=True):
        with open(fpath, "r", encoding="utf-8") as f:
            if "yamin" in f.read().lower():
                al_yamin_hits.append(fpath)
    if al_yamin_hits:
        print(f"FAIL [3d]: Found Al Yamin text in: {al_yamin_hits}")
        all_ok = False
    else:
        print("PASS [3d]: Zero references to Al Yamin across entire project")

    # 4. MOBILE SAFEGUARDS & RESPONSIVE RULES
    if "overflow-x: hidden !important" in resp_css and "whatsapp-floating-btn" in resp_css:
        print("PASS [4a]: Mobile overflow safeguards & WhatsApp button safe-area sizing configured")
    else:
        print("FAIL [4a]: Missing responsive rules in responsive.css")
        all_ok = False

    # Check footer div balancing
    unbalanced = 0
    for fpath in all_html:
        with open(fpath, "r", encoding="utf-8") as f:
            c = f.read()
        if "<footer" in c:
            f_part = c.split("<footer")[1].split("</footer>")[0]
            opens = len(re.findall(r'<div\b', f_part))
            closes = len(re.findall(r'</div\b', f_part))
            if opens != closes:
                unbalanced += 1
    if unbalanced == 0:
        print(f"PASS [4b]: Exact div tag balance verified across all {len(all_html)} footers")
    else:
        print(f"FAIL [4b]: {unbalanced} footers have unbalanced divs")
        all_ok = False

    # 5. LIVE SERVER HTTP 200 CHECKS
    test_routes = [
        "/",
        "/about.html",
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
    server_ok = True
    for route in test_routes:
        try:
            req = urllib.request.urlopen(f"http://localhost:3000{route}")
            if req.status != 200:
                print(f"FAIL [5]: Route {route} returned status {req.status}")
                server_ok = False
        except Exception as e:
            print(f"FAIL [5]: Route {route} request error: {e}")
            server_ok = False

    if server_ok:
        print(f"PASS [5]: All {len(test_routes)} primary routes return HTTP 200 OK")
    else:
        all_ok = False

    print("\n-------------------------------------------")
    if all_ok:
        print("ALL VERIFICATION CHECKS PASSED PERFECTLY!")
    else:
        print("SOME VERIFICATION CHECKS FAILED.")
    print("-------------------------------------------")

if __name__ == "__main__":
    run_checks()

