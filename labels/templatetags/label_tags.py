from django import template

register = template.Library()

@register.filter
def get_label(obj):
    """Returns the label for an object if it exists."""
    return getattr(obj, 'label', None)