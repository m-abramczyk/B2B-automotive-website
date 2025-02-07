document.addEventListener('DOMContentLoaded', () => {

    window.addEventListener('scroll', () => {
        requestAnimationFrame(handleScroll);
    });

    window.addEventListener('load', () => {
        handleScroll();
    });

    window.addEventListener('resize', () => {
        handleScroll();
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

});