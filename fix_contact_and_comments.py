import glob
import re

# 1. Fix contact.html
contact_form_and_footer = """                    </form>
                </div>

                <!-- Direct Contact Details & Location Map -->
                <div class="reveal reveal-right delay-1">
                    <div style="background-color: var(--color-white); border-radius: var(--radius-lg); padding: clamp(1.75rem, 3.5vw, 2.5rem); box-shadow: var(--shadow-sm); border: 1px solid var(--color-border); margin-bottom: 2rem;">
                        <h3 style="font-size: 1.35rem; font-weight: 800; color: var(--color-primary-dark); margin-bottom: 1.5rem;">Direct Contact Information</h3>
                        
                        <div style="display: flex; flex-direction: column; gap: 1.25rem;">
                            <div style="display: flex; gap: 1rem; align-items: flex-start;">
                                <div style="width: 44px; height: 44px; border-radius: 50%; background: rgba(30, 227, 61, 0.12); display: flex; align-items: center; justify-content: center; flex-shrink: 0; color: var(--color-accent-dark);">
                                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07A19.5 19.5 0 0 1 4.69 12 19.79 19.79 0 0 1 1.61 3.42C1.6 2.3 2.4 1.44 3.52 1.44h3a2 2 0 0 1 2 1.72c.127.96.361 1.903.7 2.81a2 2 0 0 1-.45 2.11L7.91 9.91a16 16 0 0 0 6.09 6.09l1.63-1.63a2 2 0 0 1 2.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>
                                </div>
                                <div>
                                    <h4 style="font-size: 0.85rem; font-weight: 700; color: var(--color-muted); text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 0.25rem;">Telephone</h4>
                                    <a href="tel:+919391816116" style="font-size: 1.05rem; font-weight: 800; color: var(--color-primary-dark); text-decoration: none;">+91 9391816116</a>
                                </div>
                            </div>

                            <div style="display: flex; gap: 1rem; align-items: flex-start;">
                                <div style="width: 44px; height: 44px; border-radius: 50%; background: rgba(30, 227, 61, 0.12); display: flex; align-items: center; justify-content: center; flex-shrink: 0; color: var(--color-accent-dark);">
                                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><polyline points="22,6 12,13 2,6"></polyline></svg>
                                </div>
                                <div>
                                    <h4 style="font-size: 0.85rem; font-weight: 700; color: var(--color-muted); text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 0.25rem;">Email Address</h4>
                                    <a href="mailto:info@varnithglobal.com" style="font-size: 1.05rem; font-weight: 800; color: var(--color-primary-dark); text-decoration: none;">info@varnithglobal.com</a>
                                </div>
                            </div>

                            <div style="display: flex; gap: 1rem; align-items: flex-start;">
                                <div style="width: 44px; height: 44px; border-radius: 50%; background: rgba(30, 227, 61, 0.12); display: flex; align-items: center; justify-content: center; flex-shrink: 0; color: var(--color-accent-dark);">
                                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg>
                                </div>
                                <div>
                                    <h4 style="font-size: 0.85rem; font-weight: 700; color: var(--color-muted); text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 0.25rem;">Registered Office</h4>
                                    <p style="font-size: 0.95rem; color: var(--color-text); line-height: 1.5; margin: 0;">4-36, 1st Floor, Vikash Nagar, Dilshuknagar,<br>Hyderabad, Telangana – 500060, India</p>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- Map Embed -->
                    <div style="border-radius: var(--radius-lg); overflow: hidden; height: 260px; box-shadow: var(--shadow-sm); border: 1px solid var(--color-border);">
                        <iframe 
                            src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3808.2045582319483!2d78.53235657493498!3d17.36592888351786!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bcb98e79e6717a5%3A0xe212c4e09559c47e!2sDilsukhnagar%2C%20Hyderabad%2C%20Telangana!5e0!3m2!1sen!2sin!4v1700000000000!5m2!1sen!2sin" 
                            width="100%" 
                            height="100%" 
                            style="border:0;" 
                            allowfullscreen="" 
                            loading="lazy" 
                            referrerpolicy="no-referrer-when-downgrade"
                            title="Varnith Global Office Location">
                        </iframe>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- FOOTER -->
    <footer style="background-color: var(--color-primary-dark); color: var(--color-white); padding: clamp(3rem, 6vw, 5rem) 0 0;">
        <div class="container">
            <div style="display: grid; grid-template-columns: 1.8fr 1fr 1fr 1.8fr; gap: 2.5rem; align-items: start; padding-bottom: 3rem; border-bottom: 1px solid rgba(255,255,255,0.1);">
                <!-- Company Info -->
                <div>
                    <a href="index.html" style="display: inline-block; margin-bottom: 1.25rem; background: #ffffff; padding: 6px 14px; border-radius: 8px;">
                        <img src="assets/images/varnith-website-logo.svg" alt="Varnith Global Logo" style="height: 40px; width: auto; display: block; object-fit: contain;">
                    </a>
                    <p style="color: #a0b2b0; font-size: 0.9rem; line-height: 1.7; margin-bottom: 1.5rem;">Varnith Global brings together HR consulting, professional development and technology solutions to help businesses and individuals move forward.</p>
                </div>

                <!-- Quick Links -->
                <div>
                    <h4 style="font-size: 0.85rem; font-weight: 800; text-transform: uppercase; letter-spacing: 0.1em; color: var(--color-white); margin-bottom: 1.25rem;">Quick Links</h4>
                    <ul style="display: flex; flex-direction: column; gap: 0.75rem;">
                        <li><a href="index.html" style="color: #a0b2b0; font-size: 0.9rem;">Home</a></li>
                        <li><a href="about.html" style="color: #a0b2b0; font-size: 0.9rem;">About Us</a></li>
                        <li><a href="services.html" style="color: #a0b2b0; font-size: 0.9rem;">Services</a></li>
                        <li><a href="courses.html" style="color: #a0b2b0; font-size: 0.9rem;">Courses</a></li>
                        <li><a href="contact.html" style="color: #a0b2b0; font-size: 0.9rem;">Contact Us</a></li>
                    </ul>
                </div>

                <!-- Services -->
                <div>
                    <h4 style="font-size: 0.85rem; font-weight: 800; text-transform: uppercase; letter-spacing: 0.1em; color: var(--color-white); margin-bottom: 1.25rem;">Our Services</h4>
                    <ul style="display: flex; flex-direction: column; gap: 0.75rem;">
                        <li><a href="services/hr-consulting/talent-acquisition" style="color: #a0b2b0; font-size: 0.9rem;">Talent Acquisition</a></li>
                        <li><a href="services/hr-consulting/recruitment-process-outsourcing" style="color: #a0b2b0; font-size: 0.9rem;">RPO Solutions</a></li>
                        <li><a href="services/hr-consulting/executive-search-hiring" style="color: #a0b2b0; font-size: 0.9rem;">Executive Search</a></li>
                        <li><a href="services/technology-transformation" style="color: #a0b2b0; font-size: 0.9rem;">Technology Solutions</a></li>
                    </ul>
                </div>

                <!-- Corporate Address Card Column -->
                <div>
                    <div class="footer-address-frame">
                        <div class="footer-card-top-accent"></div>
                        <div class="footer-address-inner">
                            <div class="footer-card-logo-box">
                                <img src="assets/images/varnith-website-logo.svg" alt="Varnith Technologies Private Limited" class="footer-card-logo">
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
                    </div>
                </div>
            </div>"""

