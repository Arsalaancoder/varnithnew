/* ==========================================================================
   VARNITH GLOBAL - GA4 ANALYTICS MODULE
   ========================================================================== */

(function() {
    'use strict';

    const getGAId = () => {
        if (window.GA_MEASUREMENT_ID) return window.GA_MEASUREMENT_ID;
        if (typeof SITE_CONFIG !== 'undefined' && SITE_CONFIG.GA_MEASUREMENT_ID) return SITE_CONFIG.GA_MEASUREMENT_ID;
        return null;
    };

    const initGA4 = () => {
        const gaId = getGAId();
        if (!gaId || gaId.trim() === '' || gaId === 'G-XXXXXXXXXX') {
            return;
        }

        // Dynamically load Google Analytics Script
        const script = document.createElement('script');
        script.async = true;
        script.src = `https://www.googletagmanager.com/gtag/js?id=${encodeURIComponent(gaId)}`;
        document.head.appendChild(script);

        window.dataLayer = window.dataLayer || [];
        function gtag() { window.dataLayer.push(arguments); }
        window.gtag = gtag;

        gtag('js', new Date());
        gtag('config', gaId, {
            send_page_view: true,
            anonymize_ip: true
        });
    };

    // Public event tracking function (Safe against PII leakage)
    window.trackEvent = function(eventName, params = {}) {
        if (typeof window.gtag === 'function') {
            // Strip potential PII before sending
            const sanitizedParams = { ...params };
            delete sanitizedParams.email;
            delete sanitizedParams.phone;
            delete sanitizedParams.name;
            delete sanitizedParams.message;
            delete sanitizedParams.company;

            window.gtag('event', eventName, sanitizedParams);
        }
    };

    // Auto initialize on DOM ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initGA4);
    } else {
        initGA4();
    }
})();
