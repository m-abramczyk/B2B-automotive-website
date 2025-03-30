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
    const body = document.querySelector('body'); // used in Lightbox
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
    // current section underline

    const sectionLinks = document.querySelectorAll('#nav-desktop > li > a');

    if (sectionLinks.length > 0) {
        // Get current URL path and normalize it
        let currentPath = window.location.pathname;
        currentPath = currentPath.replace(/^\/[a-z]{2}\//, '/'); // Remove "/en/" or any 2-letter language code and replace with "/"

        sectionLinks.forEach(link => {
            let linkPath = new URL(link.href).pathname;
            linkPath = linkPath.replace(/^\/[a-z]{2}\//, '/'); // Remove "/en/" if present and replace with "/"

            // Check if current path starts with or includes the link path
            if (currentPath === linkPath || currentPath.startsWith(linkPath)) {
                link.classList.add('current-section');
            }
        });
    }

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


    ///////////////////////////////////////////////////////////////////
    // Case Studies Cover Slider

    const coverSlider = document.querySelector('#cs-cover-slider');

    if (coverSlider) {

        const covers = coverSlider.querySelectorAll('.cover');
        const captions = document.querySelectorAll('.cs-slider-caption');
        const coverIndexContainer = document.querySelector('.cover-index-container');
        const arrowLeft = document.querySelector('.cs-slider-arrow-left');
        const arrowRight = document.querySelector('.cs-slider-arrow-right');
        const counterSlash = document.querySelector('.cs-counter-slash');

        let scrollWidth = coverSlider.offsetWidth;
        let currentIndex = 0;

        // click scrolling
        function scrollLeft() {
            if (currentIndex > 0) {
                currentIndex--;
                coverSlider.scrollLeft -= scrollWidth;
            } else {
                // Fake loop: Jump to last cover
                currentIndex = covers.length - 1;
                coverSlider.scrollLeft = scrollWidth * currentIndex;
            }
            updateCounter();
        }

        function scrollRight() {
            if (currentIndex < covers.length - 1) {
                currentIndex++;
                coverSlider.scrollLeft += scrollWidth;
            } else {
                // Fake loop: Jump to first cover
                currentIndex = 0;
                coverSlider.scrollLeft = 0;
            }
            updateCounter();
        }

        arrowLeft.addEventListener('click', scrollLeft);
        arrowRight.addEventListener('click', scrollRight);

        // create cover index elements
        covers.forEach((cover, index) => {
            const coverIndex = document.createElement('span');
            coverIndex.textContent = index + 1;
            coverIndex.classList.add('cs-cover-index');
            coverIndexContainer.insertBefore(coverIndex, counterSlash);
        });

        const coverNumber = document.createElement('span');
        coverNumber.textContent = covers.length;
        coverIndexContainer.insertBefore(coverNumber, arrowRight);

        // update counter
        function updateCounter() {
            const coverIndexElements = coverIndexContainer.querySelectorAll('.cs-cover-index');
            if (covers.length === 0) { return; }

            coverIndexElements.forEach(element => { element.classList.remove('cs-current'); });
            coverIndexElements[currentIndex].classList.add('cs-current');

            captions.forEach(element => { element.classList.remove('cs-current'); });
            captions[currentIndex].classList.add('cs-current');
        }

        window.addEventListener('load', updateCounter);

    }



    ///////////////////////////////////////////////////////////////////
    // Carousel
    
    document.querySelectorAll('.carousel-slider').forEach((slider) => {
        const slides = slider.querySelectorAll('img');
        const blockContainer = slider.parentNode.closest('div'); // Scope within the nearest parent block
    
        if (!blockContainer) return;

        const arrowLeftButton = blockContainer.querySelector('.carousel-arrow-left');
        const arrowRightButton = blockContainer.querySelector('.carousel-arrow-right');
        const slideIndexContainer = blockContainer.querySelector('.slide-index-container');
        const slideCaptionContainer = blockContainer.querySelector('.slide-caption-container');
        const slideLongCaptionContainer = blockContainer.querySelector('.slide-long-caption-container');
        const slideYearContainer = blockContainer.querySelector('.slide-year-container');
    
        let scrollWidth = slider.offsetWidth;
        let currentSlideIndex = 0;
    

        // click scrolling
        function scrollLeft() { slider.scrollLeft -= scrollWidth; }
        function scrollRight() { slider.scrollLeft += scrollWidth; }
    
        arrowLeftButton.addEventListener('click', scrollLeft);
        arrowRightButton.addEventListener('click', scrollRight);
    
        // Observe slide changes
        const observer = new IntersectionObserver(entries => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    currentSlideIndex = Array.from(slides).indexOf(entry.target);
                    updateSlideCounter();
                    hideUnusedArrow();
                }
            });
        }, { threshold: 0.51 }); // slightly over half of slide has to be visible to update slide data, to ensure that snap scrolling triggers
    
        slides.forEach(slide => observer.observe(slide));
    
        slides.forEach((slide, index) => {
            // Create slide index element
            const slideIndexElement = document.createElement('p');
            slideIndexElement.textContent = index + 1;
            slideIndexElement.classList.add('slide-index');
            slideIndexContainer.appendChild(slideIndexElement);
            
            // Create caption element
            const captionElement = document.createElement('p');
            captionElement.textContent = slide.dataset.imageCaption || ''; // Use data attribute for caption
            captionElement.classList.add('slide-caption');
            slideCaptionContainer.appendChild(captionElement);

            if (blockContainer.classList.contains('block-timeline')) {
                // Create Timeline captions
                const yearElement = document.createElement('p');
                yearElement.textContent = slide.dataset.imageYear || '';
                yearElement.classList.add('slide-caption');
                slideYearContainer.appendChild(yearElement);

                const longCaptionElement = document.createElement('p');
                longCaptionElement.textContent = slide.dataset.imageLongCaption || '';
                longCaptionElement.classList.add('slide-caption');
                slideLongCaptionContainer.appendChild(longCaptionElement);
            }
        });
    
        function updateSlideCounter() {

            const slideIndexElements = slideIndexContainer.querySelectorAll('.slide-index');
            const slideCaptionElements = slideCaptionContainer.querySelectorAll('.slide-caption');

            if (slides.length === 0) { return; }

            slideIndexElements.forEach(element => { element.classList.remove('current-slide'); });
            slideIndexElements[currentSlideIndex].classList.add('current-slide');

            slideCaptionElements.forEach(element => { element.classList.remove('current-caption'); });
            slideCaptionElements[currentSlideIndex].classList.add('current-caption');

            if (blockContainer.classList.contains('block-timeline')) {

                const slideLongCaptionElements = slideLongCaptionContainer.querySelectorAll('.slide-caption');
                const slideYearElements = slideYearContainer.querySelectorAll('.slide-caption');

                slideYearElements.forEach(element => { element.classList.remove('current-caption'); });
                slideYearElements[currentSlideIndex].classList.add('current-caption');

                slideLongCaptionElements.forEach(element => { element.classList.remove('current-caption'); });        
                slideLongCaptionElements[currentSlideIndex].classList.add('current-caption'); 
            }
        }
    
        // Gray-out unused arrows
        function hideUnusedArrow() {
            
            if (currentSlideIndex === 0) { arrowLeftButton.classList.add('arrow-hidden'); }
            else { arrowLeftButton.classList.remove('arrow-hidden'); }
            
            if (currentSlideIndex === slides.length - 1) { arrowRightButton.classList.add('arrow-hidden'); }
            else { arrowRightButton.classList.remove('arrow-hidden'); }
        }

        // Set the height of slide caption container to tallest caption
        function adjustCaptionHeight() {

            // If block-timeline, adjust parent container height
            if (blockContainer.classList.contains('block-timeline')) {

                if (window.innerWidth >= 1280) {

                    const slideYearElements = slideYearContainer.querySelectorAll('.slide-caption');
                    const slideCaptionElements = slideCaptionContainer.querySelectorAll('.slide-caption');
                    const slideLongCaptionElements = slideLongCaptionContainer.querySelectorAll('.slide-caption');
                    const captionsContainer = blockContainer.querySelector('.timeline-captions');
                    
                    if (slideYearElements.length === 0 && slideCaptionElements.length === 0 && slideLongCaptionElements.length === 0) return;
            
                    // Temporarily remove class to get natural height
                    slideYearElements.forEach(caption => caption.classList.remove('slide-caption'));
                    slideCaptionElements.forEach(caption => caption.classList.remove('slide-caption'));
                    slideLongCaptionElements.forEach(caption => caption.classList.remove('slide-caption'));
            
                    // Measure tallest caption of each array
                    const maxHeightYear = slideYearElements.length
                        ? Math.max(...Array.from(slideYearElements).map(caption => caption.offsetHeight))
                        : 0;
                    const maxHeightCaption = slideCaptionElements.length
                        ? Math.max(...Array.from(slideCaptionElements).map(caption => caption.offsetHeight))
                        : 0;
                    const maxHeightLongCaption = slideLongCaptionElements.length
                        ? Math.max(...Array.from(slideLongCaptionElements).map(caption => caption.offsetHeight))
                        : 0;
            
                    // Reapply the class after measurement
                    slideYearElements.forEach(caption => caption.classList.add('slide-caption'));
                    slideCaptionElements.forEach(caption => caption.classList.add('slide-caption'));
                    slideLongCaptionElements.forEach(caption => caption.classList.add('slide-caption'));
            
                    // Combine heights and apply to parent container
                    const combinedMaxHeight = maxHeightYear + maxHeightCaption + maxHeightLongCaption;
                    captionsContainer.style.height = `${combinedMaxHeight}px`;
        
                } else {
                
                    // Reset height for smaller screens
                    const captionsContainer = blockContainer.querySelector('.timeline-captions');
                    captionsContainer.style.height = "auto";
                }
                
                return; // Exit block-timeline logic
            }

            // Logic for non-block-timeline
            const slideCaptionElements = slideCaptionContainer.querySelectorAll('.slide-caption');
            if (slideCaptionElements.length === 0) return;
            let maxHeight = 0;
    
            // Temporarily remove class to get natural height
            slideCaptionElements.forEach(caption => caption.classList.remove('slide-caption'));
    
            // Measure tallest caption
            maxHeight = Math.max(
                ...Array.from(slideCaptionElements).map(caption => caption.offsetHeight)
            );
    
            // Reapply the class after measurement
            slideCaptionElements.forEach(caption => caption.classList.add('slide-caption'));
    
            // Apply height to container
            slideCaptionContainer.style.height = `${maxHeight}px`;
            
        }
    
        updateSlideCounter();

        // Called on load and resize
        function updateCarousel() {
            scrollWidth = slider.offsetWidth;
            updateSlideCounter();
            hideUnusedArrow();
            adjustCaptionHeight();
        }

        window.addEventListener('load', updateCarousel);
        window.addEventListener('resize', updateCarousel);

    });


    ///////////////////////////////////////////////////////////////////
    // Lightbox

    // const lightboxTriggers = blockContainer.querySelectorAll('.lightbox-trigger img');
    // const relatedLightbox = blockContainer.querySelector('.lightbox');

    // if (!relatedLightbox) return;

    // const lightboxCloseButton = relatedLightbox.querySelector('.lightbox-close-button');
    // const lightboxSlider = relatedLightbox.querySelector('.carousel-slider');
    // const lightboxSlides = lightboxSlider ? lightboxSlider.querySelectorAll('img') : [];

    // // Click open Lightbox
    // lightboxTriggers.forEach((image, index) => {
    //     image.addEventListener('click', () => {
    //         currentSlideIndex = index;
    //         startLightbox();
    //         updateCarousel(lightboxSlider, currentSlideIndex);
    //     });
    // });

    // // Click close Lightbox
    // lightboxCloseButton.addEventListener('click', e => {
    //     closeLightbox();
    // });

    // // Utilities //////////////////////////////////////////
    // function startLightbox() {
    //     currentScroll = window.scrollY;
    //     relatedLightbox.classList.add('lightbox-active');
    //     nav.classList.add('lightbox-active');
    //     setTimeout(() => {
    //         body.classList.add('lightbox-active');
    //     }, 150); // Timeout same as lightbox css transition
    // }

    // function closeLightbox() {
    //     relatedLightbox.classList.remove('lightbox-active');
    //     body.classList.remove('lightbox-active');
    //     nav.classList.remove('lightbox-active');
    //     window.scrollTo(0, currentScroll);
    // }





    ///////////////////////////////////////////////////////////////////
    // Wiper

    document.querySelectorAll('.image-wiper').forEach((wiper) => {
        const blockContainer = wiper.closest('.block'); // Scope to contentBlock
        const divider = blockContainer.querySelector('.divider');
        const imageLeftContainer = blockContainer.querySelector('.wiper-left');
        const imageLeft = blockContainer.querySelector('.wiper-left > img');

        const container = wiper;
        let barActive = false;
        let currentRatio = 0.5;
        
        // Initialize or reset divider position
        function initializeDivider() {
            const containerWidth = container.offsetWidth;
            const initLeft = containerWidth * currentRatio;

            divider.style.left = `${initLeft}px`;
            imageLeftContainer.style.width = `${initLeft}px`;
            imageLeft.style.minWidth = `${containerWidth}px`;
        }

        // Update divider position based on clientX coordinate
        function moveDivider(clientX) {
            const rect = container.getBoundingClientRect();
            let newLeft = clientX - rect.left;

            // Constrain divider within bounds
            if (newLeft < 1) newLeft = 1;
            if (newLeft > rect.width - 1) newLeft = rect.width - 1;

            // Update divider position and left image container width
            currentRatio = newLeft / rect.width;
            divider.style.left = `${newLeft}px`;
            imageLeftContainer.style.width = `${newLeft}px`;
        }
        
        // Enable dragging when user presses down on the divider
        divider.addEventListener('pointerdown', (e) => {
            barActive = true;
            e.preventDefault();
            divider.setPointerCapture(e.pointerId);
            container.style.cursor = 'ew-resize'; // Change cursor on pointerdown
        });

        // Update wiper during drag
        container.addEventListener('pointermove', (e) => {
            if (barActive) {
                requestAnimationFrame(() => {
                    moveDivider(e.clientX);
                });
            }
        });

        // When pointer is released or canceled, stop dragging
        const endInteraction = (e) => {
            barActive = false;
            container.style.cursor = 'default'; // Reset cursor on release
        };

        container.addEventListener('pointerup', endInteraction);
        container.addEventListener('pointercancel', endInteraction);
        container.addEventListener('pointerleave', endInteraction);

        // Jump-to-click
        container.addEventListener('pointerdown', (e) => {
            // Check if the event target is not the divider
            if (!divider.contains(e.target)) {
                e.preventDefault();
                // Capture pointer events on container so dragging continues even if pointer leaves
                container.setPointerCapture(e.pointerId);
                moveDivider(e.clientX);
                barActive = true;                
                container.style.cursor = 'ew-resize'; // Change cursor on jump-to-click
            }
        });

        initializeDivider();
        window.addEventListener('resize', initializeDivider);
    
    });

});