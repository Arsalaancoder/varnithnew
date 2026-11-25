import os
from build_templates import get_header, get_footer

def create_page(title, meta_desc, hero_tag, hero_title, hero_desc, hero_bg, breadcrumbs, overview_label, overview_title, overview_p1, overview_p2, overview_badges, overview_card_title, overview_card_bullets, metrics, capabilities_title, capabilities_desc, capabilities, methodology_title, methodology_desc, methodology_steps, benefits_title, benefits_desc, benefits, why_title, why_desc, why_points, related_services, active_page, target_files, capabilities_custom_html=None):
    
    # Generate HTML
    metrics_html = ""
    for idx, (label, val) in enumerate(metrics):
        border_style = 'border-left: 1px solid var(--color-border);' if idx > 0 else ''
        metrics_html += f'''
                <div style="padding: 0.5rem; {border_style}">
                    <div style="font-size: 0.78rem; text-transform: uppercase; font-weight: 800; color: var(--color-muted); letter-spacing: 0.05em;">{label}</div>
                    <div style="font-size: 1.25rem; font-weight: 800; color: var(--color-primary); margin-top: 0.25rem;">{val}</div>
                </div>'''

    badge_html = " ".join([f'<span style="background: var(--color-background); border: 1px solid var(--color-border); padding: 0.35rem 0.85rem; border-radius: 20px; font-size: 0.82rem; font-weight: 600; color: var(--color-primary-dark);">{b}</span>' for b in overview_badges])

    bullets_html = "".join([f'<li style="display: flex; align-items: center; gap: 0.65rem; font-size: 0.95rem; color: var(--color-text); font-weight: 600;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="var(--color-accent)" stroke-width="3"><polyline points="20 6 9 17 4 12"></polyline></svg> {b}</li>' for b in overview_card_bullets])

    cap_cards_html = ""
    for cap_title, cap_desc, cap_svg in capabilities:
        cap_cards_html += f'''
        <div class="card card-glass card-glass-white reveal reveal-up" style="padding: 2.25rem 2rem; border-top: 4px solid var(--color-primary); box-shadow: var(--shadow-sm); transition: transform 0.25s ease, box-shadow 0.25s ease;">
            <div style="width: 52px; height: 52px; background: rgba(10, 43, 112, 0.08); border-radius: var(--radius-sm); display: flex; align-items: center; justify-content: center; margin-bottom: 1.25rem; color: var(--color-primary);">
                {cap_svg}
            </div>
            <h3 style="font-size: 1.2rem; font-weight: 800; color: var(--color-primary-dark); margin-bottom: 0.75rem;">{cap_title}</h3>
            <p style="color: var(--color-muted); font-size: 0.92rem; line-height: 1.6; margin: 0;">{cap_desc}</p>
        </div>'''

    method_cards_html = ""
    peel_colors = [
        ("#FF7A00", "#E65100"),
        ("#00C4D8", "#0088A3"),
        ("#84CC16", "#4D7C0F"),
        ("#8B5CF6", "#5B21B6")
    ]
    for idx, (step_num, step_title, step_desc, step_icon) in enumerate(methodology_steps):
        c1, c2 = peel_colors[idx % len(peel_colors)]
        method_cards_html += f'''
                <div class="peel-card">
                    <svg class="peel-badge" viewBox="0 0 68 96" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <defs>
                            <linearGradient id="peel-{active_page}-{idx}" x1="0" y1="0" x2="60" y2="90" gradientUnits="userSpaceOnUse">
                                <stop offset="0%" stop-color="{c1}" />
                                <stop offset="100%" stop-color="{c2}" />
                            </linearGradient>
                            <linearGradient id="curl-sheen-{active_page}-{idx}" x1="0" y1="0" x2="35" y2="35" gradientUnits="userSpaceOnUse">
                                <stop offset="0%" stop-color="#FFFFFF" />
                                <stop offset="65%" stop-color="#F1F5F9" />
                                <stop offset="100%" stop-color="#CBD5E1" />
                            </linearGradient>
                        </defs>
                        <path d="M0 0 H52 C52 0 54 24 40 50 C28 72 16 86 0 96 V0 Z" fill="url(#peel-{active_page}-{idx})" />
                        <path d="M0 0 C15 3 28 15 36 36 L0 0 Z" fill="rgba(0,0,0,0.22)" transform="translate(2, 2)" />
                        <path d="M0 0 C16 4 30 16 38 38 L0 0 Z" fill="url(#curl-sheen-{active_page}-{idx})" />
                    </svg>
                    <div class="peel-card-body">
                        <h3 class="peel-card-title">{step_num}. {step_title}</h3>
                        <p class="peel-card-desc">{step_desc}</p>
                    </div>
                    <div class="peel-card-icon">
                        {step_icon}
                    </div>
                </div>'''

    benefits_cards_html = ""
    for ben_title, ben_desc, ben_metric in benefits:
        benefits_cards_html += f'''
        <div class="card card-glass card-glass-white reveal reveal-up" style="padding: 2.25rem 2rem; border-left: 4px solid var(--color-accent); box-shadow: var(--shadow-sm); transition: transform 0.25s ease, box-shadow 0.25s ease;">
            <div style="font-size: 1.5rem; font-weight: 800; color: var(--color-primary); margin-bottom: 0.5rem;">{ben_metric}</div>
            <h3 style="font-size: 1.15rem; font-weight: 800; color: var(--color-primary-dark); margin-bottom: 0.5rem;">{ben_title}</h3>
            <p style="color: var(--color-muted); font-size: 0.92rem; line-height: 1.6; margin: 0;">{ben_desc}</p>
        </div>'''

    why_cards_html = ""
    for idx, (w_title, w_desc) in enumerate(why_points):
        why_cards_html += f'''
        <div class="card card-glass card-glass-white reveal reveal-up" style="padding: 2rem; border-left: 4px solid var(--color-accent-dark); box-shadow: var(--shadow-sm);">
            <div style="font-size: 2rem; font-weight: 800; color: var(--color-accent-dark); line-height: 1; margin-bottom: 0.5rem;">0{idx+1}</div>
            <h3 style="font-size: 1.15rem; font-weight: 800; color: var(--color-primary-dark); margin-bottom: 0.5rem;">{w_title}</h3>
            <p style="color: var(--color-muted); font-size: 0.9rem; line-height: 1.6; margin: 0;">{w_desc}</p>
        </div>'''

    related_cards_html = ""
    for rel_title, rel_url, rel_desc in related_services:
        related_cards_html += f'''
        <a href="{rel_url}" class="card card-glass card-glass-white reveal reveal-up" style="text-decoration: none; padding: 1.75rem 1.5rem; border: 1px solid var(--color-border); border-radius: var(--radius-md); box-shadow: var(--shadow-xs); display: block; transition: all 0.25s ease;">
            <h4 style="color: var(--color-primary-dark); font-size: 1.05rem; font-weight: 800; margin-bottom: 0.4rem;">{rel_title} &rarr;</h4>
            <p style="color: var(--color-muted); font-size: 0.88rem; line-height: 1.5; margin: 0;">{rel_desc}</p>
        </a>'''

    breadcrumb_html = ""
    for idx, (b_title, b_url) in enumerate(breadcrumbs):
        if idx > 0:
            breadcrumb_html += '<svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="9 18 15 12 9 6"></polyline></svg>'
        if b_url:
            breadcrumb_html += f'<a href="{b_url}">{b_title}</a>'
        else:
            breadcrumb_html += f'<span>{b_title}</span>'

    # Capabilities Section Layout
    if capabilities_custom_html:
        capabilities_section_html = f'''
    <!-- CORE CAPABILITIES GRID (CUSTOM DESIGN REFERENCE) -->
    <section id="capabilities" class="section" style="background: #f8fafc; border-top: 1px solid var(--color-border); border-bottom: 1px solid var(--color-border);">
        <div class="container">
            <div class="section-header center">
                <span class="section-label">SERVICES &amp; DELIVERABLES</span>
                <h2 class="section-title">{capabilities_title}</h2>
                <p class="section-desc">{capabilities_desc}</p>
            </div>

            {capabilities_custom_html}
        </div>
    </section>'''
    else:
        capabilities_section_html = f'''
    <!-- CORE CAPABILITIES GRID -->
    <section id="capabilities" class="section">
        <div class="container">
            <div class="section-header center">
                <span class="section-label">SERVICES &amp; DELIVERABLES</span>
                <h2 class="section-title">{capabilities_title}</h2>
                <p class="section-desc">{capabilities_desc}</p>
            </div>

            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 1.5rem; margin-top: 2rem;">
                {cap_cards_html}
            </div>
        </div>
    </section>'''

    full_html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="{meta_desc}">
    <title>{title} | Varnith Global</title>
    <!-- Favicon & Icons -->
    <link rel="icon" type="image/svg+xml" href="/assets/images/favicon.svg">
    <link rel="icon" type="image/x-icon" href="/favicon.ico">
    <link rel="icon" type="image/png" sizes="32x32" href="/favicon.png">
    <link rel="apple-touch-icon" href="/favicon.png">

    <!-- Open Graph Metadata -->
    <meta property="og:type" content="website">
    <meta property="og:site_name" content="Varnith Global">
    <meta property="og:title" content="{title} | Varnith Global">
    <meta property="og:description" content="{meta_desc}">
    <meta property="og:image" content="https://varnithglobal.com{hero_bg}">

    <!-- Custom StyleSheets -->
    <link rel="stylesheet" href="/css/style.css">
    <link rel="stylesheet" href="/css/responsive.css">
    <link rel="stylesheet" href="/css/animations.css">

    <!-- Structured Data (Service Schema) -->
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "Service",
      "name": "{title}",
      "provider": {{
        "@type": "Organization",
        "name": "Varnith Global",
        "url": "https://varnithglobal.com/"
      }},
      "description": "{meta_desc}"
    }}
    </script>
