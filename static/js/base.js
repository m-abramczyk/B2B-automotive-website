document.addEventListener('DOMContentLoaded', () => {

    window.addEventListener('scroll', () => {
        if (!ticking) {
            requestAnimationFrame(handleScroll);
            ticking = true;
        }
    });

    window.addEventListener('load', () => {
        handleScroll();
        handleNavBackground();
        setDropdownTabindex();
    });

    window.addEventListener('resize', () => {
        handleScroll();
        updateTranslationValue();
        closeNavMobileResize();
        closeAllDropdowns();
        setDropdownTabindex();        
    });

    ///////////////////////////////////////////////////////////////////
    // Parallax Header
    // Nav Scroll Behavior

    const header = document.querySelector('header');
    const headerContent = document.querySelector('#header-content');
    let windowHeight = window.innerHeight;

    let lastScrollY = window.scrollY;
    let lastTimestamp = performance.now();
    let ticking = false;
    const SCROLL_THRESHOLD = 1.75;
    const NAV_HIDE_CLASS = "hidden";
    
    function handleScroll() {

        const scroll = window.scrollY;
        const isVisible = scroll < windowHeight;

        // Nav Scroll Behavior
        const deltaY = scroll - lastScrollY;
        const timestamp = performance.now();
        const timeDiff = timestamp - lastTimestamp;
        const activeDropdown = document.querySelector('#nav-desktop .dropdown.active');
        
        lastTimestamp = timestamp;

        if (pageTop) {
            nav.classList.remove(NAV_HIDE_CLASS);
        } else if (!activeDropdown) {
            if (Math.abs(deltaY) / timeDiff > SCROLL_THRESHOLD) {
                if (deltaY > 0) {
                    nav.classList.add(NAV_HIDE_CLASS);
                } else {
                    nav.classList.remove(NAV_HIDE_CLASS);
                }
            }
        }

        lastScrollY = scroll;
        ticking = false;

        // Parallax Header
        if (!headerContent) {return;}
        if (!isVisible) {return;}

        const contentRect = headerContent.getBoundingClientRect();
        const headerBottom = header.offsetTop + header.offsetHeight;
        const contentBottom = headerContent.offsetTop + headerContent.offsetHeight;

        if (contentRect.top <= 0) {

            const rate = Math.min((scroll - headerContent.offsetTop) * 0.33, headerBottom - contentBottom).toFixed(0);
            headerContent.style.transform = `translateY(${rate}px)`;

        } else {
            // reset position if scrolled back up to prevent uncaught residual pixels translation
            headerContent.style.transform = `translateY(0)`;
        }
    }

    ///////////////////////////////////////////////////////////////////
    // Nav Dropdown Content

    const nav = document.querySelector('nav');
    const dropdowns = nav.querySelectorAll('[data-dropdown]');
    const dropdownTriggers = nav.querySelectorAll('[data-dropdown-trigger]');
    const dropdownCloseTriggers = nav.querySelectorAll('[data-dropdown-close-trigger]');
    const blurredContent = document.querySelectorAll('body > *:not(nav)');
    
    // Disable tabindex
    const dropdownContentLinks = nav.querySelectorAll("#nav-desktop .dropdown-content a");
    dropdownContentLinks.forEach(link => {
        link.setAttribute('tabindex', '-1');
    });

    function activateDropdown(trigger) {

        deactivateDropdowns();
    
        const currentDropdown = trigger.closest('[data-dropdown]');
        currentDropdown.classList.add('active');
        blurContentOn();

        // Enable tabindex
        currentDropdown.querySelectorAll('#nav-desktop .dropdown-content a').forEach(link => {
            link.setAttribute('tabindex', link.getAttribute('tabindex') === '-1' ? '0' : '-1');
        });
        
    }
    
    function deactivateDropdowns() {

        dropdowns.forEach(dropdown => {
            dropdown.classList.remove('active');
            blurContentOff();

            // Reset Tabindex
            dropdown.querySelectorAll('#nav-desktop .dropdown-content a').forEach(link => link.setAttribute('tabindex', '-1'));
        });
    }
    
    // Handle dropdown activation
    dropdownTriggers.forEach(trigger => {
        trigger.addEventListener('mouseenter', () => {
            activateDropdown(trigger);
            updateTranslationValue();
        });
    });
    
    // Close dropdowns when leaving nav
    nav.addEventListener('mouseleave', () => {
        deactivateDropdowns();
        updateTranslationValue();
    });
    
    // Close dropdowns when hovering a non-dropdown link
    dropdownCloseTriggers.forEach(closeTrigger => {
        closeTrigger.addEventListener('mouseenter', () => {
            deactivateDropdowns();
            updateTranslationValue();
        });
    });

    ///////////////////////////////////////////////////////////////////
    // Nav mobile toggle

    const navMobileToggle = document.getElementById('hamb');
    const animationToggle = document.querySelector("#hamb > svg");
    const navMobile = document.getElementById('nav-mobile');
    const content = document.querySelector('body');
    let currentScroll;
    let isAnimating = false;

    const navMobileLinks = navMobile.querySelectorAll('a');
    navMobileLinks.forEach(link => {
        link.setAttribute('tabindex', '-1');
    });

    navMobileToggle.addEventListener('click', () => {

        if (isAnimating) {return;}
        else {isAnimating = true;}

        animateHamb();

        if (!navMobile.classList.contains('nav-active')) {
            startNavMobile();
        } else {
            closeNavMobile();
        }
    });

    function startNavMobile() {

        currentScroll = window.scrollY;
        navMobile.classList.add('nav-active');
        animationToggle.classList.add('nav-active');

        updateTranslationValue();
        blurContentOn();

        setTimeout(() => {
            content.classList.add('nav-active');
            navMobileLinks.forEach(link => {
                link.setAttribute('tabindex', '0');
            });        
        }, 300); // Timeout same as #nav-mobile transition
    }

    function animateHamb() {
        animationToggle.classList.add('animation');
        setTimeout(() => {
            animationToggle.classList.remove('animation');
            isAnimating = false; // new clicks only after animation finished
        }, 300); // Timeout same as #nav-mobile transition
    }

    function closeNavMobile() {

        animationToggle.classList.remove('nav-active');
        navMobile.classList.remove('nav-active');
        content.classList.remove('nav-active');
        window.scrollTo(0, currentScroll);

        updateTranslationValue();
        blurContentOff();

        navMobileLinks.forEach(link => {
            link.setAttribute('tabindex', '-1');
        });
    }

    // Close nav if resizing to desktop
    function closeNavMobileResize() {
        if (window.innerWidth > 1280 && navMobile.classList.contains('nav-active')) {closeNavMobile();}
    }

    // Blur Content utilities
    function blurContentOn() {blurredContent.forEach(object => object.classList.add('dropdown-active'));}
    function blurContentOff() {blurredContent.forEach(object => object.classList.remove('dropdown-active'));}


    ///////////////////////////////////////////////////////////////////
    // Nav Background

    const navBackground = document.querySelector('#nav-background');

    const pageTopObserver = document.createElement('div');
        pageTopObserver.setAttribute('data-page-top-observer', '');
        nav.before(pageTopObserver);

    let pageTop = true;

    function handleNavBackground() {

        const navBackgroundObserver = new IntersectionObserver((entries) => {
            pageTop = entries[0].isIntersecting;

            updateTranslationValue();
            
        }, {rootMargin: `20% 0px 0px 0px`,});
        navBackgroundObserver.observe(pageTopObserver);
    }

    function updateTranslationValue() {

        const navHeight = nav.offsetHeight;
        const activeDropdown = document.querySelector('#nav-desktop .dropdown.active');

        if (pageTop && !activeDropdown && (!nav.matches(':hover') || window.innerWidth < 1280) && !navMobile.classList.contains('nav-active')) {
            
            navBackground.style.transform = `translateY(0)`;

        } else {

            if (activeDropdown) {
                const dropdownContent = activeDropdown.querySelector('.dropdown-content');
                translationValue = dropdownContent.getBoundingClientRect().bottom;
            } else {translationValue = navHeight;}

            navBackground.style.transform = `translateY(${translationValue}px)`;
        }

    }

    nav.addEventListener('mouseenter', updateTranslationValue);
    nav.addEventListener('mouseleave', updateTranslationValue);


    ///////////////////////////////////////////////////////////////////
    // Footer Dropdown Content

    const dropdownButton = document.querySelectorAll("[data-footer-dropdown-button]");
    dropdownButton.forEach(button => {    
        button.addEventListener('click', e => {

            let currentDropdown;

            currentDropdown = e.target.closest('[data-footer-dropdown]');
            const dropdownContent = currentDropdown.querySelector('.footer-dropdown-content');

            if (currentDropdown.classList.contains('active')) {
                // Set dropdown height to 0 before collapsing
                dropdownContent.style.maxHeight = "0";
            } else {
                // Set dropdown height on opening
                dropdownContent.style.maxHeight = dropdownContent.scrollHeight + "px";
            }

            currentDropdown.classList.toggle('active');

            // Toggle tabindex
            currentDropdown.querySelectorAll('.footer-dropdown-content a').forEach(link => {
                link.setAttribute('tabindex', link.getAttribute('tabindex') === '-1' ? '0' : '-1');
            });

        });
    });

    // Set tabindex -1 (mobile) or 0 (desktop) on load / rsize
    const footerDropdownLinks = document.querySelectorAll(".footer-dropdown-content a");
    function setDropdownTabindex() {
                
        footerDropdownLinks.forEach(link => {
            if (window.innerWidth < 1280) {
                link.setAttribute('tabindex', '-1');
            } else {
                link.setAttribute('tabindex', '0');
            }
        });
    }

    // Close all footer dropdowns if resizing between mobile and desktop
    function closeAllDropdowns() {

        if (window.innerWidth > 1280) {
            document.querySelectorAll("[data-footer-dropdown].active").forEach(dropdown => {
                dropdown.classList.remove('active');
                dropdown.querySelector('.footer-dropdown-content').style.maxHeight = "0";
            });
        }
    }

});