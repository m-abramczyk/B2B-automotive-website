from modeltranslation.translator import register, TranslationOptions
from .models import Clients, Founders, FounderInfo, Specialists, SpecialistInfo, Timeline, TimelineImage

@register(Clients)
class ClientsTranslationOptions(TranslationOptions):
    fields = (
        'header',
        'button_clients_text',
    )

@register(Founders)
class FoundersTranslationOptions(TranslationOptions):
    fields = (
        'header',
    )

@register(FounderInfo)
class FounderInfoTranslationOptions(TranslationOptions):
    fields = (
        'role',
    )

@register(Specialists)
class SpecialistsTranslationOptions(TranslationOptions):
    fields = (
        'header',
    )

@register(SpecialistInfo)
class SpecialistInfoTranslationOptions(TranslationOptions):
    fields = (
        'role',
    )

@register(Timeline)
class TimelineTranslationOptions(TranslationOptions):
    fields = (
        'header',
    )

@register(TimelineImage)
class TimelineImageTranslationOptions(TranslationOptions):
    fields = (
        'caption',
        'long_caption',
        'year',
    )