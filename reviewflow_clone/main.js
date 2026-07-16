document.addEventListener('DOMContentLoaded', () => {
    // ── MOBILE MENU TOGGLE ──
    const hamburger = document.getElementById('hamburger-btn');
    const mobileMenu = document.getElementById('mobile-menu');
    const mobileOverlay = document.getElementById('mobile-overlay');
    const body = document.body;

    function openMobileMenu() {
        hamburger.classList.add('active');
        mobileMenu.classList.add('active');
        mobileOverlay.classList.add('active');
        body.style.overflow = 'hidden';
    }

    function closeMobileMenu() {
        hamburger.classList.remove('active');
        mobileMenu.classList.remove('active');
        mobileOverlay.classList.remove('active');
        body.style.overflow = '';
    }

    if(hamburger) {
        hamburger.addEventListener('click', function() {
            hamburger.classList.contains('active') ? closeMobileMenu() : openMobileMenu();
        });
    }

    if(mobileOverlay) {
        mobileOverlay.addEventListener('click', closeMobileMenu);
    }

    // Close menu on pressing escape
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape' && mobileMenu.classList.contains('active')) {
            closeMobileMenu();
        }
    });

    // Close menu when a link inside mobile menu is clicked
    const mobileLinks = document.querySelectorAll('.mobile-nav-links a, .mobile-cta a');
    mobileLinks.forEach(link => {
        link.addEventListener('click', closeMobileMenu);
    });

    // ── HEADER SCROLL EFFECT ──
    const header = document.getElementById('site-header');
    
    function handleScroll() {
        if (window.scrollY > 50) {
            header.classList.add('scrolled');
        } else {
            header.classList.remove('scrolled');
        }
    }

    window.addEventListener('scroll', handleScroll);
    handleScroll(); // Init
});
