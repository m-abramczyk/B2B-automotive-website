from modeltranslation.translator import register, TranslationOptions
from .models import Expert

@register(Expert)
class ExpertTranslationOptions(TranslationOptions):
    fields = (
        'role',
        'header',
        'button_text',
    )