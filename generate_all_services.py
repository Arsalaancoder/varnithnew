import os
import sys
from generate_service_base import create_page

# Common SVG icons
ICONS = {
    "search": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>',
    "users": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M23 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path></svg>',
    "briefcase": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="7" width="20" height="14" rx="2" ry="2"></rect><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"></path></svg>',
    "check_circle": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg>',
    "calendar": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line></svg>',
    "award": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="8" r="7"></circle><polyline points="8.21 13.89 7 23 12 20 17 23 15.79 13.88"></polyline></svg>',
    "cpu": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="4" width="16" height="16" rx="2" ry="2"></rect><rect x="9" y="9" width="6" height="6"></rect><line x1="9" y1="1" x2="9" y2="4"></line><line x1="15" y1="1" x2="15" y2="4"></line><line x1="9" y1="20" x2="9" y2="23"></line><line x1="15" y1="20" x2="15" y2="23"></line><line x1="20" y1="9" x2="23" y2="9"></line><line x1="20" y1="14" x2="23" y2="14"></line><line x1="1" y1="9" x2="4" y2="9"></line><line x1="1" y1="14" x2="4" y2="14"></line></svg>',
    "trending_up": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="23 6 13.5 15.5 8.5 10.5 1 18"></polyline><polyline points="17 6 23 6 23 12"></polyline></svg>',
    "shield": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg>',
    "target": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><circle cx="12" cy="12" r="6"></circle><circle cx="12" cy="12" r="2"></circle></svg>',
    "heart": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path></svg>',
    "bar_chart": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="20" x2="12" y2="10"></line><line x1="18" y1="20" x2="18" y2="4"></line><line x1="6" y1="20" x2="6" y2="16"></line></svg>',
    "layers": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="12 2 2 7 12 12 22 7 12 2"></polygon><polyline points="2 17 12 22 22 17"></polyline><polyline points="2 12 12 17 22 12"></polyline></svg>',
    "globe": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><line x1="2" y1="12" x2="22" y2="12"></line><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path></svg>',
    "cloud": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 10h-1.26A8 8 0 1 0 9 20h9a5 5 0 0 0 0-10z"></path></svg>',
    "git_branch": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="6" y1="3" x2="6" y2="15"></line><circle cx="18" cy="6" r="3"></circle><circle cx="6" cy="18" r="3"></circle><path d="M18 9a9 9 0 0 1-9 9"></path></svg>',
    "user_check": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="8.5" cy="7" r="4"></circle><polyline points="17 11 19 13 23 9"></polyline></svg>'
}

