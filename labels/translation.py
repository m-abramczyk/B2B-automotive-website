from modeltranslation.translator import register, TranslationOptions
from .models import Label

@register(Label)
class LabelTranslationOptions(TranslationOptions):
    fields = ('label_text',)