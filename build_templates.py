import os

def get_header(active_page=""):
    return f'''    <!-- TOP ANNOUNCEMENT BAR -->
    <div class="announcement-bar">
        <div class="container">
            <span class="announcement-text">HR Consulting · Talent Solutions · Training &amp; Development · Technology Transformation</span>
            <div class="announcement-links">
                <a href="mailto:info@varnithglobal.com" class="announcement-link">
                    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><polyline points="22,6 12,13 2,6"></polyline></svg>
                    info@varnithglobal.com
                </a>
                <a href="tel:+919391816116" class="announcement-link">
                    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07A19.5 19.5 0 0 1 4.69 12 19.79 19.79 0 0 1 1.61 3.42C1.6 2.3 2.4 1.44 3.52 1.44h3a2 2 0 0 1 2 1.72c.127.96.361 1.903.7 2.81a2 2 0 0 1-.45 2.11L7.91 9.91a16 16 0 0 0 6.09 6.09l1.63-1.63a2 2 0 0 1 2.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>
                    +91 9391816116
                </a>
            </div>
        </div>
    </div>

    <!-- STICKY HEADER & NAV -->
    <header class="header-nav">
        <div class="container">
            <a href="/" class="logo" aria-label="Varnith Global Home">
                <img src="/assets/images/varnith-website-logo.svg" alt="Varnith Global" class="site-logo">
            </a>

            <!-- Desktop Menu -->
            <nav class="nav-menu">
                <div class="nav-item">
                    <a href="/" class="nav-link">Home</a>
                </div>
                <div class="nav-item">
                    <a href="/about.html" class="nav-link">About Us</a>
                </div>
                <div class="nav-item has-dropdown active">
                    <a href="/services.html" class="nav-link dropdown-toggle" aria-haspopup="true" aria-expanded="false">
                        HR Consulting
                        <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"></polyline></svg>
                    </a>
                    <div class="dropdown-menu dropdown-hr-consulting">
                        <a href="/services/hr-consulting/talent-acquisition" class="dropdown-link {'active' if active_page == 'talent-acquisition' else ''}">
                            <strong>Talent Acquisition</strong>
                            <span>Sourcing, technical &amp; volume recruitment</span>
                        </a>
                        <a href="/services/hr-consulting/recruitment-process-outsourcing" class="dropdown-link {'active' if active_page == 'rpo' else ''}">
                            <strong>Recruitment Process Outsourcing (RPO)</strong>
                            <span>End-to-end scalable hiring solutions</span>
                        </a>
                        <a href="/services/hr-consulting/executive-search-hiring" class="dropdown-link {'active' if active_page == 'executive-search' else ''}">
                            <strong>Executive Search &amp; Hiring</strong>
                            <span>Leadership &amp; C-suite placements</span>
                        </a>
                        <a href="/services/hr-consulting/dei-hiring" class="dropdown-link {'active' if active_page == 'dei-hiring' else ''}">
                            <strong>DE&amp;I Hiring</strong>
                            <span>Diversity, Equity &amp; Inclusion strategies</span>
                        </a>
                        <a href="/services/hr-consulting/talent-intelligence" class="dropdown-link {'active' if active_page == 'talent-intelligence' else ''}">
                            <strong>Talent Intelligence</strong>
                            <span>Market analytics &amp; workforce planning</span>
                        </a>
                        <a href="/services/technology-transformation" class="dropdown-link {'active' if active_page == 'technology-transformation' else ''}">
                            <strong>Technology Transformation</strong>
                            <span>IT consulting &amp; digital solutions</span>
                        </a>
                        <div style="grid-column: 1 / -1; border-top: 1px solid var(--color-border); margin-top: 0.35rem; padding-top: 0.5rem; text-align: center;">
                            <a href="/services.html" style="font-weight: 700; font-size: 0.85rem; color: var(--color-primary); display: inline-flex; align-items: center; gap: 0.35rem;">View All Solutions &amp; Services →</a>
                        </div>
                    </div>
                </div>
                <div class="nav-item has-dropdown">
                    <a href="/courses.html" class="nav-link dropdown-toggle" aria-haspopup="true" aria-expanded="false">
                        Courses
                        <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"></polyline></svg>
                    </a>
                    <div class="dropdown-menu dropdown-courses">
                        <a href="/course-devops.html" class="dropdown-link">
                            <strong>DevOps</strong>
                            <span>CI/CD &amp; Cloud Automation</span>
                        </a>
                        <a href="/course-sap-basis.html" class="dropdown-link">
                            <strong>SAP Basis Security</strong>
                            <span>Administration &amp; Access</span>
                        </a>
                        <a href="/course-sap-grc.html" class="dropdown-link">
                            <strong>SAP GRC</strong>
                            <span>Governance, Risk &amp; Controls</span>
                        </a>
                        <a href="/course-data-science.html" class="dropdown-link">
                            <strong>Data Science</strong>
                            <span>Analysis, ML &amp; Python</span>
                        </a>
                        <a href="/course-python.html" class="dropdown-link">
                            <strong>Python</strong>
                            <span>Core, OOP &amp; Automation</span>
                        </a>
                        <a href="/course-software-testing.html" class="dropdown-link">
                            <strong>Software Testing</strong>
                            <span>Manual, Selenium &amp; API</span>
                        </a>
                        <a href="/course-azure-data-factory.html" class="dropdown-link">
                            <strong>Azure Data Factory</strong>
                            <span>Cloud ETL &amp; Pipelines</span>
                        </a>
                        <a href="/course-snowflake.html" class="dropdown-link">
                            <strong>Snowflake</strong>
                            <span>Cloud Data Warehousing</span>
                        </a>
                        <a href="/course-salesforce.html" class="dropdown-link">
                            <strong>Salesforce</strong>
                            <span>Admin &amp; Configuration</span>
                        </a>
                        <a href="/course-aws.html" class="dropdown-link">
                            <strong>AWS</strong>
                            <span>Infrastructure &amp; Architecture</span>
                        </a>
                        <div style="grid-column: 1 / -1; border-top: 1px solid var(--color-border); margin-top: 0.35rem; padding-top: 0.5rem; text-align: center;">
                            <a href="/courses.html" style="font-weight: 700; font-size: 0.85rem; color: var(--color-primary); display: inline-flex; align-items: center; gap: 0.35rem;">View All Courses →</a>
                        </div>
                    </div>
                </div>
                <div class="nav-item">
                    <a href="/contact.html" class="nav-link">Contact Us</a>
                </div>
            </nav>

            <div class="nav-cta">
                <a href="/contact.html" class="btn btn-primary">Let's Talk →</a>
            </div>

            <!-- Hamburger Button for Mobile -->
            <button class="hamburger" aria-label="Toggle Navigation" aria-expanded="false">
                <span></span>
                <span></span>
                <span></span>
            </button>
        </div>
    </header>

    <!-- Mobile Navigation Drawer -->
    <div class="mobile-nav-overlay"></div>
    <div class="mobile-nav-drawer">
        <div class="mobile-menu-items">
            <div class="mobile-menu-item">
                <a href="/" class="mobile-menu-link">Home</a>
            </div>
            <div class="mobile-menu-item">
                <a href="/about.html" class="mobile-menu-link">About Us</a>
            </div>
            <div class="mobile-menu-item">
                <a href="/services.html" class="mobile-menu-link mobile-dropdown-toggle" aria-expanded="false">
                    HR Consulting
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"></polyline></svg>
                </a>
                <div class="mobile-submenu">
                    <a href="/services/hr-consulting/talent-acquisition" class="mobile-submenu-link {'active' if active_page == 'talent-acquisition' else ''}">Talent Acquisition</a>
                    <a href="/services/hr-consulting/recruitment-process-outsourcing" class="mobile-submenu-link {'active' if active_page == 'rpo' else ''}">Recruitment Process Outsourcing (RPO)</a>
                    <a href="/services/hr-consulting/executive-search-hiring" class="mobile-submenu-link {'active' if active_page == 'executive-search' else ''}">Executive Search &amp; Hiring</a>
                    <a href="/services/hr-consulting/dei-hiring" class="mobile-submenu-link {'active' if active_page == 'dei-hiring' else ''}">DE&amp;I Hiring</a>
                    <a href="/services/hr-consulting/talent-intelligence" class="mobile-submenu-link {'active' if active_page == 'talent-intelligence' else ''}">Talent Intelligence &amp; Workforce Planning</a>
                    <a href="/services/technology-transformation" class="mobile-submenu-link {'active' if active_page == 'technology-transformation' else ''}">Technology Transformation</a>
                    <a href="/services.html" class="mobile-submenu-link" style="font-weight: 700; color: var(--color-primary);">All Solutions Overview &rarr;</a>
                </div>
            </div>
            <div class="mobile-menu-item">
                <a href="/courses.html" class="mobile-menu-link mobile-dropdown-toggle" aria-expanded="false">
                    Courses
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"></polyline></svg>
                </a>
                <div class="mobile-submenu">
                    <a href="/course-devops.html" class="mobile-submenu-link">DevOps</a>
                    <a href="/course-sap-basis.html" class="mobile-submenu-link">SAP Basis Security</a>
                    <a href="/course-sap-grc.html" class="mobile-submenu-link">SAP GRC</a>
                    <a href="/course-data-science.html" class="mobile-submenu-link">Data Science</a>
                    <a href="/course-python.html" class="mobile-submenu-link">Python</a>
                    <a href="/course-software-testing.html" class="mobile-submenu-link">Software Testing</a>
                    <a href="/course-azure-data-factory.html" class="mobile-submenu-link">Azure Data Factory</a>
                    <a href="/course-snowflake.html" class="mobile-submenu-link">Snowflake</a>
                    <a href="/course-salesforce.html" class="mobile-submenu-link">Salesforce</a>
                    <a href="/course-aws.html" class="mobile-submenu-link">AWS</a>
                    <a href="/courses.html" class="mobile-submenu-link" style="font-weight: 700; color: var(--color-primary);">View All Courses &rarr;</a>
                </div>
            </div>
            <div class="mobile-menu-item">
                <a href="/contact.html" class="mobile-menu-link">Contact Us</a>
            </div>
        </div>
        <div class="mobile-cta">
            <a href="/contact.html" class="btn btn-primary" style="width: 100%; text-align: center;">Let's Talk &rarr;</a>
        </div>
    </div>'''

