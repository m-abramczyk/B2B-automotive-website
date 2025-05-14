# B2B automotive website

A multilingual B2B website for an automotive design company, built with Django and a custom frontend.

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [License](#license)

## Overview

G3 is a custom-built B2B marketing website developed for a design firm in the automotive sector. It supports English, German, and Polish, and offers a modular CMS allowing non-technical staff to manage dynamic content without developer input.

## Features

- Custom Django CMS with modular content blocks catering to flexible page layout
- Multilingual support (EN, DE, PL) using django internationalization framework and `django-modeltranslation`
- CMS page duplication based on `django-clone` and supplementary placeholder image logic
- Custom frontend components (carousels, modals, parallax, image comparison wipers)
- Responsive design built from Figma using CSS `clamp()` and grid systems
- Dockerized deployment on Ubuntu VPS
- Image cleanup automation (via `django-cleanup`)

## Tech Stack

- **Backend**: Python, Django, Django CMS, django-modeltranslation
- **Frontend**: HTML5, CSS3, JavaScript (ES6), no dependencies
- **Admin UI**: django-nested-admin, TinyMCE, django-clone
- **DevOps**: Docker, Nginx, Gunicorn, Ubuntu VPS

## License

This project is for demonstration purposes only. All rights reserved.
