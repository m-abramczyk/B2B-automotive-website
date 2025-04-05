from modeltranslation.translator import register, TranslationOptions
from .models import CaseStudy, CaseStudyData, Section, SectionImage

@register(CaseStudy)
class CaseStudyTranslationOptions(TranslationOptions):
    fields = (
        'menu_title',
        'header',
        'labels_header',
        'text',
        'meta_title',
        'meta_description',
    )

@register(CaseStudyData)
class CaseStudyDataTranslationOptions(TranslationOptions):
    fields = (
        'data_type',
        'data_content',
    )

@register(Section)
class SectionTranslationOptions(TranslationOptions):
    fields = (
        'header',
        'text',
    )

@register(SectionImage)
class SectionImageTranslationOptions(TranslationOptions):
    fields = (
        'caption',
    )