import os
import re

PAGES = [
    {
        "name": "Talent Acquisition",
        "url": "/services/hr-consulting/talent-acquisition",
        "folder_file": "services/hr-consulting/talent-acquisition/index.html",
        "flat_file": "services/hr-consulting/talent-acquisition.html",
        "heading": "Finding the Right Talent to Build a Stronger Future",
        "desc_snippet": "We help organizations identify, attract and acquire skilled professionals",
        "hero_bg": "/assets/images/talent.jpg",
        "topics": [
            "What is Talent Acquisition",
            "Our Talent Acquisition Approach",
            "Understanding Client Requirements",
            "Candidate Sourcing & Identification",
            "Technical & Non-Technical Recruitment",
            "Candidate Screening & Evaluation",
            "Interview Coordination",
            "Recruitment & Selection Support",
            "Benefits for Organizations",
            "Why Choose Varnith Global"
        ]
    },
    {
        "name": "Recruitment Process Outsourcing (RPO)",
        "url": "/services/hr-consulting/recruitment-process-outsourcing",
        "folder_file": "services/hr-consulting/recruitment-process-outsourcing/index.html",
        "flat_file": "services/hr-consulting/recruitment-process-outsourcing.html",
        "heading": "Smarter Recruitment. Scalable Hiring. Better Results.",
        "desc_snippet": "Streamline your recruitment operations with scalable hiring solutions",
        "hero_bg": "/assets/images/hr-tech-hero.jpg",
        "topics": [
            "What is Recruitment Process Outsourcing",
            "End-to-End Recruitment Solutions",
            "Recruitment Planning & Strategy",
            "Candidate Sourcing",
            "Screening & Shortlisting",
            "Interview Coordination",
            "Recruitment Process Management",
            "Scalable Hiring Solutions",
            "Benefits of RPO",
            "Why Choose Varnith Global"
        ]
    },
    {
        "name": "Executive Search & Hiring",
        "url": "/services/hr-consulting/executive-search-hiring",
        "folder_file": "services/hr-consulting/executive-search-hiring/index.html",
        "flat_file": "services/hr-consulting/executive-search-hiring.html",
        "heading": "Connecting Organizations with Exceptional Leadership Talent",
        "desc_snippet": "We support organizations in identifying and attracting experienced leadership professionals",
        "hero_bg": "/assets/images/consulting-process.jpg",
        "topics": [
            "Executive Search Overview",
            "Leadership Recruitment",
            "C-Suite Hiring",
            "Senior Management Recruitment",
            "Leadership Talent Identification",
            "Candidate Evaluation",
            "Organizational & Cultural Alignment",
            "Executive Hiring Approach",
            "Benefits to Organizations",
            "Why Choose Varnith Global"
        ]
    },
    {
        "name": "DE&I Hiring",
        "url": "/services/hr-consulting/dei-hiring",
        "folder_file": "services/hr-consulting/dei-hiring/index.html",
        "flat_file": "services/hr-consulting/dei-hiring.html",
        "heading": "Building Diverse Teams. Creating Inclusive Workplaces.",
        "desc_snippet": "We support organizations in developing inclusive recruitment approaches",
        "hero_bg": "/assets/images/about-team.jpg",
        "topics": [
            "Understanding Diversity, Equity & Inclusion",
            "Inclusive Recruitment Strategies",
            "Diverse Talent Identification",
            "Equitable Hiring Practices",
            "Inclusive Candidate Experiences",
            "Workplace Diversity",
            "Building Inclusive Teams",
            "Organizational Benefits",
            "Why Choose Varnith Global"
        ]
    },
    {
        "name": "Talent Intelligence",
        "url": "/services/hr-consulting/talent-intelligence",
        "folder_file": "services/hr-consulting/talent-intelligence/index.html",
        "flat_file": "services/hr-consulting/talent-intelligence.html",
        "heading": "Turning Talent Insights into Strategic Decisions",
        "desc_snippet": "Leverage talent intelligence and workforce insights to better understand talent markets",
        "hero_bg": "/assets/images/ai-intel.jpg",
        "topics": [
            "What is Talent Intelligence",
            "Workforce Insights",
            "Talent Market Analysis",
            "Skills & Competency Insights",
            "Workforce Planning",
            "Recruitment Market Trends",
            "Data-Informed Talent Decisions",
            "Strategic Workforce Development",
            "Organizational Benefits",
            "Why Choose Varnith Global"
        ]
    },
    {
        "name": "Technology Transformation",
        "url": "/services/technology-transformation",
        "folder_file": "services/technology-transformation/index.html",
        "flat_file": "services/technology-transformation.html",
        "heading": "Transforming Businesses Through Intelligent Technology",
        "desc_snippet": "We help organizations explore technology-led opportunities, modernize business operations",
        "hero_bg": "/assets/images/technology-expertise-cards.jpeg",
        "topics": [
            "Technology Transformation Overview",
            "IT Consulting",
            "Digital Transformation",
            "AI-Led Solutions",
            "Business Process Modernization",
            "Technology Strategy",
            "Digital Innovation",
            "Organizational Efficiency",
            "Why Choose Varnith Global"
        ]
    }
]

