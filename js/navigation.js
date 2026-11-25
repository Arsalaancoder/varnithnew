/**
 * VARNITH GLOBAL - UNIFIED NAVIGATION SCRIPT
 * Manages sticky navbar, desktop dropdowns (hover & click-toggle),
 * outside-click dismissal, mobile nav drawer and accordion submenus.
 */

document.addEventListener('DOMContentLoaded', () => {
    // --- ELEMENT SELECTORS ---
    const hamburger = document.querySelector('.hamburger');
    const mobileNavDrawer = document.querySelector('.mobile-nav-drawer');
    const mobileNavOverlay = document.querySelector('.mobile-nav-overlay');
    const headerNav = document.querySelector('.header-nav');
    const backToTop = document.querySelector('.back-to-top');
    const dropdownNavItems = document.querySelectorAll('.nav-item.has-dropdown');
    const mobileDropdownToggles = document.querySelectorAll('.mobile-dropdown-toggle');

    // --- 1. STICKY NAVBAR & BACK-TO-TOP ---
    const handleScroll = () => {
        const scrollTop = window.scrollY || document.documentElement.scrollTop;
        
        if (headerNav) {
            if (scrollTop > 40) {
                headerNav.classList.add('scrolled');
            } else {
                headerNav.classList.remove('scrolled');
            }
        }

        if (backToTop) {
            if (scrollTop > 400) {
                backToTop.classList.add('visible');
            } else {
                backToTop.classList.remove('visible');
            }
        }
    };

    window.addEventListener('scroll', handleScroll, { passive: true });
    handleScroll();

    // --- 2. DESKTOP SERVICES DROPDOWN (CLICK & HOVER TOGGLE) ---
    dropdownNavItems.forEach(item => {
        const toggleBtn = item.querySelector('.dropdown-toggle');
        const dropdownMenu = item.querySelector('.dropdown-menu');
        if (!toggleBtn || !dropdownMenu) return;

        // Click toggle for desktop & touch
        toggleBtn.addEventListener('click', (e) => {
            e.preventDefault();
            e.stopPropagation();

            const isCurrentlyOpen = item.classList.contains('dropdown-open');

            // Close any other open dropdowns
            dropdownNavItems.forEach(other => {
                other.classList.remove('dropdown-open');
                const otherBtn = other.querySelector('.dropdown-toggle');
                if (otherBtn) otherBtn.setAttribute('aria-expanded', 'false');
            });

            if (!isCurrentlyOpen) {
                item.classList.add('dropdown-open');
                toggleBtn.setAttribute('aria-expanded', 'true');
            } else {
                item.classList.remove('dropdown-open');
                toggleBtn.setAttribute('aria-expanded', 'false');
            }
        });

        // Hover support for mouse users on desktop
        item.addEventListener('mouseenter', () => {
            if (window.innerWidth >= 1024) {
                item.classList.add('dropdown-open');
                toggleBtn.setAttribute('aria-expanded', 'true');
            }
        });

        item.addEventListener('mouseleave', () => {
            if (window.innerWidth >= 1024) {
                item.classList.remove('dropdown-open');
                toggleBtn.setAttribute('aria-expanded', 'false');
            }
        });

        // Close dropdown when any item inside is clicked
        dropdownMenu.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', () => {
                item.classList.remove('dropdown-open');
                toggleBtn.setAttribute('aria-expanded', 'false');
            });
        });

        // Keyboard accessibility
        toggleBtn.addEventListener('keydown', (e) => {
            if (e.key === 'Enter' || e.key === ' ' || e.key === 'ArrowDown') {
                e.preventDefault();
                item.classList.add('dropdown-open');
                toggleBtn.setAttribute('aria-expanded', 'true');
                const firstLink = dropdownMenu.querySelector('a');
                if (firstLink) firstLink.focus();
            }
        });
    });

    // Close desktop dropdown on outside click
    document.addEventListener('click', (e) => {
        if (!e.target.closest('.nav-item.has-dropdown')) {
            dropdownNavItems.forEach(item => {
                item.classList.remove('dropdown-open');
                const toggleBtn = item.querySelector('.dropdown-toggle');
                if (toggleBtn) toggleBtn.setAttribute('aria-expanded', 'false');
            });
        }
    });

    // Close desktop dropdown on Escape key
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') {
            dropdownNavItems.forEach(item => {
                item.classList.remove('dropdown-open');
                const toggleBtn = item.querySelector('.dropdown-toggle');
                if (toggleBtn) toggleBtn.setAttribute('aria-expanded', 'false');
            });
        }
    });

    // --- 3. MOBILE NAV DRAWER OPEN / CLOSE ---
    const openMobileNav = () => {
        if (!hamburger || !mobileNavDrawer || !mobileNavOverlay) return;
        hamburger.classList.add('open');
        hamburger.setAttribute('aria-expanded', 'true');
        mobileNavDrawer.classList.add('open');
        mobileNavOverlay.classList.add('open');
        document.body.style.overflow = 'hidden';
    };

    const closeMobileNav = () => {
        if (!hamburger || !mobileNavDrawer || !mobileNavOverlay) return;
        hamburger.classList.remove('open');
        hamburger.setAttribute('aria-expanded', 'false');
        mobileNavDrawer.classList.remove('open');
        mobileNavOverlay.classList.remove('open');
        document.body.style.overflow = '';
    };

    if (hamburger) {
        hamburger.addEventListener('click', () => {
            if (mobileNavDrawer && mobileNavDrawer.classList.contains('open')) {
                closeMobileNav();
            } else {
                openMobileNav();
            }
        });
    }

    if (mobileNavOverlay) {
        mobileNavOverlay.addEventListener('click', closeMobileNav);
    }

    // --- 4. MOBILE SUBMENU ACCORDION ---
    mobileDropdownToggles.forEach(toggleLink => {
        toggleLink.addEventListener('click', (e) => {
            e.preventDefault();
            const parent = toggleLink.parentElement;
            const submenu = parent ? parent.querySelector('.mobile-submenu') : null;
            if (!submenu) return;

            const isOpen = submenu.classList.contains('open');

            // Close other submenus first
            document.querySelectorAll('.mobile-submenu').forEach(sub => {
                sub.classList.remove('open');
                const prevLink = sub.previousElementSibling;
                if (prevLink) {
                    prevLink.setAttribute('aria-expanded', 'false');
                    const icon = prevLink.querySelector('svg');
                    if (icon) icon.style.transform = 'rotate(0deg)';
                }
            });

            if (!isOpen) {
                submenu.classList.add('open');
                toggleLink.setAttribute('aria-expanded', 'true');
                const icon = toggleLink.querySelector('svg');
                if (icon) icon.style.transform = 'rotate(180deg)';
            } else {
                submenu.classList.remove('open');
                toggleLink.setAttribute('aria-expanded', 'false');
                const icon = toggleLink.querySelector('svg');
                if (icon) icon.style.transform = 'rotate(0deg)';
            }
        });
    });

    // Close mobile drawer when any link is clicked
    document.querySelectorAll('.mobile-menu-link:not(.mobile-dropdown-toggle), .mobile-submenu-link, .mobile-cta a').forEach(link => {
        link.addEventListener('click', () => {
            closeMobileNav();
        });
    });

    // --- 5. ACTIVE PAGE NAVIGATION HIGHLIGHTER ---
    const highlightActiveNav = () => {
        const path = window.location.pathname.split('/').pop().replace('.html', '') || 'index';
        const navLinks = document.querySelectorAll('.nav-menu .nav-link, .mobile-menu-link');

        navLinks.forEach(link => {
            const href = link.getAttribute('href');
            if (!href) return;
            const cleanHref = href.split('/').pop().replace('.html', '');

            if (cleanHref === path || (path === 'index' && (cleanHref === '' || cleanHref === 'index'))) {
                link.classList.add('active');
            }
        });
    };

    highlightActiveNav();
});