def get_footer():
    return '''    <!-- FOOTER -->
    <footer class="footer" style="background-color: var(--color-primary-dark); color: var(--color-white); padding: clamp(3rem, 6vw, 5rem) 0 0;">
        <div class="container">
            <div class="footer-grid">
                <!-- Company Info -->
                <div>
                    <a href="/" style="display: inline-block; margin-bottom: 1.25rem; background: #ffffff; padding: 6px 14px; border-radius: 8px;">
                        <img src="/assets/images/varnith-website-logo.svg" alt="Varnith Global" style="height: 44px; width: auto; display: block;">
                    </a>
                    <p style="color: #a0b2b0; font-size: 0.9rem; line-height: 1.6; margin-bottom: 1.5rem;">
                        Varnith Global is a leading workforce consulting and technology solutions provider empowering enterprises with specialized talent acquisition, corporate learning, and digital transformation.
                    </p>
                </div>

                <!-- HR Solutions Links -->
                <div>
                    <h4 style="color: var(--color-white); font-size: 1.05rem; margin-bottom: 1.25rem; font-weight: 700;">HR Consulting</h4>
                    <ul style="list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 0.65rem;">
                        <li><a href="/services/hr-consulting/talent-acquisition" style="color: #a0b2b0; text-decoration: none; font-size: 0.9rem;">Talent Acquisition</a></li>
                        <li><a href="/services/hr-consulting/recruitment-process-outsourcing" style="color: #a0b2b0; text-decoration: none; font-size: 0.9rem;">Recruitment Process (RPO)</a></li>
                        <li><a href="/services/hr-consulting/executive-search-hiring" style="color: #a0b2b0; text-decoration: none; font-size: 0.9rem;">Executive Search</a></li>
                        <li><a href="/services/hr-consulting/dei-hiring" style="color: #a0b2b0; text-decoration: none; font-size: 0.9rem;">DE&amp;I Hiring</a></li>
                        <li><a href="/services/hr-consulting/talent-intelligence" style="color: #a0b2b0; text-decoration: none; font-size: 0.9rem;">Talent Intelligence</a></li>
                        <li><a href="/services.html" style="color: var(--color-accent); text-decoration: none; font-size: 0.9rem; font-weight: 600;">All Services &rarr;</a></li>
                    </ul>
                </div>

                <!-- Courses Links -->
                <div>
                    <h4 style="color: var(--color-white); font-size: 1.05rem; margin-bottom: 1.25rem; font-weight: 700;">Key Courses</h4>
                    <ul style="list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 0.65rem;">
                        <li><a href="/course-sap-basis.html" style="color: #a0b2b0; text-decoration: none; font-size: 0.9rem;">SAP Basis Security</a></li>
                        <li><a href="/course-devops.html" style="color: #a0b2b0; text-decoration: none; font-size: 0.9rem;">DevOps Cloud</a></li>
                        <li><a href="/course-data-science.html" style="color: #a0b2b0; text-decoration: none; font-size: 0.9rem;">Data Science</a></li>
                        <li><a href="/course-aws.html" style="color: #a0b2b0; text-decoration: none; font-size: 0.9rem;">AWS Architecture</a></li>
                        <li><a href="/services/technology-transformation" style="color: #a0b2b0; text-decoration: none; font-size: 0.9rem;">Technology Transformation</a></li>
                    </ul>
                </div>

                <!-- Corporate Address Card Column (Al Yamin Reference Style) -->
                <div>
                    <div class="footer-address-frame">
                        <div class="footer-card-top-accent"></div>
                        <div class="footer-address-inner">
                            <div class="footer-card-logo-box">
                                <img src="/assets/images/varnith-website-logo.svg" alt="Varnith Technologies Private Limited" class="footer-card-logo">
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
                    </div>
                </div>
            </div>

            <!-- Bottom Legal Bar -->
            <div style="padding: 1.5rem 0; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 1rem; font-size: 0.85rem; color: #a0b2b0;">
                <div>&copy; 2026 Varnith Global. All rights reserved.</div>
                <div style="display: flex; gap: 1.5rem;">
                    <a href="/privacy-policy.html" style="color: #a0b2b0; text-decoration: none;">Privacy Policy</a>
                    <a href="/terms.html" style="color: #a0b2b0; text-decoration: none;">Terms of Service</a>
                </div>
            </div>
        </div>
    </footer>

    <!-- Floating WhatsApp Contact Button -->
    <a href="https://wa.me/919391816116?text=Hello%20Varnith%20Global%2C%20I%20would%20like%20to%20know%20more%20about%20your%20services." 
       class="whatsapp-floating-btn" 
       target="_blank" 
       rel="noopener noreferrer" 
       aria-label="Chat with us on WhatsApp">
        <svg viewBox="0 0 24 24" fill="currentColor">
            <path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 0 1-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 0 1-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 0 1 2.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0 0 12.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 0 0 5.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 0 0-3.48-8.413Z"/>
        </svg>
        <span class="whatsapp-tooltip">Chat with us on WhatsApp</span>
    </a>

    <!-- Core Scripts -->
    <script src="/js/site-config.js"></script>
    <script src="/js/navigation.js"></script>
    <script src="/js/animations.js"></script>
    <script src="/js/main.js"></script>'''
print('Template components ready.')