def run_tests():
    all_passed = True
    print("=== VERIFYING ALL SIX SERVICE PAGES ===\n")
    
    hero_bgs = set()
    
    for idx, p in enumerate(PAGES, 1):
        print(f"[{idx}/6] Verifying: {p['name']} ({p['url']})")
        
        # 1. Check folder file exists
        if not os.path.exists(p['folder_file']):
            print(f"  FAILED: Missing folder file {p['folder_file']}")
            all_passed = False
        else:
            print(f"  PASS: Found {p['folder_file']}")
            
        # 2. Check flat file exists
        if not os.path.exists(p['flat_file']):
            print(f"  FAILED: Missing flat file {p['flat_file']}")
            all_passed = False
        else:
            print(f"  PASS: Found {p['flat_file']}")
            
        # 3. Read content
        with open(p['folder_file'], 'r', encoding='utf-8') as f:
            html = f.read()
            
        # Check Hero Heading
        if p['heading'] in html:
            print(f"  PASS: Hero heading found: \"{p['heading']}\"")
        else:
            print(f"  FAILED: Hero heading NOT found: \"{p['heading']}\"")
            all_passed = False
            
        # Check Description
        if p['desc_snippet'] in html:
            print(f"  PASS: Hero description matched")
        else:
            print(f"  FAILED: Hero description NOT matched")
            all_passed = False
            
        # Check Hero Image is distinct
        if p['hero_bg'] in hero_bgs:
            print(f"  FAILED: Duplicate hero background: {p['hero_bg']}")
            all_passed = False
        else:
            hero_bgs.add(p['hero_bg'])
            print(f"  PASS: Unique hero background {p['hero_bg']}")
            
        # Check Topics
        missing_topics = []
        for t in p['topics']:
            # Search case-insensitive partial match
            t_clean = re.sub(r'[^a-zA-Z0-9 ]', '', t).lower()
            html_clean = re.sub(r'[^a-zA-Z0-9 ]', '', html).lower()
            if t_clean not in html_clean:
                missing_topics.append(t)
        if missing_topics:
            print(f"  WARNING/FAIL: Missing topics: {missing_topics}")
            all_passed = False
        else:
            print(f"  PASS: All {len(p['topics'])} required topic sections present")
            
        # Check essential components
        checks = [
            ("Breadcrumb navigation", 'class="breadcrumb"'),
            ("3D Peel Methodology cards", 'class="peel-card"'),
            ("Capabilities section", 'id="capabilities"'),
            ("Benefits section", 'TANGIBLE ADVANTAGES'),
            ("Why Varnith section", 'THE VARNITH ADVANTAGE'),
            ("Related services", 'Explore Related Solutions'),
            ("CTA section", 'GET STARTED TODAY'),
            ("Site Logo", '/assets/images/varnith-website-logo.svg'),
            ("CSS Style link", '/css/style.css'),
            ("Global Footer", 'class="footer"')
        ]
        
        for name, snippet in checks:
            if snippet in html:
                print(f"  PASS: {name} present")
            else:
                print(f"  FAILED: {name} missing snippet \"{snippet}\"")
                all_passed = False
                
        print()

    # Dropdown link check on index.html
    print("=== VERIFYING DROPDOWN IN INDEX.HTML ===")
    with open("index.html", "r", encoding="utf-8") as f:
        index_html = f.read()
        
    for p in PAGES:
        if f'href="{p["url"]}"' in index_html:
            print(f"  PASS: index.html links to {p['url']}")
        else:
            print(f"  FAILED: index.html does NOT link to {p['url']}")
            all_passed = False
            
    print("\nOVERALL STATUS:", "SUCCESS - ALL TESTS PASSED!" if all_passed else "FAILURES DETECTED")
    return all_passed

if __name__ == "__main__":
    passed = run_tests()
    exit(0 if passed else 1)