</head>
<body>

{get_header(active_page)}

    <!-- INNER PAGE HERO -->
    <section class="inner-hero" style="background: linear-gradient(135deg, #060919 0%, #0c1438 60%, #060919 100%);">
        <div class="container">
            <span class="inner-hero-label">{hero_tag}</span>
            <h1 class="inner-hero-title">{hero_title}</h1>
            <p class="inner-hero-desc" style="max-width: 680px;">{hero_desc}</p>
            <div class="breadcrumb">
                {breadcrumb_html}
            </div>
            <div style="margin-top: 2rem; display: flex; gap: 1rem; flex-wrap: wrap;">
                <a href="/contact.html?service={active_page}" class="btn btn-primary">Request Consultation &rarr;</a>
                <a href="#capabilities" class="btn btn-outline" style="border-color: rgba(255,255,255,0.4); color: var(--color-white);">Explore Capabilities &darr;</a>
            </div>
        </div>
    </section>

    <!-- KEY HIGHLIGHTS BAR -->
    <div style="background-color: var(--color-white); border-bottom: 1px solid var(--color-border); padding: 1.5rem 0;">
        <div class="container">
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1.5rem; text-align: center;">
                {metrics_html}
            </div>
        </div>
    </div>

    <!-- SOLUTION OVERVIEW -->
    <section class="section" style="background-color: var(--color-white); border-bottom: 1px solid var(--color-border);">
        <div class="container">
            <div class="grid-2">
                <div class="reveal reveal-left">
                    <span class="section-label">{overview_label}</span>
                    <h2 class="section-title">{overview_title}</h2>
                    <p style="color: var(--color-muted); font-size: 1.02rem; line-height: 1.7; margin-bottom: 1.25rem;">
                        {overview_p1}
                    </p>
                    <p style="color: var(--color-muted); font-size: 1.02rem; line-height: 1.7; margin-bottom: 2rem;">
                        {overview_p2}
                    </p>
                    <div style="display: flex; gap: 0.75rem; flex-wrap: wrap;">
                        {badge_html}
                    </div>
                </div>
                <div class="reveal reveal-right">
                    <div class="card card-glass card-glass-white" style="padding: 2.5rem; border-left: 4px solid var(--color-primary); box-shadow: var(--shadow-sm);">
                        <h3 style="font-size: 1.25rem; font-weight: 800; color: var(--color-primary-dark); margin-bottom: 1.25rem;">{overview_card_title}</h3>
                        <ul style="list-style: none; display: flex; flex-direction: column; gap: 0.85rem; margin-bottom: 1.75rem; padding: 0;">
                            {bullets_html}
                        </ul>
                        <div style="background: var(--color-background); border-radius: var(--radius-sm); padding: 1.25rem;">
                            <div style="font-weight: 700; color: var(--color-primary-dark); font-size: 0.95rem; margin-bottom: 0.25rem;">Custom Enterprise Engagement</div>
                            <p style="font-size: 0.88rem; color: var(--color-muted); margin: 0; line-height: 1.5;">We adapt to your organizational structures, tech stack demands, and growth milestones with custom SLA terms.</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

