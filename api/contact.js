// Vercel Serverless Function for Production Contact Form Handling
// Location: /api/contact.js

const rateLimitMap = new Map();

export default async function handler(req, res) {
    // Enable CORS headers
    res.setHeader('Access-Control-Allow-Credentials', 'true');
    res.setHeader('Access-Control-Allow-Origin', '*');
    res.setHeader('Access-Control-Allow-Methods', 'GET,OPTIONS,POST');
    res.setHeader(
        'Access-Control-Allow-Headers',
        'X-CSRF-Token, X-Requested-With, Accept, Accept-Version, Content-Length, Content-MD5, Content-Type, Date, X-Api-Version'
    );

    if (req.method === 'OPTIONS') {
        return res.status(200).end();
    }

    if (req.method !== 'POST') {
        return res.status(405).json({ success: false, error: 'Method not allowed. Use POST.' });
    }

    try {
        const body = typeof req.body === 'string' ? JSON.parse(req.body) : req.body;
        const { name, email, phone, company, service, message, consent, website } = body || {};

        // 1. Honeypot check (Spam Prevention)
        if (website && website.trim() !== '') {
            // Silently reject bot submissions
            return res.status(200).json({ success: true, message: 'Inquiry processed successfully.' });
        }

        // 2. IP Rate Limiting (Max 5 submissions per 10 minutes per IP)
        const ip = req.headers['x-forwarded-for'] || req.socket.remoteAddress || '127.0.0.1';
        const now = Date.now();
        const windowMs = 10 * 60 * 1000;
        const userRequests = rateLimitMap.get(ip) || [];
        const recentRequests = userRequests.filter(time => now - time < windowMs);

        if (recentRequests.length >= 5) {
            return res.status(429).json({
                success: false,
                error: 'Too many requests. Please wait a few minutes before submitting again.'
            });
        }

        recentRequests.push(now);
        rateLimitMap.set(ip, recentRequests);

        // 3. Server-side Field Validation & Sanitization
        const cleanName = (name || '').trim();
        const cleanEmail = (email || '').trim().toLowerCase();
        const cleanPhone = (phone || '').trim();
        const cleanCompany = (company || '').trim();
        const cleanService = (service || '').trim();
        const cleanMessage = (message || '').trim();

        if (!cleanName || cleanName.length < 2) {
            return res.status(400).json({ success: false, error: 'Please enter a valid full name.' });
        }

        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!cleanEmail || !emailRegex.test(cleanEmail)) {
            return res.status(400).json({ success: false, error: 'Please enter a valid business email address.' });
        }

        if (!cleanPhone || cleanPhone.length < 8) {
            return res.status(400).json({ success: false, error: 'Please enter a valid contact phone number.' });
        }

        if (!cleanMessage || cleanMessage.length < 10) {
            return res.status(400).json({ success: false, error: 'Please provide project details (minimum 10 characters).' });
        }

        if (!consent) {
            return res.status(400).json({ success: false, error: 'You must accept the privacy policy to submit.' });
        }

        // 4. Production Email Dispatching via Configured Provider (if env vars are present)
        const destinationEmail = process.env.CONTACT_DESTINATION_EMAIL || 'info@varnithglobal.com';
        const resendApiKey = process.env.RESEND_API_KEY;
        const sendgridApiKey = process.env.SENDGRID_API_KEY;
        const webhookUrl = process.env.CONTACT_WEBHOOK_URL;

        if (resendApiKey) {
            // Send via Resend API
            await fetch('https://api.resend.com/emails', {
                method: 'POST',
                headers: {
                    'Authorization': `Bearer ${resendApiKey}`,
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    from: 'Varnith Global Inquiry <onboarding@resend.dev>',
                    to: [destinationEmail],
                    subject: `New Website Inquiry from ${cleanName} - ${cleanCompany || 'Direct'}`,
                    html: `
                        <h2>New Inquiry Received from Website</h2>
                        <p><strong>Name:</strong> ${cleanName}</p>
                        <p><strong>Email:</strong> ${cleanEmail}</p>
                        <p><strong>Phone:</strong> ${cleanPhone}</p>
                        <p><strong>Company:</strong> ${cleanCompany || 'N/A'}</p>
                        <p><strong>Service / Solution:</strong> ${cleanService || 'General Inquiry'}</p>
                        <p><strong>Message / Requirements:</strong></p>
                        <blockquote style="background: #f4f4f4; padding: 12px; border-left: 4px solid #009688;">
                            ${cleanMessage.replace(/\n/g, '<br>')}
                        </blockquote>
                    `
                })
            });
        } else if (sendgridApiKey) {
            // Send via SendGrid API
            await fetch('https://api.sendgrid.com/v3/mail/send', {
                method: 'POST',
                headers: {
                    'Authorization': `Bearer ${sendgridApiKey}`,
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    personalizations: [{ to: [{ email: destinationEmail }] }],
                    from: { email: destinationEmail, name: 'Varnith Global' },
                    subject: `New Website Inquiry from ${cleanName}`,
                    content: [{
                        type: 'text/plain',
                        value: `Name: ${cleanName}\nEmail: ${cleanEmail}\nPhone: ${cleanPhone}\nCompany: ${cleanCompany}\nService: ${cleanService}\nMessage: ${cleanMessage}`
                    }]
                })
            });
        } else if (webhookUrl) {
            // Forward to custom webhook
            await fetch(webhookUrl, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    name: cleanName,
                    email: cleanEmail,
                    phone: cleanPhone,
                    company: cleanCompany,
                    service: cleanService,
                    message: cleanMessage,
                    submittedAt: new Date().toISOString()
                })
            });
        }

        // Return successful JSON response
        return res.status(200).json({
            success: true,
            message: 'Thank you for reaching out to Varnith Global. Our team will contact you within 24 business hours.'
        });

    } catch (err) {
        console.error('Error processing contact form:', err);
        return res.status(500).json({
            success: false,
            error: 'An internal error occurred while processing your request. Please try again or contact us directly via email.'
        });
    }
}