def build_all_pages():
    print("Beginning generation of all 6 individual service pages...")

    # =========================================================================
    # 1. TALENT ACQUISITION
    # =========================================================================
    create_page(
        title="Talent Acquisition",
        meta_desc="Strategic Talent Acquisition services by Varnith Global. Identifying, attracting and acquiring skilled technical and non-technical professionals aligned with organizational goals.",
        hero_tag="HR CONSULTING & RECRUITMENT",
        hero_title="Finding the Right Talent to Build a Stronger Future",
        hero_desc="We help organizations identify, attract and acquire skilled professionals who align with their business requirements, organizational culture and long-term objectives.",
        hero_bg="/assets/images/talent.jpg",
        breadcrumbs=[("Home", "/"), ("HR Consulting", "/services.html"), ("Talent Acquisition", None)],
        overview_label="WHAT IS TALENT ACQUISITION?",
        overview_title="Strategic Talent Acquisition Engineered for Modern Enterprises",
        overview_p1="Talent Acquisition is far more than filling vacant job openings. It is a strategic discipline focused on forecasting future organizational requirements, understanding talent market dynamics, and cultivating continuous pipelines of top-tier talent. At Varnith Global, we align our recruitment capabilities directly with your business milestones, engineering high-impact talent acquisition strategies that support sustainable competitive advantage.",
        overview_p2="Whether addressing rapid headcount growth, critical technical niche skill sets, or corporate business operations, our talent acquisition specialists apply structured sourcing methodologies, deep talent market intelligence, and comprehensive competency-based assessments to deliver candidates who not only fulfill role criteria but thrive within your corporate culture.",
        overview_badges=["Niche Tech Sourcing", "Corporate Staffing", "Culture-Fit Vetting", "Global Talent Pipelines"],
        overview_card_title="Strategic Capabilities at a Glance",
        overview_card_bullets=[
            "Rigorous multi-channel candidate sourcing across active & passive networks",
            "Comprehensive technical screening and competency evaluation frameworks",
            "Full interview lifecycle coordination and candidate experience management",
            "Offer management, compensation benchmarking, and onboarding advisory",
            "Data-informed recruitment metrics tracking time-to-hire and retention rate"
        ],
        metrics=[
            ("Time-to-Hire Reduction", "35% Average"),
            ("Offer Acceptance Rate", "92%"),
            ("Candidate Retention", "95% at 1 Year"),
            ("Talent Pipeline", "50,000+ Pre-Vetted")
        ],
        capabilities_title="Comprehensive Talent Acquisition Solutions",
        capabilities_desc="From detailed requirement analysis to final onboarding, our end-to-end recruitment capabilities ensure seamless candidate identification and selection.",
        capabilities=[
            ("Understanding Client Requirements", 
             "We partner with internal hiring managers and HR stakeholders to conduct thorough requirement discovery. This includes job description calibration, skills matrix definition, cultural alignment criteria, and organizational outcome expectations.",
             ICONS["target"]),
            ("Candidate Sourcing & Identification", 
             "Leveraging proprietary talent databases, executive networks, social platforms, and specialized talent communities, we identify high-caliber active and passive candidates that conventional job boards fail to reach.",
             ICONS["search"]),
            ("Technical & Non-Technical Recruitment", 
             "Specialized recruitment tracks tailored to both complex engineering, cloud, software, and data domains, as well as essential corporate functions including finance, human resources, sales, marketing, and operations.",
             ICONS["cpu"]),
            ("Candidate Screening & Evaluation", 
             "Structured competency-based behavioral interviewing, technical skill verifications, reference background checks, and psychometric assessments to ensure accurate qualification matching prior to client submission.",
             ICONS["check_circle"]),
            ("Interview Coordination & Scheduling", 
             "Full-cycle administrative and logistical management of interview schedules across multiple time zones, facilitating smooth communication between candidates and internal hiring panels with zero friction.",
             ICONS["calendar"]),
            ("Recruitment & Selection Support", 
             "Guidance through decision calibration, offer structuring, market salary benchmarking, candidate counter-offer mitigation, and active engagement through day one of employment to maximize acceptance.",
             ICONS["award"])
        ],
        methodology_title="Our Talent Acquisition Approach",
        methodology_desc="A disciplined, four-stage recruitment methodology ensuring transparency, speed, and exceptional candidate quality.",
        methodology_steps=[
            ("01", "Discover & Define", "Deep-dive workshops to audit job specs, team dynamics, compensation bands, and exact technical/soft skill benchmarks.", ICONS["target"]),
            ("02", "Source & Engage", "Targeted multi-tier candidate mapping, personalized outreach, and proactive engagement of passive top performers.", ICONS["users"]),
            ("03", "Screen & Calibrate", "Multi-point technical assessments, cultural-fit evaluations, and structured feedback loops with hiring managers.", ICONS["check_circle"]),
            ("04", "Select & Onboard", "Offer negotiation assistance, smooth transition support, and post-placement check-ins ensuring long-term retention.", ICONS["award"])
        ],
        benefits_title="Benefits for Organizations",
        benefits_desc="Partnering with Varnith Global empowers your leadership and HR teams with measurable recruitment impact.",
        benefits=[
            ("Accelerated Time-to-Fill", "Minimize operational disruption and lost productivity by reducing your average hiring cycle time by up to 35% through pre-screened talent pools.", "35% Faster"),
            ("Superior Quality of Hire", "Multi-stage competency assessments and culture mapping result in high-impact performers who integrate rapidly and deliver measurable results.", "92% Fit Rate"),
            ("Optimized Cost-Per-Hire", "Lower recruitment overhead, reduce reliance on fragmented agencies, and eliminate expensive mishires through rigorous vetting.", "40% Cost Savings"),
            ("Enhanced Employer Brand", "Deliver an exemplary, respectful, and prompt candidate experience that elevates your reputation across candidate communities.", "98% Positive Rating")
        ],
        why_title="Why Choose Varnith Global for Talent Acquisition?",
        why_desc="We combine deep industry expertise, cutting-edge recruitment technology, and dedicated client commitment.",
        why_points=[
            ("Domain-Specialized Recruiters", "Our talent consultants specialize in designated verticals, bringing deep technical insight and market knowledge to every search engagement."),
            ("Rigorous Multi-Tier Screening", "Every candidate profile submitted to your hiring team has undergone rigorous resume verification, technical evaluation, and cultural calibration."),
            ("Transparent SLA-Driven Delivery", "We work against clear service level agreements, providing real-time pipeline visibility, weekly recruitment dashboards, and continuous communication."),
            ("Extensive Pre-Vetted Network", "Access a proprietary database of thoroughly evaluated professionals ready for rapid deployment into critical enterprise roles.")
        ],
        related_services=[
            ("Recruitment Process Outsourcing (RPO)", "/services/hr-consulting/recruitment-process-outsourcing", "Scale recruitment operations with dedicated turnkey talent teams and enterprise process management."),
            ("Executive Search & Hiring", "/services/hr-consulting/executive-search-hiring", "Confidential search and placement for executive, VP, and C-suite leadership roles."),
            ("Talent Intelligence", "/services/hr-consulting/talent-intelligence", "Harness workforce insights, market salary data, and competitor talent mapping for smarter planning.")
        ],
        active_page="talent-acquisition",
        target_files=[
            "services/hr-consulting/talent-acquisition/index.html",
            "services/hr-consulting/talent-acquisition.html",
            "talent-acquisition.html"
        ],
        capabilities_custom_html="""
            <!-- End-to-End Recruitment Process Board (Matching Design Reference) -->
            <div class="recruitment-process-board reveal reveal-up">
                <div class="process-board-header">
                    <div class="process-board-badge">
                        <span class="badge-sub">OUR END-TO-END</span>
                        <span class="badge-title">RECRUITMENT PROCESS</span>
                    </div>
                </div>

                <div class="process-steps-grid">
                    <!-- Step 01: Understanding Client Requirements -->
                    <div class="process-step-card step-card-blue">
                        <div class="process-card-top">
                            <div class="process-card-title-group">
                                <span class="process-card-num num-blue">01</span>
                                <h4 class="process-card-title">Understanding<br>Client Requirements</h4>
                            </div>
                            <div class="process-card-icon-box icon-box-blue">
                                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                    <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
                                    <polyline points="14 2 14 8 20 8"></polyline>
                                    <line x1="16" y1="13" x2="8" y2="13"></line>
                                    <line x1="16" y1="17" x2="8" y2="17"></line>
                                    <polyline points="10 9 9 9 8 9"></polyline>
                                </svg>
                            </div>
                        </div>
                        <p class="process-card-desc">
                            We partner with internal hiring managers and HR stakeholders to conduct thorough requirement discovery. This includes job description calibration, skills matrix definition, cultural alignment criteria, and organizational outcome expectations.
                        </p>
                    </div>

                    <!-- Step 02: Candidate Sourcing & Identification -->
                    <div class="process-step-card step-card-green">
                        <div class="process-card-top">
                            <div class="process-card-title-group">
                                <span class="process-card-num num-green">02</span>
                                <h4 class="process-card-title">Candidate Sourcing<br>&amp; Identification</h4>
                            </div>
                            <div class="process-card-icon-box icon-box-green">
                                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                    <circle cx="11" cy="11" r="8"></circle>
                                    <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
                                    <path d="M11 8a3 3 0 1 0 0 6 3 3 0 0 0 0-6z"></path>
                                </svg>
                            </div>
                        </div>
                        <p class="process-card-desc">
                            Leveraging proprietary talent databases, executive networks, social platforms, and specialized talent communities, we identify high-caliber active and passive candidates that conventional job boards fail to reach.
                        </p>
                    </div>

                    <!-- Step 03: Technical & Non-Technical Recruitment -->
                    <div class="process-step-card step-card-purple">
                        <div class="process-card-top">
                            <div class="process-card-title-group">
                                <span class="process-card-num num-purple">03</span>
                                <h4 class="process-card-title">Technical &amp; Non-<br>Technical Recruitment</h4>
                            </div>
                            <div class="process-card-icon-box icon-box-purple">
                                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                    <circle cx="12" cy="12" r="3"></circle>
                                    <path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"></path>
                                </svg>
                            </div>
                        </div>
                        <p class="process-card-desc">
                            Specialized recruitment tracks tailored to both complex engineering, cloud, software, and data domains, as well as essential corporate functions including finance, human resources, sales, marketing, and operations.
                        </p>
                    </div>

                    <!-- Step 04: Candidate Screening & Evaluation -->
                    <div class="process-step-card step-card-orange">
                        <div class="process-card-top">
                            <div class="process-card-title-group">
                                <span class="process-card-num num-orange">04</span>
                                <h4 class="process-card-title">Candidate Screening<br>&amp; Evaluation</h4>
                            </div>
                            <div class="process-card-icon-box icon-box-orange">
                                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                    <path d="M16 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path>
                                    <circle cx="8.5" cy="7" r="4"></circle>
                                    <polyline points="17 11 19 13 23 9"></polyline>
                                </svg>
                            </div>
                        </div>
                        <p class="process-card-desc">
                            Structured competency-based behavioral interviewing, technical skill verifications, reference background checks, and psychometric assessments to ensure accurate qualification matching prior to client submission.
                        </p>
                    </div>

                    <!-- Step 05: Interview Coordination & Scheduling -->
                    <div class="process-step-card step-card-red">
                        <div class="process-card-top">
                            <div class="process-card-title-group">
                                <span class="process-card-num num-red">05</span>
                                <h4 class="process-card-title">Interview Coordination<br>&amp; Scheduling</h4>
                            </div>
                            <div class="process-card-icon-box icon-box-red">
                                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                    <rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect>
                                    <line x1="16" y1="2" x2="16" y2="6"></line>
                                    <line x1="8" y1="2" x2="8" y2="6"></line>
                                    <line x1="3" y1="10" x2="21" y2="10"></line>
                                    <polyline points="12 14 12 17 14 17"></polyline>
                                </svg>
                            </div>
                        </div>
                        <p class="process-card-desc">
                            Full-cycle administrative and logistical management of interview schedules across multiple time zones, facilitating smooth communication between candidates and internal hiring panels with zero friction.
                        </p>
                    </div>

                    <!-- Step 06: Recruitment & Selection Support -->
                    <div class="process-step-card step-card-teal">
                        <div class="process-card-top">
                            <div class="process-card-title-group">
                                <span class="process-card-num num-teal">06</span>
                                <h4 class="process-card-title">Recruitment &amp;<br>Selection Support</h4>
                            </div>
                            <div class="process-card-icon-box icon-box-teal">
                                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                    <path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path>
                                </svg>
                            </div>
                        </div>
                        <p class="process-card-desc">
                            Guidance through decision calibration, offer structuring, market salary benchmarking, candidate counter-offer mitigation, and active engagement through day one of employment to maximize acceptance.
                        </p>
                    </div>
                </div>

                <div class="process-board-footer">
                    EXPERTISE &nbsp;|&nbsp; EFFICIENCY &nbsp;|&nbsp; SUCCESS
                </div>
            </div>
        """
    )

    # =========================================================================
    # 2. RECRUITMENT PROCESS OUTSOURCING (RPO)
    # =========================================================================
    create_page(
        title="Recruitment Process Outsourcing (RPO)",
        meta_desc="Scalable RPO solutions by Varnith Global. Streamline recruitment operations, improve hiring efficiency, and scale your workforce on demand.",
        hero_tag="ENTERPRISE WORKFORCE SOLUTIONS",
        hero_title="Smarter Recruitment. Scalable Hiring. Better Results.",
        hero_desc="Streamline your recruitment operations with scalable hiring solutions designed to improve recruitment efficiency, simplify talent acquisition and support your organization's evolving workforce requirements.",
        hero_bg="/assets/images/hr-tech-hero.jpg",
        breadcrumbs=[("Home", "/"), ("HR Consulting", "/services.html"), ("RPO Solutions", None)],
        overview_label="WHAT IS RECRUITMENT PROCESS OUTSOURCING?",
        overview_title="Turnkey Recruitment Operations Built for Elastic Enterprise Growth",
        overview_p1="Recruitment Process Outsourcing (RPO) is a strategic business partnership where an organization entrusts all or part of its recruitment operations to an external workforce specialist. Unlike traditional staffing agencies that operate on transactional vacancy placement, an RPO partner integrates directly into your business structure, managing the people, technology, processes, and metrics across the entire talent lifecycle.",
        overview_p2="Varnith Global provides agile, scalable RPO solutions that adapt seamlessly to volatile market demands, seasonal expansions, new market entries, or organizational transformations. We act as an authentic extension of your internal human resources team, embedding proven recruitment workflows, leading HR tech stacks, and dedicated talent advisory consultants.",
        overview_badges=["End-to-End RPO", "Project-Based RPO", "Selective Function RPO", "Embedded Talent Teams"],
        overview_card_title="RPO Operational Scope",
        overview_card_bullets=[
            "Full recruitment lifecycle ownership from job definition through onboarding",
            "Deployment of dedicated on-site or remote recruitment delivery teams",
            "Standardized ATS workflows, automated candidate scoring, and reporting",
            "Talent branding, candidate experience optimization, and DE&I compliance",
            "Predictable operational cost models and transparent SLA delivery"
        ],
        metrics=[
            ("Hiring Scalability", "100% Elastic"),
            ("Cost-Per-Hire Reduction", "30-50%"),
            ("Candidate Experience", "96% Positive"),
            ("Compliance Adherence", "100% Audit-Ready")
        ],
        capabilities_title="End-to-End Recruitment Solutions",
        capabilities_desc="We engineer, execute, and optimize every phase of your recruitment architecture to deliver measurable hiring performance.",
        capabilities=[
            ("Recruitment Planning & Strategy", 
             "Developing proactive workforce demand forecasting, capacity planning models, talent segmentation matrices, and recruitment timelines aligned with corporate fiscal objectives.",
             ICONS["layers"]),
            ("Candidate Sourcing Engines", 
             "Building dedicated talent pipeline funnels utilizing artificial intelligence sourcing tools, global talent databases, referral programs, and targeted omnichannel employer branding campaigns.",
             ICONS["search"]),
            ("Screening & Shortlisting Frameworks", 
             "Applying rigorous multi-stage candidate qualification protocols including structured situational interviews, verified skill assessments, and strict compliance validation.",
             ICONS["check_circle"]),
            ("Interview Coordination & Logistics", 
             "Managing seamless candidate communication, interview panel logistics, automated calendar scheduling, and candidate prep briefings to maximize interview completion rates.",
             ICONS["calendar"]),
            ("Recruitment Process Management", 
             "End-to-end administration of candidate records in your applicant tracking system (ATS), workflow governance, hiring manager feedback coordination, and vendor management.",
             ICONS["briefcase"]),
            ("Scalable Hiring Solutions", 
             "Elastic resource allocation allowing organizations to rapidly scale hiring teams up or down based on fluctuating seasonal demands or urgent project ramp-ups without permanent overhead.",
             ICONS["trending_up"])
        ],
        methodology_title="Our RPO Implementation Methodology",
        methodology_desc="A proven, phased operational deployment that ensures smooth transition, zero business disruption, and rapid time-to-value.",
        methodology_steps=[
            ("01", "Audit & Design", "Analyzing historical recruitment data, auditing existing hiring workflows, defining custom SLA benchmarks, and architecting the optimal delivery model.", ICONS["target"]),
            ("02", "Deploy & Integrate", "Assembling dedicated recruitment teams, integrating with your tech stack, aligning brand messaging, and establishing governance councils.", ICONS["layers"]),
            ("03", "Execute & Manage", "Executing active sourcing, candidate management, interview workflows, and stakeholder communication against strict performance SLAs.", ICONS["cpu"]),
            ("04", "Analyze & Optimize", "Continuous process refinement using weekly performance analytics, hiring manager satisfaction reviews, and proactive cost optimization.", ICONS["bar_chart"])
        ],
        benefits_title="Benefits of RPO for Organizations",
        benefits_desc="Transforming talent acquisition from an administrative bottleneck into an enterprise competitive advantage.",
        benefits=[
            ("Substantial Cost Savings", "Consolidate agency spend, eliminate duplicate tool subscriptions, and reduce internal administrative burden with predictable, optimized hiring economics.", "Up to 50% Lower"),
            ("Rapidly Scalable Operations", "Instantly adapt to surges in hiring demand or strategic freezes without the pain of recruiting or laying off internal talent acquisition staff.", "Zero Overhead"),
            ("Accelerated Cycle Times", "Streamlined candidate engagement funnels and dedicated sourcing recruiters cut vacancy durations and eliminate hiring pipeline bottlenecks.", "40% Faster Cycles"),
            ("World-Class Candidate Experience", "Consistent, transparent, and empathetic communication across all touchpoints reinforces positive perception of your corporate brand.", "96% CSAT Score")
        ],
        why_title="Why Choose Varnith Global for RPO?",
        why_desc="A trusted workforce partner combining enterprise scalability with personalized, high-touch execution.",
        why_points=[
            ("Flexible Engagement Models", "Choose between enterprise full-lifecycle RPO, project-based burst recruitment, or selective functional outsourcing tailored to your immediate needs."),
            ("Embedded Partnership Approach", "Our recruiters integrate directly into your corporate culture, adopting your brand voice, email domains, and values to represent you seamlessly in the market."),
            ("Cutting-Edge HR Tech Integration", "We leverage modern ATS platforms, AI-driven candidate mapping, and predictive recruitment analytics without requiring additional software investment."),
            ("Strict Compliance & Governance", "Ensuring complete adherence to local labor laws, employment standards, data privacy regulations, and audit-ready documentation across every hire.")
        ],
        related_services=[
            ("Talent Acquisition", "/services/hr-consulting/talent-acquisition", "Specialized permanent hiring and niche candidate search for critical enterprise vacancies."),
            ("DE&I Hiring", "/services/hr-consulting/dei-hiring", "Embed diversity, equity, and inclusion principles into your foundational recruitment workflows."),
            ("Talent Intelligence", "/services/hr-consulting/talent-intelligence", "Gain competitive intelligence on talent pools, compensation benchmarks, and geographic availability.")
        ],
        active_page="rpo",
        target_files=[
            "services/hr-consulting/recruitment-process-outsourcing/index.html",
            "services/hr-consulting/recruitment-process-outsourcing.html",
            "rpo.html"
        ],
        capabilities_custom_html="""
            <!-- End-to-End Recruitment Process Board (Matching Design Reference) -->
            <div class="recruitment-process-board reveal reveal-up">
                <div class="process-board-header">
                    <div class="process-board-badge">
                        <span class="badge-sub">OUR END-TO-END</span>
                        <span class="badge-title">RECRUITMENT PROCESS</span>
                    </div>
                </div>

                <div class="process-steps-grid">
                    <!-- Step 01: Recruitment Planning & Strategy -->
                    <div class="process-step-card step-card-blue">
                        <div class="process-card-top">
                            <div class="process-card-title-group">
                                <span class="process-card-num num-blue">01</span>
                                <h4 class="process-card-title">Recruitment Planning<br>&amp; Strategy</h4>
                            </div>
                            <div class="process-card-icon-box icon-box-blue">
                                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                    <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
                                    <polyline points="14 2 14 8 20 8"></polyline>
                                    <line x1="16" y1="13" x2="8" y2="13"></line>
                                    <line x1="16" y1="17" x2="8" y2="17"></line>
                                    <polyline points="10 9 9 9 8 9"></polyline>
                                </svg>
                            </div>
                        </div>
                        <p class="process-card-desc">
                            We partner with internal hiring managers and HR stakeholders to conduct thorough workforce demand forecasting, capacity planning models, talent segmentation matrices, and recruitment timelines aligned with corporate fiscal objectives.
                        </p>
                    </div>

                    <!-- Step 02: Candidate Sourcing & Pipeline -->
                    <div class="process-step-card step-card-green">
                        <div class="process-card-top">
                            <div class="process-card-title-group">
                                <span class="process-card-num num-green">02</span>
                                <h4 class="process-card-title">Candidate Sourcing<br>&amp; Pipeline</h4>
                            </div>
                            <div class="process-card-icon-box icon-box-green">
                                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                    <circle cx="11" cy="11" r="8"></circle>
                                    <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
                                    <path d="M11 8a3 3 0 1 0 0 6 3 3 0 0 0 0-6z"></path>
                                </svg>
                            </div>
                        </div>
                        <p class="process-card-desc">
                            Deploying dedicated talent pipeline funnels utilizing artificial intelligence sourcing tools, global talent databases, referral networks, and targeted omnichannel employer branding campaigns to engage top-tier active and passive candidates.
                        </p>
                    </div>

                    <!-- Step 03: Screening & Shortlisting -->
                    <div class="process-step-card step-card-purple">
                        <div class="process-card-top">
                            <div class="process-card-title-group">
                                <span class="process-card-num num-purple">03</span>
                                <h4 class="process-card-title">Screening &amp;<br>Shortlisting</h4>
                            </div>
                            <div class="process-card-icon-box icon-box-purple">
                                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                    <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path>
                                    <polyline points="22 4 12 14.01 9 11.01"></polyline>
                                </svg>
                            </div>
                        </div>
                        <p class="process-card-desc">
                            Applying rigorous multi-stage candidate qualification protocols including structured situational interviews, verified technical skill assessments, cultural alignment reviews, and strict compliance validation before client presentation.
                        </p>
                    </div>

                    <!-- Step 04: Interview Coordination & Logistics -->
                    <div class="process-step-card step-card-orange">
                        <div class="process-card-top">
                            <div class="process-card-title-group">
                                <span class="process-card-num num-orange">04</span>
                                <h4 class="process-card-title">Interview Coordination<br>&amp; Logistics</h4>
                            </div>
                            <div class="process-card-icon-box icon-box-orange">
                                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                    <rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect>
                                    <line x1="16" y1="2" x2="16" y2="6"></line>
                                    <line x1="8" y1="2" x2="8" y2="6"></line>
                                    <line x1="3" y1="10" x2="21" y2="10"></line>
                                    <polyline points="12 14 12 17 14 17"></polyline>
                                </svg>
                            </div>
                        </div>
                        <p class="process-card-desc">
                            Full-cycle administrative and logistical management of interview schedules across multiple time zones, automated calendar scheduling, and candidate prep briefings to ensure smooth, friction-free interactions with hiring panels.
                        </p>
                    </div>

                    <!-- Step 05: Recruitment Process Management -->
                    <div class="process-step-card step-card-red">
                        <div class="process-card-top">
                            <div class="process-card-title-group">
                                <span class="process-card-num num-red">05</span>
                                <h4 class="process-card-title">Recruitment Process<br>Management</h4>
                            </div>
                            <div class="process-card-icon-box icon-box-red">
                                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                    <rect x="2" y="7" width="20" height="14" rx="2" ry="2"></rect>
                                    <path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"></path>
                                </svg>
                            </div>
                        </div>
                        <p class="process-card-desc">
                            End-to-end administration of candidate records in your applicant tracking system (ATS), workflow governance, hiring manager feedback loops, vendor management, and real-time SLA reporting.
                        </p>
                    </div>

                    <!-- Step 06: Scalable Hiring Solutions -->
                    <div class="process-step-card step-card-teal">
                        <div class="process-card-top">
                            <div class="process-card-title-group">
                                <span class="process-card-num num-teal">06</span>
                                <h4 class="process-card-title">Scalable Hiring<br>Solutions</h4>
                            </div>
                            <div class="process-card-icon-box icon-box-teal">
                                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                    <polyline points="23 6 13.5 15.5 8.5 10.5 1 18"></polyline>
                                    <polyline points="17 6 23 6 23 12"></polyline>
                                </svg>
                            </div>
                        </div>
                        <p class="process-card-desc">
                            Elastic resource allocation allowing organizations to rapidly scale hiring teams up or down based on fluctuating seasonal demands or urgent project ramp-ups with guaranteed cost efficiency and zero permanent overhead.
                        </p>
                    </div>
                </div>

                <div class="process-board-footer">
                    EXPERTISE &nbsp;|&nbsp; EFFICIENCY &nbsp;|&nbsp; SUCCESS
                </div>
            </div>
        """
    )

    # =========================================================================
    # 3. EXECUTIVE SEARCH & HIRING
    # =========================================================================
    create_page(
        title="Executive Search & Hiring",
        meta_desc="Confidential Executive Search & Leadership Hiring by Varnith Global. Connecting organizations with transformative C-suite, VP, and Board-level leaders.",
        hero_tag="LEADERSHIP & C-SUITE ACQUISITION",
        hero_title="Connecting Organizations with Exceptional Leadership Talent",
        hero_desc="We support organizations in identifying and attracting experienced leadership professionals who align with their strategic vision, organizational culture and business goals.",
        hero_bg="/assets/images/consulting-process.jpg",
        breadcrumbs=[("Home", "/"), ("HR Consulting", "/services.html"), ("Executive Search", None)],
        overview_label="EXECUTIVE SEARCH OVERVIEW",
        overview_title="Transformative Leadership Search Conducted with Discretion and Rigor",
        overview_p1="Exceptional leadership is the definitive catalyst for organizational longevity, strategic innovation, and enterprise valuation. Identifying and securing high-caliber executives requires a level of discretion, market access, and strategic advisory far beyond conventional recruitment. At Varnith Global, our Executive Search practice operates as trusted counsel to Boards of Directors, CEOs, and corporate leadership teams.",
        overview_p2="We engage with seasoned leaders who are actively shaping industries and driving transformative results. By combining thorough market research, deep industry relationships, and comprehensive leadership competency evaluations, we identify visionaries equipped to navigate disruption, foster high-performing cultures, and deliver sustained enterprise value.",
        overview_badges=["C-Suite Placements", "VP & Managing Directors", "Board Appointments", "Discreet Headhunting"],
        overview_card_title="Executive Search Highlights",
        overview_card_bullets=[
            "100% confidential search protocols safeguarding corporate brand integrity",
            "Direct partner-led engagement across every phase of the executive search",
            "Deep leadership assessment covering strategic vision and cultural fit",
            "Comprehensive executive compensation benchmarking and offer advisory",
            "Dedicated 12-month post-placement leadership onboarding support"
        ],
        metrics=[
            ("Search Success Rate", "98% Completed"),
            ("Confidentiality Index", "100% Protected"),
            ("Leadership Tenure", "4.2 Years Avg"),
            ("Candidate Diversity", "45% Diverse Slate")
        ],
        capabilities_title="Comprehensive Leadership Search Capabilities",
        capabilities_desc="Our bespoke executive search methodologies ensure access to elite leadership talent across sectors and functional disciplines.",
        capabilities=[
            ("Leadership Recruitment", 
             "Targeted identification and headhunting of proven organizational leaders capable of driving operational excellence, managing cross-functional teams, and executing core business mandates.",
             ICONS["users"]),
            ("C-Suite Hiring (CEO, CTO, CFO, CHRO)", 
             "Bespoke, confidential search engagements for board-level and C-suite positions requiring strategic vision, fiduciary governance, and transformational leadership capabilities.",
             ICONS["award"]),
            ("Senior Management Recruitment", 
             "Identifying high-impact Vice Presidents, Senior Directors, and General Managers capable of bridging boardroom strategy with tactical, day-to-day execution.",
             ICONS["briefcase"]),
            ("Leadership Talent Identification", 
             "Comprehensive talent mapping that uncovers hidden, non-applicant executive talent across direct competitors, complementary industries, and global enterprise ecosystems.",
             ICONS["search"]),
            ("Candidate Evaluation & Psychometrics", 
             "Multi-dimensional executive assessments evaluating strategic decision-making, crisis management capabilities, emotional intelligence, and leadership agility.",
             ICONS["check_circle"]),
            ("Organizational & Cultural Alignment", 
             "Rigorous cultural compatibility assessments ensuring incoming leaders resonate with corporate values, leadership philosophies, and long-term shareholder objectives.",
             ICONS["heart"])
        ],
        methodology_title="Our Executive Hiring Approach",
        methodology_desc="A methodical, confidential executive search framework built on rigorous discovery, market intelligence, and structured alignment.",
        methodology_steps=[
            ("01", "Mandate & Calibration", "In-depth consultations with Board members and leadership to define strategic priorities, core competencies, and ideal executive profiles.", ICONS["target"]),
            ("02", "Ecosystem Mapping", "Conducting exhaustive talent mapping across targeted markets, establishing confidential executive dialogues, and creating a qualified candidate pool.", ICONS["globe"]),
            ("03", "Assessment & Selection", "Conducting structured executive interviews, 360-degree reference evaluations, and presenting a calibrated executive shortlist.", ICONS["check_circle"]),
            ("04", "Offer & Integration", "Facilitating confidential contract negotiations, compensation package structuring, and executing structured 100-day executive onboarding plans.", ICONS["award"])
        ],
        benefits_title="Benefits to Organizations",
        benefits_desc="Strategic executive appointments create transformative impact across an organization's performance, stability, and growth.",
        benefits=[
            ("Visionary Strategic Direction", "Secure leaders capable of articulating strategic vision, identifying new revenue streams, and guiding organizations through market disruption.", "Catalyst for Growth"),
            ("Complete Search Discretion", "Safeguard sensitive corporate transitions, restructuring initiatives, or strategic pivots through confidential search protocols.", "100% Confidential"),
            ("De-risked Executive Appointments", "Multi-point competency and background evaluations significantly mitigate the substantial financial and operational risks of a leadership mismatch.", "98% Retention"),
            ("Accelerated Leadership Impact", "Structured transition planning ensures newly appointed executives integrate seamlessly and begin delivering value within their first 100 days.", "Rapid Impact")
        ],
        why_title="Why Choose Varnith Global for Executive Search?",
        why_desc="Trusted by enterprise boards and founders to solve their most critical leadership challenges.",
        why_points=[
            ("Partner-Led Engagements", "Every executive search assignment is directly managed and executed by senior partners with extensive industry and leadership advisory expertise."),
            ("Proprietary Leadership Network", "Direct access to high-impact leaders, executives, and innovators who do not participate in public job markets or transactional recruitment."),
            ("Holistic Fit Assessment", "We evaluate candidates not merely on past accomplishments, but on future adaptability, emotional resilience, and cultural integration."),
            ("Extended Placement Guarantees", "Our executive search mandates are backed by robust replacement guarantees and structured check-in schedules during the leader's critical first year.")
        ],
        related_services=[
            ("Talent Acquisition", "/services/hr-consulting/talent-acquisition", "Build out high-performing functional teams beneath newly appointed executive leaders."),
            ("DE&I Hiring", "/services/hr-consulting/dei-hiring", "Ensure diverse representation and inclusive hiring practices across leadership and board levels."),
            ("Talent Intelligence", "/services/hr-consulting/talent-intelligence", "Analyze competitor organizational structures and executive compensation benchmarks.")
        ],
        active_page="executive-search",
        target_files=[
            "services/hr-consulting/executive-search-hiring/index.html",
            "services/hr-consulting/executive-search-hiring.html",
            "executive-hiring.html"
        ]
    )

    # =========================================================================
    # 4. DE&I HIRING
    # =========================================================================
    create_page(
        title="DE&I Hiring (Diversity, Equity & Inclusion)",
        meta_desc="Strategic DE&I Recruitment Solutions by Varnith Global. Building diverse talent pipelines, inclusive hiring practices, and equitable organizational cultures.",
        hero_tag="DIVERSITY, EQUITY & INCLUSION",
        hero_title="Building Diverse Teams. Creating Inclusive Workplaces.",
        hero_desc="We support organizations in developing inclusive recruitment approaches that encourage diverse talent participation, equitable opportunities and stronger workplace cultures.",
        hero_bg="/assets/images/about-team.jpg",
        breadcrumbs=[("Home", "/"), ("HR Consulting", "/services.html"), ("DE&I Hiring", None)],
        overview_label="UNDERSTANDING DIVERSITY, EQUITY & INCLUSION",
        overview_title="Fostering Workplace Equity as a Sustainable Strategic Advantage",
        overview_p1="Diversity, Equity, and Inclusion (DE&I) is no longer a corporate checkbox or public relations initiative—it is a proven driver of enterprise innovation, employee engagement, and business performance. Research consistently demonstrates that organizations with diverse leadership and inclusive teams outperform homogeneous competitors across profitability, creativity, and talent retention.",
        overview_p2="Varnith Global partners with forward-thinking enterprises to audit, redesign, and execute inclusive talent acquisition strategies. We help organizations dismantle unconscious bias in recruitment, expand talent funnels into historically underrepresented talent communities, and establish objective, skills-first evaluation frameworks that cultivate authentic workplace diversity.",
        overview_badges=["Inclusive Sourcing", "Unconscious Bias Mitigation", "Equitable Assessment", "Diverse Slates"],
        overview_card_title="DE&I Strategic Focus Areas",
        overview_card_bullets=[
            "Gender balance, ethnic representation, and neurodiverse talent sourcing",
            "Inclusive job description re-engineering and gender-neutral language calibration",
            "Blind resume screening protocols and structured competency evaluation",
            "Diverse interview panel assembly and bias-mitigation training frameworks",
            "Comprehensive DE&I hiring analytics, funnel tracking, and retention metrics"
        ],
        metrics=[
            ("Diverse Candidate Slate", "Min 50% Mandate"),
            ("Unconscious Bias Reduction", "85% Measurable"),
            ("Retention of Diverse Hires", "94% at 18 Months"),
            ("Community Partnerships", "40+ DE&I Networks")
        ],
        capabilities_title="Comprehensive DE&I Recruitment Capabilities",
        capabilities_desc="We embed equitable principles across every phase of your talent acquisition lifecycle to build balanced, high-performing teams.",
        capabilities=[
            ("Inclusive Recruitment Strategies", 
             "Designing end-to-end diversity hiring blueprints that align organizational DE&I goals with practical talent acquisition processes and measurable milestones.",
             ICONS["layers"]),
            ("Diverse Talent Identification", 
             "Proactively tapping into specialized diversity networks, professional affinity associations, women-in-tech communities, and minority professional organizations.",
             ICONS["users"]),
            ("Equitable Hiring Practices", 
             "Auditing screening criteria, eliminating pedigree bias, standardizing interview scorecards, and institutionalizing structured rubric-based evaluations.",
             ICONS["shield"]),
            ("Inclusive Candidate Experiences", 
             "Creating welcoming, accessible, and transparent interview experiences that signal psychological safety and genuine organizational commitment to inclusion.",
             ICONS["heart"]),
            ("Workplace Diversity Advisory", 
             "Providing strategic consulting to hiring managers on fostering psychological safety, mitigating unconscious bias, and facilitating smooth team onboarding.",
             ICONS["award"]),
            ("Building Inclusive Teams", 
             "Advising on balanced team composition, employee resource group (ERG) empowerment, and equitable pathways for career development and promotion.",
             ICONS["target"])
        ],
        methodology_title="Our Inclusive Recruitment Methodology",
        methodology_desc="A systematic framework designed to remove structural barriers and create equal access to high-impact career opportunities.",
        methodology_steps=[
            ("01", "Audit & Baseline", "Conducting comprehensive talent audits to identify hiring pipeline leaks, demographic drop-offs, and bias vulnerabilities in existing job postings.", ICONS["target"]),
            ("02", "Re-engineer & Calibrate", "Revamping job descriptions with inclusive language, anonymizing candidate profiles, and implementing standardized competency rubrics.", ICONS["layers"]),
            ("03", "Expand & Engage", "Deploying targeted outreach across specialized diversity channels, minority leadership forums, and affirmative talent networks.", ICONS["users"]),
            ("04", "Measure & Sustain", "Tracking recruitment funnel demographics, evaluating retention metrics, and continuously calibrating hiring manager practices.", ICONS["bar_chart"])
        ],
        benefits_title="Organizational Benefits of DE&I Hiring",
        benefits_desc="Investing in genuine diversity and inclusion creates compounding advantages across all business dimensions.",
        benefits=[
            ("Accelerated Innovation", "Teams with varied backgrounds and viewpoints solve complex problems faster and develop more creative, market-resonant solutions.", "Higher Innovation"),
            ("Expanded Talent Market", "Overcome talent scarcity by engaging underrepresented candidate communities that traditional recruitment channels consistently overlook.", "Expanded Pipeline"),
            ("Enhanced Employer Brand", "Top-tier professionals actively seek inclusive employers, significantly boosting candidate acceptance rates and overall brand esteem.", "High Acceptance"),
            ("Measurable Financial Return", "Organizations with diverse workforces consistently demonstrate superior financial performance and stronger employee engagement.", "Superior ROI")
        ],
        why_title="Why Choose Varnith Global for DE&I Hiring?",
        why_desc="Authentic commitment backed by proven methodologies and deep community relationships.",
        why_points=[
            ("Data-Driven Approach", "We move beyond superficial diversity targets to implement structured, measurable processes that eliminate systemic bias from recruitment."),
            ("Extensive Specialized Networks", "Established partnerships with diverse professional associations, university affinity groups, and specialized diversity conferences."),
            ("Objective, Skills-First Screening", "Our evaluation frameworks focus strictly on demonstrated competencies, potential, and values-alignment, eliminating pedigree and halo bias."),
            ("Comprehensive Stakeholder Enablement", "We equip hiring managers and interview panels with practical bias-awareness tools to ensure fair, objective candidate assessments.")
        ],
        related_services=[
            ("Talent Acquisition", "/services/hr-consulting/talent-acquisition", "Integrate inclusive sourcing principles across all ongoing technical and corporate hiring."),
            ("Executive Search & Hiring", "/services/hr-consulting/executive-search-hiring", "Ensure diverse representation across your executive team and corporate Board."),
            ("Talent Intelligence", "/services/hr-consulting/talent-intelligence", "Access demographic talent mapping and competitive DE&I workforce benchmarks.")
        ],
        active_page="dei-hiring",
        target_files=[
            "services/hr-consulting/dei-hiring/index.html",
            "services/hr-consulting/dei-hiring.html",
            "dei-hiring.html"
        ]
    )

    # =========================================================================
    # 5. TALENT INTELLIGENCE
    # =========================================================================
    create_page(
        title="Talent Intelligence & Workforce Insights",
        meta_desc="Strategic Talent Intelligence & Market Analytics by Varnith Global. Turn workforce data into actionable recruitment and organizational planning decisions.",
        hero_tag="MARKET ANALYTICS & INSIGHTS",
        hero_title="Turning Talent Insights into Strategic Decisions",
        hero_desc="Leverage talent intelligence and workforce insights to better understand talent markets, identify skills requirements and support informed recruitment and workforce planning decisions.",
        hero_bg="/assets/images/ai-intel.jpg",
        breadcrumbs=[("Home", "/"), ("HR Consulting", "/services.html"), ("Talent Intelligence", None)],
        overview_label="WHAT IS TALENT INTELLIGENCE?",
        overview_title="Data-Informed Workforce Strategies in an Evolving Global Talent Market",
        overview_p1="Talent Intelligence is the synthesis of external labor market data, competitor workforce analytics, internal human capital metrics, and emerging skill trends into strategic business intelligence. In today's volatile economic landscape, relying on intuition or anecdotal observations to guide workforce planning leads to costly hiring delays, compensation misalignments, and strategic vulnerabilities.",
        overview_p2="Varnith Global's Talent Intelligence practice equips executive leadership and HR strategists with actionable, empirical insights. We decode talent market dynamics—identifying skill shortages before they impact delivery, benchmarking compensation packages against actual market offers, and mapping competitor talent movements to inform proactive organizational planning.",
        overview_badges=["Competitor Talent Mapping", "Compensation Benchmarking", "Skill Supply & Demand", "Location Feasibility"],
        overview_card_title="Strategic Intelligence Deliverables",
        overview_card_bullets=[
            "Comprehensive competitor workforce sizing, structure, and talent movement mapping",
            "Real-time geographic compensation, benefits, and equity benchmarking reports",
            "Emerging technology skill supply-and-demand forecasting and scarcity alerts",
            "Location feasibility studies for enterprise global capability centers (GCCs)",
            "Predictable workforce modeling supporting mergers, acquisitions, and expansions"
        ],
        metrics=[
            ("Market Data Accuracy", "98.5% Validated"),
            ("Hiring Cost Optimization", "25-35%"),
            ("Global Markets Covered", "20+ Hubs"),
            ("Custom Intelligence Reports", "Bespoke Delivery")
        ],
        capabilities_title="Comprehensive Talent Intelligence Capabilities",
        capabilities_desc="We transform vast labor market datasets into clear, actionable roadmaps that de-risk major strategic workforce decisions.",
        capabilities=[
            ("Workforce Insights & Analytics", 
             "Deep-dive analysis into workforce demographics, tenure patterns, voluntary turnover indicators, and internal mobility bottlenecks across key enterprise functions.",
             ICONS["bar_chart"]),
            ("Talent Market Analysis", 
             "Macro and micro assessments of candidate supply, market saturation, employment mobility indices, and passive candidate sentiment across key industries.",
             ICONS["globe"]),
            ("Skills & Competency Insights", 
             "Mapping emerging versus declining technical and business competencies to identify organizational skill gaps and inform reskilling or acquisition plans.",
             ICONS["cpu"]),
            ("Strategic Workforce Planning & Development", 
             "Aligning future business capability demands with headcount models, attrition forecasts, budget constraints, workforce planning, and strategic workforce development roadmaps.",
             ICONS["layers"]),
            ("Recruitment Market Trends", 
             "Monitoring real-time shifts in remote/hybrid work models, employer value proposition (EVP) drivers, signing incentives, and competitive hiring practices.",
             ICONS["trending_up"]),
            ("Data-Informed Talent Decisions", 
             "Providing executive-ready intelligence dossiers that eliminate guesswork in salary negotiation, new hub establishment, and restructuring initiatives.",
             ICONS["target"])
        ],
        methodology_title="Our Talent Intelligence Framework",
        methodology_desc="A disciplined analytical methodology integrating big data aggregation, human curation, and strategic executive synthesis.",
        methodology_steps=[
            ("01", "Scope & Hypothesize", "Defining critical business questions, target geographic markets, benchmark peer groups, and specific role classifications.", ICONS["target"]),
            ("02", "Aggregate & Clean", "Mining structured and unstructured data from millions of public profiles, job boards, salary surveys, and proprietary enterprise datasets.", ICONS["cpu"]),
            ("03", "Analyze & Validate", "Cross-referencing algorithmic trends with qualitative insights from our active recruitment consultants and industry specialists.", ICONS["check_circle"]),
            ("04", "Synthesize & Advise", "Delivering interactive executive dashboards and comprehensive strategic reports with actionable recommendations.", ICONS["award"])
        ],
        benefits_title="Organizational Benefits of Talent Intelligence",
        benefits_desc="Empower your leadership with empirical data that turns uncertainty into decisive strategic advantage.",
        benefits=[
            ("De-risked Expansion Decisions", "Validate talent availability, cost structures, and competitive density before investing capital in new office locations or development centers.", "De-risked Growth"),
            ("Precise Compensation Structuring", "Eliminate offer rejections and wage inflation by structuring compensation packages grounded in verified real-time market data.", "Accurate Benchmarks"),
            ("Proactive Capability Building", "Identify impending skill shortages 12 to 18 months ahead, enabling proactive reskilling, training, or strategic talent acquisition.", "Predictive Planning"),
            ("Competitive Advantage", "Stay ahead of competitor restructuring, talent raids, and hiring freezes with continuous market surveillance and intelligence alerts.", "Market Edge")
        ],
        why_title="Why Choose Varnith Global for Talent Intelligence?",
        why_desc="We unite advanced data analytics with the practical real-world insight of active executive recruiters.",
        why_points=[
            ("Real-World Ground Truth", "Unlike pure software dashboards, our data is continually calibrated by real recruiters speaking with thousands of candidates weekly."),
            ("Customized Strategic Reports", "We deliver tailored, context-rich intelligence dossiers addressing your specific strategic questions, not generic off-the-shelf data."),
            ("Holistic Global Coverage", "Deep visibility into major talent corridors across North America, Europe, India, and emerging tech hubs in Southeast Asia."),
            ("Direct Executive Application", "Our deliverables are crafted for C-suite decision-makers, translating complex data into clear strategic and budgetary implications.")
        ],
        related_services=[
            ("Talent Acquisition", "/services/hr-consulting/talent-acquisition", "Operationalize market intelligence into targeted candidate sourcing campaigns."),
            ("Recruitment Process Outsourcing (RPO)", "/services/hr-consulting/recruitment-process-outsourcing", "Apply labor market analytics across your entire enterprise recruitment architecture."),
            ("Technology Transformation", "/services/technology-transformation", "Modernize your internal HR systems and analytics infrastructure through advanced IT consulting.")
        ],
        active_page="talent-intelligence",
        target_files=[
            "services/hr-consulting/talent-intelligence/index.html",
            "services/hr-consulting/talent-intelligence.html",
            "talent-intelligence.html"
        ]
    )

    # =========================================================================
    # 6. TECHNOLOGY TRANSFORMATION
    # =========================================================================
    create_page(
        title="Technology Transformation & IT Consulting",
        meta_desc="Strategic Technology Transformation & AI-led solutions by Varnith Global. Accelerate digital innovation, modernize business processes, and enhance operational efficiency.",
        hero_tag="DIGITAL & IT CONSULTING",
        hero_title="Transforming Businesses Through Intelligent Technology",
        hero_desc="We help organizations explore technology-led opportunities, modernize business operations and embrace digital innovation through strategic IT consulting and AI-led solutions.",
        hero_bg="/assets/images/technology-expertise-cards.jpeg",
        breadcrumbs=[("Home", "/"), ("Services", "/services.html"), ("Technology Transformation", None)],
        overview_label="TECHNOLOGY TRANSFORMATION OVERVIEW",
        overview_title="Empowering Enterprise Modernization with Pragmatic, AI-Led Innovation",
        overview_p1="In an era of relentless technological acceleration, enterprise success hinges on an organization's ability to seamlessly modernize core systems, automate legacy processes, and harness data-driven intelligence. Technology Transformation is not simply about adopting newer software—it is a comprehensive reimagining of how business capabilities, human talent, and intelligent architectures interact to deliver value.",
        overview_p2="Varnith Global provides strategic IT consulting and digital transformation advisory. We guide organizations through the complexities of cloud modernization, AI-assisted business workflows, automated data pipelines, and scalable enterprise architectures—ensuring that every technological investment delivers measurable operational efficiency, robust cybersecurity, and accelerated commercial growth.",
        overview_badges=["Cloud Modernization", "AI Workflow Automation", "Enterprise Architecture", "DevOps & CI/CD"],
        overview_card_title="Core Technology Domains",
        overview_card_bullets=[
            "Enterprise cloud migration, multi-cloud strategy, and microservices architecture",
            "AI-powered automation for business processes, document workflows, and analytics",
            "Custom enterprise software modernization, API integrations, and refactoring",
            "DevOps pipeline orchestration, automated testing, and security compliance",
            "IT organization restructuring, digital upskilling, and tech governance advisory"
        ],
        metrics=[
            ("Process Efficiency", "Up to 60% Faster"),
            ("Deployment Frequency", "5x Increase"),
            ("System Uptime", "99.9% Reliability"),
            ("ROI Realization", "Under 12 Months")
        ],
        capabilities_title="Comprehensive Technology Transformation Services",
        capabilities_desc="From executive technology roadmaps to hands-on systems architecture, our solutions bridge business vision and technical execution.",
        capabilities=[
            ("IT Consulting & Strategic Roadmapping", 
             "Conducting enterprise architecture audits, technology debt evaluations, and designing multi-year digital transformation blueprints aligned with commercial priorities.",
             ICONS["layers"]),
            ("Digital Transformation Advisory", 
             "Guiding organizations through cultural and operational shifts required to embrace agile delivery, continuous innovation, and digital-first business models.",
             ICONS["trending_up"]),
            ("AI-Led Solutions & Workflow Automation", 
             "Implementing pragmatic artificial intelligence, machine learning models, robotic process automation (RPA), and intelligent document processing to streamline operations.",
             ICONS["cpu"]),
            ("Business Process Modernization", 
             "Deconstructing cumbersome legacy operational workflows, eliminating friction points, and implementing automated digital processes that enhance customer experience.",
             ICONS["git_branch"]),
            ("Technology Strategy & Architecture", 
             "Designing resilient cloud-native architectures, scalable API ecosystems, and robust data foundations built for high throughput, security, and elasticity.",
             ICONS["cloud"]),
            ("Digital Innovation & Organizational Efficiency", 
             "Aligning technological modernization with workforce empowerment, providing training, change management, and governance to ensure sustained adoption.",
             ICONS["shield"])
        ],
        methodology_title="Our Technology Transformation Approach",
        methodology_desc="A structured, iterative transformation methodology engineered to deliver continuous value without operational disruption.",
        methodology_steps=[
            ("01", "Assess & Envision", "Auditing current architecture, technical debt, security posture, and workflow bottlenecks to establish clear transformation benchmarks.", ICONS["target"]),
            ("02", "Architect & Plan", "Designing target-state cloud architectures, API frameworks, AI integration plans, and a phased, low-risk execution roadmap.", ICONS["layers"]),
            ("03", "Build & Modernize", "Executing agile sprints for system migration, cloud modernization, automated CI/CD pipeline setup, and process automation.", ICONS["cpu"]),
            ("04", "Adopt & Optimize", "Driving change management, technical documentation, staff upskilling, and establishing ongoing performance monitoring frameworks.", ICONS["bar_chart"])
        ],
        benefits_title="Benefits for Modern Organizations",
        benefits_desc="Accelerate business agility, reduce technical debt, and unlock new avenues for digital growth.",
        benefits=[
            ("Substantial Efficiency Gains", "Automate repetitive manual operations and streamline core data workflows to reduce process cycle times by up to 60%.", "60% Efficiency"),
            ("Accelerated Time-to-Market", "Modern cloud architectures and automated DevOps pipelines enable rapid feature releases and prompt response to market shifts.", "5x Faster Delivery"),
            ("Elimination of Technical Debt", "Modernize fragile legacy monoliths into scalable, maintainable microservices with lower maintenance overhead.", "Reduced Risk"),
            ("Empowered, Productive Teams", "Equip your workforce with intelligent digital tools, clear process automation, and reduced administrative friction.", "Higher Output")
        ],
        why_title="Why Choose Varnith Global for Technology Transformation?",
        why_desc="A pragmatic technology advisory partner that bridges enterprise strategy, deep tech expertise, and human capital.",
        why_points=[
            ("Strategy Rooted in Business Reality", "We do not recommend technology for its own sake. Every recommendation is directly tied to measurable revenue, cost, or risk outcomes."),
            ("Integrated Talent & Tech Synergy", "As both a premier talent and technology partner, we ensure you have both the architectural blueprint and the skilled specialists to execute it."),
            ("Vendor-Agnostic Advisory", "Unbiased recommendations tailored strictly to your technical ecosystem, whether AWS, Azure, Google Cloud, SAP, or open-source stacks."),
            ("Proven Implementation Discipline", "Our senior technology consultants bring decades of enterprise delivery experience, ensuring projects launch on time, on budget, and to spec.")
        ],
        related_services=[
            ("Talent Intelligence", "/services/hr-consulting/talent-intelligence", "Map global technology talent pools and compensation to staff your digital initiatives."),
            ("Recruitment Process Outsourcing (RPO)", "/services/hr-consulting/recruitment-process-outsourcing", "Scale up specialized software, cloud, and AI engineering teams rapidly."),
            ("Talent Acquisition", "/services/hr-consulting/talent-acquisition", "Recruit permanent architects, DevOps engineers, and digital transformation leaders.")
        ],
        active_page="technology-transformation",
        target_files=[
            "services/technology-transformation/index.html",
            "services/technology-transformation.html",
            "it-services.html",
            "technology-transformation.html"
        ]
    )

    print("All 6 individual service pages generated successfully!")

if __name__ == "__main__":
    build_all_pages()
