/**
 * VARNITH GLOBAL - ZERO-DEPENDENCY LOCAL WEB SERVER
 * Runs on pure Node.js (no npm install required).
 * Supports clean URLs, proper MIME types, and dual port listening (3000 & 8080).
 */

const http = require('http');
const fs = require('fs');
const path = require('path');
const { exec } = require('child_process');

const PORT_PRIMARY = process.env.PORT || 3000;
const PORT_SECONDARY = 8080;
const ROOT_DIR = __dirname;

const MIME_TYPES = {
    '.html': 'text/html; charset=utf-8',
    '.css': 'text/css; charset=utf-8',
    '.js': 'application/javascript; charset=utf-8',
    '.json': 'application/json; charset=utf-8',
    '.png': 'image/png',
    '.jpg': 'image/jpeg',
    '.jpeg': 'image/jpeg',
    '.gif': 'image/gif',
    '.webp': 'image/webp',
    '.svg': 'image/svg+xml',
    '.ico': 'image/x-icon',
    '.woff': 'font/woff',
    '.woff2': 'font/woff2',
    '.ttf': 'font/ttf',
    '.xml': 'application/xml',
    '.txt': 'text/plain'
};

const REDIRECTS = {
    '/solutions': '/services.html',
    '/solutions.html': '/services.html',
    '/industries': '/services.html',
    '/industries.html': '/services.html',
    '/training': '/courses.html',
    '/training.html': '/courses.html',
    '/services': '/services.html',
    '/services/hr-consulting': '/services.html',
    '/courses': '/courses.html',
    '/about': '/about.html',
    '/contact': '/contact.html',
    '/ai-solutions.html': '/it-services.html'
};

function requestHandler(req, res) {
    // Enable CORS and cache headers
    res.setHeader('Access-Control-Allow-Origin', '*');
    res.setHeader('Access-Control-Allow-Methods', 'GET, HEAD, OPTIONS');

    if (req.method === 'OPTIONS') {
        res.writeHead(204);
        res.end();
        return;
    }

    const parsedUrl = new URL(req.url, `http://${req.headers.host || 'localhost'}`);
    let pathname = decodeURIComponent(parsedUrl.pathname);

    // Normalize trailing slash
    if (pathname.length > 1 && pathname.endsWith('/')) {
        pathname = pathname.slice(0, -1);
    }

    // Check custom redirects
    if (REDIRECTS[pathname]) {
        res.writeHead(301, { 'Location': REDIRECTS[pathname] });
        res.end();
        return;
    }

    // Default to index.html for root
    if (pathname === '/' || pathname === '') {
        pathname = '/index.html';
    }

    let filePath = path.join(ROOT_DIR, pathname);

    // If no extension, try appending .html (clean URL support) or checking for index.html in directory
    if (!path.extname(filePath)) {
        if (fs.existsSync(filePath + '.html')) {
            filePath = filePath + '.html';
        } else if (fs.existsSync(path.join(filePath, 'index.html'))) {
            filePath = path.join(filePath, 'index.html');
        }
    }

    // Security: Prevent path traversal outside ROOT_DIR
    if (!filePath.startsWith(ROOT_DIR)) {
        res.writeHead(403, { 'Content-Type': 'text/plain' });
        res.end('403 Forbidden');
        return;
    }

    fs.stat(filePath, (err, stats) => {
        if (err || !stats.isFile()) {
            // Serve custom 404 page if exists
            const notFoundPath = path.join(ROOT_DIR, '404.html');
            if (fs.existsSync(notFoundPath)) {
                res.writeHead(404, { 'Content-Type': 'text/html; charset=utf-8' });
                fs.createReadStream(notFoundPath).pipe(res);
            } else {
                res.writeHead(404, { 'Content-Type': 'text/plain' });
                res.end('404 Not Found');
            }
            return;
        }

        const ext = path.extname(filePath).toLowerCase();
        const contentType = MIME_TYPES[ext] || 'application/octet-stream';

        res.writeHead(200, {
            'Content-Type': contentType,
            'Content-Length': stats.size,
            'Cache-Control': 'no-cache'
        });

        fs.createReadStream(filePath).pipe(res);
    });
}

function startServer(port, isPrimary = false) {
    const server = http.createServer(requestHandler);
    server.on('error', (err) => {
        if (err.code === 'EADDRINUSE') {
            console.log(`[Varnith Server] Port ${port} is already in use (skipping duplicate listener).`);
        } else {
            console.error(`[Varnith Server] Error on port ${port}:`, err.message);
        }
    });

    server.listen(port, () => {
        console.log(`[Varnith Global] Server running at http://localhost:${port}/`);
        if (isPrimary && process.env.OPEN_BROWSER) {
            const startCmd = process.platform === 'win32' ? 'start' : (process.platform === 'darwin' ? 'open' : 'xdg-open');
            exec(`${startCmd} http://localhost:${port}/`);
        }
    });
}

// Start on primary port 3000
startServer(PORT_PRIMARY, true);

// Also start on secondary port 8080 (for VS Code default launch configuration)
if (PORT_PRIMARY != PORT_SECONDARY) {
    startServer(PORT_SECONDARY, false);
}

