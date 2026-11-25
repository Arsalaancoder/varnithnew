/* ==========================================================================
   VARNITH GLOBAL - SITE CONFIGURATION & SINGLE SOURCE OF TRUTH
   ========================================================================== */

const SITE_CONFIG = {
    // Legal & Branding Information
    LEGAL_NAME: "Varnith Global",
    SHORT_NAME: "Varnith Global",
    BRAND_TAGLINE: "HR Consulting, Talent Solutions, Training & Development and Technology Transformation.",

    // Domain & Environment Config
    SITE_URL: "https://varnithglobal.com",
    PRODUCTION_DOMAIN: "https://varnithglobal.com",

    // Contact Information (Single Source of Truth)
    ADDRESS: "4-36, 1st Floor, Vikash Nagar, Dilshuknagar, Hyderabad, Telangana 500060",
    ADDRESS_STREET: "4-36, 1st Floor, Vikash Nagar, Dilshuknagar",
    ADDRESS_CITY: "Hyderabad",
    ADDRESS_REGION: "Telangana",
    ADDRESS_POSTAL: "500060",
    ADDRESS_COUNTRY: "IN",

    PHONE_DISPLAY: "+91 9391816116",
    PHONE_RAW: "9391816116",
    PHONE_TEL: "tel:+919391816116",

    EMAIL_DISPLAY: "info@varnithglobal.com",
    EMAIL_MAILTO: "mailto:info@varnithglobal.com",

    BUSINESS_HOURS: "Monday – Saturday: 9:00 AM – 6:30 PM IST",

    // External Services & Social Links
    GOOGLE_MAPS_EMBED: "https://www.google.com/maps?q=Vikash+Nagar,+Dilsukhnagar,+Hyderabad,+Telangana+500060&output=embed",
    GOOGLE_MAPS_DIRECT: "https://maps.google.com/?q=Vikash+Nagar,+Dilsukhnagar,+Hyderabad,+Telangana+500060",

    LINKEDIN_URL: "https://www.linkedin.com/company/varnith-global",
    WHATSAPP_NUMBER: "919391816116",
    WHATSAPP_DEFAULT_MESSAGE: "Hello Varnith Global, I would like to inquire about your services.",

    // Google Analytics 4 Config
    GA_MEASUREMENT_ID: (typeof window !== 'undefined' && window.GA_MEASUREMENT_ID) ? window.GA_MEASUREMENT_ID : ""
};

if (typeof module !== 'undefined' && module.exports) {
    module.exports = SITE_CONFIG;
}