{capabilities_section_html}

    <!-- CONSULTING PROCESS INTEGRATION (CORNER PEEL METHODOLOGY) -->
    <section class="section" style="background-color: var(--color-white); border-top: 1px solid var(--color-border); border-bottom: 1px solid var(--color-border);">
        <div class="container">
            <div class="section-header center">
                <span class="section-label" style="background: rgba(10, 43, 112, 0.08); color: var(--color-primary); padding: 0.35rem 1rem; border-radius: 20px; font-size: 0.8rem; font-weight: 800; letter-spacing: 0.1em;">OUR METHODOLOGY</span>
                <h2 class="section-title">{methodology_title}</h2>
                <p class="section-desc">{methodology_desc}</p>
            </div>

            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1.75rem; margin-top: 2.5rem;" class="reveal reveal-up">
                {method_cards_html}
            </div>

            <div style="text-align: center; margin-top: 3rem; padding-top: 1.5rem; border-top: 1px solid var(--color-border);">
                <span style="font-size: 0.9rem; font-weight: 800; letter-spacing: 0.2em; color: var(--color-primary); text-transform: uppercase;">PARTNERSHIP &nbsp;&bull;&nbsp; INNOVATION &nbsp;&bull;&nbsp; GROWTH</span>
            </div>
        </div>
    </section>

    <!-- BENEFITS SECTION -->
    <section class="section">
        <div class="container">
            <div class="section-header center">
                <span class="section-label">TANGIBLE ADVANTAGES</span>
                <h2 class="section-title">{benefits_title}</h2>
                <p class="section-desc">{benefits_desc}</p>
            </div>

            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 1.5rem; margin-top: 2rem;">
                {benefits_cards_html}
            </div>
        </div>
    </section>

    <!-- WHY VARNITH GLOBAL -->
    <section class="section" style="background-color: var(--color-white); border-top: 1px solid var(--color-border); border-bottom: 1px solid var(--color-border);">
        <div class="container">
            <div class="section-header center">
                <span class="section-label">THE VARNITH ADVANTAGE</span>
                <h2 class="section-title">{why_title}</h2>
                <p class="section-desc">{why_desc}</p>
            </div>

            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.5rem; margin-top: 2rem;">
                {why_cards_html}
            </div>
        </div>
    </section>

    <!-- RELATED SERVICES -->
    <section class="section">
        <div class="container">
            <div class="section-header center">
                <span class="section-label">EXPAND YOUR CAPABILITIES</span>
                <h2 class="section-title">Explore Related Solutions</h2>
                <p class="section-desc">Connect talent acquisition, strategic outsourcing, workforce intelligence, and enterprise technology under one integrated partner.</p>
            </div>

            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 1.5rem; margin-top: 2rem;">
                {related_cards_html}
            </div>
        </div>
    </section>

    <!-- FINAL CTA SECTION -->
    <section class="section section-dark" style="text-align: center;">
        <div class="container">
            <span class="section-label" style="color: var(--color-accent); font-weight: 800; letter-spacing: 0.1em;">GET STARTED TODAY</span>
            <h2 class="section-title" style="color: var(--color-white); max-width: 700px; margin: 0 auto 1.5rem;">Ready to Transform Your Organization with Varnith Global?</h2>
            <p style="color: #d0dbe5; max-width: 600px; margin: 0 auto 2.5rem; font-size: 1.05rem; line-height: 1.6;">
                Schedule a confidential consultation with our specialized HR consulting and technology advisors to discuss your exact talent or transformation requirements.
            </p>
            <div style="display: flex; gap: 1.25rem; justify-content: center; flex-wrap: wrap;">
                <a href="/contact.html?service={active_page}" class="btn btn-primary" style="padding: 0.95rem 2.25rem; font-size: 1rem;">Schedule Consultation &rarr;</a>
                <a href="/services.html" class="btn btn-outline" style="border-color: rgba(255,255,255,0.6); color: var(--color-white); padding: 0.95rem 2.25rem; font-size: 1rem;">View All Solutions</a>
            </div>
        </div>
    </section>

{get_footer()}
</body>
</html>'''

    for tf in target_files:
        dir_name = os.path.dirname(tf)
        if dir_name:
            os.makedirs(dir_name, exist_ok=True)
        with open(tf, 'w', encoding='utf-8') as f:
            f.write(full_html)
        print(f"Generated: {tf}")

print("Generator function ready.")