with open("contact.html", "r", encoding="utf-8") as f:
    c = f.read()

# Replace from </form></div> to footer grid end
pattern = re.compile(r'</form>\s*</div>.*?<!-- Corporate Address Card Column.*?(?=\s*<div\s*style=[\'"][^\'"]*padding:\s*1\.5rem)', re.DOTALL)
new_c = pattern.sub(contact_form_and_footer, c)

with open("contact.html", "w", encoding="utf-8") as f:
    f.write(new_c)
print("Updated contact.html correctly!")

# 2. Clean any "Al Yamin" mentions in comments or text across all files
all_html_files = glob.glob("**/*.html", recursive=True)
cleaned = 0
for fpath in all_html_files:
    with open(fpath, "r", encoding="utf-8") as fp:
        content = fp.read()
    if "al yamin" in content.lower():
        # Replace case-insensitively in comments or text
        new_content = re.sub(r'Al Yamin Reference Style', 'Varnith Corporate Style', content, flags=re.IGNORECASE)
        new_content = re.sub(r'Al Yamin', 'Varnith', new_content, flags=re.IGNORECASE)
        with open(fpath, "w", encoding="utf-8") as fp:
            fp.write(new_content)
        cleaned += 1
        print(f"Cleaned Al Yamin reference in: {fpath}")

print(f"Cleaned comments across {cleaned} files.")

