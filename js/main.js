/* ==========================================================================
   VARNITH GLOBAL - MAIN SCRIPT
   ========================================================================== */

document.addEventListener('DOMContentLoaded', () => {
    // 2. FAQ ACCORDION LOGIC
    const faqItems = document.querySelectorAll('.faq-item');
    faqItems.forEach(item => {
        const trigger = item.querySelector('.faq-question');
        if (!trigger) return;
        
        trigger.addEventListener('click', () => {
            const isOpen = item.classList.contains('active');
            
            // Close other FAQ items for clean look
            document.querySelectorAll('.faq-item').forEach(el => {
                el.classList.remove('active');
                const ans = el.querySelector('.faq-answer');
                if (ans) ans.style.maxHeight = null;
            });
            
            if (!isOpen) {
                item.classList.add('active');
                const answer = item.querySelector('.faq-answer');
                if (answer) answer.style.maxHeight = answer.scrollHeight + 'px';
            }
        });
    });

    // 3. CONTACT FORM PRESELECTION & REAL ASYNC SUBMISSION
    const contactForm = document.getElementById('varnith-contact-form');
    
    if (contactForm) {
        // Pre-select service/solution from URL query parameter (e.g. ?service=software-development)
        const urlParams = new URLSearchParams(window.location.search);
        const serviceParam = urlParams.get('service') || urlParams.get('solution');
        const serviceSelect = document.getElementById('form-service');

        if (serviceParam && serviceSelect) {
            const decodedService = decodeURIComponent(serviceParam).toLowerCase().replace(/[-_]/g, ' ');
            for (let i = 0; i < serviceSelect.options.length; i++) {
                const optValue = serviceSelect.options[i].value.toLowerCase().replace(/[-_]/g, ' ');
                const optText = serviceSelect.options[i].text.toLowerCase();
                if (optValue.includes(decodedService) || optText.includes(decodedService) || decodedService.includes(optValue)) {
                    serviceSelect.selectedIndex = i;
                    break;
                }
            }
        }

        contactForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            
            // Retrieve field elements
            const nameEl = document.getElementById('form-name');
            const emailEl = document.getElementById('form-email');
            const phoneEl = document.getElementById('form-phone');
            const companyEl = document.getElementById('form-company');
            const serviceEl = document.getElementById('form-service');
            const messageEl = document.getElementById('form-message');
            const privacyEl = document.getElementById('form-privacy');
            const honeypotEl = document.getElementById('form-website');

            const name = nameEl ? nameEl.value.trim() : '';
            const email = emailEl ? emailEl.value.trim() : '';
            const phone = phoneEl ? phoneEl.value.trim() : '';
            const company = companyEl ? companyEl.value.trim() : '';
            const service = serviceEl ? serviceEl.value : '';
            const message = messageEl ? messageEl.value.trim() : '';
            const privacyChecked = privacyEl ? privacyEl.checked : false;
            const website = honeypotEl ? honeypotEl.value.trim() : '';

            // Clean previous alerts
            document.querySelectorAll('.form-group .error-msg, .form-banner-error').forEach(el => el.remove());
            document.querySelectorAll('.form-group input, .form-group select, .form-group textarea').forEach(el => {
                el.classList.remove('error-field');
            });

            let isValid = true;

            const showError = (fieldId, msg) => {
                isValid = false;
                const field = document.getElementById(fieldId);
                if (field) {
                    field.classList.add('error-field');
                    const parent = field.closest('.form-group') || field.parentElement;
                    
                    const errEl = document.createElement('span');
                    errEl.className = 'error-msg';
                    errEl.setAttribute('role', 'alert');
                    errEl.style.color = '#e53e3e';
                    errEl.style.fontSize = '0.8rem';
                    errEl.style.marginTop = '0.35rem';
                    errEl.style.display = 'block';
                    errEl.innerText = msg;
                    
                    parent.appendChild(errEl);
                }
            };

            // Client Validation Checks
            if (!name) {
                showError('form-name', 'Full Name is required');
            }
            
            if (!email) {
                showError('form-email', 'Email is required');
            } else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
                showError('form-email', 'Please enter a valid email address');
            }
            
            if (!phone) {
                showError('form-phone', 'Phone Number is required');
            } else if (!/^[0-9+\s-]{8,18}$/.test(phone.replace(/\s+/g, ''))) {
                showError('form-phone', 'Please enter a valid phone number');
            }

            if (!message) {
                showError('form-message', 'Message / Requirements details are required');
            } else if (message.length < 10) {
                showError('form-message', 'Please enter at least 10 characters detailing your requirements.');
            }
            
            if (!privacyChecked) {
                showError('form-privacy', 'You must accept the Privacy Policy to submit your request.');
            }
            
            if (!isValid) return;

            // Submit loading state
            const submitBtn = contactForm.querySelector('button[type="submit"]');
            const origText = submitBtn ? submitBtn.innerHTML : 'Submit Inquiry';
            if (submitBtn) {
                submitBtn.disabled = true;
                submitBtn.innerHTML = 'Processing Inquiry... <svg class="animate-spin" width="16" height="16" viewBox="0 0 24 24" fill="none" style="animation: spin 1s linear infinite; vertical-align: middle; margin-left: 6px;"><circle cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4" stroke-linecap="round" stroke-dasharray="31.4 31.4" fill="none"></circle></svg>';
            }

            try {
                const response = await fetch('/api/contact', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({
                        name,
                        email,
                        phone,
                        company,
                        service,
                        message,
                        consent: privacyChecked,
                        website
                    })
                });

                const result = await response.json();

                if (response.ok && result.success) {
                    // Track successful form submission in GA4 (No PII)
                    if (typeof window.trackEvent === 'function') {
                        window.trackEvent('contact_form_submit_success', { service });
                    }

                    // Display success modal
                    const successModal = document.createElement('div');
                    successModal.className = 'success-modal';
                    successModal.setAttribute('role', 'dialog');
                    successModal.setAttribute('aria-modal', 'true');
                    successModal.style.position = 'fixed';
                    successModal.style.inset = '0';
                    successModal.style.backgroundColor = 'rgba(3, 36, 34, 0.9)';
                    successModal.style.display = 'flex';
                    successModal.style.alignItems = 'center';
                    successModal.style.justifyContent = 'center';
                    successModal.style.zIndex = '1100';
                    successModal.style.opacity = '0';
                    successModal.style.transition = 'opacity 0.4s ease';
                    
                    successModal.innerHTML = `
                        <div class="success-card" style="background-color: var(--color-white); border-radius: var(--radius-md); padding: 3rem; max-width: 500px; width: 90%; text-align: center; box-shadow: var(--shadow-lg);">
                            <div style="width: 72px; height: 72px; background-color: var(--color-accent); border-radius: var(--radius-full); display: flex; align-items: center; justify-content: center; margin: 0 auto 1.5rem;">
                                <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="var(--color-primary-dark)" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>
                            </div>
                            <h3 style="margin-bottom: 1rem; font-size: 1.5rem; color: var(--color-primary-dark);">Inquiry Received!</h3>
                            <p style="color: var(--color-muted); margin-bottom: 2rem; line-height: 1.6;">${result.message || 'Thank you for contacting Varnith Global. Our team will review your requirements and reach out to you shortly.'}</p>
                            <button id="close-success-btn" class="btn btn-dark" style="width: 100%;">Return to Website</button>
                        </div>
                    `;
                    
                    document.body.appendChild(successModal);
                    
                    setTimeout(() => {
                        successModal.style.opacity = '1';
                    }, 50);
                    
                    // Reset form fields after successful submission
                    contactForm.reset();
                    
                    document.getElementById('close-success-btn').addEventListener('click', () => {
                        successModal.style.opacity = '0';
                        setTimeout(() => successModal.remove(), 400);
                    });
                } else {
                    throw new Error(result.error || 'Server rejected submission.');
                }
            } catch (err) {
                console.error('Contact form submission error:', err);
                
                if (typeof window.trackEvent === 'function') {
                    window.trackEvent('contact_form_submit_error', { error: err.message });
                }

                // Show accessible inline error banner without clearing form inputs
                const banner = document.createElement('div');
                banner.className = 'form-banner-error';
                banner.setAttribute('role', 'alert');
                banner.style.backgroundColor = '#fff5f5';
                banner.style.border = '1px solid #feb2b2';
                banner.style.color = '#c53030';
                banner.style.padding = '1rem';
                banner.style.borderRadius = 'var(--radius-sm)';
                banner.style.marginBottom = '1.5rem';
                banner.style.fontSize = '0.9rem';
                banner.innerText = err.message || 'Unable to submit inquiry at this moment. Please try again or email us directly at info@varnithglobal.com.';
                
                contactForm.prepend(banner);
            } finally {
                if (submitBtn) {
                    submitBtn.disabled = false;
                    submitBtn.innerHTML = origText;
                }
            }
        });
    }

    // 4. CTA CLICK GA4 TRACKING
    document.querySelectorAll('.btn-primary, .btn-secondary, .nav-cta a').forEach(btn => {
        btn.addEventListener('click', () => {
            if (typeof window.trackEvent === 'function') {
                const label = btn.innerText.trim();
                window.trackEvent('cta_click', { cta_label: label });
            }
        });
    });

    // 5. Inject CSS helper for spin animation and error fields
    const spinStyle = document.createElement('style');
    spinStyle.innerHTML = `
        @keyframes spin { 100% { transform: rotate(360deg); } }
        .error-field { border-color: #e53e3e !important; background-color: rgba(229, 62, 62, 0.03) !important; }
        :focus-visible { outline: 2px solid var(--color-primary, #009688) !important; outline-offset: 2px !important; }
    `;
    document.head.appendChild(spinStyle);
});
