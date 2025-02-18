document.addEventListener('DOMContentLoaded', () => {

    window.addEventListener('scroll', () => {
        requestAnimationFrame(handleScroll);
    });

    window.addEventListener('load', () => {
        handleScroll();
        handleNavBackground();
    });

    window.addEventListener('resize', () => {
        handleScroll();
        handleNavBackground();
    });

    ///////////////////////////////////////////////////////////////////
    // Parallax Header Content

    const header = document.querySelector('header');
    const headerContent = document.querySelector('#header-content');
    let windowHeight = window.innerHeight;
    
    function handleScroll() {

        const scroll = window.scrollY;
        const isVisible = scroll < windowHeight;

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
    const dropdownContent = nav.querySelectorAll('.dropdown-content > li');
    
    // Disable tabindex
    const dropdownContentLinks = nav.querySelectorAll("#nav-desktop .dropdown-content a");
    dropdownContentLinks.forEach(link => {
        link.setAttribute('tabindex', '-1');
    });

    function activateDropdown(trigger) {

        deactivateDropdowns();
    
        const currentDropdown = trigger.closest('[data-dropdown]');
        currentDropdown.classList.add('active');

        // Enable tabindex
        currentDropdown.querySelectorAll('#nav-desktop .dropdown-content a').forEach(link => {
            link.setAttribute('tabindex', link.getAttribute('tabindex') === '-1' ? '0' : '-1');
        });
        
    }
    
    function deactivateDropdowns() {

        dropdowns.forEach(dropdown => {
            dropdown.classList.remove('active');

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
    // Handle Nav Background

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

        let translationValue = navHeight;

        if (activeDropdown) {
            const dropdownContent = activeDropdown.querySelector('.dropdown-content');
            translationValue = dropdownContent.getBoundingClientRect().bottom;
        }

        if (!pageTop || nav.matches(':hover')) {
            navBackground.style.transform = `translateY(${translationValue}px)`;                
        } else {
            navBackground.style.transform = 'translateY(0)';
        }

    }

    nav.addEventListener('mouseenter', updateTranslationValue);
    nav.addEventListener('mouseleave', updateTranslationValue);

});