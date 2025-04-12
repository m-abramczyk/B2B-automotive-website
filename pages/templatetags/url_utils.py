from django import template
from django.utils.translation import get_language
from urllib.parse import urlparse

register = template.Library()

@register.filter
def i18n_url(url):
    if not url:
        return "#"
    
    # Leave external URLs or anchor links untouched
    parsed = urlparse(url)
    if parsed.scheme or parsed.netloc or url.startswith("#"):
        return url

    # Prevent double prefixing
    lang = get_language()
    if url.startswith(f'/{lang}/'):
        return url

    # Apply prefix to internal relative URLs
    return f'/{lang}{url}' if url.startswith('/') else f'/{lang}/{url}'